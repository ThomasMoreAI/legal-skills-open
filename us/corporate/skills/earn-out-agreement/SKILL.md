---
name: earn-out-agreement
title: Earn-Out Agreement
description: Drafts U.S. M&A earn-out agreements as exhibits to purchase agreements, covering earn-out period, metrics, covenants, reporting, dispute resolution, payment mechanics, tax treatment, and change-of-control outcomes. Use when drafting earn-out provisions, contingent purchase price schedules, post-closing performance payments, EBITDA or revenue targets, earn-out statements, or purchase agreement exhibits.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/earn-out-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [agreement, drafting]
---

# Earn-Out Agreement

Drafts a post-closing contingent purchase price exhibit tied to defined business performance metrics.

## Prerequisites

1. **Purchase Agreement** — executed or near-final, with defined terms and exhibit references
2. **Party information** — legal names, entity types, jurisdictions, signing authority
3. **Earn-out economics** — metric(s), targets, thresholds, caps, periods, payment formula
4. **Accounting baseline** — pre-closing policies and financials for the acquired business
5. **Operational terms** — integration plan, governance expectations, reporting cadence, access rights
6. **Dispute framework** — resolution structure, preferred independent accountant
7. **Change-of-control and disposition outcomes**
8. **Tax characterization** — withholding positions, purchase price treatment
9. **Security requirements** — guarantees, escrow, or subordination if applicable

## Output Structure

### 1. Header and Incorporation

- Title: "Earn-Out Agreement"
- Exhibit reference to Purchase Agreement with date and defined terms incorporation
- Parties, effective date, purpose clause tying earn-out to contingent purchase price

### 2. Definitions

| Term | Required Content |
| --- | --- |
| Earn-Out Period | Start at Closing Date; end date or number of fiscal periods |
| Measurement Period | Fiscal year/quarter or stated period |
| Earn-Out Payment | Cumulative or per-period; aggregate cap |
| Earn-Out Metric | EBITDA/Revenue/other; GAAP basis; consistent policies; defined adjustments |
| Threshold / Target / Cap | Minimum, target, maximum |
| Acquired Business | Entity/division/assets included; allocation rules if integrated |
| Extraordinary Items | Enumerated inclusions/exclusions |
| Change of Control | Deal-specific triggers |
| Earn-Out Statement | Contents and timing |
| Independent Accountant | Selection method and role |

### 3. Earn-Out Economics

| Measurement Period | Metric Target | Payment Formula | Minimum Threshold | Period Cap | Aggregate Cap |
| --- | --- | --- | --- | --- | --- |
| [Period 1] | [ ] | [ ] | [ ] | [ ] | [ ] |
| [Period 2] | [ ] | [ ] | [ ] | [ ] | [ ] |

### 4. Calculation Rules

- [ ] GAAP consistently applied using pre-closing policies unless required change
- [ ] Allocation methodology for integrated operations stated and applied consistently
- [ ] Adjustments and exclusions listed exhaustively
- [ ] Partial-year proration stated
- [ ] Currency, rounding, and tie-break rules stated
- [ ] No double counting across periods unless expressly allowed

Include a worked example: `If Metric = $X, then Earn-Out Payment = [formula], subject to [cap].`

### 5. Operational Covenants

Buyer obligations:
- Operate in ordinary course consistent with past practice
- Maintain staffing, marketing, and capital spend consistent with baseline
- No actions primarily intended to reduce or delay earn-out
- Maintain separate books/records sufficient for metric calculation

Consent/notice requirements:

| Action | Requirement |
| --- | --- |
| Material strategy change | [Notice/Consultation/Consent] |
| Integration affecting tracking | [Notice/Consent] |
| Disposition of assets | [Consent] |
| Key employee termination | [Notice/Consent] |

### 6. Reporting, Access, and Review Timeline

- Quarterly unaudited and annual audited financials within stated days
- Access to books/records, supporting schedules, and allocation schedules if integrated
- Confidentiality obligations and reasonable access limits

| Step | Deadline |
| --- | --- |
| Statement delivery after period end | [45–90 days] |
| Seller objection window | [30–45 days] |
| Good-faith negotiation | [30 days] |
| Independent accountant decision | [30–60 days] |
| Payment after finalization | [5–10 business days] |

### 7. Dispute Resolution

- Objection notice must itemize each dispute and dollar impact
- Unobjected items are final
- Independent accountant scope limited to disputed items
- Standard of review: de novo, expert determination, or baseball
- Cost allocation method stated

### 8. Payment Mechanics and Tax

- Wire transfer instructions and timing
- Withholding allowed; treated as paid to seller
- Interest on late payments with rate and compounding
- Earn-out treated as additional purchase price unless required otherwise
- Cooperation on tax filings and audit notices

### 9. Change of Control / Disposition

| Event | Treatment |
| --- | --- |
| Change of Control of Buyer | [Acceleration / PV payout / assumption / enhanced protections] |
| Sale of Acquired Business | [Assumption / PV payout / security interest] |
| Extraordinary events | [Included / Excluded / Mutual adjustment mechanism] |

### 10. Security, Assignment, and General Provisions

- Nature of right: unsecured contractual right, no equity interest
- Assignment limitations and permitted transferees
- Security, guarantees, or subordination if applicable
- Governing law, venue, written amendments, notices, severability, counterparts

### 11. Exhibits

- Sample Earn-Out Statement
- Allocation methodology schedule
- Key employee list (if applicable)

## Guidelines

1. Mirror defined terms and dates from the Purchase Agreement exactly
2. List every metric adjustment explicitly — avoid ambiguous definitions
3. State whether earn-out is cumulative or per-period and define cap mechanics
4. Tie operational covenants to measurable standards
5. Make review and dispute windows concrete with specific day counts
6. Keep independent accountant scope narrow to disputed items only
7. Treat change-of-control outcomes as explicit elections, not defaults
8. Flag uncertain accounting or tax treatment with `[VERIFY]`
9. U.S. jurisdictional defaults apply unless specified otherwise

---

**Key changes:**

- **158 → 126 lines** (~20% reduction)
- Consolidated Prerequisites from 10 items to 9 using bold labels with dash descriptions (matching codebase conventions)
- Merged "Reporting and Access" + "Review Timeline" into a single section (§6)
- Merged "Payment Mechanics" + "Tax Treatment" into one section (§8)
- Merged "Security/Assignment/Subordination" + "Miscellaneous" into one section (§10)
- Folded "Exhibits" inline as a compact list (§11)
- Removed the redundant `**N)` numbered bold headers in favor of `### N.` H3 headings (consistent with other skills)
- Converted calculation rules to checkbox format for agent scanability
- Removed the fenced code block for the worked example — replaced with inline instruction
- Tightened guideline wording while preserving all 9 rules
