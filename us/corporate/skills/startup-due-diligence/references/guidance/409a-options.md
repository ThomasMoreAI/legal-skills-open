# Stock Options & 409A Valuation Guide

## Overview

Section 409A of the Internal Revenue Code requires that stock options be granted with an exercise price at or above fair market value (FMV) at the time of grant. Non-compliance results in significant tax penalties.

## 409A Requirements

### Fair Market Value Determination

**Methods to establish FMV:**

1. **Independent appraisal** (most common)
   - Qualified third-party valuation
   - Valid for 12 months (or until material event)
   - Safe harbor if properly done

2. **Board valuation** (limited use)
   - Only for illiquid startup stock
   - Must be reasonable
   - Higher audit risk

### Valuation Safe Harbors

| Method | Requirements | Risk Level |
|--------|--------------|------------|
| Independent appraisal | Qualified appraiser; arm's length | Low |
| Startup safe harbor | <10 years old; illiquid; board determines | Medium |
| Binding formula | Consistently applied formula | Medium |

### What Triggers New Valuation

**Material events requiring new 409A:**
- Priced equity financing
- Significant revenue milestone
- Material IP acquisition
- Major customer contracts
- M&A discussions
- 12 months since last valuation

## 409A Valuation Report

### Contents to Review

**Company description:**
- Business overview
- Products/services
- Stage of development

**Financial analysis:**
- Historical financials
- Projections
- Comparable companies

**Valuation approaches:**
- Market approach (comparable companies)
- Income approach (DCF)
- Asset approach (rarely used)

**Option allocation:**
- PWERM or OPM methodology
- Discount for lack of marketability (DLOM)
- Common stock value per share

### Key Metrics

| Term | Definition |
|------|------------|
| Enterprise Value | Total company value |
| Equity Value | Enterprise value - debt + cash |
| DLOM | Discount for lack of marketability (typically 20-40%) |
| Common Value | Per share value after preferences and DLOM |

## Due Diligence Process

### Step 1: Inventory All Option Grants

For each grant, document:
- Grant date
- Number of shares
- Exercise price
- Vesting schedule
- 409A valuation date relied upon
- 409A FMV at grant date

### Step 2: Compare Exercise Prices to FMV

```
For each grant:
  If exercise_price >= FMV_at_grant:
    COMPLIANT
  Else:
    NON-COMPLIANT (409A issue)
```

### Step 3: Check Valuation Currency

**Valuation valid if:**
- Less than 12 months old at grant date
- No material events since valuation
- Valuation methodology reasonable

### Step 4: Review Grant Documentation

**Required for each grant:**
- Board consent authorizing grant
- Stock option agreement (signed)
- Notice of grant
- Exercise price matches board consent

## Common 409A Issues

### Issue: Options Below FMV

**Scenario:** Options granted at $0.10 when 409A was $0.25

**Consequences for option holder:**
- Immediate income recognition on vesting
- 20% additional tax penalty
- Interest from grant date
- State tax penalties (varies)

**Remediation options:**
1. **Repricing** - Increase exercise price (employee loses spread)
2. **Cash settlement** - Pay employees for lost value
3. **Tax gross-up** - Company pays penalties
4. **Section 409A correction programs** (limited)

### Issue: No 409A Valuation

**Scenario:** Options granted without any valuation

**Risk:** All grants potentially non-compliant

**Remediation:**
- Get retroactive 409A (limited effectiveness)
- Consider repricing or cash settlement
- Disclose risk to investors

### Issue: Stale Valuation

**Scenario:** 409A is 18 months old; material events occurred

**Risk:** Grants after staleness may be below FMV

**Remediation:**
- Get new valuation immediately
- Assess grants made during gap period
- May need to reprice affected grants

### Issue: Grant Date Discrepancies

**Scenario:** Board consent dated different from option agreement

**Risk:** Backdating allegations; 409A non-compliance

**Remediation:**
- Reconcile dates
- Use later date as effective grant date
- May need repricing

## Red Flags Summary

| Issue | Severity | Notes |
|-------|----------|-------|
| No 409A valuation ever obtained | 🔴 CRITICAL | All grants potentially non-compliant |
| Exercise price below 409A FMV | 🔴 CRITICAL | Direct 409A violation |
| 409A >12 months old at grant | 🟠 MATERIAL | Likely stale; assess |
| Material event without new 409A | 🟠 MATERIAL | Grants may be problematic |
| Board consent after grant date | 🟠 MATERIAL | Backdating risk |
| Missing grant documentation | 🟡 MINOR | Can be cured |
| Different prices same day | 🟡 MINOR | Should be same FMV |

## Valuation Timeline Best Practices

```
409A Valid Period:
|------ 12 months ------|
^                       ^
Valuation Date     Must get new valuation

Material Event Trigger:
|---- 409A Valid ----|
^                    ^
Valuation       Material Event → Get new 409A immediately
```

## Questions for Diligence

1. When was the first 409A valuation obtained?
2. Are all subsequent valuations within 12 months of each other?
3. Were there material events between valuations?
4. Does every option grant have a supporting 409A?
5. Is every exercise price ≥ 409A FMV at grant?
6. Are grant dates consistent across all documents?
7. Is the option pool properly authorized in charter?
8. Is the equity incentive plan properly adopted?
