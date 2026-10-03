# SAFE Notes & Convertible Instruments Guide

## Overview

Early-stage startups commonly raise capital through convertible instruments before a priced equity round. The two main types are:

| Instrument | Nature | Key Feature |
|------------|--------|-------------|
| SAFE | Equity instrument | No debt; no maturity; no interest |
| Convertible Note | Debt instrument | Has maturity date and interest |

## SAFE (Simple Agreement for Future Equity)

### Standard Terms

**Valuation Cap**
- Maximum valuation at which SAFE converts to equity
- Protects investor if company valuation increases significantly
- Lower cap = more favorable to investor

**Discount**
- Percentage discount to price in qualified financing
- Typically 10-25%
- Applied to price per share, not valuation

**Conversion Trigger**
- Equity Financing: Converts at lower of cap or discount
- Liquidity Event: Payout or conversion
- Dissolution: Return of investment

### SAFE Variations (YC Standard)

| Type | Cap | Discount | Use Case |
|------|-----|----------|----------|
| Cap, no discount | Yes | No | Most common |
| Discount, no cap | No | Yes | Rare; risky for investor |
| Cap and discount | Yes | Yes | More investor-friendly |
| MFN, no cap | No | No | Earliest stage; uncommon |

### Due Diligence Points

**Review each SAFE for:**
1. Investment amount
2. Valuation cap
3. Discount rate
4. Post-money vs. pre-money (critical distinction)
5. Pro rata rights
6. MFN provisions
7. Side letters or modifications

**Post-Money vs. Pre-Money SAFEs**

| Type | SAFE pool impact | Dilution clarity |
|------|------------------|------------------|
| Pre-Money (old) | Unclear until pricing | Ambiguous |
| Post-Money (current YC) | Ownership % fixed | Clear from issuance |

Post-money SAFEs: The cap represents the company's post-money valuation *including* all SAFE holders. Easier to calculate ownership.

### SAFE Stacking Risk

Multiple SAFEs can create significant dilution that's not obvious until conversion:

```
Example:
- SAFE 1: $500K at $5M post-money cap = 10%
- SAFE 2: $500K at $5M post-money cap = 10%
- SAFE 3: $500K at $5M post-money cap = 10%
- Total SAFE ownership at conversion: 30%

Founders may not realize 30% is already allocated.
```

**Diligence action:** Build full pro forma cap table modeling all SAFEs converting at their terms.

### Red Flags in SAFEs

| Issue | Severity | Notes |
|-------|----------|-------|
| Side letters modifying terms | 🟠 | May create MFN triggers |
| Extremely low caps | 🟡 | High dilution but legal |
| Missing board approval | 🔴 | Authorization issue |
| No securities filings | 🟠 | Compliance gap |
| Conflicting MFN provisions | 🟠 | May affect new investment |

## Convertible Notes

### Standard Terms

**Principal Amount**
- Investment amount

**Interest Rate**
- Typically 2-8% annually
- Simple interest (not compound)
- Accrues until conversion

**Maturity Date**
- When note becomes due if not converted
- Typically 18-24 months
- Creates repayment obligation

**Conversion Terms**
- Qualified financing threshold
- Valuation cap
- Discount rate

### Conversion Mechanics

**At Qualified Financing:**
```
Conversion Price = Lower of:
  (a) Cap Price: Cap / Fully Diluted Shares
  (b) Discount Price: Round Price × (1 - Discount %)

Shares Issued = (Principal + Accrued Interest) / Conversion Price
```

**At Maturity (if not converted):**
- Repayment: Company must repay principal + interest
- Conversion: Convert at maturity cap (if specified)
- Extension: Parties agree to extend maturity

### Due Diligence Points

**Review each note for:**
1. Principal amount
2. Interest rate and accrual
3. Maturity date
4. Qualified financing threshold
5. Valuation cap
6. Discount rate
7. Conversion mechanics
8. Repayment terms
9. Security interest (if any)
10. Subordination provisions

### Red Flags in Convertible Notes

| Issue | Severity | Notes |
|-------|----------|-------|
| Maturity date passed/imminent | 🔴 | Creates repayment obligation |
| Secured notes | 🟠 | Liens on company assets |
| High interest rate (>8%) | 🟡 | Unusual; verify arms-length |
| Personal guarantees | 🟠 | Founder liability |
| No qualified financing threshold | 🟡 | Converts on any equity |
| Missing board/stockholder approval | 🔴 | Authorization issue |

## Cap Table Modeling

### Steps for Analysis

1. **List all convertible instruments**
   - SAFEs with terms
   - Convertible notes with terms
   - Calculate accrued interest on notes

2. **Determine conversion scenario**
   - Proposed round valuation
   - Pre-money or post-money basis

3. **Calculate conversion prices**
   - Apply caps and discounts
   - Determine which applies

4. **Model share issuances**
   - Shares to each holder
   - Dilution to existing stockholders

5. **Verify with company's model**
   - Compare results
   - Reconcile differences

### Sample Conversion Calculation

```
Given:
- Pre-money valuation: $8M
- SAFE: $200K at $6M post-money cap
- Note: $100K principal, 6% interest, 2 years, $5M cap, 20% discount
- Pre-financing fully diluted shares: 8,000,000

SAFE Conversion:
- Cap price: $6M / 8M shares = $0.75/share
- Shares: $200K / $0.75 = 266,667 shares

Note Conversion:
- Accrued interest: $100K × 6% × 2 = $12K
- Total converting: $112K
- Cap price: $5M / 8M = $0.625/share
- Discount price: ($8M / 8M) × 0.80 = $0.80/share
- Use cap price (lower): $0.625/share
- Shares: $112K / $0.625 = 179,200 shares
```

## Key Questions for Diligence

1. Are all SAFE/note terms accurately captured in cap table?
2. Is accrued interest on notes calculated correctly?
3. Are there any side letters or modifications?
4. Are any notes past maturity?
5. Are MFN provisions triggered by new investment?
6. What is total dilution from conversion?
7. Have all securities filings been made?
8. Is board/stockholder approval documented?
