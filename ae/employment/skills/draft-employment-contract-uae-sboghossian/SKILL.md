---
name: draft-employment-contract-uae-sboghossian
title: Employment Contract — UAE Federal Onshore
description: Use when drafting a UAE federal onshore employment contract under Federal Decree-Law No. 33/2021 (as amended). All UAE onshore contracts must be definite-term (indefinite contracts were abolished), registered with MOHRE, and capped at 3-year initial term. Covers mandatory MOHRE registration, end-of-service gratuity (EOSG) on basic salary only, 30-day annual leave, Cabinet Decision 1/2022 non-compete limits, and the critical DIFC/ADGM override — those free zones use entirely separate employment regimes.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-employment-contract-uae
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ae
practice: employment
language: en
---

# Employment Contract — UAE Federal Onshore

## When to use this

Use this skill to draft an employment contract for an employee working for a UAE mainland (onshore) employer registered with the Department of Economic Development (DED) or equivalent emirate authority. Governing law: Federal Decree-Law No. 33/2021 on the Regulation of Labour Relations (and its implementing Cabinet Decisions), which replaced the prior Federal Law No. 8/1980.

**Critical scoping rule:** Federal Decree-Law 33/2021 applies to **onshore UAE employers only**. If the employer is registered in:
- **DIFC**: DIFC Employment Law (DIFC Law 4/2021) applies — use a separate DIFC contract.
- **ADGM**: ADGM Employment Regulations 2024 apply — use a separate ADGM contract.
- **Other free zones** (DMCC, JAFZA, Sharjah, etc.): federal law generally applies unless the free-zone authority has issued specific employment regulations.

Always identify the employer's registration to determine the correct regime before drafting.

## Required inputs

| Input | Why it matters | Default |
|-------|----------------|---------|
| Employer (full legal name, TRN, trade license number, address) | MOHRE registration requires exact details | — |
| Employee (full name, nationality, passport number) | Residence visa and work permit basis | — |
| Role and grade | Core obligation; basis for EOSG calculation if salary changes | — |
| Salary breakdown (basic + allowances) | EOSG calculated on basic salary only under federal law | — |
| Start date | Work permit activation; EOSG accrual begins | — |
| Contract term (max 3 years) | Mandatory definite-term format | 3 years |

## Key structural rules under Federal Decree-Law 33/2021

### Definite-term contracts only
**Federal Decree-Law 33/2021 abolished indefinite-term contracts** for onshore UAE employment. All contracts must be definite-term with a maximum initial term of **3 years**. Contracts are renewable; there is no limit on number of renewals.

Failure to convert pre-2022 indefinite contracts to definite terms (deadline was February 2023) means the contract is governed by the new law but treated as if it were a renewable 3-year contract.

### MOHRE standard form
All employment contracts must be in the **MOHRE standard electronic form** and registered on the MOHRE portal. The standard form has fixed fields; additional provisions may be attached as an "Additional Terms" appendix but must not contradict the standard form.

### Work permit and residence visa
Onshore employment is conditional on:
- MOHRE work permit issuance.
- GDRFA (General Directorate of Residency and Foreigners Affairs) residence visa.

Include: "This employment is conditional on the Employee holding and maintaining valid MOHRE work authorization and UAE residence visa. The Employer shall facilitate sponsorship; the Employee is responsible for compliance with immigration law."

## Mandatory provisions

### Working hours
- Maximum: **8 hours per day / 48 hours per week**.
- Reduced during Ramadan: for Muslim employees, working hours are reduced by **2 hours per day**.
- Overtime: permitted beyond limits; minimum overtime rate of **1.25×** regular hourly rate; **1.5×** for overtime worked between 9 pm and 4 am.

### Annual leave
- **30 calendar days** per year after completing one full year of service.
- Pro-rated for first year and on termination.
- Employer may schedule leave; employee may request leave timing.
- Leave pay must be paid before the employee takes leave.

### Sick leave (Article 31)
After probation:
- First 15 days: full pay.
- Next 30 days: half pay.
- Subsequent sick leave: unpaid.
Total entitlement: 45 days per year.

### Maternity / paternity leave
- Maternity: **60 working days** (45 days full pay + 15 days half pay).
- Paternity: **5 working days** within the first 6 months after birth.

### End-of-Service Gratuity (EOSG)

EOSG calculation:
- **First 5 years**: 21 calendar days' **basic salary** per year of service.
- **6th year onwards**: 30 calendar days' **basic salary** per year of service.
- Pro-rated for fractions of a year.

**Critical:** EOSG is calculated on **basic salary only** — housing, transport, and other allowances are excluded. This is the opposite of KSA (where EOSA is on total salary).

Maximum EOSG = 2 years' basic salary (cap under federal law).

EOSG is payable on termination regardless of who terminates, but not during probation. If employee resigns within the first year, no EOSG is earned.

### Probation period
- Maximum: **6 months** (increased from 3 months under the prior law).
- During probation: either party may terminate with **14 days' notice** (employer) or **1 month's notice** (employee moving to another UAE employer) or **14 days' notice** (employee moving outside UAE).
- No EOSG earned during probation if terminated.

### Notice period
- Minimum 30 days; maximum 90 days as agreed in the contract.
- Pay-in-lieu of notice is permitted.
- If employee resigns without providing proper notice, employer may deduct notice-period salary.

## Salary structure

Federal law requires the salary to be stated in the MOHRE form with breakdown:

| Component | Notes |
|---|---|
| Basic salary (الراتب الأساسي) | EOSG calculation base; minimum 50% of total package by convention |
| Housing allowance (بدل السكن) | Employer-provided or cash allowance |
| Transportation allowance (بدل النقل) | Fixed amount |
| Other allowances | Education, telephone, food |

**Total remuneration** = all components. State all amounts in AED.

For expatriate senior employees with USD/GBP-denominated contracts: specify the exchange rate mechanism; the MOHRE requires AED equivalent on registration.

## Non-compete (Cabinet Decision 1/2022)

Federal Decree-Law 33/2021 and Cabinet Decision 1/2022 permit non-compete clauses with:
- **Duration**: maximum **2 years** post-termination.
- **Geographic scope**: must be reasonable relative to the employee's actual work.
- **Activity scope**: limited to activities that genuinely compete with the employer's business.
- No statutory compensation requirement (unlike some jurisdictions) — but courts may refuse to enforce an overly broad clause.

Post-2022, UAE courts have become more willing to enforce reasonable non-competes; conversely, overbroad clauses (national blanket, multi-year, all-industry) are routinely declared invalid.

### DIFC and ADGM — completely separate regimes

Do **not** use this skill for DIFC or ADGM employees. These free zones have their own employment laws that differ materially from the federal law:

| Feature | UAE Federal | DIFC (Law 4/2021) | ADGM (Regs 2024) |
|---|---|---|---|
| Contract type | Definite-term only | Definite or indefinite permitted | Definite or indefinite permitted |
| EOSG calculation | Basic salary only | Complex formula (Law 4/2021 Art. 18) | ADGM formula |
| Minimum leave | 30 days | 20 working days | 20 working days |
| Registration | MOHRE | DIFC internal | ADGM RA |
| Governing court | UAE labor courts | DIFC Courts | ADGM Courts |

## Document structure

1. Employer details (بيانات صاحب العمل) — legal name, TRN, trade license, address.
2. Employee details (بيانات العامل) — name, nationality, passport, position.
3. Contract type and term (نوع العقد ومدته) — definite; start and end date; renewal mechanism.
4. Probation period (فترة التجربة) — duration; termination notice during probation.
5. Place of work (مكان العمل).
6. Working hours (ساعات العمل).
7. Salary (الراتب) — itemized breakdown; currency AED; payment date.
8. Annual leave (الإجازة السنوية).
9. Sick leave (الإجازة المرضية).
10. Maternity/paternity leave (إجازة الأمومة/الأبوة).
11. EOSG statement (مكافأة نهاية الخدمة) — statutory entitlement stated; calculation methodology.
12. Notice period (مدة الإشعار).
13. Non-compete (شرط عدم المنافسة) — if applicable.
14. Confidentiality and IP (السرية والملكية الفكرية).
15. Work permit and residency (تصريح العمل والإقامة).
16. Governing law (القانون الحاكم) — Federal Decree-Law 33/2021.
17. Signatures (التوقيعات) — bilingual; date.

## Common mistakes

1. **Drafting indefinite-term contracts** — abolished under Federal Decree-Law 33/2021; MOHRE will not register them.
2. **EOSG calculated on total salary** — federal law uses basic salary only; including allowances overstates liability.
3. **Probation period set at 3 months** — maximum is 6 months; using 3 months is valid but unnecessarily short for senior roles.
4. **DIFC/ADGM employment governed by federal law** — wrong regime; entirely different law and courts apply.
5. **Non-compete scope too broad** — Cabinet Decision 1/2022 parameters apply; national blanket clauses are challengeable.
6. **Missing work-permit condition** — if work permit is not issued, the contract has no legal basis; the condition must be explicit.

## Related skills

- [[draft-employee-handbook]] — workplace policies document supplementing the contract
- [[kb-employment-law-uae]] — UAE labor law reference pack with statutory thresholds and Cabinet Decisions
- [[draft-employment-contract-ksa]] — KSA employment contract
- [[draft-employment-contract-lb]] — Lebanese employment contract
