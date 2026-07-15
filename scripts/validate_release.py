#!/usr/bin/env python3
"""Validate the Career Centre repository and submission materials."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "career-command-centre"
SKILL = PLUGIN / "skills" / "career-command-centre"
CLAUDE_PLUGIN = ROOT / "plugins" / "claude-career-centre"
CLAUDE_SKILL = CLAUDE_PLUGIN / "skills" / "career-centre"
CLAUDE_MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
PUBLIC_SITE = ROOT / "public-site"
PLACEHOLDER_PATTERN = re.compile(r"(?:PUBLIC_[A-Z_]+_REQUIRED|PUBLIC_SUPPORT_ROUTE_REQUIRED)")


class _LocalAssetParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.references: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        for key in ("href", "src"):
            value = values.get(key)
            if value:
                self.references.append(value)


def _validate_public_site(
    errors: list[str], warnings: list[str], *, submission_ready: bool
) -> None:
    required_pages = [
        "index.html",
        "install.html",
        "privacy.html",
        "terms.html",
        "support.html",
        "release-notes.html",
        "404.html",
    ]
    for name in required_pages:
        path = PUBLIC_SITE / name
        if not path.is_file() or len(path.read_text(encoding="utf-8").split()) < 20:
            errors.append(f"Static public page is missing or too short: public-site/{name}")

    html_paths = sorted(PUBLIC_SITE.glob("*.html"))
    for path in html_paths:
        text = path.read_text(encoding="utf-8")
        if "<meta name=\"viewport\"" not in text:
            errors.append(f"Static page lacks a viewport declaration: {path.relative_to(ROOT)}")
        if text.count('class="skip-link"') != 1 or 'href="#main-content"' not in text:
            errors.append(f"Static page lacks one keyboard skip link: {path.relative_to(ROOT)}")
        if 'id="main-content"' not in text:
            errors.append(f"Static page lacks a main-content target: {path.relative_to(ROOT)}")
        if 'class="brand"' in text and 'aria-label="Career Centre home"' not in text:
            errors.append(f"Static page has an unnamed mobile home link: {path.relative_to(ROOT)}")
        if "PUBLIC_" in text:
            errors.append(f"Static page contains a public placeholder: {path.relative_to(ROOT)}")
        if "—" in text or "–" in text:
            errors.append(f"Static page contains a forbidden display dash: {path.relative_to(ROOT)}")

        parser = _LocalAssetParser()
        parser.feed(text)
        for reference in parser.references:
            parsed = urlsplit(reference)
            if parsed.scheme or parsed.netloc or reference.startswith(("#", "mailto:", "tel:")):
                continue
            clean_path = unquote(parsed.path)
            if not clean_path:
                continue
            target = (PUBLIC_SITE / clean_path.lstrip("/")) if clean_path.startswith("/") else (path.parent / clean_path)
            if not target.resolve().is_file():
                errors.append(
                    f"Broken local public-site reference in {path.relative_to(ROOT)}: {reference}"
                )

    homepage = (PUBLIC_SITE / "index.html").read_text(encoding="utf-8")
    required_copy = [
        "Your Career Centre is ready",
        "advanced preferences",
        "Quick CV review",
        "Share your CVs",
        "Reference CV formatting",
        "Career Passport",
        "saved snapshot",
        "No automatic applications",
        "Install Career Centre",
    ]
    for phrase in required_copy:
        if phrase.casefold() not in homepage.casefold():
            errors.append(f"Static homepage is missing required product copy: {phrase}")

    readiness_labels = re.findall(r"<dt>([^<]+)</dt>", homepage)
    expected_readiness_labels = [
        "Target",
        "Geography",
        "Sources",
        "Compensation",
        "CV",
        "Sections",
        "Application pack",
    ]
    if readiness_labels != expected_readiness_labels:
        errors.append(
            "Static homepage readiness labels must be exactly "
            f"{expected_readiness_labels}; got {readiness_labels}."
        )

    download = PUBLIC_SITE / "downloads" / "career-centre-chatgpt-skill.zip"
    latest_path = ROOT / "release" / "LATEST.json"
    try:
        expected = json.loads(latest_path.read_text(encoding="utf-8"))["skill"]["sha256"]
        actual = hashlib.sha256(download.read_bytes()).hexdigest()
        if actual != expected:
            errors.append("Public skill download does not match release/LATEST.json.")
    except Exception as exc:
        errors.append(f"Public skill download cannot be validated: {exc}")

    claude_download = PUBLIC_SITE / "downloads" / "career-centre-claude-plugin.zip"
    claude_latest_path = ROOT / "release" / "CLAUDE_LATEST.json"
    try:
        expected = json.loads(claude_latest_path.read_text(encoding="utf-8"))["sha256"]
        actual = hashlib.sha256(claude_download.read_bytes()).hexdigest()
        if actual != expected:
            errors.append("Public Claude plugin download does not match release/CLAUDE_LATEST.json.")
    except Exception as exc:
        errors.append(f"Public Claude plugin download cannot be validated: {exc}")

    try:
        site_latest = json.loads((ROOT / "release" / "PUBLIC_SITE_LATEST.json").read_text(encoding="utf-8"))
        site_bundle = ROOT / "release" / str(site_latest["file"])
        site_actual = hashlib.sha256(site_bundle.read_bytes()).hexdigest()
        if site_actual != site_latest["sha256"]:
            errors.append("Public-site bundle does not match release/PUBLIC_SITE_LATEST.json.")
    except Exception as exc:
        errors.append(f"Public-site bundle cannot be validated: {exc}")

    support_html = (PUBLIC_SITE / "support.html").read_text(encoding="utf-8")
    has_external_support = bool(re.search(r'href="https://[^\"]+"', support_html))
    if submission_ready and not has_external_support:
        errors.append("Submission-ready public support page requires a working external support route.")
    elif not has_external_support:
        warnings.append("Draft-only: the static support page still needs its publisher-matched issue route.")


def _run_tests(errors: list[str]) -> None:
    for label, skill_root in (("ChatGPT", SKILL), ("Claude", CLAUDE_SKILL)):
        process = subprocess.run(
            [sys.executable, str(skill_root / "scripts" / "run_tests.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            env={**__import__("os").environ, "PYTHONDONTWRITEBYTECODE": "1"},
        )
        if process.returncode:
            errors.append(f"{label} unit/contract tests failed:\n" + process.stdout + process.stderr)


def validate(*, submission_ready: bool) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    manifest_path = PLUGIN / ".codex-plugin" / "plugin.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"Plugin manifest cannot be read: {exc}"], warnings
    if manifest.get("name") != PLUGIN.name:
        errors.append("Plugin manifest name must match its folder name.")
    version = manifest.get("version")
    if not isinstance(version, str) or not version:
        errors.append("Plugin manifest must declare a version.")
    skill_path = PLUGIN / str(manifest.get("skills", ""))
    if not skill_path.exists():
        errors.append("Manifest skills path does not exist.")
    interface = manifest.get("interface", {})
    prompts = interface.get("defaultPrompt", [])
    if not isinstance(prompts, list) or not 1 <= len(prompts) <= 3:
        errors.append("Manifest must define one to three starter prompts.")
    for key in ("composerIcon", "logo"):
        value = interface.get(key)
        if not value or not (PLUGIN / str(value)).is_file():
            errors.append(f"Manifest interface.{key} must point to an existing file.")

    try:
        claude_manifest = json.loads(
            (CLAUDE_PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")
        )
    except Exception as exc:
        errors.append(f"Claude plugin manifest cannot be read: {exc}")
        claude_manifest = {}
    if claude_manifest.get("name") != "career-centre":
        errors.append("Claude plugin manifest must use the career-centre identity.")
    if claude_manifest.get("displayName") != "Career Centre":
        errors.append("Claude plugin must display the Career Centre name.")
    if claude_manifest.get("version") != version:
        errors.append("ChatGPT and Claude package versions must match.")
    if not (CLAUDE_SKILL / "SKILL.md").is_file():
        errors.append("Claude Career Centre skill is missing.")

    try:
        marketplace = json.loads(CLAUDE_MARKETPLACE.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"Claude marketplace manifest cannot be read: {exc}")
        marketplace = {}
    entries = marketplace.get("plugins", [])
    if marketplace.get("name") != "hoplittlebunny-career-tools":
        errors.append("Claude marketplace identity is invalid.")
    if len(entries) != 1 or entries[0].get("source") != "./plugins/claude-career-centre":
        errors.append("Claude marketplace must expose the native Career Centre plugin.")
    elif entries[0].get("version") != version or marketplace.get("version") != version:
        errors.append("Claude marketplace and plugin package versions must match.")

    required_audit_files = [
        ROOT / "THIRD_PARTY_NOTICES.md",
        ROOT / "docs" / "OPEN_SOURCE_REPO_AUDIT.md",
        ROOT / "docs" / "LICENSE_COMPATIBILITY.md",
    ]
    for path in required_audit_files:
        if not path.is_file() or len(path.read_text(encoding="utf-8").split()) < 20:
            errors.append(f"Open-source audit record is missing or too short: {path.relative_to(ROOT)}")
    for skill_root in (SKILL, CLAUDE_SKILL):
        reviewer = skill_root / "scripts" / "review_cv_text.py"
        if not reviewer.is_file():
            errors.append(f"Qualitative CV diagnostic is missing: {reviewer.relative_to(ROOT)}")

    cases_path = ROOT / "submission" / "REVIEWER_TEST_CASES.json"
    try:
        cases = json.loads(cases_path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"Reviewer cases cannot be read: {exc}")
        cases = {}
    if len(cases.get("positive", [])) != 5:
        errors.append("Submission must contain exactly five positive reviewer cases.")
    if len(cases.get("negative", [])) != 3:
        errors.append("Submission must contain exactly three negative reviewer cases.")
    identifiers = [case.get("id") for group in ("positive", "negative") for case in cases.get(group, [])]
    if len(identifiers) != len(set(identifiers)):
        errors.append("Reviewer case IDs must be unique.")

    required_public = [
        PUBLIC_SITE / "index.md",
        PUBLIC_SITE / "privacy.md",
        PUBLIC_SITE / "terms.md",
        PUBLIC_SITE / "support.md",
    ]
    for path in required_public:
        if not path.is_file() or len(path.read_text(encoding="utf-8").split()) < 20:
            errors.append(f"Public page is missing or too short: {path.relative_to(ROOT)}")

    all_files = [
        path
        for plugin_root in (PLUGIN, CLAUDE_PLUGIN)
        for path in plugin_root.rglob("*")
        if path.is_file()
    ]
    forbidden = [
        path for path in all_files
        if path.suffix.casefold() in {".pyc", ".pyo", ".html", ".htm"} or "__pycache__" in path.parts
    ]
    if forbidden:
        errors.append("Plugin contains forbidden generated artifacts: " + ", ".join(path.name for path in forbidden))
    for path in all_files:
        if path.suffix.casefold() in {".png", ".docx"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if "/Users/" in text or "C:\\Users\\" in text:
            errors.append(f"Plugin source leaks an absolute user path: {path.relative_to(ROOT)}")

    listing_text = (ROOT / "submission" / "LISTING.md").read_text(encoding="utf-8")
    support_text = (PUBLIC_SITE / "support.md").read_text(encoding="utf-8")
    unresolved = PLACEHOLDER_PATTERN.findall(listing_text + "\n" + support_text)
    legal_keys = ("websiteURL", "privacyPolicyURL", "termsOfServiceURL")
    if submission_ready:
        if unresolved:
            errors.append("Public URL placeholders remain: " + ", ".join(sorted(set(unresolved))))
        for key in legal_keys:
            value = interface.get(key)
            if not isinstance(value, str) or not value.startswith("https://"):
                errors.append(f"Submission-ready manifest requires an HTTPS interface.{key}.")
    elif unresolved:
        warnings.append("Draft-only: public website/support/privacy/terms URLs are not live yet.")

    _validate_public_site(errors, warnings, submission_ready=submission_ready)
    _run_tests(errors)
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--submission-ready", action="store_true")
    args = parser.parse_args()
    errors, warnings = validate(submission_ready=args.submission_ready)
    report = {
        "submission_ready_mode": args.submission_ready,
        "passed": not errors,
        "errors": errors,
        "warnings": warnings,
    }
    print(json.dumps(report, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
