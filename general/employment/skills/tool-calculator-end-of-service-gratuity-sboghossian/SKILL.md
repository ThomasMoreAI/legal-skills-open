---
name: tool-calculator-end-of-service-gratuity-sboghossian
title: Tool — End-of-Service Gratuity / Award Calculator
description: Use when computing end-of-service gratuity (EOSG) or termination indemnity entitlements across MENA jurisdictions. Covers UAE Federal (Decree-Law 33/2021), DIFC (DEWS scheme), KSA (Labor Law Royal Decree M/51), and Lebanon (Labor Law Decree 207/1946). Returns the computed entitlement, step-by-step workings, caveats on partial years and resignation scenarios, and a disclaimer on contract-specific variations.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/tool/tool-calculator-end-of-service-gratuity
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Tool — End-of-Service Gratuity / Award Calculator

## What it does

Computes end-of-service entitlements (gratuity, indemnity, or DEWS balance) for employees in UAE Federal, DIFC, KSA, and Lebanese jurisdictions. Returns the computed amount, the full step-by-step calculation with the relevant legal formula, and caveats the user must verify against the actual employment contract and applicable collective agreements.

## Inputs

| Field | Type | Required | Notes |
|---|---|---|---|
| `jurisdiction` | enum | Yes | `UAE`, `DIFC`, `KSA`, `LB` |
| `monthlyBasicSalary` | number | Yes | Gross basic only — exclude housing, transport, other allowances (except KSA, where broader definition applies) |
| `yearsOfService` | number | Yes | Decimal years acceptable (e.g., 5.5) |
| `terminationReason` | enum | Yes | `employer_termination`, `resignation`, `mutual_agreement`, `redundancy` |
| `currency` | string | No | Defaults to jurisdiction currency (AED, SAR, LBP) |
| `monthsInPartialYear` | number | Conditional | Required if `yearsOfService` has a decimal component |

## Jurisdiction formulas

### UAE Federal (Decree-Law No. 33/2021)

**Salary base:** Basic salary only (housing, transport, and other allowances excluded).

**Formula:**
- Years 1–5: **21 days' basic salary** per year of service
- Year 6+: **30 days' basic salary** per year of service
- Pro-rated for partial years (minimum vesting: completion of 1 month)
- **Cap:** Total gratuity cannot exceed 2 years' total basic salary

**Daily rate computation:**
```
daily_basic = monthly_basic × 12 / 365
gratuity_year_1_to_5 = daily_basic × 21 × min(years, 5)
gratuity_year_6_plus = daily_basic × 30 × max(years - 5, 0)
total = min(gratuity_year_1_to_5 + gratuity_year_6_plus, monthly_basic × 24)
```

**Resignation reductions (UAE Federal):**
- Service < 1 year: no entitlement
- Service 1–3 years: 1/3 of full entitlement
- Service 3–5 years: 2/3 of full entitlement
- Service > 5 years: full entitlement

---

### DIFC (DEWS — DIFC Employee Workplace Savings Scheme)

Under the DEWS scheme (mandatory from February 2020 under DIFC Law No. 2/2019 and DIFC Employee Workplace Savings Scheme Rules):

- **Old EOSG is replaced** by monthly employer contributions to a DEWS savings account.
- **Employer contribution rate:**
  - Years 1–5: **5.83%** of monthly basic salary
  - Year 6+: **8.33%** of monthly basic salary
- On termination, the vested DEWS balance is paid to the employee.
- Vesting is immediate from month 1; there is no cliff.

**Note:** Employees who were employed before the DEWS effective date may have a legacy EOSG calculation for the pre-DEWS period + DEWS balance for the post-DEWS period. Confirm cutover date in the employment contract.

---

### KSA (Labor Law, Royal Decree M/51, Article 84)

**Salary base:** **Last wage including allowances** (broader than UAE — basic + housing + transport + regular allowances).

**Formula (employer-initiated termination — full entitlement):**
- Years 1–5: **half-month's wage** per year
- Year 6+: **one month's wage** per year

**Resignation reductions (sliding scale):**
- Service < 2 years: no entitlement
- Service 2–5 years: 1/3 of full entitlement
- Service 5–10 years: 2/3 of full entitlement
- Service > 10 years: full entitlement

**Misconduct dismissal (Article 80):** Employee forfeits EOSG entitlement if dismissed for cause under Article 80 grounds (e.g., serious misconduct, criminal conviction).

---

### Lebanon (Labor Law, Decree No. 207 of 1946)

**Statutory base:** Art 50 of the Labor Law.

**Formula:**
- Years 1–5: **one month of salary per year** of service
- Year 6+: **half a month's salary per year**

**Termination without cause (by employer):** Full statutory indemnity payable.

**Termination for cause:** If the employer has just cause, no indemnity is due. The threshold for "just cause" is high under Lebanese law and is frequently litigated.

**Resignation:** Employee is not entitled to the full indemnity on voluntary resignation. A separate notice-period indemnity may apply.

**NSSF layer:** In addition to the Labor Law indemnity, registered workers in Lebanon may have entitlements under the National Social Security Fund (NSSF) end-of-service scheme. These are separate calculations.

**Currency caveat — critical:** Lebanese salary contracts pre-2019 denominated in LBP require expert determination of the lawful conversion rate given the 2019–2023 financial crisis and BDL currency unification in February 2023. Default to BDL official rate unless instructed otherwise; flag the currency risk explicitly in output.

## Output schema

```json
{
  "jurisdiction": "UAE",
  "grossBasicSalary": 20000,
  "currency": "AED",
  "yearsOfService": 7.5,
  "terminationReason": "employer_termination",
  "computation": {
    "dailyRate": 657.53,
    "firstFiveYears": {
      "formula": "21 days × 5 years",
      "amount": 69040.84
    },
    "remainingYears": {
      "formula": "30 days × 2.5 years",
      "amount": 49315.07
    },
    "subTotal": 118355.91,
    "cap": 480000,
    "capApplied": false
  },
  "totalEntitlement": 118355.91,
  "caveats": [
    "Excludes housing and transport allowances per UAE Federal Decree-Law 33/2021",
    "Actual entitlement subject to contract terms and any valid waiver or settlement agreement",
    "NSSF or additional contractual gratuity not included"
  ],
  "disclaimer": "This is a legal-professional tool. Final entitlement must be confirmed by the supervising lawyer against the actual contract and applicable laws."
}
```

## Failure modes and escalation

| Scenario | Handling |
|---|---|
| Salary denominated in foreign currency | Convert at current BDL/BIS official rate; flag conversion date |
| Service period spans pre- and post-DEWS (DIFC) | Compute legacy EOSG for pre-DEWS period + DEWS balance for post-DEWS period separately |
| LBP contract pre-2019 (Lebanon) | Flag currency ambiguity; do not compute without expert rate instruction |
| Contract contains higher-than-statutory gratuity | Note that statutory formula is the minimum; contractual rate applies if higher |
| Misconduct dispute | Do not reduce EOSG automatically; flag that forfeiture requires a valid cause determination |

## Related skills

- [[tool-calculator-statutory-interest]]
- [[pa-workflow-employment]]
- [[draft-termination-letter]]
- [[kb-employment-law-mena]]
