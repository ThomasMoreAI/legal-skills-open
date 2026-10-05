---
name: bankruptcy-judicialmind
title: Bankruptcy Law
description: Bankruptcy law skill for insolvency and debt restructuring matters. Use when the user needs assistance with Chapter 7, Chapter 11, Chapter 13, creditor rights, preference actions, or bankruptcy litigation. Triggers on keywords like "bankruptcy", "Chapter 7", "Chapter 11", "Chapter 13", "insolvency", "creditor", "debtor", "discharge", "reorganization", "automatic stay", "proof of claim", "preference".
author: judicialmind
author_url: https://github.com/judicialmind/legal-skills/tree/main/skills/bankruptcy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: bankruptcy
language: en
sources:
- title: Claims Guide
  path: references/claims-guide.md
---

# Bankruptcy Law

This skill provides expert guidance for bankruptcy proceedings, restructuring, and creditor rights.

## Core Capabilities

### 1. Debtor Representation
- Chapter 7 liquidation
- Chapter 11 reorganization
- Chapter 13 wage earner
- Asset protection planning

### 2. Creditor Representation
- Proof of claim filing
- Adequate protection
- Relief from stay motions
- Preference/fraudulent transfer defense

### 3. Business Restructuring
- Pre-bankruptcy planning
- DIP financing
- Sale transactions (§363)
- Plan confirmation

### 4. Bankruptcy Litigation
- Adversary proceedings
- Contested matters
- Appeals
- Non-dischargeability actions

## Chapter Comparison

| Feature | Chapter 7 | Chapter 11 | Chapter 13 |
|---------|-----------|------------|------------|
| **Purpose** | Liquidation | Reorganization | Wage earner plan |
| **Who** | Individuals, businesses | Any debtor | Individuals with regular income |
| **Debt Limits** | None | None | $2.75M total (2024) |
| **Trustee** | Yes (liquidating) | Usually debtor-in-possession | Yes (standing) |
| **Duration** | 3-6 months | 1-3+ years | 3-5 years |
| **Asset disposition** | Non-exempt liquidated | Retained, reorganized | Retained |
| **Discharge** | Most debts | Per plan | Per plan |

## Chapter 7 Liquidation

### Eligibility (Means Test)
```
1. Calculate Current Monthly Income (CMI)
   - Average income for 6 months before filing
   - Compare to state median income

2. If above median, apply means test:
   - Deduct allowed expenses (IRS standards + actual)
   - Calculate disposable income
   - If disposable income too high, presumption of abuse
```

### Exemptions
**Federal vs. State**: Debtor may choose federal exemptions if state allows

**Common Federal Exemptions** (11 U.S.C. §522(d)):
| Property | Amount (2024) |
|----------|---------------|
| Homestead | $27,900 |
| Motor vehicle | $4,450 |
| Household goods | $14,875 aggregate |
| Jewelry | $1,875 |
| Wildcard | $1,475 + $13,950 unused homestead |
| Tools of trade | $2,800 |
| Retirement accounts | Generally unlimited |

### Chapter 7 Timeline
```
Filing → Automatic Stay → 341 Meeting (21-40 days) →
Deadline for Objections (60 days after 341) →
Trustee Report of No Distribution (or asset case) →
Discharge (60 days after 341) → Case Closed
```

## Chapter 11 Reorganization

### Key Features
- Debtor-in-possession (DIP) continues operations
- Automatic stay protects debtor
- Exclusivity period to propose plan
- Creditor committees may be appointed
- Disclosure statement required before solicitation

### Chapter 11 Timeline
```
Filing → First Day Motions → DIP Financing →
341 Meeting → Claims Bar Date →
Disclosure Statement → Plan Confirmation →
Effective Date → Emergence
```

### First Day Motions (Common)
- Cash collateral use
- DIP financing
- Payment of critical vendors
- Employee wage payment
- Utility adequate assurance
- Joint administration
- Rejection of executory contracts

### Plan Confirmation Requirements
1. **Best interests test**: Creditors receive at least as much as Chapter 7
2. **Feasibility**: Debtor can make plan payments
3. **Good faith**: Plan proposed in good faith
4. **Acceptance**: Requisite votes obtained
5. **Priority claims paid**: Unless claimant agrees otherwise

### Classification and Voting
- Claims grouped by substantially similar legal rights
- Class accepts if:
  - Over 1/2 in number vote yes, AND
  - Over 2/3 in amount vote yes
- Cramdown available if at least one impaired class accepts

### Cramdown Requirements (§1129(b))
- Plan does not discriminate unfairly
- Plan is fair and equitable:
  - Secured claims: Retain lien, receive present value
  - Unsecured claims: Either paid in full OR no junior class receives anything (absolute priority rule)

## Chapter 13 Wage Earner

### Eligibility Requirements
- Individual with regular income
- Secured debt under $2,750,000 (2024)
- Unsecured debt under $2,750,000 (2024)
- Current on tax filings

### Plan Requirements
- 3-5 years depending on income
- Priority claims paid in full
- Secured claims: Adequate protection
- Unsecured claims: Best interests and projected disposable income

### Chapter 13 Plan Contents
```
1. Payment terms (amount, duration)
2. Treatment of secured claims
3. Treatment of priority claims
4. Treatment of unsecured claims
5. Adequate protection payments
6. Executory contract treatment
7. Property to surrender
```

### Chapter 13 Discharge
**Debts discharged**: Most unsecured debts after plan completion
**Hardship discharge**: Available if completion impossible through no fault of debtor

## Automatic Stay (§362)

### Stay Prohibits
- Collection actions
- Enforcement of judgments
- Creation/perfection of liens
- Setoff
- Litigation commencement/continuation

### Stay Exceptions (§362(b))
- Criminal proceedings
- Domestic support obligations
- Police power actions
- Certain tax proceedings
- Pension loan repayments

### Relief from Stay (§362(d))
**Grounds**:
1. For cause (including lack of adequate protection)
2. No equity and property not necessary for reorganization
3. Single-asset real estate cases

**Motion Process**:
- 30-day deadline for preliminary hearing
- Burden shifting depends on ground

## Preferences and Fraudulent Transfers

### Preference Elements (§547)
1. Transfer of property
2. To or for benefit of creditor
3. On account of antecedent debt
4. Made while insolvent
5. Within 90 days (or 1 year for insiders)
6. Enables creditor to receive more than Chapter 7

### Preference Defenses
| Defense | Description |
|---------|-------------|
| Contemporaneous exchange | New value given at same time |
| Ordinary course | Payment in ordinary course of business |
| New value | Subsequent new value provided |
| Purchase money | PMSI for new value |
| Small preference | Under $7,575 (business) or $600 (consumer) |

### Fraudulent Transfer (§548)
**Actual Fraud**: Transfer with intent to hinder, delay, defraud
**Constructive Fraud**: Transfer for less than reasonably equivalent value while:
- Insolvent or became insolvent
- Unreasonably small capital
- Believed would incur debts beyond ability to pay

**Look-back Period**: 2 years (§548); longer under state law (§544)

## Claims and Distributions

### Priority of Claims (§507)
1. Domestic support obligations
2. Administrative expenses
3. Gap claims (involuntary cases)
4. Employee wages (up to $15,150, 180 days)
5. Employee benefit contributions
6. Grain farmers and fishermen
7. Consumer deposits ($3,350 cap)
8. Tax claims
9. DUI judgment claims
10. General unsecured claims

### Proof of Claim
**Filing Deadline**: 70 days after petition (Chapter 7/13) or as set by court (Chapter 11)
**Contents**: Amount, basis, security, priority

### Claim Objections
- Claim filed without supporting documentation
- Amount disputed
- Claim paid
- Claim subject to defense
- Claim improperly classified

## Non-Dischargeable Debts (§523)

| Debt Type | Chapter 7 | Chapter 13 |
|-----------|-----------|------------|
| Certain taxes | Non-dischargeable | Non-dischargeable |
| Student loans (absent hardship) | Non-dischargeable | Non-dischargeable |
| Domestic support | Non-dischargeable | Non-dischargeable |
| Fraud-based debts | Non-dischargeable | Dischargeable |
| Willful and malicious injury | Non-dischargeable | Dischargeable |
| Government fines | Non-dischargeable | Dischargeable |
| DUI judgment | Non-dischargeable | Non-dischargeable |

## Integration with Other Skills

- **litigation**: Adversary proceedings, contested matters
- **corporate-ma**: Distressed M&A, §363 sales
- **contract-lifecycle**: Executory contract issues
- **real-estate**: Property of the estate, foreclosure
- **tax-law**: Tax claims, discharge of tax debts

## Reference Files

For detailed guidance:
- `references/chapter-7-checklist.md` - Chapter 7 filing guide
- `references/chapter-11-process.md` - Reorganization procedures
- `references/claims-guide.md` - Proof of claim and objections
