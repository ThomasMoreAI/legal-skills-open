---
name: class-claim-form
title: Class Member Claim Form
description: Drafts U.S. class action settlement claim forms compliant with FRCP 23 and court approval orders. Triggers on claim form drafting, settlement administrator packets, online claim workflows, or class member submission forms.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/class-claim-form
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [drafting, pleading]
---

# Class Member Claim Form

Produces a court-compliant claim form enabling class members to submit settlement claims with verifiable eligibility and documentation.

## Prerequisites

Gather before drafting:

1. Preliminary or final approval order and settlement agreement
2. Case caption, court, judge, case number
3. Class definition and class period dates
4. Claim categories, eligibility criteria, payment formula/tiers
5. Submission deadline (date, time, time zone, postmark vs. receipt rule)
6. Settlement administrator contact (name, address, email, phone, portal URL)
7. Documentation requirements and no-doc thresholds
8. Privacy/data-retention policy; e-sign and accessibility requirements

## Workflow

1. **Header and deadline** — "Official Claim Form," exact case caption, court, case number, administrator contact, deadline with postmark/receipt rule.
2. **Eligibility summary** — Plain-language class definition referencing class period.
3. **Claimant identification** — Fields aligned to class definition (legal name during class period, current name if different, address, email, phone, alternate contact).
4. **Class criteria fields** — Purchase/transaction dates, account IDs, employment dates—tailored to class definition.
5. **Claim details** — Claim type checkboxes, dates, amounts, identifiers tied to compensation formula.
6. **Documentation** — List acceptable proof per claim type; state copies-vs-originals rule; note no-doc threshold if any.
7. **Certification and release** — Perjury attestation covering class membership, truthfulness, no duplicate payment. Separate release acknowledgment checkbox. Include state-specific waiver language if unknown claims are released (e.g., Cal. Civ. Code § 1542 — verify applicability).
8. **Signature** — Signature, printed name, date, representative relationship if applicable, e-sign acceptance statement.
9. **Submission instructions** — Mail, email, and portal options; confirmation process; contact info if no confirmation within stated period.
10. **Post-submission** — Review timeline, approval/denial notice, appeal or cure process.

## Required Notices

Every form must include:

- Submission does not guarantee payment
- Settlement subject to court approval/finality
- Attorneys' fees and costs may be deducted
- False statements may lead to denial and penalties
- Privacy and data-use disclosure
- ADA/accessibility and translation availability

## Documentation by Claim Type

| Type | Primary Proof | Alternative |
|---|---|---|
| Purchase-based | Receipts, invoices, bank/card statements | Affidavit (if permitted) |
| Account-based | Account statements, confirmations | Admin verification |
| Employment-based | Pay stubs, HR records | Employer verification |

## Pitfalls and Checks

- Mirror settlement agreement definitions exactly — never invent eligibility criteria.
- Use plain language; define any legal terms.
- Align all language with court orders and class notice.
- Never promise payment or specific amounts unless the order mandates it.
- Require authority documents for estates, minors, or representatives.
- Avoid collecting SSNs; if court-ordered, request last four digits only.
- Ensure E-SIGN Act compliance for electronic submissions.
- For state-court class actions, adapt to the applicable state rule instead of FRCP 23.

---

Key changes from the original:

- **Description** tightened to a single sentence with clear trigger guidance
- **Removed** the verbose template skeleton — the 10-step workflow now carries the same structural guidance in compact form
- **Consolidated** the section checklist, field rules table, and documentation matrix into the workflow steps and a single lean documentation table
- **Merged** the required notices checklist into a simple bullet list (removed checkbox syntax)
- **Folded** release options guidance into workflow step 7
- **Kept** the pitfalls/guidelines section with all original legal guardrails intact
