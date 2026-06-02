---
name: oh-statewide-format
title: Ohio Statewide Format — Civ. R. 10 + Per-Court Local Rules
description: Use when drafting any Ohio court filing — applies Ohio Civ. R. 10 caption + signature requirements, the common local-rule format conventions adopted by most Ohio Common Pleas and Municipal Courts (Letter paper; 1-inch margins with 1.5-inch top on first page for caption; 12-point minimum body font; double-spaced body), the Ohio public- domain citation format `YYYY-Ohio-NNNN` mandatory in appellate cases since 2002, and the affidavit-vs- declaration terminology distinction (Ohio uses "affidavit" under R.C. 2319.04 + Civ. R. 56; "declaration under penalty of perjury" is federal practice). Triggers include "Ohio court filing format", "Ohio Civ. R. 10", "Ohio caption", "Ohio attorney registration number", "Ohio public-domain citation", "Ohio affidavit format", "first page caption Ohio", "Common Pleas local rules format".
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/oh-court-docs/skills/oh-statewide-format
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Ohio Statewide Format — Civ. R. 10 + Per-Court Local Rules

> **NOT LEGAL ADVICE.** Verify the specific court's local
> rules before every filing. Format compliance varies
> materially between Common Pleas, Municipal, County, and
> Court of Claims venues.

## At a glance

Ohio has **no single statewide pleading-format rule**
analogous to a uniform civil-rules code that dictates
formatting across all courts. Format requirements live
across three layers:

1. **Ohio Civ. R. 10** — caption + signature block + form
   of pleadings (statewide minimum)
2. **Ohio Rules of Superintendence** (Sup. R. — most
   relevant: Sup. R. 26 on records and Sup. R. 44-47 on
   case-management standards)
3. **Per-court local rules** — each Common Pleas court
   publishes its own Loc. R. with page limits, certificate-
   of-service requirements, working-copy conventions, etc.

This skill enforces the common-denominator baseline. Always
cross-reference the assigned court's local rules.

## Caption format (Civ. R. 10(A))

Every pleading caption must include:

- **Court name** in full: `IN THE COURT OF COMMON PLEAS OF
  CUYAHOGA COUNTY, OHIO` (or the applicable court)
- **Division** if applicable: `CIVIL DIVISION` /
  `DOMESTIC RELATIONS DIVISION` / `JUVENILE DIVISION` /
  `PROBATE DIVISION`
- **Case number** — Common Pleas case numbers typically
  follow `CVNNNNNN` (general civil), `DRNNNNNN` (domestic
  relations), or court-specific patterns
- **Parties** — `<Plaintiff Name>` / `vs.` / `<Defendant
  Name>` (Ohio uses `vs.` with periods)
- **Title of the document** — e.g., `DEFENDANT'S ANSWER`,
  `MOTION TO DISMISS`, `NOTICE OF HEARING`

The first-page caption block typically occupies the top
1.5 inches; body text begins below.

## Paper format (statewide common denominator)

- **Paper**: Letter (8.5 x 11 inches)
- **Margins**: 1.5-inch top on first page (caption block);
  1-inch top on subsequent pages; 1-inch sides + bottom
- **Font**: 12-point minimum (Times New Roman or
  comparable serif preferred)
- **Line spacing**: double-spaced body (most local rules)
- **Page numbering**: footer with page number; some courts
  require `Page X of Y` format
- **Color**: black text on white paper

## Line numbering (pleading paper)

Apply continuous line numbering down the left margin of every
generated Ohio pleading. Line numbers count every line of the
body and restart on each page.

Ohio Civ. R. 10 and per-court local rules do **not**
themselves require line numbering, and an Ohio filing without
it is rule-compliant across Common Pleas, Municipal, and
County courts. But line-numbered pleading paper is universal
practice across the `claude-legal` marketplace: it lets the
court and opposing counsel cite to an exact location ("page 4,
lines 12–15") and never harms an Ohio filing. Apply it **by
default** to every motion, memorandum, affidavit, notice of
hearing, and proposed order. Exhibits and attachments are
exempt.

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
numbering, Ohio Civ. R. 10 and per-court local rules do
**not** require it, but it is universal convention across the
`claude-legal` marketplace. Apply it **by default** to every
line-numbered pleading; exhibits and attachments are exempt.

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
## Signature block (Civ. R. 11)

- **Counsel signature** must include:
  - Attorney's name
  - **Ohio Supreme Court attorney registration number**
    (`Atty. Reg. #NNNNNNN` — required under Gov. Bar R.
    VI(1)(B))
  - Firm name (if any)
  - Address + phone + fax + email
- **Pro se signature** must include:
  - Name + address + phone + email
  - The designation `Pro Se` or `Self-Represented`
  - **Omit attorney registration number** (don't fabricate)

## Affidavit vs. Declaration terminology

Ohio practice uses **affidavit** under **R.C. 2319.04** for
notarized sworn statements and uses **affidavit** under
**Civ. R. 56(C)** for summary-judgment support. The
federal-style "declaration under penalty of perjury"
terminology (28 U.S.C. § 1746) is **not** Ohio civil
practice. The `oh-draft-declaration` skill produces Ohio-
correct affidavits despite its scaffolder-conventional
name.

## Citation format (Ohio public-domain citation)

Ohio adopted a **public-domain citation system in 2002** —
**`YYYY-Ohio-NNNN`** format is **mandatory** in appellate
cases. Examples:

- *Smith v. Jones*, 100 Ohio St.3d 543, 2003-Ohio-1234,
  paragraph 12
- *State v. Brown*, 2018-Ohio-5678 (10th Dist.)

Trial-court citations follow the reporter's conventions:

- Ohio Supreme Court: `Ohio St.3d`
- Ohio Court of Appeals: `Ohio App.3d`
- Trial court: `Ohio Misc.2d`

For statutory citations:

- `R.C. 1345.01` (preferred) or `Ohio Rev. Code Ann.
  § 1345.01`
- Ohio Civ. R.: `Civ. R. 10(A)` (no `Ohio` prefix in
  in-state filings)
- Ohio Evid. R.: `Evid. R. 803(6)`

## Common per-court local-rule variations

These vary materially by court. Verify before filing:

- **Page limits on briefs** — many Common Pleas courts cap
  motion briefs at 15-25 pages; some impose 30
- **Working copies** — some judges require courtesy paper
  copies; others rely on electronic filing only
- **Certificate of service** — format and signature
  requirements vary; verify Loc. R.
- **Proposed orders** — some courts require a Word version
  emailed to chambers; others require a tendered paper
  original

## Composition with other oh- skills

- `oh-quality-check` — runs pre-filing format + content QC
- `oh-cuya` / `oh-frank` / etc. — flagship Common Pleas
  local-rule overlays
- `oh-county-courts` — long-tail roll-up
- `oh-municipal-courts` — Municipal Court format
  conventions
- `oh-pro-se` — pro-se signature + tone framework
- `oh-fact-check` — Ohio public-domain citation
  verification
