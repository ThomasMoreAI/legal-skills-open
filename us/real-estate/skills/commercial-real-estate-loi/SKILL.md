---
name: commercial-real-estate-loi
title: Commercial Real Estate Purchase LOI
description: Drafts a U.S. commercial real estate purchase letter of intent (LOI) framing core deal terms as non-binding while isolating binding provisions (confidentiality, exclusivity). Triggers on LOI/term-sheet requests for commercial property acquisition, PSA pre-wire, exclusivity, or due-diligence entry.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/commercial-real-estate-loi
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
---

# Commercial Real Estate Purchase LOI

Proposes deal terms and a negotiation framework for commercial property acquisition while limiting binding effect to specified provisions only.

## Gather Before Drafting

1. **Parties** — legal names, entity types, authority, notice addresses.
2. **Property** — street address, county/state, APN(s), included/excluded assets.
3. **Economics** — price, consideration type, deposit amount and timing, financing posture.
4. **Timeline** — due-diligence period, PSA target, closing target.
5. **Binding scope** — confidentiality terms, exclusivity window, expense allocation, governing law.

## Document Structure

### Header & Intro

- Date, seller name/address, subject line: "Letter of Intent – [Property Address/Name]".
- Identify buyer, seller, property, and intended transaction.
- State non-binding nature except specified sections.

### Core Terms

| Term | Instruction | Placeholder |
|---|---|---|
| Buyer | Full legal name; allow assignment to affiliate/SPE if intended | `[Buyer Legal Name]` |
| Seller | Full legal name; confirm record title holder(s) | `[Seller Legal Name]` |
| Property | Address, county, state, APN(s), improvements, fixtures | `[Property Description]` |
| Purchase Price | Fixed or adjustable; state adjustment method | `[Price]` |
| Consideration | Cash, debt assumption, seller financing, or mix | `[Consideration]` |
| Earnest Money | Amount, timing after PSA, escrow holder, refundability triggers | `[Deposit Terms]` |
| Due Diligence | Days from PSA; scope; buyer discretion; termination right | `[DD Period/Scope]` |
| Financing | Contingent or cash; proof of funds/commitment | `[Financing Terms]` |
| Closing | Target date or days after contingencies; extensions | `[Closing Date]` |
| Closing Costs | Allocation of title, escrow, taxes, surveys, fees | `[Cost Allocation]` |

### Due-Diligence Scope Checklist

- Physical inspections and access rules
- Environmental review and reports
- Title commitment, exceptions, survey
- Leases, rent roll, tenant files, estoppels
- Operating statements and expense history
- Zoning, permitted use, compliance records
- Service contracts and vendor agreements

### Binding Provisions Block

Create a discrete section titled "Binding Provisions" expressly stating these terms bind while all others do not.

| Item | Required Elements |
|---|---|
| Confidentiality | Scope, permitted disclosures, duration, exclusions, remedies |
| Exclusivity | Start, duration, prohibited activities, breach consequences |
| Expenses | Each side bears own costs (or seller reimburses on breach) |
| Governing Law | State law and venue for binding provisions only |

### Acceptance Block

- Acceptance deadline (date/time, delivery method).
- Buyer signature block (name/title/date).
- Seller block labeled "Agreed and Accepted" (name/title/date).

### Optional Clauses (include only if provided)

| Clause | When |
|---|---|
| Tenant Estoppels / SNDA | Multi-tenant or credit-sensitive deals |
| PSA Milestones | Staged diligence or deposit increases |
| Risk Allocation | Casualty/condemnation between LOI and closing |
| Broker Commission | Broker involved or allocation disputes anticipated |

## Pitfalls & Checks

- Restate non-binding status both in the intro and immediately before signature blocks.
- Isolate binding sections; add a severability sentence for those sections only.
- Avoid "agreement to agree" language unless expressly intended.
- Do not include good-faith negotiation obligations unless the client accepts that exposure.
- Use specific dates and dollar amounts; bracket unknowns with `[placeholder]`.
- Verify compliance with local transfer-tax and escrow customs.
- If seller is not the record owner, require evidence of authority to sell.

---
