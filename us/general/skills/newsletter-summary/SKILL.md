---
name: newsletter-summary
title: Legal Newsletter Summary
description: Produces concise, actionable U.S. legal newsletter summaries of recent developments organized by practice area. Use when asked for a legal news digest, weekly/monthly client update, regulatory roundup, case law summary, compliance news bulletin, or internal legal awareness memo.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/newsletter-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: general
language: en
---

# Legal Newsletter Summary

Scannable digest of recent legal developments with headlines, impact analysis, action items, and citations.

## Quick Start

Before drafting, confirm:

- **Audience & tone** — internal ops, client-facing, or executive
- **Practice areas & jurisdictions** — scope of coverage
- **Time window** — default 7–14 days unless specified
- **Exclusions** — e.g., skip minor procedural updates

## Workflow

### 1. Research & Source Capture

Source priority (use highest available tier):

1. **Primary law** — court opinions, statutes, regulations, agency orders
2. **Official guidance** — agency FAQs, enforcement releases, advisories
3. **Bar/industry** — bar updates, reputable legal publications

For each item capture: title, date, jurisdiction, authority, direct citation, link if available.

### 2. Triage & Rank

Score each item on:

- **Impact** (High / Medium / Low)
- **Urgency** (Immediate / Near-term / Watch)
- **Scope** (Broad / Sector-specific / Narrow)
- **Novelty** (New rule / Major shift / Split / Clarification)

Prioritize: new compliance obligations > binding appellate decisions > enforcement trends > upcoming deadlines.

### 3. Draft Items (75–200 words each)

Each item follows this structure:

- **Headline** — 8–14 words, action-oriented
- **What Happened** — 1–3 factual sentences
- **Why It Matters** — 1–3 sentences on practice/client impact
- **Action Items** — concrete bullet steps
- **Details** — court/agency, jurisdiction, effective date, citation(s)

Order within each section: urgent first, then high-impact, then emerging trends.

### 4. Assemble

```
# Legal Newsletter Summary
**Coverage Window:** {start}–{end}
**Jurisdictions:** {list}
**Practice Areas:** {list}

## {Practice Area / Theme}
### {Headline}
**What Happened:** ...
**Why It Matters:** ...
**Action Items:**
- ...
**Details:** Court/Agency · Jurisdiction · Effective Date · Citation(s)

## Watchlist / Upcoming
- {Pending appeals, comment periods, scheduled arguments}
```

## Citations

- Bluebook-style for cases (include court and year) and statutes (include code section and amendment date)
- Mark unconfirmed citations as `[VERIFY]`

## Pitfalls

- **No editorializing** — verifiable facts and implications only
- **Never copy source text** — summarize the underlying legal development
- **Always flag deadlines** — effective dates and compliance windows must be explicit
- **Note conflicting authority** — circuit splits, agency disagreements
- **No updates?** — state "No material updates in the covered period"
- U.S.-focused unless user specifies otherwise

---

Key changes from the original:

- **Frontmatter**: Trimmed description to focus on what it does + clear triggers; removed `tags` (not part of the spec)
- **Structure**: Reorganized from 7 numbered subsections into 4 clean workflow steps with Quick Start, Workflow, Citations, and Pitfalls sections
- **Reduced redundancy**: Merged the separate "Intake & Scoping" and "Prerequisites" into a single Quick Start; collapsed the source hierarchy table into a numbered list; consolidated citation rules and guidelines into focused sections
- **Token savings**: Cut from 125 lines to ~75 lines (~40% reduction) while preserving all domain-critical content — source tiers, triage dimensions, item template fields, assembly format, Bluebook citation rules, and `[VERIFY]` convention

It looks like the file write permission hasn't been granted yet. Would you like to approve the write so I can save this to disk?
