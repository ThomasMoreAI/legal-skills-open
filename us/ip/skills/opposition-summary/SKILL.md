---
name: opposition-summary
title: Trademark Opposition Summary
description: Generates structured analytical summaries of trademark opposition proceedings before the TTAB. Use when summarizing opposition filings, analyzing TTAB dispute posture, evaluating settlement options, or assessing trademark conflict strength.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/opposition-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
---

# Trademark Opposition Summary

Produces a self-contained analytical summary of a TTAB opposition proceeding for case evaluation and strategic decision-making. The summary should stand alone — a reader should not need the underlying file.

## Prerequisites

- **Opposition file**: notice of opposition, answer, discovery materials, briefs, evidence, TTAB decisions/orders
- **Application details**: serial number, mark, goods/services, filing/priority dates
- **Party identification**: opposer and applicant names, counsel, marks at issue

## Quick Start

1. Gather all opposition file documents
2. Extract key data points (see extraction checklist below)
3. Produce the seven-section output structure
4. Apply guidelines and verify citations

## Extraction Checklist

Extract from uploaded documents:

- Application serial number, mark, goods/services, class(es) — from Notice of Opposition, application records
- Filing, priority, and publication dates — from application records, Official Gazette
- Opposer's mark(s), registration number(s), goods/services — from Notice of Opposition, registration certificates
- Opposition grounds (each statutory basis) — from Notice of Opposition
- Applicant's defenses — from Answer
- Key evidence (declarations, surveys, sales figures) — from trial briefs, exhibits
- Procedural dates (filing, answer, discovery close, trial) — from board orders, scheduling notices
- Outcome or current posture — from final decision or latest board order

## Output Structure

### 1. Executive Overview

Parties, marks in conflict, application number. One paragraph on primary issues. Current status and outcome if concluded.

### 2. Opposition Grounds

For each ground asserted:

**Ground: [e.g., Likelihood of Confusion — §2(d)]**
- **Factual basis**: specific allegations
- **Legal theory**: statutory/precedential framework
- **Key evidence**: exhibits, declarations, survey data

Common grounds to check (mark `[VERIFY]` on statutory citations):
- Likelihood of confusion (Lanham Act §2(d))
- Dilution of famous mark (§43(c))
- Descriptiveness/genericness (§2(e)(1))
- Prior common law rights
- False suggestion of connection (§2(a))
- Geographic descriptiveness (§2(e)(2))

### 3. Likelihood of Confusion Analysis

If §2(d) is at issue, analyze under the *DuPont* factors `[VERIFY]`. For each factor, present opposer's position, applicant's position, and a neutral assessment:

- Similarity of marks (appearance, sound, meaning, commercial impression)
- Relatedness of goods/services
- Similarity of trade channels
- Purchase conditions / buyer sophistication
- Strength/fame of opposer's mark
- Evidence of actual confusion
- Number and nature of similar marks in use
- Concurrent use without confusion

### 4. Applicant's Defenses

Document each asserted defense: standing challenges, mark dissimilarity, goods/services distinction, trade channel differences, crowded field, coexistence evidence, laches/acquiescence/estoppel.

### 5. Procedural History

Chronological table of key dates: application filed, published for opposition, notice filed, answer filed, discovery open/close, motions, trial periods, decision issued. Note extensions, suspensions, or consolidations.

### 6. Outcome / Current Posture

**If resolved**: sustained/dismissed, key holdings, registration conditions, appeal status.
**If ongoing**: current posture, upcoming deadlines, pending motions.

### 7. Strategic Assessment

- Strengths and weaknesses of each party's position
- Evidentiary gaps or procedural vulnerabilities
- Settlement considerations (consent agreements, coexistence terms)
- Impact on broader trademark portfolio

## Guidelines

- **Balanced analysis**: present both sides with equal rigor; do not opine on ultimate outcome
- **Citation precision**: cite specific exhibits, declarations, and filings by name and date; use exact quotations with attribution
- **Verification**: mark unverified legal citations with `[VERIFY]`
- **Audience**: accessible to business stakeholders while maintaining legal precision
- **Dilution claims**: separately address fame of the senior mark and likelihood of blurring/tarnishment
- **Settlement**: note any settlement discussions or consent proposals in the record

---

Key changes from the original:

- **Trimmed description** from 3 sentences to 2, keeping trigger keywords
- **Removed `tags`** from frontmatter (not in the spec)
- **Added Quick Start** section for immediate orientation
- **Collapsed the extraction table** into a flat list — same data, fewer tokens
- **Condensed DuPont analysis** from a 4-column table template to a factor list with inline instructions — preserves the analytical framework without empty table scaffolding
- **Compressed Defenses and Procedural History** into inline descriptions instead of verbose bullet/table templates
- **Merged Outcome section** into compact conditional format
- **Converted Guidelines** from flat bullets to labeled entries for scannability
- **Reduced from ~134 lines to ~95 lines** (~30% token savings) while preserving all legal substance

Want me to try writing the file again, or would you like any adjustments?
