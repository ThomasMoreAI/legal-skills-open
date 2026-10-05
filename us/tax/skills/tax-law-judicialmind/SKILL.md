---
name: tax-law-judicialmind
title: Tax Law
description: Tax law skill for tax compliance, planning, and disputes. Use when the user needs assistance with federal or state taxes, tax planning, IRS matters, tax structuring, corporate taxes, or international tax. Triggers on keywords like "tax", "IRS", "income tax", "corporate tax", "tax planning", "deduction", "tax credit", "1031 exchange", "transfer pricing", "SALT", "tax audit".
author: judicialmind
author_url: https://github.com/judicialmind/legal-skills/tree/main/skills/tax-law
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: tax
language: en
sources:
- title: Audit Defense
  path: references/audit-defense.md
- title: Entity Selection
  path: references/entity-selection.md
- title: International Tax
  path: references/international-tax.md
---

# Tax Law

This skill provides expert guidance for tax compliance, planning, and controversy matters.

## Core Capabilities

### 1. Tax Compliance
- Federal and state filing requirements
- Corporate, partnership, and individual returns
- Employment taxes
- Sales and use tax

### 2. Tax Planning
- Entity selection
- Transaction structuring
- Compensation planning
- Estate and gift planning

### 3. Tax Controversy
- Audit representation
- Appeals
- Tax court litigation
- Penalty abatement

### 4. International Tax
- Cross-border transactions
- Transfer pricing
- FATCA/CRS compliance
- Treaty planning

## Entity Taxation Overview

### Entity Selection Tax Comparison

| Entity | Tax Treatment | SE Tax | Losses | Income Splitting |
|--------|--------------|--------|--------|-----------------|
| Sole Proprietorship | Pass-through | Yes | Deductible | No |
| Partnership/LLC | Pass-through | Yes (active) | K-1 to partners | Yes |
| S Corporation | Pass-through | No on distributions | K-1 to shareholders | Limited |
| C Corporation | Double taxation | No | Trapped in corp | N/A |

### C Corporation Tax Rates (2024)
- Flat 21% federal corporate rate
- State taxes vary (0% to ~12%)

### Individual Tax Rates (2024)
| Rate | Single | MFJ |
|------|--------|-----|
| 10% | $0-$11,600 | $0-$23,200 |
| 12% | $11,601-$47,150 | $23,201-$94,300 |
| 22% | $47,151-$100,525 | $94,301-$201,050 |
| 24% | $100,526-$191,950 | $201,051-$383,900 |
| 32% | $191,951-$243,725 | $383,901-$487,450 |
| 35% | $243,726-$609,350 | $487,451-$731,200 |
| 37% | Over $609,350 | Over $731,200 |

### Pass-Through Deduction (§199A)
- 20% deduction for qualified business income
- Subject to W-2 wage/property limitations at higher incomes
- Specified service trades excluded at higher incomes
- Phase-out: $191,950 single / $383,900 MFJ (2024)

## Corporate Tax Issues

### M&A Tax Structuring

| Structure | Tax to Seller | Tax to Buyer |
|-----------|--------------|--------------|
| Stock sale | Capital gains | Carryover basis |
| Asset sale | Ordinary + capital | Stepped-up basis |
| 338(h)(10) | Treated as asset sale | Stepped-up basis |
| Type A Merger | Tax-free (if qualified) | Carryover basis |
| Type B Stock-for-Stock | Tax-free (if qualified) | Carryover basis |
| Type C Assets-for-Stock | Tax-free (if qualified) | Carryover basis |

### Tax-Free Reorganization Requirements
- Business purpose
- Continuity of business enterprise
- Continuity of shareholder interest (varies by type)
- Step transaction doctrine considerations

### Net Operating Losses
- Post-2017 NOLs: 80% of taxable income limitation
- Indefinite carryforward (no carryback except farms/insurance)
- §382 limitations on change of ownership

## Employment Tax

### Payroll Tax Rates (2024)
| Tax | Employee | Employer | Wage Base |
|-----|----------|----------|-----------|
| Social Security | 6.2% | 6.2% | $168,600 |
| Medicare | 1.45% | 1.45% | Unlimited |
| Additional Medicare | 0.9% | - | $200,000/$250,000 |
| FUTA | - | 0.6% | $7,000 |

### Worker Classification
**Employee vs. Independent Contractor** (IRS factors):
1. Behavioral control
2. Financial control
3. Relationship type

**Consequences of Misclassification**:
- Back employment taxes
- Penalties and interest
- Benefit plan issues
- State unemployment taxes
- Workers' compensation

## Sales and Use Tax

### Nexus After *Wayfair* (2018)
- Physical presence not required
- Economic nexus thresholds (typically $100K sales or 200 transactions)
- Marketplace facilitator laws

### Common Exemptions
- Resale
- Manufacturing equipment
- Certain services
- Food (varies by state)
- Nonprofits (varies)

## International Tax

### US International Tax Framework

**Outbound** (US companies investing abroad):
- Worldwide taxation with foreign tax credit
- GILTI (Global Intangible Low-Taxed Income)
- Subpart F income
- BEAT (Base Erosion and Anti-Abuse Tax)
- FDII (Foreign-Derived Intangible Income deduction)

**Inbound** (Foreign companies in US):
- ECI (Effectively Connected Income) taxed at regular rates
- FDAP (Fixed, Determinable, Annual, Periodical) income subject to withholding
- FIRPTA (Foreign Investment in Real Property Tax Act)
- Branch profits tax

### Transfer Pricing
**Methods**:
1. Comparable Uncontrolled Price (CUP)
2. Resale Price Method
3. Cost Plus Method
4. Comparable Profits Method (CPM)
5. Profit Split Method

**Documentation Requirements**:
- §6662(e) penalty avoidance
- Country-by-country reporting (large MNEs)
- Master file and local file

### Tax Treaties
**Common Benefits**:
- Reduced withholding rates
- Permanent establishment threshold
- Tie-breaker rules for residence
- Limitation on benefits

## Tax Controversy

### Audit Process
```
Correspondence Audit → Examination (Field/Office) →
30-Day Letter → Appeals Conference →
90-Day Letter → Tax Court Petition or Pay and Sue
```

### Penalty Abatement

**Reasonable Cause Factors**:
- Ordinary business care and prudence
- Reliance on professional advice
- First-time abatement (clean compliance history)
- Undue hardship
- Ignorance of law (limited circumstances)

**Common Penalties**:
| Penalty | Rate | Code Section |
|---------|------|--------------|
| Failure to file | 5%/month, max 25% | §6651(a)(1) |
| Failure to pay | 0.5%/month, max 25% | §6651(a)(2) |
| Accuracy-related | 20% | §6662 |
| Fraud | 75% | §6663 |
| Substantial understatement | 20% | §6662(d) |

### Statute of Limitations
| Situation | Period |
|-----------|--------|
| General | 3 years from filing |
| >25% omission | 6 years |
| Fraud | Unlimited |
| No return filed | Unlimited |

## Common Planning Strategies

### Individual
- Retirement account contributions (401k, IRA)
- Health Savings Account (HSA)
- Charitable giving strategies
- Capital loss harvesting
- Timing of income/deductions
- Qualified Opportunity Zone investments

### Business
- Entity selection optimization
- Timing of asset purchases (§179, bonus depreciation)
- R&D tax credits
- Work Opportunity Tax Credit
- State tax incentives
- Cost segregation studies

### Real Estate
- 1031 like-kind exchanges
- Opportunity Zones
- Depreciation strategies
- Passive activity loss planning
- REIT structures

## Key Tax Resources

| Source | Content | URL |
|--------|---------|-----|
| IRS.gov | Official guidance, forms | irs.gov |
| Tax Court | Opinions, rules | ustaxcourt.gov |
| Treasury | Regulations, treaties | treasury.gov |
| Tax Notes | News, analysis | taxnotes.com |
| BNA/Bloomberg Tax | Research platform | bloombergtax.com |

## Integration with Other Skills

- **corporate-ma**: Transaction tax structuring
- **legal-research**: Tax authority research
- **compliance-tracking**: Tax compliance monitoring
- **international-arbitration**: Tax treaty disputes
- **bankruptcy**: Tax claims in bankruptcy

## Reference Files

For detailed guidance:
- `references/entity-selection.md` - Entity comparison analysis
- `references/audit-defense.md` - IRS audit procedures
- `references/international-tax.md` - Cross-border planning
