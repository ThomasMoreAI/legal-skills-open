---
name: az-superior-courts-codearranger
title: Arizona Superior Courts — Roll-Up
description: 'Use when filing in an Arizona Superior Court other than Maricopa or Pima, which have their own overlay skills. The Superior Court is Arizona''s single general-jurisdiction court, with a division in each of 15 counties. Covers the other 13 counties as a directory, all applying statewide Ariz. R. Civ. P. but each with its own local rules and compulsory-arbitration jurisdictional limit set by local rule. Triggers: "Arizona Superior Court", "Pinal County Superior Court", "Yavapai Superior Court", "which Arizona Superior Court", "what county is my Arizona case in", "Arizona county superior court local rules", "Arizona compulsory arbitration limit". Tells reader to confirm the county''s local rules, compulsory-arbitration limit, and AZTurboCourt status. Layer on top of `az-statewide-format`.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-superior-courts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Arizona Superior Courts — Roll-Up

> **NOT LEGAL ADVICE.** Drafting and filing guidance only. Verify
> the controlling county's local rules, its compulsory-arbitration
> jurisdictional limit, and its AZTurboCourt e-filing status with
> the clerk and the current rules before filing.

Use this skill in addition to `az-statewide-format` when the case
is in an Arizona **Superior Court** other than the two
highest-volume counties, which have their own overlay skills:

| County | Principal city | Skill |
|--------|----------------|-------|
| Maricopa | Phoenix | `az-maricopa` |
| Pima | Tucson | `az-pima` |

## What the Superior Court is

The **Superior Court** is Arizona's single **court of general
jurisdiction**, established by the Arizona Constitution (art. VI).
It is **one unified statewide court** that sits in **divisions, one
in and for each of the state's 15 counties** — so a filing is
captioned in the "Superior Court of the State of Arizona, in and
for the County of [COUNTY]," not in a separately constituted county
court. It hears:

- **civil cases without a dollar ceiling** (the limited-jurisdiction
  Justice Courts handle civil claims at or below their statutory
  cap — see `az-justice-courts`);
- **domestic relations**, custody, support, and protective-order
  matters (see `az-family-court`, `az-family-law`);
- **felony** criminal matters, **probate**, and **juvenile**; and
- **appeals** from Justice Courts and many municipal and
  administrative matters.

Because the Superior Court is unified, the **statewide Arizona Rules
of Civil Procedure (Ariz. R. Civ. P.)** and **Arizona Rules of
Evidence (Ariz. R. Evid.)** apply in every county. Each county
division layers its own **local rules** on top.

## Confirm the county — and its local rules

**Do not assume a county's practice from another county's.** Each
county's Superior Court adopts **local rules** governing motion
practice, civil case management, scheduling/trial-setting, chambers
or judge copies, and assignment. Look up the controlling county and
its local rules through the Arizona Judicial Branch directory at
**azcourts.gov**.

**Agent behavior:** before drafting anything county-specific (a
notice of hearing, a trial-setting request, a page-limited motion, a
proposed form of order), confirm (1) which county the case is in,
(2) that county's current local rules, and (3) its e-filing status.
Local rules govern on top of the statewide Ariz. R. Civ. P.

## Compulsory arbitration — limit is set per county

Arizona requires **compulsory (court-annexed) arbitration** for civil
cases at or below a dollar threshold, under **Ariz. R. Civ. P. 72-77
and A.R.S. § 12-133**. Critically, the **dollar limit is set by each
county's Superior Court by local rule**, not by a single statewide
number — so the amount-in-controversy cutoff for mandatory
arbitration **varies county to county**. Whether a given case is
subject to compulsory arbitration (and the deadline to file the
Certificate of Compulsory Arbitration that Ariz. R. Civ. P. 72(b)
requires with the complaint) turns on that county's current local
rule. **Confirm the county's arbitration limit before stating whether
a case is arbitration-eligible.**

## Most-populous other counties — directory

Name the county and its principal court location generically;
**confirm each county's local rules, its compulsory-arbitration
limit, and its AZTurboCourt status** before relying on any specific.

| County | Principal court location |
|--------|--------------------------|
| Pinal | Florence |
| Yavapai | Prescott / Camp Verde |
| Mohave | Kingman |
| Yuma | Yuma |
| Coconino | Flagstaff |
| Cochise | Bisbee |
| Navajo | Holbrook |
| Apache | St. Johns |
| Gila | Globe |
| Graham | Safford |
| Greenlee | Clifton |
| La Paz | Parker |
| Santa Cruz | Nogales |

This list covers the other 13 counties (every Arizona county outside
Maricopa and Pima). For any county, confirm the current divisions,
judges, and local rules via the Arizona Judicial Branch directory at
azcourts.gov.

## Caption — generic Superior Court variant

```
        SUPERIOR COURT OF THE STATE OF ARIZONA
        IN AND FOR THE COUNTY OF [COUNTY]

[PLAINTIFF],
       Plaintiff,
v.                                     No. ____________________
                                       [Hon. ___________________]
[DEFENDANT],
       Defendant.
```

See `az-statewide-format` for the full Ariz. R. Civ. P. 10 caption,
the State Bar number in the signature block, and statewide drafting
conventions. The case number and required cover sheet vary by county;
confirm the county's accepted civil case-category codes and whether a
**Certificate of Compulsory Arbitration** must accompany the complaint.

## Filing — AZTurboCourt status varies by county

Arizona e-filing runs through **AZTurboCourt**. E-filing is
**mandatory for some counties and case types and not yet required in
others**, and acceptance details differ by county division. Confirm
the controlling county's AZTurboCourt status and whether e-filing is
mandatory before assembling a packet. See `az-file-packet`.

## Composition

- For statewide format: `az-statewide-format`
- For the two flagship counties: `az-maricopa`, `az-pima`
- For limited-jurisdiction civil claims below the cap:
  `az-justice-courts`
- For domestic relations / custody / support / protective orders:
  `az-family-court`, `az-family-law`
- For the first responsive pleading: `az-first-30-days`
- For scheduling and filing: `az-schedule-hearing`, `az-file-packet`
- For pro se conventions: `az-pro-se`

## References

- `az-law-references` — Ariz. R. Civ. P., Ariz. R. Evid., A.R.S.,
  and local-rules corpus (confirm each county's compulsory-arbitration
  limit and local rules here)
- Arizona Judicial Branch directory (azcourts.gov) — confirm the
  county division, its local rules, and its AZTurboCourt status
