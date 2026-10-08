from __future__ import annotations

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


class CanadaRoleDecisionFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        cls.persona = load_persona(cls.fixture["persona"])
        cls.evidence_ids = {item["evidence_id"] for item in cls.persona["evidence"]}

    def _scenario(self, scenario_id: str) -> dict:
        for scenario in self.fixture["scenarios"]:
            if scenario["scenario_id"] == scenario_id:
                return scenario
        raise AssertionError(f"missing scenario: {scenario_id}")

    def test_fixture_is_synthetic_and_covers_both_outcomes(self) -> None:
        self.assertTrue(self.fixture["synthetic"])
        self.assertEqual(self.fixture["market"], "Canada")
        outcomes = {scenario["expected_outcome"] for scenario in self.fixture["scenarios"]}
        self.assertEqual(outcomes, {"pursue", "do_not_pursue"})

    def test_every_expected_decision_passes_the_role_dossier_contract(self) -> None:
        for scenario in self.fixture["scenarios"]:
            errors = validate_role_dossier(scenario["expected_decision"])
            self.assertEqual(errors, [], f"{scenario['scenario_id']}: {errors}")

    def test_cited_evidence_resolves_to_the_persona_evidence_set(self) -> None:
        for scenario in self.fixture["scenarios"]:
            for requirement in scenario["expected_decision"]["requirement_map"]:
                for evidence_id in requirement["evidence_ids"]:
                    self.assertIn(evidence_id, self.evidence_ids, requirement["requirement"])

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

    def test_pursue_scenario_maps_every_essential_requirement_to_real_evidence(self) -> None:
        dossier = self._scenario("pursue")["expected_decision"]
        essentials = [item for item in dossier["requirement_map"] if item["importance"] == "essential"]
        self.assertGreaterEqual(len(essentials), 3)
        for requirement in essentials:
            self.assertIn(requirement["assessment"], {"direct", "adjacent"})
            self.assertTrue(requirement["evidence_ids"])

    def test_every_requirement_and_its_importance_come_from_the_role_description(self) -> None:
        for scenario in self.fixture["scenarios"]:
            role = scenario["role_description"]
            stated = {(text, "essential") for text in role["essential_requirements"]}
            stated |= {(text, "important") for text in role.get("important_requirements", [])}
            mapped = {(item["requirement"], item["importance"])
                      for item in scenario["expected_decision"]["requirement_map"]}
            self.assertEqual(mapped, stated, scenario["scenario_id"])

    def test_do_not_pursue_scenario_keeps_unmet_essentials_as_gaps(self) -> None:
        dossier = self._scenario("do_not_pursue")["expected_decision"]
        self.assertEqual(dossier["decision"], "skip")
        self.assertTrue(dossier["skip_reason"].strip())

        essentials = [item for item in dossier["requirement_map"] if item["importance"] == "essential"]
        self.assertTrue(essentials)
        for requirement in essentials:
            self.assertEqual(requirement["assessment"], "gap")
            self.assertEqual(requirement["evidence_ids"], [])

    def test_outcome_maps_to_the_expected_decision(self) -> None:
        expected = {"pursue": "apply", "do_not_pursue": "skip"}
        for scenario in self.fixture["scenarios"]:
            self.assertEqual(scenario["expected_decision"]["decision"], expected[scenario["expected_outcome"]],
                             scenario["scenario_id"])

    def test_a_gap_has_no_evidence_and_everything_else_has_some(self) -> None:
        for scenario in self.fixture["scenarios"]:
            for item in scenario["expected_decision"]["requirement_map"]:
                self.assertEqual(item["assessment"] == "gap", item["evidence_ids"] == [], item["requirement"])

    def test_met_requirements_share_vocabulary_with_the_evidence_they_cite(self) -> None:
        """A heuristic, not proof: a met requirement must share at least two words, and at least
        a third of its words, with the wording of the evidence it cites. Restrictions are
        excluded, since they forbid claims. Generic words can still overlap by chance."""
        wording_fields = ("text", "safe_wording", "source_excerpt", "role_relevance")
        evidence_words = {
            item["evidence_id"]: set(re.findall(
                r"[a-z]{5,}", " ".join(str(item.get(field, "")) for field in wording_fields).lower()))
            for item in self.persona["evidence"]
        }
        for scenario in self.fixture["scenarios"]:
            for item in scenario["expected_decision"]["requirement_map"]:
                if item["assessment"] == "gap":
                    continue
                words = set(re.findall(r"[a-z]{5,}", item["requirement"].lower()))
                cited = set().union(*(evidence_words[evidence_id] for evidence_id in item["evidence_ids"]))
                shared = words & cited
                self.assertGreaterEqual(len(shared), 2, item["requirement"])
                self.assertGreaterEqual(len(shared) * 3, len(words), item["requirement"])

    def test_figures_in_the_decision_text_come_from_the_persona(self) -> None:
        evidence_text = " ".join(str(v) for item in self.persona["evidence"] for v in item.values())
        for scenario in self.fixture["scenarios"]:
            dossier = scenario["expected_decision"]
            for field in ("main_match", "main_risk", "cv_angle"):
                for number in re.findall(r"\d+", dossier.get(field) or ""):
                    self.assertIn(number, evidence_text, f"{scenario['scenario_id']}.{field}")

    def test_evidence_boundaries_quote_real_persona_restrictions(self) -> None:
        guard = self._scenario("do_not_pursue")["evidence_boundaries"]
        self.assertTrue(guard["forbidden_claims"])
        restrictions_by_id = {item["evidence_id"]: item.get("restrictions", []) for item in self.persona["evidence"]}
        for entry in guard["grounding"]:
            evidence_id, _, quoted = entry.partition(" restriction: ")
            self.assertIn(evidence_id, restrictions_by_id, entry)
            self.assertIn(quoted, restrictions_by_id[evidence_id], entry)


if __name__ == "__main__":
    unittest.main()
