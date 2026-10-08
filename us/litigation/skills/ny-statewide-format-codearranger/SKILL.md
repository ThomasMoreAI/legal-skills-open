---
name: ny-statewide-format-codearranger
title: New York Statewide Format
description: Use when drafting or formatting any document for a New York state court (Supreme Court, County Court, Civil Court of the City of New York, District Court, City Court, or Town/Village Justice Court). Triggers include 'draft a New York pleading', 'format an affidavit', 'apply 22 NYCRR § 202.5', '22 NYCRR 202.5-b NYSCEF format', 'build a New York caption', 'verify NY citation style', 'Tanbook citation', 'CPLR caption', 'verified complaint format', 'affirmation under CPLR 2106'. Covers **22 NYCRR § 202.5** page/font/margin requirements, **22 NYCRR § 202.5-b** NYSCEF electronic-filing, **New York caption** (CPLR 305(a) / CPLR 2101), document-title conventions, **verified vs. unverified pleading** distinction (CPLR 3020–3021), affidavit (CPLR 2309) vs. affirmation (CPLR 2106) signature blocks, and **Tanbook** citation format.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-statewide-format
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# New York Statewide Format

> **NOT LEGAL ADVICE.** This skill provides drafting assistance
> only. Verify against current rules and case law before filing.

New York has no single, all-encompassing format rule.
Format requirements live across three layers:

1. **22 NYCRR § 202.5** — Uniform Civil Rules for the Supreme
   Court and County Court: page/font/margin rules for paper
   filings.
2. **22 NYCRR § 202.5-b** — NYSCEF (New York State Courts
   Electronic Filing) technical requirements for e-filed
   documents. NYSCEF is mandatory in most Supreme Court
   counties.
3. **Part rules** — every Justice of the Supreme Court
   publishes individual "Part Rules" (sometimes called "Rules
   of Practice") that override or supplement the uniform
   rules. Check the assigned Justice's Part Rules **before
   every filing.**

## Paper / page rules (22 NYCRR § 202.5(a))

- **Paper size**: 8½ × 11 inch (Letter)
- **Margins**: 1 inch on top, bottom, and both sides
- **Spacing**: Double-spaced text; quotations of 50+ words
  may be single-spaced and indented
- **Font**: Typeface that produces a clear copy; the rule
  is silent on a specific point size, but Times New Roman
  12-point or Courier New 12-point is the de facto standard.
  The Commercial Division (NY County, Kings County, Nassau,
  Westchester, Erie, etc.) requires **12-point** specifically
  under 22 NYCRR § 202.70(g) Rule 17.
- **Color**: Black ink on white paper for paper filings;
  NYSCEF accepts black-and-white or color PDFs but the body
  text must be readable monochrome.
- **Page numbering**: Bottom center or bottom right; format
  per Part Rules (some Justices require "Page X of Y").
- **Stapling / binding**: Paper filings — top-stapled, no
  fancy binding. NYSCEF — single PDF per document.

## NYSCEF technical requirements (22 NYCRR § 202.5-b)

NYSCEF is mandatory in: NY County, Kings, Bronx, Queens,
Richmond (commercial only), Nassau, Suffolk, Westchester,
Rockland, Erie, Monroe, Onondaga, and most other Supreme
Court counties. Civil Court of the City of New York uses a
parallel system (UCMS / CCEF).

- **File format**: PDF (text-searchable preferred; image-
  only PDFs allowed for true-paper exhibits)
- **Bookmarks**: Required for documents with multiple
  exhibits; bookmark to first page of each exhibit
- **File size**: 100 MB per upload cap
- **Naming**: Descriptive document title; no special
  characters
- **Signature**: An "/s/ Name" typed line plus an `e-filed
  by [Name]` line on the cover page; NYSCEF stamps the
  document automatically
- **Document codes**: NYSCEF requires selecting a document
  type from a controlled list (Affirmation, Affidavit,
  Memorandum of Law, Notice of Motion, Order, etc.). Pick
  the closest match.

## Line numbering (pleading paper)

Apply continuous line numbering down the left margin of every
generated New York pleading. Line numbers count every line of
the body and restart on each page.

22 NYCRR § 202.5 (paper) and § 202.5-b (NYSCEF) do **not**
themselves require line numbering, and a New York filing
without it is rule-compliant and routine; NYSCEF accepts PDFs
with or without line numbering. But line-numbered pleading
paper is universal practice across the `claude-legal`
marketplace: it lets the court and opposing counsel cite to an
exact location ("page 4, lines 12–15") and never harms a New
York filing. Apply it **by default** to every motion,
affirmation, memorandum, notice, and proposed order. Exhibits
and attachments are exempt.

**Two distinct numbering mechanics in New York** — both should
be ON by default:

- **Paragraph numbering** under CPLR 3014 — sequentially
  numbered paragraphs in the body of every pleading; verified
  pleadings under CPLR 3020 retain the sequential paragraph
  numbering. This is the NY-pleading content mechanic.
- **Line numbering** — line numbers in the left margin
  enabling page+line pinpoint citation. This is the layout
  mechanic added here.

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
numbering, 22 NYCRR § 202.5 and § 202.5-b do **not** require
it, but it is universal convention across the `claude-legal`
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
## The New York caption (CPLR 305(a) and 2101)

```
SUPREME COURT OF THE STATE OF NEW YORK
COUNTY OF [COUNTY]
----------------------------------------- X
[PLAINTIFF NAME(S)],                       :
                                           :  Index No. [#####/YYYY]
                          Plaintiff(s),    :
                                           :  [DOCUMENT TITLE]
            -against-                      :
                                           :  Hon. [JUSTICE NAME]
[DEFENDANT NAME(S)],                       :  Part [##]
                                           :
                          Defendant(s).    :
----------------------------------------- X
```

Notes:

- **"-against-"** is the New York convention for the party
  separator. Not "v." or "vs."
- **Index Number**: assigned at the time of action
  commencement under CPLR 306-a. Format `[######/YYYY]`
  (e.g., `651234/2024`). Required on every paper after
  commencement.
- **The "X" enclosure** on the left side is traditional;
  the dotted-line ladder on the right is common but not
  mandated.
- **County name** appears in all caps below the court name.
- **"Hon. [Justice]"** and **"Part [##]"** are added once a
  case is assigned; can be omitted before assignment.

## Document title conventions

NY uses descriptive document titles centered below the
caption box, in bold or underlined or all-caps:

- **NOTICE OF MOTION** — formal scheduling document (CPLR
  2214); see `ny-draft-note`
- **VERIFIED COMPLAINT** — verified-pleading prefix
  (CPLR 3020) when the complaint is sworn-to
- **COMPLAINT** — unverified pleading (less common in
  consumer-debt and matrimonial matters)
- **AFFIRMATION OF [NAME] IN SUPPORT OF [MOTION]** — sworn
  statement by an attorney (CPLR 2106); see
  `ny-draft-declaration`
- **AFFIDAVIT OF [NAME] IN SUPPORT OF [MOTION]** — sworn
  statement by a non-attorney (CPLR 2309)
- **MEMORANDUM OF LAW IN SUPPORT OF [MOTION]** — legal
  argument; not required if all law is in the affirmation
  but Commercial Division Rule 17 prefers a separate memo
- **PROPOSED ORDER** — see `ny-draft-order`

## Verified vs. unverified pleadings (CPLR 3020)

**CPLR 3020(b)** *requires* verification when:

- The complaint alleges an account-stated claim (most
  consumer-debt complaints) — CPLR 3020(d)(2)
- The pleading must be served on the State of New York or
  a State official sued in an official capacity
- Either party has demanded verification

**CPLR 3020(a)** says a *verified pleading* may be served on
*any* opposing party who must then *answer with a verified
answer* (CPLR 3020(a)). This creates a tactical decision:
verifying your complaint forces the defendant to verify
their answer, which can deter frivolous denials.

Verification is a sworn statement at the foot of the
pleading: "[Affiant] swears the following pleading is true
to the affiant's own knowledge, except as to matters
alleged on information and belief which the affiant
believes to be true." Signed and notarized (CPLR 3021).

## Citation format — Tanbook

The **New York Law Reports Style Manual** ("Tanbook") is the
official citation manual for New York state court filings.
Key conventions vs. Bluebook:

- **Court of Appeals**: `Roe v. Doe, 1 NY3d 100, 105 (2003)`
  — note the missing periods (`NY3d` not `N.Y.3d`)
- **Appellate Division**: `Smith v. Jones, 50 AD3d 200,
  201 (1st Dept 2008)` — `AD3d`, department in parens
- **Supreme/County Trial**: `Roe v. Doe, 15 Misc 3d 100
  (Sup Ct, NY County 2007)` — published trial decisions go
  to `Misc 3d` (Miscellaneous Reports, 3rd Series)
- **Statutes**: `CPLR 3211(a)(7)` — no italics, no "N.Y."
  prefix in body text; "N.Y. C.P.L.R. § 3211(a)(7)" in
  out-of-state Bluebook context
- **Sessions Laws**: `L 2021, ch 593` — chapter laws
- **Public Authorities**: `Public Authorities Law § 1276`
- **Spaces in citations**: no spaces in compound abbreviations
  (`NYS2d` not `N.Y.S. 2d`)
- **Pinpoint cites**: `at 105` for parallel reporter; no
  pinpoint with "p." or "pp."

## State context

| Layer | Authority |
|---|---|
| Format rule | 22 NYCRR § 202.5 (paper) + § 202.5-b (NYSCEF) |
| Civil rules | CPLR (Civil Practice Law and Rules) |
| Evidence | Guide to NY Evidence + selected CPLR evidence sections (no codified code) |
| Statute | N.Y. CPLR; N.Y. Gen. Bus. Law; N.Y. Gen. Oblig. Law; N.Y. Real Prop. Law; N.Y. Real Prop. Acts. Law; etc. |
| Style manual | New York Law Reports Style Manual (Tanbook) |
| E-filing | NYSCEF (Supreme/County); UCMS/CCEF (NYC Civil Court) |

## Composition with other ny- skills

- `ny-nyco` / `ny-kings` / `ny-bronx` / `ny-nassau` /
  `ny-queens` / `ny-county-courts` — venue-specific overlays
  (Part Rules, courthouse logistics, scheduling)
- `ny-pro-se` — pro se conventions
- `ny-draft-motion`, `-declaration`, `-note`, `-order` —
  scaffolders that use these format conventions
- `ny-law-references` — full CPLR + Tanbook + 22 NYCRR
  reference corpora
- `ny-quality-check` — pre-filing QC against this format
  rule
