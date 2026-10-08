---
name: tx-hcdc-codearranger
title: Harris County District Courts (Houston)
description: Use when drafting or filing civil documents in the Harris County District Courts — the Houston-area trial courts and Texas's largest trial-court system. Triggers include "Harris County District Court", "file in Harris County", "sued in Harris County", "Houston district court", "Harris County District Clerk", "Harris County civil district court", "Harris County family district court", "Harris County eFileTexas", "Harris County cause number", "Houston civil filing", "234th District Court Harris County", "Harris County central docket", "Harris County local rules". Covers the civil and family district courts, the central-docket / random assignment, the Harris County District Clerk and eFileTexas e-filing, the local rules pointer, the ancillary docket, and cause-number conventions. Layer on top of `tx-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-hcdc
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Harris County District Courts (Houston)

> **NOT LEGAL ADVICE.** These notes describe the venue's procedural
> mechanics as a drafting aid, not legal advice. Local rules,
> standing orders, and judge-specific practices change; verify with
> the Harris County District Clerk and the current Harris County
> local rules before relying on anything here.

Use this skill in addition to `tx-statewide-format` when the matter
is a **civil** case in the **Harris County District Courts**, which
sit in **Houston** and form the largest trial-court system in Texas
by caseload.

## The court

Texas's general-jurisdiction trial court is the **District Court**.
Harris County has a large bench of **numbered District Courts** —
each a separate court with its own number and elected judge (for
example, the "234th Judicial District Court of Harris County,
Texas"). The Harris County District Courts are organized into
divisions:

- **Civil District Courts** — general civil litigation, with no upper
  jurisdictional dollar limit; contract, tort, debt, real-property,
  and injunctive matters.
- **Family District Courts** — divorce, SAPCR (suits affecting the
  parent-child relationship), and related domestic-relations matters.
  Route family matters through `tx-family-court`.
- (Criminal District Courts handle felonies and are outside this
  civil-drafting skill.)

A civil action is captioned in the **[Nth] Judicial District Court of
Harris County, Texas** — see `tx-statewide-format` for the full
caption with the **§** divider.

## Central docket / random assignment

Harris County uses a **central-docket** model: a new civil case is
filed with the District Clerk and **randomly assigned** by the clerk
to one of the civil District Courts, which then manages the case
through disposition. There is also an **ancillary docket** that hears
time-sensitive matters (temporary restraining orders, temporary
injunctions, and other emergency relief) when the assigned court is
unavailable. Do not assume which court will hear an emergency
application — confirm the current ancillary-docket / emergency-relief
procedure with the clerk and the local rules before noticing
emergency relief.

## Local rules

Practice in these courts is governed by the **statewide Texas Rules of
Civil Procedure (TRCP)** and **Texas Rules of Evidence (Tex. R.
Evid.)**, as supplemented by the **Harris County (Civil Trial
Division) local rules** and each judge's standing orders / court
procedures. The local rules and standing orders address civil case
management, docket control / scheduling orders, motion-setting and
oral-hearing practice (including any submission-docket vs. oral-
hearing distinction), and chambers-copy requirements.

Do not hard-code rule numbers, page limits, or motion-setting
mechanics from memory — read the current Harris County local rules
and the assigned court's standing orders in `tx-law-references` (or
confirm with the clerk and the court's website) before relying on
them.

## E-filing — the Harris County District Clerk and eFileTexas

The **Harris County District Clerk** maintains the district-court
record and intakes filings. Electronic filing runs through the
statewide **eFileTexas.gov** portal (Tyler Technologies **Odyssey
File & Serve**), under **TRCP 21(f)** and **Tex. R. Jud. Admin. 10**:

- **E-filing is mandatory for attorneys** in civil matters in the
  District Courts.
- **Self-represented filers may e-file** through eFileTexas.gov and
  are encouraged to; confirm whether the clerk also accepts paper
  filing from a self-represented party.
- The **civil case information sheet (TRCP 78a)** accompanies the
  initial filing of an original petition.

Confirm the current document-type selections, the filing-fee /
fee-waiver workflow (a **Statement of Inability to Afford Payment of
Court Costs** may apply), and any local cover-sheet requirement
before assembling a packet. See `tx-file-packet`.

## Case management and scheduling

After the case is filed and answered, the assigned court manages it
through a **docket control order / scheduling order** setting
discovery deadlines tied to the **TRCP 190 discovery level**,
dispositive-motion dates (note the **TRCP 166a** summary-judgment
timing — motion served at least **21 days** before the hearing,
response due **7 days** before, and Texas's distinct **no-evidence**
motion under 166a(i)), and the trial setting. **Calendar your
obligations from the docket control order entered in your specific
case**, and confirm the assigned judge's individual procedures and
any chambers-copy requirement. See `tx-schedule-hearing`,
`tx-hearings`, `tx-discovery`, and `tx-deadlines`.

## Cause-number conventions

A Harris County civil cause number follows the county's pattern
(commonly a year prefix plus a sequential number, with a court /
case-type designation assigned at intake). **Confirm the exact
cause-number format and the assigned court** the District Clerk
gives your case; once assigned, the cause number and the assigned
court anchor the caption per `tx-statewide-format`. Do not guess the
format — verify it against the clerk's intake.

**Agent behavior:** before drafting a Notice of Hearing, setting a
page-limited motion, or calendaring a deadline, read the current
Harris County local rules and the assigned court's standing orders in
`tx-law-references`, the docket control order entered in the case, and
the assigned judge's procedures. Confirm the civil-vs-family division,
the eFileTexas document-type selection, and any chambers-copy
requirement with the clerk.

## Composition

- For statewide format and the Texas caption: `tx-statewide-format`
- For the Original Answer and the TRCP 99 "Monday rule" answer
  deadline: `tx-first-30-days`
- For drafting motions / notices / orders / declarations:
  `tx-draft-motion`, `tx-draft-note`, `tx-draft-order`,
  `tx-draft-declaration`
- For computing deadlines (TRCP 4): `tx-deadlines`
- For scheduling a hearing and oral argument: `tx-schedule-hearing`,
  `tx-hearings`
- For discovery (TRCP 190 levels / 169 expedited): `tx-discovery`
- For assembling and e-filing a packet: `tx-file-packet`
- For other venues: `tx-dcdc` (Dallas County), `tx-county-courts`
  (other counties' District Courts and County Courts at Law),
  `tx-justice-courts` (Justice / small-claims / eviction)
- For family-law matters in the family district courts:
  `tx-family-court`, `tx-family-law`
- For pro se conventions: `tx-pro-se`

## References

- `tx-law-references` — Texas Rules of Civil Procedure, Texas Rules
  of Evidence, the Texas statutes corpus, and the Harris County
  local-rules pointer
- Harris County District Clerk and the Harris County (Civil Trial
  Division) local rules; the assigned court's standing orders
  (confirm current versions with the clerk and the court's website)
