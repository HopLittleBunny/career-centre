from __future__ import annotations

import json
import unittest
from pathlib import Path


class PackageContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.skill_root = Path(__file__).resolve().parents[1]
        self.plugin_root = self.skill_root.parents[1]

    def test_all_schema_files_are_valid_json(self) -> None:
        schemas = sorted((self.skill_root / "schemas").glob("*.json"))
        self.assertGreaterEqual(len(schemas), 4)
        for path in schemas:
            with self.subTest(path=path.name):
                json.loads(path.read_text(encoding="utf-8"))

    def test_skill_has_simple_first_interaction_and_safety_boundaries(self) -> None:
        text = (self.skill_root / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Ask for the latest CV in one warm sentence", text)
        self.assertIn("maximum of four items", text)
        self.assertIn("Never auto-submit", text)
        self.assertIn("Default application pack is CV plus cover letter", text)
        self.assertIn("Exact posting link: missing - not reviewed", text)
        self.assertIn("Your Career Centre is ready", text)
        self.assertIn("change my advanced preferences", text)
        self.assertIn("page 2 at least 80% filled", text)
        self.assertIn("Use global, market-aware defaults", text)
        self.assertIn("Any role identified by title, company or posting link", text)
        self.assertIn("including a weak candidate, inspected rejection, near miss or example", text)
        self.assertIn("exact employer posting is accessible, it is authoritative", text)
        self.assertIn("Never let a mirror override or relabel salary", text)
        self.assertIn("it is not a separate `reference CV`", text)
        self.assertIn("Create or refresh a CV base", text)
        self.assertIn("CV bases and reference-format documents", text)
        self.assertIn("Do not approve the document on the generic document capability's self-reported QA alone", text)

    def test_skill_description_routes_cv_base_and_reference_format_language(self) -> None:
        text = (self.skill_root / "SKILL.md").read_text(encoding="utf-8")
        frontmatter = text.split("---", 2)[1]
        for phrase in (
            "Primary skill for any request about a person's own job search",
            "Must be used for creating a reusable CV base",
            "generic document tools may assist only after this career skill is loaded",
            '"create a CV base"',
            '"use this CV as my format"',
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, frontmatter)

    def test_release_tree_contains_no_compiled_or_html_artifacts(self) -> None:
        forbidden = [
            path
            for path in self.plugin_root.rglob("*")
            if path.is_file() and (path.suffix.casefold() in {".pyc", ".pyo", ".html", ".htm"} or "__pycache__" in path.parts)
        ]
        self.assertEqual(forbidden, [])

    def test_manifest_matches_plugin_folder(self) -> None:
        manifest = json.loads((self.plugin_root / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["name"], self.plugin_root.name)
        self.assertEqual(manifest["interface"]["developerName"], "Amit Sharma")
        self.assertIsInstance(manifest["interface"]["defaultPrompt"], list)
        self.assertLessEqual(len(manifest["interface"]["defaultPrompt"]), 3)


if __name__ == "__main__":
    unittest.main()
