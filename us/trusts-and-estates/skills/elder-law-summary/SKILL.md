---
name: elder-law-summary
title: Elder Law Summary
description: Generates structured elder law summaries covering estate planning, elder abuse, healthcare rights, Medicaid eligibility, and guardianship with prioritized action plans. Triggers when the user requests an elderly client matter summary, elder care legal overview, long-term care planning review, or guardianship assessment.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/elder-law-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: trusts-and-estates
language: en
tags: [analysis, summarization, summary, transactional]
---

# Elder Law Summary

Structured legal overview for elderly client matters — jurisdiction-specific analysis across all elder law domains with a prioritized action plan. Serves both legal professionals and family caregivers.

## Prerequisites

Gather before generating:

1. **Client profile** — age, state, capacity status, living situation
2. **Legal documents** — wills, trusts, POAs, advance directives, guardianship orders
3. **Financials** — asset inventory, income sources, benefit status (Medicare/Medicaid/SSI)
4. **Medical context** — conditions, care needs, current arrangements
5. **Triggers** — suspected abuse, Medicaid application, capacity decline, family disputes

## Output Structure

### 1. Executive Overview

| Element | Content |
|---|---|
| Client snapshot | Name, age, state, capacity status, living situation |
| Critical issues | Top 3–5 pressing legal concerns |
| Immediate actions | Time-sensitive items (deadlines, reporting obligations) |
| Risk level | Low / Moderate / High with justification |

### 2. Domain Analysis

Analyze each applicable domain:

**Estate Planning** — Inventory documents; note execution defects, staleness, missing instruments. Identify untitled assets, missing beneficiary designations, outdated fiduciaries. Recommend specific documents to draft/update.

**Elder Abuse** — Flag suspicious transactions, undue influence signs, neglect markers. State-specific mandatory reporting rules and applicable agencies. Remedies: protective orders, civil claims, criminal referrals, APS reporting.

**Healthcare Rights & Advance Directives** — Directive validity and consistency with current wishes. Medicare/Medicaid enrollment and eligibility issues. Nursing home residents' rights, HIPAA considerations.

**Medicaid & Long-Term Care** — State-specific income/asset eligibility limits. Look-back period (60 months; 30 months California pre-2024 `[VERIFY]`); flag disqualifying transfers. Spousal protections, exempt assets, permissible planning tools. Verify regulatory compliance.

**Guardianship / Conservatorship** — Assess necessity vs. less restrictive alternatives (POA, representative payee, supported decision-making). Jurisdiction-specific filing requirements, costs, timelines. Review existing order scope and reporting compliance.

**Benefits & Income** — Social Security, SSI, pension, veteran's benefits. Tax implications of current arrangements.

### 3. Document Review Findings

When documents are uploaded:

| Document | Key Facts | Red Flags | Status |
|---|---|---|---|
| {name} | {dates, parties, terms} | {concerns} | Valid / Defective / Stale |

### 4. Prioritized Action Plan

| Priority | Action | Owner | Urgency |
|---|---|---|---|
| Immediate | e.g., file APS report | Attorney | 24–48 hrs |
| Short-term | e.g., update POA | Attorney + family | 2–4 weeks |
| Long-term | e.g., Medicaid pre-planning | Attorney + advisor | 3–6 months |

## Pitfalls & Checks

- **Always specify state** — Medicaid thresholds, guardianship procedures, and abuse reporting vary dramatically by jurisdiction
- **Plain language** — explain legal concepts accessibly; output serves attorneys and family caregivers
- **Cite uploaded documents** by name when identifying facts or concerns
- **Capacity observations only** — note concerns without clinical determinations; recommend formal evaluation where appropriate
- **`[VERIFY]` tag** — mark any statutory cite or threshold not confirmed against current law
- **Least restrictive alternative** — frame recommendations to preserve client autonomy and dignity
- **Include state contacts** where actionable (APS hotline, state Medicaid office, long-term care ombudsman)

---

It looks like I don't have write permission to the file. Could you grant write access so I can save the rewrite, or would you like to copy the output above directly?
