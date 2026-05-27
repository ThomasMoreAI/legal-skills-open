---
name: project-summary
title: Legal Project Management Summary
description: Generates structured legal project management summaries with RAG status indicators, budget variance analysis, and prioritized action items. Use when creating matter status reports, project updates, portfolio reviews, or resource allocation summaries for litigation, transactional, or regulatory matters.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/project-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
tags: [corporate, litigation, regulatory, summarization, summary, transactional]
---

# Legal Project Management Summary

Produces a stakeholder-ready project status summary from matter files, task lists, budgets, and correspondence.

## Prerequisites

1. **Matter files** — pleadings, contracts, filings, or deal documents defining scope
2. **Task/milestone data** — completed and upcoming deliverables with dates
3. **Budget information** — original budget, current spend, projections
4. **Team roster** — attorneys, paralegals, experts, co-counsel with role assignments
5. **Correspondence/status notes** — emails, memos, or prior status reports

## Output Structure

### 1. Executive Overview

Two to three sentences covering current project status, phase, and any critical issues requiring immediate attention.

### 2. Project Objectives

| Element | Detail |
|---|---|
| Overarching goal | Strategic outcome aligned to client business objective |
| Specific deliverables | Enumerated list with target dates |
| Success criteria | Measurable outcomes or legal benchmarks |
| Governing constraints | Contractual obligations, regulatory deadlines, court orders |

### 3. Resources

**Team Composition:**

| Name/Role | Allocation % | Primary Responsibilities | Notes |
|---|---|---|---|

Include lead counsel, associates, paralegals, and external experts.

**Budget Summary:**

| Metric | Amount |
|---|---|
| Original budget | |
| Spent to date | |
| Projected total | |
| Variance | |
| Key cost drivers | |

If over budget, include mitigation strategy.

### 4. Timeline

**Completed Milestones:**

| Milestone | Target Date | Actual Date | Status |
|---|---|---|---|

**Upcoming Deliverables:**

| Deliverable | Target Date | Owner | Dependencies | Risk Level |
|---|---|---|---|---|

Flag timeline risks (pending rulings, third-party delays, resource constraints) and note contingency plans for critical-path items.

### 5. Status Assessment

Rate each dimension **R/Y/G** (Red/Yellow/Green):

| Dimension | Rating | Notes |
|---|---|---|
| Schedule adherence | | |
| Budget compliance | | |
| Work product quality | | |
| Team capacity | | |
| Client satisfaction | | |
| Risk exposure | | |

For any Yellow or Red: state root cause, corrective action, assigned owner, and remediation deadline.

### 6. Risk Register

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|

Rate likelihood and impact as H/M/L. Flag matter-type-specific risks:

- **Litigation** — adverse rulings, emerging legal theories, discovery issues
- **Transactional** — regulatory changes, counterparty issues, market conditions
- **Regulatory** — enforcement trends, compliance gaps, agency communications

### 7. Action Items

Prioritize by urgency: Immediate / This Week / This Month / Strategic.

| # | Action | Owner | Due Date | Priority |
|---|---|---|---|---|

Include process improvement recommendations where supported by project performance data.

## Guidelines

- **Privilege protection** — Mark litigation strategy or attorney mental impressions as `[PRIVILEGED]`. Review before external distribution.
- **Audience calibration** — Client-facing: emphasize business impact, minimize jargon. Internal: include granular task detail and legal analysis.
- **Tiered access** — Note where redaction is needed if stakeholders have different information rights.
- **Conflicts/ethics** — Flag conflict of interest, malpractice exposure, or ethical concerns in the Risk Register.
- **Data-driven** — Anchor assessments to specific documents, dates, and metrics. Do not speculate without supporting evidence.

---

**Key changes made:**

- **Description** — trimmed from 50+ words to a tighter statement while preserving trigger guidance
- **Removed empty placeholder rows** in Team Composition table (replaced with inline instruction)
- **Consolidated Budget table** — dropped the "Mitigation (if over)" row into a one-line note below the table
- **Action Items table** — dropped `Resources Needed` and `Success Criteria` columns to reduce noise; kept the essential tracking fields
- **Risk Register** — merged the three separate matter-type paragraphs into a compact bulleted list
- **Guidelines** — cut the `Formatting` bullet (redundant with table structure already shown) and tightened each remaining bullet to one line
- **Overall** — ~35% fewer tokens while preserving all seven output sections and legal domain accuracy
