---
name: co-county-courts-codearranger
title: Colorado County Courts — Roll-Up
description: This skill should be used when filing in a Colorado state court other than the Denver District Court (2nd JD) or Arapahoe County District Court (18th JD). Covers the most-populous counties' civil courts (Jefferson, Adams, El Paso, Boulder, Larimer, Douglas, Weld, Pueblo, Mesa, Broomfield) plus a statewide directory of all 22 judicial districts and Colorado's two types of trial courts (district courts and county courts). Triggers include county names ("Jefferson County", "El Paso County", "Boulder County"), JD numbers ("1st JD", "4th JD", "20th JD"), and specific courthouse names. Layer on top of `co-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/co-court-docs/skills/co-county-courts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Colorado County Courts — Roll-Up

> **NOT LEGAL ADVICE.** Drafting and filing guidance only. Verify
> every step against the current local rules of the filing court and
> any chambers practice standards before filing.

Use this skill in addition to `co-statewide-format` when the case is
in a Colorado state court **other than** the Denver District Court
(see `co-denver`) or Arapahoe County District Court (see
`co-arapahoe`). Within Colorado there are two trial courts: the
**District Court** (general civil jurisdiction over $25,000, domestic
relations, probate, juvenile, mental health, felony criminal) and the
**County Court** (limited civil jurisdiction up to $25,000,
small-claims up to $7,500, FED eviction, traffic, misdemeanors).

## Colorado's 22 Judicial Districts

Colorado has 22 judicial districts (with Broomfield County technically
part of the 17th JD as of this writing; the legislature has authorized
a future 23rd JD for Douglas County):

| JD | Counties | Chief seat / principal courthouse |
|---|---|---|
| 1 | Jefferson, Gilpin | Jefferson County Courts & Administration Building, Golden |
| 2 | Denver | Lindsey-Flanigan Courthouse, Denver |
| 3 | Las Animas, Huerfano | Las Animas County Courthouse, Trinidad |
| 4 | El Paso, Teller | El Paso County Combined Courts, Colorado Springs (Centennial Hall) |
| 5 | Clear Creek, Eagle, Lake, Summit | Eagle, Summit, Clear Creek, Lake county courthouses (each) |
| 6 | Archuleta, La Plata, San Juan | La Plata County Courthouse, Durango |
| 7 | Delta, Gunnison, Hinsdale, Montrose, Ouray, San Miguel | Montrose County Courthouse |
| 8 | Jackson, Larimer | Larimer County Justice Center, Fort Collins |
| 9 | Garfield, Pitkin, Rio Blanco | Garfield County Courthouse, Glenwood Springs |
| 10 | Pueblo | Pueblo County Judicial Building |
| 11 | Chaffee, Custer, Fremont, Park | Fremont County Justice Center, Cañon City |
| 12 | Alamosa, Conejos, Costilla, Mineral, Rio Grande, Saguache | Alamosa County Courthouse |
| 13 | Kit Carson, Logan, Morgan, Phillips, Sedgwick, Washington, Yuma | Logan County Justice Center, Sterling |
| 14 | Grand, Moffat, Routt | Routt County Combined Courts, Steamboat Springs |
| 15 | Baca, Cheyenne, Kiowa, Prowers | Prowers County Courthouse, Lamar |
| 16 | Bent, Crowley, Otero | Otero County Courthouse, La Junta |
| 17 | Adams, Broomfield | Adams County Justice Center, Brighton |
| 18 | Arapahoe, Douglas, Elbert, Lincoln | Arapahoe County District Court, Centennial |
| 19 | Weld | Weld County Courthouse, Greeley |
| 20 | Boulder | Boulder County Justice Center, Boulder |
| 21 | Mesa | Mesa County Justice Center, Grand Junction |
| 22 | Dolores, Montezuma | Montezuma County Courthouse, Cortez |

A future **23rd JD** (Douglas County) is authorized by HB22-1210 with
an implementation date in 2025-2026 — verify current effective date
before relying on cross-county practice between Arapahoe and Douglas.

## Most-populous county courts — quick reference

These are the highest-volume civil-filing courts after Denver and
Arapahoe:

### El Paso County District Court (4th JD)

- **Courthouse**: El Paso County Combined Courts (Centennial Hall),
  270 S. Tejon St., Colorado Springs, CO 80903
- **Case number format**: standard `YYYYCV0#####`
- **Distinctives**: Highest combined civil + domestic + criminal
  caseload after Denver. 4th JD operates an Office of the District
  Attorney with significant civil-presence; Civil division generally
  follows statewide C.R.C.P. 121 § 1-15 practice with chambers
  copies required by many judges for motions over 25 pages.
- **Pro se**: 4th JD operates a Self-Help Center on site.

### Jefferson County District Court (1st JD)

- **Courthouse**: Jefferson County Courts & Administration Building,
  100 Jefferson County Pkwy., Golden, CO 80401
- **Phone**: (303) 271-6215 (civil division)
- **Case number format**: standard `YYYYCV0#####`
- **Hours**: Monday-Friday, 8:00 AM - 4:30 PM
- **Distinctives**: One of the busiest civil courts west of Denver.
  Jefferson County is Colorado's 4th most populous county and handles
  a high volume of family law cases. The 1st JD's clerk publishes a
  court-wide standing order on case management; expert disclosures
  and ADR deadlines vary by judge.
- **E-filing**: Uses CCEFS for all electronic filing. Most civil
  divisions request electronic copies of proposed orders via the
  CCEFS workflow and do not require a separate emailed Word copy.
- **Family law practice**: Jefferson County handles significant
  family law caseloads. Family court commissioners hear temporary
  orders, child support modifications, and contested parenting time
  matters. Permanent orders hearings for contested dissolutions
  typically require judicial assignment.
- **Self-help resources**: The 1st JD operates an on-site Self-Help
  Center with family law forms, pro se assistance, and referrals to
  low-cost legal clinics.
- **Local practices**: 
  - Chambers copies required for motions over 25 pages
  - Initial Status Conferences (ISCs) in family cases typically
    scheduled within 42 days of service
  - Mediation encouraged and often court-ordered in family matters
  - Standing case management order addresses discovery deadlines
    and pre-trial requirements

### Adams County District Court (17th JD)

- **Courthouse**: Adams County Justice Center, 1100 Judicial Center
  Drive, Brighton, CO 80601
- **Case number format**: standard `YYYYCV0#####`
- **Distinctives**: The 17th JD now also includes Broomfield County
  matters. Civil judges in Adams typically require **chambers
  copies** for any motion exceeding the standard 15-page limit.

### Boulder County District Court (20th JD)

- **Courthouse**: Boulder County Justice Center, 1777 6th St.,
  Boulder, CO 80302
- **Case number format**: standard `YYYYCV0#####`
- **Distinctives**: The 20th JD has piloted certain complex-case
  management practices; civil divisions are split between Boulder
  and the Longmont satellite (mostly limited-jurisdiction matters in
  Longmont).
- A strong **ADR program** — many Boulder judges actively encourage
  mediation early in the case-management cycle.

### Larimer County District Court (8th JD)

- **Courthouse**: Larimer County Justice Center, 201 LaPorte Ave.,
  Fort Collins, CO 80521
- **Case number format**: standard `YYYYCV0#####`

### Douglas County District Court (currently 18th JD; future 23rd JD)

- **Courthouse**: Douglas County Justice Center, 4000 Justice Way,
  Castle Rock, CO 80109
- Currently administered as part of the 18th JD (see `co-arapahoe`)
  but operating from a separate courthouse with separate divisions.
- HB22-1210 separates Douglas County into its own 23rd JD on a
  phased timeline — verify the **effective date** before relying on
  cross-county venue and procedure between Arapahoe and Douglas.

### Weld County District Court (19th JD)

- **Courthouse**: Weld County Courthouse, 901 9th Ave., Greeley, CO
  80631
- **Case number format**: standard `YYYYCV0#####`

### Pueblo County District Court (10th JD)

- **Courthouse**: Pueblo County Judicial Building, 320 W. 10th St.,
  Pueblo, CO 81003
- **Case number format**: standard `YYYYCV0#####`

### Mesa County District Court (21st JD)

- **Courthouse**: Mesa County Justice Center, 125 N. Spruce St.,
  Grand Junction, CO 81501

### Broomfield County (within 17th JD)

- **Courthouse**: Broomfield Combined Courts, 17 DesCombes Drive,
  Broomfield, CO 80020 — though many filings route to the 17th JD's
  principal Brighton location.

## County Court — limited-jurisdiction civil

Every Colorado county also operates a **County Court** with:

- **Civil jurisdiction up to $25,000** (C.R.S. § 13-6-104) — debt
  collection cases below that threshold typically file here, not in
  district court
- **Small claims up to $7,500** under C.R.S. § 13-6-403; governed by
  C.R.C.P. 501-521 (Rules of Procedure for Small Claims Court);
  attorneys generally not permitted to represent parties under
  C.R.C.P. 510(b) without leave
- **FED (forcible entry and detainer / eviction)** under C.R.S. art.
  40 of title 13 and C.R.C.P. 401
- **Misdemeanors and traffic**

The county court's case-number format is **`YYYYC0######`** (district
court is `YYYYCV0#####`). Captions read "COUNTY COURT, [COUNTY]
COUNTY, COLORADO" rather than "DISTRICT COURT".

### Debt-collection filings — typically county court

Most consumer debt-buyer cases file in **County Court** because the
amount in controversy falls below $25,000. The procedural rules in
county court are C.R.C.P. 301-411 (a streamlined parallel to the
district-court C.R.C.P. 1-129):

- **Answer due**: 21 days from service (C.R.C.P. 312)
- **Trial by judge or jury** (jury demand under C.R.C.P. 338)
- **Limited discovery** as the court directs (no presumptive
  C.R.C.P. 26(a)(1) disclosures in county court)
- **Appeals** to the district court of the same county under C.R.C.P.
  411 within 14 days (C.A.R. 3.1; C.R.C.P. 411)

See `co-consumer-debt` for the typical county-court debt-buyer answer
template.

## County-court small-claims

For amounts under $7,500, the **Small Claims Court** is the
small-volume venue. Key distinctives:

- Pro se only by default (attorney representation requires leave
  per C.R.C.P. 510(b))
- Single-judge trial; no jury
- Limited or no discovery
- Filed using **JDF 250** (Notice, Claim, and Summons to Appear)
- Trial typically held within 60-90 days of filing
- Appeals to the county district court within 14 days of entry of
  judgment under C.R.C.P. 520

## Caption — generic county district court variant

```
DISTRICT COURT, [COUNTY] COUNTY, COLORADO
[Courthouse address]
[City, CO ZIP]

Plaintiff(s): [NAME],                           ▲ COURT USE ONLY ▲
                                                ┌──────────────────┐
v.                                              │ Case Number:     │
                                                │  YYYYCV0#####    │
Defendant(s): [NAME].                           │                  │
                                                │ Division: ##     │
                                                │ Courtroom: ###   │
                                                └──────────────────┘

                [DOCUMENT TITLE IN ALL CAPS]
```

## Authoritative source — pull the current local rules every time

The Colorado Judicial Branch publishes per-JD pages with current
local rules, administrative orders, judges, and chambers practice
standards:

**https://www.coloradojudicial.gov/courts/judicial-districts**

**Agent behavior**: when drafting a notice or scheduling for any
non-Denver / non-Arapahoe court, fetch the current JD page for the
controlling district. Local administrative orders frequently modify
defaults (e.g., **chambers copy** thresholds, **proposed-order Word
copy** requirements, **ADR-by-default** at case management).

## Filing — CCEFS statewide

All Colorado district courts and most county courts accept e-filing
through **Colorado Courts E-Filing (CCEFS)**:

**https://www.jbits.courts.state.co.us/efiling/**

Pro se filers may also file in person at the county clerk's office
or by mail. The Colorado Judicial Branch operates **CCEFS Pro Se**
for unrepresented parties — confirm county-court availability before
relying on it.

## Composition

- For statewide format: `co-statewide-format`
- For Denver matters: `co-denver`
- For Arapahoe matters: `co-arapahoe`
- For drafting motions: `co-draft-motion`
- For pro se conventions: `co-pro-se`
- For consumer-debt defense in county court: `co-consumer-debt`

## References

- `references/jd-directory.md` — full directory of all 22 JDs with
  contact info
- `references/county-court-rules.md` — C.R.C.P. 301-411 (county
  court rules) summary
- `references/small-claims.md` — Small Claims Court process under
  C.R.C.P. 501-521
- `references/fed-eviction.md` — FED procedure in county court
