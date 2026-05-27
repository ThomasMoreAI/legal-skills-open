---
name: client-advisory-summary
title: Client Advisory Summary
description: Produces client-ready U.S. regulatory advisory summaries translating legal developments into actionable impacts with effective-date tracking and Bluebook citations. Trigger when the user requests a client advisory, regulatory update, compliance memo, law-change summary, or industry alert.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/client-advisory-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
tags: [analysis, drafting, research, summarization, summary]
---

# Client Advisory Summary

Translate recent legal developments into a concise, actionable advisory with deadlines, impact analysis, and recommended next steps.

## Quick Start

Gather before drafting:

1. **Client profile** — industry, products/services, geography, size/thresholds.
2. **Jurisdiction & scope** — federal, state, agency, or court.
3. **Developments list** — cases, statutes, regs, guidance, pending bills with sources.
4. **Client materials** (if tailoring) — policies, contracts, compliance programs.
5. **Format preference** — memo vs. letter; branding requirements.

## Workflow

### 1. Research Intake

- Confirm each development's status: enacted, final rule, proposed, guidance, or decision.
- Capture controlling authority, citation, publication date.
- Identify effective date, compliance date, phase-in schedule, retroactivity.
- Verify applicability thresholds (industry, size, activity, geography).
- Note conflicts or overlaps with prior law or guidance.
- Cross-check against at least two authoritative sources.

### 2. Draft Advisory

Follow this structure:

| Section | Content |
|---|---|
| **Header** | Client name, matter/topic, date, author(s) |
| **Executive Summary** | 2–3 paragraphs: top developments, immediate implications, key deadlines. Write for non-lawyers. |
| **Developments & Impact** | One entry per development (see analysis fields below) |
| **Open Questions** | Assumptions made, missing facts, client inputs needed |
| **Recommended Next Steps** | Priority actions with owners and timelines |
| **Contact** | Relationship partner / team |

**Per-development analysis fields:**

| Field | Content |
|---|---|
| Authority & Status | Statute/reg/decision/guidance + final/proposed + issuing body |
| Key Changes | Plain-language summary of what changed |
| Dates | Effective, compliance, and enforcement dates |
| Applicability | Who is covered; thresholds; exclusions |
| Client Impact | Categorize by timing (`Immediate` / `Short-term` / `Long-term`) and type (`Compliance` / `Operational` / `Strategic` / `Reputational`) |
| Risk Level | `High`, `Medium`, or `Low` |
| Recommended Actions | Concrete steps, owner, suggested timeline |
| Citations | Bluebook format |

### 3. Review & Finalize

- Verify all Bluebook citations; mark uncertain ones `[VERIFY]` and list in Open Questions.
- Use tables or timelines when multiple deadlines exist.
- Include client-specific examples where possible.
- Target 2–5 pages unless instructed otherwise.

## Pitfalls

- **Omitting deadlines** — always surface effective and compliance dates.
- **Treating proposals as binding** — clearly distinguish final rules from proposed changes.
- **Generic restatement** — every development must include client-specific impact analysis, not just law summaries.
- **Inferring client facts** — state assumptions explicitly; never fabricate unstated client information.
- **Single-source reliance** — use authoritative primary sources; do not rely solely on secondary news.
- **Jurisdiction drift** — default to U.S. law. For non-U.S. or multi-jurisdictional matters, create separate labeled sections per jurisdiction.

---

Key changes from the original:

- **Description** rewritten in third-person with explicit trigger guidance instead of keyword list
- **Collapsed** the verbose "Output Structure / Process" section into a streamlined 3-step workflow (Research Intake → Draft Advisory → Review & Finalize)
- **Merged** the advisory outline template, development analysis table, impact tags, citation rules, and formatting rules into two compact tables within the Draft step
- **Replaced** the do/don't guidelines with a focused Pitfalls section using bolded anti-pattern labels
- **Removed** the stray non-English text ("конкретні") in the original analysis table
- **Cut ~40% of tokens** while preserving all domain-accurate legal content
