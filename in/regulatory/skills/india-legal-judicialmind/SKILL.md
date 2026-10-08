---
name: india-legal-judicialmind
title: Indian Legal System
description: Indian law and courts skill for practice in India. Use when the user needs assistance with Indian courts, Indian statutes (IPC, CrPC, CPC), constitutional law, commercial law, or Indian legal procedures. Triggers on keywords like "India", "Indian law", "Supreme Court of India", "High Court", "IPC", "CrPC", "CPC", "Indian Constitution", "NCLT", "arbitration India", "Bombay High Court", "Delhi High Court".
author: judicialmind
author_url: https://github.com/judicialmind/legal-skills/tree/main/skills/india-legal
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: in
practice: regulatory
language: en
sources:
- title: Court Procedures
  path: references/court-procedures.md
- title: Ibc Process
  path: references/ibc-process.md
- title: Writ Practice
  path: references/writ-practice.md
---

# Indian Legal System

This skill provides expert guidance for legal practice in India covering courts, procedures, and substantive law.

## Core Capabilities

### 1. Court System
- Supreme Court of India
- High Courts
- District Courts
- Specialized tribunals

### 2. Civil Practice
- Code of Civil Procedure (CPC)
- Commercial disputes
- Arbitration
- Writ jurisdiction

### 3. Criminal Practice
- Indian Penal Code (IPC)
- Criminal Procedure Code (CrPC)
- Bail and trial procedures
- Appeals

### 4. Specialized Areas
- Constitutional law
- Corporate law
- Intellectual property
- Tax law

## Indian Court Structure

### Court Hierarchy
```
┌─────────────────────────────────────────────────┐
│         SUPREME COURT OF INDIA                   │
│    (Chief Justice + 33 Judges)                  │
│    Original, Appellate, Advisory Jurisdiction   │
│    New Delhi                                    │
└─────────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────┐
│              HIGH COURTS (25)                    │
│    One or more per state/UT                     │
│    Original and Appellate Jurisdiction          │
│    Writ Jurisdiction (Art. 226)                 │
└─────────────────────────────────────────────────┘
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ DISTRICT &   │ │ SESSIONS     │ │ SPECIALIZED  │
│ CIVIL COURTS │ │ COURTS       │ │ TRIBUNALS    │
│ (Civil)      │ │ (Criminal)   │ │ NCLT, ITAT,  │
└──────────────┘ └──────────────┘ │ NGT, SAT     │
                                  └──────────────┘
```

### High Courts
| High Court | Jurisdiction |
|------------|--------------|
| Supreme Court | All India, Delhi (seat) |
| Bombay | Maharashtra, Goa, Dadra & Nagar Haveli |
| Delhi | NCT of Delhi |
| Calcutta | West Bengal, Andaman & Nicobar |
| Madras | Tamil Nadu, Puducherry |
| Karnataka | Karnataka |
| Gujarat | Gujarat |
| Kerala | Kerala, Lakshadweep |
| Punjab & Haryana | Punjab, Haryana, Chandigarh |
| Allahabad | Uttar Pradesh |
| Telangana | Telangana |
| Andhra Pradesh | Andhra Pradesh |
| Rajasthan | Rajasthan |
| Madhya Pradesh | Madhya Pradesh |
| Patna | Bihar |

### Specialized Tribunals
| Tribunal | Jurisdiction |
|----------|--------------|
| NCLT | Company law, insolvency |
| NCLAT | Appeals from NCLT |
| ITAT | Income tax |
| CESTAT | Customs, excise, service tax |
| NGT | Environmental matters |
| SAT | Securities law |
| CAT | Central government service |
| DRT | Debt recovery |
| RERA | Real estate regulation |

## Constitutional Framework

### Fundamental Rights (Part III)
| Article | Right |
|---------|-------|
| 14 | Equality before law |
| 19 | Freedom of speech, assembly, movement, etc. |
| 20 | Protection against ex post facto laws |
| 21 | Right to life and personal liberty |
| 22 | Protection against arrest |
| 25-28 | Religious freedom |
| 29-30 | Cultural and educational rights |
| 32 | Right to constitutional remedies |

### Writ Jurisdiction
| Writ | Purpose | Article |
|------|---------|---------|
| Habeas Corpus | Unlawful detention | 32, 226 |
| Mandamus | Compel public duty | 32, 226 |
| Certiorari | Quash lower court order | 32, 226 |
| Prohibition | Prevent excess jurisdiction | 32, 226 |
| Quo Warranto | Challenge public office | 32, 226 |

### PIL (Public Interest Litigation)
**Relaxed standing requirements**:
- Letter can be treated as petition
- Any public-spirited person
- Issues of public importance
- Protection of fundamental rights

## Civil Procedure (CPC 1908)

### Court Fees and Jurisdiction
| Court | Pecuniary Jurisdiction (Varies by State) |
|-------|------------------------------------------|
| District Court | Typically above ₹20-50 lakhs |
| City Civil Court | Typically ₹3-20 lakhs |
| Small Causes Court | Up to ₹3 lakhs |
| Consumer Forums | Varies by forum level |

### Key CPC Provisions
| Order/Section | Topic |
|---------------|-------|
| Section 9 | Courts to try civil suits |
| Section 20 | Place of suing |
| Order I | Parties to suits |
| Order II | Frame of suit |
| Order VI | Pleadings generally |
| Order VII | Plaint |
| Order VIII | Written statement |
| Order XI | Discovery and inspection |
| Order XVIII | Hearing and examination |
| Order XX | Judgment and decree |
| Order XXXIX | Temporary injunctions |
| Order XLI | Appeals from decrees |

### Limitation Periods (Common)
| Type of Suit | Limitation |
|--------------|------------|
| Contract breach | 3 years |
| Recovery of money | 3 years |
| Specific performance | 3 years |
| Fraud | 3 years from discovery |
| Tort/injury | 1 year |
| Appeal to High Court | 90 days |
| Appeal to Supreme Court | 90 days |

### Commercial Courts
**Threshold**: ₹3 lakhs or above (₹1 crore for High Court original jurisdiction)

**Covered Disputes**:
- Mercantile documents
- Partnership agreements
- Intellectual property
- Infrastructure projects
- Joint ventures
- Shareholders agreements
- Technology agreements

## Criminal Procedure (CrPC 1973)

### Court Jurisdiction
| Court | Trial Jurisdiction |
|-------|-------------------|
| Sessions Court | Cases with imprisonment > 7 years |
| Magistrate First Class | Imprisonment up to 3 years |
| Magistrate Second Class | Imprisonment up to 1 year |
| Executive Magistrate | Preventive actions, maintenance |

### Cognizable vs. Non-Cognizable
| Type | Police Power | Warrant Needed | Bail |
|------|--------------|----------------|------|
| Cognizable | Can arrest without warrant | No | May be non-bailable |
| Non-Cognizable | Cannot arrest without warrant | Yes | Bailable |

### Bail Provisions
| Type | Section | Circumstances |
|------|---------|---------------|
| Regular bail | 437, 439 | During trial |
| Anticipatory bail | 438 | Before arrest |
| Interim bail | 437, 439 | Temporary pending hearing |
| Default bail | 167(2) | Investigation not completed in time |

**Default Bail Time Limits**:
- 60 days: Offenses with imprisonment < 10 years
- 90 days: Offenses with imprisonment ≥ 10 years, death, or life

### FIR and Investigation
```
FIR (Section 154) → Investigation (Chapter XII) →
Charge Sheet (Section 173) → Cognizance (Section 190) →
Charges Framed → Trial → Judgment
```

## Indian Penal Code (IPC 1860)

### Key Offenses
| Section | Offense |
|---------|---------|
| 120B | Criminal conspiracy |
| 302 | Murder |
| 304 | Culpable homicide |
| 376 | Rape |
| 379-382 | Theft |
| 384-389 | Extortion |
| 390-402 | Robbery |
| 403-404 | Criminal misappropriation |
| 405-409 | Criminal breach of trust |
| 415-420 | Cheating |
| 463-477A | Forgery |
| 499-500 | Defamation |
| 503-507 | Criminal intimidation |

### White Collar Crimes
| Offense | Section/Act |
|---------|-------------|
| Cheating | IPC 420 |
| Criminal breach of trust | IPC 406-409 |
| Forgery | IPC 463-465 |
| Money laundering | PMLA |
| Corruption | Prevention of Corruption Act |
| Corporate fraud | Companies Act 2013 |

## Corporate Law

### Companies Act 2013
| Topic | Sections |
|-------|----------|
| Incorporation | 3-22 |
| Directors | 149-172 |
| Meetings | 96-122 |
| Related party transactions | 188 |
| Oppression and mismanagement | 241-246 |
| Winding up | 270-365 |

### NCLT Jurisdiction
- Company law matters
- Insolvency and bankruptcy (IBC)
- Oppression and mismanagement
- Class actions
- Mergers and amalgamations

### Insolvency and Bankruptcy Code (IBC 2016)
**Corporate Insolvency Resolution Process (CIRP)**:
1. Application (Section 7, 9, or 10)
2. Admission and moratorium
3. Appointment of IRP/RP
4. Formation of CoC
5. Resolution plan
6. Approval or liquidation

**Timeline**: 180 days (extendable by 90 days, max 330 days)

## Arbitration (Arbitration and Conciliation Act 1996)

### Key Provisions
| Section | Topic |
|---------|-------|
| 7 | Arbitration agreement |
| 9 | Interim measures (court) |
| 11 | Appointment of arbitrators |
| 17 | Interim measures (tribunal) |
| 34 | Setting aside award |
| 36 | Enforcement of award |

### Institutional Arbitration
- Indian Council of Arbitration (ICA)
- Mumbai Centre for International Arbitration (MCIA)
- Delhi International Arbitration Centre (DIAC)
- Singapore International Arbitration Centre (SIAC) - frequently used for India

### Section 34 Grounds (Setting Aside)
1. Party incapacity
2. Invalid agreement
3. No proper notice
4. Award beyond scope
5. Composition/procedure violation
6. Non-arbitrable subject matter
7. Public policy violation

## Legal Research Resources

### Primary Sources
| Source | Content | URL |
|--------|---------|-----|
| Indian Kanoon | Free case law | indiankanoon.org |
| SCC Online | Comprehensive database | scconline.com |
| Manupatra | Case law, statutes | manupatra.com |
| India Code | Central acts | indiacode.nic.in |
| Supreme Court | Official website | sci.gov.in |

### Citation Format
```
AIR CITATION:
AIR [Year] [Court] [Page]
Example: AIR 2020 SC 1234

SCC CITATION:
([Year]) [Volume] SCC [Page]
Example: (2020) 5 SCC 123

SCALE CITATION:
[Year] [Volume] SCALE [Page]
```

## Integration with Other Skills

- **legal-research**: Indian case law research
- **litigation**: Indian court procedures
- **corporate-ma**: Indian M&A and NCLT
- **international-arbitration**: India-seated arbitration
- **compliance-tracking**: Indian regulatory compliance

## Reference Files

For detailed guidance:
- `references/court-procedures.md` - Indian court filing procedures
- `references/ibc-process.md` - Insolvency process guide
- `references/writ-practice.md` - Constitutional writ procedures
