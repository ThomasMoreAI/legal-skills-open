---
name: notice-of-annual-shareholders-meeting
title: Notice of Annual Shareholders Meeting
description: Drafts a U.S. corporate annual shareholders meeting notice enforcing record-date accuracy, notice timing, quorum/vote thresholds, proxy logistics, and agenda disclosures under charter/bylaws and state statutes. Triggers on requests involving annual meeting notice, shareholder meeting notice, record date, quorum, proxy voting, or annual meeting agenda.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/notice-of-annual-shareholders-meeting
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [drafting, letter]
---

# Notice of Annual Shareholders Meeting

Produces a legally defensible annual-meeting notice that protects shareholder voting rights and supports validity of meeting actions.

## Gather Before Drafting

- State of incorporation, charter/articles, bylaws, shareholder agreements
- Legal name, stock classes, voting rights per class
- Meeting date/time/timezone, format (in-person / virtual / hybrid), venue or platform URL
- Record date (COB cutoff) and transfer-agent or stock-ledger source
- Full agenda with proposed resolutions and board recommendations
- Quorum rules and vote thresholds (ordinary, special, class-specific)
- Public companies: proxy materials, filing references, e-delivery settings
- Authorized signatory and approved distribution method

## Core Workflow

### 1. Validate Compliance Inputs

For each item, apply the stricter of statute vs. bylaws:

- **Notice window** — use the longer minimum notice period.
- **Record date** — only holders of record at COB are eligible; confirm against transfer agent/ledger.
- **Meeting access** — no ambiguity on venue, platform, or registration steps.
- **Vote standards** — tie each proposal to its exact threshold (majority, supermajority, class vote).
- **Proxy rules** — deadline, delivery methods, revocation procedure, and counting rules must be explicit.

### 2. Draft Required Sections

1. Header: "NOTICE OF ANNUAL MEETING OF SHAREHOLDERS"
2. Corporate identity and legal authority (bylaws + state act)
3. Meeting date, time, timezone, place or platform
4. Record-date statement and voting eligibility
5. Agenda with short description of each item
6. Quorum and voting requirements by proposal type
7. Proxy issuance, delivery, revocation, and late-proxy handling
8. Shareholder contacts and material-access instructions
9. Signature block: date, officer name, title, contact

### 3. Template

```text
NOTICE OF ANNUAL MEETING OF SHAREHOLDERS
[Corporation Legal Name], a [State] corporation

To: Shareholders of record as of [Record Date] at close of business.

Notice is hereby given that a meeting of shareholders will be held on [Meeting Date], at [Time] [Timezone], at [Location / Virtual Platform].

This meeting will consider:
1. [Agenda Item]
2. [Agenda Item]
3. [Agenda Item]

Record Date: [Record Date] (COB)
Eligible Voters: [Class-by-class voting rights]
Quorum: [Quorum standard]
Vote Requirements: [Majority / supermajority / class vote per proposal]

Proxy Instructions:
- Deadline: [Deadline]
- Delivery: [Mail / telephone / electronic]
- Revocation: [Method / recipient / last-minute rule]

[Contact for materials, accommodations, and inquiries]

Sincerely,
[Name], [Title]
[Date]
```

### 4. Quality Gates

- Notice timing verified against both statute and bylaws minimums.
- Distribution method and proof-of-service documented.
- Proposal descriptions match actual resolutions.
- Public-company filing/disclosure references reconciled [VERIFY].
- SEC proxy rule compliance confirmed before final output [VERIFY].

## Pitfalls

- Never include unnoticed substantive business under "other business."
- Do not conflate annual-meeting notice periods with special-meeting timing rules.
- For public companies, federal reporting obligations override internal defaults when they conflict.
- Keep statutory and bylaw requirements consistent across header, body, and signature block.
- Include contingency language for location/platform changes.
