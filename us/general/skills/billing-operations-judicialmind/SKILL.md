---
name: billing-operations-judicialmind
title: Billing & Operations
description: Legal billing and law firm operations skill for time tracking, invoicing, and financial management. Use when the user needs assistance with timekeeping, invoice review, billing guidelines, LEDES format, outside counsel management, or legal spend analysis. Triggers on keywords like "billing", "invoice", "timekeeping", "LEDES", "billing guidelines", "legal spend", "outside counsel", "time entry", "fee arrangement", "legal operations".
author: judicialmind
author_url: https://github.com/judicialmind/legal-skills/tree/main/skills/billing-operations
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: general
language: en
sources:
- title: Budget Templates
  path: references/budget-templates.md
- title: Ledes Format
  path: references/ledes-format.md
- title: Utbms Codes
  path: references/utbms-codes.md
---

# Billing & Operations

This skill provides expert guidance for legal billing, timekeeping, and law firm financial operations.

## Core Capabilities

### 1. Time Management
- Time entry best practices
- Contemporaneous recording
- Task-based billing
- UTBMS codes

### 2. Invoice Management
- Invoice preparation
- Bill review
- LEDES compliance
- E-billing submission

### 3. Budget Management
- Matter budgets
- Fee estimates
- Variance tracking
- Cost controls

### 4. Legal Operations
- Outside counsel management
- Billing guidelines
- Spend analytics
- Performance metrics

## Time Entry Best Practices

### Quality Time Entry Elements
```
EFFECTIVE TIME ENTRY FORMAT

Date: [Date]
Timekeeper: [Name]
Matter: [Number]
Time: [Increments per policy]
Task Code: [UTBMS if required]
Activity Code: [UTBMS if required]

Description:
[Action verb] + [specific subject] + [purpose/outcome]

EXAMPLE:
"Drafted motion to compel discovery responses re: defendant's
production deficiencies; analyzed applicable rules and case law
supporting our position."

NOT:
"Worked on motion" (too vague)
"Research and drafting" (no context)
```

### Common Time Entry Errors
| Error | Problem | Correction |
|-------|---------|------------|
| Block billing | Combined tasks without breakdown | Separate each task |
| Vague descriptions | No meaningful detail | Specific subject/purpose |
| Administrative tasks | Non-billable billed | Remove or adjust |
| Excessive research | Unbounded research time | Cap and explain |
| Travel time | Billed at full rate | Reduce rate or exclude |
| Internal conferences | Multiple timekeepers | Limit attendees |

### UTBMS Task Codes (Common)
| Code | Description |
|------|-------------|
| L110 | Fact Investigation/Development |
| L120 | Analysis/Strategy |
| L130 | Experts/Consultants |
| L140 | Document Preparation (Non-Discovery) |
| L150 | Document Review |
| L160 | Court Filing Preparation/Review |
| L190 | Other Litigation Tasks |
| L210 | Pleadings |
| L220 | Discovery |
| L230 | Discovery/Trial Motions |
| L310 | Witness Interviews |
| L320 | Deposition |
| L330 | Jury Consulting |
| L340 | Trial Prep/Trial |
| L350 | ADR |
| L410 | Settlement/Negotiation |
| L510 | Appeal |

### UTBMS Activity Codes (Common)
| Code | Description |
|------|-------------|
| A101 | Plan and prepare for |
| A102 | Research |
| A103 | Draft/revise |
| A104 | Review/analyze |
| A105 | Communicate (within legal team) |
| A106 | Communicate (with client) |
| A107 | Communicate (other outside counsel) |
| A108 | Communicate (other external) |
| A109 | Appear for/attend |
| A110 | Manage data/files/documents |
| A111 | Other |

## Invoice Preparation

### Invoice Checklist
- [ ] Matter information correct
- [ ] Billing period clear
- [ ] Time entries reviewed for quality
- [ ] Descriptions comply with guidelines
- [ ] Block billing eliminated
- [ ] Rates correct
- [ ] Expenses documented
- [ ] Discounts applied
- [ ] LEDES format (if required)
- [ ] Budget status included
- [ ] Prior balance shown
- [ ] Payment terms stated

### Invoice Format
```
[FIRM LETTERHEAD]

INVOICE

Invoice Number: [Number]
Invoice Date: [Date]
Due Date: [Date]

Bill To:
[Client Name]
[Address]

Matter: [Number] - [Description]
Billing Period: [Start] - [End]

─────────────────────────────────────────────────────
PROFESSIONAL FEES
─────────────────────────────────────────────────────

[Date] [Timekeeper] [Hours] [Rate] [Amount]
       [Description of services]

[Continue for all entries...]

       Subtotal Professional Fees:    $[X]
       [Discount, if any]:           -$[X]
       Total Professional Fees:       $[X]

─────────────────────────────────────────────────────
DISBURSEMENTS
─────────────────────────────────────────────────────

[Date] [Description]                  $[X]

       Total Disbursements:           $[X]

─────────────────────────────────────────────────────

CURRENT CHARGES:                      $[X]
PRIOR BALANCE:                        $[X]
TOTAL DUE:                            $[X]

Payment Terms: Net 30 days
```

## LEDES Format

### LEDES 1998B Structure
```
Line 1: Header row with field names
Line 2+: Data rows

Fields (pipe-delimited):
INVOICE_DATE|INVOICE_NUMBER|CLIENT_ID|LAW_FIRM_MATTER_ID|
INVOICE_TOTAL|BILLING_START_DATE|BILLING_END_DATE|
INVOICE_DESCRIPTION|LINE_ITEM_NUMBER|EXP/FEE/INV_ADJ_TYPE|
LINE_ITEM_NUMBER_OF_UNITS|LINE_ITEM_ADJUSTMENT_AMOUNT|
LINE_ITEM_TOTAL|LINE_ITEM_DATE|LINE_ITEM_TASK_CODE|
LINE_ITEM_EXPENSE_CODE|LINE_ITEM_ACTIVITY_CODE|
TIMEKEEPER_ID|LINE_ITEM_DESCRIPTION|LAW_FIRM_ID|
LINE_ITEM_UNIT_COST|TIMEKEEPER_NAME|TIMEKEEPER_CLASSIFICATION|
CLIENT_MATTER_ID
```

### LEDES Expense Codes (Common)
| Code | Description |
|------|-------------|
| E101 | Copying/Reproduction |
| E102 | Outside Printing |
| E103 | Word Processing |
| E104 | Facsimile |
| E105 | Telephone |
| E106 | Online Research |
| E107 | Delivery/Messenger |
| E108 | Postage |
| E109 | Local Travel |
| E110 | Out-of-Town Travel |
| E111 | Meals |
| E112 | Court Fees |
| E113 | Subpoena Fees |
| E114 | Witness Fees |
| E115 | Deposition Transcripts |
| E116 | Trial Transcripts |
| E117 | Trial Exhibits |
| E118 | Litigation Support |
| E119 | Experts |
| E120 | Private Investigators |
| E121 | Arbitrators/Mediators |

## Billing Guidelines

### Common Billing Guidelines Requirements
```
OUTSIDE COUNSEL BILLING GUIDELINES

1. STAFFING
   - Identify lead attorney
   - Limit number of attorneys
   - No training on client matters
   - Prior approval for additional timekeepers

2. RATES
   - Approved rate schedule
   - Annual rate increases capped
   - Blended rates for certain work
   - Alternative fee arrangements

3. ACTIVITIES
   - Prior approval thresholds
   - Limit internal conferences
   - Travel time at reduced rate
   - No administrative tasks

4. EXPENSES
   - Pre-approval for >$[threshold]
   - Reasonable and necessary only
   - No overhead expenses
   - Itemization required

5. INVOICING
   - Monthly submission required
   - LEDES format mandatory
   - Task/activity codes required
   - 90-day submission deadline

6. REPORTING
   - Monthly status reports
   - Budget-to-actual tracking
   - Matter assessments
   - Accrual estimates
```

### Approval Thresholds (Sample)
| Activity | Threshold |
|----------|-----------|
| Engage expert | $10,000 |
| Retain local counsel | $5,000 |
| Single deposition | $15,000 |
| Motion/brief | $25,000 |
| Settlement authority | Per matter |
| Appeal | Requires approval |
| Travel | $2,500 |

## Budget Management

### Matter Budget Template
```
MATTER BUDGET

Matter: [Number/Description]
Budget Period: [Dates]
Prepared by: [Name]
Approved by: [Name]
Date: [Date]

PHASE BUDGET BREAKDOWN

Phase                    Hours    Fees        Expenses    Total
──────────────────────────────────────────────────────────────
1. Case Assessment         25     $12,500        $500    $13,000
2. Pleadings              50     $25,000      $1,000    $26,000
3. Discovery             200    $100,000     $30,000   $130,000
4. Depositions           100     $50,000     $25,000    $75,000
5. Motions                75     $37,500      $2,000    $39,500
6. Trial Prep            150     $75,000     $15,000    $90,000
7. Trial                 100     $50,000     $10,000    $60,000
──────────────────────────────────────────────────────────────
TOTAL                    700    $350,000     $83,500   $433,500

ASSUMPTIONS
- [Key assumption 1]
- [Key assumption 2]

CONTINGENCIES
- [Item]: +$[X]
- [Item]: +$[X]

BUDGET RANGE
Low:  $375,000
Mid:  $433,500
High: $525,000
```

### Budget Variance Reporting
```
BUDGET VARIANCE REPORT

Matter: [Number]
Period: [Dates]
As of: [Date]

                    Budget      Actual      Variance    %
────────────────────────────────────────────────────────────
Fees               $100,000    $115,000    -$15,000   -15%
Expenses            $25,000     $22,000     +$3,000   +12%
TOTAL              $125,000    $137,000    -$12,000   -10%

EXPLANATION OF VARIANCES
[Description of why actual differs from budget]

FORECAST TO COMPLETION
Remaining budget: $[X]
Estimated to complete: $[X]
Projected variance: $[X]

RECOMMENDATIONS
[Actions to address variance]
```

## Legal Spend Analytics

### Key Metrics
| Metric | Calculation | Target |
|--------|-------------|--------|
| Realization rate | Collected / Billed | >95% |
| Write-off rate | Write-offs / Billed | <5% |
| Collection period | Days to payment | <45 days |
| Budget accuracy | Actual vs. Budget | ±10% |
| Cycle time | Matter open to close | Declining |
| Cost per matter | Total spend / matters | Varies |

### Spend Analysis Categories
```
LEGAL SPEND ANALYSIS

Period: [Dates]
Total Spend: $[X]

BY MATTER TYPE
─────────────────────────
Litigation        40%
Transactions      25%
Regulatory        15%
Employment        10%
IP                10%

BY FIRM
─────────────────────────
Firm A            35%
Firm B            25%
Firm C            20%
Other             20%

BY PHASE (LITIGATION)
─────────────────────────
Discovery         45%
Depositions       20%
Motions           15%
Trial             10%
Other             10%
```

## Alternative Fee Arrangements

### AFA Types
| Type | Structure | Best For |
|------|-----------|----------|
| Fixed fee | Set amount for scope | Predictable matters |
| Capped fee | Maximum total | Risk sharing |
| Success fee | Bonus for outcome | Aligned incentives |
| Holdback | % withheld pending outcome | Performance |
| Blended rate | Single rate all timekeepers | Simplified billing |
| Volume discount | Reduced rates for volume | Ongoing relationships |
| Collar | Shared savings/overruns | Balanced risk |

### AFA Considerations
- Clear scope definition
- Change order process
- Assumptions documented
- Out-of-scope defined
- Success metrics established
- Payment milestones
- True-up provisions

## Integration with Other Skills

- **client-intake**: Fee arrangements
- **case-management**: Matter tracking
- **legal-analytics**: Cost analysis
- **compliance-tracking**: Billing compliance
- **e-discovery**: Vendor cost management

## Reference Files

For detailed guidance:
- `references/ledes-format.md` - LEDES specification
- `references/utbms-codes.md` - Complete UTBMS code list
- `references/budget-templates.md` - Budget format examples
