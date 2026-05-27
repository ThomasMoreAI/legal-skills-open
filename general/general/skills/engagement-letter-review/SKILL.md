---
name: engagement-letter-review
title: Engagement Letter Review
description: Reviews attorney engagement letters for completeness, fee clarity, scope definition, and potential client-side risks. Flags missing provisions, ambiguous terms, and unusual fee arrangements. Use when the user mentions "engagement letter", "retainer agreement", "fee agreement review", "scope of representation", or needs to evaluate terms before signing or sending an engagement letter.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/engagement-letter-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
tags: [transactional, agreement, analysis]
---

# Engagement Letter Review

Reviews attorney engagement letters and retainer agreements to ensure they are complete, clearly scoped, and protect both attorney and client interests.

## What It Analyzes

### Fee Structure
- Fee type identification (hourly, flat, contingency, hybrid, subscription)
- Rate clarity and billing increment disclosure
- Expense and cost-advancement terms
- Fee modification or escalation provisions
- Trust account and retainer replenishment terms

### Scope of Representation
- Matter description specificity
- Excluded matters and carve-outs
- Conditions that trigger scope expansion
- Multi-party representation disclosures

### Term and Termination
- Duration and renewal terms
- Withdrawal and termination rights (both sides)
- File retention and return obligations
- Post-termination fee obligations (liens, outstanding balances)

### Risk Provisions
- Limitation of liability clauses
- Arbitration or dispute resolution clauses
- Conflict waiver language
- Consent-to-disclose provisions
- Insurance and indemnification terms

### Compliance
- Jurisdiction-specific requirements (trust accounts, fee disclosures)
- Required disclosures for contingency arrangements
- Client rights notices

## Output

Returns a structured assessment with:
- **Completeness score** — percentage of standard provisions present
- **Risk flags** — ranked by severity (high/medium/low)
- **Missing provisions** — recommended additions
- **Ambiguous terms** — language that could create disputes
- **Comparison notes** — how terms compare to standard market practice

## Usage

Provide the engagement letter text or document. Optionally specify:
- **Perspective**: `attorney` (drafting) or `client` (reviewing incoming)
- **Jurisdiction**: state or jurisdiction for compliance checks
- **Practice area**: to calibrate scope expectations (e.g., litigation vs. corporate)

## Example Prompts

- "Review this engagement letter — am I missing anything before I send it?"
- "Flag any unusual terms in this retainer agreement"
- "Does this engagement letter comply with California rules?"
- "Compare the fee structure here to standard market terms for IP litigation"
