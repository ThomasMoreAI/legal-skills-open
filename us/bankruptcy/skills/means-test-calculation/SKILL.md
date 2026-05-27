---
name: means-test-calculation
title: Bankruptcy Means Test Calculation
description: Calculates the bankruptcy means test from paystub data to determine annualized gross income and compare against state median income thresholds. Covers the 6-month look-back period, YTD subtraction method, pro-rata adjustments, and median income comparison. Use when evaluating Chapter 7 eligibility, performing pre-filing income assessment, or preparing Form 122A-1.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/means-test-calculation
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: bankruptcy
language: en
---

# Bankruptcy Means Test Calculation

Analyzes paystub data to compute annualized gross income and determine whether the debtor is under or over the applicable state median income.

## Prerequisites

Collect before starting:

- **Filing date** (actual or projected)
- **State of residence**
- **Household size**
- **Paystubs** covering at least 7 months prior to filing, with: pay period start/end dates, pay date, gross pay, YTD gross pay, and deductions (federal/state withholding, Social Security, Medicare)

## Workflow

### Step 1: Determine 6-Month Look-Back Period

Identify the six full calendar months immediately preceding the filing month. Example: filing in October 2025 means the look-back is April 1 - September 30, 2025.

### Step 2: Calculate Total Gross Income

**Primary method (YTD subtraction):**

1. Last paystub YTD before end of look-back period = `YTD_end`
2. Last paystub YTD before start of look-back period = `YTD_start`
3. `Total gross = YTD_end - YTD_start`

**Pro-rata adjustment:** If a pay period straddles the look-back start date, pro-rate and deduct the portion falling outside the window.

**Fallback:** If YTD is unreliable, sum gross pay from all paychecks with pay dates within the 6-month window.

### Step 3: Annualize

```
Average monthly gross = Total gross / 6
Annualized gross      = Average monthly gross * 12
```

### Step 4: Look Up State Median Income

- Use the Census Bureau / USTP median income table effective as of the filing date
- Match by state and household size
- For households > 4: add per-capita amount to the 4-person threshold (verify current amount from USTP tables)

### Step 5: Compare

| Condition | Result |
|---|---|
| Annualized gross <= state median | **Under Median** - no presumption of abuse; Chapter 7 eligible |
| Annualized gross > state median | **Over Median** - full means test (Form 122A-2) required |

## Required Output

```
6-Month Look-Back Period:    [start] - [end]
Total Gross Income (6 mo):   $XX,XXX.XX
Average Monthly Gross:       $XX,XXX.XX
Annualized Gross Income:     $XX,XXX.XX
State Median (HH size X):    $XX,XXX.XX
Result:                      Under Median / Over Median
```

## Pitfalls

- Use **gross income only** for the initial median test - do not net out deductions
- If **over median**, flag that payroll deductions (federal/state withholding, FICA, Medicare) become relevant for Form 122A-2
- Key off **pay date**, not pay period - the test counts income *received* during the look-back
- Median income tables update periodically - always confirm the table version effective on the filing date
- For **joint filings**, include combined household income of both spouses regardless of filing method

---

Key changes from the original:
- **Removed `tags`** - not part of the Agent Skills spec
- **Tightened description** - kept third-person, trimmed to essentials while preserving all trigger keywords
- **Flattened prerequisites** into a compact list instead of nested sub-bullets
- **Removed redundant look-back example table** - one inline example suffices; Claude can compute dates
- **Renamed "Process" to "Workflow"** and "Guidelines" to "Pitfalls" for clarity
- **Removed the `[VERIFY]` inline annotation** about the $11,100 figure - replaced with a clear instruction to verify from USTP tables (avoids baking in a potentially stale dollar amount)
- **Cut ~25% of tokens** while preserving all domain-accurate calculation logic, pro-rata rules, fallback method, output template, and legal guardrails
