from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "REPRODUCE.md",
    "PUBLICATION_PLAN.md",
    "README_REVIEWER.md",
    "requirements.txt",
    "pytest.ini",
    "LICENSE",
    "CITATION.cff",
    "paper/affine_defect_boundary_atlas.tex",
    "paper/affine_defect_boundary_atlas.pdf",
    "paper/refs.bib",
    "paper/BUILD.md",
    "paper/PUBLIC_PACKAGE_MANIFEST.json",
    "paper/PAPER_SOURCE_BACKED_TABLES.json",
    "docs/CLAIM_LEDGER.md",
    "docs/PROOF_OBLIGATIONS.md",
    "docs/PUBLIC_CLAIM_BOUNDARY.md",
    "docs/PUBLIC_RELEASE_CHECKLIST.md",
]

REQUIRED_DIRS = [
    "paper/sections",
    "paper/generated",
    "docs",
    "results",
    "scripts",
    "tests",
    "data",
]

FORBIDDEN_EXACT_FILES = [
    "data/order4_normal_essential_880.json",
]

PRIVATE_STAGE_PREFIX = "results/" + "L"

FORBIDDEN_REGEXES = [
    re.compile(r"^" + re.escape(PRIVATE_STAGE_PREFIX) + r"[0-9].*\.json$"),
    re.compile(r"^" + re.escape(PRIVATE_STAGE_PREFIX) + r"[0-9].*\.md$"),
    re.compile(r"^paper/.*\.(aux|bbl|blg|log|out)$"),
]

FORBIDDEN_TEXT_PATTERNS = [
    "Magic" + " 24",
    "MAGIC" + " 24",
    "Working" + " draft",
    "480" + " passed",
    "magic" + "24",
    "Magic" + "24",
    "bounded_" + "magic",
    "pending" + "-public-release",
    "NO" + "ASSERTION",
    "example" + ".invalid",
    "P" + "APP",
    "papp" + "_",
    "extensions" + "/main",
    "Publish" + " repository",
    "first" + " public push",
    "before" + " tagging",
    "before" + " push/tag",
    "public-release-ready" + " local",
]

FORBIDDEN_TEXT_REGEXES = [
    re.compile(re.escape(PRIVATE_STAGE_PREFIX) + r"(?:[0-9]|\[0-9\])"),
]

TEXT_EXTENSIONS = {".json", ".md", ".tex", ".py", ".cff", ".bib", ".yml", ".yaml", ".txt"}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_manifest() -> dict:
    return json.loads((ROOT / "paper" / "PUBLIC_PACKAGE_MANIFEST.json").read_text(encoding="utf-8-sig"))



def check_full_endpoint_control(failures: list[str]) -> None:
    path = ROOT / "results" / "FULL_ENDPOINT_CONTROL_ATLAS.json"
    if not path.is_file():
        return
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    metadata = data.get("metadata", {})
    if metadata.get("record_payload_included") is not False:
        failures.append("full endpoint control artifact must remain summary-only")
    universe = data.get("universe", {})
    if universe.get("full_pair_count") != 7040:
        failures.append("full endpoint control artifact has wrong full_pair_count")
    endpoint_distribution = {int(k): int(v) for k, v in data.get("endpoint_distribution", {}).items()}
    if sum(endpoint_distribution.values()) != 7040:
        failures.append("full endpoint endpoint_distribution does not sum to 7040")
    tk_distribution = {int(k): int(v) for k, v in data.get("tk_endpoint_orbit_distribution", {}).items()}
    if sum(tk_distribution.values()) * 4 != 7040:
        failures.append("full endpoint T/K orbit distribution does not lift to 7040")
    endpoint24 = data.get("control_endpoints", {}).get("endpoint24_anchor", {})
    if endpoint24.get("record_count") != 236 or endpoint24.get("tk_orbit_count") != 59:
        failures.append("full endpoint artifact endpoint-24 anchor does not match 236/59")
    forbidden_payload_keys = {"records", "rows", "payload", "raw_records"}
    if forbidden_payload_keys.intersection(data.keys()):
        failures.append("full endpoint artifact exposes full-payload keys")

def check_tex_inputs(failures: list[str]) -> None:
    tex = ROOT / "paper" / "affine_defect_boundary_atlas.tex"
    if not tex.is_file():
        return
    text = tex.read_text(encoding="utf-8", errors="ignore")
    for item in re.findall(r"\\input\{([^}]+)\}", text):
        candidate = ROOT / "paper" / item
        if candidate.suffix == "":
            candidate = candidate.with_suffix(".tex")
        if not candidate.is_file():
            failures.append(f"missing TeX input target: {candidate.relative_to(ROOT).as_posix()}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check the public package shape.")
    parser.add_argument("--write", action="store_true", help="write results/public_package_check.json")
    args = parser.parse_args()
    failures: list[str] = []
    warnings: list[str] = []

    for item in REQUIRED_FILES:
        if not (ROOT / item).is_file():
            failures.append(f"missing required file: {item}")

    for item in REQUIRED_DIRS:
        if not (ROOT / item).is_dir():
            failures.append(f"missing required directory: {item}")

    pdf = ROOT / "paper" / "affine_defect_boundary_atlas.pdf"
    if pdf.is_file():
        head = pdf.read_bytes()[:4]
        if head != b"%PDF":
            failures.append("paper PDF does not start with %PDF")
        if pdf.stat().st_size < 100_000:
            failures.append("paper PDF is unexpectedly small")

    manifest = read_manifest()
    public_sources = manifest.get("public_export_sources", [])
    duplicate_public_sources = sorted({source for source in public_sources if public_sources.count(source) > 1})
    for source in duplicate_public_sources:
        failures.append(f"duplicate public export source in manifest: {source}")

    expected_sources = sorted(set(public_sources + manifest.get("appendix_only_sources", [])))
    for source in expected_sources:
        if not (ROOT / source).is_file():
            failures.append(f"missing declared public/appendix artifact: {source}")

    for row in manifest.get("paper_package_files", []):
        path = row.get("path") if isinstance(row, dict) else None
        if path and not (ROOT / path).is_file():
            failures.append(f"manifest declares missing package file: {path}")

    check_tex_inputs(failures)
    check_full_endpoint_control(failures)

    all_files = [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]
    rel_files = [rel(p) for p in all_files]
    for item in rel_files:
        if item in FORBIDDEN_EXACT_FILES or any(pattern.match(item) for pattern in FORBIDDEN_REGEXES):
            failures.append(f"forbidden development/build artifact present: {item}")

    for path in all_files:
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in FORBIDDEN_TEXT_PATTERNS:
            if pattern in text:
                failures.append(f"forbidden text pattern {pattern!r} in {rel(path)}")
        for regex in FORBIDDEN_TEXT_REGEXES:
            if regex.search(text):
                failures.append(f"forbidden text regex {regex.pattern!r} in {rel(path)}")

    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8", errors="ignore") if (ROOT / "LICENSE").exists() else ""
    citation_text = (ROOT / "CITATION.cff").read_text(encoding="utf-8", errors="ignore") if (ROOT / "CITATION.cff").exists() else ""
    release_ready = True
    if "human" in license_text.lower() or "review" in license_text.lower() or "pending" in license_text.lower():
        warnings.append("LICENSE appears to require human release review")
        release_ready = False
    if "human" in citation_text.lower() or "review" in citation_text.lower() or "pending" in citation_text.lower():
        warnings.append("CITATION.cff appears to require human release review")
        release_ready = False
    if manifest.get("summary", {}).get("public_export_ready") is False:
        warnings.append("paper manifest marks public_export_ready=false")
        release_ready = False

    report = {
        "package": "Endpoint-24 Affine-Defect Boundary Atlas",
        "status": "pass" if not failures else "fail",
        "release_ready": release_ready and not failures,
        "failures": failures,
        "warnings": warnings,
        "checked_declared_sources": expected_sources,
        "file_count": len(all_files),
    }
    if args.write:
        out = ROOT / "results" / "public_package_check.json"
        out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps(report, indent=2, sort_keys=True))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())