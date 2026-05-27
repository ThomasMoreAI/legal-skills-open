---
name: bill-of-sale-personal-property
title: Personal Property Bill of Sale (CRE)
description: Drafts a U.S. CRE personal property Bill of Sale transferring equipment, fixtures, FF&E, inventory, and other tangible assets. Handles inclusion/exclusion schedules, price allocation, tax responsibility, and risk of loss. Trigger when the user needs a bill of sale, asset schedule, equipment transfer document, or personal property conveyance tied to a CRE closing.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/bill-of-sale-personal-property
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [agreement, drafting, transactional]
---

# Personal Property Bill of Sale (CRE)

Transfers tangible personal property in a CRE transaction with price allocation, risk allocation, and closing mechanics aligned to the purchase agreement.

## Quick Start

Gather before drafting:

| Input | Detail |
|---|---|
| Parties | Legal names, entity type, formation state, addresses, signatory title |
| Asset schedule | Included items with identifiers (serial/VIN/model); excluded items list |
| Price | Total consideration, allocated personal property amount, payment method/timing |
| Taxes | Sales/use tax allocation and reporting responsibility |
| Risk & delivery | Risk-of-loss transfer point, removal location/deadline, transport costs |
| Reps/warranties | Title, authority, liens, condition model (AS IS or limited warranty) |
| PSA alignment | Defined terms, closing conditions, survival, remedies from purchase agreement |
| Jurisdiction | Governing law state, notarization requirement |

## Drafting Workflow

1. **Mirror PSA terms.** Import defined terms from the purchase agreement verbatim — do not re-define.
2. **Insert parties.** Full legal names, entity types, formation states, authority language.
3. **Set effective date.** Align transfer trigger to closing date/time in PSA.
4. **Attach asset schedule (Exhibit A).** List each item with category, manufacturer, model, serial/VIN, quantity, location. Add explicit exclusions in Exhibit B.
5. **State consideration & allocation.** Purchase price, payment method, credits/deposits. Note IRS Form 8594 obligation if applicable.
6. **Assign tax responsibility.** Specify which party handles sales/use/transfer taxes and filings.
7. **Choose condition model.** Either "AS IS, WHERE IS" (conspicuous disclaimer) with title/authority reps, or limited condition warranties.
8. **Allocate risk of loss & delivery.** Transfer point, removal deadline, transport costs on Buyer.
9. **Add conditions precedent.** Tie effectiveness to real property closing if applicable.
10. **Add indemnity/survival only if negotiated in PSA.** Otherwise omit for clean close.
11. **Close with governing law, counterparts, e-signature, and execution blocks.**

## Template

Adapt for jurisdiction and deal terms:

```text
BILL OF SALE (PERSONAL PROPERTY)

This Bill of Sale is made as of [DATE] by and between:
Seller: [LEGAL NAME], a [ENTITY TYPE] organized under [STATE], at [ADDRESS] ("Seller").
Buyer: [LEGAL NAME], a [ENTITY TYPE] organized under [STATE], at [ADDRESS] ("Buyer").

1. Transfer. Seller sells, assigns, and transfers to Buyer all right, title, and interest in the personal property in Exhibit A ("Personal Property"), with all accessories, spare parts, manuals, and warranties, except items in Exhibit B (Excluded Property).

2. Consideration. $[AMOUNT] ([WORDS]), payable by [METHOD] at [TIME]. Deposit/credit of $[AMOUNT] applied to purchase price.

3. Allocation. $[AMOUNT] allocated to Personal Property. Parties will file IRS Form 8594 consistent with this allocation if applicable.

4. Taxes. [Seller/Buyer] responsible for sales/use/transfer taxes and required filings.

5. Title; Authority. Seller has good title free of liens except [PERMITTED LIENS] and authority to transfer.

6. Condition. [AS IS, WHERE IS — conspicuous format / OR limited condition warranties].

7. Risk of Loss; Delivery. Risk passes to Buyer [AT CLOSING/UPON PAYMENT]. Buyer removes from [LOCATION] by [DATE]; Buyer bears removal and transport costs.

8. Conditions Precedent. Effective only upon closing under [PSA NAME/DATE].

9. Governing Law. Governed by [STATE] law.

10. Counterparts; E-Signatures. May be executed in counterparts and by electronic signature.

SELLER: [ENTITY NAME]
By: __________________________ Name: [PRINT] Title: [TITLE]

BUYER: [ENTITY NAME]
By: __________________________ Name: [PRINT] Title: [TITLE]
```

**Exhibit A — Included Personal Property**

| Category | Manufacturer | Model | Serial/VIN | Qty | Location | Notes |
|---|---|---|---|---|---|---|

**Exhibit B — Excluded Property**

| Item | Reason | Owner/Disposition |
|---|---|---|

## Pitfalls & Checks

- **Exclusions required.** Every on-site item that does not convey must appear in Exhibit B.
- **AS IS conspicuousness.** If disclaiming condition, format the clause in bold/caps per UCC § 2-316 guidance.
- **Titled property.** Vehicles, vessels, or aircraft need separate title-transfer mechanics and may require notary blocks.
- **PSA alignment.** Effective date, defined terms, and closing conditions must match the purchase agreement exactly.
- **Deferred payment.** If Seller retains a security interest, include UCC-1 filing obligations.
- **Tax compliance.** Confirm sales/use tax responsibility and reporting for the governing state.
- **No extras.** Do not add inspection rights or indemnity unless negotiated in the PSA.

---

Key changes from the original:

- **Frontmatter description** — tightened to third-person with clear trigger guidance, removed the "trigger keywords" list in favor of natural trigger language
- **Collapsed Prerequisites + Inputs Checklist** into a single "Quick Start" table — eliminates the redundancy between the two original sections
- **Renamed "Output Structure / Process"** to clearer "Drafting Workflow" with numbered steps preserved
- **Trimmed template** — removed redundant phrasing ("For good and valuable consideration"), compressed execution blocks
- **Renamed "Guidelines" to "Pitfalls & Checks"** with bold lead terms for scannability
- **Removed** the separate Prerequisites section entirely (folded into Quick Start table)
