---
name: tx-statewide-format-codearranger
title: Texas Statewide Court Document Formatting
description: 'Use when the user asks to "format a Texas pleading", "draft a Texas court document", "build a Texas caption", "format a Texas petition", or "format a Texas motion" for any Texas District Court, County Court at Law, or Justice Court. Triggers: "Texas caption", "TRCP 45 form of pleadings", "TRCP 47 statement of relief", "Rule 47(c) damages range Texas", "TRCP 57 signature block", "State Bar of Texas bar number", "TRCP 78a civil case information sheet", "TRCP 21a certificate of service", "eFileTexas.gov", "Odyssey File & Serve Texas", "Cause No.", "line numbering", "Page X of Y footer", "Texas Rules of Form Greenbook", "pet. denied citation". Covers the TRCP 45/47 form of pleadings, the Rule 47(c) statement-of-relief range, the caption, the TRCP 57 signature block with the State Bar of Texas number, the TRCP 21/21a filing and certificate of service, eFileTexas.gov e-filing under TRCP 21(f) and Tex. R. Jud. Admin. 10, line-numbered pleading paper, footer conventions, and Greenbook
  citation format.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-statewide-format
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Texas Statewide Court Document Formatting

> **NOT LEGAL ADVICE.** This skill assists with drafting and
> formatting only. Verify against the current Texas Rules of Civil
> Procedure, the Texas Rules of Judicial Administration, the Supreme
> Court of Texas e-filing rules, and the local rules and standing
> orders of the filing court before submitting any document.

Use these conventions whenever drafting a paper to be filed in a
Texas trial court — a **District Court**, a **County Court at Law**
or **Constitutional County Court**, or a **Justice Court**. Texas has
**no single strict statewide pleading-paper rule** fixing margins,
font, and line spacing the way some jurisdictions do. Instead, the
form of a Texas court document flows from a handful of **Texas Rules
of Civil Procedure (TRCP)**: **TRCP 45** (form of pleadings), **TRCP
47** (claims for relief, including the **Rule 47(c)**
statement-of-relief range), **TRCP 57** (signing and the State Bar of
Texas bar number), **TRCP 78a** (civil case information sheet), and
**TRCP 21 / 21a** (filing and service). Electronic filing runs under
**TRCP 21(f)** and the **Texas Rules of Judicial Administration (Tex.
R. Jud. Admin.) 10** technology standards.

## Governing rules

- **TRCP 45** — Form of Pleadings: pleadings must consist of a
  **plain and concise statement** of the cause of action or defense.
  No technical forms are required; allegations are simple, concise,
  and direct.
- **TRCP 47** — Claims for Relief: an original pleading stating a
  claim must contain a short statement of the cause of action, the
  **Rule 47(c)** statement of the **range of monetary relief** sought
  (see below), a demand for judgment, and (where applicable) a
  request for disclosure.
- **TRCP 57** — Signing of Pleadings: every pleading is signed by at
  least one attorney of record in the attorney's individual name,
  with the attorney's **State Bar of Texas number**, address,
  telephone number, email, and fax (if any); a self-represented party
  signs in person.
- **TRCP 78a** — Civil Case Information Sheet: a **civil case
  information sheet** in the form promulgated by the Supreme Court of
  Texas must accompany the **initial filing** of an original petition
  or application.
- **TRCP 21 / 21a** — Filing and Service: motions and applications
  are filed and served; e-service is required for those who
  electronically file; **TRCP 21a** sets the service methods and the
  add-on time (e.g., extra days when service is by mail, commercial
  delivery, fax, or email) — the exact triggers are drift-prone, so
  confirm them against the corpus.
- **TRCP 4** — Computation of Time: exclude the first day, include
  the last; if the last day is a Saturday, Sunday, or **legal
  holiday**, the period runs to the next day that is not. See
  `tx-deadlines`.

Pull the verbatim rule text from the `tx-law-references` corpus at
`../tx-law-references/references/court-rules/` before relying on any
specific service add-on day, deadline, or form figure — those values
live in the rule text and never drift here.

## The Rule 47(c) statement of relief — a Texas requirement

**TRCP 47(c)** requires an original pleading stating a claim for
monetary relief to affirmatively plead that the party seeks one of
the **statutory ranges of relief** — for example, a band such as
"only monetary relief of $250,000 or less," graduating up through
the higher bands to "monetary relief over $1,000,000." The exact
band language and dollar thresholds are set by the rule and are
drift-prone — confirm the **current Rule 47(c) bands** against
`../tx-law-references/references/court-rules/`.

This matters procedurally: a pleading that **omits** the Rule 47(c)
statement is subject to special exceptions and the party may **not be
permitted to conduct discovery** until the pleading is amended to add
it, and an omission can complicate a **default judgment**. Always
include the Rule 47(c) statement in an original petition that seeks
money. The chosen band also drives the **TRCP 190 discovery level**
and whether the case is an **expedited action under TRCP 169** (see
`tx-discovery`).

## Paper and legibility

Texas does not impose a single statewide font/margin/spacing rule for
pleadings. Customary, court-accepted practice for a clean,
e-filing-ready document:

| Item | Practice (confirm local rules) |
|------|--------------------------------|
| Paper / ink | US Letter, 8½ × 11 in., black text on white |
| Font | A legible serif at **12 point** or larger |
| Line spacing | **Double** or **1½** spacing in the body |
| Margins | **≥ 1"** all around |
| Caption | Court identifier above/beside the party block |
| Document title | Centered heading; also carried in the footer |
| Page numbers | Each page numbered; `Page X of Y` in the footer |

Local rules of a specific court (and a judge's standing orders) may
add page limits on motions and briefs, chambers-copy requirements,
and exhibit-tabbing conventions. `scripts/format-check.py` validates a
generated `.docx` against this baseline and flags departures.

## Line numbering (pleading paper) — applied BY DEFAULT

Apply continuous line numbering down the left margin of every
generated Texas pleading. Line numbers count every body line and
**restart on each page**.

The TRCP do not themselves require line numbering, and a Texas
document filed without line numbers is rule-compliant. But
line-numbered pleading paper is the universal convention across this
marketplace: it lets the court and opposing counsel cite an exact
location ("page 4, lines 12–15") and never harms a Texas filing.
Apply it **by default** to every petition, motion, response,
affidavit, unsworn declaration, notice, and proposed order. Exhibits
and attachments are exempt.

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
the section's `<w:sectPr>`. The numbers render in the left margin and
do not shift the text margin.

**Do NOT set `start` explicitly.** An explicit `start: 1` renders off
by one in LibreOffice (the first body line shows "2"). Omit `start` —
it defaults to 1 in OOXML.

If you use a two-section page-1 layout (a deeper top margin to seat
the caption, then a normal continuation section), **set `lineNumbers`
on BOTH sections**, or numbering stops at the section break.

## Required footer (mandatory on every generated document)

Every generated document MUST carry a running footer on every page:

- **Left**: the document title (and, conventionally, the cause
  number) — e.g., `ORIGINAL PETITION — Cause No. ____________`. Keep
  it to a single line so it never wraps; this places the title at the
  bottom of each page.
- **Right**: `Page X of Y`, where `X` is the current page number and
  `Y` is the total page count. Use Word's `PAGE` and `NUMPAGES`
  fields — never a static number.
- **Font**: matches the body font family, may be slightly smaller.
- **Alignment**: a right-aligned tab stop places the page counter
  flush right while the title stays flush left.

The footer runs continuously from page 1 through the last exhibit
page — do not restart or suppress pagination anywhere.

## Caption structure

A Texas caption carries (1) the **cause number**, (2) the **title of
the court**, including the county, (3) the **party block** with the
party designations, and (4) the **title of the document**. The court
identifier is centered/right and in ALL CAPS:

```
                          CAUSE NO. ____________

JANE DOE,                          §   IN THE [NTH] JUDICIAL
                                   §   DISTRICT COURT
       Plaintiff,                  §
                                   §
v.                                 §   OF
                                   §
ACME COLLECTIONS, LLC,             §
                                   §   [COUNTY] COUNTY, TEXAS
       Defendant.                  §
```

Texas captions conventionally use the **section sign (§)** as the
vertical divider between the party column (left) and the court
identifier (right). The court identifier takes one of these forms:

- **District Court**: `IN THE [NTH] JUDICIAL DISTRICT COURT OF
  [COUNTY] COUNTY, TEXAS`.
- **County Court at Law**: `IN THE COUNTY COURT AT LAW NO. [N] OF
  [COUNTY] COUNTY, TEXAS`.
- **Constitutional County Court**: `IN THE COUNTY COURT OF [COUNTY]
  COUNTY, TEXAS`.
- **Justice Court**: `IN THE JUSTICE COURT, PRECINCT [N], PLACE [N],
  [COUNTY] COUNTY, TEXAS` (see `tx-justice-courts`).

### The caption elements in order

1. **Cause number.** `CAUSE NO. ____________` — blank on an initial
   filing (the clerk assigns it on intake) and populated on every
   subsequent paper. For county-specific case-number conventions see
   the venue skills (`tx-hcdc`, `tx-dcdc`, `tx-county-courts`).
2. **Party block** (left column). The parties stacked with their
   designations, separated by a `v.`:
   - **Plaintiff / Defendant** in general civil actions;
   - **Petitioner / Respondent** in family-law and many special
     proceedings (`tx-family-court`).
3. **Court identifier block** (right column, ALL CAPS) — one of the
   forms above, naming the court and the county.
4. **Document title.** A centered ALL-CAPS heading below the caption
   (e.g., `PLAINTIFF'S ORIGINAL PETITION`), and restated in the
   footer so it sits at the bottom of every page.

## Numbered paragraphs and the body

Under **TRCP 45**, the body is a plain, concise statement; allegations
are conventionally made in **numbered paragraphs**, each limited so
far as practicable to a single set of circumstances. Number with an
Arabic numeral, a period, and a tab. A written instrument attached as
an **exhibit is part of the pleading**. State separate causes of
action in separate, captioned sections where separation aids clarity.

## Initiating pleading and responsive pleading — terminology

- The **initiating pleading** is the **Original Petition** (e.g.,
  `Plaintiff's Original Petition`), not a "complaint."
- The **responsive pleading** is the **Original Answer**, which in
  Texas commonly takes the form of a **general denial under TRCP 92**.
  Certain matters must be raised by **verified plea under TRCP 93**
  (e.g., denial of a sworn account under TRCP 185 / 93(10), lack of
  capacity, defect of parties). See `tx-first-30-days`.
- Defects or vagueness in a pleading are challenged by **special
  exceptions (TRCP 91)** — there is **no general demurrer** in Texas —
  and a claim with **no basis in law or fact** may be challenged by a
  **TRCP 91a motion to dismiss**.

## Sworn statements: affidavit or unsworn declaration

Texas accepts either a sworn **affidavit** (notarized) or an
**unsworn declaration** under **Tex. Civ. Prac. & Rem. Code
§ 132.001**, which may substitute for an affidavit on most matters
when it is in writing, subscribed by the declarant as true under
penalty of perjury, and in substantially the statutory form. Use the
unsworn declaration where a notary is impractical; confirm the
statutory jurat language against
`../tx-law-references/references/tx-statutes-debt/`. See
`tx-draft-declaration`.

## Signature block (TRCP 57)

Under TRCP 57, every pleading is **signed**. An attorney signs in the
attorney's individual name and must include the **State Bar of Texas
number**:

```
                                   /s/ [Name]
                                   [Name]
                                   State Bar No. ________
                                   [Firm name]
                                   [Street address]
                                   [City, TX  ZIP]
                                   Tel: (###) ###-####
                                   Fax: (###) ###-####
                                   Email: name@example.com
                                   ATTORNEY FOR [PARTY]
```

**Self-represented filers omit the State Bar number** and identify as
pro se:

```
                                   /s/ [Name]
                                   [Name]
                                   [Street address]
                                   [City, TX  ZIP]
                                   Tel: (###) ###-####
                                   Email: name@example.com
                                   [PARTY], Pro Se / Self-Represented
```

See `tx-pro-se` for the full self-represented drafting framework.

## Certificate of service (TRCP 21a)

Every paper required to be served on the other parties carries a
**certificate of service** under TRCP 21a. Place it at the foot of
the document:

```
                   CERTIFICATE OF SERVICE

I certify that on [date] a true and correct copy of the foregoing
[Document Title] was served on all counsel/parties of record in
accordance with TRCP 21a:

  [Opposing party / counsel name]
  [Address / email]
  by [the eFileTexas.gov electronic-service system /
      certified mail, return receipt requested /
      first-class U.S. mail / email / fax as permitted by TRCP 21a].

                                   /s/ [Signer name]
                                   [Signer name]
```

TRCP 21a prescribes the permitted methods of service and the add-on
time for non-electronic service. Initial process (citation and the
petition) is served under **TRCP 99 / 106** — not Rule 21a. The
defendant's answer deadline on citation follows the Texas **"Monday
rule" (TRCP 99)**: the answer is due by **10:00 a.m. on the Monday
next after the expiration of twenty days after the date of service**
(this is NOT a flat 20-day count). In Justice Court the answer
deadline is different (TRCP 502.5) — see `tx-justice-courts`.

## Filing mechanics: eFileTexas.gov (TRCP 21(f); Tex. R. Jud. Admin. 10)

Texas's statewide electronic-filing portal is **eFileTexas.gov** (the
Tyler Technologies **Odyssey File & Serve** platform), governed by
**TRCP 21(f)** and the **Tex. R. Jud. Admin. 10** technology
standards adopted by the Supreme Court of Texas.

- **E-filing is mandatory for attorneys** in civil matters in the
  appellate courts, District Courts, statutory County Courts,
  Constitutional County Courts, and statutory probate courts.
- **Self-represented filers may e-file** through eFileTexas.gov and
  are encouraged to; some courts also accept paper filing from a
  self-represented party — confirm the venue's posture.
- **Justice Courts also file through eFileTexas.**
- The **civil case information sheet (TRCP 78a)** accompanies the
  initial filing.
- The assisted self-help front end is **TexasLawHelp.org**, which
  hosts guided forms and the courts' guided-filing tools.

Confirm whether the venue mandates e-filing for your filer type and
which document types it accepts before assembling a packet. See the
venue skills and `tx-file-packet`.

## Citation format (Texas Rules of Form — "Greenbook")

Texas legal citation follows the **Texas Rules of Form** (the
"Greenbook"), published by the Texas Law Review Association. Texas
abolished its official Texas Reports; cite the **South Western
Reporter**:

- **Supreme Court of Texas**: `In re Columbia Med. Ctr. of Las
  Colinas, 290 S.W.3d 204 (Tex. 2009)`.
- **Court of Appeals**: include the **court of appeals district** and
  the **petition-history parenthetical**: `Doe v. Roe, 123 S.W.3d
  456 (Tex. App.—Dallas 2003, pet. denied)`. The **"pet. denied" /
  "pet. ref'd" / "no pet."** writ-or-petition disposition
  parenthetical is a Texas signature — never omit it for an
  intermediate-court case.
- **Statutes**: `Tex. Civ. Prac. & Rem. Code § 16.004`; `Tex. Fin.
  Code § 392.101`; `Tex. Bus. & Com. Code § 17.50`; `Tex. Fam. Code
  § 153.131`.
- **Rules**: `Tex. R. Civ. P. 166a`; `Tex. R. Evid. 803(6)`.

See `tx-fact-check` for citation verification against the corpus.

## Producing documents programmatically

For `.docx` generation, use the `docx` npm package. Key points:

- Set page size explicitly to US Letter (12,240 × 15,840 DXA) — the
  library defaults to A4.
- Use a legible serif at **12 point** or larger with double or 1½
  line spacing.
- Build the caption with the **§** divider between the party column
  and the court-identifier column; choose the court identifier form
  for the venue (District / County Court at Law / Constitutional
  County Court / Justice Court).
- Build the footer with a right-aligned tab stop and use
  `PageNumber.CURRENT` / `PageNumber.TOTAL_PAGES` for "Page X of Y";
  carry the document title at the left so it sits at the bottom of
  each page.
- Apply the `lineNumbers` section property above (omit `start`); set
  it on every section if you use a two-section page-1 layout.
- Include the **Rule 47(c)** statement-of-relief paragraph in any
  original petition seeking money.

Run `scripts/format-check.py` on the generated `.docx` to validate
the baseline.

## Composition

- For Harris County (Houston) District Courts: `tx-hcdc`
- For Dallas County District Courts: `tx-dcdc`
- For other counties' District Courts and County Courts at Law:
  `tx-county-courts`
- For Justice of the Peace / small-claims / eviction matters:
  `tx-justice-courts` (and `tx-smith-county-jp` for Smith County)
- For family-law venue and intake: `tx-family-court`
- For drafting specific document types: `tx-draft-motion`,
  `tx-draft-declaration`, `tx-draft-note`, `tx-draft-order`
- For pro se conventions: `tx-pro-se`
- For the first responsive pleading and the Monday rule:
  `tx-first-30-days`
- For pre-filing QC: `tx-quality-check`
- For citation verification: `tx-fact-check`
- For deadline computation (TRCP 4): `tx-deadlines`

## References

- `tx-law-references` — canonical TRCP, Tex. R. Evid., Tex. R. Jud.
  Admin., the Texas statutes corpus, and local-rules pointers at
  `../tx-law-references/references/court-rules/`
- `scripts/format-check.py` — Texas format-baseline validation
