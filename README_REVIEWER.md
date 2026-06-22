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
- Replay target: finite endpoint-24 affine-defect atlas, with a summary-only full endpoint aggregate control artifact as context.
- Public export: published public companion repository; tag `v1.0.1` has passed local and clean-clone package checks.
- License/citation: finalized as MIT / `CITATION.cff` for this public package.

## Main Guardrail

The package supports finite-certified and endpoint-24 finite statements. It does not
claim a non-enumerative proof of the B3 count `60`, a full non-affine
classification, or a universal theorem for all endpoint-24 order-four
magic-square behavior.