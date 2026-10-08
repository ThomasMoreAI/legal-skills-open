---
name: conversation-intake-employment-contract-sboghossian
title: Intake — Employment Contract
description: Use when a user wants to draft or review an employment contract and Claude must collect the minimum viable inputs before generating the document. Triggers on any request to create, draft, or prepare an employment agreement, offer letter, or work contract. Covers MENA jurisdictions (UAE onshore, DIFC, KSA, LB, EG) with secondary coverage of FR, UK, and EU. Routes to jurisdiction-specific drafting skills once intake is complete.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/conversation/conversation-intake-employment-contract
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Intake — Employment Contract

## When this applies

Activate whenever a user requests help drafting, preparing, or reviewing an employment contract, offer letter, fixed-term agreement, or any instrument that creates an employer-employee relationship. This skill collects the minimum viable information before routing to the jurisdiction-specific drafting skill. Do not route prematurely — a contract drafted without a confirmed jurisdiction is likely non-compliant.

## Behavior

Conduct a single-turn intake (or two-turn maximum) gathering all six required fields. Where the user has already provided some information in their opening message, extract it silently and ask only for what is still missing.

### Required fields

1. **Jurisdiction of employment** — where the employee will *physically work*, not where the employer is incorporated. This is the single most important input: it determines which labor statute governs, notice-period minima, termination entitlements, and whether a work permit is required.

   | Jurisdiction | Governing statute / framework |
   |---|---|
   | UAE (onshore) | Federal Decree-Law No. 33/2021 on the Regulation of Labour Relations |
   | DIFC | DIFC Employment Law (DIFC Law No. 2/2019, as amended) |
   | ADGM | ADGM Employment Regulations 2019 |
   | KSA | Saudi Labor Law (Royal Decree M/51, 2005, amended to 2022) |
   | Lebanon | Lebanese Labor Law (Law of 1946, as amended) |
   | Egypt | Egyptian Labor Law No. 12/2003 |
   | France | French Labor Code (Code du Travail) |
   | UK | Employment Rights Act 1996; Working Time Regulations 1998 |

2. **Employer entity** — full legal name, commercial registration (CR) number or equivalent, registered address. This goes directly into the contract header and affects statutory employer obligations.

3. **Employee** — full name, nationality, and passport/ID number. Nationality is material in MENA: non-Saudi employees in KSA require an iqama (residence permit) and the contract is typically tied to the kafala sponsorship chain; UAE non-citizen employees require a work permit under the Ministry of Human Resources and Emiratisation (MOHRE).

4. **Role** — job title, reporting line, work location (on-site / remote / hybrid / field-based). Location affects applicable labor law when an employee splits time across borders.

5. **Compensation** — base salary in the relevant currency, allowance structure, bonus formula if any. MENA-specific: UAE and KSA contracts commonly include housing and transport allowances as separate line items. Confirm whether salary is stated gross or net (relevant in FR and LB where income tax withholding applies). Confirm whether MOHRE minimum wage requirements apply (UAE: AED 4,000/month minimum for skilled workers under certain permit categories — verify current threshold).

6. **Term type** — see jurisdiction table below.

### Term-type jurisdiction table

| Jurisdiction | Default | Notes |
|---|---|---|
| UAE onshore | Definite only (post-2021 law) | Maximum 3 years, renewable; indefinite contracts abolished |
| DIFC | Either | Common law; indefinite most common; fixed-term used for project roles |
| ADGM | Either | Common law; same as DIFC |
| KSA — Saudi national | Either | Indefinite convertible after 2 renewals |
| KSA — non-Saudi | Definite | Maximum 5 years; tied to iqama validity |
| Lebanon | Either | No statutory maximum; indefinite presumed unless otherwise specified |
| Egypt | Either | Indefinite after second renewal of definite contracts |
| France | Indefinite (CDI) default | CDD (definite) restricted; maximum 18 months + 1 renewal |
| UK | Either | No maximum; unfair dismissal rights vest at 2 years |

## Optional inputs

Collect these if the user volunteers them or if they are clearly relevant to the role; do not ask for all of them if they slow the intake.

- **Probation period** — statutory limits: UAE 6 months (cannot exceed); KSA 90 days (extendable to 180 by agreement); LB typically 3–6 months; DIFC 6 months. Confirm desired period if the user has a preference.
- **Non-compete / non-solicitation** — scope, duration, geography. Enforceability varies significantly: UAE post-2021 law permits enforceable non-competes up to 2 years in same sector/geography; KSA courts apply narrowly; LB courts routinely void overly broad covenants.
- **IP assignment** — critical for tech or creative roles. Confirm whether the employer wants an express assignment of all work-product IP (standard for software developers; needs explicit clause in civil-law jurisdictions including LB, EG, FR).
- **Equity / stock options** — if applicable, flag that the ESOP documentation is a separate instrument; intake here simply notes it exists.
- **Dependents under sponsorship** — UAE / KSA: if employer is sponsoring dependents (spouse, children), note in contract or ancillary letter; affects termination package because cancelling the work visa triggers dependent visa cancellations.
- **Collective agreement / CBA** — FR, UK: does a sector-level collective agreement apply? It may set higher minimums than the statutory floor.

## Examples

**Good intake opening:**
> "I need to draft an employment contract for a software engineer joining our UAE-based DIFC entity. He's Indian, salary AED 25,000/month, fixed-term 1 year. We want a 3-month probation and non-compete for 1 year post-exit."

Claude silently extracts: jurisdiction = DIFC, employer type = DIFC entity, employee nationality = Indian, salary = AED 25,000, term = fixed-term 1 year, probation = 3 months, non-compete = 1 year. Asks only: "What is the full legal name and DIFC registration number of the employer, and the full name and passport number of the employee?"

**Thin intake opening:**
> "I need an employment contract."

Claude asks all six required fields in a single, numbered message with sensible MENA defaults pre-indicated.

## Edge cases

- **Remote-first / multi-country employee**: if the employee works from a different country than the employer's registered address, surface the risk of an unintended permanent establishment and dual-jurisdiction labor law exposure. Flag and recommend specialist tax advice before proceeding.
- **Secondment**: if the user is seconding an employee between group entities (common in GCC conglomerates), recommend a Secondment Agreement rather than a new employment contract; the original employment relationship typically continues.
- **Contractor misclassification**: if the described role looks like an employment relationship but the user says "contractor", flag the misclassification risk (UAE Federal Decree-Law, KSA Social Insurance obligations) before drafting.

## Do not

- Draft the contract until jurisdiction is confirmed.
- Assume UAE law when the user says "Gulf" or "Middle East" — ask which country.
- Omit the work-permit / iqama dependency flag for non-national employees in KSA and UAE — it is a frequent oversight with material legal consequence.
- Apply US at-will employment concepts to any MENA jurisdiction — termination without cause triggers statutory end-of-service benefits (EOSB) in all GCC states.

## Related skills

- [[draft-employment-contract-lb]]
- [[draft-employment-contract-ksa]]
- [[draft-employment-contract-uae]]
- [[draft-employment-contract-difc]]
- [[kb-labor-law-mena]]
- [[conversation-intake-shareholders-agreement]]
- [[heuristic-statute-of-limitations-flag]]
