---
name: article-summary
title: Legal Article Summary
description: Generates structured 500-800 word summaries of legal articles distilling thesis, methodology, arguments, authorities, conclusions, and significance. Triggers when summarizing legal scholarship, reviewing law review articles, preparing literature reviews, or triaging articles for full reading.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/article-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
tags: [analysis, corporate, summarization, summary]
---

# Legal Article Summary

Produces a structured summary (500–800 words) of a legal article that works as both a standalone reference and a read/skip triage tool.

## Prerequisites

- Full article text or sufficient excerpts covering thesis, methodology, arguments, and conclusions
- Citation info: author(s), title, journal, volume, year
- Target audience: academic, practitioner, or general (defaults to practitioner)

## Quick Start

1. Collect the article text and citation details
2. Classify the article type (doctrinal / empirical / policy / comparative / theoretical)
3. Produce the header block and six summary sections below
4. Verify summarized points against the original before delivering

## Output Format

### Header Block

| Field | Content |
|-------|---------|
| Citation | Bluebook or jurisdiction-appropriate format |
| Author(s) | Name(s) and affiliation if relevant |
| Publication | Journal/venue and date |
| Article Type | Doctrinal / Empirical / Policy / Comparative / Theoretical |

### Summary Sections (500–800 words total)

**1. Thesis & Research Question** — Central argument in 1-2 sentences. Identify the legal problem: doctrinal gap, policy critique, empirical question, or theoretical development.

**2. Methodology & Approach** — Method (case law analysis, statutory interpretation, comparative, empirical, theoretical). Note dataset, jurisdiction scope, or time period if applicable.

**3. Key Arguments & Findings** — Major points in logical sequence mirroring the author's reasoning. Use numbered list for distinct arguments. Preserve the author's emphasis; reflect counterarguments if substantially treated.

**4. Authorities & Precedents** — Key cases, statutes, regulations, or principles forming the analytical foundation. Note usage: supporting, distinguishing, or criticizing.

**5. Conclusions & Recommendations** — Separate analytical findings (evidence-supported) from normative proposals (reform/practice changes). Note stated limitations or areas for further research.

**6. Significance & Implications** — Relationship to existing scholarship (confirms, challenges, extends). Practical impact on practice, judicial decisions, legislation, or regulatory policy. Novel contributions.

## Pitfalls

- **Editorializing** — present arguments faithfully; no evaluative commentary unless requested
- **Flattening hedges** — preserve modal language ("may," "suggests," "could"); do not convert tentative conclusions into definitive statements
- **Over-quoting** — use direct quotes sparingly, only when phrasing is particularly significant
- **Oversimplifying** — preserve qualifications, conditions, and nuanced reasoning
- **Conflating arguments** — verify each summarized point maps to a distinct original argument
- **Terminology drift** — match the article's legal terms; briefly gloss highly specialized concepts essential to the core argument
