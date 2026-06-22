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
    checked_extensions = {".md", ".tex", ".py", ".cff", ".bib", ".yml", ".yaml", ".txt"}
    offenders = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in checked_extensions:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if OLD_PROJECT in text or OLD_DRAFT in text or OLD_COMPACT in text or OLD_DEV_PREFIX in text:
            offenders.append(path.relative_to(ROOT).as_posix())
    assert offenders == []


def test_declared_scope_artifacts_present() -> None:
    manifest = json.loads((ROOT / "paper" / "PUBLIC_PACKAGE_MANIFEST.json").read_text(encoding="utf-8"))
    expected = sorted(set(manifest["public_export_sources"] + manifest["appendix_only_sources"]))
    missing = [p for p in expected if not (ROOT / p).is_file()]
    assert missing == []