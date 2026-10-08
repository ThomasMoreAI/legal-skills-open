---
name: co-statewide-format-codearranger
title: Colorado Statewide Court Document Formatting
description: 'Use when drafting Colorado court documents — pleadings, motions, declarations, proposed orders under **C.R.C.P. 10** (form of pleadings) and **Chief Justice Directive 11-01** (statewide filing standards). Covers the **flexible caption** (four-row table: court-type / county / address; parties; attorney/pro se + COURT USE ONLY box; title), numbered paragraphs, signature blocks (with Colorado attorney registration #), exhibits, footer with page count, line numbering, and citation format. Triggers: "draft a Colorado pleading", "C.R.C.P. 10", "CJD 11-01", "flexible caption", "Colorado declaration".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/co-court-docs/skills/co-statewide-format
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Colorado Statewide Court Document Formatting

> **NOT LEGAL ADVICE.** This skill assists with drafting and
> formatting only. Verify against current Colorado Rules of Civil
> Procedure, Chief Justice Directives, and the local rules of the
> filing court before submitting any document.

Use these rules whenever drafting a paper to be filed in a Colorado
state court. They derive from **C.R.C.P. 10** (Form of Pleadings,
Motions, and Other Documents) and **Chief Justice Directive 11-01**
(Standards for the Filing of Pleadings in Colorado State Courts).

## C.R.C.P. 10 + CJD 11-01 format requirements (mandatory)

| Item | Rule |
|------|------|
| Paper size | US Letter, 8½ × 11 inches |
| Sides | Single-sided only |
| Margins (all sides) | **Minimum 1 inch** (top, bottom, left, right) |
| Line spacing | **Double-spaced** for pleadings and motion text; single-spaced permitted for block quotes, footnotes, captions, and signature blocks |
| Body font size | **12 point** minimum |
| Font family | Clear, legible — Times New Roman, Arial, Century Schoolbook, or Calibri are all accepted |
| Color | **Black ink only** — no colored highlighting or colored text in the body. Color is permitted in exhibits only when grayscale would lose meaning (color photos, screenshots where color carries information) |
| Page numbers | Each page numbered consecutively; convention is `Page X of Y` in the footer |
| Caption | Two-block layout: party block on the left, case-number / division / courtroom block on the right |

Colorado uses a **uniform 1-inch margin on all four sides of every
page, including page 1** — there is no enlarged page-1 top margin
and no required leading whitespace before the caption.

`scripts/format-check.py` validates these requirements against a
generated `.docx`.

## Default typography

- **Font**: Times New Roman 12 pt (most common in district court);
  Arial 12 pt also accepted under CJD 11-01
- **Line spacing**: Double for pleadings and motion text; single for
  block quotes, signature blocks, and captions
- **Paragraph numbering**: Bold Arabic numeral followed by a period
  and a tab, e.g. `1.\tI am the Petitioner...`
- **Bold lead-ins** for labeled paragraphs: `**Background.**` at the
  start of a paragraph, then regular text in roman

## Required footer (mandatory on every generated document)

Every generated document MUST carry a running footer on every page
with:

- **Left**: a short document identifier — typically
  `[Document title] — Case No. [case number]` (e.g.,
  `Motion to Dismiss — Case No. 2025CV031234`). Keep it to a single
  line so it never wraps.
- **Right**: `Page X of Y`, where `X` is the current page number and
  `Y` is the total page count. Use Word's `PAGE` and `NUMPAGES`
  fields — never a static number.
- **Font**: 10 pt; matches body font family.
- **Alignment**: right-aligned tab stop at 9,360 DXA (6.5") places
  the page counter flush right while the title stays flush left.

The footer runs continuously from page 1 through the last exhibit
page — do not restart or suppress pagination anywhere.

## Line numbering (pleading paper)

Apply continuous line numbering down the left margin of every
generated Colorado pleading. Line numbers count every line of
the body and restart on each page.

C.R.C.P. 10 and CJD 11-01 do **not** themselves require line
numbering, and a Colorado pleading filed without line numbers
is rule-compliant. But line-numbered pleading paper is
universal practice across the `claude-legal` marketplace: it
lets the court and opposing counsel cite to an exact location
("page 4, lines 12–15") and never harms a Colorado filing.
Apply it **by default** to every motion, memorandum,
declaration, notice, and proposed order. Exhibits and
attachments are exempt.

For programmatically generated `.docx` documents, apply line
numbering through the section's `lineNumbers` property:

```javascript
import { LineNumberRestartFormat } from "docx";

sections: [{
  properties: {
    page: { /* size + margins */ },
    lineNumbers: {
      countBy: 1,                                // number every line
      restart: LineNumberRestartFormat.NEW_PAGE, // restart 1.. each page
    },
  },
  // ...
}]
```

This emits `<w:lnNumType w:countBy="1" w:restart="newPage"/>`
into the section's `<w:sectPr>`. The numbers render in the
left margin and do not shift the 1-inch text margin.

**Do NOT set `start` explicitly.** An explicit `start: 1`
renders off by one in LibreOffice (the first body line shows
"2"). Omit `start` — it defaults to 1 in OOXML.

## Margin rule (double vertical line)

Draw a double vertical rule — two thin parallel lines
(~0.75 pt each, with a ~7 pt gap between them) — down the left
margin between the line numbers and the body text. It is the
standard companion to line-numbered pleading paper. Like line
numbering, C.R.C.P. 10 and CJD 11-01 do **not** require it,
but it is universal convention across the `claude-legal`
marketplace. Apply it **by default** to every line-numbered
pleading; exhibits and attachments are exempt.

Implement it as two independent full-height line shapes
anchored in the page header, so they repeat on every page —
**not** as an OOXML `double` page border, whose style couples
the inter-line gap to the line weight (widening the gap
thickens both lines into heavy bars).

Draw each line as a thin filled rectangle (VML `v:rect`).
**One shape per `<w:pict>`** — multiple `<v:rect>` elements in
a single `<w:pict>` will not all render; each rectangle needs
its own `<w:pict>` inside its own `<w:r>` run.

`docx-js` has no first-class API for header-anchored VML
shapes. Add them with the docx skill's **unpack → edit → pack**
workflow: generate the file with docx-js (give each section an
empty `Header` so a `word/header1.xml` part exists, and keep the
`lineNumbers` section property from above), then rewrite the
header XML and repack:

```bash
python scripts/office/unpack.py out.docx unpacked/
#   ... inject the rule into unpacked/word/header*.xml (helper below) ...
python scripts/office/pack.py unpacked/ out.docx --original out.docx
```

Inside each `unpacked/word/header*.xml`, declare the VML namespace
on the root `<w:hdr>` and add the two runs — one `v:rect` per
`<w:pict>` per `<w:r>` — inside the header paragraph. A document
can have several header parts (first-page / even / default, or one
per section); add the runs to **each** distinct `word/header*.xml`,
giving every `v:rect` a unique `id`. This stdlib helper (no
`python-docx`) does it and is idempotent:

```python
import pathlib, re

def _runs(i):
    outer = ('<w:r><w:pict><v:rect id="VRuleOuter%d" '
             'style="position:absolute;margin-left:60pt;margin-top:21.6pt;'
             'width:0.75pt;height:748.8pt;'
             'mso-position-horizontal-relative:page;'
             'mso-position-vertical-relative:page;z-index:-251658240" '
             'fillcolor="black" stroked="f"/></w:pict></w:r>') % i
    return outer + (outer.replace('VRuleOuter%d' % i, 'VRuleInner%d' % i)
                         .replace('margin-left:60pt', 'margin-left:67pt'))

word = pathlib.Path('unpacked/word')

# 1. Double rule: one set of shapes per distinct header part (unique ids).
for i, hdr in enumerate(sorted(word.glob('header*.xml'))):
    xml = hdr.read_text(encoding='utf-8')
    if 'VRuleOuter' in xml:                                   # idempotent
        continue
    if 'xmlns:v=' not in xml:
        xml = re.sub(r'(<w:hdr\b)',
                     r'\1 xmlns:v="urn:schemas-microsoft-com:vml"', xml, count=1)
    xml = xml.replace('</w:p>', _runs(i) + '</w:p>', 1)       # first header para
    hdr.write_text(xml, encoding='utf-8')

# 2. Keep line numbers off header/footer text.
for f in list(word.glob('header*.xml')) + list(word.glob('footer*.xml')):
    xml = f.read_text(encoding='utf-8')
    xml = re.sub(r'(<w:pPr(?:\s[^>]*)?>)(?!<w:suppressLineNumbers/>)',
                 r'\1<w:suppressLineNumbers/>', xml)
    xml = re.sub(r'(<w:p(?:\s[^>]*)?>)(?!<w:pPr)',
                 r'\1<w:pPr><w:suppressLineNumbers/></w:pPr>', xml)
    f.write_text(xml, encoding='utf-8')
```

The `<w:lnNumType>` line-numbering element is already emitted by
docx-js's `lineNumbers` section property (above), so the patch only
touches the header / footer parts.

**Geometry** (US Letter, 1-inch margins, line-number `distance`
360 twips = ¼″): body text starts at 72 pt and the line-number
gutter at ~54 pt, so the two rules at `margin-left` **60 pt** and
**67 pt** sit ~7 pt apart, clear of both. The gap is the difference
of the two values; `margin-top:21.6pt` + `height:748.8pt` spans the
full page height; `width:0.75pt` is the line weight.

Verify with `python scripts/office/validate.py out.docx` then
`python scripts/office/soffice.py --headless --convert-to pdf
out.docx`; confirm two thin parallel lines with a clear gap between
the numbers and the text on **every** page and that the header /
footer text is not line-numbered. Then open the `.docx` in
Microsoft Word, where VML renders slightly differently and the
output must still be correct.
## Caption structure (C.R.C.P. 10(a) + CJD 11-01)

Colorado uses the **statewide "flexible caption"** published by the
Colorado Judicial Branch (the JDF blank caption template at
[coloradojudicial.gov/.../flexiblecaption_0.pdf](https://www.coloradojudicial.gov/sites/default/files/2023-07/flexiblecaption_0.pdf)).
It is a single bordered table divided into four stacked rows. The
right-side **"COURT USE ONLY"** box pairs with the **attorney / party-
without-attorney information row** — not with the party row above it.
This is the most common mis-drafting error and the linter checks for
it.

```
┌──────────────────────────────────────────────────────────────────┐
│ ☐ Small Claims  ☐ County Court  ☒ District Court                 │
│ ☐ Probate Court ☐ Juvenile Court ☐ Water Court                   │
│ [COUNTY] County, Colorado                                        │
│ Court Address: [street address, city, CO ZIP]                    │
├──────────────────────────────────────────────────────────────────┤
│ Plaintiff(s): VELOCITY INVESTMENTS, LLC,                         │
│                                                                  │
│ v.                                                               │
│                                                                  │
│ Defendant(s): JOHN DOE.                                          │
├───────────────────────────────────────────┬──────────────────────┤
│ Attorney or Party Without Attorney:       │ ▲ COURT USE ONLY ▲   │
│ (Name & Address)                          │                      │
│   Jane Q. Public                          │ Case Number:         │
│   123 Main St., Denver, CO 80202          │   2025CV031234       │
│                                           │                      │
│ Phone Number: (303) 555-0100              │ Div.: 12  Ctrm.: 270 │
│ FAX Number: (303) 555-0101                │                      │
│ E-mail: jane@example.com                  │                      │
│ Atty. Reg. #: 12345 (omit if pro se)      │                      │
├───────────────────────────────────────────┴──────────────────────┤
│                  [INSERT TITLE OF FORM]                          │
│             (e.g., MOTION TO DISMISS UNDER C.R.C.P. 12(b)(5))    │
└──────────────────────────────────────────────────────────────────┘
```

### The four rows in order

1. **Court identifier row** (full width). Six court-type checkboxes
   on two lines — Small Claims / County Court / District Court on
   the first line; Probate Court / Juvenile Court / Water Court on
   the second. Mark exactly **one** with a filled box (☒) or an
   inline `[X]`. Then `[COUNTY] County, Colorado` on its own line,
   then `Court Address:` with the courthouse street address.
2. **Party row** (full width). Plaintiff(s) / Petitioner(s) on top,
   then `v.` (or `In re:` for in-rem captions), then Defendant(s) /
   Respondent(s). Use the party designations that match the case
   type — `Plaintiff` / `Defendant` for civil; `Petitioner` /
   `Respondent` for domestic-relations, probate, and most special
   proceedings; `In the Matter of` for guardianships, name changes,
   and similar.
3. **Attorney / party-without-attorney row** (split into two cells).
   - **Left cell** (≈ 4,800 DXA): the attorney-or-pro-se information
     block. Required fields in this exact order: **Attorney or Party
     Without Attorney: (Name & Address)** → **Phone Number** → **FAX
     Number** (write "N/A" if none) → **E-mail** → **Atty. Reg. #**
     (pro se filers leave this field absent — do not write "N/A"
     here; the field is for licensed attorneys only).
   - **Right cell** (≈ 2,160 DXA): the **▲ COURT USE ONLY ▲** box
     containing `Case Number:`, then `Div.:` and `Ctrm.:` on a
     single line. 1-pt black border on all four sides of this cell.
     The case-number field is left blank by the filer on an initial
     pleading — the clerk stamps the number on acceptance — but is
     populated on every subsequent filing.
4. **Form-title row** (full width). The document title in ALL CAPS,
   centered, immediately below the caption table. This is the only
   row that does not require a border around the cell.

### Build it as a single 4-row table

The whole caption is one bordered table with row 3 split into two
cells. Do **not** try to stack two independent tables or float the
COURT USE ONLY box outside the row — it belongs in row 3.

| Row | Cells | Width (DXA) | Border |
|-----|-------|-------------|--------|
| 1. Court identifier | 1 (full) | 9,360 | 1 pt all sides |
| 2. Party block | 1 (full) | 9,360 | 1 pt all sides |
| 3. Attorney info + COURT USE ONLY | 2 (split) | 4,800 / 2,160 (right cell narrower with reserved gutter) | 1 pt all sides on both cells |
| 4. Form title | 1 (full), centered, ALL CAPS | 9,360 | no border (sits outside the caption table proper) |

Place the document title (row 4) between the bordered caption and
the body. If you prefer the title inside the bordered table, that is
also acceptable under CJD 11-01 — JDF forms vary on this point.

### Captions that vary from the standard layout

- **Appellate filings** (Colorado Supreme Court, Colorado Court of
  Appeals): use the appellate caption per C.A.R. 28, not the
  flexible caption. The flexible caption is a **trial-court**
  template.
- **Water Court**: same flexible caption, but check the Water Court
  box and add the water division number in the court-identifier row
  (e.g., "Water Division 1").
- **Probate / Juvenile**: check the corresponding box. Juvenile
  Court captions in dependency-and-neglect cases use the "In the
  Interest of [child]" party designation in row 2.
- **Domestic relations**: row 2 uses **In re the Marriage of:** /
  **In re the Parental Responsibilities concerning:** with
  Petitioner / Co-Petitioner / Respondent rather than Plaintiff /
  Defendant.

## Required body elements

Every affidavit or declaration needs:

1. **Salutation clause** at the top of the body:
   "I, [Name], being first duly sworn upon oath" (affidavit) **or**
   "I, [Name], under penalty of perjury pursuant to C.R.S.
   § 13-27-104, declare as follows:" (declaration)
2. **Numbered paragraphs** with substantive content
3. **Verification clause** at the end (declaration form):
   "I declare under penalty of perjury pursuant to the laws of the
   State of Colorado that the foregoing is true and correct."
4. **Date and place of execution**:
   "Executed on [date] at [city], [state]."
5. **Signature block** with signer name, role, address, phone, email

Motions and memoranda do not need a perjury clause but do need:

- A signature block with name, address, phone, email
- A Colorado attorney-registration number (`#XXXXX`) if the signer is
  a Colorado-licensed lawyer; pro se filers omit this
- A short **certificate of service** at the foot of the document
  showing how, when, and on whom the document was served

## Signature block format

```
Respectfully submitted this ___ day of __________, 20__.

                                        ____________________________
                                        [Name]
                                        [Reg. No. ##### (if attorney)]
                                        [Street address]
                                        [City, CO ZIP]
                                        Phone: (###) ###-####
                                        Email: name@example.com
                                        [Pro Se / Attorney for Party]
```

The attorney-registration number is **mandatory** on every pleading
filed by a Colorado-licensed lawyer — see C.R.C.P. 11(a). Pro se
filers omit the number and add "Pro Se" or "Self-Represented" on the
last line.

## Certificate of service

Every document filed with the court must include a certificate of
service unless filed under seal or otherwise excused. Place it at the
foot of the document **above the signature block**:

```
                    CERTIFICATE OF SERVICE

I certify that on [date], a true and correct copy of the foregoing
[Document Title] was served on:

  [Opposing party name]
  [Address]
  via [E-Service through CCEFS / U.S. Mail, postage prepaid /
       email at name@example.com per C.R.C.P. 5(b)(2)(E)]

                                        ____________________________
                                        [Signer name]
```

Under C.R.C.P. 5(b), service by Colorado Courts E-Filing (CCEFS)
constitutes valid electronic service; pro se filers without a CCEFS
account must serve by mail, hand delivery, or email per C.R.C.P.
5(b)(2)(E).

## Exhibits

Embed exhibits at the end of the document, after the signature block
and certificate of service, in this order:

1. **Exhibit List** page, centered title, each entry like:
   `Exhibit A:    [one-line description]`
2. One **cover page per exhibit**: `EXHIBIT A` centered and bold at
   the top of the page, followed by an italic caption describing the
   exhibit, then the exhibit image or text
3. Footer pagination continues through the exhibits — do not restart
   the page counter

Reference exhibits in the body by letter: "True and correct copies of
the disputed account statements are attached hereto as **Exhibits A
through D**."

## The four document templates

See `references/templates/` for complete scaffolds:

- `declaration.md` — declaration / affidavit with numbered paragraphs
  and exhibits
- `motion-with-memo.md` — C.R.C.P. 121 § 1-15 motion with the
  combined motion-and-brief format (Colorado allows a unified
  document under the local Rule 121 conventions)
- `notice-of-setting.md` — notice that places a motion on the
  court's calendar after the JA/clerk has assigned a hearing
- `proposed-order.md` — proposed order for judge signature, with the
  caption replicated and the dispositional language sliced into
  numbered findings and a separate "IT IS THEREFORE ORDERED" block

Each template includes the caption, body skeleton, signature block,
certificate of service, and (for declarations) exhibit list
scaffolding.

## Citation format

Follow the Colorado Appellate Court conventions and the ICW Style
Manual. Common forms:

- Colorado Supreme Court: `People v. Smith, 2020 CO 12, ¶ 15, 456 P.3d 789` (post-2012 cases) or `People v. Jones, 252 P.3d 1191 (Colo. 2011)` (pre-2012)
- Colorado Court of Appeals: `Smith v. Jones, 2019 COA 45, ¶ 22, 432 P.3d 100`
- Tenth Circuit: `Spann v. Carter, 23 F.4th 1131 (10th Cir. 2022)`
- C.R.S.: `C.R.S. § 13-80-103.5` (always use the `§` symbol for
  Colorado statutes)
- C.R.C.P.: `C.R.C.P. 12(b)(5)` (no section symbol for rules)
- C.R.E.: `C.R.E. 803(6)`
- Federal statutes: `15 U.S.C. § 1692g`

Italicize case names (including `v.`). Use the public-domain neutral
citation format (`2020 CO 12, ¶ 15`) for Colorado Supreme Court and
Court of Appeals decisions issued after January 1, 2012; the parallel
P.3d citation is required.

## Producing documents programmatically

For `.docx` generation, use the `docx` npm package. Key points:

- Set page size explicitly to US Letter (12,240 × 15,840 DXA) —
  `docx-js` defaults to A4
- Use Times New Roman at `size: 24` (half-points = 12 pt)
- Apply uniform 1,440 DXA margins to all four sides on every section
- Build the right-block table cell with a 1-pt border on all four
  sides for the case-number / division / courtroom box
- Use `LevelFormat.BULLET` with a numbering config for bullets —
  never unicode bullet characters
- Build the footer with a right-aligned tab stop at 9,360 DXA and
  use `PageNumber.CURRENT` / `PageNumber.TOTAL_PAGES` for
  "Page X of Y"

For format validation, run `scripts/format-check.py` on the generated
`.docx`.

## Filing mechanics: paper vs. e-filing

Colorado is largely on **Colorado Courts E-Filing (CCEFS)** for
attorneys (mandatory for represented parties in most counties);
pro se filers may file electronically through CCEFS Pro Se if
available in the filing county, otherwise by paper at the clerk's
window. See `co-file-packet` for the full e-filing workflow.

## Composition

- For drafting a Colorado motion or memorandum: `co-draft-motion`
- For drafting a Colorado declaration: `co-draft-declaration`
- For drafting a notice of setting / hearing: `co-draft-note`
- For drafting a proposed order: `co-draft-order`
- For court-specific overlays: `co-denver`, `co-arapahoe`,
  `co-county-courts`
- For pro se conventions: `co-pro-se`
- For pre-filing QC: `co-quality-check`

## References

- `references/templates/declaration.md`
- `references/templates/motion-with-memo.md`
- `references/templates/notice-of-setting.md`
- `references/templates/proposed-order.md`
- `references/crcp-10-full-text.md` — the full rule text
- `references/cjd-11-01-full-text.md` — full text of the CJD
- `references/caption-format.md` — caption structure with the two-block layout and docx-js recipe
- `references/exhibit-handling.md` — exhibit list, cover page, and pagination
- `references/citation-format.md` — Colorado neutral-citation conventions
