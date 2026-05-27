---
name: notice-to-perform
title: Notice to Perform
description: Drafts a U.S. residential real estate Notice to Perform (cure notice) identifying contractual defaults, demanding specific cure actions, and preserving remedies. Use when drafting a notice to perform, notice to cure, default notice, or breach-and-cure letter for a residential purchase agreement or lease.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/notice-to-perform
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
---

# Notice to Perform

Draft a legally compliant cure demand that serves as an evidentiary record.

## Prerequisites

Collect before drafting:

1. Executed agreement with all addenda, schedules, and disclosures
2. Party names, roles, and service addresses exactly as in the agreement
3. Specific breaches with dates, amounts, and documentary support
4. Governing law, venue, and property location
5. Contract notice clause (method, address, timing, cure period)
6. Statutory notice requirements for the jurisdiction and contract type

## Required Inputs

| Field | Source |
|---|---|
| Sender and recipient legal names and roles | Agreement |
| Property address and APN | Agreement / records |
| Agreement title and execution date | Agreement |
| Notice clause section reference | Agreement |
| Breach description with dates and amounts | Records |
| Cure actions required | Agreement |
| Cure deadline | Contract / statute |
| Service method and address | Contract / statute |

## Workflow

### 1. Build the Timeline

| Date | Event | Evidence |
|---|---|---|
| YYYY-MM-DD | Obligation due | Invoice / email / section |
| YYYY-MM-DD | Nonperformance occurred | Record |
| YYYY-MM-DD | Prior notice or communication | Email / letter |

### 2. Determine Cure Period

| Basis | Rule | Deadline |
|---|---|---|
| Contract | Stated cure period and method | Service date + contract days |
| Statute | Minimum notice period applies | Service date + statutory days |
| Reasonableness | Only if no contract or statute governs | Fact-based, documented |

If statutory requirements are uncertain, mark with `[VERIFY]` and request confirmation.

### 3. Draft the Notice

Follow this checklist:

- [ ] Identify parties, roles, and agreement details
- [ ] Quote the exact breached provisions with section numbers
- [ ] State factual breach narrative with dates and amounts
- [ ] Specify cure actions in measurable terms
- [ ] Set deadline with date, time, and time zone
- [ ] State consequences tied to contract and law
- [ ] Include reservation of rights
- [ ] Include signature block and authority
- [ ] Add certificate of service with method details

### 4. Notice Template

​
