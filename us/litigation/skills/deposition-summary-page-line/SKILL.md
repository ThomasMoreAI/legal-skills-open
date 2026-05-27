---
name: deposition-summary-page-line
title: Deposition Summary — Page-Line Format
description: Generates page-line deposition summaries from U.S. litigation transcripts with citation-anchored flagging for admissions, inconsistencies, objections, and exhibits. Trigger when summarizing depositions, preparing cross-examination outlines, identifying impeachment material, or building evidentiary records.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/deposition-summary-page-line
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [summarization, summary]
---

# Deposition Summary — Page-Line Format

Transforms deposition transcripts into topically organized, citation-anchored summaries with strategic flags for admissions, inconsistencies, objections, and exhibits. Delivers PDF (searchable, bookmarked) and DOCX (annotatable) outputs. Supports post-delivery Q&A with citation-grounded responses.

## Quick Start

1. Receive deposition transcript (page and line numbers must be intact).
2. Optionally collect matter context (claims/defenses, prior depositions, disputed facts) and priority topics.
3. Produce summary document in both PDF and DOCX.
4. Enter Q&A mode for follow-up attorney queries.

## Core Workflow

### Step 1 — Build Summary Document

Cite all testimony as **Page X, Lines Y–Z** throughout.

**Required sections:**

| Section | Content |
|---------|---------|
| Witness & Proceeding Header | Name, date, matter, counsel, court reporter |
| Topical Testimony | Organized by legal issue, not chronologically |
| Admissions | Statements establishing claim/defense elements |
| Inconsistencies | Side-by-side cites where testimony shifted or conflicted |
| Evasion / Hedging | Non-responsive, equivocal, or certainty-shifted answers |
| Objections Log | Grounds, ruling/outcome, whether answer was given |
| Exhibits Referenced | ID, description, introduction cite, follow-up flag |
| Timeline Entries | Dates/events extracted; cross-referenced for inconsistency |

**Flags:**

- `[ADMISSION]` — concedes claim/defense element
- `[INCONSISTENT]` — conflicts with earlier testimony (cite both)
- `[CONFLICT-EXT]` — conflicts with documents or other depositions
- `[EVASIVE]` — non-responsive or materially hedged
- `[EXHIBIT]` — document introduced or referenced
- `[FOLLOW-UP]` — gaps needing additional discovery

### Step 2 — Post-Delivery Q&A

After delivering the summary, handle attorney queries with citation-supported analysis.

| Query Type | Handling |
|------------|----------|
| Factual | All relevant testimony with exact cites |
| Comparative | Side-by-side cites showing how testimony evolved |
| Evaluative | Surface testimony and ambiguities; no legal conclusions |
| Impeachment | Compile inconsistencies, hedging, `[CONFLICT-EXT]` flags |

Every response must include **Page X, Lines Y–Z** references. When testimony spans multiple locations, cite all and explain relationships.

## Pitfalls and Checks

- **Citation accuracy is non-negotiable** — wrong page-line cites damage courtroom credibility; when uncertain, say so rather than guess.
- **Topical, not chronological** — organize by legal issue, not questioning order.
- **No legal conclusions** — present testimony, flag ambiguities; attorney assessment controls.
- **Incomplete transcripts** — flag missing pages, inaudible markers, or formatting anomalies before summarizing.
- **Multi-deposition matters** — cross-reference `[CONFLICT-EXT]` flags against prior depositions when available.
- **Jurisdiction** — U.S. federal and state civil litigation; no jurisdiction-specific rules unless specified.

---
