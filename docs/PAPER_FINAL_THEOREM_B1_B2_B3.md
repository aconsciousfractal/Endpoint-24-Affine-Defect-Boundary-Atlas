# Paper Final Theorem B1/B2/B3

Status: Public appendix theorem/proof seed. It records the paper-local finite theorem and is bundled for reviewer audit; it is not the source of truth for public replay scope.

Public source note:

- The public source map is `docs/SOURCE_MAP.md` / `paper/SOURCE_MAP.md`.
- Private draft docs and record-level support-action payloads are not shipped.
- The public B3 matrix is the sanitized summary in `paper/PAPER_SOURCE_BACKED_TABLES.json`.

Claim boundary: paper-local finite theorem only.  No public record-level widening, no
universal Endpoint-24 affine-defect atlas claim, no record-level payload promotion, no full endpoint
23/27 classification, no complete B2 conceptual theorem, no full B3 non-affine
classification, and no non-enumerative first-principles proof of the B3
support-action multiplicity matrix.  Step5+ and Step9+ are first-principles
structural upgrades; Step10+ proves the B3 clause templates; and Item10 closes
the B3 column-profile classification intrinsically as a function of
`(signature, M)`.  Item7-I and Item7-J add the endpoint transport package:
selected-value non-affine is the exact finite B3 endpoint selector in the L8
endpoint-24 T/K quotient, and its 15 orbits are exactly the Item7-H
lower-geometry transport atoms.  Item8-A names the global T/K freeness theorem;
Item8-B makes explicit that the B3 quotient count is `15 = 60/4`; Item8-C
decouples the B3 record-level selector from orbit enumeration; Item8-D adds the
parallel B2 endpoint boundary package; Item9 collapses the count-60 debt to the
finite endpoint kernel and row-degree pattern without claiming a symbolic count
proof; and Item11 proves the remaining defect-6 realization residue is
integer-magic rather than F2-linear.

## LaTeX Preamble Snippet

```latex
\newcommand{\F}{\mathbb F}
\newcommand{\A}{\mathcal A}
\newcommand{\Derr}{\mathcal D}
\newcommand{\supp}{\operatorname{supp}}
\newcommand{\TK}{T/K}
```

## Statement

```latex
\begin{theorem}[Affine-defect boundary atlas, paper-local form]\label{thm:b123-affine-defect-boundary}
Inside the certified Endpoint-24 affine-defect atlas extension atlas, consider square-mask pairs in the
bounded one-incidence model.  Quotient statements are taken modulo the verified
D4 essential representatives and the verified free \(\TK\)-action of L7.
Then the following finite assertions hold.
\begin{enumerate}
  \item Endpoint \(24\) has exactly \(236\) records and \(59\) free
        \(\TK\)-orbits.  Item8-A packages this as a named global
        \(\TK\cong V_4\) freeness theorem, giving \(236=59\cdot4\).
  \item The affine defect \(\delta\) takes only the values \(0,4,6\); on
        endpoint \(24\) the record split is \(144/64/28\).
  \item The exact affine/V4 core is the cell
        \((\text{selected affine},\delta=0)\), with \(144\) records and
        \(36\) \(\TK\)-orbits.
  \item The selected-affine boundary B2 is the cell
        \((\text{selected affine},\delta=4)\), with \(32\) records and
        \(8\) \(\TK\)-orbits, finite-closed at the P3 boundary theorem level.
        Item8-D packages B2 by the endpoint selector
        \(\texttt{selected\_value\_affine\_and\_cell\_value\_nonaffine}\),
        matching the eight P3 canonicalized boundary components.
  \item The non-affine boundary B3 is the cell
        \((\text{selected non-affine},\delta\in\{4,6\})\), with \(60\)
        records and \(15\) \(\TK\)-orbits.  Its support-action matrix has
        \(64\) signature/profile candidate cells, exactly \(15\) realized
        cells, exactly \(49\) absent cells, and no classification errors
        against the Step6 bilinear support-action certificate.  Step5+ proves
        the \((\delta,\dim D)\) dichotomy atlas-independently for degree-at-most
        two bijections of \(\F_2^4\), and Step9+ makes the error-fiber parity
        bridge first-principles.  Step6+ is the original defect-mask split
        certificate, and Item10 sharpens it to an 8/8 intrinsic column
        classification by `(signature, M)`; Step10+ proves the NF1/NF2/NF3
        clause templates.
        Item7-I/J package the endpoint transport theorem: inside the endpoint-24
        \(T/K\) quotient, selected-value non-affineness selects exactly the
        \(15\) B3 carrier orbits, and these are precisely the lower-geometry
        transport atoms carrying the support-action payload.  Item8-B/C refine this
        statement: \(15=60/4\) follows from freeness, and the finite record-level
        B3 selector is selected xor nonzero before quotienting.
        Item9 collapses the remaining count-60 debt to the finite endpoint kernel
        \(\delta=0,4,6\mapsto36,16,7\), the B3 row-degree pattern
        \(1,1,1,2,2,1,4,3\), and the diagonal-plane avatar
        \(\delta=0,4,6\leftrightarrow24,8,0\).  Item10 then upgrades the
        column side: all eight B3 profile columns are intrinsic to
        \((S,M)\), using \(\delta\), the zero pattern of \(M\), and
        \(D=\operatorname{span}(M)\).  Item11 locates the remaining realization
        residue at defect six: integer magic realizes exactly \(13\) of the
        \(35\) two-dimensional error spaces; all \(35\) are F2-completable and
        the realized \(13\)-set has trivial \(GL(4,2)\) stabilizer.
  \item Endpoints \(23\) and \(27\) are absent from the affine selected-plane
        layer B1 by the four-point xor criterion.  This is a scoped relative
        absence theorem, not a full endpoint-23/27 classification.
\end{enumerate}
\end{theorem}
```

## Proof

```latex
\begin{proof}
Index cells by \(\F_2^4\) and use value-minus-one labels in \(\F_2^4\).  Let
\(L:\F_2^4\to\F_2^4\) be the label map of a normal order-4 magic square.  Let
\(A\) be the affine interpolation of \(L\) on \(\{0,e_1,e_2,e_3,e_4\}\), and set
\[
  E=L+A, \qquad \delta=|\supp(E)|.
\]
Here addition is in characteristic two.  Step2 certifies from the raw essential
squares that endpoint \(24\) has the \(\delta\)-split \(144/64/28\), and that
the pair consisting of selected-value affineness and \(\delta\) gives the
endpoint-24 cross-table.

Step3+ and Step4 derive the degree bound.  Theorem A says that row and column
line-xor zero imply \(\deg L\le 2\).  The line-xor input is the
order-four nim-sum (``Nimm0/Lemma B'') property: written in label units
\(0..15\), every row and column of a normal order-four magic square has nim-sum
(xor) zero.  This
is a known structural feature of order-four magic squares, to be read against the
classical structural literature~\cite{ollerenshawBondi,wardMagicVectorSpaces}
and the binary-tesseract viewpoint~\cite{sudberyTesseract}.  We do not rely on
that literature as a proof source: Step4 gives an independent, self-contained
finite derivation, verifying Lemma B on all \(7040\) normal magic squares by a
row-pair certificate generated directly from the row, column, and diagonal sum
constraints (no saved atlas).  Thus \(E\) is quadratic after subtracting \(A\).

\paragraph{Attribution note (to confirm before submission).}
The references above are the standard structural sources for order-four magic
squares and the natural home for the nim-sum property, but the precise
bibliographic statement of ``rows and columns have nim-sum zero'' should be
verified in~\cite{ollerenshawBondi} (or the originating source of the
``Nimm0'' name) before it is attributed as a quoted theorem; absent that
confirmation, the in-paper status of Lemma B is the self-contained Step4 finite
derivation.

Step5 proves the stronger bilinear form.  The pure row-pair and pure column-pair
quadratic coefficients vanish, so
\[
  E(r,c)=B_{11}r_1c_1+B_{10}r_1c_0+B_{01}r_0c_1+B_{00}r_0c_0.
\]
The \(2\times2\) coefficient matrix has one rank-one side for every normal
magic square.  Consequently \(\delta=0,4,6\) exactly as \(\dim\Derr=0,1,2\),
where \(\Derr\) is the span of the bilinear coefficient vectors.  Step5+ upgrades
the one-dependent-side input from an atlas fact to Lemma C: a GL(4,2)-symmetry
complete finite proof shows that every degree-at-most-two bijection of
\(\F_2^4\) has \(\dim\Derr\le2\) and hence the same \((\delta,\dim D)\)
dichotomy.  The corner identity
\(B_{11}+B_{10}+B_{01}+B_{00}=0\) is a magic refinement, not part of Lemma C.

Step9+ records the error-fiber parity bridge.  The Step5+ factorization gives an
atlas-independent error-fiber shape.  If \(\delta=4\), then
\(\Derr=\{0,u\}\) and \(E=u\) on its four-cell support \(\Sigma\), so for the
selected mask \(M\),
\[
  \bigoplus_{c\in M}L(c)=u\cdot(|M\cap\Sigma|\bmod 2).
\]
If \(\delta=6\), the three nonzero fibers \(\Sigma_u,\Sigma_v,\Sigma_{u+v}\)
contribute the selected xor by their parities:
\[
  \bigoplus_{c\in M}L(c)=
  (|M\cap\Sigma_u|\bmod2)u+
  (|M\cap\Sigma_v|\bmod2)v+
  (|M\cap\Sigma_{u+v}|\bmod2)(u+v).
\]

For four distinct selected labels in \(\F_2^4\), the selected set is an affine
plane if and only if its xor is zero.  On endpoint \(24\), this selected-xor
axis separates the exact affine row, the B2 selected-affine extras, and the B3
non-affine records.  L7 supplies the verified free \(\TK\cong V_4\) action,
preserving endpoints and giving four records per quotient orbit.  Item8-A names this
as the global \(\TK\cong V_4\) freeness theorem: all \(7040\) square-mask pairs
form \(1760\) free quotient orbits, and endpoint 24 satisfies \(236=59\cdot4\).
Therefore the endpoint-24 quotient split is \(36+8+15=59\).

The B2 cell \((\text{selected affine},\delta=4)\) is finite-closed by the P3 B2
boundary theorem, and Step9+ shows it is the even-intersection side of the
\(\delta=4\) error support.  Item8-D adds the endpoint package: the selector
\(\texttt{selected\_value\_affine\_and\_cell\_value\_nonaffine}\) selects
\(8\) free quotient orbits and \(32\) records, matching the eight P3
canonicalized B2 components.  The \(\delta=4\) part of B3 is the odd-intersection
side of the same support, while the \(\delta=6\) part is governed by the
three-fiber parity formula above.  For the remaining B3 support-action
multiplicity, Step6 recomputes each B3 error support from the Step5 bilinear
matrix, quotients by L7 \(\TK\)-transport, groups by defect-mask support gates,
and verifies that the \(13\) compressed support-action clauses reproduce the
\(15/49\) support-action matrix exactly.  Step6+ first isolated the eight defect-mask columns into intrinsic classes plus
apparent mask-transport splits.  Item10 sharpens that statement: all eight
columns are intrinsic to the selected signature and bilinear matrix \(M\).  The
old \(DM01/DM02\) split is the zero-pattern dichotomy of \(M\) (uniform
\(xJ\) versus one zero side), and the \(DM04/DM06\) split is separated by
\(D=\operatorname{span}(M)\).  Step10+ then proves the three clause templates:
defect-4 singleton xor error, defect-6 non-xor pair support, and defect-6
non-xor triple support.  This gives \(60\) B3 records, \(15\) B3 \(\TK\)-orbits,
\(15\) realized cells, \(49\) absent cells, and zero false positives or false
negatives.  Item11 explains the remaining boundary: the 15/49 realization
pattern is finite-certified because the defect-6 arithmetic cut realizes
\(13\) of \(35\) two-flats, even though all \(35\) are F2-completable and no
linear symmetry selects the realized set.

Item7-I/J add the endpoint transport formulation needed for the final paper
package.  In the L8 endpoint-24 \(\TK\)-quotient, the selector
\(\texttt{selected\_value\_nonaffine}\) is exact: it selects \(15\) quotient
orbits and \(60\) records, with no false positive, no false negative, and no
partial orbit.  Item7-I then matches these \(15\) endpoint orbits bijectively
with the Item7-H lower-geometry transport atoms \(\texttt{STEP6-SA01}\) through
\(\texttt{STEP6-SA15}\), attaching the defect split \(8+7\), the eight
signature multiplicities, and the relation-code payload.  This is the
paper-local finite endpoint theorem used for export; it is not a symbolic proof
that the non-affine endpoint state must have exactly \(15\) quotient orbits.

Item8-B then reduces the finite B3 quotient count to freeness: \(15=60/4\).
Item8-C records the stronger provenance boundary: over the Step2 record-level
delta stratification, B3 is selected exactly by nonzero selected xor before any
quotient orbit count is used.  The count \(60\) remains finite-certified rather
than symbolically derived.
Item9 then records the count-60 collapse:
\(60=4(1+1+1+2+2+1+4+3)\), the endpoint quotient kernel
\(\delta=0,4,6\mapsto36,16,7\), and the finite diagonal-plane avatar
\(\delta=0,4,6\leftrightarrow24,8,0\).  The count \(60\) and the
kernel counts remain finite-certified rather than symbolically derived.
Item10 closes the column-classification residue by proving that the eight B3
columns are intrinsic to \((S,M)\).  Item11 then proves that the remaining
realization residue is not an F2 or linear-algebraic theorem: among the \(35\)
defect-6 two-flats, integer magic realizes \(13\), all \(35\) are
bijection-completable under Lemma C, and the \(GL(4,2)\) stabilizer of the
realized \(13\)-set is trivial.
Finally, P2 gives the B1 scoped corollary for endpoints \(23\) and \(27\):
their selected signatures have nonzero xor, while every L1 selected plane has
zero xor.  This proves the stated paper-local finite theorem.
\end{proof}
```

## Public Certificate Table

This public appendix lists only artifacts shipped in this repository. Private draft docs, record-level payloads, and development-only tests are intentionally not public replay dependencies.

| Claim block | Public artifact | Public verification |
|---|---|---|
| Endpoint-24 delta split and two-invariant table | `results/DELTA_STRATIFICATION.json` | `scripts/check_public_package.py`; `tests/test_public_package.py` |
| Direction lemma | `results/DIRECTION_LEMMA_CERTIFICATE.json` | `scripts/check_public_package.py`; `tests/test_public_package.py` |
| Degree bound | `results/DEGREE_BOUND_CERTIFICATE.json` | `scripts/check_public_package.py`; `tests/test_public_package.py` |
| Lemma B line-xor derivation | `results/LEMMA_B_LINE_XOR_DERIVATION.json` | `scripts/check_public_package.py`; `tests/test_public_package.py` |
| Atlas-independent defect/dimD dichotomy | `results/STEP5PLUS_DELTA_DIM_FIRST_PRINCIPLES.json` | `scripts/check_public_package.py`; `tests/test_public_package.py` |
| Error-fiber parity bridge | `results/STEP9PLUS_ERROR_FIBER_PARITY.json` | `scripts/check_public_package.py`; `tests/test_public_package.py` |
| B3 public support-action matrix summary | `paper/PAPER_SOURCE_BACKED_TABLES.json` | `scripts/check_public_package.py`; `tests/test_public_package.py` |
| B3 defect-mask intrinsic/residue split | `results/STEP6PLUS_DEFECT_MASK_CLASSES.json` | `scripts/check_public_package.py`; `tests/test_public_package.py` |
| B3 clause-template families | `results/STEP10PLUS_CLAUSE_FAMILIES.json` | `scripts/check_public_package.py`; `tests/test_public_package.py` |
| B3 paper-local endpoint transport package | `results/ITEM7_PAPER_LOCAL_ENDPOINT_TRANSPORT_PACKAGE.json` | `scripts/check_public_package.py`; `tests/test_public_package.py` |
| Global T/K freeness theorem | `results/ITEM8A_GLOBAL_TK_FREENESS_THEOREM.json` | `scripts/check_public_package.py`; `tests/test_public_package.py` |
| B3 freeness count reduction | `results/ITEM8B_FREENESS_COUNT_REDUCTION.json` | `scripts/check_public_package.py`; `tests/test_public_package.py` |
| B2 endpoint boundary package | `results/ITEM8D_B2_ENDPOINT_BOUNDARY_PACKAGE.json` | `scripts/check_public_package.py`; `tests/test_public_package.py` |
| Count-60 collapse/kernel geometry | `results/ITEM9_COUNT60_COLLAPSE_KERNEL_GEOMETRY.json` | `scripts/check_public_package.py`; `tests/test_public_package.py` |
| Intrinsic B3 column classification | `results/ITEM10_INTRINSIC_COLUMN_CLASSIFICATION.json` | `scripts/check_public_package.py`; `tests/test_public_package.py` |
| Defect-6 realizability obstruction | `results/ITEM11_DELTA6_REALIZABILITY_OBSTRUCTION.json` | `scripts/check_public_package.py`; `tests/test_public_package.py` |
| Claim boundary and verification gate | `results/P6_final_verification_gate.json` | `scripts/check_public_package.py`; `tests/test_public_package.py` |

## Guardrails

- The theorem is finite and paper-local to the certified extension atlas.
- The statement is not a public release claim and does not authorize record-level
  payload promotion.
- B1 is scoped to absence from the affine selected-plane layer; it is not a full
  endpoint-23/27 classification.
- B2 is finite-closed; no complete conceptual B2 theorem is claimed.
- B3 is closed at finite bilinear support-action level.  Item10 closes the
  column-profile classification intrinsically as a function of `(signature, M)`,
  and Step10+ proves the clause templates; no full non-affine classification and
  no non-enumerative first-principles proof of the 15/49 realization matrix is
  claimed.

- Item9 reduces the count debt to the finite endpoint kernel `{36,16,7}` and
  B3 row-degree pattern `1,1,1,2,2,1,4,3`; it does not prove the count 60
  non-enumeratively.  Item11 proves the remaining defect-6 realization cut is
  irreducibly integer-magic: `13/35` realized two-flats, all `35` F2-completable,
  and no nontrivial `GL(4,2)` stabilizer.

Release note: this appendix is reviewer support for the public paper. The main manuscript already integrates the Item10/Item11 summaries without promoting them to a non-enumerative 15/49 proof.
