# Entity Selection Tax Analysis Reference Guide

## Overview

Entity selection is one of the most important tax planning decisions for a business. The choice affects income taxation, employment taxes, liability protection, and operational flexibility. This guide analyzes the tax implications of major entity types.

---

## ENTITY TYPES COMPARISON

### Summary Table

| Factor | C Corporation | S Corporation | Partnership | LLC (Default) | Sole Proprietorship |
|--------|--------------|---------------|-------------|---------------|---------------------|
| Federal Tax | Entity level | Pass-through | Pass-through | Pass-through | Pass-through |
| Self-Employment Tax | No (wages subject to FICA) | Reasonable salary subject | Generally yes | Generally yes | Yes |
| Liability Protection | Yes | Yes | Limited partners only | Yes | No |
| Number of Owners | Unlimited | Max 100, restrictions | Unlimited | Unlimited | 1 |
| Owner Types | Any | US individuals, estates, trusts | Any | Any | Individual |
| Allocation Flexibility | Pro rata by shares | Pro rata by shares | Flexible | Flexible | N/A |
| Formation Complexity | Moderate | Moderate | Low-Moderate | Low | None |

---

## C CORPORATION

### Tax Characteristics

**IRC Subchapter C** (§§ 301-385)

**Federal Income Tax**:
- Flat 21% corporate tax rate (IRC § 11)
- Taxed at entity level
- Dividends taxed again to shareholders (double taxation)

**Qualified Dividends**:
- 0%/15%/20% rate for individual shareholders
- Must meet holding period requirements
- Additional 3.8% NIIT may apply

### Double Taxation Analysis

**Example**: $1,000,000 corporate income

| Layer | Amount | Rate | Tax |
|-------|--------|------|-----|
| Corporate Tax | $1,000,000 | 21% | $210,000 |
| Dividend Distribution | $790,000 | 23.8%* | $188,020 |
| **Total Tax** | | | **$398,020** |
| **Combined Rate** | | | **39.8%** |

*Assumes top individual rate (20% + 3.8% NIIT)

### Advantages

**Qualified Small Business Stock (QSBS)** (IRC § 1202):
- Exclusion of gain on sale of QSBS
- 100% exclusion for stock acquired after 9/27/2010
- Requirements:
  - C corporation
  - Gross assets ≤ $50 million
  - Active business requirement
  - 5-year holding period
  - Original issue stock

**Section 1244 Stock**:
- Ordinary loss treatment (up to $50,000/$100,000 MFJ)
- Small business corporation
- Original issue stock

**Fringe Benefits**:
- 100% deductible health insurance
- Group term life insurance
- Dependent care assistance
- Educational assistance

**Income Retention**:
- Retain earnings at 21% rate
- Accumulated earnings tax risk (IRC § 531)
- Personal holding company risk (IRC § 541)

### Disadvantages

**Double Taxation**:
- Corporate level tax on income
- Shareholder level tax on distributions
- Higher combined rate than pass-through

**Limited Loss Utilization**:
- Corporate losses trapped at entity level
- Cannot pass through to shareholders
- Carryforward rules apply (IRC § 172)

---

## S CORPORATION

### Tax Characteristics

**IRC Subchapter S** (§§ 1361-1379)

**Pass-Through Taxation**:
- No entity-level federal tax (generally)
- Income/loss passes through to shareholders
- Items retain character (ordinary, capital, etc.)
- Reported on Schedule K-1

### Eligibility Requirements (IRC § 1361(b))

| Requirement | Rule |
|-------------|------|
| Number of shareholders | Maximum 100 |
| Shareholder types | US individuals, estates, certain trusts |
| Stock classes | One class only (voting differences OK) |
| Entity type | Domestic corporation |
| Ineligible corporations | Banks (certain), insurance companies, DISCs, certain affiliated groups |

### Built-In Gains Tax (IRC § 1374)

Applies when:
- C corporation converts to S corporation
- Has built-in gains at conversion
- Sells assets within recognition period (5 years)

Tax: 21% on recognized built-in gains

### Passive Investment Income Tax (IRC § 1375)

Applies when:
- S corporation has C corporation E&P
- Passive investment income > 25% of gross receipts

Tax: 35% on excess net passive income

**Termination Risk**: If excess passive income for 3 consecutive years

### Reasonable Compensation Requirement

**IRS Focus Area**:
- Shareholder-employees must receive reasonable compensation
- Wages subject to FICA (15.3% combined)
- Distributions not subject to employment taxes
- Aggressive salary minimization scrutinized

**Factors for Reasonable Compensation**:
- Duties and responsibilities
- Time and effort devoted
- Comparable salaries
- Dividend history
- Company profitability
- Employee qualifications

### S Corporation vs. Partnership

| Factor | S Corporation | Partnership |
|--------|---------------|-------------|
| Self-employment tax | Only on wages | Distributive share (generally) |
| Basis from debt | Shareholder loans only | All entity debt (partner share) |
| Special allocations | Not permitted | Permitted (substantial economic effect) |
| Fringe benefits | Limited for >2% shareholders | Limited for partners |
| State taxation | May have entity-level tax | Usually pass-through |

---

## PARTNERSHIP

### Tax Characteristics

**IRC Subchapter K** (§§ 701-777)

**Pass-Through Taxation**:
- No entity-level federal tax
- Income/loss passes through to partners
- Items retain character
- Reported on Schedule K-1

### Formation (IRC § 721)

**General Rule**: No gain/loss recognized on contribution of property in exchange for partnership interest

**Exceptions**:
- Services contribution (taxable to service partner)
- Disguised sales (IRC § 707(a)(2)(B))
- Liabilities in excess of basis

### Allocation Rules (IRC § 704)

**Substantial Economic Effect**:
- Partners' agreement must have economic effect
- Effect must be substantial
- Must follow capital account rules

**Special Allocations Permitted**:
- Income/loss allocations
- Specific item allocations
- Retroactive allocations (with limits)

**Section 704(c)**: Built-in gain/loss allocated to contributing partner

### Distribution Rules

**Current Distributions** (IRC § 731):
- Generally no gain recognition
- Basis reduction
- Gain if cash exceeds basis

**Liquidating Distributions** (IRC § 731, 732):
- Basis equals outside basis
- Gain/loss recognition possible
- Character rules apply

### Partner's Basis (IRC § 705)

**Increases**:
- Capital contributions
- Share of income
- Share of tax-exempt income
- Increase in share of liabilities

**Decreases**:
- Distributions
- Share of losses
- Share of nondeductible expenses
- Decrease in share of liabilities

### Self-Employment Tax

**General Partners**:
- Distributive share generally subject to SE tax
- IRC § 1402(a)

**Limited Partners**:
- Distributive share generally NOT subject to SE tax
- Exception for guaranteed payments for services
- IRC § 1402(a)(13)

**LLC Members**:
- Fact-intensive analysis
- IRS proposed regulations (withdrawn)
- Material participation test commonly applied

---

## LIMITED LIABILITY COMPANY (LLC)

### Federal Tax Classification

**Default Classification** (Check-the-Box, Treas. Reg. § 301.7701-3):

| LLC Type | Default Classification |
|----------|----------------------|
| Single-member | Disregarded entity (sole proprietorship) |
| Multi-member | Partnership |

**Elective Classification**:
- Form 8832 to elect corporation treatment
- Form 2553 to elect S corporation treatment (if eligible)

### Single-Member LLC (SMLLC)

**Disregarded Entity**:
- Reported on owner's return (Schedule C for individual)
- Self-employment tax on net earnings
- No separate return required (federal)
- State treatment varies

**Advantages**:
- Liability protection
- Tax simplicity
- No double taxation

### Multi-Member LLC

**Partnership Default**:
- Partnership tax rules apply
- Schedule K-1 reporting
- SE tax analysis required

**Election Options**:
- Elect C corporation status (Form 8832)
- Elect S corporation status (Forms 8832 + 2553)

### LLC Operating Agreement Tax Provisions

**Key Tax Clauses**:
- Allocation of income/loss
- Distribution waterfall
- Tax matters partner/partnership representative
- Tax distribution provisions
- Built-in gain/loss allocations
- Section 754 elections

---

## QUALIFIED BUSINESS INCOME DEDUCTION (IRC § 199A)

### Overview

**20% Deduction** for qualified business income from:
- Sole proprietorships
- Partnerships
- S corporations
- Certain trusts and estates

### Limitations

**Taxable Income Thresholds** (2024):

| Filing Status | Threshold | Phase-In Range |
|--------------|-----------|----------------|
| Single | $182,100 | $182,100 - $232,100 |
| MFJ | $364,200 | $364,200 - $464,200 |

**W-2 Wage/UBIA Limitation** (above threshold):
Greater of:
- 50% of W-2 wages, OR
- 25% of W-2 wages + 2.5% of UBIA of qualified property

### Specified Service Trade or Business (SSTB)

**Excluded Fields** (for taxpayers above threshold):
- Health
- Law
- Accounting
- Actuarial science
- Performing arts
- Consulting
- Athletics
- Financial services
- Brokerage services
- Investment management
- Trading
- Any business where principal asset is reputation/skill of owners

**Exception**: Engineering and architecture are NOT SSTBs

---

## ENTITY SELECTION DECISION MATRIX

### Key Questions

1. **Number and type of owners?**
   - Multiple classes of equity → C Corp
   - Foreign investors → Partnership or C Corp
   - Institutional investors → Often prefer pass-through

2. **Anticipated losses?**
   - Losses valuable to owners → Pass-through
   - Expected profitability → Consider all options

3. **Exit strategy?**
   - IPO planned → C Corp (typically)
   - Sale to strategic → Consider QSBS for C Corp
   - Long-term hold → Pass-through often preferred

4. **State tax considerations?**
   - Entity-level state taxes
   - Composite return requirements
   - Withholding for nonresidents

5. **Employment tax optimization?**
   - Reasonable salary + distributions → S Corp
   - Maximize QBI deduction → Consider W-2 limitations

### Comparative Tax Analysis Example

**Scenario**: $500,000 net business income, single owner, all distributed

| Factor | C Corp | S Corp | SMLLC |
|--------|--------|--------|-------|
| Entity tax | $105,000 | $0 | $0 |
| Salary/SE income | $150,000* | $150,000* | $500,000 |
| FICA (employer+employee) | $18,578 | $18,578 | $22,899** |
| Dividend/distribution | $245,000 | $350,000 | $0 |
| Dividend tax | $58,310 | $0 | $0 |
| Ordinary tax (after SE ded) | $32,676 | $74,844 | $140,538*** |
| QBI deduction benefit | $0 | ($16,996) | ($18,246) |
| **Total Tax** | **$214,564** | **$76,426** | **$145,191** |

*Assumed reasonable salary
**SE tax (12.4% on $160,200 + 2.9% on all)
***Before QBI deduction

**Note**: Actual calculations vary based on individual circumstances, state taxes, and other factors.

---

## CONVERSION CONSIDERATIONS

### C Corp to S Corp
- S election effective prospectively
- Built-in gains tax applies (5-year recognition period)
- Accumulated E&P issues
- LIFO recapture

### Partnership to Corporation
- Generally tax-free under IRC § 351
- May trigger gain in certain circumstances
- Debt relief issues

### Corporation to Partnership
- Taxable liquidation
- Gain recognition at corporate and shareholder levels
- Consider alternatives (F reorganization, QSub)

---

## KEY CITATIONS

- **C Corporations**: IRC §§ 301-385
- **S Corporations**: IRC §§ 1361-1379
- **Partnerships**: IRC §§ 701-777
- **Classification**: Treas. Reg. § 301.7701-1 through -3
- **QBI Deduction**: IRC § 199A; Treas. Reg. § 1.199A
- **Self-Employment**: IRC § 1402
- **QSBS**: IRC § 1202

---

*Last Updated: March 2026*
*This reference is for informational purposes only and does not constitute legal advice.*
