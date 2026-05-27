---
name: communication-summarization
title: Communication Summarization
description: Generates structured memorandum-style summaries of legal communications (email threads, meeting notes, correspondence, negotiation records). Captures decisions, commitments, deadlines, party positions, and legally significant language. Triggers when the user asks to summarize communication chains for corporate matters, discovery review, settlement negotiations, or matter file management.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/communication-summarization
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
tags: [corporate, memo, summarization, summary]
---

# Communication Summarization

Distills legal communication chains into a structured memorandum capturing decisions, commitments, deadlines, and legally significant elements.

## Quick Start

1. Collect source communications (email threads, meeting notes, transcripts)
2. Gather matter context if available (contracts, prior agreements, party relationships)
3. Produce memorandum following the output structure below

## Output Structure

### Header Block

| Field | Content |
|---|---|
| To | [Requesting attorney / matter file] |
| From | CaseMark |
| Date | [Today's date] |
| Re | Communication Summary — [Matter/Subject] |
| Sources | [All documents/threads reviewed] |

### 1. Executive Overview

2–3 sentences: purpose of communications, period covered, key outcome or current status.

### 2. Background and Context

- Parties involved (names, roles, organizations)
- Communication period (date range)
- Subject matter / transaction / dispute

### 3. Key Decisions and Agreements

| Date | Parties | Decision / Agreement | Source |
|---|---|---|---|

Flag agreements that modify existing contracts, could constitute acceptance/waiver/novation, or contain representations/admissions.

### 4. Commitments and Deadlines

| Date | Party | Commitment / Obligation | Source |
|---|---|---|---|

### 5. Outstanding Issues

- Unresolved disputes or open questions
- Conflicting party positions
- Gaps in the communication record

### 6. Legally Significant Language

Flag and quote verbatim (with source and date) any:
- Notice language (contractual or statutory)
- Admissions or representations
- Document/information requests
- References to contracts, statutes, or legal authorities
- Language that could toll deadlines or trigger obligations

### 7. Action Items

| Priority | Action | Responsible Party | Due Date | Source |
|---|---|---|---|---|

## Pitfalls and Checks

- **Attribution required** — every factual claim must cite source document, sender, and date; never synthesize without attribution
- **Neutral tone** — report what parties said; do not characterize beyond what the source explicitly states
- **Superseding communications** — when later messages modify or override earlier ones, explicitly note the relationship
- **Multi-party matters** — organize by party or topic when three or more distinct parties are involved
- **Gaps** — flag missing correspondence or ambiguities; may indicate spoliation issues or areas needing clarification
- **Jurisdiction** — US default; flag references to non-US law or cross-border obligations for separate review

---

Key changes:
- **Description** rewritten in third-person with explicit trigger guidance ("Triggers when...")
- **Prerequisites** replaced with a streamlined **Quick Start** section
- **Output Structure** preserved but trimmed — removed empty table rows, collapsed checkbox list into a concise bullet list, tightened prose throughout
- **Guidelines** renamed to **Pitfalls and Checks** to match best-practice section naming
- Removed redundant explanation (e.g. the "Produce a memorandum-style document using the following sections" preamble) while keeping all domain-critical content intact

It looks like I don't have write permissions to the file. Would you like to grant write access so I can save it, or would you prefer to copy the content above manually?
