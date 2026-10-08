---
name: wa-kcsc-codearranger
title: King County Superior Court
description: This skill should be used when drafting or filing documents in the King County Superior Court (KCSC), the general-jurisdiction trial court for King County, sitting in Seattle (King County Courthouse) and Kent (Maleng Regional Justice Center, "MRJC"). Triggers include "KCSC", "King County Superior Court", "Seattle case assignment area" / "Kent case assignment area", "MRJC", "Maleng Regional Justice Center", "case schedule" / "order setting civil case schedule", "case information cover sheet" / "case assignment designation" / "CICS", "working copies to the judge", "Submit Working Copies", "Note for Civil Motion Calendar" in King County Superior Court, "Ex Parte via the Clerk", or a KCSC cause number ("25-2-#####-# SEA" / "... KNT"). For the King County *District* Court (limited jurisdiction, ≤ $100,000) use the `wa-kcdc` skill; for other counties' superior/district courts use `wa-county-courts`. Layer on top of the `wa-statewide-format` skill.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-kcsc
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Civil Motion Practice
  path: references/civil-motion-practice.md
- title: Filing Procedures
  path: references/filing-procedures.md
- title: Seattle And Mrjc
  path: references/seattle-and-mrjc.md
---

# King County Superior Court

Use this skill in addition to `wa-statewide-format` when the case is in
King County Superior Court (KCSC). KCSC is the court of **general
jurisdiction** for King County (matters above the $100,000 district-court
ceiling, plus anything filed in superior court by choice — many
debt-collection and consumer-protection actions land here), and it sits
at two facilities:

> **NOT LEGAL ADVICE.** These notes describe the venue's
> procedural mechanics as a drafting aid, not legal advice. Local
> rules and judge-specific practices change; verify with the clerk
> and the current local rules before relying on anything here.

- **King County Courthouse — Seattle**, 516 Third Ave, Seattle, WA 98104
- **Maleng Regional Justice Center (MRJC) — Kent**, 401 Fourth Ave N,
  Kent, WA 98032

Each facility hosts its share of judge departments, an Ex Parte and
Probate department, and Clerk's filing windows. Which facility a case is
assigned to is fixed by the **Case Assignment Area** under **LCR 82**
(Seattle vs. Kent), and that area travels with the cause number for the
life of the case.

## Caption — KCSC variant

```
   IN THE SUPERIOR COURT OF THE STATE OF WASHINGTON
            IN AND FOR THE COUNTY OF KING
```

Cause numbers follow `YY-2-######-# SEA` or `YY-2-######-# KNT` for civil
cases (year, case-type digit `2`, sequence, check digit, and the **case
assignment area code** — `SEA` for Seattle, `KNT` for Kent). Include the
**full number with the area code** on the right side of the caption
directly below "No." Per LCR 82, the Clerk **may reject** a filing that
omits the area code.

## Authoritative source — pull the current form, calendar, and LCR every time

The King County Superior Court site and the Department of Judicial
Administration (DJA, the Clerk) are the canonical sources for the current
e-filing application, the **Submit Working Copies** tool, the case
schedule template, the **CICS / Case Assignment Designation** form, and
the local rules:

- **Superior Court** —
  `https://kingcounty.gov/en/court/superior-court`
- **DJA (Clerk's Office) — filing and forms** —
  `https://kingcounty.gov/en/dept/dja`
  → "Court forms and document filing" → **Electronic Filing** and **Forms**
- **King County LCR (local civil rules)** — on the DJA site
  (`https://kingcounty.gov/en/dept/dja/courts-jails-legal-system/superior-court-local-rules/local-civil-rules`)
  and at `https://www.courts.wa.gov/court_rules/` → "Superior Court
  Rules" → King County. The LCR is amended roughly annually — check the
  effective date stamped on the rule set.

**Agent behavior**: when drafting a Note for Civil Motion Calendar,
preparing working copies, scheduling an ex parte presentation, or filing
an initial pleading, fetch the current form and the current LCR text from
the sources above. Department assignments, motion calendar timing, the
working-copy submission tool, and LCR provisions change without notice —
do not cache values across sessions or rely on specifics hardcoded in
this plugin. The in-repo `wa-law-references/references/court-rules/`
corpus carries the **statewide** rule sets (CR, ER, etc.); the King
County LCR is **not** mirrored there.

## Civil motion practice — noted to the assigned department (LCR 7)

KCSC does **not** run a single county-wide motion docket the way KCDC
does. Instead, a noted civil motion is set on the **assigned judge's
department calendar**, or — for certain agreed or procedural matters —
presented in **Ex Parte** (Ex Parte via the Clerk, or the Ex Parte and
Probate Department in person).

**Step 1 — Decide where the motion goes.**

- **A case with an assigned judge**: note the motion on that department's
  civil motion calendar, following the department's posted procedures
  (most departments accept self-noting; check the department's page on
  the Superior Court site for any cutoff, page-limit, or scheduling-clerk
  requirement).
- **Chief Civil** hears certain pre-assignment and cross-departmental
  matters.
- **Ex Parte** (agreed orders, defaults, supplemental-proceeding orders,
  many procedural orders): present via the Clerk's **Ex Parte via the
  Clerk** process, or in person at the Ex Parte and Probate Department.

**Step 2 — Note the motion with the LCR 7 / CR 6 notice period.**

Compute timing under **LCR 7** read with **CR 6** (and apply RCW 1.16.050
holidays — use the `wa-deadlines` skill). Read the current LCR 7 for the
exact numbers (commonly **at least 9 court days** before the hearing for
a noted civil motion served in person, with shorter periods if served
electronically and specific response/reply deadlines — confirm the
current text). Do **not** rely on memorized numbers; LCR 7 has been
amended.

**Step 3 — Confirm the motion.**

The moving party generally must **confirm** the motion (and state whether
oral argument is requested) by the deadline in LCR 7 / the department's
posted procedure. An unconfirmed motion is typically **struck**.

**Step 4 — Deliver working copies (mandatory — see below).**

**Step 5 — E-file the packet through the Clerk.**

E-file the Note for Civil Motion Calendar, Motion, supporting
Declaration(s), exhibits, and Proposed Order through the **King County
Superior Court Clerk's E-Filing application** (linked from the DJA
filing page above). The Clerk returns an electronic conformed copy for
initial pleadings. Serve under **CR 5** the same day and attach a
Declaration/Certificate of Service.

> ⚠ **Filings without the case-assignment-area code in the cause number
> may be rejected under LCR 82**, and **motions without timely working
> copies are often passed over** — see `references/civil-motion-practice.md`.

## Confirmations, continuances, and strikes

- **Confirmations**: KCSC **requires** confirmation of contested civil
  motions under LCR 7 (this is different from KCDC, which does not).
  Confirm by the LCR 7 / department deadline, and state whether oral
  argument is requested. Unconfirmed motions are struck.
- **Continuances**: by agreement, submit an **Agreed Order to Continue**
  via the Ex Parte process before the hearing; contested continuances go
  as a **noted motion** to the assigned department.
- **Strikes**: notify the assigned department and serve the other parties
  promptly; follow the department's posted strike procedure.

## Filing rules of thumb

- **E-filing**: e-file through the **Superior Court Clerk's E-Filing
  application** (DJA). Initial pleading e-filings receive an electronic
  conformed copy back from the Clerk. View later filings through
  **eRecords**.
- **Case Information Cover Sheet / Case Assignment Designation
  ("CICS")**: filed with the **initial pleading** — it classifies the
  case type and certifies the LCR 82 assignment area. Civil and
  family-law versions exist; use the **civil** CICS for a debt or
  general civil matter. Pull the current form from the DJA forms page.
- **Order Setting Civil Case Schedule (LCR 4)**: for most civil case
  types, the Clerk issues a **Case Schedule** at filing that fixes
  deadlines (confirmation of joinder, witness disclosures, discovery
  cutoff, dispositive-motion cutoff, **trial date**, etc.) keyed to the
  filing date. Some case types are exempt — check LCR 4. Missing a Case
  Schedule deadline can mean sanctions or exclusion of evidence.
- **Working copies**: **required** under LCR 7. Deliver to the assigned
  judge's department through the Clerk's **Submit Working Copies** tool
  (or as the department directs) by the LCR 7 deadline, with the
  working-copy coversheet.
- **Service**: serve opposing counsel the same day under CR 5 (email,
  personal, mail, fax as permitted). Attach a Certificate / Declaration
  of Service to every filing.
- **Format**: GR 14 plus the King County LCR formatting provisions —
  run `plugins/wa-court-docs/scripts/format-check.py` and the
  `wa-quality-check` skill before filing.

## Document set for a noted motion

Every motion noted for a civil motion calendar should travel as a packet:

1. **Motion** (primary relief sought)
2. **Supporting Memorandum** (argument; only if the motion is not
   self-contained)
3. **Supporting Declaration(s)** with exhibits
4. **Proposed Order** granting the relief
5. **Note for Civil Motion Calendar** (the department's scheduling form)
6. **Certificate / Declaration of Service**
7. **Working copies** of items 1–5, delivered separately through the
   Submit Working Copies tool with the working-copy coversheet (LCR 7)

When e-filing, upload each item as a separate PDF. Working copies are
**not** filed in the Clerk's record — they are delivered to chambers.

## Note for Civil Motion Calendar — recommended template

Unlike KCDC, KCSC does **not** require an email date request to a
central scheduler before filing. The moving party generally **self-notes**
the motion (subject to the assigned department's posted procedures) on a
date that meets LCR 7 / CR 6 timing.

The Note for Civil Motion Calendar travels with the motion packet; pull
the current King County form from the DJA forms page. Required content:

```
   IN THE SUPERIOR COURT OF THE STATE OF WASHINGTON
            IN AND FOR THE COUNTY OF KING

[Plaintiff],                       NO. [YY-2-#####-# SEA/KNT]
              Plaintiff,
   v.                              NOTE FOR CIVIL MOTION CALENDAR
[Defendant],
              Defendant.

TO THE CLERK OF THE COURT AND TO ALL PARTIES:

PLEASE TAKE NOTICE that [movant] will bring the following motion on
for hearing before the Honorable [judge], Department [#], on
[date] at [time], at the [Seattle / Kent (MRJC)] facility:

   [Exact motion title, e.g., Defendant's Motion to Compel
   Discovery under CR 37(a)]

[X]  Oral argument is requested.   [ ]  Oral argument is waived.

Estimated time required: [minutes].

DATED this ___ day of __________, 20__.

                                 ______________________________
                                 [Name][, pro se if applicable]
                                 [Address] [Phone] [Email]
```

Confirm the motion by the LCR 7 deadline (the department's posted
procedure says how — typically through the department's online
confirmation page).

## RALJ appeals from KCDC

Appeals from King County **District** Court go to KCSC under the
**RALJ** (Rules for Appeal of Decisions of Courts of Limited
Jurisdiction). Timing, notice of appeal, and record designation are
governed by the RALJ (text in
`wa-law-references/references/court-rules/RALJ.md`) plus the King County
LCR's RALJ provisions — not by the RAP. Use `wa-deadlines` for the
deadlines.

## References

- `references/seattle-and-mrjc.md` — facilities, LCR 82 case assignment
  area, the CICS form, the cause-number code
- `references/civil-motion-practice.md` — LCR 7 noting/confirmation,
  LCR 4 case schedule, working copies, the Note for Civil Motion
  Calendar
- `references/filing-procedures.md` — e-filing through the Clerk
  (DJA), service under CR 5, working-copy mechanics, Certificate of
  Service template
