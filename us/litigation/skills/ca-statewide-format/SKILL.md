---
name: ca-statewide-format
title: California Statewide Court Document Formatting
description: 'This skill should be used when the user asks to "draft a pleading", "format a California court document", "apply California Rules of Court", "CRC 2.100", "CRC 2.111", "build a caption", "create a declaration", "format a motion", "notice of motion", "proposed order", or any similar request for statewide California document formatting. Covers California Rules of Court (CRC) 2.100-2.119 page-format requirements (paper size, margins, font, line spacing, line numbers, page numbers, footers, two-hole punch, recyclable paper), CRC 2.111 caption requirements (attorney info block, court name, party block, case number, document title), CRC 2.112 document titles, numbered lines, declaration verification under Code of Civil Procedure section 2015.5, exhibit attachment under CRC 3.1110(f), and citation format per the California Style Manual (6th edition). Also covers e-filing basics through the California Courts eCourt / Odyssey portal and the statewide TylerConnect system. Trigger phrases:
  "format a California pleading", "California caption format", "declaration for California court", "line numbers on pleading paper", "notice of motion California", "two-hole punch California", "CRC 2.100 format", "California Rules of Court formatting", "California Style Manual citation".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ca-court-docs/skills/ca-statewide-format
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# California Statewide Court Document Formatting

Use these rules whenever drafting a paper to be filed in a
California superior court. They derive from the **California Rules
of Court (CRC), rules 2.100-2.119** (Form and Format of Papers)
and statewide drafting conventions used by California superior
courts.

California has a unified trial court system — all civil matters,
regardless of amount in controversy, file in **Superior Court** of
the relevant county (Cal. Const., art. VI, § 10; Code Civ. Proc.,
§§ 85-86). Small claims (≤ $10,000 for individuals, ≤ $5,000 for
businesses) are a sub-procedure within the superior court (Code
Civ. Proc., § 116.220). Unlimited civil jurisdiction begins at
$25,000; cases at or below $35,000 may be subject to judicial
arbitration (Code Civ. Proc., § 1141.11 et seq.).

> **NOT LEGAL ADVICE.** Generated content is a drafting aid;
> verify against current California Rules of Court, applicable
> Code of Civil Procedure sections, and the local rules of the
> specific superior court before filing.

## CRC 2.100-2.119 format requirements (mandatory)

| Item | Rule | Requirement |
|------|------|-------------|
| Paper size | CRC 2.102 | US Letter, 8½ × 11 inches |
| Sides | CRC 2.102 | Single-sided only |
| Color | CRC 2.103 | White paper; black ink only |
| Recycled paper | CRC 2.103 | Must use recycled paper with a recycled-content notice, or state compliance on the first page (in practice, most courts accept plain white paper without a printed notice) |
| Ink | CRC 2.103 | Black ink; no colored text or highlighting in the body |
| Hole punch | CRC 2.119 | **Two holes at the top**, centered (standard two-hole punch, 2¾" apart) |
| Top margin, page 1 | CRC 2.106 | At least **2.5 inches** — space for the attorney/party info block |
| All other margins | CRC 2.106 | At least **1 inch** on all sides |
| Font / type | CRC 2.104–2.105 | **12-point** type; fonts "essentially equivalent to" Courier, Times New Roman, or Arial; no condensed type |
| Line spacing | CRC 2.108(a) | Body: **1.5 or double-spaced**; single-spacing allowed for block quotations, footnotes, and headings |
| Line numbers | CRC 2.108(b) | Consecutively numbered lines on the **left margin**, one number per line, printed in the same font as the body; 28 lines per page is conventional for double-spaced, 33 for 1.5-spaced |
| Page numbers | CRC 2.109 | Bottom of every page, centered or right-aligned |
| Footer | CRC 2.110 | Short title of the document + case number + page number on every page |
| Title block | CRC 2.111 | Attorney / party info in upper-left within **2.5 inches** from top; caption block starts at 2.5-inch mark |
| Two-hole punch | CRC 2.119 | At top, before filing |

When producing a `.docx` programmatically for conversion to PDF
and upload to an eCourt filing portal, set the page-1 top margin
to 2.5 inches and subsequent pages to 1 inch. Use a section break
between page 1 and page 2 to implement the different top margins.

**Do not use colored highlighting or colored text** anywhere in
the pleading body.

## Default typography

- **Font**: Times New Roman 12 pt (Courier 12 pt or Arial 12 pt
  are also accepted under CRC 2.105)
- **Line spacing**: double-spaced or 1.5-spaced for body text;
  single-spaced for block quotations, headings, signature blocks,
  and tables
- **Line numbers**: printed on the left margin, consecutively
  numbered, same font as body (typically 10-pt or 12-pt); 28 lines
  per page for double-spacing is the California standard (derived
  from the Judicial Council pleading paper standard)
- **Paragraph style**: no hanging indent required; paragraphs may
  be numbered or not, but declarations typically use numbered
  paragraphs for ease of reference
- Bold lead-ins for labeled sections: `**Background.**` at the
  start of a paragraph, then regular text

## Required footer (CRC 2.110 — mandatory on every page)

Every generated document MUST carry a running footer on every page:

- **Left or centered**: short title of the document (e.g.,
  "PLAINTIFF'S MOTION TO COMPEL") — keep to a single line
- **Right**: page number (e.g., "Page 3 of 10") using Word's
  `PAGE` and `NUMPAGES` fields — never a static number
- **Case number**: CRC 2.110 requires the case number in the
  footer; common practice is "Case No. [NNNNNN]" on the same line
  as the title (or on a second footer line)
- **Font**: 10 pt Times New Roman

Example footer: `DEFENDANT'S MOTION TO COMPEL — Case No. 24STCV12345    Page 1 of 8`

The footer runs on every page, from page 1 through the last
exhibit page. Do not suppress it on page 1.

See `references/docx-generation.md` for the exact `docx-js` recipe.

## Attorney / party info block (CRC 2.111)

California's caption format uses a **one-column layout** in which
the attorney/party info block sits in the upper left, the court
name and county are centered below, and the party block plus case
info sit underneath in a right-`)`-separated two-column structure:

```
[Attorney / Party info block — lines 1-10, upper left]

                IN THE SUPERIOR COURT OF CALIFORNIA
                     COUNTY OF LOS ANGELES

[PARTY A],                                    )
                                              )  Case No. [NNNNNN]
              Plaintiff,                      )
                                              )  NOTICE OF MOTION AND
   vs.                                        )  MOTION TO COMPEL
                                              )  FURTHER RESPONSES TO
[PARTY B],                                    )  SPECIAL
                                              )  INTERROGATORIES;
              Defendant.                      )  MEMORANDUM OF POINTS
                                              )  AND AUTHORITIES
                                              )
                                              )  Date:  [Date]
                                              )  Time:  [Time]
                                              )  Dept.: [Dept.]
                                              )  Judge: Hon. [Name]
```

**Attorney/party info block** (CRC 2.111(a)) — upper-left, within
the top 2.5 inches of page 1:

```
[ATTORNEY NAME / PARTY NAME, pro se], State Bar No. ______
[Firm name, if applicable]
[Street Address]
[City, CA ZIP]
Telephone: (___) ___-____
Fax: (___) ___-____
Email: ___________@_____________

Attorney for [Plaintiff / Defendant]: [CLIENT NAME]
```

**Court name line** (CRC 2.111(b)):

```
              IN THE SUPERIOR COURT OF CALIFORNIA
                   COUNTY OF [COUNTY NAME]
```

Both lines centered and in ALL CAPS or in title case depending on
local practice; most California courts use all-caps for the court
name line.

**Party block**: parties listed in normal case (not all-caps);
role (Plaintiff, Defendant, etc.) indented below the party name.
Each line of the party block ends with a closing parenthesis `)`
that forms the right-side rule of the caption. The case number
and document title are placed to the right of this `)`-chain.

Use **"vs."** (with period) between parties — California style.
Some California courts use "v." but "vs." is conventional and
accepted.

## CRC 2.112 — Document titles

The document title must:

- Appear at or near the top of page 1, typically just below the
  caption box
- State the **type of document** clearly (Motion, Declaration,
  Opposition, Reply, Notice of Motion, Proposed Order, etc.)
- For motions: identify the relief sought and the legal basis
  (e.g., "MOTION TO COMPEL FURTHER RESPONSES TO FORM
  INTERROGATORIES, SET ONE; MEMORANDUM OF POINTS AND AUTHORITIES")
- For hearings: include date, time, and department in the caption
  right column (see above)

## Line numbering (CRC 2.108(b))

**MANDATORY**: California pleadings must carry consecutively
numbered lines on the left margin. CRC 2.108(b) lays out the
substantive requirements:

- Each line on each page numbered consecutively
- Beginning with the number 1 on each page
- Lines spaced 1/4-inch (1.5-spaced) or 1/3-inch (double-
  spaced) apart, matching the body line spacing
- Pre-numbered pleading paper (Judicial Council 28-line paper)
  is widely used by paper filers

For programmatically generated `.docx` documents, apply line
numbering through the section's `lineNumbers` property
(`countBy: 1`, `restart: LineNumberRestartFormat.NEW_PAGE`).
The numbers render in the left margin and do not shift the
text margin. When using the two-section pattern (page 1 at
2.5-inch top margin; pages 2+ at 1-inch top margin), apply
the `lineNumbers` property to BOTH sections so numbering
continues across the section break.

Do not pass a `start` value — an explicit `start: 1` renders
off by one in LibreOffice. See `references/docx-generation.md`
for the full recipe.

## Margin rule (double vertical line)

Draw a double vertical rule — two thin parallel lines (~0.75 pt
each, with a ~7 pt gap between them) — down the left margin
between the line numbers and the body text. It is the standard
companion to the line-numbered pleading paper that CRC
2.108(b) requires, and matches the pre-printed Judicial Council pleading
paper that paper filers use. Apply it **by default** to every
line-numbered pleading; exhibits and attachments are exempt.

Implement it as two independent full-height line shapes anchored
in the page header, so they repeat on every page — **not** as an
OOXML `double` page border, whose style couples the inter-line
gap to the line weight (widening the gap thickens both lines into
heavy bars). When using the two-section pattern (page 1 at a
larger top margin; pages 2+ at 1 inch), the patch loops over both
sections so the rule repeats across the section break. See
`references/docx-generation.md` for the exact recipe.

## CRC 2.119 — Two-hole punch

Before filing any paper document, punch two holes at the top of
the document, centered, 2¾ inches apart (standard two-hole
punch). For e-filed documents, the physical punch requirement
does not apply — the PDF is filed digitally. If the court
requests a courtesy copy, the courtesy copy must be punched.

## Declaration verification (Code Civ. Proc., § 2015.5)

California declarations are signed under penalty of perjury
under Code of Civil Procedure section 2015.5, which provides
the statutory equivalent to notarization for most court
declarations. The closing clause must state:

> "I declare under penalty of perjury under the laws of the
> State of California that the foregoing is true and correct."
> "Executed on [date], at [city], California."

Note the required elements:
1. Penalty of perjury
2. "Under the laws of the State of California"
3. Date of execution
4. Place of execution (city, California)

For declarations signed outside California, add the out-of-state
location and confirm the form meets Code Civ. Proc., § 2015.5
requirements.

## Caption structure (CRC 2.111) — detailed

See `references/caption-format.md` for the full layout with
docx-js code. Key points:

- Attorney block: upper-left, within 2.5 inches, 10-12 lines
- Court name: centered, bold, all-caps or title case
- Party block: left-justified; each line ends with `)`
- Case number and document title: right of the `)` chain
- Hearing info (date, time, dept., judge): in the right column
  below the document title, for noticed motions
- **Use "vs."** between parties; some courts accept "v."

## Required body elements

Every declaration needs:

1. **Opening identification**: "I, [Name], am the [role, e.g.,
   Defendant, Declarant] in the above-captioned action. I have
   personal knowledge of the matters stated herein and, if called
   as a witness, could and would testify competently thereto."
2. **Numbered paragraphs** (optional but strongly recommended)
3. **Perjury verification** (Code Civ. Proc., § 2015.5):
   "I declare under penalty of perjury under the laws of the
   State of California that the foregoing is true and correct."
4. **Date and place of execution**: "Executed on [date], at
   [city], California."
5. **Signature block**: signer name, role, address, phone, email

Motions and memoranda do not need a perjury clause but need:
1. A signature block
2. A **Proof of Service** (CRC 3.1300(c); Code Civ. Proc.,
   § 1013a) if served with the filing — typically a POS-030
   form or a similar declaration of service

## Exhibits (CRC 3.1110(f))

California practice uses **lettered exhibits** (Exhibit A, B, C,
etc.) in most courts. Some courts and practitioners use numbered
exhibits; confirm with local rules or practice in the specific
department.

CRC 3.1110(f) governs exhibit attachment: each exhibit must have
a tab protruding from the right side of the pages for ease of
reference. For e-filed PDFs, bookmarks serve as the functional
equivalent of physical tabs.

See `references/exhibit-handling.md` for the full protocol.

## The four document templates

See the `references/templates/` directory for complete scaffolds:

- `declaration.md` — declaration with numbered paragraphs and
  exhibits, Code Civ. Proc., § 2015.5 verification
- `motion-with-memo.md` — notice of motion, memorandum of points
  and authorities, and proposed order
- `notice-of-motion.md` — standalone Notice of Motion under Code
  Civ. Proc., § 1010
- `proposed-order.md` — findings and order for judge signature

Each template includes the caption, body skeleton, signature
block, and (for declarations) exhibit list scaffolding.

## Citation format (California Style Manual, 6th ed.)

Follow the California Style Manual (Cal. Style Manual) published
by the Judicial Council. Common forms:

- California Supreme Court: `Burnham v. Superior Court (1990) 495 U.S. 604`; for California cases: `Serrano v. Priest (1971) 5 Cal.3d 584`
- California Court of Appeal: `Vons Companies, Inc. v. Seabest Foods, Inc. (1996) 14 Cal.4th 434`
- U.S. Supreme Court: `Iqbal (2009) 556 U.S. 662`
- 9th Circuit: `Ashcroft v. Iqbal (9th Cir. 2007) 490 F.3d 157`
- California Rules of Court: `Cal. Rules of Court, rule 2.100` (not "CRC 2.100" in formal filings)
- Code of Civil Procedure: `Code Civ. Proc., § 1010` (abbreviate; use "§" with a space)
- Civil Code: `Civ. Code, § 1542`
- Evidence Code: `Evid. Code, § 1200`
- California Constitution: `Cal. Const., art. VI, § 10`
- Federal statutes: `15 U.S.C. § 1692k(a)(1)` (use periods in "U.S.C.")
- Federal regulations: `12 C.F.R. § 1006.30`

**Distinctive California style choices**:

- Year in parentheses immediately after the case name: `Smith v.
  Jones (2021) 55 Cal.App.5th 100`
- Reporter abbreviations: Cal., Cal.2d, Cal.3d, Cal.4th, Cal.5th
  (California Supreme Court); Cal.App., Cal.App.2d, Cal.App.3d,
  Cal.App.4th, Cal.App.5th (Court of Appeal)
- Do NOT include parallel cites (unlike Bluebook) unless citing
  a very old case where the official reporter is the primary cite
- Italicize case names; do not italicize "Id." or "Ibid."
- "Id." for the immediately preceding cite (no signal needed);
  "Ibid." is rarely used in California practice
- Abbreviate "§" (not "sec.") with a space before the number;
  use "§§" for multiple sections
- "Ante" and "post" used for internal cross-references in
  appellate briefs (not common in trial court practice)

## Producing documents programmatically

For `.docx` generation, follow `references/docx-generation.md`.
Key California-specific points:

- Page-1 top margin: 2.5 inches (CRC 2.110 attorney/party info
  block)
- Subsequent pages: 1 inch top margin — requires a Word section
  break between page 1 and page 2
- Line numbering: required under CRC 2.108(b); apply via the
  section's `lineNumbers` property (`countBy: 1`, `restart: LineNumberRestartFormat.NEW_PAGE`) on BOTH sections of the
  two-section pattern. Do not pass `start: 1` explicitly — it
  renders off by one in LibreOffice.
- Footer: CRC 2.110 footer on every page including page 1

For format validation, use the bundled
`plugins/ca-court-docs/scripts/format-check.py` on a generated
`.docx`.

## eFiling — California eCourt and TylerConnect

Most California superior courts now accept (or require) electronic
filing. Two main platforms:

- **Odyssey eFileCA** (Tyler Technologies): Used by Los Angeles
  Superior Court, Sacramento Superior Court, and many others.
  Portal: https://www.efileca.com (redirects to the Tyler portal)
- **File & ServeXpress**: Used by San Francisco Superior Court,
  San Mateo, Alameda, and others.
  Portal: https://www.fileandservexpress.com/
- **OC eFiling / Odyssey** (Orange County): separate portal at
  https://oc.courtreserve.com or via efileca.com

Key statewide requirements:
- Accepted format: PDF only for filed documents (the `.docx` is
  the working copy)
- File size limits vary by court (typically 10-25 MB per document)
- Document codes are selected from a dropdown in the portal —
  match the CRC 2.112 document title type
- For self-represented litigants: check whether the court
  requires mandatory eFiling for represented parties and whether
  pro se filers may still paper-file (rules vary by county)

## Compose with court-specific skills

This skill is **always** layered with:

- `ca-lasc` — if the case is in Los Angeles Superior Court
- `ca-sfsc` — if the case is in San Francisco Superior Court
- `ca-county-courts` — for any other county
- `ca-pro-se` — if the litigant is self-represented

The court-specific skill adds local rule variations, motion
reservation protocols, tentative-ruling practice, and venue-
specific filing quirks.

## References

- `references/crc-2-100-full-text.md` — concise summary of CRC
  2.100-2.119 for quick citation
- `references/caption-format.md` — caption structure with full
  docx-js example
- `references/exhibit-handling.md` — exhibit tabs, CRC 3.1110(f),
  and pagination
- `references/docx-generation.md` — `docx` npm library patterns
  for California pleadings with line numbering
- `references/templates/` — the four document templates

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against current rules and case law before filing.
