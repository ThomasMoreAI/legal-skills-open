---
name: divorce-settlement-summary
title: Divorce Settlement Summary
description: Produces structured summaries of U.S. divorce settlement agreements (MSAs), extracting material terms across property, custody, support, taxes, insurance, fees, and deadlines. Triggers on requests for divorce settlement summary, MSA summary, marital settlement agreement, property division, child custody, parenting plan, child support, or alimony extraction.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/divorce-settlement-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
tags: [litigation, summarization, summary]
---

# Divorce Settlement Summary

Neutral, litigation-ready summary of a divorce settlement agreement extracting all material terms and action items.

## Quick Start

Collect before summarizing:
- Executed or draft settlement agreement (with attachments/exhibits/schedules)
- Case identifiers (parties, case number, court/jurisdiction, settlement date)
- Parenting plan / custody exhibit (if separate)
- Financial schedules (asset/debt lists, QDRO details, support worksheets)

## Output Template

Fill every applicable section. Omit only sections the agreement does not address.

### 1) Identifying Information
- Parties
- Case number
- Court/jurisdiction (state + county)
- Agreement date / effective date
- Status (executed / draft / contingent on approval)
- Incorporation into judgment (yes/no; conditions)

### 2) Marital Property Division

Short narrative, then table by asset class:

| Asset Class | Specific Asset | Value / Valuation Date | Awarded To | Transfer Mechanics | Deadline / Conditions |
|---|---|---|---|---|---|

Asset classes: real property, financial accounts (bank/brokerage/crypto), retirement (401(k)/IRA/pension — note QDRO), business interests, vehicles/titled property, personal property, IP/royalties, other (stock options, windfalls, claims).

### 3) Debts and Liabilities

| Debt Type | Creditor / Account | Balance / Date | Responsibility | Refinance / Indemnity | Deadline |
|---|---|---|---|---|---|

### 4) Child Custody and Parenting Plan
- Legal custody (sole/joint; decision domains)
- Physical custody / timesharing (% if stated)
- Regular schedule, holiday schedule, vacation/travel
- Transportation / exchange logistics
- Communication protocols (methods, notice periods)
- Relocation / modification clauses
- Supervision / restrictions
- Tie-breaker / dispute mechanism

### 5) Child Support
- Guideline basis (state guideline / deviation)
- Obligor → obligee; amount and frequency
- Start date, duration, termination triggers
- Health insurance (who, plan, cost split)
- Unreimbursed medical (allocation %, thresholds)
- Childcare / education / extracurricular allocations
- Payment method (wage assignment / direct)
- Arrears treatment

### 6) Spousal Support / Alimony
- Type (temporary / rehabilitative / permanent / lump sum)
- Amount, frequency, start date, duration
- Termination / modification triggers
- Tax treatment (if stated)
- Security (life insurance, liens, guarantees)

### 7) Taxes
- Filing status allocations
- Dependency exemptions / credits
- Refund / liability allocation
- Property transfer tax responsibilities
- Retirement transfer treatment

### 8) Insurance and Benefits
- Life insurance securing support (amount, beneficiary, duration)
- Health insurance obligations
- COBRA / continuation coverage

### 9) Attorney's Fees and Costs
- Fee responsibility and any reimbursement/offsets

### 10) Dispute Resolution and Enforcement
- Mediation / arbitration requirements
- Venue / forum selection
- Enforcement / contempt provisions

### 11) Confidentiality / Non-Disparagement
- Scope and exceptions (court filings, legal advice, compliance)

### 12) Deadlines and Action Items

| Action | Responsible Party | Deadline | Proof Required |
|---|---|---|---|

Cover: deed transfers, refinancing, QDRO submission, account rollovers, title changes, document deliveries.

### 13) Exhibits and Attachments

List each exhibit with a one-line description. Do not reproduce contents.

### 14) Ambiguities / Inconsistencies

Identify unclear or conflicting terms factually.

## Pitfalls and Checks

- **Neutrality**: No fairness analysis or advocacy language.
- **Precision**: Use exact figures, dates, and percentages from the agreement.
- **Gaps**: Flag missing data or cross-referenced schedules as "not provided."
- **Jurisdiction**: Note state-specific terms without redefining them; custody and support rules vary by state.
- **Citations**: Mark uncertain legal citations as `[VERIFY]`.
