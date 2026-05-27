---
name: cognovit-promissory-note
title: Cognovit Promissory Note
description: 'Drafts a U.S. cognovit promissory note with confession of judgment clause, enforceability gate, and execution formalities. Use when preparing a commercial loan note with cognovit language, confession of judgment, warrant of attorney, or waiver of notice/hearing rights. Triggers: cognovit, confession of judgment, warrant of attorney, waiver of defenses.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/cognovit-promissory-note
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
---

# Cognovit Promissory Note

Draft an enforceable cognovit promissory note compliant with governing-state law. A cognovit clause lets a borrower authorize entry of judgment without prior notice or hearing — most states prohibit or heavily restrict this, so enforceability must be confirmed before drafting.

## Prerequisites

Collect before drafting:

- **Governing law / forum** — state and venue for enforcement
- **Parties** — legal names, entity types, formation states, addresses, authorized signers
- **Loan terms** — principal, rate, term, payment schedule, fees, prepayment
- **Transaction type** — commercial vs consumer classification; any statutory exemptions
- **Authority docs** — resolutions, incumbency certificates, consents (if entity borrower)
- **Collateral / guaranties** — summary of related security documents, if any

## Quick Start

1. Run the **Enforceability Gate** (below) — if cognovit is prohibited, stop and output a standard note + guaranty + security agreement instead.
2. Draft the note using the **Document Sections** outline.
3. Walk the **Checks** list before finalizing.

## Enforceability Gate (Do First)

| Check | Action | Output |
|---|---|---|
| Cognovit permitted? | Research governing-state statutes + recent case law | Allow / deny with citations or `[VERIFY]` |
| Consumer restriction? | Confirm borrower classification | If consumer or mixed-use, treat as **prohibited** unless clear statutory exception |
| Required warnings / format? | Identify mandatory warning text, font size, capitalization, separate acknowledgment | Insert exact statutory warning or `[VERIFY]` |
| Execution formalities? | Check witness / notary / affidavit / attorney requirements | Add required signature formalities |

**If prohibited or materially restricted:** output alternative structure (standard note + guaranty + security agreement) and stop.

## Document Sections

### 1. Preamble and Parties

- Date, principal (numeric and words)
- Lender and Borrower: legal name, entity type, formation state, address, signatory title
- Authority evidence: resolution/consent, incumbency, power/authority certification

### 2. Economic Terms

| Term | Details |
|---|---|
| Principal | Amount; fees/points treatment |
| Interest | Fixed/variable; index, margin, caps/floors; accrual method; day-count |
| Payments | Amounts, dates, schedule type, grace period |
| Application | Order: fees → interest → principal (or specified) |
| Prepayment | Permitted? Penalty? Formula; usury compliance |

### 3. Confession of Judgment Clause

Include all of:

- **Authority grant** — borrower authorizes any attorney to confess judgment after default
- **Scope** — principal, interest, fees, costs, attorney fees
- **Timing** — upon default or after cure period
- **Forum** — permitted courts; must align with governing-law / venue clause
- **Waivers** — notice, hearing, defenses, discovery, jury trial (if allowed)
- **Statutory warning** — exact required text and formatting per governing state

### 4. Defaults and Remedies

- Monetary default (failure to pay; grace period)
- Cross-default (thresholds, if applicable)
- Insolvency events (bankruptcy, assignment for benefit of creditors)
- Misrepresentation (material statements)
- Collateral events (if secured: impairment, transfer, insurance failures)
- Remedies: acceleration, confession of judgment, collection costs

### 5. Governing Law, Jurisdiction, Venue

- Governing law with substantial relationship to transaction
- Consent to jurisdiction and venue
- Waiver of forum non conveniens (if allowed)
- **Jury trial waiver** — must be conspicuous

### 6. Execution and Acknowledgments

- Signature blocks with titles and entity capacity
- Witness / notary blocks (if required by state)
- Separate cognovit acknowledgment (if required by state)

### 7. Exhibits (as needed)

- Amortization schedule
- Authority documents
- Collateral schedule

## Template Skeleton

```text
COGNOVIT PROMISSORY NOTE

Date: [Date]
Principal Amount: $[Amount] ([Words])

FOR VALUE RECEIVED, [Borrower] ("Borrower") promises to pay to the
order of [Lender] ("Lender") the Principal Amount plus interest:

1.  Interest.
2.  Payments.
3.  Application of Payments.
4.  Prepayment.
5.  Events of Default.
6.  Remedies; Acceleration.
7.  Confession of Judgment. [Full clause + statutory warning + waivers]
8.  Governing Law; Jurisdiction; Venue.
9.  Jury Trial Waiver. [CONSPICUOUS]
10. Notices.
11. Miscellaneous.

BORROWER:                         LENDER:
By: ______________                By: ______________
Name/Title:                       Name/Title:
Date:                             Date:

[Notary / Witness Blocks if required]
[Separate Cognovit Acknowledgment if required]
```

## Checks

- [ ] Enforceability gate passed — cognovit is permitted for this transaction type in the governing state
- [ ] Consumer / mixed-use classification confirmed; if consumer, cognovit clause omitted
- [ ] Statutory warning language is exact, conspicuous, and placed per statute
- [ ] Confession clause forum aligns with governing law and has substantial relationship to transaction
- [ ] Usury analysis complete — includes all fees/charges treated as interest; exemptions noted
- [ ] Waivers are conspicuous and not buried in boilerplate
- [ ] Execution formalities match governing-state requirements (witnesses, notary, acknowledgment)
- [ ] If enforceability is unclear, alternative structure (standard note + guaranty + security agreement) recommended instead
