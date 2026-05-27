---
name: seller-consulting-agreement
title: Seller Consulting Agreement
description: 'Drafts a U.S. seller consulting agreement for post-closing transition services in M&A and asset purchase transactions. Use when a seller must provide knowledge-transfer, transition, or consulting services to a buyer after closing. Trigger: consulting agreement, seller services, transition services, post-closing consulting, asset purchase, M&A.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/seller-consulting-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
---

# Seller Consulting Agreement

Drafts a post-closing consulting agreement where the seller provides transition services to the buyer, aligned with the underlying purchase documents.

## Prerequisites

Collect before drafting:

1. **Transaction documents** — purchase agreement, schedules, earnout/holdback terms.
2. **Service scope** — topics, deliverables, frequency, timeline.
3. **Compensation** — rate/retainer, expense policy, payment terms.
4. **Restrictive covenants** — existing non-compete/non-solicit in deal docs.
5. **IP/work product** — ownership expectations, system access needs.
6. **Governing law/venue** — preferred state and dispute forum.

## Quick Start

1. Gather term sheet inputs (see table below).
2. Draft agreement following the clause outline.
3. Cross-check against purchase agreement for conflicts.
4. Attach schedules for complex scope, rates, or restrictions.

## Term Sheet Inputs

Capture these before drafting:

| Item | Prompt | Notes |
|---|---|---|
| Parties | Legal names, entity types, addresses | Seller = consultant; Buyer = client |
| Effective Date | Closing date or specified date | Tie to transaction closing |
| Term | Start/end, renewal mechanics | 6–24 months typical |
| Scope | Specific services + exclusions | Avoid operational control language |
| Deliverables | Meetings, intros, docs, training | Measurable outputs |
| Time/Location | Hours, availability, remote/on-site | Include travel expectations |
| Compensation | Retainer / hourly / project | Define billable increments |
| Expenses | Reimbursable categories + pre-approval | Cap or per diem if needed |
| Confidentiality | Definition + exceptions | Cross-reference deal NDA |
| IP/Work Product | Work-for-hire or assignment | Address pre-existing IP |
| Restrictions | Non-compete / non-solicit | Align with purchase agreement |
| Liability | Cap, exclusions, indemnity | Carve-outs for confidentiality/IP |
| Disputes | Negotiation → arbitration/litigation | Injunctive relief carve-out |
| Notices | Methods + addresses | Email notice if allowed |

## Agreement Outline

```text
1.  Parties; Effective Date
2.  Recitals (reference transaction + consulting purpose)
3.  Definitions (Confidential Information, Services, Work Product)
4.  Scope of Services; Deliverables; Availability; Location
5.  Standard of Performance; No Agency Authority
6.  Independent Contractor; Taxes; Benefits
7.  Compensation; Invoicing; Payment Terms; Late Fees
8.  Expenses; Approval; Documentation
9.  Term; Renewal; Termination (cause + convenience); Effect of Termination
10. Confidentiality; Permitted Disclosures; Return/Destruction
11. Work Product Ownership; IP Assignment; License-Back (if needed)
12. Representations and Warranties (authority, compliance, non-infringement)
13. Indemnification (mutual); Defense control; Mitigation
14. Limitation of Liability; No Consequential Damages; Carve-outs
15. Restrictive Covenants (align with purchase agreement)
16. Governing Law; Venue; Dispute Resolution; Injunctive Relief
17. Miscellaneous (Notices, Assignment, Entire Agreement, Amendment,
    Severability, Counterparts, E-Signatures)
18. Signatures
```

## Optional Schedules

| Schedule | Use When |
|---|---|
| A: Services | Complex deliverables or milestones |
| B: Rates/Retainer | Multiple rates or blended services |
| C: Expense Policy | Detailed travel/expense rules |
| D: Non-Compete/Non-Solicit | Restrictions not in purchase agreement |

## Pitfalls and Checks

- **Purchase agreement alignment** — term, restrictions, and confidentiality must not conflict with the deal documents.
- **No managerial authority** — avoid language granting consultant operational control unless explicitly required.
- **Earnout/holdback linkage** — if compensation ties to earnout, mirror purchase agreement mechanics exactly.
- **Liability cap carve-outs** — carve confidentiality and IP breaches from general liability caps.
- **Return/destruction** — include clear obligation for client materials at termination.
- **Arbitration specifics** — specify seat, rules, arbitrator count, and fee allocation.
- **Non-compete enforceability** — confirm jurisdiction-specific limits on scope and duration.
- **Statutory citations** — mark with [VERIFY] for any added by the drafter.

---

**Key changes made:**

- **Frontmatter**: Removed `tags` (not in spec), tightened description with clear trigger guidance.
- **Eliminated redundancy**: The original had three overlapping sections (clause checklist, drafting template, term sheet) that largely repeated the same items. Consolidated into one term sheet table + one agreement outline.
- **Added Quick Start**: Four-step summary for fast orientation.
- **Renamed sections**: "Output Structure / Process" → focused sections (Term Sheet Inputs, Agreement Outline). "Guidelines" → "Pitfalls and Checks" for scannability.
- **Reduced from 115 → ~88 lines** while preserving all domain-accurate legal content.
