---
name: ediscovery-review-summary
title: E-Discovery Collection & Review Summary
description: Produces an internal U.S. litigation e-discovery status summary covering ESI collection, processing, search-term hits, review throughput, relevance and privilege rates, and completion forecasts. Triggers when the user requests an e-discovery status report, collection log summary, processing report, review statistics, coding report, search-term results, or privilege review summary.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/ediscovery-review-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [summarization, summary]
---

# E-Discovery Collection & Review Summary

Internal status report tracking ESI from collection through attorney review, with completion projections.

## Prerequisites

- Custodian list with collection scope (systems, date ranges, locations)
- Collection logs and processing reports from vendor
- Review platform exports (coding, reviewer activity, search-term results)
- Search-term list or Boolean queries
- Review protocol (relevance, privilege, issue tags) and QC standards
- Key deadlines the review must meet
- Protective order or confidentiality requirements for reporting

## Quick Start

1. Gather source data (collection logs, processing reports, review exports, search-term results, privilege summaries).
2. Normalize custodian names into a master mapping table.
3. Run integrity checks — pipeline totals must satisfy: Collected ≥ Processed ≥ Loaded ≥ Reviewed.
4. Compute core metrics tables (see below).
5. Draft executive summary with risks and recommendations.
6. Apply work-product legend.

## Core Metrics

### A. Collection & Processing by Custodian

Per custodian: Collected GB, Item Count, Processed %, Load Failures, File-Type Mix, Exceptions.

### B. Search-Term Effectiveness

Per term/query: Hits, Hit Rate %, Sample Precision %, Overlap %, Recommended Action.

### C. Review Status (Matter-Level)

Total Reviewable, Reviewed Count, % Reviewed, Relevant %, Privileged %, Non-Responsive %, Est. Completion Date.

### D. Reviewer Productivity

Per reviewer/team: Docs Reviewed, Hours, Docs/Hour, Relevant %, Privileged %, QC Rate %.

### E. Privilege Patterns

Per custodian: Privileged %, Dominant Doc Types, Red Flags.

## Key Formulas

| Metric | Formula |
|---|---|
| Hit Rate % | hits ÷ total reviewable corpus |
| Precision % | relevant hits ÷ sampled hits |
| Review Velocity | docs reviewed ÷ time period |
| Completion ETA | remaining docs ÷ current velocity |
| Privilege Rate % | privileged ÷ reviewed |

## Executive Summary Template

- **Collection completeness** — status and anomalies
- **Processing health** — success rate and key errors
- **Search-term performance** — top/weak terms and overlap
- **Review progress** — reviewed %, relevance %, privilege %
- **Forecast** — ETA with assumptions
- **Risks & actions** — top three items

## Integrity Checks

- Custodian names align across all sources (master mapping table).
- Pipeline totals are monotonically decreasing through each stage.
- Every search term in the term list appears in the results export.
- Coding records contain reviewer, date, relevance, and privilege fields.
- Processing errors are reconciled against re-runs.

## Findings & Recommendations

- List missing sources and resulting limitations.
- Flag custodians with outlier volumes or error rates.
- Identify low-precision or high-overlap search terms.
- Note reviewer inconsistencies and QC actions taken.
- Recommend resource changes or search-term refinement.
- Document assumptions and gaps with impact and mitigation.

## Pitfalls

- Report only aggregate metrics — never disclose privileged content.
- If counts conflict, surface the discrepancy and state the suspected cause.
- Use U.S. discovery terminology; confirm local rules before external distribution.
- Mark uncertain legal citations with `[VERIFY]`.
- Keep narrative neutral and data-driven; avoid strategy conclusions.
- Always include: "Attorney Work Product / Privileged & Confidential. Internal use only."

---
