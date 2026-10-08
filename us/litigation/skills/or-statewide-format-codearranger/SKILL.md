---
name: or-statewide-format-codearranger
title: Oregon Statewide Court Document Formatting
description: This skill should be used when the user asks to "draft a pleading", "format an Oregon court document", "apply UTCR 2.010", "UTCR formatting", "build a caption", "create a declaration", "format a motion", "notice of hearing", or "proposed order" for any Oregon circuit court. Covers Uniform Trial Court Rules (UTCR) 2.010 page formatting, UTCR 2.100 caption requirements, UTCR 2.110 document titles, UTCR 2.120 confidential information / SSN redaction, numbered paragraphs, line-numbered pleading paper, signature blocks, exhibit lists and cover pages, and citation format per the Oregon Appellate Courts Style Manual.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/or-court-docs/skills/or-statewide-format
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Caption Format
  path: references/caption-format.md
- title: Docx Generation
  path: references/docx-generation.md
- title: Exhibit Handling
  path: references/exhibit-handling.md
- title: Declaration
  path: references/templates/declaration.md
- title: Motion With Memo
  path: references/templates/motion-with-memo.md
- title: Notice Of Hearing
  path: references/templates/notice-of-hearing.md
- title: Proposed Order
  path: references/templates/proposed-order.md
- title: Utcr 2 010 Full Text
  path: references/utcr-2-010-full-text.md
---

# Oregon Statewide Court Document Formatting

Use these rules whenever drafting a paper to be filed in an Oregon
circuit court. They derive from the **Uniform Trial Court Rules
(UTCR) Chapter 2** (Form of Documents) and common statewide drafting
conventions used by the Oregon Judicial Department (OJD).

Oregon consolidated its trial courts in 1998 — there is no separate
district court system. All civil matters file in **Circuit Court**
regardless of amount in controversy. Small claims (≤ $10,000) and
court-annexed mandatory arbitration ($10,000–$50,000) are
sub-procedures **within** Circuit Court (ORS Ch. 46 and ORS 36.400
et seq., respectively).

> **NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
> against current UTCR, ORCP, and the local Supplemental Local Rules
> (SLR) for the specific circuit before filing.

## UTCR 2.010 format requirements (mandatory)

| Item | Rule |
|------|------|
| Paper size | US Letter, 8½ × 11 inches |
| Sides | Single-sided only |
| Top margin, page 1 | **At least 3 inches** to leave room for the clerk's filing stamp |
| All other margins | **At least 1 inch** (top of subsequent pages, bottom, left, right) |
| Color | Black or blue-black ink only; **no colored or highlighted text** in the body |
| Attachments / exhibits | Same rule applies unless the nature of the attachment makes compliance impractical (color photo as evidence, native screenshots) |
| Citations | Conform to the Oregon Appellate Courts Style Manual (latest edition, OJD) |
| eFiling | Mandatory in every circuit court through **File and Serve** (Tyler) — accept PDFs only |

When producing a `.docx` programmatically for upload to File and
Serve, apply a 1-inch top margin to the whole section and add ~2
inches of leading space before the caption on page 1 so the
effective top margin for page 1 is 3 inches. Subsequent pages then
fall at 1 inch automatically.

**Do not use colored highlighting or colored text** anywhere in the
pleading body. Color is permitted in attachments only when the
nature of the attachment makes B&W impractical (for example, a
native phone screenshot).

## Default typography

- **Font**: Times New Roman 12 pt (Arial 12 pt is also accepted)
- **Line spacing**: 1.5 or double-spaced for body text; single-spaced
  for block quotations, signature blocks, and tables
- **Paragraph numbering**: Bold Arabic numeral followed by a period
  and tab, e.g. `1.\tI am the Defendant...`
- **Bold lead-ins** for labeled paragraphs: `**Background.**` at
  the start of a paragraph, then regular text

## Required footer (mandatory on every generated document)

Every generated document MUST carry a running footer on every page
with:

- **Left**: a short document identifier — typically
  `[Document title] — Case No. [case number]` (e.g., `Motion to
  Compel — Case No. 25CV12345`). Keep it to a single line so it
  never wraps.
- **Right**: `Page X of Y`, where `X` is the current page and `Y` is
  the total page count. Use Word's `PAGE` and `NUMPAGES` fields —
  never a static number.
- **Font**: 10 pt Times New Roman (matches body font family;
  smaller for visual hierarchy).
- **Alignment**: a right-aligned tab stop at 9,360 DXA (6.5″)
  places the page counter flush right while the title stays flush
  left.

The footer runs continuously from page 1 through the last exhibit
page — do not restart or suppress pagination anywhere.
`scripts/format-check.py` validates the footer and will FAIL on a
document missing the `NUMPAGES` field, the `PAGE` field, or a
non-pagination title on the left.

See `references/docx-generation.md` for the exact `docx-js` recipe.

## Line numbering (pleading paper)

Apply continuous line numbering down the left margin of every
generated pleading — the classic "pleading paper" convention.
Line numbers count every line of the body and restart on each
page.

UTCR 2.010 does **not** itself require line numbering, and an
Oregon filing without it is rule-compliant. But line-numbered
pleading paper is common across Oregon civil practice and lets
the court and opposing counsel cite to an exact location ("page
4, lines 12–15"). Apply it **by default** to every motion,
memorandum, declaration, notice of hearing, and proposed
order. Exhibits and attachments are exempt.

Set line numbering on the section properties — count every line,
restart each page. The numbers sit in the left margin and do
not change the 1-inch text margin. See
`references/docx-generation.md` for the exact `docx-js` recipe,
including the `start`-attribute caveat (pass no `start` value —
an explicit `start: 1` renders off by one in LibreOffice).

## Margin rule (double vertical line)

Draw a double vertical rule — two thin parallel lines (~0.75 pt
each, with a ~7 pt gap between them) — down the left margin
between the line numbers and the body text. It is the standard
companion to line-numbered pleading paper. Like line numbering,
UTCR 2.010 does **not** require it, but it is common convention.
Apply it **by default** to every line-numbered pleading; exhibits
and attachments are exempt.

Implement it as two independent full-height line shapes anchored
in the page header, so they repeat on every page — **not** as an
OOXML `double` page border, whose style couples the inter-line
gap to the line weight (widening the gap thickens both lines into
heavy bars). See `references/docx-generation.md` for the exact
recipe.

## Caption structure (UTCR 2.100)

Two columns separated by a vertical rule:

```
            IN THE CIRCUIT COURT OF THE STATE OF OREGON
                  FOR THE COUNTY OF MULTNOMAH

VELOCITY INVESTMENTS, LLC,         │  Case No. 25CV12345
                                   │
        Plaintiff,                 │  [DOCUMENT TITLE IN ALL CAPS,
                                   │   BOLD, WRAPPED TO 4–6 LINES]
        v.                         │
                                   │
JOHN DOE,                          │
                                   │
        Defendant.                 │
```

UTCR 2.100 requirements:

- **Court header** (top, centered, bold): "IN THE CIRCUIT COURT OF
  THE STATE OF OREGON" on line 1, "FOR THE COUNTY OF [COUNTY]" on
  line 2
- **Party block** (left): parties in ALL CAPS, bold; role
  (Plaintiff, Defendant, Petitioner, Respondent) in normal case,
  indented under the party name
- **Case number** (top right, bold): `25CV12345` (year-CV-sequence,
  no spaces or dashes) for civil cases; small claims `25SC12345`;
  domestic relations `25DR12345`
- **Document title** (right, all caps, bold, wrapped): the full
  UTCR 2.110 title — every required descriptor in capitals
- **Vertical rule**: one line, on the right edge of the left cell OR
  the left edge of the right cell (not both — avoids double rules).
  This caption-internal column divider is distinct from the
  left-margin double rule above; do not conflate the two.
- **Horizontal rule** below the caption separating it from the body

Build the caption as a two-cell borderless table; add the vertical
border as above. Cell widths 4,680 DXA each on a 9,360 DXA (6.5-inch)
content area.

Use **"v."** (lowercase, with period) between parties — Oregon
convention. Not "vs."

## UTCR 2.110 — Document titles

The title at the top of the document (and in the caption) must:

- Be in ALL CAPS, bold
- State the **party making the filing** (e.g., "DEFENDANT'S MOTION
  TO COMPEL")
- State the **nature of the document** with enough specificity that
  the clerk can index it correctly (e.g., "MOTION TO COMPEL
  PRODUCTION OF DOCUMENTS UNDER ORCP 46")
- Identify whether the matter is **on the merits** or part of a
  subsidiary proceeding (small claims, mandatory arbitration, etc.)
- For motions: state whether oral argument is requested and the
  type of hearing (e.g., "ORAL ARGUMENT REQUESTED — 20 MINUTES")

The title appears in three places: the caption right column, again
at the top of the body on page 1, and in the document filename when
uploaded to File and Serve.

## UTCR 2.120 — Confidential information

Redact before filing. UTCR 2.100(7) and 2.120 require that the
following be omitted from publicly filed documents:

- Social Security numbers (use last four digits only)
- Bank account numbers, credit-card numbers (last four only)
- Dates of birth (year only, except for minor parties in family
  cases)
- Names of minor children (use initials)
- Home addresses of victims, witnesses (where applicable)

Confidential personal information is filed on a **separate
Confidential Information Form (CIF)** under UTCR 2.130 and is
sealed by the clerk.

## Required body elements

Every declaration needs (under ORCP 1 E and ORS 9.320, declarations
"under penalty of perjury" are accepted in place of notarized
affidavits for most filings — see ORCP 1 E and 28 USC § 1746
language):

1. **Salutation clause** at the top of the body:
   "I, [Name], declare under penalty of perjury under the laws of
   the State of Oregon that the following is true and correct:"
2. **Numbered paragraphs** with substantive content
3. **Verification clause** at the end (Oregon form):
   "I hereby declare that the above statements are true to the
   best of my knowledge and belief, and I understand they are
   made for use as evidence in court and are subject to penalty
   for perjury."
   (Or the shorter ORCP 1 E form: "I declare under penalty of
   perjury under the laws of the State of Oregon that the
   foregoing is true and correct.")
4. **Date and place of execution**:
   "DATED this ____ day of __________, 20__."
   "Executed at [city], Oregon."
5. **Signature block** with signer name, role, address, phone,
   email

Motions and memoranda do not need a perjury clause but do need a
signature block with name, role, address, phone, and email, plus a
**Certificate of Service** (UTCR 1.090 / ORCP 9 G) if served with
the filing.

## Exhibits

Embed exhibits at the end of the paper, after the signature block,
in this order:

1. **Exhibit List** page, centered title, each entry like:
   `Exhibit 1:    [one-line description]`
2. One **cover page per exhibit**: `EXHIBIT 1` centered and bold at
   the top of the page, followed by an italic caption describing
   the exhibit, then the exhibit image or text
3. Footer pagination continues through the exhibits — do not
   restart the page counter

Oregon convention is **numbered exhibits** ("Exhibit 1, Exhibit 2,
...") not lettered. This differs from Washington (lettered, "Exhibit
A, Exhibit B, ..."). Reference exhibits in the body by number:
"True and correct screenshots are attached as **Exhibits 1
through 4**."

## The four document templates

See the `references/templates/` directory for complete scaffolds:

- `declaration.md` — declaration with numbered paragraphs and
  exhibits
- `motion-with-memo.md` — motion with companion memorandum
- `notice-of-hearing.md` — Oregon-standard notice form
  (analogous to a "Note for Motion Docket")
- `proposed-order.md` — findings and order for judge signature

Each template includes the caption, body skeleton, signature block,
and (for declarations) exhibit list scaffolding.

## Citation format (Oregon Appellate Courts Style Manual)

Follow the Oregon Appellate Courts Style Manual (the "OACSM" or
"Oregon Style Manual") published by the OJD. Common forms:

- Oregon Supreme Court: `Buchler v. Oregon Corrections Div., 316 Or 499, 853 P2d 798 (1993)`
- Oregon Court of Appeals: `State v. Smith, 250 Or App 1, 280 P3d 1 (2012)`
- 9th Circuit: `Mansor v. Or. Inv. Co., 819 F3d 1119 (9th Cir 2016)`
- ORS: `ORS 12.080(1)` (no section symbol for ORS in Oregon style)
- ORCP: `ORCP 47 C` (subsections by upper-case letter, separated by
  spaces, no parentheses)
- OEC: `OEC 803(6)` (subsections in parentheses, by number)
- UTCR: `UTCR 2.010(1)`
- Federal statutes: `15 USC § 1692k(a)(1)` (no periods in "USC" in
  Oregon style; Bluebook would use "U.S.C.")
- Federal regulations: `12 CFR § 1006.30` (Oregon style; no periods
  in "CFR")

**Distinctive Oregon style choices**:
- No periods after `Or`, `Or App`, `P2d`, `P3d`, `F2d`, `F3d`, `US`,
  `USC`, `CFR` (Bluebook puts periods after all)
- Use `v.` (with period) between parties; italicize case names
  including the `v.`
- Spaces, not parentheses, separate ORCP subsection letters: `ORCP
  21 A` not `ORCP 21(A)`
- OEC subsections use parentheses with numerals: `OEC 803(6)`
- No "&" or "et seq." within citations — use page pins

Italicize case names (including `v.`). Use the regional reporter
(P2d / P3d) — Oregon does not have its own state reporter for the
Supreme Court, only the Oregon Reports (Or, Or App), which are
parallel-cited.

## Producing documents programmatically

For `.docx` generation, use the `docx` npm package and follow the
patterns in `references/docx-generation.md`. Key points:

- Set page size explicitly to US Letter (12,240 × 15,840 DXA) —
  `docx-js` defaults to A4
- Use `Times New Roman` at `size: 24` (half-points = 12 pt)
- Add a leading paragraph with `spacing: { before: 2880 }` (2
  inches) on page 1 to yield the 3-inch effective top margin
- Use `LevelFormat.BULLET` with a numbering config for bullets —
  never unicode bullet characters
- Build the footer with a right-aligned tab stop at 9,360 DXA and
  use `PageNumber.CURRENT` / `PageNumber.TOTAL_PAGES` for "Page X
  of Y"

For format validation, use the bundled `scripts/format-check.py`
on a generated `.docx`.

## eFiling — OJD File and Serve

Every Oregon circuit court accepts (and requires) electronic filing
through **File and Serve** (Tyler Tech), the OJD's statewide
eFiling portal:

- Self-represented filer portal: https://www.courts.oregon.gov/services/online/Pages/efile.aspx
- File and Serve: https://oregon.tylertech.cloud/
- File size limit: typically 25 MB per document; larger filings are
  split into separately uploaded PDFs
- Accepted format: PDF only (no .docx for the filed document
  itself; the .docx is the working copy)
- Document codes are picked from a dropdown matching the UTCR 2.110
  title — pick the closest match

Service through File and Serve counts as service for parties who
have registered for eService (ORCP 9 G(1)(d), UTCR 21.100). For
parties who have not registered, follow ORCP 9 D (mail, hand
delivery, or any of the other approved methods).

## Compose with court-specific skills

This skill is **always** layered with:

- `or-multcc` — if the case is in Multnomah County Circuit Court
- `or-wccc` — if the case is in Washington County Circuit Court
- `or-county-courts` — for any other county
- `or-pro-se` — if the litigant is self-represented

The court-specific skill adds the local SLR variations, motion
scheduling, working-copy practice, and the venue-specific filing
quirks.

## References

- `references/utcr-2-010-full-text.md` — the full rule text for
  quick citation
- `references/caption-format.md` — caption structure with full
  docx-js example
- `references/exhibit-handling.md` — exhibit list, cover page, and
  pagination
- `references/docx-generation.md` — `docx` npm library patterns for
  Oregon pleadings
- `references/templates/` — the four document templates
