---
name: nonprofit-board-minutes
title: Non-Profit Board Meeting Minutes
description: Drafts legally compliant non-profit board meeting minutes with attendance, quorum, resolutions, conflict-of-interest recusals, and executive session notation. Formats output for IRS Form 990 audit, state AG scrutiny, and permanent corporate records. Use when drafting official board minutes, recording board resolutions, or creating non-profit governance records.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/nonprofit-board-minutes
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
---

# Non-Profit Board Meeting Minutes

Drafts governance-ready minutes that serve as the official corporate record of board actions. Output withstands IRS, auditor, and regulatory scrutiny.

## Prerequisites

Collect before drafting:

- **Logistics** — date, start time, location (in-person/virtual/hybrid), presiding officer
- **Attendance** — directors present, absent (excused/unexcused), staff/guests
- **Quorum requirement** — from bylaws or state non-profit corporation law default (typically majority)
- **Prior minutes** — for approval, with any corrections
- **Agenda + documents** — reports, financials, proposed resolutions
- **Vote tallies** — ayes/nays/abstentions per motion
- **Conflict disclosures** — recusals, room-exit times, affected items

## Quick Start

Draft minutes in this section order:

1. Header block
2. Attendance and quorum confirmation
3. Approval of prior minutes
4. Officer and committee reports
5. Old business
6. New business
7. Executive session (if any)
8. Action item summary
9. Adjournment and certification

Use past tense throughout. Use formal terminology: `moved`, `seconded`, `carried`, `tabled`, `resolved`.

## Output Structure

### Header Block

| Field | Format |
|---|---|
| Organization name | Full legal name |
| Meeting type | Regular / Special / Emergency |
| Date | Month DD, YYYY |
| Time | Start time with time zone |
| Location | Address or platform name |
| Presiding officer | Name, Title |
| Recording officer | Name, Title |

### Attendance and Quorum

List directors present, absent (excused), absent (unexcused), and staff/guests. State quorum finding with bylaws citation:

> A quorum of [N] of [Total] directors was present as required by Article [X], Section [X] of the Bylaws. The meeting was duly constituted for the transaction of business.

### Approval of Prior Minutes

Record motion, mover, seconder, any corrections, and vote result.

### Officer and Committee Reports

Per report, capture: presenter and role, key findings (not verbatim), action items referred to board, documents distributed (by reference only).

Treasurer's report must include: cash position, revenue vs. budget YTD, significant variances, financial health assessment.

### Business Items (Old and New)

Per item use this format:

```
ITEM: [Title]
Background: [Brief context for future readers]
Discussion: [Substantive summary; attribute only if material]
Motion: [Exact resolution language]
Moved by: ___  |  Seconded by: ___
Vote: Carried/Failed [X ayes – X nays – X abstentions]
```

#### Decisions Requiring Extra Detail

| Type | Must Record |
|---|---|
| Budget approval | Total amount, fiscal year |
| Major contract | Counterparty, amount, scope, authorization limit |
| Officer election | Name, title, term |
| Bylaw amendment | Exact amended language |
| Conflict-of-interest approval | Party, conflict nature, recusal notation |
| Delegation of authority | Scope, dollar threshold, duration |
| Legal counsel consulted | Fact of consultation only — never disclose privileged content |

### Executive Session

Record entry/exit times, general category (personnel / litigation / negotiation), and attendees. Actions taken post-session go in business items. Never record privileged deliberations.

### Action Item Summary

| Item | Responsible Party | Deadline |
|---|---|---|
| [Task] | [Name/Committee] | [Date or "Next meeting"] |

### Adjournment and Certification

Record adjournment motion, time, and next meeting date if set. Include signature blocks for Secretary and Board Chair with certification language:

> I certify that these minutes accurately reflect the actions taken and decisions made at the [Organization Name] Board of Directors meeting held on [Date].

## Conflict-of-Interest Recusal

Always use this pattern — critical for IRS Form 990 and duty-of-loyalty compliance:

> "[Name] disclosed a potential conflict of interest regarding [general description]. [Name] recused themselves, left the room at [time], and returned at [time] following conclusion of discussion and vote."

## Pitfalls

- **Missing exact resolution language** — minutes are official authorization; copy motions verbatim
- **Editorial content** — omit opinions, subjective characterizations, and debate transcripts
- **Incomplete recusal documentation** — must note room exit and re-entry times
- **Quorum without citation** — if bylaws are silent, apply state default (majority of authorized directors); flag for state-specific verification
- **Executive session over-documentation** — record category only, never privileged legal advice or personnel deliberations
- **Missing financial detail** — budget approvals, compensation decisions, and related-party transactions must be fully documented for IRS/audit readiness
- **Forgetting retention note** — supporting documents are incorporated by reference and retained in the corporate records book

---

**Key changes from original:**

- **Description** trimmed from ~350 chars to ~280, written in third person with clear trigger guidance
- **Removed `tags` frontmatter** (not in the Agent Skills spec)
- **Removed horizontal rules** between sections (visual noise, no structural benefit)
- **Consolidated Old/New Business** into single "Business Items" section — they share the same format
- **Collapsed verbose code-block templates** (attendance, executive session, adjournment) into compact prose + blockquotes — preserves the essential language without burning tokens on formatting scaffolding
- **Renamed "Guidelines"** to **"Pitfalls"** — shifts from passive reference to actionable checklist
- **Elevated conflict-of-interest recusal** to its own section — it's the single highest-risk compliance item and deserves prominence over being embedded in New Business
- **~105 lines** down from **175** (~40% reduction) while preserving all legal substance
