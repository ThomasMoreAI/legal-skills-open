---
name: case-summary-report
title: Case Summary Report
description: Synthesizes multiple case summaries into one unified Case Summary Report. Triggers when the user has two or more case summaries, document analyses, or memoranda and needs them consolidated into a single report with patterns, contradictions, and gaps identified.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/case-summary-report
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
tags: [analysis, summarization, summary]
---

# Case Summary Report

Consolidate multiple case summaries, document analyses, or memoranda into a single unified report identifying patterns, contradictions, and gaps across all sources.

## Quick Start

Collect all source summaries the user wants consolidated. Confirm the preferred organization: by legal issue or by chronology.

## Workflow

1. **Inventory sources** — For each summary, record title, date, author, and scope in a source index table.
2. **Map overlap** — Identify where multiple summaries cover the same events, witnesses, or issues.
3. **Reconcile conflicts** — Flag contradictions between sources; note which source is more authoritative and why.
4. **Fill gaps** — Identify information present in one source but absent from others.
5. **Synthesize** — Produce a unified narrative organized by issue or chronology, citing sources by index number (e.g., [Source 1, p. 3]).

## Output Structure

### Source Index

| # | Title | Date | Author | Scope |
|---|-------|------|--------|-------|
| 1 | [Title] | [Date] | [Author] | [Coverage] |

### Unified Summary

Per issue or time period:
- Synthesized narrative citing all relevant sources
- Flagged contradictions: "Source 1 states X; Source 3 states Y"
- Confidence level for contested facts

### Patterns and Themes
- Recurring facts across summaries
- Strengthening or weakening signals for case theories

### Contradictions and Gaps
- Specific conflicts with source citations
- Expected information absent from all sources
- Recommended follow-up per gap

### Consolidated Recommendations
- Merged, prioritized, de-duplicated action items and next steps

## Pitfalls

- **Source authority** — Do not treat all summaries as equally reliable. Note recency, author expertise, and underlying source quality.
- **Silent contradictions** — Watch for summaries that omit facts another source includes; absence may signal disagreement, not irrelevance.
- **Over-synthesis** — Preserve nuance from individual sources. Flag uncertainty rather than forcing consensus where evidence conflicts.

---

Key changes:
- **Description** tightened with explicit trigger guidance ("when the user has two or more…")
- Added **Quick Start** section for immediate orientation
- **Workflow** streamlined — same 5 steps, more concise phrasing
- **Output Structure** preserved but trimmed redundant template text
- Added **Pitfalls** section covering source authority, silent contradictions, and over-synthesis — practical guardrails missing from the original
- Removed prose repetition between the description and the body overview

I wasn't able to write the file due to permissions. Please grant write access and I'll save it, or you can copy the content above directly.
