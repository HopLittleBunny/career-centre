#!/usr/bin/env python3
"""Validate and package the Claude Career Centre plugin."""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "claude-career-centre"
SKILL = PLUGIN / "skills" / "career-centre"
MANIFEST = PLUGIN / ".claude-plugin" / "plugin.json"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate() -> list[str]:
    errors: list[str] = []
    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"Claude plugin manifest cannot be read: {exc}"]
    if manifest.get("name") != "career-centre":
        errors.append("Claude plugin name must be career-centre.")
    if manifest.get("displayName") != "Career Centre":
        errors.append("Claude plugin displayName must be Career Centre.")
    if manifest.get("version") != "4.0.0-beta.3":
        errors.append("Claude plugin version must match the public beta.")
    try:
        marketplace = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    except Exception as exc:
        marketplace = {}
        errors.append(f"Claude marketplace manifest cannot be read: {exc}")
    entries = marketplace.get("plugins", [])
    if marketplace.get("name") != "hoplittlebunny-career-tools":
        errors.append("Claude marketplace must use the public Career Centre marketplace identity.")
    if len(entries) != 1 or entries[0].get("name") != "career-centre":
        errors.append("Claude marketplace must contain exactly the Career Centre plugin.")
    elif entries[0].get("source") != "./plugins/claude-career-centre":
        errors.append("Claude marketplace source must point to the native plugin directory.")
    skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    if not skill_text.startswith("---\nname: career-centre\n"):
        errors.append("Claude skill frontmatter must use the career-centre name.")
    if "ChatGPT" in skill_text:
        errors.append("Claude skill contains ChatGPT-specific host language.")
    for path in PLUGIN.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.casefold() in {".pyc", ".pyo", ".html", ".htm"} or "__pycache__" in path.parts:
            errors.append(f"Claude plugin contains a forbidden generated artifact: {path.relative_to(ROOT)}")
            continue
        if path.suffix.casefold() in {".png", ".docx"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if "/Users/" in text or "C:\\Users\\" in text:
            errors.append(f"Claude plugin leaks an absolute user path: {path.relative_to(ROOT)}")
        if "ChatGPT" in text:
            errors.append(f"Claude plugin contains ChatGPT-specific host language: {path.relative_to(ROOT)}")
    process = subprocess.run(
        [sys.executable, str(SKILL / "scripts" / "run_tests.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    if process.returncode:
        errors.append("Claude plugin tests failed:\n" + process.stdout + process.stderr)
    return errors


def build_zip(destination: Path) -> None:
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(PLUGIN.rglob("*")):
            if not path.is_file():
                continue
            if path.suffix.casefold() in {".pyc", ".pyo"} or "__pycache__" in path.parts:
                continue
            info = zipfile.ZipInfo(str(Path("career-centre") / path.relative_to(PLUGIN)))
            info.date_time = (2026, 7, 14, 0, 0, 0)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())


def main() -> int:
    errors = validate()
    if errors:
        print(json.dumps({"passed": False, "errors": errors}, indent=2))
        return 1
    release = ROOT / "release"
    release.mkdir(exist_ok=True)
    destination = release / "career-centre-4.0.0-beta.3-claude-plugin.zip"
    build_zip(destination)
    latest = {
        "version": "4.0.0-beta.3",
        "status": "submission-candidate",
        "file": destination.name,
        "sha256": sha256(destination),
    }
    latest_path = release / "CLAUDE_LATEST.json"
    latest_path.write_text(json.dumps(latest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"passed": True, "plugin_zip": str(destination), "manifest": str(latest_path), "sha256": latest["sha256"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
