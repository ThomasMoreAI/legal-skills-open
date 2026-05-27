---
name: board-meeting-summary
title: Board Meeting Summary
description: Produces a structured, objective summary of corporate board meetings covering metadata, quorum, attendance, conflicts, resolutions with vote counts, committee reports, and significant corporate actions. Use when summarizing board minutes, creating a corporate governance record, or preparing a post-meeting recap for officers, shareholders, or regulators.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/board-meeting-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Board Meeting Summary

Generates an official, concise board meeting summary suitable for the corporate minute book.

## Quick Start

1. Collect inputs: agenda, minutes/notes, attendance list, resolutions, committee reports.
2. Populate every section below. Mark missing information as `UNKNOWN` and flag it in the Issues checklist.
3. Review against Guidelines before finalizing.

## Output Sections

### 1. Meeting Metadata

| Field | Value |
|---|---|
| Date | |
| Time (start/end) | |
| Location | |
| Format (in-person/virtual/hybrid) | |
| Notice/Waiver | |
| Quorum (required/present) | |
| Chair | |
| Secretary/Recorder | |

### 2. Attendance

| Role | Name | Status | Notes |
|---|---|---|---|
| Director | | Present / Absent (Excused/Unexcused) | |
| Officer | | Present | |
| Guest/Advisor | | Present | |

### 3. Conflicts & Recusals

| Person | Matter | Disclosure | Recusal | Notes |
|---|---|---|---|---|
| | | Yes/No | Yes/No | |

### 4. Agenda Items

| # | Topic | Discussion Summary | Decision/Outcome | Follow-up |
|---|---|---|---|---|
| 1 | | | | |

### 5. Resolutions

| # | Summary (or verbatim text) | Vote (For/Against/Abstain/Recused) | Result |
|---|---|---|---|
| 1 | | | Approved/Denied/Tabled |

### 6. Significant Corporate Actions

Check all that apply. For each, add a short action summary with any conditions or limits.

- [ ] Financial statement/audit report approval
- [ ] Dividends or distributions
- [ ] Major contracts/transactions
- [ ] Stock issuance/repurchase
- [ ] Officer election/removal
- [ ] Bylaw or policy amendments
- [ ] M&A or asset sales
- [ ] Financing/borrowing authorization
- [ ] Litigation or claims decisions
- [ ] Other material actions

### 7. Committee Reports

| Committee | Key Findings/Recommendations | Board Action |
|---|---|---|
| | | Accepted/Modified/Deferred |

### 8. Executive Session

Note occurrence and general subject only. Do not disclose privileged content unless explicitly instructed.

### 9. Closing

Announcements, next meeting date/time (if set), adjournment time.

### 10. Issues / Missing Information

- [ ] Missing quorum/notice detail
- [ ] Missing vote counts
- [ ] Missing resolution text/summary
- [ ] Missing attendance confirmations
- [ ] Other: ___

## Guidelines

- **Neutral tone** — do not editorialize or speculate.
- **Precise votes** — always include exact counts; identify abstentions and recusals.
- **Summarize, don't reproduce** — condense discussion; do not copy presentations verbatim.
- **Verify compliance** — confirm recordkeeping against bylaws and governing law; do not assert compliance unless verified.
- **Preserve privilege** — exclude attorney-client content or legal strategy unless specifically directed.
