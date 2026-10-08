---
name: ca-county-courts-codearranger
title: California county superior courts (non-LA / non-SF)
description: Use when drafting or filing in California superior courts other than Los Angeles or San Francisco — Orange, San Diego, Riverside, San Bernardino, Santa Clara, Alameda, Sacramento, Contra Costa, Fresno counties. Triggers include county names plus "Superior Court", "where do I file", "eFiling", "local rules", "civil motion calendar", "tentative ruling", or case venue in those counties. For Los Angeles use `ca-lasc`; for San Francisco use `ca-sfsc`. Layer on `ca-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ca-court-docs/skills/ca-county-courts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: County Courts Directory
  path: references/county-courts-directory.md
- title: Filing And Service
  path: references/filing-and-service.md
---

# California county superior courts (non-LA / non-SF)

Use this skill in addition to `ca-statewide-format` when filing
in any California superior court other than Los Angeles or San
Francisco Superior Courts.

California has 58 counties and 58 superior courts (one per
county, consolidated under the Trial Court Unification Act of
1998). Each court has its own local rules, tentative-ruling
practices, and eFiling systems. The nine courts below account
for the second tier of case volume after Los Angeles and San
Francisco.

## County / venue table — California's most-populous counties (after LA and SF)

| County | Population | Main courthouse / address | Web portal |
|--------|------------|--------------------------|-----------|
| San Diego | ~3.3 M | Hall of Justice, 330 W. Broadway, San Diego 92101 | sdcourt.ca.gov |
| Orange | ~3.2 M | Central Justice Center, 700 Civic Center Dr. W., Santa Ana 92701 | occourts.org |
| Riverside | ~2.4 M | 4100 Main St., Riverside 92501 | riverside.courts.ca.gov |
| San Bernardino | ~2.2 M | 247 W. Third St., San Bernardino 92415 | sb-court.org |
| Santa Clara | ~1.9 M | Old Courthouse, 161 N. First St., San Jose 95113 | scscourt.org |
| Alameda | ~1.7 M | René C. Davidson Courthouse, 1225 Fallon St., Oakland 94612 | alameda.courts.ca.gov |
| Sacramento | ~1.6 M | Gordon D. Schaber Courthouse, 720 9th St., Sacramento 95814 | saccourt.ca.gov |
| Contra Costa | ~1.2 M | A.F. Bray Courthouse, 1020 Ward St., Martinez 94553 | cc-courts.org |
| Fresno | ~1.0 M | B.F. Sisk Federal Building / Hall of Records, 1100 Van Ness Ave., Fresno 93724 | fresnosuperiorcourt.org |

Always verify current addresses and contacts at the court's
website — courthouses move divisions between locations.

## Caption — county variant

The court name line uses "COUNTY OF [NAME]":

```
              IN THE SUPERIOR COURT OF CALIFORNIA
                   COUNTY OF ORANGE
```

Case number formats vary by county (see per-county notes below).

## eFiling systems

Unlike Oregon's uniform statewide File and Serve, California
courts use a **patchwork of eFiling vendors**:

| County | eFiling vendor | Portal |
|--------|---------------|--------|
| San Diego | Tyler (Odyssey eFileCA) | sdcourt.ca.gov/efiling |
| Orange | Tyler (Odyssey eFileCA) | occourts.org/online-services/ |
| Riverside | Tyler (Odyssey eFileCA) | riverside.courts.ca.gov |
| San Bernardino | Tyler (Odyssey eFileCA) via eFileSB | efiling.sb-court.org |
| Santa Clara | Tyler (Odyssey eFileCA) | scscourt.org/online-services/ |
| Alameda | File & ServeXpress | fileandservexpress.com |
| Sacramento | Tyler (Odyssey eFileCA) | saccourt.ca.gov/efiling |
| Contra Costa | Tyler (Odyssey eFileCA) | cc-courts.org |
| Fresno | Tyler (Odyssey eFileCA) | fresnosuperiorcourt.org |

**All** accept PDF only; file-size limits typically 10-25 MB
per document. For self-represented filers: eFiling is generally
voluntary (courts accept paper at the clerk's counter during
business hours), but represented parties in civil cases are
typically required to eFile.

## Tentative rulings

All nine courts below use a **tentative-ruling system** for most
civil law-and-motion matters under Cal. Rules of Court, rule
3.1308(a)(1). The statewide rule: tentatives posted by 2:00-4:00
p.m. the court day before the hearing; contest by calling the
department by 4:00 p.m.; if uncontested, the tentative becomes
the order without a hearing.

**Per-court posting time and contest window** — check the local
rules of each court; the statewide rule 3.1308 sets the floor.

## Per-county notes

### San Diego County Superior Court

- Largest court outside Los Angeles; serves 3.3 million
  residents
- **Main civil courthouse**: Central Courthouse, 1100 Union St.,
  San Diego 92101 (opened 2017; replaced the old Hall of
  Justice civil departments). The Hall of Justice (330 W.
  Broadway) retains criminal and some civil departments
- **Civil Division clerk**: (619) 450-7060
- **eFiling**: Tyler Odyssey eFileCA via
  **https://sdcourt.ca.gov/efiling/**; mandatory for represented
  parties in unlimited civil
- **Case numbers**: `37-YYYY-NNNNNNN-CU-[type]-CTL` (unlimited
  civil, Central); `YYYY-NNNNNN-CL` (limited civil)
- **Tentative rulings**: posted by 1:30 p.m. day before hearing
  at **https://www.sdcourt.ca.gov/tentativerulingsearch/**;
  contest by 4:00 p.m.
- **Local rules**: San Diego Superior Court Local Rules, posted
  at sdcourt.ca.gov — Department rules (standing orders) are
  posted per department
- **ADR**: Mandatory settlement conference before trial;
  voluntary mediation through the court's ADR office

### Orange County Superior Court

- **Main civil courthouse**: Central Justice Center (CJC),
  700 Civic Center Dr. W., Santa Ana 92701
- Other civil locations: North Justice Center (Fullerton),
  West Justice Center (Westminster), Lamoreaux Justice Center
  (Orange), Harbor Justice Center (Newport Beach / Laguna
  Niguel)
- **Civil Division**: (657) 622-5300
- **eFiling**: Tyler Odyssey eFileCA via
  **https://www.occourts.org/online-services/**; mandatory for
  unlimited civil represented parties
- **Case numbers**: `30-YYYY-NNNNNNN-CU-[type]-CJC` (unlimited,
  CJC); branch suffixes for other locations
- **Tentative rulings**: posted by 2:00 p.m. day before at
  **https://www.occourts.org/tentativerulings/**; contest by
  4:00 p.m.
- **Local rules**: OCSC Local Rules at occourts.org/general-info/
- **Complex civil**: Dept. CX at CJC handles complex civil
  cases

### Riverside County Superior Court

- **Main courthouse**: 4100 Main St., Riverside 92501 (Riverside
  Historic Courthouse; newer Civil Complex Center nearby)
- Branch locations: Murrieta (Southwest Justice Center),
  Blythe, Indio (Indio Justice Center), Hemet (Hemet Courthouse)
- **Civil clerk**: (951) 777-3147
- **eFiling**: Tyler Odyssey eFileCA via
  **https://riverside.courts.ca.gov/online-services/efiling/**
- **Tentative rulings**: posted on court website; confirm
  specific department practice for contest deadline
- **Local rules**: Riverside County Superior Court Local Rules
  at riverside.courts.ca.gov
- **Note**: Riverside is geographically large; case filing
  location depends on where the cause of action arose or where
  the defendant resides (Code Civ. Proc., § 395)

### San Bernardino County Superior Court

- **Main courthouse**: 247 W. Third St., San Bernardino 92415
  (Halls of Justice and Civil Courthouse)
- Branch locations: Rancho Cucamonga, Victorville (High Desert),
  Big Bear Lake, Joshua Tree, Barstow
- **Civil clerk**: (909) 708-8678
- **eFiling**: Tyler eFileCA via
  **https://efiling.sb-court.org/**; mandatory for represented
  parties in unlimited civil
- **Case numbers**: `CIVDS` prefix for unlimited civil at the
  main courthouse (e.g., `CIVDS2412345`); branch suffixes
  vary (CIVRS = Rancho Cucamonga; CIVVS = Victorville)
- **Tentative rulings**: posted by 3:00 p.m. day before at
  sb-court.org; check specific department
- **Local rules**: San Bernardino County Superior Court Local
  Rules at sb-court.org/civil/

### Santa Clara County Superior Court

- **Main courthouse**: Old Courthouse, 161 N. First St., San
  Jose 95113 (civil law and motion, probate); also Downtown
  Superior Court, 191 N. First St. (general civil)
- **Civil clerk**: (408) 882-2100
- **eFiling**: Tyler Odyssey eFileCA via
  **https://www.scscourt.org/online-services/efiling/**
- **Case numbers**: `YYYY-CV-NNNNNN` (general civil)
- **Tentative rulings**: posted on scscourt.org; Dept. 1 and
  other civil law-and-motion departments post tentatives by
  2:00 p.m. day before; contest by 4:00 p.m.
- **Local rules**: Santa Clara County Superior Court Local Rules
  at scscourt.org/general-info/local-rules/
- **Complex civil**: Complex Civil Litigation Center, 191 N.
  First St.

### Alameda County Superior Court

- **Main courthouse**: René C. Davidson Courthouse, 1225 Fallon
  St., Oakland 94612 (unlimited civil, probate, family)
- Also: George E. McDonald Hall of Justice (Hayward), 24405
  Amador St., Hayward 94544 (civil); Wiley W. Manuel
  Courthouse (Oakland; criminal and some civil)
- **Civil clerk**: (510) 267-6930 (René C. Davidson)
- **eFiling**: File & ServeXpress — different from most other
  California counties; portal:
  **https://www.fileandservexpress.com/**; account required;
  mandatory for unlimited civil represented parties
- **Case numbers**: `RG` prefix (René C. Davidson, general civil,
  e.g., `RG24123456`); `HG` prefix (Hayward)
- **Tentative rulings**: posted on alameda.courts.ca.gov;
  Dept. 1 (law and motion) posts tentatives by 1:30 p.m. day
  before; contest by 4:00 p.m. to Dept. 1 clerk
- **Local rules**: Alameda County Superior Court Local Rules
  at alameda.courts.ca.gov/rules/
- **ADR**: Alameda has a robust ADR program — early mediation
  is strongly encouraged at the first CMC

### Sacramento County Superior Court

- **Main courthouse**: Gordon D. Schaber Courthouse, 720 9th St.,
  Sacramento 95814 (civil, probate, family)
- Also: William R. Ridgeway Family Relations Courthouse (family
  law); Juvenile Court
- **Civil clerk**: (916) 874-5522
- **eFiling**: Tyler Odyssey eFileCA via
  **https://saccourt.ca.gov/general-info/online-filing.aspx**
- **Case numbers**: `34-YYYY-NNNNNNN-CU` (unlimited civil)
- **Tentative rulings**: posted at saccourt.ca.gov; check
  department-specific practice; most civil departments post
  tentatives by 2:00 p.m. day before
- **Local rules**: Sacramento County Superior Court Local Rules
  at saccourt.ca.gov/local-rules/
- **Note**: Sacramento is the state capital — significant
  administrative-law and state-agency civil filings; the
  Government Claims Act (Gov. Code, § 900 et seq.) and
  Tort Claims Act filings are common here

### Contra Costa County Superior Court

- **Main courthouse**: A.F. Bray Courthouse, 1020 Ward St.,
  Martinez 94553 (unlimited civil, probate)
- Also: Pittsburg (Wakefield Taylor Courthouse), Richmond
  (Richmond Justice Center)
- **Civil clerk**: (925) 608-1000
- **eFiling**: Tyler Odyssey eFileCA via
  **https://www.cc-courts.org/online-services/efiling/**
- **Case numbers**: `C` prefix for civil in Martinez (e.g.,
  `C24-12345`)
- **Tentative rulings**: posted at cc-courts.org; check
  department — Dept. 5 handles law and motion; tentatives
  posted by 2:00 p.m. day before; contest by 4:00 p.m.
- **Local rules**: Contra Costa County Superior Court Local
  Rules at cc-courts.org/general-info/

### Fresno County Superior Court

- **Main courthouse**: B.F. Sisk Federal Building / Hall of
  Records area, 1100 Van Ness Ave., Fresno 93724
- **Civil clerk**: (559) 457-2000
- **eFiling**: Tyler Odyssey eFileCA via
  **https://www.fresnosuperiorcourt.org/e-filing/**
- **Case numbers**: `YYCECG` (general civil, e.g., `24CECG01234`)
- **Tentative rulings**: posted at fresnosuperiorcourt.org;
  check specific department for posting time and contest method
- **Local rules**: Fresno County Superior Court Local Rules at
  fresnosuperiorcourt.org

## Case-number cheat sheet

| County | Unlimited civil prefix | Example |
|--------|----------------------|---------|
| San Diego | `37-YYYY-NNNNNNN-CU-` | `37-2024-00012345-CU-BC-CTL` |
| Orange | `30-YYYY-NNNNNNN-CU-` | `30-2024-01234567-CU-OR-CJC` |
| Riverside | `YYYYCVNNNNNN` | `2024CV00012345` |
| San Bernardino | `CIVDS` / `CIVRS` / `CIVVS` | `CIVDS2412345` |
| Santa Clara | `YYYY-CV-NNNNNN` | `2024-CV-123456` |
| Alameda | `RG` + year + seq. | `RG24123456` |
| Sacramento | `34-YYYY-NNNNNNN-CU` | `34-2024-00012345-CU-OR` |
| Contra Costa | `C` + year + seq. | `C24-012345` |
| Fresno | `YYCECG` + seq. | `24CECG01234` |

Always verify the case number on the court's case portal before
filing — formats can vary within a county by filing location and
case type.

## Statewide civil motion notice requirements

All California superior courts follow Code Civ. Proc., § 1005(b):

- **16 court days' notice** for most civil motions filed in
  unlimited civil
- Add **5 calendar days** if service is by first-class mail
- Add **2 court days** if service is by overnight courier
- **No addition** for electronic or personal service
- **75-day notice** for motions for summary judgment (Code Civ.
  Proc., § 437c(a)); opposition due 14 days before hearing;
  reply due 5 days before

Court days = all days except Saturdays, Sundays, and judicial
holidays listed in Code Civ. Proc., § 135.

## Filing fees — statewide schedule

All California superior courts follow the Government Code fee
schedule (Gov. Code, §§ 70600-70679). Current filing fees:

- Complaint (unlimited civil, first paper): $435 (Gov. Code,
  § 70611)
- Complaint (limited civil, over $10,000): $225
- Answer (first paper): same as complaint — $435 or $225
  (Gov. Code, § 70612)
- Motion (unlimited civil): $60 (Gov. Code, § 70617)
- Summary judgment motion: $500 (Gov. Code, § 70617(e))
- Demurrer: $60

Fee waiver: Cal. Rules of Court, rule 3.50-3.63; Judicial
Council form FW-001.

Fees are adjusted annually; pull current amounts from:
**https://www.courts.ca.gov/forms.htm** (filter "fees") or the
specific court's website.

## Document set (typical for any California county)

1. Notice of Motion and Motion (with date, time, dept., judge,
   and reservation number if applicable)
2. Memorandum of Points and Authorities (may be combined with
   motion or filed separately)
3. Supporting Declaration(s) with exhibits
4. Proposed Order ("[PROPOSED] ORDER" as title)
5. Separate Statement (required for discovery motions — CRC
   3.1345)
6. Proof of Service (POS-030 or declaration of service)

The **timing** of the reservation (before or at filing) and the
**contest deadline** for tentatives varies by county — check the
local rules for the specific court.

## Scheduling tip — confirm department practices

Every California superior court department has its own
preferences and standing orders. Before filing any motion:

1. Check the court's website for the assigned department's
   standing orders
2. Confirm whether the department uses a centralized reservation
   system (like LASC's CRS) or accepts direct calls to the
   clerk's counter
3. Download the department's standing order if posted — many
   judges post preferred format requirements, briefing-schedule
   variations, and courtesy-copy requirements

## References

- `references/county-courts-directory.md` — full directory of
  all 9 counties above: courthouse addresses, web portals,
  civil-division contacts, case-number formats, eFiling systems
- `references/filing-and-service.md` — per-county eFiling
  systems, service rules, fee schedules, and pro se filing
  procedures

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against current rules and case law before filing.
