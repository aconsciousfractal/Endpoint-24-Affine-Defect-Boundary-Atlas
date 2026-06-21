# Source Lock

`SOURCE_MAP.md` is the source of truth for export scope.  This file restates the
release lock in reviewer form.

## Public-Export Sources

These artifacts may appear in the public replay package or be cited directly as
paper-facing certificate summaries:

- `paper/REFERENCE_AUDIT.md`
- `paper/PAPER_SOURCE_BACKED_TABLES.json`
- `results/DELTA_STRATIFICATION.json`
- `results/DIRECTION_LEMMA_CERTIFICATE.json`
- `results/DEGREE_BOUND_CERTIFICATE.json`
- `results/LEMMA_B_LINE_XOR_DERIVATION.json`
- `results/STEP5PLUS_DELTA_DIM_FIRST_PRINCIPLES.json`
- `results/STEP9PLUS_ERROR_FIBER_PARITY.json`
- `results/STEP6PLUS_DEFECT_MASK_CLASSES.json`
- `results/STEP10PLUS_CLAUSE_FAMILIES.json`
- `results/ITEM8A_GLOBAL_TK_FREENESS_THEOREM.json`
- `results/ITEM8B_FREENESS_COUNT_REDUCTION.json`
- `results/ITEM8D_B2_ENDPOINT_BOUNDARY_PACKAGE.json`
- `results/ITEM9_COUNT60_COLLAPSE_KERNEL_GEOMETRY.json`
- `results/P6_final_verification_gate.json`

## Appendix-Only Sources

These may support a reviewer appendix but should not drive the main public
narrative:

- `docs/PAPER_FINAL_THEOREM_B1_B2_B3.md`
- `results/ITEM7_PAPER_LOCAL_ENDPOINT_TRANSPORT_PACKAGE.json`

## Development-Only Sources

These must stay local unless the export policy is deliberately widened:

- `data/order4_normal_essential_880.json`
- `results/L[0-9]*.json` and `results/L[0-9]*.md`
- record-level support/action payload rows inside large JSON artifacts
- `results/B3_BILINEAR_SUPPORT_ACTION.json`
- local LaTeX auxiliaries `*.aux`, `*.bbl`, `*.blg`, `*.log`, `*.out`

## Enforcement

`python -B scripts/generate_paper_public_package_manifest.py --write` parses
`SOURCE_MAP.md`, applies blocked-pattern checks, and fails on scope-policy
violations.  The B3 public matrix row must point to
`paper/PAPER_SOURCE_BACKED_TABLES.json`, not to record-level B3 payloads.