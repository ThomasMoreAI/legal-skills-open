---
name: tx-dcdc-codearranger
title: Dallas County District Courts
description: Use when drafting or filing civil documents in the Dallas County District Courts. Triggers include "Dallas County District Court", "file in Dallas County", "sued in Dallas County", "Dallas district court", "Dallas County District Clerk", "Dallas County civil district court", "Dallas County family district court", "Dallas County eFileTexas", "Dallas County cause number", "Dallas civil filing", "Dallas County central jury / assignment", "Dallas County local rules", "George Allen Courts Building". Covers the civil and family district courts, the Dallas County local rules, the central jury / case-assignment system, the Dallas County District Clerk and eFileTexas e-filing, and cause-number conventions. Layer on top of `tx-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-dcdc
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Dallas County District Courts

> **NOT LEGAL ADVICE.** These notes describe the venue's procedural
> mechanics as a drafting aid, not legal advice. Local rules,
> standing orders, and judge-specific practices change; verify with
> the Dallas County District Clerk and the current Dallas County
> local rules before relying on anything here.

Use this skill in addition to `tx-statewide-format` when the matter
is a **civil** case in the **Dallas County District Courts**, one of
the largest trial-court systems in Texas, sitting in **Dallas**.

## The court

Texas's general-jurisdiction trial court is the **District Court**.
Dallas County has a large bench of **numbered District Courts** —
each a separate court with its own number and elected judge (for
example, the "192nd Judicial District Court of Dallas County,
Texas"). The Dallas County District Courts are organized into
divisions:

- **Civil District Courts** — general civil litigation, with no upper
  jurisdictional dollar limit; contract, tort, debt, real-property,
  and injunctive matters.
- **Family District Courts** — divorce, SAPCR, and related
  domestic-relations matters. Route family matters through
  `tx-family-court`.
- (Criminal District Courts handle felonies and are outside this
  civil-drafting skill.)

A civil action is captioned in the **[Nth] Judicial District Court of
Dallas County, Texas** — see `tx-statewide-format` for the full
caption with the **§** divider.

## Case assignment and the central jury system

Dallas County administers its civil District Courts through a
county-managed **case-assignment** and **central jury** system: a new
civil case is filed with the District Clerk and assigned to a District
Court, which manages it to disposition, while jurors are drawn through
a centralized jury operation. Confirm the current assignment and
trial-setting mechanics — including how a case is set for trial and
how emergency/ancillary relief is heard when the assigned court is
unavailable — with the clerk and the Dallas County local rules before
relying on them.

## Local rules

Practice in these courts is governed by the **statewide Texas Rules of
Civil Procedure (TRCP)** and **Texas Rules of Evidence (Tex. R.
Evid.)**, as supplemented by the **Dallas County (Civil District
Courts) local rules** and each judge's standing orders / court
procedures. The local rules and standing orders address civil case
management, scheduling / docket control orders, motion-setting and
oral-hearing practice, and chambers-copy requirements.

Do not hard-code rule numbers, page limits, or motion-setting
mechanics from memory — read the current Dallas County local rules
and the assigned court's standing orders in `tx-law-references` (or
confirm with the clerk and the court's website) before relying on
them.

## E-filing — the Dallas County District Clerk and eFileTexas

The **Dallas County District Clerk** maintains the district-court
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
through a **scheduling / docket control order** setting discovery
deadlines tied to the **TRCP 190 discovery level**, dispositive-motion
dates (note the **TRCP 166a** summary-judgment timing — motion served
at least **21 days** before the hearing, response due **7 days**
before, and Texas's distinct **no-evidence** motion under 166a(i)),
and the trial setting. **Calendar your obligations from the
scheduling order entered in your specific case**, and confirm the
assigned judge's individual procedures and any chambers-copy
requirement. See `tx-schedule-hearing`, `tx-hearings`, `tx-discovery`,
and `tx-deadlines`.

## Cause-number conventions

A Dallas County civil cause number follows the county's pattern
(commonly a year/case-type designation plus a sequential number, with
a court designation assigned at intake). **Confirm the exact
cause-number format and the assigned court** the District Clerk gives
your case; once assigned, the cause number and the assigned court
anchor the caption per `tx-statewide-format`. Do not guess the format
— verify it against the clerk's intake.

**Agent behavior:** before drafting a Notice of Hearing, setting a
page-limited motion, or calendaring a deadline, read the current
Dallas County local rules and the assigned court's standing orders in
`tx-law-references`, the scheduling order entered in the case, and the
assigned judge's procedures. Confirm the civil-vs-family division, the
eFileTexas document-type selection, and any chambers-copy requirement
with the clerk.

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
- For other venues: `tx-hcdc` (Harris County / Houston),
  `tx-county-courts` (other counties' District Courts and County
  Courts at Law), `tx-justice-courts` (Justice / small-claims /
  eviction)
- For family-law matters in the family district courts:
  `tx-family-court`, `tx-family-law`
- For pro se conventions: `tx-pro-se`

## References

- `tx-law-references` — Texas Rules of Civil Procedure, Texas Rules
  of Evidence, the Texas statutes corpus, and the Dallas County
  local-rules pointer
- Dallas County District Clerk and the Dallas County (Civil District
  Courts) local rules; the assigned court's standing orders (confirm
  current versions with the clerk and the court's website)
