# Public Release Preparation Plan

Status: public-release-ready local companion repository. The remaining operational step is to confirm the GitHub remote exists, push `main`, and run the same checks from that pushed checkout.

## Completed

- [x] Create a standalone public companion repository layout.
- [x] Use the mathematical name `Endpoint-24 Affine-Defect Boundary Atlas`.
- [x] Remove old project branding and draft-status language.
- [x] Finalize `LICENSE` and `CITATION.cff`.
- [x] Include paper source, generated tables, bibliography, and rebuilt PDF.
- [x] Include curated public-export artifacts and appendix-only certificate support.
- [x] Exclude development-only raw data, record-level payload dumps, and LaTeX auxiliaries.
- [x] Add public package checks and CI smoke test.
- [x] Run repo and paper red-team passes and address their blockers.
- [x] Create the first local commit.

## Pre-Push Gate

- [ ] Confirm that `https://github.com/aconsciousfractal/Endpoint-24-Affine-Defect-Boundary-Atlas.git` exists and is the intended public remote.
- [ ] Push `main`.
- [ ] Run `python -m pytest -q` and `python scripts/run_all_reproducibility_checks.py` from a clean clone or fresh checkout of the pushed repo.
- [ ] Create a release tag only after the pushed-checkout checks pass.