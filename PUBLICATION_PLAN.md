# Public Release Preparation Plan

Status: public-release candidate. Local staging checks pass; the remaining gate is a final clean-checkout red-team pass before pushing a public remote or creating a release tag.

## P0. Staging Folder

- [x] Create a standalone public-repo folder under `P:\GitHub_puba`.
- [x] Mirror the companion-repo layout: `paper/`, `docs/`, `results/`,
  `scripts/`, `tests/`, `data/`.
- [x] Copy only curated paper source/PDF, public-export artifacts, and
  appendix-only certificate support.
- [x] Exclude development-only raw data and LaTeX auxiliary files.

## P1. Naming And Presentation

- [x] Use the mathematical name `Endpoint-24 Affine-Defect Boundary Atlas`.
- [x] Keep old project branding out of public-facing text.
- [x] Remove draft-status language from the compiled paper title block.
- [ ] Re-run a final PDF visual pass after any title/metadata edits.

## P2. Release Metadata Gate

- [x] Finalize `LICENSE` with an explicit release choice.
- [x] Finalize `CITATION.cff` with publication metadata and preferred citation.
- [x] Re-run red-team after metadata changes.
- [x] Mark `public_export_ready` true in the public package manifest.

## P3. Reproducibility Gate

- [x] Add lightweight public-package checks.
- [x] Add pytest smoke checks for the public staging shape.
- [ ] Decide whether public replay should remain artifact-only or include adapted
  certificate-regeneration scripts.
- [ ] If adapted replay scripts are added, ensure they do not depend on private
  workspace paths or raw development-only inputs.

## P4. Paper Gate

- [x] Include source, generated tables, bibliography, and built PDF.
- [ ] Confirm all PDF floats and references after final rebuild.
- [ ] Confirm all claims are covered by `docs/CLAIM_LEDGER.md` and
  `docs/PROOF_OBLIGATIONS.md`.
- [ ] Keep stronger symbolic/general claims outside the paper unless proved.

## P5. Public Repository Gate

- [x] Initialize/inspect git repository state.
- [ ] Review `git status` before first commit.
- [ ] Make first public-prep commit after this clean package pass.
- [ ] Add remote and push only after the final red-team pass.
- [ ] Create release tag and archival DOI only after public package checks pass
  from a clean clone.

## Current Blockers

1. Run a final red-team pass from a clean checkout.\n2. Confirm the GitHub remote URL before first push.\n3. Create the first public commit/tag only after that final pass.