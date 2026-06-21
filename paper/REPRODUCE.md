# Reproduce The Paper Build

This file records the paper-local build and package checks for the public
companion repository. The top-level `REPRODUCE.md` is the primary public entry
point.

## Build The Paper

From `paper/` run:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error affine_defect_boundary_atlas.tex
bibtex affine_defect_boundary_atlas
pdflatex -interaction=nonstopmode -halt-on-error affine_defect_boundary_atlas.tex
pdflatex -interaction=nonstopmode -halt-on-error affine_defect_boundary_atlas.tex
```

Expected output:

```text
paper/affine_defect_boundary_atlas.pdf
```

The current public package ships a built 10-page PDF.

## Public Package Checks

From the repository root:

```powershell
python scripts/check_public_package.py
python -m pytest -q
python scripts/run_all_reproducibility_checks.py
```

The public checks validate the curated package shape and source-map artifacts.
They do not regenerate the full development workspace or raw enumerations.

## Scope Classes

`paper/SOURCE_MAP.md` is the source of truth for export scope.

- `public-export`: allowed in the public replay package or directly cited as a
  paper-facing certificate.
- `appendix-only`: allowed as supplementary certificate material, but not as the
  main public narrative.
- `development-only`: stays out of the public package; the public package may
  cite only derived safe summaries.

`paper/PUBLIC_PACKAGE_MANIFEST.json` records those scope classes.