---
name: assignment-and-assumption-of-leases
title: Assignment and Assumption of Leases
description: Drafts an Assignment and Assumption of Leases transferring tenant leases from seller (Assignor) to buyer (Assignee) as a closing document to a commercial property PSA. Trigger when closing a commercial property sale with existing tenant leases or when a user needs lease assignment/assumption language for a real estate transaction.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/assignment-and-assumption-of-leases
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [agreement, drafting, transactional]
---

# Assignment and Assumption of Leases

Drafts a closing-ready agreement transferring all landlord rights and obligations under existing tenant leases from Assignor (seller) to Assignee (buyer) in a commercial property sale.

## Prerequisites

Collect before drafting. Use `[INSERT]` placeholders for missing items and prepend a required-information checklist.

1. **PSA** — closing date, governing law, lease-specific provisions
2. **Lease schedule / rent roll** — tenant names, suites, dates, terms, rent, deposits
3. **Party details** — legal names, entity types, addresses for Assignor and Assignee
4. **Effective date** — typically the PSA closing date
5. **Security deposit total** — aggregate amount transferred at closing

## Quick Start

1. Gather prerequisites above
2. Draft document following the output structure below
3. Run through the pitfalls checklist before finalizing

## Output Structure

### Header
- Title: `ASSIGNMENT AND ASSUMPTION OF LEASES`
- Dated: `as of [Month Day, Year]`
- Full legal entity names, types, and addresses

### Recitals (3–4 lettered paragraphs)

| Recital | Content |
|---------|---------|
| A | PSA reference — date, property address/legal description |
| B | Assignor is landlord under leases on Exhibit A |
| C | Intent to assign/assume all landlord rights per PSA |
| D *(if needed)* | Material facts: estoppels, modifications, known disputes |

### Operative Provisions

**1. Assignment** — Transfer all of Assignor's right, title, and interest in the Leases, including:
- Accrued and future rents
- Security deposits, letters of credit, guaranties
- TI allowances, options, renewal/expansion rights

**2. Assumption** — Assignee assumes all landlord obligations arising **on or after** Effective Date, including honoring deposits, TI obligations, and surviving tenant rights.

**3. Indemnification**

| Party | Scope |
|-------|-------|
| Assignor → Assignee | Claims from landlord obligations/defaults **before** Effective Date |
| Assignee → Assignor | Claims arising **on or after** Effective Date |

Both survive closing. Include notice, defense rights, and settlement approval mechanics.

**4. Security Deposit Transfer** — Assignor transfers all deposits (plus statutory interest if required) totaling `$[AMOUNT]`. Assignee acknowledges receipt and assumes return obligations. Assignor released from deposit liability after Effective Date.

**5. Rent Proration** — Assignor entitled to rents before Effective Date; Assignee on or after. Governed by PSA or closing statement.

**6. Relationship to PSA** — Assignment subject to PSA terms; PSA controls on conflict. Cross-reference PSA sections on lease assignment, estoppels, prorations.

### General Provisions
- Governing law (property state or per PSA), successors/assigns, counterparts (including electronic), entire agreement, severability

### Signature Blocks
Entity name → Signatory name/title → Date (both parties)

### Exhibit A — Lease Schedule

| Tenant | Suite | Lease Date | Commencement | Expiration | Base Rent/Mo. | Security Deposit | Notes |
|--------|-------|------------|--------------|------------|---------------|-----------------|-------|
| [Name] | [#] | [Date] | [Date] | [Date] | $[Amount] | $[Amount] | Amendments, options, disputes |

## Pitfalls and Checks

- **Anti-assignment clauses**: Verify sale-of-property exception applies per each lease or obtain tenant consent
- **Ownership-change triggers**: Review co-tenancy, exclusive use, and recapture rights triggered by landlord change
- **Tenant notice**: Flag state-specific requirements for notifying tenants of assignment and new landlord contact `[VERIFY by state]`
- **Security deposit statutes**: Verify state rules on interest accrual, escrow, and transfer procedures `[VERIFY by state]`
- **Cross-document consistency**: Align effective date and defined terms with deed, bill of sale, closing statement, and estoppel certificates
- **Problem leases**: Add carve-outs for leases with active defaults, disputes, or open cure obligations
- **Defined terms**: Capitalize consistently — Assignor, Assignee, Leases, Property, Purchase Agreement, Effective Date

---

**Key changes made:**
- **Description**: Tightened and added explicit trigger guidance ("Trigger when...")
- **Added Quick Start** section for fast orientation
- **Consolidated prose**: Removed redundant heading-level overview (was restating the description), compressed operative provisions into single-line intros with sub-bullets
- **Renamed "Guidelines" → "Pitfalls and Checks"** for scannability
- **Compressed General Provisions** into a single bullet line instead of five separate bullets
- **Reduced token count** throughout while preserving all legal substance and domain accuracy
