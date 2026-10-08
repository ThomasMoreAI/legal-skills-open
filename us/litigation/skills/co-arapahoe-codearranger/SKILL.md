---
name: co-arapahoe-codearranger
title: Arapahoe County District Court (18th Judicial District)
description: This skill should be used when drafting or filing documents in the Arapahoe County District Court (part of the 18th Judicial District, which also covers Douglas, Elbert, and Lincoln counties). Triggers include "Arapahoe County District Court", "18th JD", "Centennial courthouse", "Arapahoe County Justice Center", "Littleton courthouse", "Aurora courthouse", "Robert A. Christensen Justice Center". Covers the three Arapahoe courthouse locations (Centennial, Aurora, Littleton), the 18th JD local civil-practice standards, the multi-county venue rules that distinguish Arapahoe from neighboring Douglas County District Court, and the chambers preferences for the principal civil divisions. Layer on top of `co-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/co-court-docs/skills/co-arapahoe
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Arapahoe County District Court (18th Judicial District)

> **NOT LEGAL ADVICE.** Drafting and filing guidance only. Verify
> every step against the current 18th JD local rules and chambers
> preferences before filing.

Use this skill in addition to `co-statewide-format` when the case is
in the **Arapahoe County District Court**, part of the **18th
Judicial District** (which also covers **Douglas, Elbert, and
Lincoln** counties — though Douglas County District Court will
become its own JD as a result of HB22-1210 separation; verify
current effective date before relying on cross-county practice).

The 18th JD is the second-busiest judicial district in Colorado by
civil-case volume after Denver and El Paso.

## Three courthouse locations

| Courthouse | Address | Use |
|------------|---------|-----|
| **Arapahoe County District Court — Centennial** | 7325 S. Potomac St., Centennial, CO 80112 | Principal civil court; most CV cases filed here |
| **Aurora Municipal Justice Center (state)** | 14999 E. Alameda Pkwy., Aurora, CO 80012 | Some Arapahoe County Court matters, traffic, evictions |
| **Robert A. Christensen Justice Center — Littleton** | 1790 W. Littleton Blvd., Littleton, CO 80120 | Domestic relations, juvenile, mental health |

The principal civil filing location is the **Centennial courthouse**.
The court's website publishes assignment-by-courtroom information.

## Caption — Arapahoe District Court variant

```
DISTRICT COURT, ARAPAHOE COUNTY, COLORADO
7325 South Potomac Street
Centennial, CO 80112

Plaintiff(s): PORTFOLIO RECOVERY ASSOCIATES, LLC,  ▲ COURT USE ONLY ▲
                                                  ┌───────────────────┐
v.                                                │ Case Number:      │
                                                  │  2025CV031987     │
Defendant(s): JOHN DOE.                           │                   │
                                                  │ Division: 24      │
                                                  │ Courtroom: 401    │
                                                  └───────────────────┘

                  MOTION TO DISMISS
              (UNDER C.R.C.P. 12(b)(5))
```

Case numbers follow the standard `YYYYCV0#####` format. The Division
identifies the assigned judge's chambers; the Courtroom identifies
the physical hearing room (rooms 200-series are on the second floor,
400-series on the fourth floor of the Centennial courthouse).

## Authoritative source — pull the current chambers info every time

The 18th JD publishes its current chambers roster, courtroom
assignments, and judges' practice standards at:

**https://www.coloradojudicial.gov/courts/judicial-districts/18th-judicial-district**

**Agent behavior**: before drafting a notice, scheduling a hearing,
or formatting a chambers-copy cover sheet, fetch the current
division-to-judge mapping and the assigned judge's practice
standards. The 18th JD rotates civil-domestic-criminal assignments
periodically, and chambers preferences (e.g., chambers copy
required for any motion over 25 pages, courtesy email of proposed
orders in Word format) vary by judge.

## Motion practice — C.R.C.P. 121 § 1-15 + local conventions

Statewide C.R.C.P. 121 § 1-15 timing applies as in Denver:

- **Response**: 21 days after service
- **Reply**: 7 days after service of the response
- **Page limits**: 15 (motion / response), 10 (reply); leave required
  for excess

**18th JD distinctives:**

- Most Arapahoe District judges require a **certificate of conferral**
  (C.R.C.P. 121 § 1-15(8)) even for some borderline-dispositive
  motions — practice is to confer and certify even when in doubt.
- **Chambers copies**: some judges require courtesy copies for
  motions exceeding 20-25 pages. Always check the judge's practice
  standards; if required, deliver to the chambers office on the
  same day as e-filing.
- **Proposed orders**: many judges request a **Word-format**
  proposed order emailed directly to chambers in addition to the
  PDF filed through CCEFS. The cover sheet on the chambers copy
  should note "Proposed Order also emailed in Word format."

## Case management — C.R.C.P. 16(b)

The 18th JD follows the C.R.C.P. 16(b) timeline. The clerk's office
sets an **initial case-management conference** approximately 49 days
after the case is at issue. The parties file a **joint proposed
Case Management Order** 7 days before the CMC. The court holds the
CMC by phone or, in complex cases, in-person at the assigned
courtroom.

## Filing — CCEFS

Same as statewide. The 18th JD requires e-filing for represented
parties; pro se filers may file by paper or use CCEFS Pro Se.

Civil filing fees match the statewide schedule (C.R.S. § 13-32-101).

## Service of process

C.R.C.P. 4 service deadlines apply (63 days from complaint filing).
The Arapahoe County Sheriff's Office processes civil service
requests for in-county service; private process servers are used
extensively in the 18th JD.

## Document set for a noted motion

Identical to Denver (see `co-denver`):

1. Motion (with title in ALL CAPS citing the rule)
2. Supporting affidavit/declaration(s) with exhibits
3. Certificate of Conferral (C.R.C.P. 121 § 1-15(8))
4. Proposed Order (separate document; some judges require an
   additional Word-format email copy)
5. Certificate of Service

## Pro se resources

The 18th JD operates a **Self-Help Center** at the Centennial
courthouse. JDF forms (see `co-pro-se`) are universally accepted
for pro se filings.

## Composition

- For statewide format: `co-statewide-format`
- For motion drafting: `co-draft-motion`
- For scheduling: `co-schedule-hearing`
- For filing mechanics: `co-file-packet`
- For pro se workflows: `co-pro-se`
- For Denver matters (the other principal Colorado civil court):
  `co-denver`

## References

- `references/centennial-courthouse.md` — facility info, parking,
  clerk hours
- `references/civil-divisions.md` — division-to-judge mapping
- `references/filing-procedures.md` — CCEFS workflows, chambers
  copy conventions, Word-format proposed orders
