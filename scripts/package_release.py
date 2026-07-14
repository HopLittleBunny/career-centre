#!/usr/bin/env python3
"""Create deterministic plugin and skill ZIPs from the validated final tree."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path

from validate_release import PLUGIN, ROOT, SKILL, validate


def _zip_tree(source: Path, destination: Path, prefix: str) -> None:
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(source.rglob("*")):
            if not path.is_file():
                continue
            if path.suffix.casefold() in {".pyc", ".pyo"} or "__pycache__" in path.parts:
                continue
            info = zipfile.ZipInfo(str(Path(prefix) / path.relative_to(source)))
            info.date_time = (2026, 7, 14, 0, 0, 0)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--submission-ready", action="store_true")
    args = parser.parse_args()
    errors, warnings = validate(submission_ready=args.submission_ready)
    if errors:
        print(json.dumps({"passed": False, "errors": errors, "warnings": warnings}, indent=2))
        return 1
    manifest = json.loads((PLUGIN / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    version = manifest["version"]
    release = ROOT / "release"
    release.mkdir(exist_ok=True)
    suffix = "submission" if args.submission_ready else "draft"
    plugin_zip = release / f"career-centre-{version}-{suffix}-plugin.zip"
    skill_zip = release / f"career-centre-{version}-{suffix}-skill.zip"
    _zip_tree(PLUGIN, plugin_zip, PLUGIN.name)
    _zip_tree(SKILL, skill_zip, SKILL.name)
    latest = {
        "version": version,
        "status": suffix,
        "plugin": {"file": plugin_zip.name, "sha256": _sha256(plugin_zip)},
        "skill": {"file": skill_zip.name, "sha256": _sha256(skill_zip)},
    }
    latest_path = release / "LATEST.json"
    latest_path.write_text(json.dumps(latest, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "passed": True,
                "submission_ready": args.submission_ready,
                "plugin_zip": str(plugin_zip),
                "skill_zip": str(skill_zip),
                "latest_manifest": str(latest_path),
                "checksums": {"plugin": latest["plugin"]["sha256"], "skill": latest["skill"]["sha256"]},
                "warnings": warnings,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
