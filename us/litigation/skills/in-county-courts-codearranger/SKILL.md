---
name: in-county-courts-codearranger
title: 'Indiana County Courts (Roll-Up: All Counties Other Than Marion + Lake)'
description: 'This skill should be used when the user asks to "file in Allen Superior Court", "St. Joseph County", "Hamilton Superior", "Vigo Circuit", "Vanderburgh Superior", "Tippecanoe County", "Hendricks Superior", "Johnson County", "Madison County", "Porter County", "Clark County", "Howard Superior", "LaPorte Superior", "Elkhart Superior", "Bartholomew County", "Monroe Superior", or any other Indiana county court other than Marion or Lake. Covers the most-populous Indiana counties'' Circuit and Superior Courts plus a directory and roll-up of statewide practice quirks, the relationship between Circuit Courts (IC 33-28) and Superior Courts (IC 33-29) within a single county, and concurrent jurisdiction rules. Trigger phrases: "Allen Superior", "St. Joseph Circuit", "Hamilton County", "Tippecanoe", "Monroe Circuit Court", "Indiana county court", "Indiana Circuit Court", "Indiana judicial district".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/in-court-docs/skills/in-county-courts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Indiana County Courts (Roll-Up: All Counties Other Than Marion + Lake)

This skill covers Indiana's other 90 counties — the most-populous
counties by civil docket are detailed below, and the long tail is
served by the statewide directory. Indiana has **92 counties**,
each with its own Circuit Court (IC 33-28) and most also have one
or more Superior Courts (IC 33-29). Most counties have
**concurrent civil jurisdiction** between the Circuit Court and
the Superior Court(s); the Circuit Court has the constitutionally
guaranteed jurisdiction (Ind. Const. art. 7, § 8) and the
Superior Court is statutory (IC 33-29-1-1).

> **NOT LEGAL ADVICE.** Generated content is a drafting aid;
> verify against the current local rules of the venue county and
> the assigned court's chambers practice before filing.

## Circuit vs. Superior Court — what's the difference?

**Functionally, very little** in most counties. Both courts have:

- Civil jurisdiction over the same dollar amounts (no monetary
  ceiling in the Circuit Court; no monetary floor in most Superior
  Courts)
- Criminal jurisdiction (Class C/D felonies and misdemeanors in
  most Superior Courts; full felony jurisdiction in Circuit
  Courts)
- Probate, juvenile, family-law jurisdiction (varies by county
  rule)

The historical distinction:

- **Circuit Courts** are constitutional; every county has exactly
  one Circuit Court with one elected judge.
- **Superior Courts** are statutory; counties with sufficient
  population get one or more Superior Courts to handle overflow.

**Cause-number prefix** identifies which:

- `[CC]C01` = Circuit Court of that county (e.g., `49C01` = Marion
  Circuit; `02C01` = Allen Circuit; `71C01` = St. Joseph Circuit)
- `[CC]D01`, `D02`, ... = Superior Court Divisions (e.g., `02D02`
  = Allen Superior Court 2; `71D01` = St. Joseph Superior 1)

The Indiana county code map is on the Indiana Supreme Court's
website; the first two digits of every cause number identify the
county (`01` Adams, `02` Allen, `03` Bartholomew, ..., `92`
Whitley).

## Most-populous counties — at-a-glance directory

### Allen County (02) — Fort Wayne

- **Allen Circuit Court** (02C01) — Allen County Courthouse, 715 S.
  Calhoun St., Fort Wayne, IN 46802
- **Allen Superior Courts 1-9** (02D01-D09) — sub-specialized by
  case type:
  - 02D01 — Civil Plenary
  - 02D02 — Civil Plenary
  - 02D03 — Civil Plenary / Domestic Relations
  - 02D04 — Civil Collections
  - 02D05 — Criminal
  - 02D06 — Criminal
  - 02D07 — Domestic Relations
  - 02D08 — Family Relations
  - 02D09 — Juvenile
- **Local rules**: LR02 series. Allen has its own civil case-
  management standing order similar to Marion's CPC.
- **E-filing**: Mandatory via Odyssey since 2018.

### St. Joseph County (71) — South Bend / Mishawaka

- **St. Joseph Circuit Court** (71C01) — 101 S. Main Street, South
  Bend, IN 46601
- **St. Joseph Superior Courts 1-8** (71D01-D08) — divided across
  South Bend and Mishawaka locations; specialized civil and
  domestic-relations divisions
- **Local rules**: LR71 series.
- **Notable**: St. Joseph has a separate **Probate Court** (71J01)
  for estates and adoptions.

### Hamilton County (29) — Noblesville / Fishers / Carmel

- **Hamilton Circuit Court** (29C01) — Hamilton County Government
  & Judicial Center, One Hamilton County Square, Noblesville, IN
  46060
- **Hamilton Superior Courts 1-7** (29D01-D07) — fast-growing
  docket; 29D01-D03 carry civil cases, 29D04-D07 split between
  criminal and family law
- **Local rules**: LR29 series; Hamilton requires a CMS within 45
  days (faster than Marion's 60).
- **E-filing**: Mandatory.

### Vanderburgh County (82) — Evansville

- **Vanderburgh Circuit Court** (82C01) — Civic Center Complex,
  1 N.W. Martin Luther King Jr. Blvd., Evansville, IN 47708
- **Vanderburgh Superior Courts 1-6** (82D01-D06) — Civil Division
  1 and 2; County Division for small claims
- **Local rules**: LR82 series.

### Tippecanoe County (79) — Lafayette / West Lafayette

- **Tippecanoe Circuit Court** (79C01) — 301 Main Street,
  Lafayette, IN 47901
- **Tippecanoe Superior Courts 1-6** (79D01-D06) — civil docket
  splits across D01-D03
- **Local rules**: LR79 series.

### Vigo County (84) — Terre Haute

- **Vigo Circuit Court** (84C01) — Vigo County Courthouse, 33 S.
  3rd St., Terre Haute, IN 47807
- **Vigo Superior Courts 1-6** (84D01-D06)
- **Local rules**: LR84 series.

### Elkhart County (20) — Goshen / Elkhart

- **Elkhart Circuit Court** (20C01) — 101 N. Main Street, Goshen,
  IN 46526
- **Elkhart Superior Courts 1-6** (20D01-D06) — civil docket
  through D01 and D02
- **Local rules**: LR20 series.

### Hendricks County (32) — Danville

- **Hendricks Circuit Court** (32C01) — 1 Courthouse Square,
  Danville, IN 46122
- **Hendricks Superior Courts 1-5** (32D01-D05)
- **Local rules**: LR32 series. Fast-growing suburban-Indianapolis
  docket.

### Johnson County (41) — Franklin / Greenwood

- **Johnson Circuit Court** (41C01) — Johnson County Courthouse,
  5 E. Jefferson Street, Franklin, IN 46131
- **Johnson Superior Courts 1-3** (41D01-D03)
- **Local rules**: LR41 series.

### Monroe County (53) — Bloomington

- **Monroe Circuit Court Divisions 1-10** (53C01-C10) — Monroe is
  unusual: it operates **ten Circuit Court Divisions** rather than
  a Circuit + Superior pair. Civil cases distribute across all
  ten divisions.
- **Local rules**: LR53 series.
- **Notable**: Monroe operates a Civil Settlement Conference
  Program (CSCP) requiring mandatory settlement conference before
  trial.

### Bartholomew County (03) — Columbus

- **Bartholomew Circuit Court** (03C01) — 234 Washington St.,
  Columbus, IN 47201
- **Bartholomew Superior Courts 1-2** (03D01-D02)
- **Local rules**: LR03 series.

### Madison County (48) — Anderson

- **Madison Circuit Court Divisions 1-6** (48C01-C06) — like
  Monroe, Madison runs multiple Circuit Court Divisions.
- **Local rules**: LR48 series.

### Porter County (64) — Valparaiso

- **Porter Circuit Court** (64C01) — 16 Lincolnway, Valparaiso, IN
  46383
- **Porter Superior Courts 1-4** (64D01-D04)
- **Local rules**: LR64 series.

### Clark County (10) — Jeffersonville

- **Clark Circuit Court Divisions 1-4** (10C01-C04)
- **Clark Superior Court** (10D01)
- **Local rules**: LR10 series. Clark uses a unique unified
  Circuit-Court-Divisions model.

### Howard County (34) — Kokomo

- **Howard Circuit Court** (34C01) — 117 N. Main St., Kokomo, IN
  46901
- **Howard Superior Courts 1-4** (34D01-D04)
- **Local rules**: LR34 series.

### LaPorte County (46) — La Porte / Michigan City

- **LaPorte Circuit Court** (46C01)
- **LaPorte Superior Courts 1-4** (46D01-D04) — split between La
  Porte and Michigan City locations
- **Local rules**: LR46 series.

### Delaware County (18) — Muncie

- **Delaware Circuit Court Divisions 1-5** (18C01-C05)
- **Local rules**: LR18 series.

## Long-tail counties — accessing local rules

For counties not in the table above, look up the cause-number
prefix on the Indiana Supreme Court website
(`courts.in.gov/forms-and-publications/court-orders/local-court-
rules`). Every county publishes its local rule set as a single
PDF.

Common features across long-tail counties:

- **Single Circuit Court Judge** in many smaller counties (e.g.,
  Crawford, Switzerland, Ohio, Owen) — the same judge hears
  civil, criminal, probate, and family cases
- **Concurrent Circuit + Superior Court jurisdiction** — pleadings
  may name the Circuit Court if uncertain; the case may be
  transferred under IC 33-29-1-9
- **Mandatory Odyssey e-filing** is now statewide (effective
  June 2018); the only paper filings accepted are pro se filings
  under the Indiana Administrative Rule 16 carve-out

## Statewide directory (all 92 counties)

The full 92-county directory (county code, courts, addresses,
clerk phone, local-rule PDF link) lives in
`references/county-directory.md`. The directory is sorted
alphabetically and includes population, judicial district, and
notable practice quirks.

Indiana counties are grouped into **6 administrative districts**
for Court of Appeals review (Ind. App. Rule 1 — appellate
districts):

- **District 1** (Southeast): includes Marion, Dearborn, Shelby,
  Bartholomew, Johnson, Brown, Monroe
- **District 2** (Northeast): includes Allen, Wells, Adams, Huntington,
  Steuben
- **District 3** (Northwest): includes Lake, Porter, LaPorte,
  Jasper, Newton, Pulaski, Starke
- **District 4** (West Central): includes Tippecanoe, Vermillion,
  Parke, Putnam, Fountain, Clinton, Warren
- **District 5** (East Central): includes Madison, Delaware,
  Henry, Randolph, Hancock, Hamilton, Rush
- **District 6** (Southwest): includes Vanderburgh, Posey,
  Gibson, Knox, Daviess, Martin, Pike

## Composition — which skills layer here

- `in-statewide-format` for T.R. 5(E) / T.R. 10 baseline
- `in-pro-se` for self-represented filing
- `in-discovery` for T.R. 26-37
- `in-deadlines` for T.R. 6 deadline math
- `in-schedule-hearing` for setting hearings (per-county routing
  varies; the county directory has chambers contacts)
- `in-consumer-debt` if the case is a debt-collection action

## References

- `references/county-directory.md` — the 92-county directory
- `references/circuit-vs-superior.md` — the dual-court structure
- `references/appellate-districts.md` — the six App. Court
  districts and venue rules

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against current local rules and case law before filing.
