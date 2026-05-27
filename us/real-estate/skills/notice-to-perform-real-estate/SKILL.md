---
name: notice-to-perform-real-estate
title: Notice to Perform — Residential Real Estate
description: Drafts jurisdiction-aware residential real-estate notices to perform (cure demands) for lease, purchase, or construction agreements where a counterparty has defaulted. Trigger when the user needs a notice to perform, notice to cure, cure notice, demand to perform, residential default notice, or pre-suit notice for a U.S. residential real-estate matter.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/notice-to-perform-real-estate
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [drafting, letter, research, transactional]
---

# Notice to Perform — Residential Real Estate

Produces a litigation-defensible cure demand with breach chronology, statutory notice compliance, remedy mapping, and proof-of-service structure.

## Required Inputs

Collect before drafting. If any item is missing, return a "facts required" list — do not draft until resolved.

1. **Governing instruments** — executed agreement, riders, addenda, incorporated docs
2. **Party identifiers** — legal names, capacities, service addresses, entity IDs
3. **Contractual triggers** — notice clause, cure period, default definitions, remedy ladder, termination/fee provisions
4. **Evidence** — payment history, performance logs, communications, inspection reports, invoices, prior notices
5. **Jurisdiction** — governing law, performance location, mandatory notice form/period/method rules
6. **Sender's posture** — cure, escrow holdback, termination, specific performance, or damages sequencing

## Workflow

### 1. Intake Validation

Block drafting if missing:
- Amount due / due dates
- Governing clause for notice method
- Legal authority to sign
- Delivery details for required recipients

### 2. Breach Matrix

| Date | Obligation | Required Performance | Actual Conduct | Evidence | Contract Section |
|------|-----------|---------------------|---------------|----------|-----------------|

- One row per missed/late payment or performance failure.
- Factual language only — no conclusory legal labels.

### 3. Jurisdiction Check

Confirm and record in a tracking table:

| Item | Status | Source |
|------|--------|--------|
| Cure period minimums | Confirmed / `[VERIFY]` | Agreement + statute |
| Service method sufficiency | Confirmed / `[VERIFY]` | Agreement + statute |
| Termination / acceleration prerequisites | Confirmed / `[VERIFY]` | Contract + law |
| Tenant-protective statutory overrides | Confirmed / `[VERIFY]` | State statute |

Mark any unconfirmed legal text with `[VERIFY]`.

### 4. Draft Structure

1. Header — title, date, sender, recipient
2. Agreement identification — name, date, section references
3. Non-performance chronology — objective facts, evidence-linked
4. Cure demand — measurable conditions
5. Cure deadline — exact date/time/zone; specify "commence by" vs "complete by"
6. Remedies escalation — contract → statutory → judicial
7. Rights preservation / anti-waiver
8. Signature and authority blocks
9. Certificate of service — method, date/time, recipient, tracking/receipt proof

### 5. Style Rules

- Numbered paragraphs for citation reference.
- Short, direct sentences.
- Mirror defined terms from the agreement exactly.

## Notice Template

```
Date:
To:
From:
Re: Notice to Perform – [Agreement Name/Date]
Agreement Date:
Governing Law:
Notice Clause References:
Default Date(s):
Obligations Breached:
Breach Chronology: (table)
Cure Demanded:
Deadline: (date/time + zone)
Cure Acceptance Method/Location:
Consequences of Non-Cure:
Rights Reserved:
Authorized Signatory:
Capacity / Authority:
Certificate of Service:
  - Method:
  - Date/Time:
  - Recipient:
  - Tracking/Receipt:
```

## Final Checklist

1. Every factual assertion traceable to a document.
2. Each cure item objectively measurable.
3. Cure window meets jurisdictional/statutory minimums and contract terms.
4. Delivery method satisfies contract and governing rules.
5. Reservation of rights covers contract, legal, and equitable remedies.
6. No new legal theory introduced without `[VERIFY]`.

## Pitfalls

- Never understate statutory notice requirements in residential contexts.
- Never assume payment totals — calculate from ledger components (principal, fees, interest).
- Do not assert anti-waiver language without addressing the specific legal posture.
- Avoid emotional or persuasive language — keep it enforceable and documentary.
- Use explicit remedy mapping: contract → statutory → litigation.
- Flag uncertain clauses or statutes with `[VERIFY]` and cite the verification source.
