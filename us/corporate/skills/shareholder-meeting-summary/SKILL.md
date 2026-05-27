---
name: shareholder-meeting-summary
title: Shareholder Meeting Summary
description: Generates structured, record-quality summaries of shareholder meetings from minutes, transcripts, and related materials. Triggers when the user provides shareholder meeting documents and requests a summary, minute-book entry, or governance record covering metadata, resolutions, voting outcomes, and dissents.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/shareholder-meeting-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [summarization, summary]
---

# Shareholder Meeting Summary

Produces a structured summary of a shareholder meeting suitable for minute books, SEC filings, and governance compliance.

## Prerequisites

1. **Meeting materials** — minutes, transcripts, recordings, presentation decks, or correspondence
2. **Corporate context** — company legal name, jurisdiction, relevant bylaw provisions (quorum and voting thresholds)

## Quick Start

1. Collect all meeting materials and corporate context.
2. Extract meeting metadata and build the attendance table.
3. Summarize each agenda item with resolution text and voting results.
4. Document any dissents, appraisal rights, or procedural irregularities.
5. Record closing business and adjournment time.

## Output Structure

### 1. Meeting Metadata

| Field | Content |
|---|---|
| Corporation | Full legal name |
| Meeting type | Annual / Special (state purpose if special) |
| Date & time | Start and adjournment times |
| Location | Physical address or virtual platform |
| Presiding officer | Name and title |
| Secretary / recorder | Name and title |
| Quorum | Present shares vs. required threshold; determination method |

Attendance table:

| Name | Role | Shares Represented | Present / Proxy |
|---|---|---|---|

### 2. Agenda Items

For each item, in sequence:

- **Item number and title**
- **Substance** — what was proposed or presented
- **Material discussion** — key arguments for/against (factual only)
- **Management recommendation** (if shareholder proposal)
- **Resolution text** — full operative language for adopted resolutions
- **Voting results:**

| For | Against | Abstain | Broker Non-Votes | Method | Result |
|---|---|---|---|---|---|

### 3. Special Documentation

Capture if present:

- Dissenting shareholder statements (verbatim or detailed summary)
- Exercise of appraisal rights
- Demands for record inspection
- Fiduciary duty concerns raised
- Procedural irregularities or challenges
- Contested elections

### 4. Closing

- Other business conducted
- Announcements (future meetings, corporate actions)
- Time of adjournment

## Pitfalls and Checks

- **Neutral tone** — document what was said and decided; never editorialize unless the official minutes use specific language
- **Vote precision** — verify all counts and percentages; attribute each tally to its specific resolution
- **Flag gaps** — if materials omit vote counts or details, note the limitation explicitly rather than assuming
- **High-scrutiny items** — apply extra care to mergers, charter/bylaw amendments, director elections, executive compensation, and related-party transactions
- **No editorial commentary** — report irregularities and objections objectively
- **Consistent format** — use tabular presentation for all voting results
