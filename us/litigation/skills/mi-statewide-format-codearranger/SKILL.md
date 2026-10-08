---
name: mi-statewide-format-codearranger
title: Michigan Statewide Court Document Formatting
description: Use when formatting a Michigan pleading or court document. Triggers include "Michigan caption", "MCR 1.109", "MCR 2.113", "MiFILE", "proof of service Michigan", "P-number", "how do I format a Michigan complaint". Covers MCR 1.109 (document format, legibility, paper, caption, the MCR 1.109(E) signature requirement and sanctions, verification), MCR 2.113 (form of pleadings, caption, numbered paragraphs), the Michigan caption structure, the attorney's State Bar "P-number", proof of service under MCR 2.107, line-numbered pleading-paper conventions, the running footer, and Michigan citation format per the Michigan Appellate Opinion Manual. Canonical home for marketplace layout conventions for Michigan filings.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-statewide-format
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Michigan Statewide Court Document Formatting

> **NOT LEGAL ADVICE.** This skill assists with drafting and
> formatting only. Verify against the current Michigan Court
> Rules and the local administrative orders of the filing court
> before submitting any document.

Use these conventions whenever drafting a paper to be filed in a
Michigan state trial court. The form of a Michigan court document
is governed primarily by **MCR 1.109** (form, signing, and
electronic filing of court documents) and **MCR 2.113** (form of
pleadings), supplemented by **MCR 2.107** (service and proof of
service of subsequent papers).

## Governing rules

Michigan publishes statewide formatting requirements directly in
the Michigan Court Rules — there is no per-county format code that
displaces them:

- **MCR 1.109(D)** — form of court documents: legibility, paper
  size and quality, captioning, and the requirement that each
  document be filed on letter-size paper.
- **MCR 1.109(D)(3)** — when a document must be **verified**, and
  the permitted forms of verification.
- **MCR 1.109(E)** — the **signature requirement and sanctions**
  provision. Every document of a party represented by an attorney
  must be signed by at least one attorney of record; a
  self-represented party signs personally. The signature is the
  certification that the document is well grounded in fact and
  warranted by law, the Michigan analog of the federal
  Rule 11 certification, with sanctions for violations.
- **MCR 2.113** — form of pleadings: the caption, numbered
  paragraphs, adoption by reference, and attachment of written
  instruments.
- **MCR 2.107** — service of subsequent papers and the proof of
  service that must accompany a filed document.

Pull the verbatim rule text from the `mi-law-references` corpus at
`../mi-law-references/references/court-rules/` before relying on
any specific paper, margin, or font figure — those values live in
the rule text, not in this skill, so they never drift here.

## Paper and legibility (MCR 1.109(D)(1))

MCR 1.109(D)(1) requires every filed document to be **legible** and
on **letter-size (8½ × 11 inch) paper** of standard quality, with
the form requirements (margins, font legibility, captioning)
prescribed in the subrule. Confirm the current margin, font, and
spacing figures against the verbatim rule in the corpus — this
skill defers those values to MCR 1.109(D) rather than embedding
numbers that may change. Customary practice, consistent with the
rule:

| Item | Practice |
|------|----------|
| Paper size | US Letter, 8½ × 11 inches |
| Body font | A legible serif at no smaller than the rule's minimum (commonly 12 point) |
| Ink | Black on white |
| Page numbers | Each page numbered; `Page X of Y` in the footer |

`scripts/format-check.py` validates a generated `.docx` against
the MCR 1.109(D) baseline and flags departures.

## Line numbering (pleading paper) — applied BY DEFAULT

Apply continuous line numbering down the left margin of every
generated Michigan pleading. Line numbers count every body line
and **restart on each page**.

MCR 1.109 and MCR 2.113 do **not** themselves require line
numbering, and a Michigan document filed without line numbers is
rule-compliant. But line-numbered pleading paper is the universal
convention across the `claude-legal` marketplace: it lets the
court and opposing counsel cite an exact location ("page 4, lines
12–15") and never harms a Michigan filing. Apply it **by default**
to every motion, brief, declaration, affidavit, notice, and
proposed order. Exhibits and attachments are exempt.

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

## Required footer (mandatory on every generated document)

Every generated document MUST carry a running footer on every
page:

- **Left**: a short document identifier — typically
  `[Document title] — Case No. [case number]` (e.g.,
  `Motion for Summary Disposition — Case No. 25-123456-CZ`). Keep
  it to a single line so it never wraps.
- **Right**: `Page X of Y`, where `X` is the current page number
  and `Y` is the total page count. Use Word's `PAGE` and
  `NUMPAGES` fields — never a static number.
- **Font**: 10 pt; matches body font family.
- **Alignment**: a right-aligned tab stop at 9,360 DXA (6.5")
  places the page counter flush right while the title stays flush
  left.

The footer runs continuously from page 1 through the last exhibit
page — do not restart or suppress pagination anywhere.

## Caption structure (MCR 1.109(D) + MCR 2.113(C))

MCR 1.109(D) sets the caption form and MCR 2.113(C) requires the
first page of every pleading to contain a caption stating the
**name of the court**, the **case number** (with the case-type
code), the **parties**, and the **identity** of the document. The
Michigan caption stacks four elements:

```
                    STATE OF MICHIGAN

      IN THE CIRCUIT COURT FOR THE COUNTY OF WAYNE

VELOCITY INVESTMENTS, LLC,
                                       Case No. ____________-CZ
       Plaintiff,
                                       Hon. ____________________
v.

JOHN DOE,

       Defendant.
_________________________________________/

           MOTION FOR SUMMARY DISPOSITION
```

### The four caption elements in order

1. **Court identifier block** (centered, ALL CAPS). Name the
   sovereign and the court:
   - Circuit Court: `STATE OF MICHIGAN` / `IN THE CIRCUIT COURT
     FOR THE COUNTY OF [COUNTY]`
   - District Court: `STATE OF MICHIGAN` / `IN THE [NN]TH DISTRICT
     COURT` (district courts are numbered)
   - Probate Court: `STATE OF MICHIGAN` / `IN THE PROBATE COURT
     FOR THE COUNTY OF [COUNTY]`
2. **Party block.** On the left, the parties stacked with their
   designations, separated by a centered `v.`:
   - **Plaintiff / Defendant** for civil actions;
   - **Petitioner / Respondent** in many domestic-relations and
     probate proceedings; `In re [name/estate]` for in-rem
     captions.
   The party block is closed off on the right by the
   **case-number and judge lines** and underscored by the
   traditional Michigan caption rule — a horizontal line ending in
   a forward slash (`____/`) that separates the caption from the
   body.
3. **Case-number / judge line.** `Case No. ____________-[code]`
   carrying the two-letter **case-type code** (e.g., `CZ` general
   civil, `NZ`/`CB` business, `DM` domestic, `DC` paternity/support,
   `CK` divorce with children) and the assigned judge:
   `Hon. ____________________`. On an initial filing the case
   number is blank — the clerk assigns and stamps it — and it is
   populated on every subsequent paper.
4. **Document title** (centered, ALL CAPS) immediately below the
   caption rule: e.g., `COMPLAINT`, `ANSWER AND AFFIRMATIVE
   DEFENSES`, `MOTION FOR SUMMARY DISPOSITION`.

For the venue-specific case-type codes and local caption custom,
see `mi-wayne`, `mi-oakland`, and `mi-circuit-courts`.

## Numbered paragraphs (MCR 2.113(C))

Under MCR 2.113(C), the allegations of a pleading are made in
**numbered paragraphs**, each limited as far as practicable to a
single set of circumstances; later paragraphs may **adopt by
reference** earlier ones. Number with an Arabic numeral, a period,
and a tab: `1.\tDefendant is a resident of Wayne County,
Michigan.` State claims founded on separate transactions in
separate counts where separation aids clarity.

## Attaching written instruments (MCR 2.113(C)(2))

When a claim or defense is founded on a **written instrument** (a
contract, note, lease, or assignment), MCR 2.113(C)(2) requires a
copy be **attached** to the pleading as an exhibit (or its absence
excused), and the instrument is part of the pleading for all
purposes. Reference each exhibit by letter in the body ("a true
copy of the [instrument] is attached as **Exhibit A**") and attach
the copies after the signature block and proof of service.

## Signature block (MCR 1.109(E))

Under MCR 1.109(E), every document must be **signed by at least
one attorney of record** in the attorney's own name, or, if the
party is self-represented, **by the party**. The signature
certifies the MCR 1.109(E)(5) representations — the document is
well grounded in fact, warranted by existing law or a good-faith
argument for its extension, and not interposed for an improper
purpose — and the rule carries **sanctions** for a violation.

An attorney's signature block must include the attorney's Michigan
State Bar **"P-number"** (the bar-membership number, formatted
`P#####`):

```
Respectfully submitted,


                                   ____________________________
                                   [Name] (P#####)
                                   [Firm name]
                                   [Street address]
                                   [City, MI ZIP]
                                   Phone: (###) ###-####
                                   Email: name@example.com
                                   Attorney for [Party]
```

**Self-represented filers omit the P-number** and identify as
self-represented:

```
                                   ____________________________
                                   [Name]
                                   [Street address]
                                   [City, MI ZIP]
                                   Phone: (###) ###-####
                                   Email: name@example.com
                                   In Pro Per / Self-Represented
```

See `mi-pro-se` for the full self-represented drafting framework.

## Verification (MCR 1.109(D)(3))

MCR 1.109(D)(3) governs when a document must be **verified** and
how. A verified document is confirmed either by oath/affirmation
before a notary or other authorized officer, or by an unsworn
declaration in the form the rule permits. Close a declaration with:

```
I declare under the penalties of perjury that this [document] has
been examined by me and that its contents are true to the best of
my information, knowledge, and belief.

Executed on [date].

                                   ____________________________
                                   [Declarant name]
```

For a sworn affidavit, use a jurat ("Subscribed and sworn to
before me this ___ day of ____, 20__") with the notary block.
Confirm whether the particular filing must be sworn (notarized)
versus declared, and that MCR 1.109(D)(3) authorizes the unsworn
form for that use.

## Proof of service (MCR 2.107)

Every paper required to be served on the other parties must be
accompanied by a **proof of service** under MCR 2.107. Place it at
the foot of the document:

```
                      PROOF OF SERVICE

I certify that on [date] I served a copy of the foregoing
[Document Title] on:

  [Opposing party / counsel name]
  [Address]
  by [the court's electronic-filing system / first-class mail,
      postage prepaid / personal delivery / email as permitted by
      MCR 2.107(C)].

                                   ____________________________
                                   [Signer name]
```

MCR 2.107(C) prescribes the permitted methods of serving
subsequent papers (mail, delivery, and — where authorized —
electronic service through the court's e-filing system). Initial
process (summons and complaint) is served under **MCR 2.105**, not
MCR 2.107.

## Exhibits

Attach exhibits after the signature block and proof of service:

1. An **Exhibit List** page, centered title, each entry like
   `Exhibit A:    [one-line description]`.
2. One **cover page per exhibit**: `EXHIBIT A` centered and bold,
   then the exhibit content.
3. Footer pagination continues through the exhibits — do not
   restart the page counter.

A written instrument attached under MCR 2.113(C)(2) is itself an
exhibit and part of the pleading for all purposes.

## Citation format

Michigan citation follows the **Michigan Appellate Opinion Manual
(MAOM)** for filings before Michigan courts:

- Michigan Supreme Court: `Smith v Jones, 500 Mich 1; 890 NW2d 100
  (2017)` — note MAOM omits periods in `v`, `Mich`, and `NW2d` and
  uses a semicolon between the official and regional reporters.
- Michigan Court of Appeals: `Smith v Jones, 320 Mich App 1; 900
  NW2d 200 (2017)`
- Statutes: `MCL 600.5807` (or `Mich Comp Laws § 600.5807`)
- Court rules: `MCR 2.116(C)(10)`; evidence rules: `MRE 803(6)`

See `mi-fact-check` for citation verification against the MAOM
conventions.

## Producing documents programmatically

For `.docx` generation, use the `docx` npm package. Key points:

- Set page size explicitly to US Letter (12,240 × 15,840 DXA) —
  `docx-js` defaults to A4.
- Use a legible serif at the MCR 1.109(D) minimum size.
- Build the footer with a right-aligned tab stop at 9,360 DXA and
  use `PageNumber.CURRENT` / `PageNumber.TOTAL_PAGES` for
  "Page X of Y".
- Apply the `lineNumbers` section property above (omit `start`);
  set it on every section if you use a two-section page-1 layout.

Run `scripts/format-check.py` on the generated `.docx` to validate
the MCR 1.109(D) baseline.

## Filing mechanics: MiFILE / MiCOURT (TrueFiling)

Michigan's statewide e-filing system is **MiFILE**, the e-filing
front end to the **MiCOURT / TrueFiling** platform. E-filing is
**mandatory** in many circuit and district courts and is being
rolled out statewide; MCR 1.109(D) and the e-filing subrules
govern the form and signature of electronically filed documents.
Confirm whether the venue mandates e-filing and which document
types it accepts before assembling a packet. See the venue skills
and `mi-file-packet`.

## Composition

- For Wayne County (Detroit): `mi-wayne`
- For Oakland County (Pontiac): `mi-oakland`
- For other counties: `mi-circuit-courts`
- For drafting specific document types: `mi-draft-motion`,
  `mi-draft-declaration`, `mi-draft-note`, `mi-draft-order`
- For pro se conventions: `mi-pro-se`
- For pre-filing QC: `mi-quality-check`
- For citation verification: `mi-fact-check`

## References

- `mi-law-references` — canonical MCR, MRE, MCL, and local-rules
  corpus at `../mi-law-references/references/court-rules/`
- `scripts/format-check.py` — MCR 1.109(D) format validation
