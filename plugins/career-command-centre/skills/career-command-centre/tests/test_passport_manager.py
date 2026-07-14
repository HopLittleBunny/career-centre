from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_ROOT = Path(__file__).resolve().parents[1] / "scripts"
FIXTURE_ROOT = Path(__file__).resolve().parent / "fixtures"
sys.path.insert(0, str(SCRIPT_ROOT))
sys.path.insert(0, str(FIXTURE_ROOT))

from contracts import validate_career_passport  # noqa: E402
from factory import career_passport  # noqa: E402


class PassportManagerTests(unittest.TestCase):
    def _run(self, passport: Path, *args: str) -> subprocess.CompletedProcess[str]:
        environment = dict(os.environ)
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        return subprocess.run(
            [sys.executable, str(SCRIPT_ROOT / "manage_passport.py"), str(passport), *args],
            check=False,
            capture_output=True,
            text=True,
            env=environment,
        )

    def test_feedback_and_advanced_preference_correction_persist_safely(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "Career_Passport.json"
            path.write_text(json.dumps(career_passport()), encoding="utf-8")
            feedback = self._run(
                path,
                "append-feedback",
                "--category",
                "document",
                "--statement",
                "Keep projects above education.",
                "--confirmed",
            )
            self.assertEqual(feedback.returncode, 0, feedback.stderr or feedback.stdout)
            correction = self._run(
                path,
                "correct",
                "--field",
                "preferences.document_preferences.section_order",
                "--value-json",
                '["Professional Summary", "Role-Match Experience", "Professional Experience", "Projects", "Core Skills", "Education"]',
            )
            self.assertEqual(correction.returncode, 0, correction.stderr or correction.stdout)
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(validate_career_passport(data), [])
            self.assertTrue(data["feedback"][0]["confirmed"])
            self.assertEqual(data["feedback"][0]["statement"], "Keep projects above education.")
            self.assertEqual(data["corrections"][-1]["field"], "preferences.document_preferences.section_order")
            self.assertIn("Projects", data["preferences"]["document_preferences"]["section_order"])

    def test_field_level_cv_preferences_can_be_added_as_advanced_configuration(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "Career_Passport.json"
            path.write_text(json.dumps(career_passport()), encoding="utf-8")
            fields = {
                "contact_field_order": ["email", "linkedin"],
                "hidden_contact_fields": ["phone"],
                "show_location": True,
                "show_work_rights": False,
                "headline_mode": "role_specific",
                "date_style": "month_year",
                "section_label_overrides": {"Professional Experience": "Career Experience"},
                "notes": [],
            }
            result = self._run(
                path,
                "correct",
                "--field",
                "preferences.document_preferences.field_preferences",
                "--value-json",
                json.dumps(fields),
            )
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(validate_career_passport(data), [])
            self.assertEqual(data["preferences"]["document_preferences"]["field_preferences"], fields)

    def test_invalid_correction_fails_without_mutating_passport(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "Career_Passport.json"
            original = career_passport()
            path.write_text(json.dumps(original), encoding="utf-8")
            result = self._run(
                path,
                "correct",
                "--field",
                "preferences.currency",
                "--value-json",
                '"Australian dollars"',
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), original)


if __name__ == "__main__":
    unittest.main()
