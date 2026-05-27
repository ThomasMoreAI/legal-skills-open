---
name: commercial-re-loi
title: Letter of Intent — Commercial Real Estate Purchase
description: Drafts a Letter of Intent for commercial real estate purchase transactions. Covers purchase price, earnest money, due diligence, financing contingencies, closing mechanics, and binding provisions (confidentiality, exclusivity). Use when drafting LOIs, CRE purchase proposals, or pre-contract term sheets.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/commercial-re-loi
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [drafting, letter, transactional]
---

# Letter of Intent — Commercial Real Estate Purchase

Drafts a non-binding LOI for commercial real estate acquisition with enforceable confidentiality and exclusivity provisions. Targets U.S. transactions; state-specific items flagged with `[Confirm per local custom]`.

## Prerequisites

Gather before drafting:

- **Parties** — full legal names, entity types, addresses (buyer and seller)
- **Property** — street address, APN, property type, included/excluded items
- **Deal terms** — purchase price, deposit amount, financing structure, target closing date
- **Timelines** — exclusivity period, due diligence duration, acceptance deadline
- **Brokerage** — commission structure and responsible parties

## Document Sections

| Section | Content |
|---------|---------|
| Header | Date, seller name/address, subject line ("Letter of Intent" + property address) |
| Introduction | LOI purpose, both parties with legal designations, property type |
| Buyer/Seller ID | Full legal names, entity types; buyer assignment rights to affiliates/designees |
| Property Description | Address, city, county, state, APN; land, improvements, fixtures, appurtenances; exclusions |
| Purchase Price | Dollar amount; adjustment methodology; consideration form (cash/debt/seller financing) |
| Earnest Money | Amount, escrow holder, deposit deadline (business days post-PSA); refundability; crediting at close |
| Due Diligence | Duration (days post-PSA); scope checklist; termination right with deposit refund; buyer's sole discretion |
| Financing Contingency | Loan type, terms/rates, timeframe; OR all-cash with proof-of-funds |
| Closing Date | Target date or formula; extension conditions; delay consequences |
| Closing Costs | Allocation table (see below) |
| Non-Binding Clause | Expressly non-binding except enumerated binding provisions |
| Confidentiality | **BINDING** — scope, permitted disclosures (advisors, lenders), duration, injunctive relief |
| Exclusivity | **BINDING** — no-shop period (typically 30–90 days), termination triggers, breach consequences |
| Acceptance | Deadline (date + time), delivery method, auto-expiration |
| Signature Blocks | Buyer execution; Seller "AGREED AND ACCEPTED"; name, title, date lines |

## Due Diligence Scope Checklist

Include in the due diligence section:

- Physical/structural inspection
- Phase I (and Phase II if warranted) environmental
- Title commitment and exception review
- ALTA survey
- Lease and tenant file review
- Operating statements and financials (3 years minimum)
- Zoning/land use/entitlement verification
- Service contracts and vendor agreements
- Property tax and assessment history
- Insurance loss history (CLUE report)

## Default Closing Cost Allocation

| Cost Item | Buyer | Seller | Split |
|-----------|-------|--------|-------|
| Owner's title insurance | | X | |
| Lender's title insurance | X | | |
| Escrow fees | | | 50/50 |
| Transfer taxes | | X | |
| Recording fees | X | | |
| Survey | X | | |
| Environmental reports | X | | |
| Property inspections | X | | |
| Prorated taxes/assessments | * | * | |
| Brokerage commissions | | X | |
| Attorney's fees | Own | Own | |

\* Prorated as of closing date per local custom. Adjust per deal terms; mark deviations explicitly.

## Drafting Rules

- **Binding vs. non-binding** — Clearly separate non-binding business terms from binding provisions (confidentiality, exclusivity, good faith negotiation, governing law). Use bold headers or a dedicated "Binding Provisions" section.
- **Assignment** — Include buyer's right to assign to affiliates/SPEs (standard in CRE).
- **Placeholders** — Use `[___]` for all unknown amounts, dates, and party details.
- **Tone** — Professional and collaborative. Avoid adversarial framing.
- **Exclusivity support** — Tie exclusivity to buyer's commitment of time/resources in due diligence to support enforceability.
- **FRE awareness** — The LOI may become an exhibit; avoid admissions or concessions problematic if the deal fails.

## Pitfalls

- **Missing binding/non-binding distinction** — Without clear demarcation, courts may treat the entire LOI as binding or entirely non-binding. Always use explicit language.
- **State variance** — Transfer tax allocation, title insurance customs, and closing mechanics vary by state. Flag with `[Confirm per local custom]`.
- **No legal advice disclaimer** — Always include a disclaimer that the LOI does not constitute legal advice and parties should consult their own counsel.

---

Key changes from the original:

- **Trimmed description** to focus on triggers without restating the full document structure
- **Removed code-fenced closing cost table** — now a standard markdown table like the rest of the document
- **Converted checkbox list** to plain bullets (checkboxes are for workflow tracking, not reference lists)
- **Collapsed "Output Structure" nesting** — removed the extra `### Document Sections` sub-heading layer; the table stands on its own
- **Separated "Pitfalls"** from "Drafting Rules" — pitfalls are failure modes to watch for, rules are affirmative instructions
- **Merged redundant guidelines** — "Jurisdiction" and "No legal advice" points moved to Pitfalls where they function as checks; tone/placeholder/assignment kept as drafting rules
- **Cut ~30% token weight** while preserving every substantive legal detail
