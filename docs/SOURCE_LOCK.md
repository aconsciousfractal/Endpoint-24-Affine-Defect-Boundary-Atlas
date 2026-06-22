# Source Lock

`SOURCE_MAP.md` is the source of truth for export scope. This file restates the
public companion package lock in reviewer form.

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

## Appendix-Only Certificate Support

These artifacts are bundled for reviewer/auditor support. The main manuscript
uses their derived public summaries through `paper/PAPER_SOURCE_BACKED_TABLES.json`
or the public-export rows above.

- `docs/PAPER_FINAL_THEOREM_B1_B2_B3.md`
- `results/ITEM7_PAPER_LOCAL_ENDPOINT_TRANSPORT_PACKAGE.json`
- `results/ITEM10_INTRINSIC_COLUMN_CLASSIFICATION.json`
- `results/ITEM11_DELTA6_REALIZABILITY_OBSTRUCTION.json`

## Development-Only Sources

These must stay out of the public package unless the export policy is deliberately widened:

- `data/order4_normal_essential_880.json`
- private staged certificate artifacts (not shipped)
- record-level support/action payload rows inside large JSON artifacts
- private B3 record-level support-action source (not shipped)
- local LaTeX auxiliaries `*.aux`, `*.bbl`, `*.blg`, `*.log`, `*.out`

## Enforcement

The public repo enforces this lock with `scripts/check_public_package.py` and
`tests/test_public_package.py`. The checker verifies declared public/appendix
artifacts, TeX inputs, forbidden development artifacts, old branding, and stale
release metadata. The B3 public matrix row must point to the sanitized summary
`paper/PAPER_SOURCE_BACKED_TABLES.json`, not to record-level B3 payloads.