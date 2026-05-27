---
name: franchise-agreement-summary
title: Franchise Agreement Summary
description: Summarizes US franchise agreements into a structured overview of parties, term, territory, fees, operations, IP, transfer, termination, covenants, dispute resolution, and risks. Triggers when the user asks to summarize a franchise agreement, franchise contract, or franchisor-franchisee terms, or to extract deal terms for review, diligence, or negotiation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/franchise-agreement-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: commercial
language: en
---

# Franchise Agreement Summary

Produce a structured summary capturing the commercial deal, legal obligations, and risk points of a franchise agreement.

## Quick Start

1. Collect the complete agreement with all exhibits, schedules, and amendments.
2. Gather the definitions section and any incorporated manuals or policies.
3. Identify any ancillary agreements (development agreement, lease, guaranty, supply agreement).
4. Confirm governing law / jurisdiction.

## Workflow

1. Read the full agreement end-to-end, including exhibits.
2. Extract exact figures, time periods, and thresholds — never infer missing numbers.
3. Note defined terms that control interpretation.
4. Populate each section below. If a field is absent, state "Not specified."
5. Cite section numbers where available.

## Output Template

### Deal Snapshot

| Field | Detail |
|---|---|
| Agreement title | |
| Effective date | |
| Parties (Franchisor / Franchisee) | |
| Brand / System | |
| Location(s) / Territory | |
| Initial term | |
| Renewal options | |
| Governing law / venue | |

### Parties and Relationship

| Topic | Summary |
|---|---|
| Franchisor identity and role | |
| Franchisee entity and principals | |
| Ownership / control requirements | |
| Guaranty requirements | |
| Relationship characterization | |

### Fees and Financial Obligations

| Fee / Obligation | Amount / Formula | Timing | Notes |
|---|---|---|---|
| Initial franchise fee | | | |
| Royalty | | | |
| Marketing / ad fund | | | |
| Technology / software | | | |
| Training fees | | | |
| Supply / purchase requirements | | | |
| Minimum purchases / quotas | | | |
| Transfer fees | | | |
| Audit costs / interest / late fees | | | |

### Territory and Development

| Topic | Summary |
|---|---|
| Territory type (exclusive / protected / non-exclusive) | |
| Geographic definition | |
| Franchisor reservation of rights | |
| Performance conditions | |
| Multi-unit or development obligations | |
| Encroachment standards | |

### Operations and Standards

| Topic | Summary |
|---|---|
| Training requirements | |
| Operating manual compliance | |
| Quality control and inspections | |
| Hours of operation | |
| Staffing / management requirements | |
| Insurance requirements | |
| Reporting / recordkeeping | |
| Pricing / product restrictions | |
| Technology systems | |

### Franchisor Support

| Topic | Summary |
|---|---|
| Initial training / opening support | |
| Ongoing support / field visits | |
| Marketing support | |
| Site selection / lease assistance | |
| Proprietary systems access | |

### Intellectual Property and Data

| Topic | Summary |
|---|---|
| Trademark / brand license scope | |
| Brand standards and QC | |
| Local marketing approvals | |
| Confidentiality / trade secrets | |
| Customer data ownership | |

### Transfer, Assignment, and Succession

| Topic | Summary |
|---|---|
| Transfer rights and approvals | |
| Right of first refusal | |
| Transferee qualifications | |
| Transfer fees | |
| Death / incapacity provisions | |
| Change of control restrictions | |

### Term, Renewal, and Termination

| Topic | Summary |
|---|---|
| Initial term length | |
| Renewal conditions | |
| For-cause termination grounds | |
| Termination without cause | |
| Notice and cure periods | |
| Franchisee termination rights | |
| Post-termination obligations | |

### Restrictive Covenants

| Topic | Summary |
|---|---|
| Non-compete (during term) | |
| Post-term non-compete (duration / geography / scope) | |
| Non-solicitation (customers / employees) | |
| Exceptions / carve-outs | |

### Dispute Resolution

| Topic | Summary |
|---|---|
| Arbitration or litigation | |
| Venue and forum | |
| Mediation requirements | |
| Fee shifting / damages limits | |
| Class action waiver | |

### Exhibits and Attachments

| Exhibit | Material Terms |
|---|---|
| Territory description | |
| Approved suppliers | |
| Required forms / notices | |
| Financial schedules | |
| Other | |

### Red Flags

List provisions that are atypical, one-sided, or unusually burdensome (e.g., aggressive development schedules, broad non-competes, sweeping indemnities, unilateral amendment rights, mandatory remodels on renewal, liquidated damages).

### Ambiguities and Follow-Ups

List unclear terms, missing figures, or external documents that control key obligations.

### Recommendations

Concise next-step items for counsel review or negotiation focus.

## Pitfalls

- Never round or infer numbers — use exact figures from the agreement.
- Flag any incorporated documents not provided for review.
- Note state-specific franchise relationship or termination statutes if referenced.
- Where language is ambiguous, present possible interpretations and note the risk.
- Stay neutral — identify risks but do not provide legal advice or business recommendations.

**Key changes made:**
- Removed `tags` from frontmatter (not part of the required format)
- Tightened description to third-person with clear trigger guidance
- Renamed "Prerequisites" → "Quick Start" and "Output Structure / Process" → split into "Workflow" + "Output Template"
- Renamed "Unusual Terms / Red Flags" → "Red Flags" for brevity
- Renamed "Guidelines" → "Pitfalls" and consolidated into concise bullet checks
- Removed redundant prose throughout while preserving all domain-accurate tables and legal coverage
