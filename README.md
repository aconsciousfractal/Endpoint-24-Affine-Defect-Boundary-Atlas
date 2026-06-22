# Endpoint-24 Affine-Defect Boundary Atlas

Public companion repository for the paper:

```text
Endpoint-24 Affine-Defect Boundary Atlas
```

Author: Oleksiy Babanskyy

This repository contains the paper source/PDF, curated finite-certificate
artifacts, claim-boundary documentation, and public sanity checks for the
Endpoint-24 affine-defect boundary atlas. It is a public companion package, not
a dump of the development workspace.

## Status

Published public companion repository. The release tag `v1.0.1` has been created after local and clean-clone public-package checks.

## Layout

```text
paper/      manuscript source, PDF, bibliography, generated tables, build notes
docs/       claim ledger, proof obligations, source locks, red-team notes
results/    curated public-export and appendix-only JSON certificate artifacts
scripts/    public package sanity/reproducibility checks
tests/      pytest checks for the public package
data/       intentionally empty unless a curated public input is later approved
```

## Quick Check

```bash
python -m venv .venv
pip install -r requirements.txt
python -m pytest -q
```

Windows activation, if needed:

```powershell
.venv\Scripts\activate
```

Linux / macOS activation, if needed:

```bash
source .venv/bin/activate
```

The checks are public-package guardrails. They verify that the curated release
shape is intact, that blocked development artifacts are absent, and that the
paper metadata/PDF are present. They do not replace the mathematical arguments
or the finite certificates cited in the paper.

To write a machine-readable public-package report:

```bash
python scripts/run_all_reproducibility_checks.py
```

The report is written to `results/public_package_check.json`.

## Paper

The paper lives in `paper/`:

```text
paper/affine_defect_boundary_atlas.tex
paper/refs.bib
paper/affine_defect_boundary_atlas.pdf
paper/BUILD.md
```

Build instructions are in `paper/BUILD.md`.

## Release Boundary

The package manifest is `paper/PUBLIC_PACKAGE_MANIFEST.json`. It separates
public-export artifacts, appendix-only certificate support, and development-only
inputs that must not be published. See `docs/SOURCE_MAP.md` and
`docs/PUBLIC_CLAIM_BOUNDARY.md` before changing scope.

## Citation And License

See `CITATION.cff` for citation metadata. This repository is released under the MIT license; see `LICENSE`. Unless otherwise stated, the paper source, scripts, curated certificate artifacts, and public package documentation are covered by that license.