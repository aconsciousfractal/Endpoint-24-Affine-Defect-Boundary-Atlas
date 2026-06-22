# Public Release State

Status: published public companion repository. The `main` branch and release tag `v1.0.1` are pushed to GitHub.

## Completed

- [x] Create a standalone public companion repository layout.
- [x] Use the mathematical name `Endpoint-24 Affine-Defect Boundary Atlas`.
- [x] Remove old project branding, internal acronym leaks, private workspace paths, and draft-status language.
- [x] Finalize `LICENSE` and `CITATION.cff` for first public publication.
- [x] Include paper source, generated tables, bibliography, and rebuilt PDF.
- [x] Include curated public-export artifacts and appendix-only certificate support.
- [x] Exclude development-only raw data, record-level payload dumps, private provenance paths, and LaTeX auxiliaries.
- [x] Add hardened public package checks and CI smoke test.
- [x] Run repo and paper red-team passes and address their blockers.
- [x] Create local public-prep commits.
- [x] Publish the repository on GitHub.
- [x] Run public-package checks from a clean clone.
- [x] Create and push release tag `v1.0.1`.

## Post-Tag Gate

- [x] Keep the repository name aligned with `CITATION.cff`: `Endpoint-24-Affine-Defect-Boundary-Atlas`.
- [x] Confirm `python -m pytest -q` from a clean clone.
- [x] Confirm `python scripts/run_all_reproducibility_checks.py` from a clean clone.
- [x] Confirm `python scripts/check_public_package.py` from a clean clone.
- [ ] Optional: create a GitHub Release object from tag `v1.0.1`.
- [ ] Optional: archive/tag with DOI infrastructure if desired.
