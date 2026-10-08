---
name: prompt-pack-cross-border-employment-comparison-sboghossian
title: Cross-Border Employment Comparison
description: Use when a company needs to compare employment law requirements across multiple jurisdictions for hiring remote or locally-based employees — covering minimum employment terms, statutory benefits, notice periods, termination protections, data privacy obligations, and employer of record (EOR) considerations. Specialised for MENA comparisons (UAE, KSA, LB, EG, Qatar, Bahrain, Oman) alongside GCC, EU, and UK contexts.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-cross-border-employment-comparison
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: employment
language: en
---

# Cross-Border Employment Comparison

Cross-border employment decisions — whether to hire directly, use an employer of record, or engage as a contractor — turn on jurisdiction-specific labor law, social insurance, and tax rules that vary enormously across MENA, GCC, Europe, and beyond. A comparison memo is the essential starting point before a company commits to a hiring model in an unfamiliar jurisdiction.

## When to use this

- A company is expanding headcount into a new country and needs to understand the regulatory obligations before the first hire.
- An HR or legal team is comparing the cost and risk of direct employment versus an employer-of-record model across multiple jurisdictions.
- A company is moving an employee from one MENA jurisdiction to another (intra-group transfer) and needs to understand what changes.
- A company is considering a remote-work policy that allows employees to work from countries where the company has no entity.
- Post-M&A integration: the acquiring company needs to understand the employment terms it has inherited across multiple jurisdictions.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Jurisdictions to compare | The comparison is meaningless without specific jurisdictions | Ask the user to list all relevant countries |
| Role type (executive / professional / manual worker) | Some protections differ by employee category | Ask the user |
| Proposed employment model (direct hire / EOR / contractor) | Determines applicable legal framework | Ask the user |
| Whether the employee will be resident in the country of employment | Residency affects social insurance and visa/work permit obligations | Ask the user |
| Number of employees planned per jurisdiction | Some obligations (mass redundancy, works council) are triggered by headcount thresholds | Ask the user |

## Optional inputs

- Specific clauses of concern (non-compete, IP, probation period).
- Whether TUPE-equivalent rules apply to any transfer.
- Whether the company wants an employer-of-record recommendation or only a comparison.
- Language of employment contracts required.

## Comparison methodology

### Structure the output as a comparison table

One column per jurisdiction; rows are the comparison parameters. Below are the standard parameters; expand or contract based on the user's focus.

| Parameter | UAE (onshore) | UAE (DIFC) | KSA | Lebanon | Egypt | [Other jurisdiction] |
|---|---|---|---|---|---|---|
| Governing law | Federal Labor Law (Decree-Law No. 33 of 2021) | DIFC Employment Law No. 2 of 2019 | Labor Law (Royal Decree M/51, 2005 as amended) | Labor Code (Decree No. 7946 of 1967) | Labor Law (Law No. 12 of 2003) | [Applicable law] |
| Employment contract required | Yes; written; Arabic version binds | Yes; written in English | Yes; written; Arabic required | Yes; written | Yes; written; Arabic required | — |
| Probation period (max) | 6 months | 6 months | 3 months (extendable to 6 for certain roles) | 3 months | 3 months | — |
| Work permits / sponsorship | UAE Golden Visa, Green Visa, or employer-sponsored; MOHRE registration | DIFC visa; DIFC Authority registration | Iqama (residence permit) sponsored by employer; tied to employer | Work permit through Ministry of Labor; Lebanese nationality rules | Work permit through Ministry of Manpower | — |
| Minimum wage | No general minimum (sector-specific minimums exist) | No general minimum | SAR 4,000/month for Saudis; no minimum for expatriates | LBP-denominated; effectively nominal given currency collapse | EGP 3,500/month (2024; adjusted periodically) | — |
| Normal working hours | 8 hours/day, 48 hours/week; reduced during Ramadan | 8 hours/day, 48 hours/week | 8 hours/day, 48 hours/week; 6 hours/day during Ramadan | 48 hours/week | 48 hours/week | — |
| Annual leave (minimum) | 30 calendar days after 1 year | 20 working days | 21 days (increasing with tenure) | 15 working days (increasing with tenure) | 21 days (increasing with tenure) | — |
| Public holidays | ~15 days/year; specific to UAE calendar | Same as UAE | ~15 days/year; variable based on lunar calendar | ~15 days/year | ~14 days/year | — |
| Notice period (termination by either party) | 30 days (may be up to 90 days by contract) | 30–90 days depending on service length | 60 days for indefinite contracts | 1–3 months depending on seniority | 2 months standard | — |
| End-of-service gratuity (ESG) | Yes; mandatory; 21 days/year for first 5 years, 30 days/year thereafter; calculated on basic salary | Yes; equivalent statutory ESG | Yes; half month per year for first 5 years; 1 month/year thereafter | Yes; 1 month per year (up to 12 months maximum under Labor Code); complex calculation | Yes; 1 month per year of service | — |
| Termination protection | Cannot terminate without valid reason; arbitrary dismissal entitles employee to compensation | Employment at will with notice or payment in lieu | Cannot terminate without valid reason; arbitrary dismissal triggers double ESG + notice payment | Cannot terminate without justification; court may award reinstatement or compensation | Cannot terminate without valid reason; labor courts may award reinstatement | — |
| Social insurance / contributions | GPSSA for UAE nationals; no contributions for expatriates | DIFC DEWS scheme (mandatory for new hires; transitional) | GOSI for Saudi nationals (10% employer + 10% employee); no GOSI for expatriates | NSSF (National Social Security Fund) for Lebanese nationals and certain foreigners | Social insurance for Egyptian nationals; different rates for expatriates | — |
| Non-compete enforceability | Enforceable if reasonable (max 2 years, scope limited); UAE Labor Law Art. 12 | Enforceable as restraint of trade; courts apply reasonableness test | Enforceable if reasonable | Enforceable if reasonable and with consideration | Enforceable; courts may reduce | — |
| IP / work product ownership | Assignment must be express; employer owns work done in course of employment under Labor Law | Assignment should be express in contract; employer owns work in course of employment | Civil code and IP law apply; express assignment recommended | Lebanese IP Law; express assignment recommended | Egyptian IP Law; work done in employment belongs to employer but formal assignment is safer | — |
| Data privacy obligations for employees | UAE PDPL applies; employee data is personal data | DIFC DP Law 2020 applies | Saudi PDPL applies | No comprehensive law in force; GDPR-alignment recommended | Egyptian DP Law No. 151 of 2020 applies | — |
| Employer of record availability | EOR providers widely available; registration with MOHRE required | Separate DIFC registration required; most EORs do not cover DIFC separately | EOR available for expatriates; Saudization obligations must be met | EOR available but compliance environment complex | EOR available | — |
| Saudization / Emiratization | Emiratization quotas apply to certain sectors (banking, insurance, retail, food) | No Emiratization quota in DIFC; UAE Golden Visa may affect planning | Nitaqat system mandates Saudi workforce percentage by sector and company size | No equivalent | No equivalent | — |

### Narrative analysis for key jurisdictions

After the table, provide a short narrative paragraph for each jurisdiction highlighting:
1. The most important practical risk for the company's specific hiring scenario.
2. The recommended employment model (direct hire / EOR / contractor) with brief reasoning.
3. Any jurisdiction-specific traps for the company's industry or employee type.

## Key MENA-specific issues

**End-of-service gratuity (ESG):** Every GCC country and Lebanon mandates ESG. This is a material cash liability that accrues from day one. Companies frequently underestimate ESG exposure in financial projections. Distinguish between ESG accruing on basic salary (UAE, KSA) and total salary (some interpretations in LB).

**Sponsorship / work permit dependency:** In UAE (onshore) and KSA, the employee's right to remain in the country is tied to employment with a specific employer. Termination triggers an obligation to cancel the work permit and can force the employee to leave. This creates power imbalances that employment contracts and HR policies must address carefully.

**Saudization (Nitaqat) / Emiratization:** These quotas apply sector-by-sector and penalise companies that fall below the mandated percentage of nationals. A company hiring aggressively in KSA or UAE banking/insurance/retail must plan for Nitaqat/Emiratization from the outset.

**Lebanese Labor Code peculiarities:** The Lebanese Labor Code predates the GCC frameworks by several decades and has significant gaps. Courts have applied judge-made principles (heavily influenced by French labor law) to fill gaps. The economic collapse since 2019 has created issues with LBP-denominated minimum wages and ESG calculations; USD-denominated employment contracts are now prevalent.

**Egypt:** Egyptian Labor Courts are available to all employees including foreigners; proceedings can extend 3–5 years; monetary awards are in EGP (currency risk if the employee is paid in USD).

## Common mistakes

- Treating "Gulf countries" as uniform — UAE and KSA have materially different labor rules; Bahrain, Qatar, and Oman have their own frameworks.
- Ignoring ESG accrual when modeling the cost of a MENA headcount addition.
- Assuming a contractor arrangement avoids labor law — MENA courts apply substance-over-form tests; a consultant who works exclusively for one company on a long-term basis will be treated as an employee.
- Hiring into a jurisdiction via a foreign payroll without a local entity or EOR — this creates unlicensed employer exposure.
- Not obtaining work permits before the employee starts work — working without a permit exposes both the employee and the employer to fines and deportation risk.

## Related skills

- [[prompt-pack-employment-contract]]
- [[prompt-pack-consulting-agreement]]
- [[prompt-pack-cross-border-data-transfer-assessment]]
- [[prompt-pack-termination-letter]]
- [[prompt-pack-employees-transfer-tupe]]
