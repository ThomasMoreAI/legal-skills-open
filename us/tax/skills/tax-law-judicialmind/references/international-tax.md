# International Tax Reference Guide

## Overview

The US international tax system is based on worldwide taxation of US persons (citizens, residents, domestic corporations) with foreign tax credits to mitigate double taxation. The Tax Cuts and Jobs Act (TCJA) of 2017 fundamentally restructured international tax rules.

---

## FUNDAMENTAL CONCEPTS

### Taxation Jurisdiction

**US Persons** (worldwide taxation):
- US citizens (regardless of residence)
- US resident aliens
- Domestic corporations
- Domestic partnerships, trusts, estates

**Foreign Persons** (source-based taxation):
- Nonresident aliens
- Foreign corporations
- Foreign partnerships, trusts, estates
- Taxed only on US-source income and ECI

### Source Rules (IRC §§ 861-865)

**Income Source Determination**:

| Income Type | Source Rule |
|-------------|-------------|
| Interest | Residence of payor |
| Dividends | Incorporation of payor |
| Personal services | Where performed |
| Rent/royalties | Where property used |
| Sale of inventory | Title passage (or allocation) |
| Sale of personal property | Residence of seller (generally) |
| Sale of real property | Location of property |

### Controlled Foreign Corporation (CFC)

**Definition** (IRC § 957):
- Foreign corporation
- More than 50% owned (by vote or value)
- By US shareholders (≥10% owners)

**US Shareholder** (IRC § 951(b)):
- US person owning ≥10% of combined voting power or value
- Constructive ownership rules apply (IRC § 958)

---

## SUBPART F INCOME (IRC §§ 951-965)

### Overview
Subpart F requires current US taxation of certain CFC income, regardless of distribution.

### Categories of Subpart F Income (IRC § 952)

**1. Insurance Income** (IRC § 953)
- Income from insuring risks outside CFC's country of organization
- Includes related person insurance income

**2. Foreign Base Company Income** (IRC § 954)

| Category | Description |
|----------|-------------|
| Foreign Personal Holding Company Income | Passive income (dividends, interest, rents, royalties, gains) |
| Foreign Base Company Sales Income | Sales involving related parties with manufacturing outside CFC's country |
| Foreign Base Company Services Income | Services performed for/on behalf of related party outside CFC's country |

### High-Tax Exception (IRC § 954(b)(4))
Income not treated as FBCI if:
- Subject to foreign tax > 90% of maximum US rate (18.9% for 2024)
- Election available

### Same Country Exception
Certain exceptions for activities within CFC's country of organization:
- Sales income from property manufactured in country
- Services performed in country

### Full Inclusion Rule
If Subpart F income + insurance income > 70% of gross income, entire gross income treated as Subpart F income.

### De Minimis Rule
No Subpart F income if:
- Total FBCI and insurance income < lesser of:
  - 5% of gross income, or
  - $1 million

---

## GLOBAL INTANGIBLE LOW-TAXED INCOME (GILTI)

### Overview (IRC § 951A)

GILTI requires US shareholders of CFCs to include "tested income" exceeding a routine return on tangible assets, regardless of distribution.

### GILTI Calculation

**Step 1: Net CFC Tested Income**
- Gross income less allocable deductions
- Excludes: Subpart F income, high-taxed income (with election), effectively connected income, dividends from related CFCs

**Step 2: Net Deemed Tangible Income Return (DTIR)**
- 10% of Qualified Business Asset Investment (QBAI)
- QBAI = adjusted basis of tangible depreciable property

**Step 3: GILTI Inclusion**
```
GILTI = Net CFC Tested Income - Net DTIR - Specified Interest Expense
```

### GILTI Deduction (IRC § 250)

**Domestic Corporation Deduction**:
- 50% of GILTI (through 2025)
- 37.5% of GILTI (after 2025)
- Results in effective tax rate of 10.5% (through 2025), 13.125% (after 2025)

**Individuals**: No § 250 deduction unless § 962 election made

### Section 962 Election
Allows individual US shareholders to:
- Be taxed at corporate rates on Subpart F/GILTI
- Claim § 250 deduction
- Claim indirect foreign tax credits
- Actual distribution still taxed (with basis adjustment)

### High-Tax Exclusion (IRC § 954(b)(4); Treas. Reg. § 1.951A-2(c)(7))
Election to exclude tested income subject to foreign tax > 18.9% (90% of 21%)

---

## FOREIGN-DERIVED INTANGIBLE INCOME (FDII)

### Overview (IRC § 250)

FDII provides a reduced US tax rate on income from serving foreign markets, creating incentive to locate intangible income in the US.

### FDII Calculation

**Step 1: Deduction Eligible Income (DEI)**
- Gross income less:
  - Subpart F/GILTI inclusions
  - Financial services income
  - Dividends from CFCs
  - Domestic oil and gas income
  - Foreign branch income

**Step 2: Deemed Intangible Income (DII)**
```
DII = DEI - (10% × QBAI)
```

**Step 3: Foreign-Derived Ratio**
```
Foreign-Derived Ratio = Foreign-Derived DEI / Total DEI
```

**Step 4: FDII**
```
FDII = DII × Foreign-Derived Ratio
```

### FDII Deduction
- 37.5% deduction (through 2025)
- 21.875% deduction (after 2025)
- Results in effective rate of 13.125% (through 2025), 16.406% (after 2025)

### Foreign-Derived DEI Requirements

**Sales of Property**:
- Sold to foreign person
- For foreign use

**Services**:
- Provided to person located outside US, OR
- With respect to property located outside US

---

## FOREIGN TAX CREDIT (IRC §§ 901-909)

### Overview
US persons may credit foreign income taxes paid against US tax liability to mitigate double taxation.

### Direct vs. Indirect Credits

**Direct Credit** (IRC § 901):
- Foreign taxes paid directly by taxpayer
- Individual or corporate taxpayers

**Deemed Paid Credit** (IRC § 960):
- Corporate shareholders of CFCs
- Based on Subpart F/GILTI inclusions
- 80% of foreign taxes on GILTI (IRC § 960(d))

### Foreign Tax Credit Limitation (IRC § 904)

```
FTC Limit = US Tax × (Foreign Source Taxable Income / Worldwide Taxable Income)
```

### Separate Limitation Categories (Baskets)

| Category | Description |
|----------|-------------|
| General | Active business income |
| Passive | Passive income (interest, dividends, rents, royalties) |
| GILTI | Global intangible low-taxed income |
| Foreign Branch | Income attributable to foreign branches |

### Carryback and Carryforward
- 1-year carryback
- 10-year carryforward
- By basket

### Foreign Tax Credit vs. Deduction
- Credit generally more valuable
- Deduction may be preferred if:
  - In excess credit position
  - Low foreign effective tax rate
  - Simplicity considerations

---

## TRANSFER PRICING (IRC § 482)

### Arm's Length Standard
Transactions between related parties must reflect prices that would be charged between unrelated parties in comparable circumstances.

### Transfer Pricing Methods

**Traditional Transaction Methods**:
1. **Comparable Uncontrolled Price (CUP)** - Direct comparison to uncontrolled transactions
2. **Resale Price Method** - Resale price less appropriate markup
3. **Cost Plus Method** - Cost plus appropriate markup

**Transactional Profit Methods**:
4. **Comparable Profits Method (CPM)** - Profit level indicators
5. **Profit Split Method** - Division of combined profits

### Best Method Rule
Select method that provides most reliable measure of arm's length result given facts and circumstances.

### Documentation Requirements (IRC § 6662(e))

**Contemporaneous Documentation**:
- Principal documents
- Background documents
- Required to avoid penalties

**Country-by-Country Reporting** (IRC § 6038A):
- Required for US parented MNE groups with revenue ≥ $850 million
- Form 8975
- Exchange with tax treaty partners

### Transfer Pricing Penalties

| Documentation | Penalty |
|--------------|---------|
| Contemporaneous documentation | 20% on underpayment |
| No documentation | 40% on underpayment |
| Gross valuation misstatement | 40% on underpayment |

### Advance Pricing Agreements (APAs)
- Unilateral, bilateral, or multilateral
- Prospective certainty
- 5-year term (typical)
- Rollback possibility

---

## TAX TREATIES

### Purpose
- Prevent double taxation
- Prevent fiscal evasion
- Reduce withholding taxes
- Resolve disputes

### Key Treaty Provisions

**Permanent Establishment (PE)**:
- Fixed place of business
- Dependent agent
- Triggers source country taxation

**Business Profits** (Article 7):
- Generally taxable only in residence country
- Unless attributable to PE in source country

**Dividends** (Article 10):
- Reduced withholding rates
- Typically 5% (direct investment) / 15% (portfolio)

**Interest** (Article 11):
- Reduced withholding rates
- Often 0% for certain interest

**Royalties** (Article 12):
- Reduced or eliminated withholding
- Often 0% in US treaties

**Capital Gains** (Article 13):
- Generally residence country taxation
- Exceptions for real property

### Treaty Benefits and Limitations

**Limitation on Benefits (LOB)**:
- Anti-treaty shopping provisions
- Tests: Publicly traded, ownership/base erosion, active trade or business, derivative benefits

**Principal Purpose Test (PPT)**:
- OECD MLI provision
- Benefits denied if principal purpose is obtaining treaty benefits

---

## PARTICIPATION EXEMPTION (IRC § 245A)

### Overview
100% dividends received deduction for foreign-source portion of dividends from specified 10%-owned foreign corporations.

### Requirements
- Domestic corporate shareholder
- 10% ownership (by vote or value)
- Foreign corporation not a PFIC
- 365-day holding period

### Limitations
- No deduction for hybrid dividends (IRC § 245A(e))
- Extraordinary disposition accounts (IRC § 245A(d))
- CFC holding period requirements

---

## ANTI-DEFERRAL REGIMES

### Passive Foreign Investment Company (PFIC)

**Definition** (IRC § 1297):
- 75% of income is passive (income test), OR
- 50% of assets produce passive income (asset test)

**Taxation Regimes**:
1. **Excess Distribution** (default) - Interest charge on deferred tax
2. **Qualified Electing Fund (QEF)** - Current inclusion of earnings
3. **Mark-to-Market** - Annual gain/loss recognition

### Comparison: CFC vs. PFIC

| Factor | CFC | PFIC |
|--------|-----|------|
| Ownership threshold | >50% by 10% US shareholders | Any US person |
| Income type | Subpart F, GILTI | Passive income focus |
| US shareholder | ≥10% owner | Any owner |
| Anti-deferral mechanism | Current inclusion | Excess distribution or election |
| Foreign tax credit | Available | Limited |

---

## REPORTING REQUIREMENTS

### Key Forms

| Form | Purpose | Filing Threshold |
|------|---------|------------------|
| Form 5471 | CFC reporting | 10% US shareholder |
| Form 8865 | Foreign partnership | 10% US partner |
| Form 8858 | Foreign disregarded entity | Owner of FDE |
| Form 926 | Transfers to foreign corps | Certain transfers |
| Form 8938 | FATCA reporting | Specified thresholds |
| FBAR (FinCEN 114) | Foreign bank accounts | $10,000 aggregate |
| Form 3520/3520-A | Foreign trusts/gifts | Various thresholds |
| Form 8975 | Country-by-country report | $850M revenue |

### Penalties for Non-Filing

| Form | Penalty |
|------|---------|
| Form 5471 | $10,000 per form per year |
| Form 8865 | $10,000 per form per year |
| Form 8938 | $10,000 + additional penalties |
| FBAR | Up to $100,000 or 50% of balance (willful) |

### Reasonable Cause Exception
Penalties may be waived for reasonable cause, but burden is on taxpayer.

---

## RECENT DEVELOPMENTS

### OECD Pillar Two (Global Minimum Tax)
- 15% minimum effective tax rate
- Qualified Domestic Minimum Top-up Tax (QDMTT)
- Income Inclusion Rule (IIR)
- Undertaxed Profits Rule (UTPR)
- US adoption under consideration

### Corporate Alternative Minimum Tax (CAMT)
- 15% minimum tax on adjusted financial statement income
- Applicable corporations (>$1 billion average AFSI)
- Foreign tax credit allowed

---

## KEY CITATIONS

- **Subpart F**: IRC §§ 951-965
- **GILTI**: IRC § 951A
- **FDII**: IRC § 250
- **Foreign Tax Credit**: IRC §§ 901-909
- **Transfer Pricing**: IRC § 482; Treas. Reg. § 1.482
- **PFIC**: IRC §§ 1291-1298
- **Treaties**: IRC § 894; specific treaties
- **Participation Exemption**: IRC § 245A

---

*Last Updated: March 2026*
*This reference is for informational purposes only and does not constitute legal advice.*
