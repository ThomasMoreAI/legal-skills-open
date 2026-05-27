---
name: billing-summary
title: Legal Billing Summary
description: Produces privilege-safe U.S. corporate legal billing summaries from time and expense data. Converts entries into client-friendly narratives with categorized hours, rates, expenses, and milestones while enforcing engagement-letter rules and ethical billing safeguards. Use when asked to create a billing summary, invoice narrative, timekeeper breakdown, expense summary, or fee narrative.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/billing-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [summarization, summary]
---

# Legal Billing Summary

Generate a client-ready billing narrative that explains fees and expenses clearly while preserving privilege.

## Required Inputs

1. Billing period (start/end dates), matter name, client name
2. Time entries: timekeeper, rate, hours, description, date
3. Expense entries: date, vendor, description, amount
4. Engagement letter or billing guidelines (rates, caps, task codes, prohibited expenses)
5. Milestones or phase labels (if any)
6. Write-downs, discounts, or adjustments (if any)

## Output Structure

Populate every section below.

### 1. Header

Matter | Client | Billing Period | Responsible Attorneys | Billing Guidelines Reference

### 2. Executive Overview

3-6 sentences on the period's major workstreams and outcomes, plus a totals table:

| Metric | Amount |
| --- | --- |
| Fees | $ |
| Expenses | $ |
| Total | $ |
| Discount/Write-down | $ |
| Net Total | $ |

### 3. Timekeeper Summary

| Timekeeper | Role | Rate | Hours | Fees | Notes |
| --- | --- | --- | --- | --- | --- |

Notes column: explain scope (e.g., "board governance research," "drafted consent resolutions").

### 4. Task Category Breakdown

Default categories (override with client task codes if provided):

- Research and Analysis
- Drafting and Document Production
- Client Communications
- Internal Strategy and Case Management
- Negotiation and Counterparty Communications
- Regulatory/Compliance Work
- Filings and Formalities
- Other (define clearly)

| Category | Hours | Fees | Narrative |
| --- | --- | --- | --- |

Narrative: explain purpose and outcome in plain English; never reveal legal advice or strategy.

### 5. Phase View (optional, recommended for long periods)

| Phase / Milestone | Dates | Key Work Performed | Fees |
| --- | --- | --- | --- |

### 6. Expenses

| Date | Category | Vendor | Description | Amount | Justification |
| --- | --- | --- | --- | --- | --- |

Include subtotals for material categories (filing fees, expert/consultant, travel).

### 7. Adjustments and Compliance

- List write-downs, caps applied, or policy-driven exclusions.
- Note block-billed entries and how they were separated.
- Confirm compliance with client billing guidelines.

### 8. Forward Look (optional)

2-4 sentences on expected next-period activities and cost drivers.

## Privilege and Billing Safeguards

- **Protect privilege**: never include legal advice, mental impressions, or litigation strategy.
- **Be specific**: avoid vague phrases like "legal research" — always name the topic.
- **Tie work to objectives**: connect entries to matter goals or compliance requirements.
- **Show policy compliance**: rates, caps, task codes, approved expenses.
- **Flag anomalies**: unusual expenses, staffing changes, large time spikes.
- **No duplicate billing**: do not overlap timekeeper entries for the same task without explanation.
- **No administrative padding**: exclude admin tasks unless guidelines permit.
- **Stay consistent**: narrative must match time entry descriptions and invoice totals.
