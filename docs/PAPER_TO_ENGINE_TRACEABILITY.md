# Paper To Engine Traceability

This file maps manuscript material to reproducible engine artifacts.

| Paper area | Engine/source artifact | Generator/check |
|---|---|---|
| Title, abstract, global claim boundary | `paper/CLAIM_BOUNDARY.md`, `docs/PUBLIC_CLAIM_BOUNDARY.md` | `tests/test_paper_workspace_scaffold.py` |
| Definitions and notation | `docs/NORMALIZATION_LOCK.md`, `paper/sections/02_model_and_notation.tex` | `tests/test_paper_workspace_scaffold.py` |
| Source-backed tables | `paper/PAPER_SOURCE_BACKED_TABLES.json`, `paper/generated/source_backed_tables.tex` | `scripts/generate_paper_source_backed_tables.py` |
| Endpoint split 236 = 144 + 32 + 60 | `results/DELTA_STRATIFICATION.json` | `tests/test_delta_stratification.py` |
| Direction lemma | `results/DIRECTION_LEMMA_CERTIFICATE.json` | `tests/test_direction_lemma_certificate.py` |
| Degree bound | `results/DEGREE_BOUND_CERTIFICATE.json` | `tests/test_degree_bound_certificate.py` |
| Lemma B / Nimm0 finite proof | `results/LEMMA_B_LINE_XOR_DERIVATION.json` | `tests/test_lemma_b_line_xor_derivation.py` |
| Defect/dimD theorem | `results/STEP5PLUS_DELTA_DIM_FIRST_PRINCIPLES.json` | `tests/test_step5plus_delta_dim_first_principles.py` |
| Error-fiber parity | `results/STEP9PLUS_ERROR_FIBER_PARITY.json` | `tests/test_step9plus_error_fiber_parity.py` |
| B3 defect-mask classes | `results/STEP6PLUS_DEFECT_MASK_CLASSES.json` | `tests/test_step6plus_defect_mask_classes.py` |
| B3 clause templates | `results/STEP10PLUS_CLAUSE_FAMILIES.json` | `tests/test_step10plus_clause_families.py` |
| Global T/K freeness | `results/ITEM8A_GLOBAL_TK_FREENESS_THEOREM.json` | `tests/test_item8_pre_tex_upgrades.py` |
| B3 count reduction 15 = 60 / 4 | `results/ITEM8B_FREENESS_COUNT_REDUCTION.json` | `tests/test_item8_pre_tex_upgrades.py` |
| B2 endpoint package | `results/ITEM8D_B2_ENDPOINT_BOUNDARY_PACKAGE.json` | `tests/test_item8_pre_tex_upgrades.py` |
| Count-60 collapse | `results/ITEM9_COUNT60_COLLAPSE_KERNEL_GEOMETRY.json` | `tests/test_item9_count60_collapse_kernel_geometry.py` |
| Intrinsic B3 column classification | `results/ITEM10_INTRINSIC_COLUMN_CLASSIFICATION.json` | `tests/test_item10_intrinsic_column_classification.py` |
| Defect-6 realizability obstruction | `results/ITEM11_DELTA6_REALIZABILITY_OBSTRUCTION.json` | `tests/test_item11_delta6_realizability_obstruction.py` |
| Public package manifest | `paper/PUBLIC_PACKAGE_MANIFEST.json` | `scripts/generate_paper_public_package_manifest.py`, `tests/test_paper_workspace_scaffold.py` |
| Workspace manifest | `paper/PAPER_WORKSPACE_MANIFEST.json` | `scripts/generate_paper_workspace_manifest.py`, `tests/test_paper_workspace_scaffold.py` |

## Replay Commands

The authoritative replay path is `REPRODUCE.md`.  If this traceability table and
`REPRODUCE.md` disagree, stop and update the package before export.