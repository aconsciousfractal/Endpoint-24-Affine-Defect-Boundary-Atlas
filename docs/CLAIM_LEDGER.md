# Claim Ledger

This ledger assigns claim levels to the paper-facing claims.  Public wording
must not exceed this table.

| ID | Claim | Level | Source lock | Public status | Blocked escalation |
|---|---|---|---|---|---|
| C1 | Endpoint 24 has 236 records split as 144 + 32 + 60. | CL3 certified finite result | `results/DELTA_STRATIFICATION.json`, `paper/PAPER_SOURCE_BACKED_TABLES.json` | public with finite scope | universal endpoint classification |
| C2 | Endpoint 24 has 59 free T/K quotient orbits split as 36 + 8 + 15. | CL3 certified finite result | `results/ITEM8A_GLOBAL_TK_FREENESS_THEOREM.json`, `paper/PAPER_SOURCE_BACKED_TABLES.json` | public with finite scope | symbolic quotient classification |
| C3 | B2 has 32 records and 8 endpoint-boundary orbits under the selected-affine/cell-non-affine selector. | CL3 certified finite result | `results/ITEM8D_B2_ENDPOINT_BOUNDARY_PACKAGE.json` | public with finite scope | complete conceptual B2 theorem |
| C4 | B3 has 60 records and 15 endpoint transport orbits selected by selected-value non-affineness. | CL3 certified finite result | `results/ITEM7_PAPER_LOCAL_ENDPOINT_TRANSPORT_PACKAGE.json`, `results/ITEM8B_FREENESS_COUNT_REDUCTION.json` | finite endpoint theorem | non-enumerative count-60 proof |
| C5 | The B3 support-action matrix has 15 realized cells and 49 absent cells. | CL3 certified finite result | `paper/PAPER_SOURCE_BACKED_TABLES.json`, `results/STEP10PLUS_CLAUSE_FAMILIES.json` | public as finite matrix summary | first-principles derivation of the full matrix |
| C6 | Lemma B / Nimm0 line-xor zero is the operative finite proof, with literature used as context. | CL4 theorem import plus CL3 local finite proof | `results/LEMMA_B_LINE_XOR_DERIVATION.json`, `paper/REFERENCE_AUDIT.md` | public with attribution caveat | claiming the literature source was verified to use the exact local wording |
| C7 | The degree bound, defect/dimD dichotomy, and error-fiber parity provide the main internal theorem spine. | CL5 internal theorem / CL3 finite certificate | `results/DEGREE_BOUND_CERTIFICATE.json`, `results/STEP5PLUS_DELTA_DIM_FIRST_PRINCIPLES.json`, `results/STEP9PLUS_ERROR_FIBER_PARITY.json` | public with stated hypotheses | theorem beyond the locked normalization |
| C8 | The count-60 collapse reduces the debt to finite kernel and row-degree data. | CL3 certified finite result plus CLO obligation | `results/ITEM9_COUNT60_COLLAPSE_KERNEL_GEOMETRY.json` | public as debt reduction | symbolic proof of the count 60 |
| C9 | The eight B3 profile columns are intrinsic to `(signature, B)`. | CL3 certified finite result | `results/ITEM10_INTRINSIC_COLUMN_CLASSIFICATION.json` | appendix-backed finite claim | claiming the full 15/49 realization is first-principles |
| C10 | The defect-6 realization residue is a `13/35` integer-magic obstruction, not an F2/GL(4,2) law. | CL3 certified obstruction result | `results/ITEM11_DELTA6_REALIZABILITY_OBSTRUCTION.json` | appendix-backed boundary claim | claiming this derives the 15/49 matrix non-enumeratively |
| C11 | The public package is locally release-ready after finalized metadata, red-team closure, and passing package checks; first push/tag still requires remote confirmation and pushed-checkout checks. | CL1 release-status guardrail | `paper/PUBLIC_PACKAGE_MANIFEST.json`, `docs/RED_TEAM_REPORT.md` | public as local release status | claiming a pushed/tagged release before pushed-checkout checks |

## Claim-Level Rule

Finite replay and certified finite results can be public only with their bounded
scope.  They must not be promoted to universal or non-enumerative theorems unless
a separate proof is added and reviewed.