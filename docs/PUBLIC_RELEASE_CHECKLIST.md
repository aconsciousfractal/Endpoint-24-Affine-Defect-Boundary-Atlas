# Public Release Checklist

Use this checklist before publishing the repository or creating a release tag.

## Must Pass

- [ ] `python -m pytest -q`
- [ ] `python scripts/run_all_reproducibility_checks.py`
- [ ] Manual PDF inspection: title page, pages 8-9, references, tables, captions.
- [ ] Text scan: no old branding, no draft label, no hard-coded stale test count.
- [ ] Scope scan: no raw development-only JSON, no record-level exploratory dumps.
- [ ] Claim scan: no unproved symbolic/generalized statements beyond the stated
  finite-certified boundary.

## Human Decisions

- [x] License finalized.
- [x] Citation metadata finalized.
- [ ] Repository name confirmed.
- [ ] Release notes drafted.
- [ ] Public remote visibility approved.

## After Publication

- [ ] Test clean clone.
- [ ] Archive release artifact if desired.
- [ ] Update paper citation if DOI or repository URL changes.