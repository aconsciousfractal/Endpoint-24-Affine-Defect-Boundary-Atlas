# Proof Obligations

This file separates closed finite/theorem items from open symbolic debts.

## Closed For The Current Paper Scope

| ID | Obligation | Status | Source |
|---|---|---|---|
| PO-1 | Reproduce endpoint-24 finite split 236 = 144 + 32 + 60. | closed finite certificate | `results/DELTA_STRATIFICATION.json` |
| PO-2 | Certify line-xor zero / Lemma B in the local finite system. | closed finite proof | `results/LEMMA_B_LINE_XOR_DERIVATION.json` |
| PO-3 | Derive degree bound and defect/dimD dichotomy under locked hypotheses. | closed theorem/certificate | `results/DEGREE_BOUND_CERTIFICATE.json`, `results/STEP5PLUS_DELTA_DIM_FIRST_PRINCIPLES.json` |
| PO-4 | Derive the error-fiber parity bridge. | closed theorem/certificate | `results/STEP9PLUS_ERROR_FIBER_PARITY.json` |
| PO-5 | Reproduce B2 endpoint-boundary 32 records / 8 orbits. | closed finite certificate | `results/ITEM8D_B2_ENDPOINT_BOUNDARY_PACKAGE.json` |
| PO-6 | Reproduce B3 15 orbit / 60 record endpoint transport. | closed finite endpoint certificate | `results/ITEM7_PAPER_LOCAL_ENDPOINT_TRANSPORT_PACKAGE.json` |
| PO-7 | Reproduce B3 15/49 support-action matrix from safe public summary. | closed finite certificate | `paper/PAPER_SOURCE_BACKED_TABLES.json` |
| PO-8 | Certify that the eight B3 profile columns are intrinsic to `(signature, B)`. | closed finite certificate | `results/ITEM10_INTRINSIC_COLUMN_CLASSIFICATION.json` |
| PO-9 | Localize the remaining defect-6 realization residue and rule out F2/linear closure. | closed obstruction certificate | `results/ITEM11_DELTA6_REALIZABILITY_OBSTRUCTION.json` |
| PO-10 | Finalize release license/citation metadata and public-package red-team. | closed release gate | `LICENSE`, `CITATION.cff`, `docs/RED_TEAM_REPORT.md` |
| PO-11 | Publish summary-only full endpoint aggregate controls without widening the endpoint-24 theorem. | closed finite aggregate control | `results/FULL_ENDPOINT_CONTROL_ATLAS.json` |

## Open Or Blocked Mathematical Scope

| ID | Obligation | Public handling |
|---|---|---|
| OO-1 | Non-enumerative symbolic proof of the B3 count 60. | open; do not claim |
| OO-2 | Non-enumerative first-principles derivation of the full B3 15/49 matrix. | open; do not claim; the defect-6 realizability obstruction explains why the remaining cut is integer-arithmetic, not F2-linear |
| OO-3 | Full B3 non-affine classification beyond the saved endpoint-24 atlas. | blocked; do not claim |
| OO-4 | Full endpoint 23/27 classification. | blocked; do not claim |
| OO-5 | Conceptual classification of every endpoint or public full-payload all-endpoint atlas. | blocked; do not claim in this paper |

## Release Rule

Open mathematical obligations may be discussed only as open obligations. They
cannot be used as theorem premises or as public completion claims.