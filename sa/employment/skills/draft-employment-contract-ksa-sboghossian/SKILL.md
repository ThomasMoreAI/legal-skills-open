---
name: draft-employment-contract-ksa-sboghossian
title: Employment Contract — Saudi Arabia (KSA)
description: Use when drafting a Saudi Arabia employment contract under the KSA Labor Law (Royal Decree M/51, as amended). Covers mandatory clauses, salary structure (basic + allowances for EOSA calculation), definite vs. indefinite contract types, probation up to 180 days, GOSI registration, bilingual Arabic/English (Arabic controls, registered via Qiwa/HRSD), kafala/sponsorship mechanics for non-Saudi employees, Saudization (Nitaqat) compliance, and non-compete enforceability up to 2 years.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-employment-contract-ksa
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: sa
practice: employment
language: en
---

# Employment Contract — Saudi Arabia (KSA)

## When to use this

Use this skill to draft an employment contract governed by the KSA Labor Law (Royal Decree M/51 dated 23/8/1426H, as amended by various Royal Decrees and Ministry of Human Resources and Social Development decisions). The KSA Labor Law applies to all employees working in Saudi Arabia, with limited exclusions (domestic workers, agriculture workers, and certain government categories have separate regimes).

The contract **must be registered with HRSD via the Qiwa platform** in Arabic. English may be provided as a courtesy translation; **Arabic controls** in all disputes before Saudi courts and the HRSD.

## Required inputs

| Input | Why it matters | Default |
|-------|----------------|---------|
| Employer (full legal name, CR number, MOL/HRSD establishment code, address) | Qiwa registration requires exact establishment data | — |
| Employee (full name, nationality, Iqama / National ID number, qualifications) | Determines kafala status, GOSI contribution rate | — |
| Role and job title (Arabic + English) | Core contractual obligation; basis for performance evaluation | — |
| Place of work (city + specific location) | Determines applicable municipal license; travel obligations | — |
| Reporting line | Management structure | — |
| Salary breakdown (see structure below) | EOSA calculation base depends on component breakdown | — |
| Start date | Triggers probation, leave accrual, and GOSI enrollment | — |
| Contract type (definite / indefinite) | Determines notice period, termination rights | Definite for non-Saudis |
| Nationality | Determines kafala obligations, GOSI rates, Saudization impact | — |

## Salary structure (critical for EOSA calculation)

Saudi practice requires salary to be broken into named components. EOSA (End-of-Service Award / مكافأة نهاية الخدمة) is calculated on the **last total salary including allowances** (not basic salary alone — different from UAE where EOSG is basic salary only).

Standard structure:
| Component | Arabic | Notes |
|-----------|--------|-------|
| Basic salary | الراتب الأساسي | — |
| Housing allowance | بدل السكن | Typically 25–30% of basic |
| Transportation allowance | بدل النقل | Fixed amount or percentage |
| Other allowances | بدلات أخرى | Food, telephone, education, etc. |
| **Total salary** | إجمالي الراتب | Sum of all components; EOSA base |

Always state the total salary in SAR. If any portion is paid in USD (for expatriate employees), specify the exchange-rate mechanism.

## Mandatory provisions under KSA Labor Law

### Working hours
- Standard: 48 hours per week (8 hours/day × 6 days).
- During Ramadan: 36 hours per week (6 hours/day) for Muslim employees.
- Overtime: permitted beyond standard hours; overtime pay at not less than **basic salary + allowances × 1.5** for each hour above the daily limit.

### Annual leave
| Years of service | Leave entitlement |
|---|---|
| First 5 years | 21 working days per year |
| After 5 years | 30 working days per year |

Leave cannot be encashed unless employee is entitled and parties agree. Unused leave may be carried over (employer must allow employee to use leave within 12 months).

### Hajj leave
Muslim employees are entitled to **15 days' paid leave** for Hajj, once during their service with the employer. Cannot be deducted from annual leave.

### End-of-Service Award (EOSA / مكافأة نهاية الخدمة)
Mandatory statutory benefit:

| Years of service | Accrual per year |
|---|---|
| First 5 years | Half month's total salary per year |
| Each year thereafter | Full month's total salary per year |

**Calculation base**: last total salary (including all allowances) — not just basic salary. Pro-rate for fractions of a year.

Reductions apply if employee resigns within first 2 years (no EOSA), 2–5 years (1/3 of entitlement), 5–10 years (2/3 of entitlement). Full entitlement accrues only after 10 years of service or if terminated by employer without cause.

Always calculate EOSA using the [[kb-employment-law-ksa]] calculator or the Qiwa platform.

### Probation period
- Default: **90 days**.
- Extended: up to **180 days** by mutual written consent (must be agreed at contract inception, not mid-probation).
- During probation: either party may terminate without notice (no EOSA earned during probation if terminated).

### Notice period (indefinite contracts)
- Minimum **60 days' written notice** for monthly-paid employees terminating an indefinite contract.
- Definite contracts expire at the end of term; no notice required for expiry (but early termination by employer without cause triggers compensation).

### GOSI registration
General Organization for Social Insurance (GOSI) registration is mandatory for all employees (Saudi and expatriate):
- Saudi employees: employer 11.75% + employee 9.75% of salary.
- Non-Saudi employees: employer 2% (occupational hazard insurance only) + no employee contribution.
Include an acknowledgment that the employer has registered or will register the employee with GOSI within the required period.

## Contract type analysis

| Type | Who | Max duration | Renewal |
|---|---|---|---|
| **Definite (محدد المدة)** | Default for non-Saudis; Saudis may use | Typically max 5 years per term; renewable | Renews as definite; after 3 consecutive renewals or 4+ years, may be deemed indefinite |
| **Indefinite (غير محدد المدة)** | Default for Saudis; expatriates on certain conditions | No fixed end date | N/A |

Rule: if a definite contract is renewed more than three times or if the employee remains employed beyond a total period of 4 years, it is treated as an indefinite contract by KSA courts unless a new definite contract is entered.

## Kafala / sponsorship provisions for non-Saudi employees

The kafala (كفالة) system makes the employer the immigration sponsor for non-Saudi employees. The contract must address:
- Employer sponsors work visa and residence permit (Iqama).
- Transfer of sponsorship (نقل كفالة) requires employer consent via Qiwa; employee cannot transfer independently except under conditions established by the Qiwa platform.
- If employee resigns or is terminated, exit procedures include visa cancellation; employer must complete final settlement before releasing employee.
- Include a clause stating that the employment is conditional on the employee maintaining valid immigration status; employer will cooperate in renewing Iqama but is not liable for delays caused by government processing.

Post-2021 reform note: Saudi labor reforms introduced improved transfer mechanisms; employees with more than one year of service have enhanced transfer rights. The contract should not attempt to waive these statutory rights.

## Saudization (Nitaqat program)

Employers in KSA are subject to the Nitaqat (نطاقات) Saudization program, which requires minimum ratios of Saudi nationals in the workforce depending on the industry sector. Include:
- Acknowledgment that the employer complies with Nitaqat requirements.
- Employee's role in supporting Saudization compliance (for Saudi employees: acknowledgment of Saudization quota role).
- For non-Saudi hires: confirmation that the employer has the required quota capacity.

## Non-compete clause

KSA Labor Law permits non-compete restrictions with the following conditions for enforceability:
- **Duration**: maximum **2 years** post-employment.
- **Scope**: must be limited to the same line of business / industry as the employee's work for the employer.
- **Territory**: must be limited to a defined geographic area where the employer operates.
- **Legitimate interest**: must protect a genuine business interest (trade secrets, customer relationships, specialized training).
- Excessive scope (national blanket, indefinite duration) is unenforceable.

Draft as a separate clause; include a severability provision so that an unenforceable scope does not void the remainder of the non-compete.

## Mandatory Arabic-language contract

Per Ministerial Decision: the employment contract **must be in Arabic** and registered on the **Qiwa platform** (منصة قوى) with HRSD. English translation may be attached as Schedule 1 but Arabic controls.

The Arabic version controls in all proceedings before:
- HRSD Labor Offices (مكاتب العمل).
- Labor Courts (المحاكم العمالية).
- The Commission for the Settlement of Labor Disputes.

## Document structure

1. Parties (بيانات الأطراف) — Arabic names; employer CR; employee Iqama/ID.
2. Job title and description (المسمى الوظيفي ومهام العمل).
3. Place of work (مكان العمل).
4. Contract type and duration (نوع العقد ومدته).
5. Probation period (فترة التجربة).
6. Working hours (ساعات العمل).
7. Salary and compensation (الأجر والمزايا) — itemized per structure above.
8. Annual leave (الإجازة السنوية).
9. Hajj leave (إجازة الحج) — for Muslim employees.
10. Sick leave (الإجازة المرضية).
11. GOSI registration acknowledgment (التأمينات الاجتماعية).
12. End-of-service award (مكافأة نهاية الخدمة) — statement of statutory entitlement.
13. Notice period (مدة الإشعار).
14. Confidentiality (السرية).
15. Non-compete (عدم المنافسة) — if applicable.
16. Termination (إنهاء العقد) — grounds; notice; summary termination for cause.
17. Kafala acknowledgment (الكفالة) — for non-Saudi employees.
18. Governing law (القانون الحاكم) — KSA Labor Law.
19. Signatures (التوقيعات) — employer and employee; date in both Hijri and Gregorian.

## Common mistakes

1. **Salary stated as a lump sum without breakdown** — prevents accurate EOSA calculation; Qiwa platform requires component breakdown.
2. **Indefinite contract for non-Saudi without legal basis** — non-Saudis default to definite contracts; indefinite must be expressly permitted.
3. **Probation extended after commencement** — probation extension must be agreed at contract inception; mid-term extensions are invalid.
4. **Non-compete without geographic limit** — national blanket non-competes are routinely declared unenforceable.
5. **No Arabic version** — cannot be registered on Qiwa; not enforceable before Saudi courts.
6. **GOSI rate applied to basic only** — GOSI contributions (for Saudis) are calculated on total salary (all components).

## Related skills

- [[draft-employee-handbook]] — workplace policies that supplement this contract
- [[kb-employment-law-ksa]] — KSA labor law reference pack with statutory thresholds and recent amendments
- [[draft-employment-contract-uae]] — UAE federal employment contract for cross-border comparison
- [[draft-employment-contract-lb]] — Lebanese employment contract
