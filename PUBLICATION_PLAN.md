# Public Release Preparation Plan

Status: public-release-ready local companion repository. The repository has no Git remote configured intentionally, so GitHub Desktop should offer `Publish repository` rather than `Publish branch`.

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

## Publish Gate

- [ ] In GitHub Desktop, use `Publish repository` for `Endpoint-24-Affine-Defect-Boundary-Atlas`.
- [ ] Keep the repository name aligned with `CITATION.cff`: `Endpoint-24-Affine-Defect-Boundary-Atlas`.
- [ ] After publication, run `python -m pytest -q` and `python scripts/run_all_reproducibility_checks.py` from a clean clone or fresh checkout.
- [ ] Create a release tag only after the clean-clone checks pass.
