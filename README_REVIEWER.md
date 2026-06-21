# Reviewer Readme

This is the reviewer entry point for the Endpoint-24 Affine-Defect Boundary Atlas
public companion package.

## Recommended Review Path

1. Read `docs/PUBLIC_CLAIM_BOUNDARY.md` before quoting any claim.
2. Read `docs/CLAIM_LEDGER.md` for the claim level and source of each result.
3. Read `docs/SOURCE_LOCK.md` and `docs/NORMALIZATION_LOCK.md` before checking
   formulas or tables.
4. Run the commands in `REPRODUCE.md`.
5. Check `docs/PROOF_OBLIGATIONS.md` for open symbolic debts.
6. Read `docs/RED_TEAM_REPORT.md` before publication.
7. Use `docs/PAPER_TO_ENGINE_TRACEABILITY.md` to connect manuscript sections to
   scripts, JSON certificates, and tests.

## Current Status

- Manuscript: `paper/affine_defect_boundary_atlas.pdf`.
- Replay target: finite, paper-local endpoint-24 affine-defect atlas.
- Public export: release candidate; final push/tag requires a clean-checkout
  red-team pass.
- License/citation: finalized as MIT / `CITATION.cff` for this release candidate.

## Main Guardrail

The package supports finite-certified and paper-local statements. It does not
claim a non-enumerative proof of the B3 count `60`, a full non-affine
classification, or a universal theorem for all endpoint-24 order-four
magic-square behavior.