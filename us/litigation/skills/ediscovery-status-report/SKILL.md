---
name: ediscovery-status-report
title: E-Discovery Status Report
description: Generates a structured internal e-discovery status report tracking ESI from collection through attorney review. Covers custodian volumes, search term hit rates, review coding statistics, reviewer productivity, and projected timelines. Use when counsel, case managers, or clients need a progress report during the discovery phase of U.S. commercial litigation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/ediscovery-status-report
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# E-Discovery Status Report

Produces an attorney-work-product status report tracking ESI from collection through review for U.S. commercial litigation.

## Prerequisites

Gather before starting. Flag and caveat any gaps in the report.

1. **Vendor collection logs** — custodian names, item counts, GB volumes, file types, processing status
2. **Review platform exports** — document counts, reviewer IDs, coding dates, relevance/privilege/issue-tag designations
3. **Search term results** — hit counts per query, precision/validation sampling data if available
4. **Privilege log drafts** — finalized privilege assertions with custodian and document-type breakdowns

## Quick Start

1. Normalize custodian names across all sources into a single canonical list
2. Populate each report section using the templates below
3. Surface flags and anomalies at each stage
4. Mark final output: **ATTORNEY WORK PRODUCT — PRIVILEGED AND CONFIDENTIAL**

## Report Sections

### 1. Executive Summary

- Collection completeness status
- Search strategy effectiveness (one sentence)
- Review progress % and projected completion date
- Critical issues requiring immediate action

### 2. Collection Metrics by Custodian

| Custodian | GB Collected | Items | Email % | Office Doc % | Other % | Processing Status |
|-----------|-------------|-------|---------|-------------|---------|------------------|
| [Name] | [X.X] | [N] | [X%] | [X%] | [X%] | Complete / Pending / Error |

**Flags:**
- Volume >2× matter average → possible over-collection or key player
- Unexpectedly low volume → incomplete collection risk
- Processing error rate >5% by custodian or file type

**Validation:** Collected ≥ Processed ≥ Loaded ≥ Reviewed. Explain any downward discrepancy.

### 3. Search Term Performance

| Search Term / Boolean | Hits | Hit Rate (%) | Precision (if sampled) | Status |
|----------------------|------|-------------|----------------------|--------|
| [Term] | [N] | [X%] | [X%] | Keep / Refine / Drop |

**Flags:**
- Hit rate >30% → likely overbroad
- Hit rate <0.5% → likely underperforming
- High inter-term overlap → recommend consolidation
- If precision data exists, project relevant yield from unreviewed hits

### 4. Review Progress

| Metric | Count | % of Loaded |
|--------|-------|------------|
| Loaded to platform | [N] | 100% |
| Reviewed | [N] | [X%] |
| Coded Relevant | [N] | [X%] |
| Coded Privileged | [N] | [X%] |
| Coded Non-Responsive | [N] | [X%] |
| Remaining | [N] | [X%] |

**Reviewer Productivity:**

| Reviewer | Docs Reviewed | Avg Docs/Hr | Relevance Rate | Privilege Rate |
|----------|--------------|-------------|---------------|---------------|
| [Name] | [N] | [X] | [X%] | [X%] |

- Flag coding patterns >15% above/below team average (QC concern)
- Note velocity trend: accelerating / decelerating / stable (weekly rolling avg)
- **Projected completion:** [Date] at [N] docs/day — state assumptions explicitly

### 5. Privilege Analysis

| Custodian | Docs Reviewed | Privilege Assertions | Privilege Rate |
|-----------|--------------|---------------------|---------------|
| [Name] | [N] | [N] | [X%] |

- Note whether overall privilege rate is within expected range for matter type
- Break down privilege rate by document type (email vs. office docs vs. other)
- Flag custodians with rates >2× matter average for senior attorney QC

### 6. Recommendations & Timeline

- **Resource needs:** additional reviewers / vendor remediation / search refinement
- **Search adjustments:** specific terms to modify
- **QC actions:** reviewer-specific or category-specific
- **Risk items:** gaps, processing failures, tight deadlines
- **Milestones:** processing complete, first-pass review complete, privilege log ready (with dates)

## Pitfalls

- **Privilege substance leaks** — present privilege statistics in aggregate only; never reveal communication substance or attorney mental impressions
- **Adverse findings** — report collection gaps, QC failures, and search weaknesses without minimization so counsel can make informed decisions
- **Missing audit trail** — document how discrepancies were resolved and what validation steps were taken; the process may be challenged
- **Unstated assumptions** — all projections must explicitly state their underlying assumptions
- **Distribution control** — limit report distribution to litigation team members with case management need
