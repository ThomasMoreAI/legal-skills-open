---
name: output-citation-mena-conventions-sboghossian
title: Citation Conventions — MENA Jurisdictions
description: Use when citing primary legal sources from MENA jurisdictions — UAE federal decrees, KSA Royal Decrees, Lebanese laws, Egyptian laws, and instruments from the DIFC, ADGM, and QFC — in a jurisdiction-appropriate format. Provides the canonical citation template for each jurisdiction, covering both onshore civil-law and offshore common-law frameworks across the Gulf and Levant.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/output/output-citation-mena-conventions
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: general
language: en
---

# Citation Conventions — MENA Jurisdictions

## Scope

This skill provides the citation format for primary legal sources in each of the key MENA jurisdictions. Use the format appropriate to the jurisdiction of the cited instrument — not the jurisdiction of the lawyer drafting the document.

## UAE

### Federal legislation

UAE federal law is enacted as Federal Decree-Laws (most common for commercial/civil matters post-2021) or older Federal Laws:

```
UAE Federal Decree-Law No. 33 of 2021 on the Regulation of Labour Relations
```

Format: `UAE Federal Decree-Law No. [N] of [year] [title or subject]`

For older pre-2021 legislation:
```
UAE Federal Law No. 2 of 2015 on Commercial Companies
```

For Cabinet Decisions (implementing regulations):
```
UAE Cabinet Decision No. 1 of 2022 Concerning the Executive Regulations of Federal Decree-Law No. 33 of 2021
```

Short-form after first citation:
```
Federal Decree-Law No. 33/2021 (Labour Law)
```
or simply:
```
Labour Law, Art. 10
```

### Emirate-level legislation

Each emirate also enacts its own laws:
```
Dubai Law No. 4 of 2012 Concerning Real Property Registration
```

Format: `[Emirate] Law No. [N] of [year] [title]`

### Regulations

```
SCA Board Resolution No. [N] of [year] (UAE Securities and Commodities Authority)
```

## KSA (Saudi Arabia)

Saudi laws are enacted by Royal Decree:

```
KSA Royal Decree No. M/34 of 1433H (2012G) on Commercial Court Procedures
```

Format: `KSA Royal Decree No. M/[N]` — the `M/` prefix indicates a ministerial Royal Decree; `A/` indicates Royal Decree on governmental matters.

Note: KSA official documents use Hijri (Islamic) calendar dates (H) alongside Gregorian dates (G). Always include both when citing a Royal Decree.

Short-form:
```
Royal Decree No. M/34 (Commercial Court Procedures Law), Art. 12
```

For implementing regulations approved by a Council of Ministers Resolution:
```
KSA Council of Ministers Resolution No. [N] of [year H/G], approving [name of regulation]
```

## Lebanon

Lebanese legislation:
```
Lebanese Law No. 528 of 29 July 2003 on Financial Leasing
```

Format: `Lebanese Law No. [N] of [date] [title]`

Lebanese laws in Arabic may be cited by their date in the Official Gazette:
```
Loi n° 528 du 29 juillet 2003 relative au crédit-bail (J.O. n° 31, 7 août 2003)
```

For legislative decrees (mراسيم اشتراعية):
```
Lebanese Legislative Decree No. 67/1983
```

## Egypt

Egyptian laws:
```
Egyptian Law No. 72 of 2017 on the Capital Market
```

Format: `Egyptian Law No. [N] of [year] [title or subject]`

For Ministerial Decrees:
```
Egyptian Ministerial Decree No. [N] of [year]
```

## DIFC (Dubai International Financial Centre)

DIFC legislation uses a numbered system with the year:
```
DIFC Law No. 2 of 2019 (DIFC Contract Law 2019)
```

Short-form:
```
DIFC Contract Law 2019, Art. 12
```

DIFC Court judgments are cited using their neutral citation:
```
[2023] DIFC CA 001
```

DIFC regulations (non-law-level instruments):
```
DFSA Rule No. [N]/[year]
```

## ADGM (Abu Dhabi Global Market)

ADGM laws:
```
ADGM Companies Regulations 2020
```

ADGM Court judgments:
```
[2023] ADGMCFI 0001
```

## QFC (Qatar Financial Centre)

QFC legislation:
```
QFC Law No. [N] of [year]
```
Example:
```
QFC Law No. 7 of 2005 (QFC Law)
```

## OHADA (Organisation pour l'Harmonisation en Afrique du Droit des Affaires)

For jurisdictions in francophone West/Central Africa where OHADA applies (not core MENA, but referenced in cross-border transactions):
```
OHADA Acte uniforme relatif au droit commercial général (AUDCG), adopté le 15 décembre 2010
```

Short-form:
```
AUDCG, art. 5
```

## Cross-jurisdiction citation table

| Jurisdiction | Legislative citation template | Short-form |
|---|---|---|
| UAE federal | UAE Federal Decree-Law No. N of YYYY | FDL N/YYYY, Art. X |
| UAE emirate | [Emirate] Law No. N of YYYY | Dubai Law N/YYYY, Art. X |
| KSA | KSA Royal Decree No. M/N of YYYYH (YYYYG) | RD M/N, Art. X |
| Lebanon | Lebanese Law No. N of [date] | Law N/YYYY, Art. X |
| Egypt | Egyptian Law No. N of YYYY | Law N/YYYY, Art. X |
| DIFC | DIFC Law No. N of YYYY | DIFC [Short Title] YYYY, Art. X |
| ADGM | ADGM [Name] Regulations YYYY | ADGM [Short Title], reg. X |
| QFC | QFC Law No. N of YYYY | QFC Law N/YYYY, Art. X |

## Caveats and currency

- UAE law is in a period of rapid reform. Federal Laws enacted before 2021 may have been superseded by Federal Decree-Laws. Always verify the current version on the UAE government legal database (https://uaelegislation.gov.ae) before citing.
- KSA Hijri dates: the H-to-G conversion is approximate (±1 year depending on the Islamic month). When the Gregorian date matters (e.g., for calculating a statutory deadline), verify the exact date.
- Use [[research-regulation-lookup]] to retrieve the current canonical version of any MENA instrument before citing it in a formal document.

## Related skills

- [[output-citation-format-bluebook]] — US citations
- [[output-citation-format-oscola]] — UK/DIFC/ADGM case law and statute citations
- [[output-citation-format-civil-law-fr]] — Lebanese/francophone civil-law citations
- [[research-regulation-lookup]] — for retrieving and verifying MENA statutory text
