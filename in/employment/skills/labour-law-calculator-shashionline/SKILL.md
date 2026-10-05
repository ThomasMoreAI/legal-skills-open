---
name: labour-law-calculator-shashionline
title: 'Skill: Labour Law Calculator'
description: Calculate statutory benefits under Indian labour laws including PF, ESI, Gratuity, Bonus, Retrenchment Compensation, Notice Pay, and Leave Encashment with precise formulas
author: shashionline
author_url: https://github.com/shashionline/indian-law-plugin/tree/master/skills/labour-law-calculator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: in
practice: employment
language: en
---

# Skill: Labour Law Calculator

## Purpose
Calculate statutory benefits under Indian labour laws including PF (Provident Fund), ESI (Employee State Insurance), Gratuity, Bonus, Retrenchment Compensation, Notice Pay, and Leave Encashment with precise formulas, wage ceilings, and eligibility thresholds.

## Capabilities

### 1. PF (Provident Fund) Calculation
- Calculate employee contribution (12% of Basic + DA, capped at Rs. 15,000)
- Calculate employer contribution (12% - split into EPF 3.67% + EPS 8.33%)
- Handle voluntary contributions on higher wages
- Compute accumulated balance with interest (8.1% p.a. compound annually)
- Determine eligibility (establishments with 20+ employees)

### 2. ESI (Employee State Insurance) Calculation
- Calculate employee contribution (0.75% of gross wages, if ≤ Rs. 21,000/month)
- Calculate employer contribution (3.25% of gross wages)
- Determine eligibility threshold (wage ≤ Rs. 21,000/month)
- Apply to establishments with 10+ employees

### 3. Gratuity Calculation
- Calculate gratuity (Last drawn salary x 15 days x Years / 26)
- Apply 5-year continuous service eligibility rule
- Cap at Rs. 20 lakhs maximum
- Handle partial years (> 6 months = 1 year)
- Determine covered establishments (10+ employees)

### 4. Bonus Calculation
- Calculate statutory bonus (8.33% minimum, 20% maximum of wages)
- Apply wage ceiling (Rs. 21,000/month for eligibility, Rs. 7,000 OR Rs. 21,000 for calculation)
- Determine eligibility (establishments with 20+ employees, wage ≤ Rs. 21,000)
- Handle profit-based vs statutory minimum bonus

### 5. Retrenchment Compensation
- Calculate compensation (15 days average pay x Years of continuous service)
- Apply Section 25F ID Act formula
- Handle fractional years (> 6 months = 1 year)
- No maximum cap (unlike gratuity)

### 6. Notice Pay & Leave Encashment
- Calculate notice pay (1 month wages if termination without notice)
- Compute leave encashment (Earned leave balance x Daily wage)
- Apply leave balance rules (30 days per year of service - varies by Standing Orders)

## Calculation Frameworks

### PF (Provident Fund) Calculation

**Eligibility**: Establishments with 20+ employees

**Wage Ceiling**: Rs. 15,000/month (Basic + DA)

**Employee Contribution**:
```
If (Basic + DA) <= Rs. 15,000:
  Employee PF = (Basic + DA) x 12%

If (Basic + DA) > Rs. 15,000:
  Employee PF = Rs. 15,000 x 12% = Rs. 1,800/month
  (Unless employer voluntarily contributes on actual higher wages)
```

**Employer Contribution** (12% split):
```
EPF (Employee Provident Fund): (Basic + DA) x 3.67% -> Goes to employee's PF account
EPS (Employee Pension Scheme): (Basic + DA) x 8.33% (capped at Rs. 1,250) -> Goes to pension fund

If (Basic + DA) <= Rs. 15,000:
  EPF = (Basic + DA) x 3.67%
  EPS = (Basic + DA) x 8.33% (capped at Rs. 1,250)
  Total Employer Contribution = (Basic + DA) x 12%

If (Basic + DA) > Rs. 15,000:
  EPF = Rs. 15,000 x 3.67% = Rs. 550.50
  EPS = Rs. 1,250 (capped)
  Total = Rs. 1,800 (Rs. 550.50 + Rs. 1,250 rounded)
```

**Accumulated Balance** (with interest):
```
Interest Rate: 8.1% per annum (FY 2023-24), compounded annually
Formula: P x [(1 + r/100)^n]
Where P = Principal (annual contributions), r = 8.1%, n = years

Example: Rs. 3,600/month x 12 months = Rs. 43,200/year
After 5 years: approx Rs. 2,55,000
```

**Withdrawal Rules**:
- Allowed after 2 months unemployment (partial withdrawal)
- Full withdrawal after retirement / permanent disability / emigration

---

### ESI (Employee State Insurance) Calculation

**Eligibility**: Wage <= Rs. 21,000/month, establishments with 10+ employees

**Employee Contribution**: 0.75% of gross wages
**Employer Contribution**: 3.25% of gross wages

```
Gross Wages = Basic + DA + HRA + Other Allowances (excludes OT, bonus > ceiling)

If Gross Wages <= Rs. 21,000:
  Employee ESI = Gross Wages x 0.75%
  Employer ESI = Gross Wages x 3.25%
  Total ESI = Gross Wages x 4%

If Gross Wages > Rs. 21,000:
  NOT COVERED under ESI Act
```

**Example**:
```
Gross Wages: Rs. 18,000/month
Employee ESI: Rs. 18,000 x 0.75% = Rs. 135/month
Employer ESI: Rs. 18,000 x 3.25% = Rs. 585/month
Total: Rs. 720/month
```

**ESI Benefits**:
- Medical treatment (free for employee + family)
- Sickness benefit (70% wages for 91 days/year)
- Maternity benefit (100% wages for 26 weeks)
- Disablement benefit (90% wages for permanent disability)

---

### Gratuity Calculation

**Eligibility**: 5 years continuous service (reduced to 240 days for death/disablement)

**Formula**:
```
Gratuity = (Last Drawn Salary x 15 days x Years of Service) / 26

Where:
- Last Drawn Salary = Basic + DA (per month)
- 26 = Working days per month (for monthly wage earners)
- Years of Service = Completed years (if > 6 months in last year, count as 1 year)
```

**Maximum Cap**: Rs. 20,00,000

**Example 1: Standard Calculation**
```
Last Drawn Salary: Rs. 30,000/month
Service Period: 8 years 3 months (< 6 months, so count as 8 years)
Daily Wage: Rs. 30,000 / 26 = Rs. 1,153.85
Gratuity: Rs. 1,153.85 x 15 x 8 = Rs. 1,38,462
```

**Example 2: Partial Year Rounding**
```
Service: 7 years 8 months (> 6 months, count as 8 years)
Last Drawn Salary: Rs. 25,000
Daily Wage: Rs. 25,000 / 26 = Rs. 961.54
Gratuity: Rs. 961.54 x 15 x 8 = Rs. 1,15,385
```

**Example 3: Cap Applied**
```
Service: 35 years
Last Drawn Salary: Rs. 80,000/month
Gratuity (without cap): Rs. 80,000 / 26 x 15 x 35 = Rs. 1,61,53,846
Gratuity (with cap): Rs. 20,00,000 (capped)
```

**Tax Treatment**:
- Exempt up to Rs. 20 lakhs (for employees covered under Gratuity Act)
- Exempt up to Rs. 10 lakhs (for government employees)

---

### Bonus Calculation

**Eligibility**:
- Wage <= Rs. 21,000/month
- Establishment with 20+ employees (in a year)
- Worked minimum 30 days in a year

**Wage Ceiling for Calculation**:
- **Earlier**: Rs. 7,000/month (for calculation, even if actual wage higher)
- **Current (Post-2014 Amendment)**: Rs. 21,000/month (some states, check local rules)
- **Recommendation**: Use Rs. 7,000 for safety (conservative calculation)

**Formula**:
```
Minimum Statutory Bonus: 8.33% of wages (or Rs. 100, whichever higher)
Maximum Bonus: 20% of wages

Bonus = Wages x 8.33% (minimum)
      OR Wages x (Profit-based %) if higher (but capped at 20%)
```

**Example 1: Wage < Rs. 7,000**
```
Monthly Wage: Rs. 6,000
Annual Bonus: Rs. 6,000 x 12 months x 8.33% = Rs. 5,997.60 (minimum)
```

**Example 2: Wage > Rs. 7,000 (Ceiling Applied)**
```
Monthly Wage: Rs. 15,000
Bonus Calculation Wage: Rs. 7,000 (capped for calculation)
Annual Bonus: Rs. 7,000 x 12 x 8.33% = Rs. 6,996.80 (minimum)

If employer wants to pay on actual wages (voluntary):
Rs. 15,000 x 12 x 8.33% = Rs. 14,994
```

**Proportionate Bonus** (if worked < 12 months):
```
Worked Days: 200 days in a year
Proportionate Bonus: (Rs. 7,000 x 12 x 8.33%) x (200/365) = Rs. 3,833
```

---

### Retrenchment Compensation (Section 25F, ID Act)

**Eligibility**: Continuous service of 240 days (1 year) or more

**Formula**:
```
Retrenchment Compensation = 15 days Average Pay x Years of Continuous Service

Where:
- Average Pay = Average wages for last 12 months
- 15 days = Statutory entitlement
- Years = Completed years (if > 6 months in fractional year, count as 1 year)
```

**No Maximum Cap** (unlike gratuity - Rs. 20 lakhs cap)

**Example 1: Standard Calculation**
```
Average Monthly Pay: Rs. 22,000
Service: 6 years 8 months (> 6 months, count as 7 years)
Daily Average Pay: Rs. 22,000 / 26 = Rs. 846.15
Retrenchment Compensation: Rs. 846.15 x 15 x 7 = Rs. 88,846.15
```

**Example 2: Long Service**
```
Average Monthly Pay: Rs. 40,000
Service: 25 years
Daily Average Pay: Rs. 40,000 / 26 = Rs. 1,538.46
Retrenchment Compensation: Rs. 1,538.46 x 15 x 25 = Rs. 5,76,923
(No cap - full amount payable)
```

**Section 25F Conditions** (ALL mandatory for valid retrenchment):
1. One month notice OR Notice pay in lieu
2. Retrenchment compensation (15 days x years)
3. Government approval (if establishment has 100+ workers)

**If Section 25F not complied**: Retrenchment is ILLEGAL -> Worker entitled to reinstatement + back wages

---

### Notice Pay Calculation

**Standard Notice Period**: 1 month (as per Industrial Employment Act, varies by Standing Orders)

**Formula**:
```
If termination without notice:
  Notice Pay = 1 month gross salary

If notice given but employee relieved earlier:
  Notice Pay = (Notice period - Days worked) x Daily wage
```

**Example 1: Immediate Termination**
```
Gross Salary: Rs. 28,000/month
Notice Pay: Rs. 28,000 (full 1 month)
```

**Example 2: Partial Notice Period**
```
Gross Salary: Rs. 30,000/month
Notice Period: 30 days
Employee relieved on Day 10 (employer wants immediate exit)
Notice Pay: (30 - 10) days x (Rs. 30,000 / 26) = 20 x Rs. 1,153.85 = Rs. 23,077
```

---

### Leave Encashment Calculation

**Earned Leave Accumulation**: 1 day per 20 days worked (varies by Standing Orders)
- **Standard**: 15-18 days earned leave per year
- **Maximum Accumulation**: 30-45 days (carry forward limit - varies)

**Formula**:
```
Leave Encashment = Earned Leave Balance x Daily Wage

Where:
- Daily Wage = Monthly Salary / 26 (working days)
- Earned Leave Balance = Accumulated earned leave (not availed)
```

**Example 1: Full Year Leave Balance**
```
Monthly Salary: Rs. 25,000
Earned Leave: 20 days (accumulated)
Daily Wage: Rs. 25,000 / 26 = Rs. 961.54
Leave Encashment: 20 x Rs. 961.54 = Rs. 19,230.77
```

**Example 2: Multi-Year Accumulation**
```
Service: 5 years
Earned Leave Per Year: 15 days
Availed Leave: 10 days/year
Balance: (15 - 10) x 5 = 25 days
Monthly Salary: Rs. 35,000
Daily Wage: Rs. 35,000 / 26 = Rs. 1,346.15
Leave Encashment: 25 x Rs. 1,346.15 = Rs. 33,653.85
```

**Tax Treatment**:
- Leave encashment on retirement: Exempt up to Rs. 25 lakhs (subject to conditions)
- Leave encashment during service: Fully taxable

---

## Comprehensive Statutory Dues Calculator

### Input Parameters
```markdown
**Employee Details**:
- Name: [Employee Name]
- Service Period: [Start Date] to [End Date] = [X years Y months]
- Last Drawn Salary: Rs. [Amount]/month
- Basic Salary: Rs. [Amount]
- DA (Dearness Allowance): Rs. [Amount]
- HRA: Rs. [Amount]
- Other Allowances: Rs. [Amount]
- Gross Salary: Rs. [Total]
```

### Output Format
```markdown
## Statutory Benefits Calculation Summary

### PF (Provident Fund)
- **Contribution Basis**: Basic + DA = Rs. [Amount]
- **Employee Contribution**: Rs. [Amount] x 12% x [Months] = Rs. [Total]
- **Employer Contribution**: Rs. [Amount] x 12% x [Months] = Rs. [Total]
- **Accumulated Balance** (with 8.1% interest): Rs. [Amount]
- **Withdrawable Amount**: Rs. [Amount]

### ESI (Employee State Insurance)
- **Eligibility**: Gross Wages [<= / >] Rs. 21,000 -> [COVERED / NOT COVERED]

### Gratuity
- **Eligibility**: [X years Y months] -> [ELIGIBLE / NOT ELIGIBLE] (5 years required)
- **If Eligible**: Gratuity = Rs. [Daily x 15 x Years] = Rs. [Amount]
- **Capped at**: Rs. 20,00,000 (if calculated amount higher)

### Bonus (If Applicable)
- **Eligibility**: Wage [<= / >] Rs. 21,000, Establishment [20+ / <20] employees
- **Minimum Bonus (8.33%)**: Rs. [Wage x 12 x 8.33%] = Rs. [Amount]

### Notice Pay (If Not Given)
- **Notice Pay**: Rs. [Monthly Salary] = Rs. [Amount]

### Leave Encashment
- **Earned Leave Balance**: [X days]
- **Leave Encashment**: Rs. [Daily x Days] = Rs. [Amount]

### Retrenchment Compensation (If Applicable)
- **Retrenchment Compensation**: Rs. [Daily x 15 x Years] = Rs. [Amount]

---

## TOTAL STATUTORY DUES
| Component | Amount (Rs.) |
|-----------|--------------|
| PF (Employee + Employer) | [Amount] |
| ESI (if applicable) | [Amount] |
| Gratuity | [Amount] |
| Bonus | [Amount] |
| Notice Pay | [Amount] |
| Leave Encashment | [Amount] |
| Retrenchment Compensation (if applicable) | [Amount] |
| **GRAND TOTAL** | **[Sum]** |
```

---

## Protocols Utilized

- IL-LABOUR-EPF-ESIC.md (PF and ESI regulations)
- IL-LABOUR-GRATUITY.md (Gratuity Act 1972)
- IL-LABOUR-BONUS.md (Bonus Act 1965)
- IL-LABOUR-INDUSTRIAL-DISPUTES.md (Section 25F retrenchment)
- IL-LABOUR-EMPLOYMENT-AGREEMENT.md (Notice period, leave rules)

---

**Version:** 1.0
**Last Updated:** December 2025
**Jurisdiction:** India (PF Act 1952, ESI Act 1948, Gratuity Act 1972, Bonus Act 1965, ID Act 1947)
