---
name: prior-art-summary
title: Prior Art Summary
description: Generates structured summaries of prior art references for patent prosecution, validity analysis, and freedom-to-operate assessments. Maps disclosures to claim elements with precise citations. Use when summarizing prior art, analyzing patent landscapes, mapping references to claims, or preparing office action responses.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/prior-art-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# Prior Art Summary

Synthesizes prior art references into structured summaries mapping disclosures to claim elements for rapid landscape assessment.

## Prerequisites

- **Prior art references** — patents, applications, publications, product docs, or public disclosures
- **Invention description** — claims or specification under analysis
- **Scope directive** — prosecution, validity/invalidity, or FTO

## Workflow

### 1. Executive Overview

Produce a table covering:

- Total references reviewed (count)
- Most material references (top 3-5 with one-line rationale)
- Key gaps (claim elements with no or weak coverage)
- Art type breakdown (patents / applications / publications / other)

### 2. Individual Reference Summaries

For each reference:

| Field | Content |
|-------|---------|
| Document ID | Patent/pub number, DOI, or identifier |
| Title | Full title |
| Date | Pub/issue date; note effective prior art date if different |
| Inventor(s)/Author(s) | Names |
| Technical field | CPC/IPC classes or subject domain |
| Assignee/Publisher | Entity |

Then include:

- **Disclosure summary** — 2-4 sentences on core technical contribution
- **Key features** — bulleted list with exact quoted language and precise citation (¶, col:line, page, figure)
- **Gaps** — what the reference does NOT disclose relative to the invention

### 3. Claim-Element Mapping

| Claim Element | Ref. 1 | Ref. 2 | Ref. 3 |
|--------------|--------|--------|--------|
| Element A | ¶[0032], Fig. 3 | — | p. 12 |
| Element B | — | Col. 4:15-22 | — |

Legend: `✓` full disclosure, `~` partial, `—` absent. Always include citation location.

### 4. Combination Analysis

For each potentially obvious combination:

- **References combined** — which refs
- **Motivation to combine** — analogous art rationale, explicit suggestions, design incentives
- **Missing elements** — what remains undisclosed even in combination

### 5. Timeline

Chronological list by effective date, noting critical date boundaries (priority, filing, publication dates).

## Guardrails

- **Cite precisely** — every factual assertion needs ¶, col:line, page, or figure number
- **No legal conclusions** — organize facts for attorney judgment; never state claims are anticipated or obvious
- **Analogous art** — flag references outside the immediate field with rationale for qualification
- **Prior art status** — note references whose qualification depends on date analysis (pre-AIA vs. AIA § 102) [VERIFY]
- **Foreign-language refs** — flag language, provide translated key passages, note if machine-translated
- **Figures** — describe depicted features with enough detail to be useful without viewing the original
- **Terminology** — define specialized terms on first use in brackets
- **Order by relevance** to claim elements; use chronological only if requested or analytically significant
