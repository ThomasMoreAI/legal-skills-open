---
name: tx-county-courts-codearranger
title: Texas District Courts and County Courts — Roll-Up (Other Counties)
description: Use when filing in a Texas District Court or County Court at Law OTHER than the Harris County (`tx-hcdc`) or Dallas County (`tx-dcdc`) District Courts, and other than Justice Courts. Covers the long tail of Texas counties and the District Court vs. County Court at Law vs. Constitutional County Court jurisdictional split. Triggers include "Texas District Court", "which Texas court do I file in", "County Court at Law Texas", "Constitutional County Court", "Travis County District Court", "Bexar County District Court", "Tarrant County District Court", "Smith County District Court", "Smith County Court at Law", "Tyler Texas district court", "appeal from JP to county court Texas", "de novo appeal county court", "Texas county civil court jurisdiction", "what is the jurisdictional limit of a Texas county court at law". Tells the reader to confirm the county's courts, their local rules, and the current jurisdictional dollar caps. Layer on top of `tx-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-county-courts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Texas District Courts and County Courts — Roll-Up (Other Counties)

> **NOT LEGAL ADVICE.** Drafting and filing guidance only. Verify the
> county's courts, their current local rules, the controlling
> jurisdictional dollar caps, and the e-filing posture with the clerk
> and the current statutes before filing.

Use this skill in addition to `tx-statewide-format` when the case is
in a Texas **District Court** or **County Court at Law** in a county
other than the two highest-volume systems, which have their own
overlay skills:

| County | Principal city | Skill |
|--------|----------------|-------|
| Harris | Houston | `tx-hcdc` |
| Dallas | Dallas | `tx-dcdc` |

Justice of the Peace / small-claims / eviction matters are **not**
covered here — see `tx-justice-courts` (and `tx-smith-county-jp` for
Smith County's JP precincts).

## The three civil trial-court tiers — the jurisdictional split

Texas civil trial jurisdiction is split across three court types, and
routing the case to the right tier matters. The **dollar
jurisdictional caps are statutory and drift-prone** — confirm the
current figures against the Texas Government Code (court-organization
chapters) and the corpus, and do not hard-code them:

- **District Court** — the general-jurisdiction trial court. **No
  upper jurisdictional dollar limit.** Hears larger civil disputes,
  **title to land**, **divorce and SAPCR** (family — see
  `tx-family-court`), defamation, injunctive relief, and felonies.
  Numbered and named by the county it sits in (e.g., "[Nth] Judicial
  District Court of [County] County, Texas"). A district may serve a
  single county or several smaller counties.
- **County Court at Law (statutory county court)** — a mid-tier civil
  court created by statute (Gov't Code Ch. 25) in the more populous
  counties. Hears civil matters within a **statutory amount-in-
  controversy range** (the floor and ceiling are set by statute and
  vary; confirm the current range against the corpus), **probate** in
  many counties, and **de novo appeals from the Justice Courts**.
- **Constitutional County Court** — the single county court presided
  over by the **county judge** (a constitutional office, Gov't Code
  Ch. 26). It has a **limited civil amount-in-controversy
  jurisdiction** (statutory floor and ceiling — confirm against the
  corpus), probate, and certain appeals. In counties **without** a
  County Court at Law, the constitutional county court carries the
  mid-tier civil and probate docket; in counties **with** statutory
  County Courts at Law, much of the civil docket shifts to them.

Concurrent and overlapping jurisdiction is common (e.g., District
Court and County Court at Law may share a band of amounts).
**Confirm the county's specific court structure** — how many District
Courts, how many County Courts at Law, and which court hears which
matter — with the clerk and the county's website before choosing a
tier; a misfiled case can be challenged or transferred.

## De novo appeal from a Justice Court to the county court

An appeal from a **Justice Court** judgment goes **de novo** — a
brand-new trial — to the **county court** (the County Court at Law or
the Constitutional County Court, as the county's structure provides).
The appellant perfects the appeal under **TRCP 506** by filing an
appeal bond, making a cash deposit, or filing a **Statement of
Inability to Afford Payment of Court Costs**, within the rule's
short deadline. The case is then tried anew in the county court as if
it had originated there. The Justice Court mechanics and the appeal
trigger live in `tx-justice-courts`; this skill is the **destination
court** for that de novo appeal.

## The long tail of counties — handled here

Texas has 254 counties. Beyond Harris and Dallas, the most populous
include **Tarrant** (Fort Worth), **Bexar** (San Antonio), **Travis**
(Austin), **Collin** (McKinney), **Denton**, **El Paso**,
**Hidalgo**, **Fort Bend**, **Montgomery**, and **Williamson** — each
with its own District Courts, County Courts at Law, District Clerk,
and County Clerk, and its own local rules. **Smith County** (county
seat **Tyler**) belongs here for its higher-tier matters: its
**District Courts** (the 7th, 114th, 241st, 321st (family), and 475th
Judicial District Courts — confirm the current list with the district
clerk) and its **County Courts at Law** (confirm the current count).
Smith County's **Justice of the Peace** precincts are handled
separately in `tx-smith-county-jp`.

Do not create a separate skill per county — confirm the controlling
county's courts and local rules through the county's District Clerk /
County Clerk and the Texas Judicial Branch directory, and draft to
the statewide TRCP plus that county's local rules.

## Local rules — confirm per county

Practice is governed by the **statewide TRCP** and **Texas Rules of
Evidence**, supplemented by **each county's local rules** and each
judge's standing orders. Local rules govern civil case management,
scheduling / docket control, motion-setting and oral-hearing
practice, and chambers copies. **Do not assume one county's practice
from another's.**

**Agent behavior:** before drafting anything county-specific (a
Notice of Hearing, a trial-setting request, a page-limited motion, a
proposed order), confirm (1) which county and which court tier the
case is in, (2) the controlling jurisdictional dollar caps from the
corpus, (3) that county's current local rules and the assigned
judge's standing orders, and (4) its eFileTexas posture.

## Caption — generic variants

```
                          CAUSE NO. ____________

[PLAINTIFF],                       §   IN THE [NTH] JUDICIAL
                                   §   DISTRICT COURT
       Plaintiff,                  §
v.                                 §   OF
                                   §
[DEFENDANT],                       §
       Defendant.                  §   [COUNTY] COUNTY, TEXAS
```

For a County Court at Law, substitute `IN THE COUNTY COURT AT LAW NO.
[N] OF [COUNTY] COUNTY, TEXAS`; for a Constitutional County Court,
`IN THE COUNTY COURT OF [COUNTY] COUNTY, TEXAS`. See
`tx-statewide-format` for the full caption with the **§** divider, the
TRCP 57 signature block with the **State Bar of Texas number**, and
statewide drafting conventions. Confirm the county's accepted civil
case-type codes and cause-number format with the clerk.

## Filing — eFileTexas posture

Texas e-filing runs through **eFileTexas.gov** (Odyssey File &
Serve), under **TRCP 21(f)** and **Tex. R. Jud. Admin. 10**. E-filing
is **mandatory for attorneys** in civil matters in the District
Courts and statutory/constitutional County Courts; **self-represented
filers may e-file** and are encouraged to. The **civil case
information sheet (TRCP 78a)** accompanies the initial filing. Confirm
the controlling county's document-type selections and the filing-fee
/ fee-waiver workflow before assembling a packet. See
`tx-file-packet`.

## Composition

- For statewide format and the Texas caption: `tx-statewide-format`
- For the two flagship counties: `tx-hcdc` (Harris / Houston),
  `tx-dcdc` (Dallas)
- For Justice / small-claims / eviction and the de novo appeal
  trigger: `tx-justice-courts` (and `tx-smith-county-jp` for Smith
  County's JP precincts)
- For the Original Answer and the TRCP 99 "Monday rule":
  `tx-first-30-days`
- For drafting motions / declarations / notices / orders:
  `tx-draft-motion`, `tx-draft-declaration`, `tx-draft-note`,
  `tx-draft-order`
- For discovery and deadlines: `tx-discovery`, `tx-deadlines`
- For scheduling and filing: `tx-schedule-hearing`, `tx-hearings`,
  `tx-file-packet`
- For family-law venue and intake: `tx-family-court`, `tx-family-law`
- For pro se conventions: `tx-pro-se`

## References

- `tx-law-references` — Texas Rules of Civil Procedure, Texas Rules
  of Evidence, the Government Code court-organization and
  jurisdiction provisions (for the current dollar caps), and the
  per-county local-rules pointers
- The Texas Judicial Branch directory and each county's District
  Clerk / County Clerk — confirm the county's courts, its local
  rules and standing orders, and its eFileTexas posture
