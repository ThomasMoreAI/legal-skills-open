---
name: kb-employment-law-ksa-sboghossian
title: Knowledge Pack — KSA Labor Law
description: Use when a matter involves employment law obligations, contracts, termination, end-of-service award calculation, Saudization (Nitaqat), or HR compliance for entities operating in Saudi Arabia. Covers the KSA Labor Law (Royal Decree M/51), GOSI social insurance, Saudization quotas, notice periods, Article 80/84 termination, non-compete provisions, and the Qiwa/Mudad compliance platforms. Triggers on KSA employment contract, end-of-service gratuity KSA, Nitaqat, GOSI, Qiwa, KSA dismissal, or Saudi labor law questions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/kb/kb-employment-law-ksa
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: sa
practice: employment
language: en
---

# Knowledge Pack — KSA Labor Law

## Primary Sources

- **Labor Law** — Royal Decree M/51 dated 23/8/1426H (September 2005), as amended by Royal Decrees in 2015 and 2019.
- **Ministerial decisions and HRSD circulars** — Ministry of Human Resources and Social Development issues implementing guidance.
- **GOSI (General Organization for Social Insurance)** — social insurance contributions and regulations.
- **Qiwa platform** — electronic labor-relations system for contract registration, mobility, and grievances.
- **Mudad** — Wage Protection System (WPS) compliance platform.

All onshore employment relationships in KSA are governed exclusively by the KSA Labor Law. DIFC-style free-zone exemptions do not exist in KSA; all employers (including those in special economic zones) follow KSA Labor Law unless specifically exempted by a zone-specific decree.

## Working Hours

| Category | Standard |
|---|---|
| General | 8 hours/day, 48 hours/week |
| Ramadan (Muslim workers) | 6 hours/day, 36 hours/week |
| Overtime premium | 50% of hourly wage (additional on base; must be agreed in advance) |
| Weekly rest | Friday as minimum rest day; employer may substitute another day |

Night work and hazardous work attract additional protections per HRSD regulations.

## Probation

- Maximum **90 days** (extendable to **180 days** with mutual written consent before the 90-day period expires).
- Either party may terminate during probation without notice or end-of-service award.
- Probation time counts toward continuous service once passed.

## Contract Types

| Type | Default Applicability |
|---|---|
| **Definite term** | Default for non-Saudi nationals (max initial term 5 years; renewable). 2023 reforms: auto-renews to same terms if both parties continue without new agreement |
| **Indefinite** | Default for Saudi nationals; non-Saudis eligible if specific conditions met |

- Employment contract must be in Arabic or bilingual (Arabic controls in dispute).
- Must be registered on **Qiwa platform** within 30 days.

## Annual Leave (Art 109)

| Service Duration | Annual Leave Entitlement |
|---|---|
| Less than 5 years | 21 days paid leave |
| 5 years or more | 30 days paid leave |

- Employees are entitled to Eid Al-Fitr, Eid Al-Adha, and National Day public holidays in addition.
- Leave must be taken within the year or carried forward with employer consent; payment in lieu on termination.

## Sick Leave

- Maximum **120 days** per year:
  - First 30 days: full pay
  - Next 60 days: half pay
  - Remaining 30 days: unpaid

## Notice Periods (Art 76)

- **Indefinite contracts paid monthly**: minimum **60 days** notice by either party.
- Other arrangements (e.g., weekly/daily workers): proportionate notice per Article.
- Employer may pay wages in lieu of notice.
- Notice period runs from service of written notice.

## End-of-Service Award (Arts 84–85)

The end-of-service award is a mandatory entitlement based on years of service and the reason for departure:

### Calculation

| Service Period | Accrual Rate |
|---|---|
| First 5 years | Half-month salary per year |
| After 5 years | Full month salary per year |

**Salary base**: last wage paid (basic salary + regular allowances; excludes non-regular items).

### Entitlement by departure reason

| Reason | Award |
|---|---|
| Termination by employer (without just cause) | Full award |
| End of definite-term contract by employer | Full award |
| Resignation (< 2 years service) | **Forfeited** |
| Resignation (2–5 years service) | 1/3 of full award |
| Resignation (5–10 years service) | 2/3 of full award |
| Resignation (10+ years service) | Full award |
| Termination for cause (Art 80) | Employer may argue forfeiture; court decides on facts |

### GOSI interaction

GOSI contributions may partially replace end-of-service costs for Saudi nationals — employers registered with GOSI pay monthly contributions; GOSI benefits supplement the statutory award on separation.

## Termination for Cause Without Compensation (Art 80)

Employer may terminate without notice or end-of-service award if:

1. Employee assumes a **false identity or forged qualifications** to obtain employment.
2. Employee commits an **error causing major financial loss** to the employer (employer must notify HRSD within 3 days of discovery).
3. Employee **violates safety instructions** after written warning.
4. Employee **assaults** or threatens employer, supervisor, or co-workers.
5. Employee fails in **essential duties** and fails to rectify after written notice and investigation.
6. Employee **reveals trade secrets** or engages in competing business.
7. Employee **absent 30 days per year or 15 consecutive days** without justification (written warnings required first).
8. Employee convicted of an **honor crime or dishonesty** offense.

Procedural requirement: employer should conduct investigation and provide opportunity to respond before dismissing under Art 80.

## Saudization (Nitaqat)

The **Nitaqat** program requires private-sector employers to maintain a minimum percentage of Saudi national employees, varying by:
- **Industry category** (construction has lower targets; services/professional sectors higher)
- **Employer size tier** (small / medium / large / giant)

| Compliance tier | Color | Consequence |
|---|---|---|
| Excellent/Platinum | Green+ | Access to all government services + visa quota bonuses |
| Satisfactory | Green | Normal services |
| Medium | Yellow | Restricted visa services |
| Non-compliant | Red | Suspended visa quotas + loss of government services |

Employers must monitor Saudization ratio through **Qiwa** and **HRSD portals**. Sector-specific Vision 2030 targets are being raised annually.

## Sponsorship and Worker Mobility (2021+ Reforms)

- The traditional **kafala (sponsorship)** system has been partially reformed:
  - Workers under Qiwa can **change jobs without employer consent** after 1 year of service (subject to conditions and not applicable to all categories).
  - **Exit and re-entry permits** no longer require employer approval for most workers.
  - **Exit without return** no longer requires employer approval.
- Employer remains the **visa sponsor** for GDRFA/Iqama purposes.
- Transfer of Iqama to new employer processed via Qiwa platform.
- Domestic workers and certain categories excluded from reformed mobility rules.

## Non-Compete (Art 83)

- Enforceable for up to **2 years** post-termination.
- Scope must be **reasonable in geography, duration, and type of work**.
- Employee must have had access to trade secrets, clients, or confidential information.
- Courts apply the proportionality test; excessively broad clauses may be reduced to reasonable scope.

## Social Insurance: GOSI

| Contribution | Saudi Nationals | Non-Saudis |
|---|---|---|
| Occupational Hazards | 2% (employer) | 2% (employer) |
| Annuities | 9% (employer) + 9% (employee) | Not applicable |
| Unemployment (SANED) | 1% (employer) + 1% (employee) | Not applicable |

- Registration with GOSI mandatory within first month of employment.
- Failure to register attracts penalties and back-contributions.

## Compliance Platforms

| Platform | Function |
|---|---|
| **Qiwa** | Contract registration; labor mobility; dispute filing; Nitaqat tracking |
| **Mudad** (WPS) | Wage Protection System — mandatory payroll via approved banks |
| **GOSI portal** | Social insurance registration + monthly contribution payment |
| **HRSD** | Ministry portal — employer registration, permits, grievances |

## Wage Protection System (WPS / Mudad)

- All private-sector employers must pay wages electronically through Mudad-registered banks.
- Payment must be made within the first of every month (or contractual date, if earlier).
- Delays of more than 30 days trigger HRSD penalties including suspension of visa issuance and labor permits.

## Practical Drafting Notes

- Employment contracts must be in **Arabic** (or bilingual with Arabic controlling).
- Non-compete and confidentiality clauses: add separately as appendices; courts are more willing to enforce well-scoped written covenants.
- Severance calculations: always compute on **gross last wage**, being careful to include regular allowances.
- Domestic workers are covered by a **separate domestic worker law** — different rules apply.
- Female employees: protected from dismissal during maternity leave (90-day paid maternity leave under Labor Law as amended).

## Caveats & Currency

KSA Labor Law amendments continue under Vision 2030 labor-market reforms. Saudization percentages and Qiwa platform procedures are updated regularly by HRSD. The 2021 worker mobility reforms are implemented progressively; verify current scope of reform categories with latest HRSD circulars. GOSI contribution rates are subject to periodic adjustment.

## Related Skills

- [[kb-employment-law-uae]]
- [[kb-employment-law-lb]]
- [[kb-data-privacy-ksa-pdpl]]
- [[kb-fintech-licensing-cma-ksa]]
- [[draft-employment-contract]]
