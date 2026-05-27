---
name: summarize-files
title: Summarize Legal Documents
description: Generates structured summaries of legal documents (contracts, pleadings, correspondence, transactional materials). Triggers when the user asks to summarize case files, agreements, pleadings, or any legal materials for review, onboarding, or status reporting.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/summarize-files
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
tags: [agreement, litigation, pleading, summarization, summary, transactional]
---

# Summarize Legal Documents

Produce standalone, structured summaries of one or more legal documents for professional reference.

## Quick Start

1. Receive one or more legal files (contracts, pleadings, correspondence, transactional docs).
2. Read all uploaded content exhaustively — never sample or skip sections.
3. Classify each document, extract key data, and output the summary using the template below.

## Workflow

### 1. Classify Document Type

| Type | Analysis Focus |
|---|---|
| Contract / Agreement | Parties, obligations, terms, defined terms, reps & warranties, conditions precedent, dispute provisions |
| Pleading | Causes of action, factual allegations, relief requested, procedural posture, legal authority |
| Correspondence | Negotiation positions, admissions, strategic signals, communication timeline |
| Transactional | Deal structure, consideration, reps & warranties, closing conditions, indemnification |

### 2. Extract Key Data

From every document, capture:
- Parties (full legal names, roles)
- Key dates and deadlines
- Monetary amounts and consideration
- Claims, defenses, or obligations
- Legal authority cited
- Exhibits, attachments, referenced materials
- Defined terms (use consistently throughout)
- Ambiguities or internal conflicts

### 3. Output Summary

```
# Summary: [Document Title / Subject Matter]
Date of Summary: [date]

## Overview
[Type, parties, fundamental purpose — 2-3 sentences]

## Key Parties
[Table or list: name, role, relationship]

## Substantive Summary
[Organized by logical sections mirroring the source structure]

## Key Terms and Conditions
[Dates, deadlines, amounts, obligations — use tables where appropriate]

## Notable Issues
[Ambiguities, conflicts, missing information, concerns]

## Source Attribution
[For multi-file summaries: which document each key fact derives from]
```

## Pitfalls and Checks

- **Completeness over brevity** — never omit material information; flag conflicts rather than resolving by assumption.
- **Source attribution** — cite which document each significant fact comes from, especially across multiple files.
- **Preserve precision** — retain qualifications, limitations, and conditions; use defined terms as defined in the source.
- **Proportional length** — target 70-90% reduction while retaining all material information.
- **No legal conclusions** — summarize positions as presented; do not evaluate merits or predict outcomes.
- **Readability** — bold party names and key terms; use tables for claims, obligations, or chronological events.
