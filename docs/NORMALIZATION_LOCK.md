# Normalization Lock

This file fixes the notation and indexing used by the manuscript, generated
tables, and tests.

## Cell And Label Model

- Cells are indexed by `F_2^4`.
- Row bits are the first two coordinates and column bits are the last two
  coordinates in the local scripts.
- Cell labels use `value - 1`, so square values 1..16 become labels 0..15.
- The endpoint-24 selected values are values in the high block containing 11.

## Affine Interpolation And Error

- `A` is the affine interpolation of `L` on the fixed anchor frame `{0,e1,e2,e3,e4}`.
- `L` is the label map of the square.
- `E = L + A` over `F_2` is the affine-interpolation error.
- `D` is the span of the bilinear error coefficient directions.
- `delta = |support(E)|` and the certified dichotomy is `delta in {0,4,6}` with
  `dim D in {0,1,2}` under the locked hypotheses.

## Branch Labels

- Exact affine core: selected-value affine, selected-mask affine, cell-value
  affine.
- B2: selected-value affine, selected-mask affine, cell-value non-affine.
- B3: selected-value non-affine, selected-mask non-affine, cell-value
  non-affine.

## Transport And Matrix Conventions

- `T/K` is the finite quotient transport group certified as free in the locked
  endpoint atlas.
- B3 signatures are the eight non-affine 4-subsets of selected values containing
  11.
- B3 defect-mask profiles are the eight support-action column profiles used in
  the `15/49` matrix.
- Matrix entry `1` means realized under the finite support-action certificate;
  `.` means absent by the locked clause-failure classification.

## Forbidden Normalization Drift

Do not change value labels, selected-mask convention, endpoint definition,
`delta`, `D`, branch labels, or T/K quotient meaning without regenerating the
source-backed tables, manifests, and regressions.