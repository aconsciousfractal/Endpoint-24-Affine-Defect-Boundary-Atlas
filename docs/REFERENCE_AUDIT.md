# Reference Audit

This file records the bibliography verification pass for the working paper.
Verification date: 2026-06-21.

The paper still treats the local finite certificates as the proof sources.  The
external literature supplies classical context, enumeration context, and
attribution targets.  In particular, the row/column nim-sum-zero statement is
not quoted as a theorem from an external source until the exact statement and
name origin are pinned down in that source; Step4 remains the operative proof.

## Verified Bibliographic Rows

| Key | Verification source | Checked metadata | Paper role | Claim status |
|---|---|---|---|---|
| `ollerenshawBondi` | Crossref DOI `10.1098/rsta.1982.0093` | title, authors, journal, volume `306`, issue `1495`, pages `443--532`, print date `1982-09-15` | classical order-four structure | context only for Nimm0 wording |
| `wardMagicVectorSpaces` | Crossref title/DOI lookup | title, author `James E. Ward`, journal, volume `53`, issue `2`, pages `108--111`, DOI `10.1080/0025570X.1980.11976839` | vector-space viewpoint | context |
| `sudberyTesseract` | Crossref title/DOI lookup | title, author, journal, volume `97`, issue `538`, pages `8--12`, DOI `10.1017/S0025557200005374` | Durer/tesseract viewpoint | context |
| `beckCohenCuomoGribelyukMagic` | Crossref title/DOI lookup | title, authors, journal, volume `110`, issue `8`, pages `707--717`, DOI `10.1080/00029890.2003.11920010` | general enumeration context | context |
| `beckVanHerick4x4Enumeration` | Crossref title/DOI lookup | title, authors, journal, volume `80`, issue `273`, pages `617--621`, DOI `10.1090/S0025-5718-10-02347-1` | order-four enumeration context | context |
| `takemura880` | arXiv page `2601.06131` | title, author, submitted `2026-01-05`, arXiv DOI `10.48550/arXiv.2601.06131`, primary class `math.GM` | modern 880-square computational context | preprint context |

## Corrections Made

- `ollerenshawBondi` issue corrected from `1490` to `1495`.
- `wardMagicVectorSpaces` expanded from initials-only metadata to Crossref DOI metadata.
- `sudberyTesseract` expanded with volume, issue, pages, and DOI.
- `takemura880` primary class corrected to `math.GM` and tagged as an arXiv preprint.

## Citation Guardrail

Use the external references for context only unless the manuscript quotes a
specific external theorem whose statement has been checked verbatim.  Current
paper wording must keep:

```text
The manuscript treats the Step4 finite derivation as the proof source; the
classical order-four literature supplies context rather than an unverified
quoted theorem.
```