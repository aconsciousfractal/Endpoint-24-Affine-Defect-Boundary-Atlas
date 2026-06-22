from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD_PROJECT = "Magic" + " 24"
OLD_DRAFT = "Working" + " draft"
OLD_COMPACT = "magic" + "24"
OLD_DEV_PREFIX = "bounded_" + "magic"
OLD_INTERNAL_CODE = "P" + "APP"
OLD_INTERNAL_KEY = "papp" + "_"
OLD_DEV_PATH = "extensions" + "/main"
STALE_PUBLISH_REPO = "Publish" + " repository"
STALE_FIRST_PUBLIC_PUSH = "first" + " public push"
STALE_BEFORE_TAGGING = "before" + " tagging"
STALE_BEFORE_PUSH_TAG = "before" + " push/tag"
STALE_PUBLIC_READY_LOCAL = "public-release-ready" + " local"


def test_public_package_check_passes() -> None:
    completed = subprocess.run(
        [sys.executable, "scripts/check_public_package.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr
    report = json.loads(completed.stdout)
    assert report["status"] == "pass"
    assert report["release_ready"] is True


def test_old_branding_absent_from_public_text() -> None:
    checked_extensions = {".json", ".md", ".tex", ".py", ".cff", ".bib", ".yml", ".yaml", ".txt"}
    offenders = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in checked_extensions:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        patterns = [
            OLD_PROJECT,
            OLD_DRAFT,
            OLD_COMPACT,
            OLD_DEV_PREFIX,
            OLD_INTERNAL_CODE,
            OLD_INTERNAL_KEY,
            OLD_DEV_PATH,
            STALE_PUBLISH_REPO,
            STALE_FIRST_PUBLIC_PUSH,
            STALE_BEFORE_TAGGING,
            STALE_BEFORE_PUSH_TAG,
            STALE_PUBLIC_READY_LOCAL,
        ]
        if any(pattern in text for pattern in patterns):
            offenders.append(path.relative_to(ROOT).as_posix())
    assert offenders == []


def test_declared_scope_artifacts_present() -> None:
    manifest = json.loads((ROOT / "paper" / "PUBLIC_PACKAGE_MANIFEST.json").read_text(encoding="utf-8"))
    expected = sorted(set(manifest["public_export_sources"] + manifest["appendix_only_sources"]))
    missing = [p for p in expected if not (ROOT / p).is_file()]
    assert missing == []