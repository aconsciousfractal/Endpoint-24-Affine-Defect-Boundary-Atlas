# Reproducing The Public Package Checks

This repository is a standalone public companion package for the
Endpoint-24 affine-defect boundary atlas paper.

## Environment

- Python 3.10+
- `pytest`
- A LaTeX distribution for rebuilding the paper

Install the Python test dependency:

```bash
pip install -r requirements.txt
```

Run the public test suite:

```bash
python -m pytest -q
```

Run the bundled public-package audit command:

```bash
python scripts/run_all_reproducibility_checks.py
```

This writes `results/public_package_check.json` and checks the public package
shape. It is intentionally lightweight: the full development workspace and raw
enumeration inputs are outside the public export.

## Paper Build

From `paper/` run:

```bash
pdflatex -interaction=nonstopmode -halt-on-error affine_defect_boundary_atlas.tex
bibtex affine_defect_boundary_atlas
pdflatex -interaction=nonstopmode -halt-on-error affine_defect_boundary_atlas.tex
pdflatex -interaction=nonstopmode -halt-on-error affine_defect_boundary_atlas.tex
```

## Main Artifact Map

| Paper layer | Canonical public artifacts |
|---|---|
| Source-backed tables | `paper/PAPER_SOURCE_BACKED_TABLES.json` |
| Endpoint and delta split | `results/DELTA_STRATIFICATION.json` |
| Direction and degree lemmas | `results/DIRECTION_LEMMA_CERTIFICATE.json`, `results/DEGREE_BOUND_CERTIFICATE.json` |
| First-principles defect spine | `results/STEP5PLUS_DELTA_DIM_FIRST_PRINCIPLES.json` |
| Error-fiber parity | `results/STEP9PLUS_ERROR_FIBER_PARITY.json` |
| B2/B3 finite boundary packages | `results/ITEM8D_B2_ENDPOINT_BOUNDARY_PACKAGE.json`, `results/ITEM8B_FREENESS_COUNT_REDUCTION.json` |
| Claim gate | `results/P6_final_verification_gate.json` |

## Scope Boundary

The scripts replay public-package checks and inspect curated artifacts. The
mathematical proof text and claim limits are in the paper and in `docs/`.
Development-only raw data and record-level exploratory outputs are deliberately
not part of this public package.