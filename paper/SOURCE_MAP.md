# Paper Source Map

Every manuscript claim must point to one of these source artifacts before
public export.  The scope column controls what can be carried into the public
package.

Scope values:

- `public-export`: include in the public replay package or cite directly as a
  paper-facing certificate.
- `appendix-only`: usable as supplementary certificate material, but keep it
  out of the main public narrative unless a reviewer asks for the finite rows.
- `development-only`: keep local to `extensions/main`; cite only a derived
  public summary.

| Paper block | Source artifact | Role | Public wording | Scope |
|---|---|---|---|---|
| Bibliography audit | `paper/REFERENCE_AUDIT.md` | verified metadata and citation caveats | context only | public-export |
| Source-backed tables | `paper/PAPER_SOURCE_BACKED_TABLES.json` | public table/figure payload summary | finite-certified summary | public-export |
| Final theorem extraction | `docs/PAPER_FINAL_THEOREM_B1_B2_B3.md` | theorem/proof seed | paper-local | appendix-only |
| Endpoint-24 delta table | `results/DELTA_STRATIFICATION.json` | finite endpoint split | certified proposition | public-export |
| Direction lemma | `results/DIRECTION_LEMMA_CERTIFICATE.json` | selected-xor direction | certified proposition | public-export |
| Degree bound | `results/DEGREE_BOUND_CERTIFICATE.json` | `deg L <= 2` | certified proposition | public-export |
| Lemma B/Nimm0 finite proof | `results/LEMMA_B_LINE_XOR_DERIVATION.json` | row/column xor zero | finite proof with citation caveat | public-export |
| Step5+ dichotomy | `results/STEP5PLUS_DELTA_DIM_FIRST_PRINCIPLES.json` | first-principles defect spine | theorem/lemma | public-export |
| Step9+ parity | `results/STEP9PLUS_ERROR_FIBER_PARITY.json` | first-principles error fibers | theorem/lemma | public-export |
| B3 matrix | `paper/PAPER_SOURCE_BACKED_TABLES.json` | `15/49` finite matrix summary | certified proposition | public-export |
| B3 intrinsic/residue split | `results/STEP6PLUS_DEFECT_MASK_CLASSES.json` | six intrinsic classes plus two splits | certified proposition | public-export |
| B3 clause templates | `results/STEP10PLUS_CLAUSE_FAMILIES.json` | NF1/NF2/NF3 templates | theorem/lemma for templates | public-export |
| B3 endpoint transport | `results/ITEM7_PAPER_LOCAL_ENDPOINT_TRANSPORT_PACKAGE.json` | carrier orbits and payload | paper-local finite theorem | appendix-only |
| Global `T/K` freeness | `results/ITEM8A_GLOBAL_TK_FREENESS_THEOREM.json` | free quotient | finite theorem | public-export |
| B3 count reduction | `results/ITEM8B_FREENESS_COUNT_REDUCTION.json` | `15=60/4` | certified proposition | public-export |
| B3 selector probe | `results/ITEM8C_SELECTOR_DECOUPLING_PROBE.json` | finite selector probe with record-level fields | finite selector | development-only |
| B2 endpoint package | `results/ITEM8D_B2_ENDPOINT_BOUNDARY_PACKAGE.json` | B2 `32/8` package | finite theorem | public-export |
| Count-60 collapse | `results/ITEM9_COUNT60_COLLAPSE_KERNEL_GEOMETRY.json` | kernel and row-degree reduction | finite certified debt reduction | public-export |
| Intrinsic B3 column classification | `results/ITEM10_INTRINSIC_COLUMN_CLASSIFICATION.json` | 8/8 column profile classification by `(signature, M)` | certified column refinement | appendix-only |
| Defect-6 realizability obstruction | `results/ITEM11_DELTA6_REALIZABILITY_OBSTRUCTION.json` | `13/35` arithmetic realization cut and no linear symmetry | certified obstruction boundary | appendix-only |
| Claim boundary | `results/P6_final_verification_gate.json` | blocked/allowed claims | mandatory guardrail | public-export |

## Development-Only Inputs

The following files are not paper-facing source rows.  They may be used to
regenerate local certificates, but the public package should expose only their
paper-safe derived summaries unless the export policy is deliberately widened.

| Development artifact | Reason |
|---|---|
| `data/order4_normal_essential_880.json` | raw essential-square universe; not cited directly by the manuscript |
| `results/L[0-9]*.json` and `results/L[0-9]*.md` | exploratory/intermediate levels superseded by the named paper-facing certificates |
| record-level support/action payload rows inside large JSON artifacts | useful for audit, not needed for main public claims |
| `results/B3_BILINEAR_SUPPORT_ACTION.json` | large support-action source with record-level rows; public paper uses `paper/PAPER_SOURCE_BACKED_TABLES.json` summary |
| local LaTeX auxiliaries `*.aux`, `*.bbl`, `*.blg`, `*.log`, `*.out` | build outputs, not source |

## Public Export Rule

The public package should contain only artifacts needed to replay the
paper-facing claims: TeX source, bibliography, source map, claim boundary,
reference audit, source-backed table summaries, tests, and the small certificate
JSON rows marked `public-export`.  `appendix-only` artifacts may be bundled as a
separate certificate appendix.  `development-only` artifacts stay in
`extensions/main`.

Next task: run human license/citation review for public export.