---
name: az-statewide-format-codearranger
title: Arizona Statewide Court Document Formatting
description: 'Use when the user asks to "format an Arizona pleading", "draft an Arizona court document", "apply Ariz. R. Civ. P. 10", "build an Arizona caption", "format an Arizona complaint", or "format an Arizona motion" for any Arizona state court — Superior Court, Justice Court, or family-law proceeding. Triggers: "Arizona caption", "Ariz. R. Civ. P. 10", "form of pleadings Arizona", "Rule 7.1 motion", "AZTurboCourt", "Arizona e-filing", "certificate of service Arizona", "line numbering", "Arizona motion format", "how do I format an Arizona complaint". Covers the Ariz. R. Civ. P. 10 caption form, numbered paragraphs, Rule 11 signature block with State Bar bar number, Rule 5 electronic filing via AZTurboCourt, certificate of service, line-numbered pleading paper, footer conventions, and Arizona citation format.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-statewide-format
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Arizona Statewide Court Document Formatting

> **NOT LEGAL ADVICE.** This skill assists with drafting and
> formatting only. Verify against the current Arizona Rules of
> Civil Procedure and the local rules and administrative orders
> of the filing court before submitting any document.

Use these conventions whenever drafting a paper to be filed in an
Arizona state trial court. The form of an Arizona court document
is governed primarily by **Ariz. R. Civ. P. 10** (form of
pleadings) and **Ariz. R. Civ. P. 7.1** (form and presentation of
motions), supplemented by **Ariz. R. Civ. P. 11** (signing of
documents and sanctions) and **Ariz. R. Civ. P. 5 / 5.1** (service
and filing, including electronic filing).

## Governing rules

- **Ariz. R. Civ. P. 10(a)** — the caption: every pleading must
  have a caption **in the form prescribed by Ariz. R. Civ. P.
  5.2(a)** and carry the pleading's designation; the complaint's
  title must name all parties, and other documents may use
  "*et al.*" after the first party on each side.
- **Ariz. R. Civ. P. 5.2(a)** — the actual caption **form**: the
  upper-left block with the filer's name, address, phone, email,
  and (for an attorney) the **State Bar of Arizona attorney
  identification number** and party represented; the centered court
  title; the action title; the case number; the document
  description; and the assigned judge.
- **Ariz. R. Civ. P. 10(b)** — allegations are stated in
  **numbered paragraphs**, each limited as far as practicable to a
  single set of circumstances; claims founded on separate
  transactions are stated in separate counts.
- **Ariz. R. Civ. P. 10(c)** — adoption by reference and exhibits;
  a written instrument attached as an exhibit is part of the
  pleading for all purposes.
- **Ariz. R. Civ. P. 7.1** — form of motions, including the
  requirement that a motion state the grounds and the relief
  sought, and the procedure for **requesting oral argument**.
- **Ariz. R. Civ. P. 11** — the **signature requirement and
  sanctions** provision: every document must be signed, and the
  signature certifies the representations the rule prescribes.
- **Ariz. R. Civ. P. 5** — service of pleadings and other papers
  and the proof/certificate of service.
- **Ariz. R. Civ. P. 5.1** — electronic filing through the court's
  designated system (**AZTurboCourt**).

Pull the verbatim rule text from the `az-law-references` corpus at
`../az-law-references/references/court-rules/` before relying on
any specific paper, margin, or font figure — those values live in
the rule text and the local rules, not in this skill, so they
never drift here.

## Paper and legibility

File on **letter-size (8½ × 11 inch)** paper of standard quality,
black ink on white, with a legible serif body font. Confirm the
current margin, font, and spacing figures against the verbatim
rule text and any applicable local rule in the corpus — this skill
defers those values rather than embedding numbers that may change.
Customary practice:

| Item | Practice |
|------|----------|
| Paper size | US Letter, 8½ × 11 inches |
| Body font | A legible serif, commonly 12 point |
| Ink | Black on white |
| Page numbers | Each page numbered; `Page X of Y` in the footer |

`scripts/format-check.py` validates a generated `.docx` against
the Ariz. R. Civ. P. 10 baseline and flags departures.

## Line numbering (pleading paper) — applied BY DEFAULT

Apply continuous line numbering down the left margin of every
generated Arizona pleading. Line numbers count every body line and
**restart on each page**.

Ariz. R. Civ. P. 10 does not itself require line numbering, and an
Arizona document filed without line numbers is rule-compliant. But
line-numbered pleading paper is the universal convention across
this marketplace: it lets the court and opposing counsel cite an
exact location ("page 4, lines 12–15") and never harms an Arizona
filing. Apply it **by default** to every motion, brief,
declaration, affidavit, notice, and proposed order. Exhibits and
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

If the first page uses a different top margin from later pages (to
seat the caption block), use a **two-section** layout — and set
`lineNumbers` on **both** sections, or numbering stops at the
section break. As an alternative to two sections, push page-1
content down with a leading paragraph's `spacing: { before: ... }`.
Confirm whether the filing court sets a larger page-1 top margin
against the rule text before adding the second section; if it does
not, still apply the footer and line numbers.

## Required footer (mandatory on every generated document)

Every generated document MUST carry a running footer on every
page:

- **Left**: a short document identifier — typically
  `[Document title] — Case No. [case number]`. Keep it to a single
  line so it never wraps.
- **Right**: `Page X of Y`, where `X` is the current page number
  and `Y` is the total page count. Use Word's `PAGE` and
  `NUMPAGES` fields — never a static number.
- **Font**: 10 pt; matches body font family.
- **Alignment**: a right-aligned tab stop at 9,360 DXA (6.5")
  places the page counter flush right while the title stays flush
  left.

The footer runs continuously from page 1 through the last exhibit
page — do not restart or suppress pagination anywhere.

## Caption structure (Ariz. R. Civ. P. 10(a) / 5.2(a))

Ariz. R. Civ. P. 10(a) requires the caption to be **in the form
prescribed by Ariz. R. Civ. P. 5.2(a)**. That form calls for the
**court** title, the **party** (action) title, the **case
number**, a **description** of the document, the assigned **judge**
(if known), and an upper-left filer-identification block (name,
address, phone, email, and — for an attorney — the State Bar of
Arizona attorney identification number). Confirm the exact
placement and line positions against Rule 5.2(a) in the corpus. The
Arizona caption stacks these elements:

```
        IN THE SUPERIOR COURT OF THE STATE OF ARIZONA

              IN AND FOR THE COUNTY OF MARICOPA

JANE DOE,                          )   No. ____________________
                                   )
       Plaintiff,                  )   The Honorable ___________
                                   )
v.                                 )
                                   )   [DOCUMENT TITLE]
ACME COLLECTIONS, LLC,             )
                                   )
       Defendant.                  )
___________________________________)
```

### The caption elements in order

1. **Court identifier block** (centered, ALL CAPS):
   - Superior Court: `IN THE SUPERIOR COURT OF THE STATE OF
     ARIZONA` / `IN AND FOR THE COUNTY OF [COUNTY]`.
   - Justice Court: `IN THE [PRECINCT NAME] JUSTICE COURT` /
     `[COUNTY] COUNTY, STATE OF ARIZONA` — see `az-justice-courts`
     for precinct naming and the limited-jurisdiction caption.
   - Family-law matters proceed in Superior Court; many use the
     `In re the Marriage of [names]` or `In re the Matter of`
     in-rem caption — see `az-family-court`.
2. **Party block.** On the left, the parties stacked with their
   designations, separated by a centered `v.`:
   - **Plaintiff / Defendant** for general civil actions;
   - **Petitioner / Respondent** in dissolution and many special
     proceedings.
   A column of right-hand parentheses (or a vertical rule) sets the
   party block off from the case-number / judge column, closed at
   the bottom by a horizontal line.
3. **Case-number / judge column** (right side). `No.
   ____________________` carries the case number — blank on an
   initial filing (the clerk assigns and stamps it) and populated
   on every subsequent paper. Add the assigned judge or division:
   `The Honorable ____________________`. For the county-specific
   case-number prefixes and division/department custom, see
   `az-maricopa`, `az-pima`, and `az-superior-courts`.
4. **Document title** (centered, ALL CAPS) below the caption rule:
   e.g., `COMPLAINT`, `ANSWER`, `MOTION TO DISMISS`,
   `MOTION FOR SUMMARY JUDGMENT`.

## Numbered paragraphs (Ariz. R. Civ. P. 10(b))

Under Ariz. R. Civ. P. 10(b), the allegations of a pleading are
made in **numbered paragraphs**, each limited as far as practicable
to a single set of circumstances; later paragraphs may **adopt by
reference** earlier ones. Number with an Arabic numeral, a period,
and a tab: `1.\tDefendant is a resident of Maricopa County,
Arizona.` State claims founded on separate transactions in separate
counts where separation aids clarity.

## Exhibits and adoption by reference (Ariz. R. Civ. P. 10(c))

Under Ariz. R. Civ. P. 10(c), a statement in a pleading may be
adopted by reference elsewhere in the same pleading, and a copy of
a written instrument that is an exhibit is part of the pleading for
all purposes. Reference each exhibit by letter in the body ("a true
copy of the [instrument] is attached as **Exhibit A**") and attach
the copies after the signature block and certificate of service.

## Form of motions (Ariz. R. Civ. P. 7.1)

Under Ariz. R. Civ. P. 7.1, a motion must state with particularity
the grounds for the relief sought and the relief or order sought.
A motion is presented with its supporting memorandum; the rule and
any applicable local rule govern page limits and the briefing
schedule (response and reply), so confirm those against the corpus.

A party who wants **oral argument** requests it as the rule
provides — typically by a notation in the caption or title of the
motion or response (e.g., `(Oral Argument Requested)`). Confirm the
current mechanics and any time limit against the verbatim Rule 7.1
text in the corpus. See `az-draft-motion` for the motion scaffold
and `az-hearings` for argument practice.

## Signature block (Ariz. R. Civ. P. 11)

Under Ariz. R. Civ. P. 11, every document must be **signed** by at
least one attorney of record in the attorney's own name, or, if the
party is self-represented, **by the party**. The signature
certifies the representations the rule prescribes — that the
document is warranted by existing law or a non-frivolous argument
and is not interposed for an improper purpose — and the rule
carries **sanctions** for a violation.

An attorney's signature block must include the attorney's **State
Bar of Arizona bar number**:

```
Respectfully submitted,


                                   ____________________________
                                   [Name], Bar No. ______
                                   [Firm name]
                                   [Street address]
                                   [City, AZ ZIP]
                                   Phone: (###) ###-####
                                   Email: name@example.com
                                   Attorney for [Party]
```

**Self-represented filers omit the bar number** and identify as
self-represented:

```
                                   ____________________________
                                   [Name]
                                   [Street address]
                                   [City, AZ ZIP]
                                   Phone: (###) ###-####
                                   Email: name@example.com
                                   Self-Represented [Party]
```

See `az-pro-se` for the full self-represented drafting framework.

## Certificate of service (Ariz. R. Civ. P. 5)

Every paper required to be served on the other parties is
accompanied by a **certificate of service** under Ariz. R. Civ. P.
5. Place it at the foot of the document:

```
                   CERTIFICATE OF SERVICE

I certify that on [date] I served a copy of the foregoing
[Document Title] on:

  [Opposing party / counsel name]
  [Address]
  by [the court's electronic-filing system (AZTurboCourt) /
      first-class mail, postage prepaid / personal delivery /
      email as permitted by Ariz. R. Civ. P. 5].

                                   ____________________________
                                   [Signer name]
```

Ariz. R. Civ. P. 5 prescribes the permitted methods of serving
subsequent papers. Initial process (the summons and complaint) is
served under **Ariz. R. Civ. P. 4 / 4.1 / 4.2**, not Rule 5.

## Filing mechanics: AZTurboCourt (Ariz. R. Civ. P. 5.1)

Arizona's statewide electronic-filing portal is **AZTurboCourt**.
Electronic filing is **mandatory** in many Superior Courts and is
governed by Ariz. R. Civ. P. 5.1 and the court's administrative
orders, which control the form and signature of electronically
filed documents. Confirm whether the venue mandates e-filing and
which document types it accepts before assembling a packet. See the
venue skills and `az-file-packet`.

## Citation format

Arizona filings follow standard legal citation (the Bluebook), with
Arizona-specific reporters:

- Arizona Supreme Court: `State v. Smith, 250 Ariz. 1, 475 P.3d 100
  (2020)` — the official `Ariz.` reporter plus the Pacific Reporter
  parallel.
- Arizona Court of Appeals: `Smith v. Jones, 250 Ariz. 1, 480 P.3d
  200 (App. 2020)`.
- Statutes: `A.R.S. § 12-541`.
- Court rules: `Ariz. R. Civ. P. 56(a)`; evidence rules:
  `Ariz. R. Evid. 803(6)`.

See `az-fact-check` for citation verification against the corpus.

## Producing documents programmatically

For `.docx` generation, use the `docx` npm package. Key points:

- Set page size explicitly to US Letter (12,240 × 15,840 DXA) —
  the library defaults to A4.
- Use a legible serif at the Ariz. R. Civ. P. 10 / local-rule
  minimum size.
- Build the footer with a right-aligned tab stop at 9,360 DXA and
  use `PageNumber.CURRENT` / `PageNumber.TOTAL_PAGES` for
  "Page X of Y".
- Apply the `lineNumbers` section property above (omit `start`);
  set it on every section if you use a two-section page-1 layout.

Run `scripts/format-check.py` on the generated `.docx` to validate
the Ariz. R. Civ. P. 10 baseline.

## Composition

- For Maricopa County (Phoenix): `az-maricopa`
- For Pima County (Tucson): `az-pima`
- For other Superior Courts: `az-superior-courts`
- For Justice Court (limited jurisdiction): `az-justice-courts`
- For drafting specific document types: `az-draft-motion`,
  `az-draft-declaration`, `az-draft-note`, `az-draft-order`
- For pro se conventions: `az-pro-se`
- For pre-filing QC: `az-quality-check`
- For citation verification: `az-fact-check`

## References

- `az-law-references` — canonical Ariz. R. Civ. P., Ariz. R.
  Evid., A.R.S., and local-rules corpus at
  `../az-law-references/references/court-rules/`
- `scripts/format-check.py` — Ariz. R. Civ. P. 10 format validation
