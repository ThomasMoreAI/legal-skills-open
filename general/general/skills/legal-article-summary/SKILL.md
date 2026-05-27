---
name: legal-article-summary
title: Legal Article Summary
description: Produces structured summaries of legal scholarship capturing thesis, methodology, key authorities, arguments, and significance. Use when summarizing law review articles, journal articles, case notes, or scholarship for research triage, case preparation, literature reviews, or CLE.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/legal-article-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Legal Article Summary

Structured summary of legal scholarship preserving the article's analytical spine and practical significance. Default 500–800 words unless specified.

## Quick Start

Gather before writing:
- Full article text or excerpts with page/section markers
- Citation data: author, title, journal, year, volume/issue, pages, DOI/URL
- Reader goal, length target, jurisdiction or doctrinal focus

## Core Workflow

### 1. Extract

- Identify thesis and list article section headings
- Capture methodology (doctrinal, empirical, comparative, theoretical, policy critique); note dataset/sample/timeframe if empirical
- Extract foundational authorities (not mere examples)
- Flag modal language (may/might/could/suggests) and preserve it
- Note explicit limitations or boundary conditions
- Record proposed reforms or practice changes

### 2. Structure

Include only sections that exist in the article:

| Section | Content |
|---|---|
| Citation | Author, title, journal, year, vol/issue, pages; DOI/URL if provided |
| Thesis / Question | One-sentence central claim or research question |
| Methodology / Approach | Type and key details |
| Major Arguments | 3–6 points in author's sequence, 1–3 sentences each |
| Key Authorities | Statutes, cases, regulations, doctrines relied upon |
| Counterarguments / Limits | Acknowledged limitations, caveats, counterpoints |
| Conclusions / Recommendations | Findings separated from normative proposals |
| Significance / Implications | Contribution to scholarship and practical impact |
| Future Research | Only if author explicitly flags open questions |

### 3. Write

```
**Citation:** {Author}, "{Title}," {Journal} {Year}, {Vol}({Issue}) {Pages}. {DOI/URL}

**Thesis / Question:** {One sentence}

**Methodology / Approach:** {Type; key details}

**Major Arguments / Findings:**
1. {Point}
2. {Point}
3. {Point}

**Key Authorities:** {Cases/statutes/regulations/doctrines}

**Counterarguments / Limitations:** {If any}

**Conclusions / Recommendations:** {Findings vs. proposals}

**Significance / Implications:** {Why it matters}

**Future Research:** {If stated}
```

## Pitfalls and Checks

- Stay neutral; no critique unless requested
- Preserve author's emphasis and sequencing — do not reorder
- Quote sparingly; only when exact phrasing is decisive
- Separate empirical results from normative recommendations
- If jurisdiction is ambiguous, state it; default to U.S. only when clearly implied
- For theoretical articles, specify framework and assumptions instead of empirical details
- Summarize literature-review positioning in 1–2 sentences
- Flag uncertain citations with `[VERIFY]`

---

**Key changes:**
- Removed `tags` (not part of the Agent Skills spec frontmatter)
- Tightened `description` — removed redundant keyword stuffing while keeping discovery triggers
- Replaced "Prerequisites" with a compact "Quick Start" section
- Merged the separate "Extraction checklist" and "Output Structure" into a single three-step "Core Workflow" (Extract → Structure → Write)
- Renamed "Guidelines" to "Pitfalls and Checks" per best-practice section naming
- Removed prose preamble — overview is now two sentences
- Cut ~30% of tokens while preserving all domain-specific legal guidance
