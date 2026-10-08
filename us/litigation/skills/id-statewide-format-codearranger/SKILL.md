---
name: id-statewide-format-codearranger
title: Idaho Statewide Court Document Formatting
description: 'Use when the user asks to "format an Idaho pleading", "draft an Idaho court document", "apply I.R.C.P. 2", "apply I.R.C.P. 10", "build an Idaho caption", "format an Idaho complaint", or "format an Idaho motion" for any Idaho District Court or Magistrate Division matter. Triggers: "Idaho caption", "I.R.C.P. 10 caption", "I.R.C.P. 2 form of documents", "form of pleadings Idaho", "Rule 7(b) motion Idaho", "iCourt e-filing", "iCourt E-File", "Odyssey File & Serve Idaho", "I.R.E.F.S.", "ISB number", "Idaho State Bar number", "certificate of service Idaho", "line numbering", "title at the bottom of the page Idaho", "3 inches from the top Idaho", "how do I format an Idaho complaint". Covers the I.R.C.P. 2 form-of-documents spec, the I.R.C.P. 10 caption and numbered paragraphs, the I.R.C.P. 11 signature block with the Idaho State Bar (ISB) number, I.R.E.F.S. electronic filing through iCourt, the certificate of service, line-numbered pleading paper, footer conventions, and Idaho citation
  format.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/id-court-docs/skills/id-statewide-format
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Idaho Statewide Court Document Formatting

> **NOT LEGAL ADVICE.** This skill assists with drafting and
> formatting only. Verify against the current Idaho Rules of Civil
> Procedure, the Idaho Rules for Electronic Filing and Service, and
> the local rules and administrative orders of the filing judicial
> district before submitting any document.

Use these conventions whenever drafting a paper to be filed in an
Idaho trial court — the **District Court** or its **Magistrate
Division**. The form of an Idaho court document is governed
primarily by **I.R.C.P. 2** (Form of Documents; Caption), which
carries Idaho's statewide format spec, supplemented by **I.R.C.P.
10** (Form of Pleadings; numbered paragraphs; exhibits), **I.R.C.P.
11** (Signing; representations; sanctions), and **I.R.C.P. 5**
(service and filing of subsequent papers). Electronically filed
documents are additionally governed by the **Idaho Rules for
Electronic Filing and Service (I.R.E.F.S.)**.

## Governing rules

- **I.R.C.P. 2** — Form of Documents and Caption: the statewide
  spec for paper, ink, font, spacing, margins, the position of the
  title of court and the attorney/party block, and the placement of
  the document title. The caption must carry the names of the
  parties, the title of the court, the case number, and the title
  of the document.
- **I.R.C.P. 10** — Form of Pleadings: cross-references the caption
  form in Rule 2 and requires allegations stated in **numbered
  paragraphs**; a written instrument attached as an exhibit is part
  of the pleading.
- **I.R.C.P. 11** — Signing of documents: every document must be
  signed; the signature makes the representations the rule
  prescribes, and the rule carries **sanctions** for a violation.
- **I.R.C.P. 5** — service and filing of papers after the original
  complaint, and the certificate of service.
- **I.R.C.P. 4** — service of the summons and complaint (initial
  process); the summons must be served within **182 days** of
  filing the complaint.
- **I.R.E.F.S.** — the electronic-filing-and-service rules:
  I.R.E.F.S. 4 (who must e-file), I.R.E.F.S. 6 (document form / PDF
  and size requirements), I.R.E.F.S. 17 (e-filing as consent to
  electronic service).

Pull the verbatim rule text from the `id-law-references` corpus at
`../id-law-references/references/court-rules/` before relying on
any specific paper, margin, font, or spacing figure — those values
live in the rule text and never drift here.

## Paper and legibility (I.R.C.P. 2)

File on **letter-size (8½ × 11 inch)** white paper in **black ink**.
I.R.C.P. 2 sets the baseline spec; confirm the current figures
against the verbatim rule text in the corpus rather than treating
the numbers below as fixed. Customary, rule-anchored practice:

| Item | Practice (verify against I.R.C.P. 2) |
|------|--------------------------------------|
| Paper / ink | US Letter, 8½ × 11 in., black ink on white |
| Font | At least **11 point** |
| Line spacing | **Double** or **1½** spacing |
| Margins | **≥ 1.2"** top and sides; **≥ 1"** bottom (slightly smaller permitted only to fit a single page) |
| Title of court | Begins **≥ 3"** from the top of page 1 |
| Attorney/party block | Above the title of court, **left of center**, beginning **≥ 1.2"** below the top of page 1 |
| Document title | Appears at the **BOTTOM of each page** |
| Page numbers | Each page numbered; `Page X of Y` in the footer |

`scripts/format-check.py` validates a generated `.docx` against the
I.R.C.P. 2 baseline and flags departures.

## Line numbering (pleading paper) — applied BY DEFAULT

Apply continuous line numbering down the left margin of every
generated Idaho pleading. Line numbers count every body line and
**restart on each page**.

I.R.C.P. 2 does not itself require line numbering, and an Idaho
document filed without line numbers is rule-compliant. But
line-numbered pleading paper is the universal convention across
this marketplace: it lets the court and opposing counsel cite an
exact location ("page 4, lines 12–15") and never harms an Idaho
filing. Apply it **by default** to every motion, memorandum,
affidavit, declaration, notice, and proposed order. Exhibits and
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

This emits `<w:lnNumType w:countBy="1" w:restart="newPage"/>` into
the section's `<w:sectPr>`. The numbers render in the left margin
and do not shift the text margin.

**Do NOT set `start` explicitly.** An explicit `start: 1` renders
off by one in LibreOffice (the first body line shows "2"). Omit
`start` — it defaults to 1 in OOXML.

### Page-1 top margin: title of court ≥ 3" from the top

I.R.C.P. 2 requires the **title of court to begin at least 3 inches
from the top of page 1** (with the attorney/party block seated above
it, ≥ 1.2" below the top). Page 1 therefore uses a deeper top
offset than later pages. Achieve this one of two ways:

1. **Two-section layout** — give the first section a larger page-1
   top margin (or top inset) to seat the caption block, and a
   normal top margin for the continuation section. If you use two
   sections, **set `lineNumbers` on BOTH sections**, or numbering
   stops at the section break.
2. **Single section with a leading paragraph** — push page-1 content
   down with a leading paragraph's `spacing: { before: ... }` sized
   to clear 3 inches, keeping one section.

Either way, confirm the exact 3" / 1.2" figures against the I.R.C.P.
2 text in the corpus before relying on them.

## Required footer (mandatory on every generated document)

Every generated document MUST carry a running footer on every page.
This footer also satisfies I.R.C.P. 2's requirement that the
**document title appear at the bottom of each page**:

- **Left**: the document title (and, conventionally, the case
  number) — e.g., `COMPLAINT — Case No. CV__-__-_____`. Keep it to a
  single line so it never wraps. This places the title at the
  bottom of each page as Rule 2 requires.
- **Right**: `Page X of Y`, where `X` is the current page number and
  `Y` is the total page count. Use Word's `PAGE` and `NUMPAGES`
  fields — never a static number.
- **Font**: matches the body font family, may be slightly smaller.
- **Alignment**: a right-aligned tab stop places the page counter
  flush right while the title stays flush left.

The footer runs continuously from page 1 through the last exhibit
page — do not restart or suppress pagination anywhere.

## Caption structure (I.R.C.P. 2 / 10)

I.R.C.P. 10 requires the caption to be in the form prescribed by
I.R.C.P. 2. The caption carries (1) the **names of the parties**,
(2) the **title of the court**, (3) the **case number**, and (4) the
**title of the document**. The attorney/party identification block
sits **above** the title of court, **left of center**. Confirm the
exact line positions against I.R.C.P. 2 in the corpus.

```
[Name], ISB No. ______
[Firm / self-represented]
[Street address]
[City, ID  ZIP]
Phone: (###) ###-####
Email: name@example.com
Attorney for [Party]  /  [Party], Self-Represented


       IN THE DISTRICT COURT OF THE FOURTH JUDICIAL DISTRICT
       OF THE STATE OF IDAHO, IN AND FOR THE COUNTY OF ADA


JANE DOE,                          )
                                   )   Case No. ____________________
       Plaintiff,                  )
                                   )
v.                                 )
                                   )
ACME COLLECTIONS, LLC,             )
                                   )
       Defendant.                  )
___________________________________)
```

### The caption elements in order

1. **Attorney/party block** (upper left, above the court title,
   left of center): name; the **Idaho State Bar number** (`ISB No.
   ______`) for an attorney; firm or self-represented designation;
   address; phone; email; and whom the signer represents.
2. **Court identifier block** (centered, ALL CAPS):
   - `IN THE DISTRICT COURT OF THE [NTH] JUDICIAL DISTRICT OF THE
     STATE OF IDAHO, IN AND FOR THE COUNTY OF [COUNTY]`.
   - Matters in the **Magistrate Division** are captioned in the
     same District Court but note the Magistrate Division as the
     local rule and clerk direct — see `id-ada`, `id-bonneville`,
     and `id-county-courts`.
3. **Party block.** On the left, the parties stacked with their
   designations, separated by a centered `v.`:
   - **Plaintiff / Defendant** for general civil actions;
   - **Petitioner / Respondent** in family-law and many special
     proceedings.
4. **Case-number column** (right side). `Case No.
   ____________________` — blank on an initial filing (the clerk
   assigns it) and populated on every subsequent paper. For
   county/district case-number conventions see the venue skills.
5. **Document title.** Per I.R.C.P. 2 the document title belongs at
   the **bottom of each page** (carried in the footer above). Many
   filers also restate the title in a centered ALL-CAPS heading
   below the caption rule for readability — that is conventional and
   does not displace the Rule 2 bottom-of-page requirement.

## Numbered paragraphs (I.R.C.P. 10)

Under I.R.C.P. 10, the allegations of a pleading are made in
**numbered paragraphs**, each limited as far as practicable to a
single set of circumstances; later paragraphs may **adopt by
reference** earlier ones. Number with an Arabic numeral, a period,
and a tab: `1.\tDefendant is a resident of Ada County, Idaho.`
State claims founded on separate transactions in separate counts
where separation aids clarity. A copy of a written instrument
attached as an **exhibit is part of the pleading**.

## Form of motions (I.R.C.P. 7(b))

A motion under I.R.C.P. 7(b) must state with particularity the
grounds and the relief sought, and is supported by a **Memorandum**
(the brief). A motion noticed for hearing requires a **Notice of
Hearing** served and filed **at least 14 days before the hearing**
(I.R.C.P. 7(b)) — confirm the current notice period and any local
motion-calendar practice against the corpus. See `id-draft-motion`
for the motion scaffold and `id-hearings` for argument practice.

## Signature block (I.R.C.P. 11)

Under I.R.C.P. 11, every document must be **signed** — by an
attorney of record in the attorney's own name, or, if the party is
self-represented, **by the party**. The signature makes the
representations the rule prescribes (the filing is warranted by
existing law or a non-frivolous argument and is not interposed for
an improper purpose) and the rule carries **sanctions** for a
violation.

An attorney's signature block must include the **currently valid
Idaho State Bar number (ISB #)**:

```
                                   ____________________________
                                   [Name], ISB No. ______
                                   [Firm name]
                                   [Street address]
                                   [City, ID  ZIP]
                                   Phone: (###) ###-####
                                   Email: name@example.com
                                   Attorney for [Party]
```

**Self-represented filers omit the ISB number** and identify as
self-represented:

```
                                   ____________________________
                                   [Name]
                                   [Street address]
                                   [City, ID  ZIP]
                                   Phone: (###) ###-####
                                   Email: name@example.com
                                   [Party], Self-Represented
```

See `id-pro-se` for the full self-represented drafting framework.

## Certificate of service (I.R.C.P. 5)

Every paper required to be served on the other parties is
accompanied by a **certificate of service** under I.R.C.P. 5. Place
it at the foot of the document:

```
                   CERTIFICATE OF SERVICE

I certify that on [date] I served a copy of the foregoing
[Document Title] on:

  [Opposing party / counsel name]
  [Address / email]
  by [the iCourt E-File electronic-service system /
      first-class U.S. mail, postage prepaid / personal delivery /
      email as permitted by I.R.C.P. 5 and I.R.E.F.S. 17].

                                   ____________________________
                                   [Signer name]
```

I.R.C.P. 5 prescribes the permitted methods of serving subsequent
papers. Initial process (the summons and complaint) is served under
**I.R.C.P. 4** — and the summons must be served within **182 days**
of filing the complaint — not Rule 5.

## Filing mechanics: iCourt E-File (I.R.E.F.S.)

Idaho's statewide electronic-filing portal is **iCourt E-File**
(the Tyler Technologies Odyssey File & Serve platform), governed by
the **Idaho Rules for Electronic Filing and Service (I.R.E.F.S.)**.

- **Mandatory for attorneys** (I.R.E.F.S. 4(a)).
- **Optional for self-represented individuals** (I.R.E.F.S. 4(b)) —
  but **once a self-represented party opts in, they are bound to
  e-file for the life of the case.**
- **E-filing constitutes consent to electronic service** (I.R.E.F.S.
  17).
- Documents must meet the **PDF and size requirements** of
  I.R.E.F.S. 6.
- Odyssey **Guide & File** is the assisted self-help front end for
  self-represented filers.

Confirm whether the venue mandates e-filing and which document
types it accepts before assembling a packet. See the venue skills
and `id-file-packet`.

## Citation format

Idaho filings follow standard legal citation with Idaho-specific
reporters. Idaho has **no neutral / public-domain citation** —
always cite the Idaho Reports + Pacific Reporter parallel:

- Idaho Supreme Court: `Fitzgerald v. Walker, 113 Idaho 730, 747
  P.2d 752 (1987)` — the official `Idaho` reporter plus the Pacific
  Reporter parallel.
- Idaho Court of Appeals: `Murr v. Odmark, 112 Idaho 606, 733 P.2d
  827 (Ct. App. 1987)` — add `(Ct. App. YEAR)`.
- Statutes: `Idaho Code § 5-216` or `I.C. § 5-216`.
- Rules: `I.R.C.P. 56(a)`; evidence rules: `I.R.E. 803(6)`;
  appellate rules: `I.A.R. 14`.

See `id-fact-check` for citation verification against the corpus.

## Producing documents programmatically

For `.docx` generation, use the `docx` npm package. Key points:

- Set page size explicitly to US Letter (12,240 × 15,840 DXA) — the
  library defaults to A4.
- Use a legible font at the I.R.C.P. 2 minimum (≥ 11 point) with
  double or 1½ line spacing.
- Seat the title of court ≥ 3" from the top of page 1 (two-section
  layout or a leading-paragraph `spacing: { before }`), with the
  attorney/party block ≥ 1.2" below the top.
- Build the footer with a right-aligned tab stop and use
  `PageNumber.CURRENT` / `PageNumber.TOTAL_PAGES` for "Page X of Y";
  carry the document title at the left so it sits at the bottom of
  each page per I.R.C.P. 2.
- Apply the `lineNumbers` section property above (omit `start`); set
  it on every section if you use a two-section page-1 layout.

Run `scripts/format-check.py` on the generated `.docx` to validate
the I.R.C.P. 2 baseline.

## Composition

- For Ada County (Boise / Fourth Judicial District): `id-ada`
- For Bonneville County (Idaho Falls / Seventh Judicial District):
  `id-bonneville`
- For other counties and districts: `id-county-courts`
- For drafting specific document types: `id-draft-motion`,
  `id-draft-declaration`, `id-draft-note`, `id-draft-order`
- For pro se conventions: `id-pro-se`
- For pre-filing QC: `id-quality-check`
- For citation verification: `id-fact-check`
- For deadline computation: `id-deadlines`

## References

- `id-law-references` — canonical I.R.C.P., I.R.E., I.R.E.F.S.,
  Idaho Code, and local-rules corpus at
  `../id-law-references/references/court-rules/`
- `scripts/format-check.py` — I.R.C.P. 2 format validation
