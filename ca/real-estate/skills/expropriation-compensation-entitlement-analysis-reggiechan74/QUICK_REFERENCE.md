# Expropriation Compensation Calculator - Quick Reference

## Quick Start

```bash
# Run calculator
python expropriation_calculator.py sample_commercial_expropriation.json

# Specify output file
python expropriation_calculator.py input.json output.json
```

## Compensation Components

| Component | Section | Description | Notes |
|-----------|---------|-------------|-------|
| **Market Value** | s.13 OEA | Fair market value at valuation date | Highest and best use, NOT current use |
| **Moving Costs** | s.18 OEA | Relocation expenses | Reasonable costs only (mitigation duty) |
| **Business Losses** | s.18 OEA | Revenue losses during relocation | 6-12 month reasonable period |
| **Professional Fees** | s.18 OEA | Legal, appraisal, accounting | Reasonable rates required |
| **Temporary Accommodation** | s.18 OEA | Hotel/rental during transition | Apartment preferred over hotel |
| **Construction Impacts** | s.18(2)(a) | Temporary damages during construction | Lump-sum for construction period |
| **Permanent Impacts** | s.18(2)(b) | Ongoing damages from completed works | Capitalized value loss (before-after) |
| **Interest** | - | Pre-judgment interest | From valuation date to payment (3% annual) |

## NON-Compensable Items (s.18(3) OEA)

| Item | Reason | Alternative |
|------|--------|-------------|
| **Goodwill** | Intangible value | Owner can rebuild at new location |
| **Customer Base** | Part of goodwill | Re-establish through marketing |
| **Business Reputation** | Part of goodwill | Transferable to new location |
| **Special Purchaser Premium** | Unique to specific buyer | Not market value |
| **Ongoing Losses** | After reasonable relocation period | Owner's duty to rebuild business |

## Valuation Date Rules (s.13(2) OEA)

**Rule**: Earlier of Form 7 service OR plan registration

| Scenario | Form 7 Service | Plan Registration | Valuation Date |
|----------|----------------|-------------------|----------------|
| Form 7 first | Jan 15, 2024 | Feb 1, 2024 | **Jan 15, 2024** |
| Plan first | Jun 1, 2024 | May 15, 2024 | **May 15, 2024** |
| Same day | Mar 20, 2024 | Mar 20, 2024 | **Mar 20, 2024** |

## Highest and Best Use Examples

| Current Use | Zoning | Highest and Best Use | Compensable Value |
|-------------|--------|----------------------|-------------------|
| Farm ($10K/acre) | Industrial | Industrial development | **$120K/acre** (industrial) |
| Vacant lot | Commercial | Retail plaza | **Commercial value** |
| Illegal restaurant | Residential R2 | Single-family residential | **Residential only** (illegal use excluded) |
| Legal residential | Residential R2 | Single-family residential | **Residential value** |

## Legal Tests

### 1. But-For Test (Causation)

**Question**: "But for the expropriation, would owner have incurred this cost?"

| Cost | But-For Test Result | Compensable? |
|------|---------------------|--------------|
| Moving costs | Would NOT have moved | ✓ Yes |
| Planned renovation (independent) | Would have renovated anyway | ✗ No |
| Business relocation | Would NOT have relocated | ✓ Yes |
| Unrelated legal fees | Separate litigation | ✗ No |

### 2. Reasonableness Test (Mitigation Duty)

**Standard**: Owner must use reasonable, not gold-plated, solutions

| Expense | Claimed | Reasonable | Compensable |
|---------|---------|------------|-------------|
| Moving | $25K (premium service) | $8K-$12K (standard movers) | **$12K** (top of reasonable range) |
| Hotel | $200/night × 180 days | $2K/month apartment × 6 months | **$12K** (apartment - mitigation) |
| Legal fees | $80K (200 hrs × $400/hr) | $15K-$25K (routine matter) | **$25K** (reasonable) |

### 3. Foreseeability Test

**Standard**: More liberal than tort - broadly foreseeable consequences compensable

| Harm | Tort Foreseeability | Expropriation Foreseeability | Compensable? |
|------|---------------------|------------------------------|--------------|
| Elderly owner health decline | May not be specific enough | Broadly foreseeable | ✓ Yes (if causal) |
| Employee refuses relocation | Specific employee unknown | Employee turnover foreseeable | ✓ Yes |
| Property value decline | Foreseeable | Foreseeable | ✓ Yes |

## Business Losses Formula

### Revenue Loss During Reasonable Relocation Period

```
Compensable Business Loss = (Lost Revenue × Profit Margin) + Fixed Costs

Example:
- Monthly revenue: $50,000
- Profit margin: 20%
- Fixed costs: $15,000/month
- Relocation period: 6 months

Lost profit = $50,000 × 20% × 6 = $60,000
Fixed costs = $15,000 × 6 = $90,000
Total = $150,000 (compensable)
```

### Trade Fixtures (Depreciated Value)

```
Compensable Value = New Cost × (1 - Depreciation Rate)

Example:
- Equipment new cost: $150,000
- Age: 5 years
- Useful life: 15 years
- Depreciation: 5/15 = 33%

Compensable = $150,000 × 67% = $100,000
NOT salvage value (owner loses functional equipment)
```

## Interest Calculation

**Formula**: Principal × Rate × (Days ÷ 365)

**Current Ontario Rate**: 3.0% annual

| Principal | Days | Interest @ 3% |
|-----------|------|---------------|
| $100,000 | 365 | $3,000 |
| $500,000 | 180 | $7,397 |
| $1,000,000 | 366 (leap year) | $30,082 |
| $1,960,000 | 366 | $58,961 |

## Injurious Affection - Antrim Four-Part Test

**Required for s.18(2)(b) permanent use impacts**:

| Part | Test | Example (Highway Noise) | Result |
|------|------|-------------------------|--------|
| 1 | Authorized public work | Highway authorized by statute | ✓ Pass |
| 2 | Exercise of statutory powers | Noise from statutory highway operation | ✓ Pass |
| 3 | Diminished market value | Properties near highways sell 10-15% less | ✓ Pass |
| 4 | Special, not general | Property-specific (proximity) vs. general traffic congestion | ✓ Pass |

**Property-specific (Special) vs. General**:

| Impact | Classification | Compensable? |
|--------|----------------|--------------|
| Property loses direct highway access | Special (property-specific) | ✓ Yes |
| Highway traffic congestion increases | General (affects all drivers) | ✗ No |
| Noise impacts adjacent property | Special (proximity-based) | ✓ Yes |
| Public inconvenience during construction | General (everyone affected) | ✗ No |

## Construction vs. Permanent Impacts

| Impact Type | Section | Duration | Quantification | Example |
|-------------|---------|----------|----------------|---------|
| **Construction** | s.18(2)(a) | Temporary (6-18 months) | Lump-sum for period | Noise during pile driving |
| **Permanent** | s.18(2)(b) | Ongoing after completion | Capitalized value loss | Highway traffic noise 24/7 |

### Construction Impact Example

```
Rent reduction: $1,000/month
Construction period: 12 months
Compensation: $1,000 × 12 = $12,000 (lump-sum)
```

### Permanent Impact Example

```
Before value (quiet street): $650,000
After value (highway 100m away): $568,000 (12% reduction)
Permanent impact: $82,000 (capitalized permanent loss)

OR using income approach:
Annual impact: $2,000/year
Capitalization rate: 5%
Capitalized value: $2,000 ÷ 0.05 = $40,000
```

## Sample Results

### Commercial Expropriation (50 acres)

| Component | Amount |
|-----------|--------|
| Market value (highest and best use) | $1,500,000 |
| Moving and relocation | $36,000 |
| Business losses (6 months) | $260,000 |
| Professional fees | $50,000 |
| Temporary accommodation | $9,000 |
| Construction impacts (12 months) | $20,000 |
| Permanent impacts (noise, visual) | $85,000 |
| **Subtotal** | **$1,960,000** |
| Interest (366 days @ 3%) | $58,961 |
| **TOTAL COMPENSATION** | **$2,018,961** |
| | |
| **NON-Compensable** | |
| Special purchaser premium | ($250,000) |
| Goodwill | ($150,000) |

### Residential Expropriation (0.25 acre)

| Component | Amount |
|-----------|--------|
| Market value | $850,000 |
| Moving and relocation | $18,500 |
| Professional fees | $28,000 |
| Temporary accommodation (4 months) | $10,000 |
| Construction impacts (18 months) | $11,000 |
| Permanent impacts (noise, privacy) | $100,000 |
| **Subtotal** | **$1,017,500** |
| Interest (270 days @ 3%) | $22,580 |
| **TOTAL COMPENSATION** | **$1,040,080** |

## Common Errors to Avoid

| Error | Correction |
|-------|-----------|
| Using current use instead of highest and best use | Value at zoning-permitted optimal use |
| Including special purchaser premium | Exclude - not market value |
| Claiming ongoing business losses | Limit to reasonable relocation period (6-12 months) |
| Including goodwill | NON-compensable under s.18(3) - intangible |
| Gold-plated moving costs | Reasonable costs only (mitigation duty) |
| Forgetting interest | Include from valuation date to payment |
| Wrong valuation date | MUST be earlier of Form 7 or plan registration |
| Temporary vs. permanent impacts | Temporary = lump-sum; Permanent = capitalized |

## Files in This Directory

| File | Description |
|------|-------------|
| `expropriation_calculator.py` | Main calculator (Python) |
| `sample_commercial_expropriation.json` | Commercial property with business losses |
| `sample_residential_expropriation.json` | Residential property (no business) |
| `README.md` | Complete documentation |
| `QUICK_REFERENCE.md` | This file - quick reference guide |
| `SKILL.md` | Legal framework skill (detailed analysis) |

## Legal Framework Summary

**Ontario Expropriations Act, R.S.O. 1990, c. E.26**

- **s.13**: Market value at highest and best use
- **s.13(2)**: Valuation date = earlier of Form 7 or plan registration
- **s.18**: Disturbance damages (but-for, reasonableness, foreseeability)
- **s.18(2)(a)**: Construction impacts (temporary)
- **s.18(2)(b)**: Permanent use impacts (Antrim test)
- **s.18(3)**: Goodwill and intangibles NON-compensable

**Key Case**: *Antrim Truck Centre Ltd. v. Ontario (Transportation)*, 2005 SCC 31 (four-part test)

---

**Version**: 1.0.0
**Date**: 2025-11-15
**Author**: Claude Code
