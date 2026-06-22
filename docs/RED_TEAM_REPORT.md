# Public Release Red-Team Report

Date: 2026-06-22
Scope: Endpoint-24 Affine-Defect Boundary Atlas public companion repository and paper.
Standard: release-audit checks for claim boundary, source scope, reproducibility,
metadata, old-branding hygiene, artifact leakage, TeX/PDF rebuildability, and
release-state consistency.
Reviewers: delegated read-only repo red-team and delegated read-only paper red-team, followed by local closure pass.

## Verdict

Local public companion repository: release-ready for first public push.

Remaining operational gate: publish the repository, then run the public checks from a clean clone before tagging a release.

## Red-Team Findings And Closure

| ID | Severity | Finding | Closure |
|---|---|---|---|
| RT-1 | blocker | Release-state metadata conflicted across README, plan, red-team report, proof obligations, and manifests. | Closed: release metadata now consistently describes a local public-release-ready repo with only remote/push verification remaining. |
| RT-2 | blocker | Traceability docs referenced private development scripts/tests absent from the public repo. | Closed: `docs/PAPER_TO_ENGINE_TRACEABILITY.md` now maps paper claims to public artifacts and public checks only. |
| RT-3 | high | `SOURCE_LOCK.md` listed only two appendix-only artifacts while source map/manifest listed four. | Closed: source lock now lists `PAPER_FINAL`, `ITEM7`, `ITEM10`, and `ITEM11` as appendix-only support. |
| RT-4 | high | `PAPER_WORKSPACE_MANIFEST.json` was stale development metadata. | Closed: removed from the public repo. |
| RT-5 | medium | Introduction used stale release-draft wording. | Closed: introduction now states the paper directly as a focused companion. |
| RT-6 | low | `results/public_package_check.json` can be generated as ignored local residue. | Accepted: public checks are read-only by default; `run_all_reproducibility_checks.py` writes this ignored report only on demand. |
| RT-7 | low | Underfull hbox warnings remain in the generated table. | Accepted: no overfull boxes, no unresolved citations, no unresolved references; table content is correct. |
| RT-8 | high | Internal methodology acronym leaked into public docs and the compiled PDF. | Closed: public-facing wording now uses public/release/package terminology; PDF text scan is clean. |
| RT-9 | high | Shipped provenance metadata contained private development-workspace paths and absent private source filenames. | Closed: public source maps point to shipped artifacts or explicitly mark private provenance as not shipped. |
| RT-10 | medium | Package checker did not scan JSON and did not block internal acronym/path leaks. | Closed: checker and tests now scan JSON and forbid old branding, internal acronym keys, and private workspace paths. |

## Final Local Checks

Required before push:

```powershell
python scripts/check_public_package.py
python -m pytest -q
python scripts/run_all_reproducibility_checks.py
```

The checker verifies TeX inputs, declared public/appendix artifacts, manifest
file existence, forbidden development artifacts, old branding, stale release
metadata, and PDF presence.