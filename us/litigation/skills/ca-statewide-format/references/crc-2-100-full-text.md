# CRC 2.100-2.119 — Concise Summary

California Rules of Court, rules 2.100-2.119 govern the form and
format of papers filed in California trial courts. This is a
concise reference for quick citation; verify against the current
official text at **https://www.courts.ca.gov/rules.htm**.

## Rule 2.100 — Scope

Rules 2.100-2.119 apply to papers filed in trial courts. They do
not apply to the Judicial Council forms (which have their own
format), nor to exhibits unless a rule specifically says so.

## Rule 2.101 — Definitions

- **Paper**: any document filed with the court
- **Computer-generated document**: a document produced by a word
  processor or other software (as opposed to handwritten or
  typewritten)

## Rule 2.102 — Paper size

All papers must be on **8½-inch by 11-inch** (US Letter) white
paper. Legal-size (8½ × 14) paper is not permitted.

## Rule 2.103 — Paper quality

- Paper must be **white** and **opaque**
- Paper must be **recycled** or state on the first page that
  it was printed on recycled paper. In practice, most California
  courts do not reject papers that omit the recycled-paper notice
  unless the paper is clearly non-recycled stock, but strict
  compliance requires the recycled designation
- **Black ink only** — no colored or highlighted text in the body
  of the paper

## Rule 2.104 — Type size

Type must be **12 points** minimum. No condensed type (type that
is narrower than standard 12-point characters).

## Rule 2.105 — Font

The font must be one "essentially equivalent to" one of:
- Courier (a monospaced font)
- Times New Roman (a proportional serif font)
- Arial (a proportional sans-serif font)

Other common accepted fonts: Garamond, Book Antiqua, Century
(all serif, proportional, readable). Decorative or script fonts
are not compliant.

## Rule 2.106 — Margins

| Page | Margin |
|------|--------|
| **Top margin, page 1** | **At least 2.5 inches** (to accommodate the attorney/party information block) |
| Top margin, subsequent pages | **At least 1 inch** |
| Bottom margin | **At least 1 inch** |
| Left margin | **At least 1 inch** |
| Right margin | **At least 1 inch** |

The 2.5-inch top margin on page 1 is the most commonly missed
California formatting requirement. Oregon uses 3 inches; federal
courts use 1 inch — California's 2.5-inch rule is distinctive.

## Rule 2.107 — One side only

Text must appear on **one side only** of each sheet of paper.
Double-sided printing is not permitted for court filings (though
it is common in exhibits attached to motions — verify local
practice).

## Rule 2.108 — Line spacing and line numbering

**(a) Line spacing**:

- Body text: **1.5 or double-spaced**
- Exceptions (may be single-spaced):
  - Headings
  - Footnotes
  - Block quotations (indented quotations of 50+ words)
  - Signature blocks
  - Tables

**(b) Line numbers**:

- Lines must be **consecutively numbered** on the left margin
- One line number per line of text
- Line numbers must be in the **same font** as the body text
  (or smaller — 10 pt is common for the numbers)
- **28 lines per page** is the California Judicial Council
  standard for double-spaced, 12-pt text on US Letter with
  standard margins. For 1.5-spaced text, approximately
  33 lines per page
- The line-number column is typically 0.5 inches wide; body
  text starts at the 1-inch left margin, to the right of the
  line-number column

**Implementation options**:

1. **Judicial Council pleading paper**: Use pre-numbered
   Judicial Council form paper (available at office supply
   stores or as a Word template from courts.ca.gov)
2. **Word line numbering**: Insert → Line Numbers → Continuous
   (set restart: None; count by: 1)
3. **Programmatic (docx-js)**: Two-column borderless table —
   narrow left column with numbers 1-28; wide right column
   with body text (see `references/docx-generation.md`)

## Rule 2.109 — Page numbers

- **Every page** must be numbered
- Page numbers appear at the **bottom** of the page (center or
  right-aligned are both acceptable)
- Use Arabic numerals (1, 2, 3 — not i, ii, iii)
- The first page may be numbered or may use the caption as the
  page identifier; subsequent pages must be numbered

## Rule 2.110 — Footer

Every page must have a **footer** identifying the document. The
footer must include:

1. **Short title** of the document (not the full title — an
   abbreviated version is acceptable)
2. **Case number**
3. **Page number** (may appear here instead of or in addition to
   the bottom-center number under rule 2.109)

Common California footer format:
`PLAINTIFF'S MOTION TO COMPEL — Case No. 24STCV12345 — Page 3 of 10`

Or with the page number on the right:
`Left: PLAINTIFF'S MOTION TO COMPEL — Case No. 24STCV12345   Right: Page 3 of 10`

The footer appears on **every page** including the first.

## Rule 2.111 — Format of first page

**(a) Attorney/party information block** (upper-left, within
the top 2.5 inches of page 1):

```
[Name], [State Bar No. NNNNNN / "self-represented"]
[Firm name]
[Street address]
[City, CA ZIP]
Tel: (NNN) NNN-NNNN
Fax: (NNN) NNN-NNNN
Email: xxx@xxx.com

Attorney for [Plaintiff / Defendant]: [CLIENT NAME]
[OR: "Defendant, self-represented"]
```

**(b) Court name**: centered below the attorney info block,
typically formatted as:

```
         IN THE SUPERIOR COURT OF CALIFORNIA
              COUNTY OF [COUNTY NAME]
```

**(c) Caption** — party block and case information:

The party names appear on the left; the case number and document
title appear on the right, separated by a series of closing
parentheses `)` that form the right-side rule:

```
[PARTY A],                               )
                                         )  Case No. [NNNNNN]
     Plaintiff,                          )
                                         )  [DOCUMENT TITLE]
   vs.                                   )
                                         )  Date:  [Date]
[PARTY B],                               )  Time:  [Time]
                                         )  Dept.: [Dept.]
     Defendant.                          )  Judge: [Name]
```

## Rule 2.112 — Document title

Every paper must state its **title** at the beginning of the
document (or in the caption). The title must:

- Identify the **type of document** (motion, opposition,
  declaration, order, etc.)
- Be sufficient for the clerk to index the document correctly

Common title forms:
- `NOTICE OF MOTION AND MOTION TO COMPEL FURTHER RESPONSES TO SPECIAL INTERROGATORIES; MEMORANDUM OF POINTS AND AUTHORITIES`
- `DECLARATION OF [NAME] IN SUPPORT OF DEFENDANT'S MOTION TO COMPEL`
- `[PROPOSED] ORDER GRANTING DEFENDANT'S MOTION TO COMPEL`
- `OPPOSITION TO PLAINTIFF'S MOTION FOR SUMMARY JUDGMENT`

## Rule 2.113 — Cover sheet

A **cover sheet** (Judicial Council form CM-110 for case
management, or a general cover sheet) is required when a
document is filed without a case management conference or when
otherwise specified by local rules. Most stand-alone motions
and declarations do not require a separate cover sheet — the
caption on page 1 serves as the cover.

## Rule 2.114 — Proposed orders

A proposed order must contain:

- The court name and case caption (same as the motion it
  accompanies)
- A recital of the basis for the order (e.g., "The Court,
  having considered Defendant's Motion to Compel...")
- The operative order (e.g., "IT IS ORDERED that...")
- A signature line for the judge: `____________________ [Judge's name], Judge of the Superior Court`
- A date line: `Dated: _______________`

See `references/templates/proposed-order.md` for a full scaffold.

## Rule 2.115 — Copies

Courts typically require:

- **Original** for the court file
- One or more **copies** as required by local rules (many
  courts do not require courtesy copies for e-filed documents;
  check local rules and any department standing orders)

## Rule 2.116 — Binding

Papers must be **unbound** (no staples, binders, or clips on the
filed copy — the clerk will fasten the documents). The two-hole
punch (rule 2.119) allows the clerk to bind papers in the court
folder.

## Rule 2.117 — [Reserved]

Rule 2.117 is reserved in the current California Rules of Court.

## Rule 2.118 — Handwritten or typewritten papers

Handwritten or typewritten papers (non-computer-generated) may
be filed only if legible. Line spacing and font requirements
apply. Line numbers are still required.

## Rule 2.119 — Two-hole punch

**Before filing**, punch **two holes** at the top center of the
document:

- Standard two-hole punch (2¾ inches apart, centered)
- For e-filed PDFs: the physical punch requirement does not
  apply to the electronic copy; the PDF is filed digitally
- For **courtesy copies** delivered to chambers: punch the
  copy as required

## Citation format for these rules

In a California court filing, cite these rules as:

`Cal. Rules of Court, rule 2.100`
`Cal. Rules of Court, rule 2.108(b)` (for the line-numbering subrule)

Not "CRC 2.100" (acceptable informally but not in formal filings).
Not "California Rule of Court 2.100" (the plural "Rules" is the
official title).

## Quick compliance checklist

- [ ] 8.5 × 11 inch white paper
- [ ] One side only
- [ ] Black ink only
- [ ] 12-point font (Courier, Times New Roman, Arial, or equivalent)
- [ ] Top margin page 1: at least 2.5 inches
- [ ] All other margins: at least 1 inch
- [ ] Body text: 1.5 or double-spaced
- [ ] Line numbers on left margin, consecutive
- [ ] Page numbers on bottom of every page
- [ ] Footer: short title + case number + page number, every page
- [ ] Attorney/party info block upper-left on page 1
- [ ] Court name centered
- [ ] Caption: party block left, case number and title right
- [ ] Document title at top
- [ ] Two-hole punch at top (for paper copies)

**Source**: California Rules of Court, rules 2.100-2.119 (effective
Jan. 1, 2007; last amended Jan. 1, 2020). Verify current text at:
**https://www.courts.ca.gov/cms/rules/index.cfm?title=two**
