from __future__ import annotations

import copy
import json
import re
import sys
import unittest
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_ROOT = SKILL_ROOT / "scripts"
FIXTURE_ROOT = Path(__file__).resolve().parent / "fixtures"
sys.path.insert(0, str(SCRIPT_ROOT))
sys.path.insert(0, str(FIXTURE_ROOT))

from contracts import validate_role_dossier  # noqa: E402
from factory import load_persona  # noqa: E402

FIXTURE_PATH = SKILL_ROOT / "evaluations" / "fixtures" / "role_decision_canada.json"
OUTCOME_TO_DECISION = {"pursue": "apply", "do_not_pursue": "skip"}
WORDING_FIELDS = ("text", "safe_wording", "source_excerpt", "role_relevance")
# Free text in a decision that must not carry a figure the persona does not have.
DECISION_TEXT_FIELDS = ("main_match", "main_risk", "cv_angle", "skip_reason")
EVIDENCE_ID = re.compile(r"EV-[A-Z0-9-]+")
FIGURE = re.compile(r"\d+(?:[.,]\d+)*")
MIN_SHARED_WORDS = 2
MIN_SHARED_WORD_SHARE = 3  # a met requirement shares at least 1/3 of its words with the evidence it cites


def _words(text: str) -> set[str]:
    return set(re.findall(r"[a-z]{5,}", text.lower()))


def _figures(text: str) -> set[str]:
    """Whole numbers in text, so that 45 does not match inside 145. Spelled-out figures are not detected."""
    return set(FIGURE.findall(EVIDENCE_ID.sub("", text)))


def check_role_decision(scenario: dict, persona: dict) -> list[str]:
    """Return what is wrong with a scenario's expected decision; an empty list means it is consistent.

    A structural check, not proof that a model never invents evidence: it checks that a decision matches its role
    description, cites only real source-only evidence, keeps gaps as gaps and introduces no figure the persona lacks.
    The vocabulary rule is a heuristic: a met requirement must share at least two words, and a third of its words, with
    the wording of the evidence it cites (restrictions are excluded, since they forbid claims). Generic words can still
    overlap by chance. A model harness can call this on real model output.
    """
    errors: list[str] = []
    decision = scenario["expected_decision"]
    role = scenario["role_description"]
    items = decision["requirement_map"]

    expected_decision = OUTCOME_TO_DECISION[scenario["expected_outcome"]]
    if decision["decision"] != expected_decision:
        errors.append(f"decision is {decision['decision']!r}, expected {expected_decision!r}")

    stated = {(text, "essential") for text in role["essential_requirements"]}
    stated |= {(text, "important") for text in role.get("important_requirements", [])}
    mapped = {(item["requirement"], item["importance"]) for item in items}
    if mapped != stated:
        errors.append(f"requirement map differs from the role description: {sorted(mapped ^ stated)}")

    evidence = {item["evidence_id"]: item for item in persona["evidence"]}
    evidence_words = {
        evidence_id: _words(" ".join(str(item.get(field, "")) for field in WORDING_FIELDS))
        for evidence_id, item in evidence.items()
    }
    for item in items:
        name = item["requirement"]
        is_gap = item["assessment"] == "gap"
        if is_gap != (item["evidence_ids"] == []):
            errors.append(f"{name}: a gap must have no evidence and anything else must have some")
        unknown = [evidence_id for evidence_id in item["evidence_ids"] if evidence_id not in evidence]
        if unknown:
            errors.append(f"{name}: unknown evidence {unknown}")
            continue
        if is_gap:
            continue
        cited = set().union(*(evidence_words[evidence_id] for evidence_id in item["evidence_ids"]))
        shared = _words(name) & cited
        if len(shared) < MIN_SHARED_WORDS or len(shared) * MIN_SHARED_WORD_SHARE < len(_words(name)):
            errors.append(f"{name}: shares too little wording with the evidence it cites")

    essentials = [item for item in items if item["importance"] == "essential"]
    if not essentials:
        errors.append("no essential requirement is mapped")
    unmet = [item["requirement"] for item in essentials if item["assessment"] == "gap"]
    if scenario["expected_outcome"] == "pursue" and unmet:
        errors.append(f"a pursue decision has unmet essentials: {unmet}")
    if scenario["expected_outcome"] == "do_not_pursue" and len(unmet) != len(essentials):
        errors.append("a do-not-pursue decision must keep every essential requirement a gap")

    allowed = _figures(json.dumps(persona["evidence"]))
    texts = {field: decision.get(field) or "" for field in DECISION_TEXT_FIELDS}
    texts.update({f"gap_note[{item['requirement']}]": item.get("gap_note") or "" for item in items})
    for field, text in texts.items():
        invented = _figures(text) - allowed
        if invented:
            errors.append(f"{field}: figures not in the persona evidence: {sorted(invented)}")
    return errors


class CanadaRoleDecisionFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        cls.persona = load_persona(cls.fixture["persona"])

    def _scenario(self, scenario_id: str) -> dict:
        for scenario in self.fixture["scenarios"]:
            if scenario["scenario_id"] == scenario_id:
                return scenario
        raise AssertionError(f"missing scenario: {scenario_id}")

    def test_fixture_is_synthetic_and_covers_both_outcomes(self) -> None:
        self.assertTrue(self.fixture["synthetic"])
        self.assertEqual(self.fixture["market"], "Canada")
        outcomes = {scenario["expected_outcome"] for scenario in self.fixture["scenarios"]}
        self.assertEqual(outcomes, set(OUTCOME_TO_DECISION))

    def test_every_expected_decision_passes_the_role_dossier_contract(self) -> None:
        for scenario in self.fixture["scenarios"]:
            errors = validate_role_dossier(scenario["expected_decision"])
            self.assertEqual(errors, [], f"{scenario['scenario_id']}: {errors}")

    def test_every_expected_decision_is_consistent_with_its_role_and_the_persona(self) -> None:
        for scenario in self.fixture["scenarios"]:
            self.assertEqual(check_role_decision(scenario, self.persona), [], scenario["scenario_id"])

    def test_cited_evidence_stays_source_only(self) -> None:
        confidence_by_id = {item["evidence_id"]: item["confidence"] for item in self.persona["evidence"]}
        used = {
            evidence_id
            for scenario in self.fixture["scenarios"]
            for requirement in scenario["expected_decision"]["requirement_map"]
            for evidence_id in requirement["evidence_ids"]
        }
        self.assertTrue(used)
        for evidence_id in used:
            self.assertEqual(confidence_by_id[evidence_id], "source_only")

    def test_evidence_boundaries_quote_real_persona_restrictions(self) -> None:
        guard = self._scenario("do_not_pursue")["evidence_boundaries"]
        self.assertTrue(guard["forbidden_claims"])
        restrictions_by_id = {item["evidence_id"]: item.get("restrictions", []) for item in self.persona["evidence"]}
        for entry in guard["grounding"]:
            self.assertIn(entry["evidence_id"], restrictions_by_id, entry)
            self.assertIn(entry["restriction"], restrictions_by_id[entry["evidence_id"]], entry)


class CheckRoleDecisionCatchesBrokenDecisionsTests(unittest.TestCase):
    """The check must fail when a decision is edited the way it is meant to catch."""

    @classmethod
    def setUpClass(cls) -> None:
        fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        cls.persona = load_persona(fixture["persona"])
        cls.scenarios = {scenario["scenario_id"]: scenario for scenario in fixture["scenarios"]}

    def _mutated(self, scenario_id: str, mutate) -> list[str]:
        scenario = copy.deepcopy(self.scenarios[scenario_id])
        mutate(scenario["expected_decision"])
        return check_role_decision(scenario, self.persona)

    def _assert_flagged(self, scenario_id: str, mutate, fragment: str) -> None:
        errors = self._mutated(scenario_id, mutate)
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_gap_relabelled_as_met_without_evidence(self) -> None:
        def mutate(decision):
            decision["requirement_map"][4].update(assessment="direct")  # the unevidenced important requirement

        self._assert_flagged("pursue", mutate, "a gap must have no evidence")

    def test_gap_relabelled_as_met_on_unrelated_evidence(self) -> None:
        def mutate(decision):
            decision["requirement_map"][4].update(assessment="direct", evidence_ids=["EV-P02-001"])

        self._assert_flagged("pursue", mutate, "shares too little wording")

    def test_unknown_evidence_id(self) -> None:
        def mutate(decision):
            decision["requirement_map"][0]["evidence_ids"] = ["EV-P02-999"]

        self._assert_flagged("pursue", mutate, "unknown evidence")

    def test_essential_requirement_relabelled_important(self) -> None:
        def mutate(decision):
            decision["requirement_map"][0]["importance"] = "important"

        self._assert_flagged("pursue", mutate, "differs from the role description")

    def test_essential_requirement_turned_into_a_gap_on_a_pursue_decision(self) -> None:
        def mutate(decision):
            decision["requirement_map"][0].update(assessment="gap", evidence_ids=[])

        self._assert_flagged("pursue", mutate, "unmet essentials")

    def test_unmet_essential_relabelled_as_met_on_a_do_not_pursue_decision(self) -> None:
        def mutate(decision):
            decision["requirement_map"][0].update(assessment="adjacent", evidence_ids=["EV-P02-001"])

        self._assert_flagged("do_not_pursue", mutate, "must keep every essential requirement a gap")

    def test_decision_that_contradicts_the_outcome(self) -> None:
        def mutate(decision):
            decision["decision"] = "apply"

        self._assert_flagged("do_not_pursue", mutate, "expected 'skip'")

    def test_invented_figure_that_only_matches_as_a_substring(self) -> None:
        def mutate(decision):
            decision["main_match"] = decision["main_match"].replace("45-person", "145-person")

        self._assert_flagged("pursue", mutate, "main_match: figures not in the persona evidence: ['145']")

    def test_invented_figure_in_skip_reason_and_gap_note(self) -> None:
        def mutate(decision):
            decision["skip_reason"] += " The candidate directed 300 staff."
            decision["requirement_map"][0]["gap_note"] += " Covers 12 provinces."

        errors = self._mutated("do_not_pursue", mutate)
        self.assertTrue(any(error.startswith("skip_reason") and "'300'" in error for error in errors), errors)
        self.assertTrue(any(error.startswith("gap_note") and "'12'" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
