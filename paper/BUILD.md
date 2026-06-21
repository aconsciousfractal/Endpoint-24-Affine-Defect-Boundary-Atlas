# Building The Paper

From this directory:

```bash
pdflatex -interaction=nonstopmode -halt-on-error affine_defect_boundary_atlas.tex
bibtex affine_defect_boundary_atlas
pdflatex -interaction=nonstopmode -halt-on-error affine_defect_boundary_atlas.tex
pdflatex -interaction=nonstopmode -halt-on-error affine_defect_boundary_atlas.tex
```

Known build target:

```text
engine: pdfLaTeX
primary source: affine_defect_boundary_atlas.tex
bibliography: refs.bib
current status: 10-page PDF builds from the public companion source tree
```

The TeX style uses standard `article`, theorem/proposition/certified-proposition
environments, explicit finite-certificate language, and a separate claim
boundary.

Before first public push/tag from a fresh checkout:

```powershell
python -m pytest -q
python scripts/run_all_reproducibility_checks.py
```

Keep TeX, PDF, manifests, and public package tests synchronized.