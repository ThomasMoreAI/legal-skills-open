---
name: family-law-judicialmind
title: Family Law
description: Family law skill for domestic relations matters. Use when the user needs assistance with divorce, custody, child support, alimony, prenuptial agreements, adoption, or domestic violence. Triggers on keywords like "divorce", "custody", "child support", "alimony", "prenuptial", "prenup", "visitation", "parenting plan", "adoption", "domestic violence", "restraining order", "marital property".
author: judicialmind
author_url: https://github.com/judicialmind/legal-skills/tree/main/skills/family-law
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
sources:
- title: Parenting Plans
  path: references/parenting-plans.md
- title: Property Division
  path: references/property-division.md
- title: Support Calculations
  path: references/support-calculations.md
---

# Family Law

This skill provides expert guidance for domestic relations matters including divorce, custody, and family formation.

## Core Capabilities

### 1. Divorce/Dissolution
- Grounds and procedure
- Property division
- Spousal support
- Settlement negotiations

### 2. Child Custody
- Legal and physical custody
- Parenting plans
- Modification
- Relocation

### 3. Child Support
- Guideline calculations
- Deviation factors
- Enforcement
- Modification

### 4. Family Formation
- Prenuptial agreements
- Adoption
- Surrogacy
- Guardianship

## Divorce Fundamentals

### Grounds for Divorce
| Type | Description | States |
|------|-------------|--------|
| No-fault | Irreconcilable differences, irretrievable breakdown | All states |
| Fault | Adultery, cruelty, abandonment, etc. | Most states (optional) |

### Divorce Process
```
Filing Petition → Service → Response →
Temporary Orders → Discovery → Mediation/Settlement →
Trial (if needed) → Final Judgment → Post-Decree
```

### Temporary Orders
- Temporary custody/visitation
- Temporary support (spousal and child)
- Exclusive use of residence
- Restraining orders (dissipation of assets)
- Attorney fees

## Property Division

### Marital vs. Separate Property

**Marital Property** (generally):
- Acquired during marriage
- Appreciation of separate property (active efforts)
- Commingled property
- Retirement benefits earned during marriage

**Separate Property** (generally):
- Owned before marriage
- Gifts and inheritances (to one spouse)
- Personal injury awards (pain and suffering)
- Property excluded by valid agreement

### Distribution Systems
| System | States | Approach |
|--------|--------|----------|
| Equitable Distribution | ~40 states | Fair, not necessarily equal |
| Community Property | AZ, CA, ID, LA, NV, NM, TX, WA, WI | 50/50 presumption |

### Equitable Distribution Factors
1. Length of marriage
2. Age and health of parties
3. Income and earning capacity
4. Standard of living during marriage
5. Contributions to marriage (including homemaker)
6. Economic circumstances at division
7. Tax consequences
8. Custody arrangements
9. Dissipation of assets
10. Prenuptial agreements

### Valuation Issues
| Asset | Valuation Method |
|-------|------------------|
| Real estate | Appraisal |
| Business | Income, market, or asset approach |
| Retirement | Present value of benefits |
| Stock options | Black-Scholes, intrinsic value |
| Professional degree | Varies by jurisdiction |

## Spousal Support (Alimony)

### Types of Spousal Support
| Type | Purpose | Duration |
|------|---------|----------|
| Temporary | During proceedings | Until final order |
| Rehabilitative | Enable self-support | Limited term |
| Bridge-the-gap | Transition period | Short-term |
| Durational | Set period | Varies |
| Permanent | Long-term marriages | Until death/remarriage |

### Factors Considered
1. Need of requesting spouse
2. Ability to pay of other spouse
3. Length of marriage
4. Standard of living during marriage
5. Age and health
6. Earning capacity and employability
7. Contributions to marriage
8. Marital misconduct (some states)
9. Tax implications
10. Any other relevant factors

### Modification/Termination
- Substantial change in circumstances
- Cohabitation (varies by state)
- Remarriage (usually terminates)
- Death of either party

## Child Custody

### Custody Types
| Type | Definition |
|------|------------|
| Legal custody | Decision-making authority |
| Physical custody | Residential arrangement |
| Sole custody | One parent has custody |
| Joint custody | Shared custody |
| Primary residence | Where child primarily lives |

### Best Interest Factors
1. Wishes of parents
2. Wishes of child (age-appropriate)
3. Child's relationship with each parent
4. Child's adjustment to home, school, community
5. Mental and physical health of all parties
6. History of domestic violence
7. Parenting history and involvement
8. Stability and continuity
9. Ability to co-parent
10. Geographic proximity

### Parenting Plan Elements
```
1. LEGAL CUSTODY
   - Joint or sole
   - Decision-making categories (education, healthcare, religion, activities)
   - Dispute resolution mechanism

2. PHYSICAL CUSTODY / TIME-SHARING
   - Regular schedule
   - Holiday schedule
   - Summer/vacation schedule
   - Transportation arrangements

3. COMMUNICATION
   - Child's contact with non-residential parent
   - Parent-to-parent communication methods
   - Technology/video calls

4. RELOCATION
   - Notice requirements
   - Distance triggers
   - Procedure for objection

5. MODIFICATIONS
   - Circumstances requiring review
   - Dispute resolution process
```

### Relocation
**Common Requirements**:
- Advance written notice (30-60 days typical)
- Consent of other parent or court approval
- Good faith reason for move
- Best interest analysis
- Modified parenting plan

## Child Support

### Income Shares Model (Majority)
```
1. Determine each parent's gross income
2. Calculate combined income
3. Apply guideline schedule for number of children
4. Allocate proportionally based on income percentage
5. Adjust for parenting time
6. Add mandatory add-ons (healthcare, childcare)
7. Apply deviations if appropriate
```

### Income Considerations
**Included**: Wages, salary, commissions, bonuses, self-employment, investments, rental income, Social Security, unemployment, workers' comp, pensions

**Imputed Income**: If voluntarily unemployed or underemployed

### Common Deviations
- Extraordinary medical expenses
- Educational expenses
- Travel costs for visitation
- Shared parenting time credits
- Other children obligation
- Extraordinary income

### Duration
- Generally until age 18 (or 19 in some states)
- May extend for college (varies by state)
- May extend for disabled child
- May terminate upon emancipation

### Enforcement
- Wage withholding
- Tax refund intercept
- License suspension
- Contempt proceedings
- Credit reporting

## Prenuptial Agreements

### Enforceability Requirements
1. Written and signed
2. Full financial disclosure
3. Voluntary execution
4. Not unconscionable
5. Independent counsel opportunity
6. Executed before marriage
7. No fraud, duress, or overreaching

### Common Provisions
- Property characterization
- Property division upon divorce
- Spousal support waiver/limitation
- Death provisions
- Business protection
- Debt allocation
- Sunset clauses

### Void/Voidable Provisions
- Child custody (court decides based on best interest)
- Child support (cannot waive)
- Provisions promoting divorce
- Unconscionable terms

## Adoption

### Types of Adoption
| Type | Description |
|------|-------------|
| Agency | Through licensed agency |
| Private | Direct from birth parents |
| Stepparent | Spouse of custodial parent |
| Relative | Kinship adoption |
| Foster care | From foster system |
| International | From foreign country |

### General Process
```
1. Home study
2. Matching/placement
3. Termination of parental rights (if needed)
4. Consent(s) obtained
5. Placement period
6. Finalization hearing
7. New birth certificate
```

### Consent Requirements
- Both biological parents (unless rights terminated)
- Child (if certain age, typically 12-14)
- Agency (if involved)
- Court approval

## Domestic Violence

### Protective Orders
| Type | Duration | Process |
|------|----------|---------|
| Emergency | 24-72 hours | Ex parte, immediate danger |
| Temporary | 10-30 days | Ex parte, pending hearing |
| Final | 1-5 years | After hearing, renewable |

### Relief Available
- No contact order
- Stay-away order
- Exclusive possession of residence
- Temporary custody
- Firearm surrender
- Counseling requirement
- Support orders

## Integration with Other Skills

- **litigation**: Trial practice, motion practice
- **legal-research**: State-specific law research
- **document-drafting**: Agreements and pleadings
- **tax-law**: Tax implications of divorce
- **real-estate**: Property transfers

## Reference Files

For detailed guidance:
- `references/parenting-plans.md` - Sample parenting plan provisions
- `references/property-division.md` - Asset valuation and division
- `references/support-calculations.md` - Support guideline worksheets
