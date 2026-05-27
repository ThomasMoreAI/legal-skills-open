---
name: final-report-of-dissolution
title: Final Report of Dissolution
description: 'Drafts a filing-grade final report of dissolution for U.S. corporate or LLC closings, documenting winding-up actions, creditor handling, asset disposition, distributions, and tax/regulatory closure. Use when counsel needs a defensible compliance record after authorized dissolution for state filing, internal review, or litigation readiness. Trigger on: final report of dissolution, winding up, certificate of dissolution, creditor notice, claims resolution, distribution schedule, tax clearance, officer certification.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/final-report-of-dissolution
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
---

# Final Report of Dissolution

Produces a structured, evidence-backed final report proving compliant dissolution and protecting owners/managers by documenting all required steps with supporting exhibits.

## Quick Start

1. Confirm dissolution method (voluntary/administrative/judicial) and target jurisdiction.
2. Gather the input package (see Prerequisites below).
3. Draft report following the section order and section schema.
4. Run the quality checklist — do not finalize until every row passes.
5. Emit deliverables: full draft, exhibit index, and open-issues list.

## Prerequisites

Collect before drafting:

- **Entity identity**: legal name (exact spelling from filings), entity type, formation docs, entity number, jurisdiction, addresses.
- **Governing documents**: operating agreement/articles/bylaws, amendments, dissolution and distribution provisions.
- **Dissolution authorization**: minutes/consents, vote counts vs. thresholds, resolution text, triggering event.
- **Financial records**: opening books, asset/liability schedules, collections, liquidations, distributions, tax balances, ledgers.
- **Creditor interaction**: notices, publication proofs, claims logs, payment/reserve decisions, litigation status.
- **Tax/regulatory**: final federal/state/local filings, liabilities paid, clearance confirmations, license/permit closures, foreign qualification withdrawals.
- **Filing requirements**: jurisdiction instructions, required language, exhibit labels, signature/notarization rules.

## Core Workflow

### 1. Scope and Statute Map

- Pull current state business-entity and tax-authority instructions before drafting.
- Record entity-specific statutory obligations and filing sequence.
- Flag jurisdiction-variable requirements with: `[VERIFY — State authority requirement: cite exact statute/subsection]`

### 2. Evidence Map

For each report section, confirm inputs, required exhibits, and statutory verification:

| Section | Key Inputs | Required Exhibits | Verify |
|---|---|---|---|
| Identity & background | formation papers, amendments | certified formation docs | jurisdiction statute links |
| Authorization | board/member actions, vote evidence | minutes/consents, proxies | vote threshold statutes |
| Winding up | notices, claim logs | notice/publication proofs, settlements | publication timing rules |
| Assets/liabilities | accounting records, valuations | schedules, payment proofs | asset distribution rules |
| Tax/regulatory closure | final returns, closures | clearance certificates | filing/clearance requirements |
| Certifications | officer statements | signatory authority docs | notary/affirmation rules |

### 3. Report Section Order

```
1.  Cover and Jurisdictional Basis
2.  Entity History and Structure
3.  Authorization of Dissolution
4.  Winding-Up Narrative
5.  Asset Inventory and Disposition
6.  Liability and Claim Resolution
7.  Distribution to Equity Holders
8.  Tax and Regulatory Compliance
9.  Foreign Qualification & Permit Closures
10. Supporting Exhibits and Index
11. Certifications and Signatures
12. Final Compliance Checklist
```

### 4. Section Schema

Every section must contain:

```
Section [#] — [Title]
Summary:
Facts:
Support:        (exhibit citation)
Cross-reference: (related sections/exhibits)
Risk/Gap:       ([VERIFY] items or open issues)
```

### 5. Numeric Schedules

Use tables for all financial data:

- **Asset disposition**: asset class, basis, valuation method, disposal method, date, proceeds/recipient.
- **Liability**: creditor, claim type, claimed amount, outcome, payment/reserve date, exhibit.
- **Distribution**: owner, percentage/class rights, amount, payment method, date.

### 6. Deliverables

- Full draft report.
- Exhibit index with file map.
- Open-issues list (if any): state why unresolved, impact, remediation step.

## Quality Checklist

Do not finalize until every row passes:

| Check | Pass? |
|---|---|
| Every substantive assertion has exhibit support | |
| All totals reconcile across schedules and narrative | |
| Statute/rule references are current and jurisdiction-specific | |
| Creditor satisfaction confirmed before equity distribution | |
| Signature block matches state and governance requirements | |
| Exhibit index is complete with valid labels | |
| All `[VERIFY]` items resolved or surfaced as open issues | |

## Pitfalls

- **Jurisdiction bleed**: never carry another state's language without verifying current authority.
- **Name mismatches**: preserve exact entity name spelling from filings throughout.
- **Unsupported assertions**: every paragraph on authorization, notice, taxes, and distribution must cite an exhibit.
- **Soft language on contingencies**: document contingent liabilities and disputed claims with explicit reserve/provision mechanics.
- **Inconsistent formatting**: use one format for all money figures and dates across the entire report.
- **Premature finalization**: any `[VERIFY]` tag blocks finalization until cleared or explicitly listed as an open issue.
