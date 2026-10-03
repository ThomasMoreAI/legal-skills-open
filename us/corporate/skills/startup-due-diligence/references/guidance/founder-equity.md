# Founder Equity & Vesting Guide

## Founder Stock Basics

### Standard Structure

**Typical founder equity at formation:**
- Common stock (not preferred)
- Subject to vesting
- Subject to company repurchase right
- 83(b) election filed

### Initial Issuance

**Stock Purchase Agreement should include:**
- Number of shares
- Purchase price (typically nominal: $0.0001/share)
- Vesting schedule
- Repurchase right
- Transfer restrictions
- 83(b) election acknowledgment

## Vesting

### Standard Vesting Terms

| Element | Standard | Variations |
|---------|----------|------------|
| Total period | 4 years | 3-5 years |
| Cliff | 1 year | 6 months, none |
| Post-cliff vesting | Monthly | Quarterly |
| Acceleration | Single or double trigger | None |

### Vesting Schedule Example

```
Total shares: 1,000,000
Vesting: 4-year, 1-year cliff, monthly thereafter

Month 0:  0 vested (0%)
Month 12: 250,000 vested (25%) - cliff
Month 13: 270,833 vested (27.08%)
Month 24: 500,000 vested (50%)
Month 36: 750,000 vested (75%)
Month 48: 1,000,000 vested (100%)
```

### Acceleration Provisions

**Single Trigger**
- Acceleration on change of control alone
- Less common for founders
- May deter acquirers

**Double Trigger**
- Requires: (1) Change of control + (2) Termination
- More investor-friendly
- Standard for executives

**Typical acceleration amounts:**
- 25-100% of unvested shares
- 6-24 months of accelerated vesting

## 83(b) Election

### What It Is

An 83(b) election allows the recipient of restricted stock to be taxed on the value of the stock at grant (when value is low) rather than at vesting (when value may be much higher).

### Critical Requirements

| Requirement | Detail |
|-------------|--------|
| Filing deadline | Within 30 days of grant |
| Where to file | IRS Service Center |
| What to file | Signed 83(b) election |
| Copy required | Keep copy; send to employer |

**CANNOT BE FIXED IF MISSED**

### Tax Implications

**With 83(b) election:**
```
At grant: Pay tax on (FMV - purchase price) × shares
         Typically minimal if filed early
At sale:  Pay capital gains tax on appreciation
```

**Without 83(b) election:**
```
At each vest: Pay ordinary income tax on (FMV - purchase price) × vested shares
              Potentially significant as company grows
At sale:      Pay capital gains on post-vesting appreciation only
```

### Example

```
Founder receives 1M shares at $0.0001/share
FMV at grant: $0.001/share
FMV at full vest (4 years): $1.00/share

WITH 83(b):
- Tax at grant: ($0.001 - $0.0001) × 1M = $900 ordinary income
- Tax at sale ($5/share): ($5 - $0.001) × 1M = ~$5M long-term capital gains

WITHOUT 83(b):
- Tax at vesting: ($1.00 - $0.0001) × 1M = ~$1M ordinary income
- Tax at sale: ($5 - $1) × 1M = $4M capital gains
- Plus: Taxed quarterly as shares vest at increasing values
```

## Repurchase Rights

### How They Work

Company has right to repurchase unvested shares upon termination:
- Purchase price: Original purchase price (or lower of cost/FMV)
- Exercise period: Typically 90 days after termination
- Automatic on termination for cause

### Lapse Schedule

Repurchase rights lapse as shares vest:
```
Unvested shares = subject to repurchase
Vested shares = no longer subject to repurchase
```

## Due Diligence Checklist

### For Each Founder

- [ ] Stock purchase agreement executed
- [ ] Purchase price paid
- [ ] 83(b) election filed (with proof)
- [ ] Vesting schedule documented
- [ ] Current vesting status calculated
- [ ] Acceleration provisions reviewed

### Red Flags

| Issue | Severity | Notes |
|-------|----------|-------|
| No 83(b) election | 🔴 CRITICAL | Cannot fix; major tax issue |
| No vesting | 🟠 MATERIAL | Investors will require |
| Fully vested day 1 | 🟠 MATERIAL | May need re-vesting |
| Inconsistent founder terms | 🟡 MINOR | Understand rationale |
| Missing stock purchase agreement | 🟠 MATERIAL | Document retroactively |
| Unclear repurchase terms | 🟡 MINOR | Clarify in agreement |

## Common Scenarios

### Founder Departure

**Vested shares:** Founder keeps
**Unvested shares:** Company repurchases at original price

**Important considerations:**
- Post-termination exercise period (if options)
- Non-compete obligations
- IP assignment confirmation
- Release of claims

### Adding New Co-Founder

**Typical terms:**
- Separate vesting from beginning
- May be different from original founders
- Consider contribution to date
- Cliff protects against quick departure

### Investor Requirements at Financing

**Common asks:**
- Founder re-vesting (if not vesting)
- Extended vesting period
- Modified acceleration terms
- Additional equity grants to key employees

## Questions for Diligence

1. Do all founders have signed stock purchase agreements?
2. Is there proof of 83(b) filings for each founder?
3. Were 83(b) elections filed within 30 days?
4. What are the vesting terms for each founder?
5. Are any founders fully vested already?
6. Is vesting consistent among founders?
7. Are there acceleration provisions?
8. Have any founders departed, and how was that handled?
9. Are repurchase rights properly documented?
10. Is payment for stock documented?
