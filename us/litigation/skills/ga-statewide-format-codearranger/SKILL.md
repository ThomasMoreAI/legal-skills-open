---
name: ga-statewide-format-codearranger
title: Georgia Statewide Court Document Formatting
description: 'Use when the user asks to "draft a Georgia pleading", "format a Georgia motion", "format a Georgia complaint", "build a Superior Court caption", or "build a Georgia caption" for any Georgia trial court. Triggers: "O.C.G.A. § 9-11-10 caption", "Georgia certificate of service", "O.C.G.A. § 9-11-5 service of subsequent papers", "O.C.G.A. § 9-11-11 signing", "numbered paragraphs O.C.G.A. § 9-11-10(b)", "Uniform Superior Court Rules", "USCR 36 e-filing", "Georgia Bar No. signature block", "Civil Action File No.", "PeachCourt", "Odyssey eFileGA", "line numbering", "Page X of Y footer", "Georgia citation O.C.G.A. S.E.2d". Covers the O.C.G.A. § 9-11-10 caption and numbered-paragraph form of pleadings, the Uniform Superior / State / Magistrate Court Rules, the § 9-11-11 signing requirement, the § 9-11-5 filing and certificate of service, USCR 36 e-filing through PeachCourt / Odyssey eFileGA, the marketplace format baseline, line-numbered pleading paper, footer conventions, and Georgia
  citation format.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-statewide-format
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Georgia Statewide Court Document Formatting

> **NOT LEGAL ADVICE.** This skill assists with drafting and
> formatting only. Verify against the current Georgia Civil Practice
> Act (O.C.G.A. Title 9, Chapter 11), the Uniform Rules of the filing
> court, and any judge's standing order before submitting any
> document.

Use these conventions whenever drafting a paper to be filed in a
Georgia trial court — a **Superior Court**, a **State Court**, or a
**Magistrate Court**. Georgia has **no single strict statewide
pleading-paper rule** fixing margins, font, and line spacing. Instead,
the form of a Georgia court document flows from the **Georgia Civil
Practice Act** — chiefly **O.C.G.A. § 9-11-10** (form of pleadings:
caption and numbered paragraphs), **O.C.G.A. § 9-11-7** (pleadings
allowed and their designations), **O.C.G.A. § 9-11-8** (general rules
of pleading), **O.C.G.A. § 9-11-11** (signing), and **O.C.G.A.
§ 9-11-5** (service and filing of subsequent papers, including the
certificate of service) — together with the **Uniform Superior Court
Rules (USCR)** and their parallels, the **Uniform State Court Rules**
and the **Uniform Magistrate Court Rules**. Electronic filing runs
under **USCR 36** and the statewide e-filing standards.

Pull the verbatim rule and statute text from the `ga-law-references`
corpus at `../ga-law-references/references/court-rules/` and
`../ga-law-references/references/ga-statutes-debt/` before relying on
any specific deadline, service add-on, or form figure — those values
live in the rule text and never drift here.

## Governing rules

- **O.C.G.A. § 9-11-10** — Form of pleadings.
  - **(a) Caption.** Every pleading contains a caption stating the
    **name of the court**, the **county**, the **title of the action**,
    the **file number**, and a **designation** of the pleading as
    provided in § 9-11-7(a). In the **complaint** the title of the
    action names **all the parties**; in **later pleadings** it is
    sufficient to name the **first party on each side** with an
    appropriate indication of other parties ("et al.").
  - **(b) Numbered paragraphs; separate counts.** All averments of
    claim or defense are made in **numbered paragraphs**, each limited
    so far as practicable to a **single set of circumstances**. Each
    claim founded on a separate transaction and each separate defense
    is stated in a **separate count** where separation aids clarity.
- **O.C.G.A. § 9-11-7** — Pleadings allowed; designations (complaint,
  answer, reply, etc.).
- **O.C.G.A. § 9-11-8** — General rules of pleading: a **short and
  plain statement** of the claim showing entitlement to relief; relief
  demanded; alternative and inconsistent pleading permitted.
- **O.C.G.A. § 9-11-11** — Signing of pleadings. Every pleading is
  **signed** by the party's attorney of record (or by the party if
  self-represented), with the signer's **address**. There is **no
  general requirement that pleadings be verified or accompanied by
  affidavit** except where a specific statute or rule requires it
  (certain equitable and extraordinary actions). Confirm whether your
  particular action carries a verification requirement before relying
  on the general rule.
- **O.C.G.A. § 9-11-5** — Service and filing of pleadings and other
  papers subsequent to the original complaint, and the **certificate
  of service** (see below).
- **Uniform Superior Court Rules (USCR)** govern practice in the
  Superior Courts; the **Uniform State Court Rules** parallel them in
  the State Courts, and the **Uniform Magistrate Court Rules** govern
  Magistrate Court. **USCR 36** governs electronic filing.

## Paper and legibility

Georgia does not impose a single statewide font / margin / spacing
rule for pleadings. The marketplace applies a clean, e-filing-ready
baseline **by default**, since no Georgia rule displaces it:

| Item | Baseline (confirm local rules) |
|------|--------------------------------|
| Paper / ink | US Letter, 8½ × 11 in., **black ink** on white |
| Sides | Single-sided |
| Font | A legible serif — **Times New Roman 12 pt** — or **Arial 12 pt** |
| Line spacing | **Double-spaced** body; single-spacing permitted for block quotes, captions, and signature blocks |
| Margins | **1 inch** on all four sides |
| Caption | Court name + county centered above the party block |
| Document title | Centered ALL-CAPS heading; also carried in the footer |
| Page numbers | Each page numbered; `Page X of Y` in the footer |

Local rules of a specific court (and a judge's standing order) may add
page limits on motions and briefs, chambers-copy requirements, and
exhibit-tabbing conventions. `scripts/format-check.py` validates a
generated `.docx` against this baseline and flags departures.

## Line numbering (pleading paper) — applied BY DEFAULT

Apply continuous line numbering down the left margin of every
generated Georgia pleading. Line numbers count every body line and
**restart on each page**.

The Civil Practice Act and the Uniform Rules do **not** themselves
require line numbering, and a Georgia document filed without line
numbers is rule-compliant. But line-numbered pleading paper is the
universal convention across this marketplace: it lets the court and
opposing counsel cite an exact location ("page 4, lines 12–15") and
never harms a Georgia filing. Apply it **by default** to every
complaint, motion, response, affidavit, declaration, notice, and
proposed order. Exhibits and attachments are exempt.

For programmatically generated `.docx` documents, apply line numbering
through the section's `lineNumbers` property:

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

This emits `<w:lnNumType w:countBy="1" w:restart="newPage"/>` into the
section's `<w:sectPr>`. The numbers render in the left margin and do
not shift the text margin.

**Do NOT set `start` explicitly.** An explicit `start: 1` renders off
by one in LibreOffice (the first body line shows "2"). Omit `start` —
it defaults to 1 in OOXML.

If you use a two-section page-1 layout (a deeper top margin to seat the
caption, then a normal continuation section), **set `lineNumbers` on
BOTH sections**, or numbering stops at the section break.

## Required footer (mandatory on every generated document)

Every generated document MUST carry a running footer on every page:

- **Left**: a short document identifier — typically
  `[Document title] — Civil Action File No. [number]` (e.g.,
  `Motion to Dismiss — Civil Action File No. ____________`). Keep it
  to a single line so it never wraps; this places the title at the
  bottom of each page.
- **Right**: `Page X of Y`, where `X` is the current page number and
  `Y` is the total page count. Use Word's `PAGE` and `NUMPAGES`
  fields — never a static number.
- **Font**: matches the body font family, may be slightly smaller
  (10 pt).
- **Alignment**: a right-aligned tab stop at 9,360 DXA (6.5") places
  the page counter flush right while the title stays flush left.

The footer runs continuously from page 1 through the last exhibit
page — do not restart or suppress pagination anywhere.

## Margin rule (double vertical line) — applied BY DEFAULT

Draw a double vertical rule — two thin parallel lines (~0.75 pt each,
with a ~7 pt gap between them) — down the left margin between the line
numbers and the body text. It is the standard companion to
line-numbered pleading paper. Like line numbering, no Georgia rule
requires it, but it is universal convention across this marketplace.
Apply it **by default** to every line-numbered pleading; exhibits and
attachments are exempt.

Implement it as two independent full-height line shapes anchored in
the page header, so they repeat on every page — **not** as an OOXML
`double` page border, whose style couples the inter-line gap to the
line weight (widening the gap thickens both lines into heavy bars).

Draw each line as a thin filled rectangle (VML `v:rect`). **One shape
per `<w:pict>`** — multiple `<v:rect>` elements in a single `<w:pict>`
will not all render; each rectangle needs its own `<w:pict>` inside
its own `<w:r>` run.

`docx-js` has no first-class API for header-anchored VML shapes. Add
them with the docx skill's **unpack → edit → pack** workflow: generate
the file with docx-js (give each section an empty `Header` so a
`word/header1.xml` part exists, and keep the `lineNumbers` section
property from above), then rewrite the header XML and repack:

```bash
python scripts/office/unpack.py out.docx unpacked/
#   ... inject the rule into unpacked/word/header*.xml (helper below) ...
python scripts/office/pack.py unpacked/ out.docx --original out.docx
```

Inside each `unpacked/word/header*.xml`, declare the VML namespace on
the root `<w:hdr>` and add the two runs — one `v:rect` per `<w:pict>`
per `<w:r>` — inside the header paragraph. A document can have several
header parts (first-page / even / default, or one per section); add
the runs to **each** distinct `word/header*.xml`, giving every
`v:rect` a unique `id`. This stdlib helper (no `python-docx`) does it
and is idempotent:

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

**Geometry** (US Letter, 1-inch margins, line-number `distance` 360
twips = ¼″): body text starts at 72 pt and the line-number gutter at
~54 pt, so the two rules at `margin-left` **60 pt** and **67 pt** sit
~7 pt apart, clear of both. The gap is the difference of the two
values; `margin-top:21.6pt` + `height:748.8pt` spans the full page
height; `width:0.75pt` is the line weight.

Verify with `python scripts/office/validate.py out.docx` then
`python scripts/office/soffice.py --headless --convert-to pdf
out.docx`; confirm two thin parallel lines with a clear gap between
the numbers and the text on **every** page and that the header /
footer text is not line-numbered. Then open the `.docx` in Microsoft
Word, where VML renders slightly differently and the output must still
be correct.

## Caption structure (O.C.G.A. § 9-11-10(a))

A Georgia caption carries (1) the **name of the court and the
county**, centered at the top; (2) the **party block** with the party
designations; (3) the **file number** — labeled **"Civil Action File
No."**; and (4) the **title of the document**. The court identifier is
centered and in ALL CAPS:

```
                  IN THE SUPERIOR COURT OF [COUNTY] COUNTY
                            STATE OF GEORGIA

JANE DOE,                          )
                                   )
       Plaintiff,                  )
                                   )    Civil Action
v.                                 )    File No. ____________
                                   )
ACME COLLECTIONS, LLC,             )
                                   )
       Defendant.                  )
```

The court identifier takes one of these forms (confirm the exact
court name against the venue skill):

- **Superior Court**: `IN THE SUPERIOR COURT OF [COUNTY] COUNTY,
  STATE OF GEORGIA` (general jurisdiction — divorce, equity, title to
  land, felonies, and all civil matters not exclusively elsewhere).
- **State Court**: `STATE COURT OF [COUNTY] COUNTY` (or `IN THE STATE
  COURT OF [COUNTY] COUNTY, STATE OF GEORGIA`) — limited jurisdiction
  but **no civil dollar ceiling**; most debt-collection and tort
  suits are filed here. See `ga-state-court`.
- **Magistrate Court**: `IN THE MAGISTRATE COURT OF [COUNTY] COUNTY,
  STATE OF GEORGIA` — small-claims and dispossessory matters within
  the statutory civil cap. See `ga-magistrate`.

### The caption elements in order

1. **Court and county.** The court name and county centered at the top
   of the page, with `STATE OF GEORGIA` on the line below (or appended
   to the court line). Match the court to the venue skill.
2. **Party block** (left side). The parties stacked with their
   designations, separated by a `v.`:
   - **Plaintiff / Defendant** in general civil actions;
   - **Petitioner / Respondent** in divorce, family-law, and most
     special proceedings.
   In the **complaint**, name **all** parties (§ 9-11-10(a)); in
   later pleadings, naming the **first party on each side** with
   "et al." is sufficient.
3. **File number** (right side, opposite the party block). Labeled
   **`Civil Action File No. ____________`** — left blank on an
   initial complaint (the clerk assigns it on filing) and populated on
   every subsequent paper. A column of right parentheses `)`
   conventionally divides the party block from the file-number block.
4. **Document title.** A centered ALL-CAPS heading below the caption
   (e.g., `PLAINTIFF'S COMPLAINT` or `MOTION TO DISMISS`), and
   restated in the footer so it sits at the bottom of every page.

## Numbered paragraphs and the body

Under **O.C.G.A. § 9-11-10(b)**, all averments are made in **numbered
paragraphs**, each limited so far as practicable to a single set of
circumstances. Number with an Arabic numeral, a period, and a tab.
State separate causes of action in **separate counts** where
separation aids clarity. Under **§ 9-11-8** the body is a short and
plain statement of the claim; alternative and inconsistent pleading is
permitted.

## Initiating pleading and responsive pleading — terminology

- The **initiating pleading** is the **Complaint** (§ 9-11-7).
- The **responsive pleading** is the **Answer**, which raises defenses
  and any compulsory counterclaim. See `ga-first-30-days`.
- The pleadings allowed and their designations are fixed by
  **§ 9-11-7(a)** — match the caption designation to the pleading
  type.

## Signing (O.C.G.A. § 9-11-11) and the signature block

Under § 9-11-11 every pleading is **signed** by at least one attorney
of record in the attorney's individual name (or by the party if
self-represented), and must state the signer's **address**. A licensed
attorney includes the **Georgia Bar No.**:

```
                                   /s/ [Name]
                                   [Name]
                                   Georgia Bar No. ________
                                   [Firm name]
                                   [Street address]
                                   [City, GA  ZIP]
                                   Tel: (###) ###-####
                                   Email: name@example.com
                                   Attorney for [Party]
```

**Self-represented filers omit the Georgia Bar No.** and identify as
pro se:

```
                                   /s/ [Name]
                                   [Name]
                                   [Street address]
                                   [City, GA  ZIP]
                                   Tel: (###) ###-####
                                   Email: name@example.com
                                   [Party], Pro Se
```

There is **no general verification requirement** under § 9-11-11 —
most pleadings need only the signature, not a notarized verification —
but certain equitable and extraordinary actions require verification
by statute or rule; confirm before omitting one. See `ga-pro-se` for
the full self-represented drafting framework.

## Certificate of service (O.C.G.A. § 9-11-5)

Every pleading and paper subsequent to the original complaint must be
**served** on the other parties under § 9-11-5 and carry a
**certificate of service**. Place it at the foot of the document:

```
                   CERTIFICATE OF SERVICE

I certify that on [date] I served a true and correct copy of the
foregoing [Document Title] on all parties of record in accordance
with O.C.G.A. § 9-11-5:

  [Opposing party / counsel name]
  [Address / email]
  by [the court's electronic-filing/e-service system (PeachCourt /
      Odyssey eFileGA) / statutory overnight or U.S. first-class
      mail, postage prepaid / email / hand delivery as permitted by
      O.C.G.A. § 9-11-5].

                                   /s/ [Signer name]
                                   [Signer name]
```

Section 9-11-5 prescribes the permitted methods of service for
subsequent papers. The **original complaint** is served by **summons
under O.C.G.A. § 9-11-4** (personal service, service on an agent, or
the statutory alternatives including service by publication) — not by
§ 9-11-5. See `ga-first-30-days`.

## Filing mechanics: e-filing (USCR 36; PeachCourt / Odyssey eFileGA)

Georgia electronic filing is governed by **USCR 36** and is handled
through county-dependent portals — chiefly **PeachCourt** and
**Odyssey eFileGA** (the platform varies by county; check the filing
county's posture). E-filing of civil matters is mandatory in many
counties pursuant to the statewide e-filing mandate.

- Confirm **which portal** your filing county uses before assembling a
  packet — it differs county to county.
- Some portals **auto-generate** intake documents (case-initiation
  form, summons, sheriff's entry of service) and, in domestic cases,
  auto-attach a standing order — confirm against the venue skill.
- **Self-represented filers** may e-file where the county permits;
  otherwise file by paper at the clerk's window. Confirm the venue's
  posture.

See the venue skills and `ga-file-packet` for the full e-filing
workflow.

## Citation format

Georgia legal citation follows the Georgia appellate conventions
(Bluebook-based). Common forms:

- **Statutes**: `O.C.G.A. § 9-11-10` — always use the `§` symbol for
  Georgia statutes.
- **Uniform Rules**: `USCR 6.2` (no section symbol for rules); cite
  the Uniform State Court Rules and Uniform Magistrate Court Rules by
  their own numbering.
- **Supreme Court of Georgia**: `Smith v. Jones, 308 Ga. 204, 839
  S.E.2d 651 (2020)`.
- **Court of Appeals of Georgia**: `Doe v. Roe, 350 Ga. App. 123, 828
  S.E.2d 456 (2019)`.
- **Regional reporter**: cite the **South Eastern Reporter**
  (`S.E.2d` / `S.E.`) in parallel with the official `Ga.` / `Ga. App.`
  reporter.
- **Federal statutes**: `15 U.S.C. § 1692g`.

Italicize case names (including `v.`). See `ga-fact-check` for citation
verification against the corpus.

## Producing documents programmatically

For `.docx` generation, use the `docx` npm package. Key points:

- Set page size explicitly to US Letter (12,240 × 15,840 DXA) — the
  library defaults to A4.
- Use Times New Roman at `size: 24` (half-points = 12 pt), or Arial
  12 pt, with double line spacing in the body.
- Apply uniform 1,440 DXA margins to all four sides on every section.
- Build the caption with the court name + county centered at the top,
  a `)`-divided party-block / file-number layout, and `Civil Action
  File No. ____________` on the right.
- Build the footer with a right-aligned tab stop at 9,360 DXA and use
  `PageNumber.CURRENT` / `PageNumber.TOTAL_PAGES` for "Page X of Y";
  carry the document title at the left so it sits at the bottom of
  each page.
- Apply the `lineNumbers` section property above (omit `start`); set
  it on every section if you use a two-section page-1 layout.

Run `scripts/format-check.py` on the generated `.docx` to validate the
baseline.

## Composition

- For Fulton County courts: `ga-fulton`
- For Cobb County courts: `ga-cobb`
- For Gwinnett County courts: `ga-gwinnett`
- For State Court venue and the no-dollar-ceiling civil docket:
  `ga-state-court`
- For Magistrate Court small-claims / dispossessory matters:
  `ga-magistrate`
- For other counties' courts: `ga-county-courts`
- For drafting specific document types: `ga-draft-motion`,
  `ga-draft-declaration`, `ga-draft-note`, `ga-draft-order`
- For pro se conventions: `ga-pro-se`
- For pre-filing QC: `ga-quality-check`

## References

- `references/templates/declaration.md` — declaration / affidavit with
  numbered paragraphs and exhibits
- `references/templates/motion.md` — motion scaffold with caption,
  body, signature block, and certificate of service
- `references/templates/notice-of-hearing.md` — notice placing a
  motion on the court's calendar
- `references/templates/proposed-order.md` — proposed order for judge
  signature
- `references/caption-format.md` — caption structure with the O.C.G.A.
  § 9-11-10(a) layout and docx-js recipe
- `references/certificate-of-service.md` — § 9-11-5 certificate of
  service forms and service methods
- `references/citation-format.md` — Georgia citation conventions
