---
name: closing-disclosure-tolerance
title: Closing Disclosure Tolerance
description: Applies U.S. TRID tolerance rules to compare a residential mortgage Closing Disclosure (CD) against the controlling Loan Estimate (LE). Classifies fees by tolerance bucket, validates changed-circumstance resets, computes violations, and calculates cure amounts. Use when reviewing LE-CD variance, 10% tolerance, revised LE validity, changed circumstances, tolerance cure, or pre-closing compliance QA.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/closing-disclosure-tolerance
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
---

# Closing Disclosure Tolerance

Structured TRID tolerance review for U.S. residential mortgage closings under 12 CFR Part 1026. Covers fee classification, zero/10%/unlimited tolerance testing, changed-circumstance gating, and cure calculation.

## Prerequisites

- Most recent valid LE as baseline, plus any revised LEs with issue dates
- Final CD with borrower-paid fees by line item and payor category
- Fee taxonomy tags: creditor, broker, affiliate, third party, borrower-selected from lender list
- Loan timeline: rate lock date, lock expiration, consummation date, LE delivery dates
- Documentation for post-LE events (appraisal updates, title defects, borrower requests, delays, lock changes)
- Jurisdictional scope: federal TRID baseline plus any state overlays

## Core Workflow

### 1. Normalize baseline

Use the most recent valid LE as of CD generation. Ignore invalid prior LEs unless a valid revised LE was triggered.

### 2. Classify each CD fee

| Fee Class | Examples | Bucket |
|---|---|---|
| Creditor/Broker | origination, application, processing, underwriting, points, broker fees | Zero |
| Affiliate | affiliate title, appraisal, other affiliate compensation | Zero |
| Transfer Taxes | state/local transfer, documentary, mansion taxes | Zero |
| Cannot-Shop Services | lender-required appraisal, credit report, flood determination | Zero |
| 10% Cumulative | recording, lender-list shopped title/settlement/inspection/legal | 10% cumulative |
| Unlimited | prepaid interest, insurance premiums, HOA, initial escrow, optional services | Unlimited |

### 3. Zero-tolerance test

Test each zero-tolerance fee at the line-item level:

- Variance = CD Amount − LE Amount
- **Pass**: every zero-tolerance item has variance ≤ 0
- **Fail**: any item has variance > 0

### 4. Ten-percent cumulative test

Aggregate all 10%-bucket items:

- LE Total = Σ(LE amounts)
- CD Total = Σ(CD amounts)
- Limit = LE Total × 1.10
- **Pass**: CD Total ≤ Limit

Do not test 10% items individually — this is a category-total test.

### 5. Unlimited-tolerance review

Verify items are correctly categorized as unlimited. Do not auto-pass if disclosures are missing or fees are mis-tagged.

### 6. Changed-circumstance gate

| Trigger | Allows Revised LE? |
|---|---|
| Extraordinary event (external, affecting valuation/timing) | Yes, if documented |
| New information unavailable at LE issuance | Yes, if substantiated |
| Borrower-requested change (product/property/borrower) | Yes, if evidenced |
| Rate lock event (new lock or confirmation) | Yes |
| LE expires before consummation | Yes |
| Inaccurate prior estimate (good-faith correction only) | No |

**Revised LE rules:**
- Only affected fees may be revised
- Must be issued within required timing windows with evidence
- Recompute tolerance against revised LE for affected categories only
- Flag pretext where revised LE appears to repair errors [VERIFY]

### 7. Cure calculation

Per 12 CFR 1026.19(f)(2)(v):

- Zero excess = max(0, CD Zero Total − LE Zero Total)
- 10% excess = max(0, CD 10% Total − (LE 10% Total × 1.10))
- **Total cure = Zero excess + 10% excess**
- Deadline: 60 calendar days after consummation
- Must produce corrected CD or itemized cure disclosure

### 8. Final deliverable

- Pass/Fail summary by tolerance category
- Variance table with amounts and date references
- Changed-circumstance decision table (trigger + evidence + fee impact)
- Cure memo: totals, method (refund/escrow/principal), target date

## Common Pitfalls

| Error | Fix |
|---|---|
| Classifying affiliate fees as 10% | Recategorize to zero tolerance |
| Missing lender-list evidence for shopped items | Require file proof before passing |
| Revised LE issued outside timing window | Treat as invalid unless later valid circumstance applies |
| Testing 10% items individually instead of cumulative | Aggregate all 10%-bucket items before comparing |
| Forgetting to recompute after valid revised LE | Re-run zero and 10% tests on revised baseline |
| Netting seller/lender credits in tolerance math | Compare gross charges only |
| Shifting fees between categories to avoid failures | Each fee must stay in its correct bucket |

## Special Situations

| Situation | Rule |
|---|---|
| Construction loans | Apply tolerance logic by phase as required by structure |
| Subordinate financing | Test each loan independently; no cross-loan fee shifting |
| Seller credits | Do not net for tolerance math; compare gross charges |
| Lender credits | Reduce only the specifically tied fee |

## Cross-References

- @draft-closing-disclosure-cd-residential-real-estate
- @closing-disclosure-timing-reference
- @loan-estimate-residential
- @trid-changed-circumstances

## References

- 12 CFR 1026.19(e)(3) — Good faith determination and tolerance [VERIFY]
- 12 CFR 1026.19(e)(3)(iv) — Changed circumstances [VERIFY]
- 12 CFR 1026.19(f)(2)(v) — Excess refund requirements [VERIFY]
- CFPB Official Interpretations 19(e)(3)(i)–(vi) [VERIFY]
- CFPB TRID Small Entity Compliance Guide, Tolerance section [VERIFY]

---

**Key changes from the original:**

- **Removed `tags`** — not part of the Agent Skills spec; discovery relies on `description` keywords
- **Tightened description** — third-person, keyword-rich, within 1024 chars
- **Cut ~40% token weight** — eliminated verbose text-block worksheets, redundant prose in Guidelines/Do-Don't table, and duplicated content between sections
- **Merged Guidelines + Common Errors → Common Pitfalls** — single table, no duplication with Special Situations
- **Restructured body** — Prerequisites → Core Workflow (8 numbered steps) → Pitfalls → Special Situations → References, following the quick-start / core-patterns / pitfalls progression
- **Preserved all domain accuracy** — tolerance formulas, fee classifications, changed-circumstance triggers, cure mechanics, CFR references, and [VERIFY] markers all intact
