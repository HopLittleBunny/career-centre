#!/usr/bin/env python3
"""Sync current provider downloads and build a deterministic public-site archive."""
from __future__ import annotations

import hashlib
import json
import shutil
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
RELEASE = ROOT / "release"
PUBLIC_SITE = ROOT / "public-site"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    latest = json.loads((RELEASE / "LATEST.json").read_text(encoding="utf-8"))
    claude_latest = json.loads((RELEASE / "CLAUDE_LATEST.json").read_text(encoding="utf-8"))
    if latest.get("version") != claude_latest.get("version"):
        raise SystemExit("Provider release versions do not match.")
    downloads = PUBLIC_SITE / "downloads"
    downloads.mkdir(exist_ok=True)
    skill_source = RELEASE / latest["skill"]["file"]
    claude_source = RELEASE / claude_latest["file"]
    skill_target = downloads / "career-centre-chatgpt-skill.zip"
    claude_target = downloads / "career-centre-claude-plugin.zip"
    shutil.copy2(skill_source, skill_target)
    shutil.copy2(claude_source, claude_target)
    if sha256(skill_target) != latest["skill"]["sha256"]:
        raise SystemExit("Public ChatGPT download checksum mismatch after copy.")
    if sha256(claude_target) != claude_latest["sha256"]:
        raise SystemExit("Public Claude download checksum mismatch after copy.")

    destination = RELEASE / "career-centre-public-site-20260715.zip"
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(PUBLIC_SITE.rglob("*")):
            if not path.is_file():
                continue
            info = zipfile.ZipInfo(str(Path("career-centre") / path.relative_to(PUBLIC_SITE)))
            info.date_time = (2026, 7, 15, 0, 0, 0)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())
    manifest = {
        "date": "2026-07-15",
        "version": latest["version"],
        "status": "submission",
        "file": destination.name,
        "sha256": sha256(destination),
        "downloads": {
            "chatgpt_skill_sha256": latest["skill"]["sha256"],
            "claude_plugin_sha256": claude_latest["sha256"],
        },
    }
    manifest_path = RELEASE / "PUBLIC_SITE_LATEST.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"passed": True, "archive": str(destination), "manifest": str(manifest_path), **manifest}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
