# Paper Directory

This directory contains the manuscript source and built PDF for the public
companion repository.

Current title:

```text
Endpoint-24 Affine-Defect Boundary Atlas
```

## Layout

```text
affine_defect_boundary_atlas.tex  TeX entry point
affine_defect_boundary_atlas.pdf  built paper PDF
refs.bib                          bibliography
BUILD.md                          local TeX build notes
sections/                         TeX section files
generated/                        generated TeX tables/figures
figures/                          static/generated figure assets
PAPER_SOURCE_BACKED_TABLES.json   generated table/figure data summary
PUBLIC_PACKAGE_MANIFEST.json      public package manifest

SOURCE_MAP.md                     paper claims to source artifacts and export scope
REFERENCE_AUDIT.md                bibliography metadata/caveats
CLAIM_BOUNDARY.md                 allowed/blocked public wording
README_REVIEWER.md                reviewer entry point copy
REPRODUCE.md                      reproduction notes
CITATION.cff                      citation metadata copy
LICENSE                           MIT license copy
```

## Certified Anchors

- endpoint 24: `236` records and `59` free `T/K` orbits;
- exact affine core: `144` records, `36` orbits;
- B2 selected-affine boundary: `32` records, `8` orbits;
- B3 selected-non-affine boundary: `60` records, `15` orbits;
- B3 support-action matrix: `15` realized / `49` absent cells;
- count-60 collapse: `60 = 4 * (1+1+1+2+2+1+4+3)`;
- endpoint quotient kernel: `{delta 0:36, delta 4:16, delta 6:7}`.

## Guardrail

The manuscript may state finite certified, atlas-scoped theorems. It must not
claim a non-enumerative proof of the B3 count `60`, a full non-affine
classification, a full endpoint `23/27` classification, or public record-level widening
of record-level payloads.