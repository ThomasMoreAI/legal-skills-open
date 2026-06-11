---
name: capital-call-notice
title: Capital Call Notice
description: Drafts U.S. capital call notices for PE, VC, or fund-managed LLCs aligned to LPA/operating agreement procedures and side letters. Use when drafting a capital call notice, drawdown notice, capital contribution demand, unfunded commitment call, or LP/GP capital call letter.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/capital-call-notice
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: investment-funds
language: en
---

# Capital Call Notice

Formal notice demanding capital contributions under a governing agreement with investor-level calculations, payment mechanics, and default remedies.

## Quick Start

Gather before drafting:

| Item | Detail | Source |
|---|---|---|
| Governing document | Full title, date, sections authorizing calls and remedies | LPA / Operating Agreement |
| Notice period | Minimum days, delivery method, timing rule | Notice clause |
| Allocation method | Pro rata or formula; side-letter deviations | Capital call provisions |
| Call purpose | Investment/expense/reserve; permitted use basis | Investment memo / budget |
| Default remedies | Interest rate, dilution/forfeiture, cure period | Default clause |
| Wire instructions | Bank, ABA, SWIFT, account name/number | Treasury |
| Fund/entity details | Legal name, GP/manager, signatory, address | Formation docs |
| Investor schedule | Commitments, contributions to date, unfunded, ownership % | Fund admin |

## Core Workflow

### 1. Build Capital Call Schedule

Attach as exhibit. One row per investor:

| Investor | Commitment | Contributed | Unfunded | Ownership % | Amount Due | Side Letter Notes |
|---|---|---|---|---|---|---|
| {Name} | {$} | {$} | {$} | {%} | {$} | {If any} |

### 2. Draft Calculation Statement

One paragraph stating: allocation formula, agreement compliance confirmation, aggregate call amount, and total fund commitment base.

### 3. Draft Notice Letter

```text
[Fund Letterhead]

Date: {Month DD, YYYY}

To: {Investor Legal Name}
Attn: {Contact Name/Title}
Address: {Address}

Re: Capital Call Notice under {Agreement Title} dated {Agreement Date}

Dear {Investor Name}:

Pursuant to Section {##} of the {Agreement Title} dated {Agreement Date} (the "Agreement"), the General Partner/Manager hereby issues this Capital Call Notice.

1. Aggregate Call Amount: {Total Amount}.
2. Your Pro Rata Amount Due: {Investor Amount}.

Purpose of Call: {Brief purpose aligned with permitted uses}.

Payment Due Date: {Month DD, YYYY} by {Time} {Time Zone}. Not less than the minimum notice period under Section {##}.

Payment Instructions:
Beneficiary: {Account Name}
Bank: {Bank Name}, {Bank Address}
ABA/Routing: {ABA}
SWIFT: {SWIFT}
Account No.: {Account Number}
Reference: {Reference Code / Investor ID}

Wire confirmation: {Email} with {Required details}.

Default Remedies: Failure to fund by the due date triggers remedies under Section {##}, including {exact remedies and cure period}.

Questions: {Contact Name}, {Title}, {Phone}, {Email}.

Sincerely,

{Authorized Signatory}
{Title}
{General Partner/Manager Entity}
```

### 4. Populate Default Remedies Matrix

| Remedy | Trigger | Section | Notes |
|---|---|---|---|
| Default interest | Late payment | §{##} | Rate, accrual start |
| Dilution/forfeiture | Failure to cure | §{##} | Formula, timing |
| Distribution suspension | Default status | §{##} | Duration |
| Forced transfer | Continued default | §{##} | Process, valuation |

### 5. Confirm Delivery

State the delivery method required by the notice clause. Verify delivery address or email on record matches agreement requirements.

## Pitfalls

- Cite exact section numbers from the governing agreement — never paraphrase.
- Use full month names for dates; always specify time zone for deadlines.
- Do not exceed authorized purposes; tie each use to the agreement.
- Apply side-letter modifications only to the applicable investor; keep other terms confidential.
- State remedies verbatim from the agreement; include cure periods and required follow-up notices.
- Verify signatory authority and entity names against formation docs.
- Do not disclose non-public deal terms unless permitted.
- Confirm delivery method complies with notice provisions and any electronic delivery requirements.
- Mirror governing law and jurisdiction — do not introduce new terms.
- Cross-check arithmetic: amounts must be consistent across letter body and schedule.
