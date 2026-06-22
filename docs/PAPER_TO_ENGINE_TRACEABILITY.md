# Paper To Public Package Traceability

This file maps manuscript material to public companion artifacts and public
checks. It deliberately does not list private development generators or tests.

| Paper area | Public artifact(s) | Public check |
|---|---|---|
| Title, abstract, global claim boundary | `paper/CLAIM_BOUNDARY.md`, `docs/PUBLIC_CLAIM_BOUNDARY.md` | `scripts/check_public_package.py`, `tests/test_public_package.py` |
| Definitions and notation | `docs/NORMALIZATION_LOCK.md`, `paper/sections/02_model_and_notation.tex` | TeX input check in `scripts/check_public_package.py` |
| Source-backed tables | `paper/PAPER_SOURCE_BACKED_TABLES.json`, `paper/generated/source_backed_tables.tex` | manifest/source check in `scripts/check_public_package.py` |
| Endpoint split 236 = 144 + 32 + 60 | `results/DELTA_STRATIFICATION.json` | declared public artifact check |
| Direction lemma | `results/DIRECTION_LEMMA_CERTIFICATE.json` | declared public artifact check |
| Degree bound | `results/DEGREE_BOUND_CERTIFICATE.json` | declared public artifact check |
| Lemma B / Nimm0 finite proof | `results/LEMMA_B_LINE_XOR_DERIVATION.json` | declared public artifact check |
| Defect/dimD theorem | `results/STEP5PLUS_DELTA_DIM_FIRST_PRINCIPLES.json` | declared public artifact check |
| Error-fiber parity | `results/STEP9PLUS_ERROR_FIBER_PARITY.json` | declared public artifact check |
| B3 defect-mask classes | `results/STEP6PLUS_DEFECT_MASK_CLASSES.json` | declared public artifact check |
| B3 clause templates | `results/STEP10PLUS_CLAUSE_FAMILIES.json` | declared public artifact check |
| Global T/K freeness | `results/ITEM8A_GLOBAL_TK_FREENESS_THEOREM.json` | declared public artifact check |
| B3 count reduction 15 = 60 / 4 | `results/ITEM8B_FREENESS_COUNT_REDUCTION.json` | declared public artifact check |
| B2 endpoint package | `results/ITEM8D_B2_ENDPOINT_BOUNDARY_PACKAGE.json` | declared public artifact check |
| Count-60 collapse | `results/ITEM9_COUNT60_COLLAPSE_KERNEL_GEOMETRY.json` | declared public artifact check |
| Intrinsic B3 column classification | main-paper summary in `paper/PAPER_SOURCE_BACKED_TABLES.json`; appendix support in `results/ITEM10_INTRINSIC_COLUMN_CLASSIFICATION.json` | declared appendix artifact check |
| Defect-6 realizability obstruction | main-paper summary in `paper/PAPER_SOURCE_BACKED_TABLES.json`; appendix support in `results/ITEM11_DELTA6_REALIZABILITY_OBSTRUCTION.json` | declared appendix artifact check |
| Public package manifest | `paper/PUBLIC_PACKAGE_MANIFEST.json` | manifest consistency check |

## Replay Commands

The authoritative public replay path is `REPRODUCE.md`:

```powershell
python scripts/check_public_package.py
python -m pytest -q
python scripts/run_all_reproducibility_checks.py
```

If this traceability table and `REPRODUCE.md` disagree, stop and update the
package before publication.