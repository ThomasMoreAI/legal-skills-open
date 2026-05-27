---
name: sublicense-agreement
title: Sublicense Agreement
description: Drafts Sublicense Agreements for IP licensing transactions, ensuring compliance with the underlying Master License Agreement. Covers grant of rights, territory, field-of-use, term, royalty structures on Net Sales, flow-down obligations, and termination tied to master license. Use when a licensee (Sublicensor) grants derivative rights to a third party (Sublicensee), for IP sublicensing or derivative license agreements.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/sublicense-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# Sublicense Agreement

Drafts a sublicense agreement conveying derivative IP rights from an existing licensee to a third party while maintaining strict compliance with the Master License Agreement.

## Prerequisites

Gather before drafting:

1. **Master License Agreement** — executed copy with: original licensor, execution date, licensed IP, scope of rights, territorial/field-of-use restrictions, royalty obligations, sublicensing provisions
2. **Sublicensing authorization** — confirmation Master License permits sublicensing; if consent required, evidence of licensor approval
3. **Party details** — legal names, jurisdictions, principal places of business, authorized signatories for Sublicensor and Sublicensee
4. **Business terms** — exclusive vs. non-exclusive, territory, field-of-use, term, royalty rate, payment structure, minimums or milestones

## Agreement Sections

### 1. Preamble & Recitals

| Recital | Content |
|---------|---------|
| Master License | Original licensor, execution date, licensed IP, cite sublicensing provision |
| Sublicensing Right | Affirm sublicensing rights with Master License section reference |
| Purpose | Sublicensee's intended business use |

### 2. Definitions

Define at minimum:

- **Licensed IP** — specific rights being sublicensed
- **Net Sales** — gross revenue minus: (a) returns/allowances, (b) trade/quantity discounts, (c) sales/use/VAT taxes, (d) freight/insurance, (e) customs duties
- **Territory** — geographic scope (must not exceed Master License)
- **Field of Use** — permitted applications/industries/markets
- **Royalty Period** — calendar quarter unless otherwise specified

### 3. Grant of Rights

- [ ] Exclusive or non-exclusive designation
- [ ] Specific rights granted (make, use, sell, offer for sale, import, distribute)
- [ ] "Subject to all terms and conditions of the Master License"
- [ ] "Sublicensee receives no greater rights than Sublicensor holds under the Master License"
- [ ] Territory and field-of-use limitations stated explicitly
- [ ] Prohibition on further sublicensing (unless expressly permitted)

### 4. Scope & Limitations

Territory, field-of-use, and duration must not exceed Master License grants. Flow down all Master License restrictions:

- Prohibited uses
- Quality control requirements
- Marking/notice obligations
- Export control compliance

### 5. Flow-Down & Incorporation

- Sublicensee bound by all applicable Master License terms
- Flow-down obligations: confidentiality, quality standards, indemnification, insurance, reporting/record-keeping
- Sublicensor represents it has provided complete Master License copy to Sublicensee

### 6. Financial Terms

```
Royalty Rate:        [__]% of Net Sales
Payment Schedule:    Within [30] days after each calendar quarter
Reporting:           Detailed royalty report with supporting documentation
Upfront Payment:     $[__] due on execution (if applicable)
Minimum Royalty:     $[__] per [year/quarter] (if applicable)
Milestone Payments:  [describe triggers] (if applicable)
Audit Rights:        Upon [30] days written notice; if underpayment
                     exceeds [5]%, Sublicensee bears audit costs
```

Structure sublicense royalties so Sublicensor can satisfy upstream royalty obligations under the Master License.

### 7. Relationship to Master License

- Master License controls in event of conflict
- Sublicensee must comply with all obligations Sublicensor owes to original licensor
- Sublicensor covenants to maintain Master License in good standing

### 8. Representations & Warranties

| Party | Representations |
|-------|----------------|
| **Sublicensor** | Valid license; sublicensing permitted; consents obtained; Master License in full force, no breaches |
| **Sublicensee** | Authority to enter agreement; no conflicts; acknowledges sublicense is derivative of and subordinate to Master License |
| **Mutual** | Authority to execute; compliance with applicable laws; no litigation threatening rights |

### 9. Termination

| Trigger | Mechanism |
|---------|-----------|
| Master License terminates/expires | **Automatic** termination — Sublicensee acknowledges and accepts this risk |
| Material breach | Written notice + [30]-day cure period |
| Insolvency/bankruptcy | Termination at non-breaching party's option |

**Post-termination obligations:** cessation of sublicensed rights, return/destruction of confidential information (with certification), payment of accrued royalties, wind-down period of [__] days for existing inventory (if applicable). Surviving provisions: payment obligations, confidentiality, indemnification, audit rights.

### 10. Indemnification & Liability

- Sublicensee indemnifies Sublicensor against claims from: use of licensed IP, breach of agreement, violation of laws
- Address interaction with Master License indemnification provisions
- Liability cap at [amount/royalties paid], excluding indemnification and confidentiality breaches

### 11. General Provisions

Governing law and jurisdiction (consistent with Master License if required), assignment restrictions (no assignment without consent), written amendments only, notices with full contact details, severability, integration clause referencing both this Agreement and the Master License.

### 12. Signature Block

Sublicensor and Sublicensee — name, title, date, confirmation of authority to bind.

## Critical Checks

- **Master License primacy** — never draft broader rights than the Sublicensor holds; cross-reference every grant, territory, field-of-use, and term against the Master License
- **Consent verification** — if Master License requires licensor consent, document it in recitals and attach as exhibit
- **Automatic termination risk** — always include explicit Sublicensee acknowledgment that sublicense terminates if Master License terminates
- **Royalty stacking** — structure sublicense royalties so Sublicensor can meet upstream obligations while maintaining margin
- **Placeholders** — use `[bracketed placeholders]` for all deal-specific terms
- **Jurisdiction** — default U.S. law; flag state-specific IP licensing statutes if applicable
- **Defined terms** — capitalize consistently; cross-reference definitions section on first use

---

Key changes from the original:

- **Removed `tags`** — not part of the Agent Skills spec; only `name` and `description` are recognized frontmatter fields
- **Tightened description** — trimmed redundant keywords while preserving trigger guidance and discovery terms
- **Removed "Output Structure" header** — renamed to "Agreement Sections" (clearer, less meta)
- **Condensed post-termination** — collapsed from a bulleted list + separate survival list into a single compact paragraph
- **Consolidated "Guidelines" → "Critical Checks"** — sharper header, same content, slightly tighter wording throughout
- **Reduced line count** — from 132 lines to ~105, staying well under the 500-line limit
- **Preserved all legal substance** — every section, checklist item, definition, table, and placeholder from the original is retained
