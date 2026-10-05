---
name: uk-commonwealth-judicialmind
title: UK & Commonwealth Law
description: UK and Commonwealth law skill for English law and common law jurisdictions. Use when the user needs assistance with English courts, UK legal procedures, EU law, common law principles, or Commonwealth legal systems. Triggers on keywords like "UK", "England", "English law", "High Court UK", "Supreme Court UK", "common law", "EU law", "solicitor", "barrister", "Crown Court", "Commonwealth".
author: judicialmind
author_url: https://github.com/judicialmind/legal-skills/tree/main/skills/uk-commonwealth
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: general
language: en
sources:
- title: Commercial Court
  path: references/commercial-court.md
- title: Cpr Guide
  path: references/cpr-guide.md
- title: Retained Eu Law
  path: references/retained-eu-law.md
---

# UK & Commonwealth Law

This skill provides expert guidance for legal practice in the United Kingdom and Commonwealth jurisdictions.

## Core Capabilities

### 1. English Legal System
- Court structure
- Civil procedure
- Criminal procedure
- Regulatory frameworks

### 2. Common Law Principles
- Precedent doctrine
- Equity principles
- Contract and tort
- Statutory interpretation

### 3. Commercial Practice
- Corporate transactions
- Financial services
- International trade
- Dispute resolution

### 4. EU Law Legacy
- Retained EU law
- Brexit implications
- Cross-border matters
- Regulatory divergence

## UK Court Structure

### England and Wales Courts
```
┌─────────────────────────────────────────────────┐
│           UK SUPREME COURT                       │
│    (Final appellate court for UK)               │
│    12 Justices                                  │
└─────────────────────────────────────────────────┘
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
┌─────────────────┐       ┌─────────────────┐
│ COURT OF APPEAL │       │ COURT OF APPEAL │
│ (Civil Division)│       │(Criminal Div)   │
└─────────────────┘       └─────────────────┘
        │                           │
        ▼                           ▼
┌─────────────────┐       ┌─────────────────┐
│   HIGH COURT    │       │   CROWN COURT   │
│ • Queen's Bench │       │ (Serious crimes)│
│ • Chancery      │       └─────────────────┘
│ • Family        │                 │
└─────────────────┘                 │
        │                           │
        ▼                           ▼
┌─────────────────┐       ┌─────────────────┐
│ COUNTY COURT    │       │ MAGISTRATES'    │
│ (Civil claims)  │       │ COURT           │
└─────────────────┘       │ (Summary crimes)│
                          └─────────────────┘
```

### High Court Divisions
| Division | Jurisdiction |
|----------|--------------|
| Queen's Bench | Contract, tort, commercial, judicial review |
| Chancery | Equity, trusts, companies, IP, insolvency |
| Family | Matrimonial, children, probate |

### Specialist Courts
| Court | Jurisdiction |
|-------|--------------|
| Commercial Court | High-value commercial disputes |
| Technology & Construction Court | Construction, technology, engineering |
| Admiralty Court | Shipping, maritime |
| Patents Court | Patent matters |
| Companies Court | Company matters, insolvency |
| Business and Property Courts | Commercial litigation hub |

### Scotland Court System
```
SUPREME COURT (UK appeals)
        │
COURT OF SESSION (civil) / HIGH COURT OF JUSTICIARY (criminal)
        │
SHERIFF COURTS
        │
JUSTICE OF THE PEACE COURTS
```

## Civil Procedure Rules (CPR)

### Key CPR Parts
| Part | Topic |
|------|-------|
| Part 1 | Overriding objective |
| Part 3 | Case management |
| Part 7 | Claims procedure |
| Part 8 | Alternative procedure |
| Part 16 | Statements of case |
| Part 18 | Further information |
| Part 20 | Counterclaims, third parties |
| Part 23 | Applications |
| Part 24 | Summary judgment |
| Part 25 | Interim remedies |
| Part 31 | Disclosure |
| Part 32 | Evidence |
| Part 35 | Experts |
| Part 36 | Offers to settle |
| Part 44 | Costs |

### Overriding Objective (CPR 1.1)
**Dealing with cases justly and at proportionate cost**:
- Ensuring parties on equal footing
- Saving expense
- Dealing with case proportionately
- Ensuring expeditious handling
- Allocating appropriate court resources
- Enforcing compliance

### Claim Tracks
| Track | Value | Features |
|-------|-------|----------|
| Small Claims | Up to £10,000 | Simple procedure, limited costs |
| Fast Track | £10,000-£25,000 | Standard disclosure, 30-week timetable |
| Multi-Track | Over £25,000 | Case management, tailored directions |

### Pre-Action Protocols
**Purpose**: Encourage settlement, narrow issues, promote ADR

**Common Protocols**:
- Professional negligence
- Construction and engineering
- Disease and illness
- Personal injury
- Judicial review
- Clinical disputes

### Limitation Periods
| Claim Type | Period |
|------------|--------|
| Contract | 6 years |
| Deed | 12 years |
| Tort | 6 years |
| Personal injury | 3 years |
| Defamation | 1 year |
| Judicial review | 3 months (promptly) |
| Land recovery | 12 years |

## Commercial Litigation

### Commercial Court Guide
**Characteristics**:
- High-value/complex commercial disputes
- Specialist judges
- Active case management
- Flexible procedures
- International parties common

**Claim Form (N1)**:
1. Details of claim
2. Statement of value
3. Court fee
4. Service requirements

### Disclosure
**Standard Disclosure** (CPR 31.6):
- Documents on which party relies
- Documents adversely affecting own case
- Documents adversely affecting other party's case
- Documents supporting other party's case

**Disclosure Review Document**:
- Scope of search
- Electronic documents
- Keyword searches
- Date ranges
- Custodians

### Without Prejudice & Part 36

**Without Prejudice**:
- Settlement negotiations protected
- Cannot be disclosed to court
- Exceptions: to show agreement, explain delay, estoppel

**Part 36 Offers**:
- Formal settlement offer
- Cost consequences if not beaten at trial
- Claimant offer not beaten: Interest + indemnity costs
- Defendant offer not beaten: Costs from date of offer

## Criminal Procedure

### Classification of Offenses
| Category | Trial Venue | Examples |
|----------|-------------|----------|
| Summary | Magistrates' only | Minor offenses |
| Either way | Magistrates' or Crown Court | Theft, ABH |
| Indictable only | Crown Court only | Murder, rape, robbery |

### Criminal Procedure Rules
- Case management
- Disclosure obligations
- Evidence requirements
- Sentencing procedures

### Crown Prosecution Service
**Tests for Prosecution**:
1. **Evidential**: Realistic prospect of conviction
2. **Public Interest**: Prosecution in public interest

## Company Law (Companies Act 2006)

### Key Provisions
| Section | Topic |
|---------|-------|
| Part 3 | Company formation |
| Part 10 | Directors |
| Part 11 | Derivative claims |
| Part 13 | Resolutions and meetings |
| Part 21 | Certification and transfer |
| Part 22 | Confirmation statements |
| Part 25 | Charges |
| Part 26-26A | Arrangements and reconstructions |
| Part 30 | Unfair prejudice |

### Directors' Duties (Codified)
1. Act within powers (s.171)
2. Promote success of company (s.172)
3. Exercise independent judgment (s.173)
4. Exercise reasonable care, skill, diligence (s.174)
5. Avoid conflicts (s.175)
6. Not accept third-party benefits (s.176)
7. Declare interest in transactions (s.177)

### Unfair Prejudice (s.994)
**Grounds**: Conduct of company's affairs in manner unfairly prejudicial

**Remedies**:
- Share purchase order
- Regulation of company's affairs
- Authorization of proceedings

## Financial Services Regulation

### Regulatory Bodies
| Regulator | Role |
|-----------|------|
| FCA | Conduct regulation, markets |
| PRA | Prudential regulation (banks, insurers) |
| Bank of England | Monetary policy, financial stability |

### FSMA Framework
- Authorization requirements
- Approved persons regime (now SM&CR)
- Market abuse regulation
- Listing rules

### Senior Managers & Certification Regime (SM&CR)
- Senior manager functions
- Certification regime
- Conduct rules
- Individual accountability

## Arbitration

### Arbitration Act 1996
| Section | Topic |
|---------|-------|
| 1 | General principles |
| 9 | Stay of legal proceedings |
| 12 | Power of court to extend time |
| 24 | Power to remove arbitrator |
| 33 | General duty of tribunal |
| 44 | Court powers exercisable in support |
| 67 | Challenge: substantive jurisdiction |
| 68 | Challenge: serious irregularity |
| 69 | Appeal on point of law |

### London Arbitration Institutions
- LCIA (London Court of International Arbitration)
- ICC (International Chamber of Commerce) - London seat
- LMAA (London Maritime Arbitrators Association)
- GAFTA (Grain and Feed Trade Association)

### English Arbitration Advantages
- Pro-arbitration courts
- Limited appeal grounds
- New York Convention enforcement
- Experienced practitioners
- Neutrality

## Brexit and Retained EU Law

### Retained EU Law
- EU regulations became UK law
- EU directives as implemented
- EU-derived domestic legislation
- ECJ case law (pre-2020)

### Key Changes
| Area | Change |
|------|--------|
| Jurisdiction | Brussels Recast replaced by Hague/common law |
| Recognition | EU judgments require fresh proceedings |
| Service | Bilateral arrangements |
| Choice of law | Rome I/II retained |
| Regulatory | Divergence in progress |

## Commonwealth Jurisdictions

### Common Law Family
Jurisdictions following English common law tradition:
- Australia
- Canada (except Quebec)
- New Zealand
- Singapore
- Hong Kong
- Malaysia
- India
- Nigeria
- Kenya

### Persuasive Authority
- Commonwealth decisions persuasive, not binding
- Privy Council decisions (where applicable)
- Similar statutory frameworks
- Shared legal heritage

## Legal Research Resources

| Source | Content |
|--------|---------|
| BAILII | Free UK case law |
| Westlaw UK | Comprehensive database |
| LexisNexis UK | Case law, legislation |
| Practical Law | Transaction guides |
| legislation.gov.uk | UK statutes |

### Citation Format
```
NEUTRAL CITATION (preferred):
[Year] Court Number
Example: [2023] UKSC 15

LAW REPORTS:
[Year] Volume Report Page
Example: [2023] 1 AC 123

WEEKLY LAW REPORTS:
[Year] Volume WLR Page
Example: [2023] 3 WLR 456
```

## Integration with Other Skills

- **international-arbitration**: London arbitration
- **corporate-ma**: UK transactions
- **banking-finance**: UK financial regulation
- **intellectual-property**: UK IP law
- **legal-research**: UK case law

## Reference Files

For detailed guidance:
- `references/cpr-guide.md` - Civil procedure reference
- `references/commercial-court.md` - Commercial Court procedures
- `references/retained-eu-law.md` - Brexit legal changes
