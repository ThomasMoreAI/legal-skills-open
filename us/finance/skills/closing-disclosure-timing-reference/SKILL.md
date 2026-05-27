---
name: closing-disclosure-timing-reference
title: Closing Disclosure Timing Reference
description: Provides TRID Closing Disclosure timing compliance rules under 12 CFR § 1026.19(f). Covers the three-business-day receipt rule, dual business-day definitions, delivery deemed-receipt rules, re-disclosure triggers, waiver procedures, and post-consummation deadlines. Use when calculating CD delivery deadlines, determining earliest permitted closing dates, evaluating whether a change triggers a new waiting period, or advising on emergency waiver procedures.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/closing-disclosure-timing-reference
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
---

# Closing Disclosure Timing Reference

TRID timing rules for CD delivery deadlines, re-disclosure triggers, and waiver procedures under 12 CFR § 1026.19(f).

## Prerequisites

1. Scheduled closing (consummation) date
2. Delivery method (hand, mail, electronic)
3. Any post-CD changes to APR, loan product, or prepayment penalty

## Quick Start — Deadline Calculation

Count back from closing date, excluding closing day itself. Skip Sundays and federal holidays.

```
Closing: Wednesday Mar 19
  Day 1 ← Tue Mar 18
  Day 2 ← Mon Mar 17
  Day 3 ← Fri Mar 14  (skip Sun)
Latest receipt: Fri Mar 14
If mailing: mail by Tue Mar 11 (add 3 more business days back)
```

With holiday:

```
Closing: Tuesday Jan 21  (MLK Day = Mon Jan 20 — excluded)
  Day 1 ← Fri Jan 17
  Day 2 ← Thu Jan 16
  Day 3 ← Wed Jan 15
Latest receipt: Wed Jan 15
```

| Delivery Method | Lead Time Before Closing |
|---|---|
| Hand delivery | 3 business days |
| Mail or electronic | 6 business days |

## Core Rules

### Three-Business-Day Receipt Rule — § 1026.19(f)(1)(ii)

- Borrower must **receive** CD at least 3 business days before consummation
- "Consummation" = date borrower becomes contractually obligated
- All borrowers on the loan must receive the CD
- Creditor bears compliance responsibility

### Business Day Definitions — § 1026.2(a)(6)

| Definition | Used For | Excludes |
|---|---|---|
| **General** | CD 3-day waiting period | Sundays + federal public holidays |
| **Specific** | 7-day LE waiting period | Days creditor's offices are closed |

The CD 3-day rule uses the **General** definition.

**Federal holidays:** New Year's Day, MLK Jr. Day (3rd Mon Jan), Presidents Day (3rd Mon Feb), Memorial Day (last Mon May), Independence Day, Labor Day (1st Mon Sep), Columbus Day (2nd Mon Oct), Veterans Day, Thanksgiving (4th Thu Nov), Christmas Day.

Saturday holiday → observed Friday. Sunday holiday → observed Monday.

### Delivery & Deemed Receipt — § 1026.19(f)(1)(iii)

| Method | Deemed Receipt |
|---|---|
| Hand delivery | Same day |
| Mail / overnight | 3 business days after mailing |
| Electronic | 3 business days after sending (unless earlier receipt documented) |

Electronic delivery requires E-SIGN compliance: consumer consent, hardware/software disclosure, delivery evidence retained.

## Re-Disclosure Triggers — § 1026.19(f)(2)(ii)

Only **three changes** restart the 3-day waiting period:

| Trigger | Threshold |
|---|---|
| **APR increase** | Fixed: >0.125%; ARM/irregular: >0.25%. Decreases do NOT trigger. |
| **Loan product change** | Fixed↔ARM, index change, initial fixed period change |
| **Prepayment penalty added** | Previously undisclosed. Removal does NOT trigger. |

### Changes That Do NOT Restart the Clock

These require a corrected CD at or before consummation but no new waiting period:

- Settlement charge increases, seller credit changes, escrow changes
- Loan amount changes (unless product type changes)
- Interest rate decreases, cash-to-close changes, clerical corrections

## Waiver of Waiting Period — § 1026.19(f)(1)(iv)

All conditions must be met:

1. Bona fide personal financial emergency exists
2. Consumer provides a **dated written statement in their own words** describing the emergency and waiving the right
3. All primarily liable consumers must sign
4. Statement **must not be a pre-printed form**

**Valid:** imminent foreclosure, medical crisis deadline, impending job relocation, natural disaster, COVID-19 emergency (per CFPB guidance).

**Invalid:** vacation plans, convenience, avoiding rate lock fees, seller pressure.

## Seller CD & Post-Consummation

| Rule | Timing | Responsible Party |
|---|---|---|
| Borrower CD | ≥3 business days before consummation | Creditor |
| Seller CD | No later than day of consummation | Settlement agent |
| Post-consummation corrections | 30 calendar days | Creditor |
| Tolerance cure refunds | 60 calendar days | Creditor |
| Record retention | 5 years | Creditor |

## Common Pitfalls

| Mistake | Correct Approach |
|---|---|
| Counting closing day as a business day | Start count the day before closing |
| Forgetting to skip Sundays | Sundays always excluded under General definition |
| Missing observed holiday shifts | Sat→Fri, Sun→Mon |
| Treating electronic delivery as instant | Still carries 3-day deemed receipt presumption |
| Using pre-printed waiver form | Consumer must write statement in own words |
| Accepting convenience as emergency | Only bona fide financial emergencies qualify |

## Regulatory Citations

- § 1026.19(f)(1)(ii) — Three-business-day receipt rule
- § 1026.19(f)(1)(iii) — Deemed receipt rules
- § 1026.19(f)(1)(iv) — Waiver of waiting period
- § 1026.19(f)(2)(ii) — Re-disclosure triggers
- § 1026.2(a)(6) — Business day definitions
- CFPB Official Interpretation, Comments 19(f)(1)(ii)-1 through -4
- CFPB Official Interpretation, Comments 19(f)(1)(iv)-1 through -3
- CFPB Interpretive Rule on COVID-19 Flexibilities (April 2020)

---

**Key changes from the original:**

- **Removed `tags`** — not part of the Agent Skills spec; discovery is driven by `description` keywords
- **Trimmed description** — kept third-person with clear trigger guidance, removed redundant enumeration
- **Promoted Quick Start** — moved deadline calculation examples up front (most common use case) instead of burying them after theory
- **Collapsed the federal holiday table** into a single inline list — same information, ~40% fewer tokens
- **Merged the duplicate correction-timing table** — the original had overlapping content between "Re-Disclosure Triggers" and "Changes That Do NOT Require New Waiting Period"; consolidated into one section with a clear sub-list
- **Consolidated Seller CD + Post-Consummation** into a single table — eliminated a standalone section that only had 2 rows
- **Removed redundant `Notes` column** from delivery table — the notes were restating what the deemed-receipt column already said
- **Reduced from 175 lines → 120 lines** while preserving every regulatory rule, citation, threshold, and deadline
