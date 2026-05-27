---
name: discovery-summary
title: Discovery Document Summarization
description: Generates structured, citeable summaries of discovery documents (interrogatories, RFPs, RFAs, depositions, productions). Extracts admissions, inconsistencies, evidentiary gaps, and objections with precise source citations. Use when summarizing discovery responses, preparing for depositions, identifying discovery gaps, or building trial preparation materials.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/discovery-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Discovery Document Summarization

Produces a structured summary of discovery materials with precise citations for trial preparation and case strategy. Applies regardless of which side the user represents.

## Prerequisites

- **Discovery documents** — interrogatory responses, RFP responses, RFA answers, deposition transcripts, produced documents
- **Case context** — claims, defenses, key issues, parties
- **Citation sources** — Bates ranges, response numbers, or transcript page:line references

## Quick Start

1. Identify discovery types present in the materials
2. Produce the four-part output structure below
3. Cite every factual assertion to a specific source

## Output Structure

### 1. Executive Overview

3–5 paragraph narrative covering:

- Significant admissions or revelations
- Key documents or testimony
- Inconsistencies across responses
- Notable refusals, evasions, or privilege assertions
- Critical evidentiary gaps

### 2. Discovery Breakdown

Organize by discovery type or by claim/issue — whichever better serves the matter.

Per section, include a header block:

| Field | Detail |
|---|---|
| Discovery Type | Interrogatories / RFP / RFA / Deposition |
| Requesting Party | {name} |
| Responding Party | {name} |
| Date(s) | {response date(s)} |

Then summarize:

- **Admissions** — quote or paraphrase with exact citation
- **Produced documents** — description, Bates range, relevance (1–2 sentences)
- **Objections** — type and whether it blocked material disclosure
- **Evasive/incomplete responses** — what specifically was avoided

### 3. Cross-Reference Analysis

| Topic/Fact | Source A (cite) | Source B (cite) | Consistent? | Notes |
|---|---|---|---|---|
| {fact} | {cite} | {cite} | Yes/No | {discrepancy detail} |

### 4. Outstanding Discovery Issues

- [ ] Incomplete responses requiring follow-up (list by response number)
- [ ] Objections warranting meet-and-confer or motion to compel
- [ ] New custodians or document sources identified in testimony
- [ ] Areas where supplemental requests are warranted
- [ ] Privilege log deficiencies

## Pitfalls and Checks

- **Cite everything** — every assertion needs a response number, Bates stamp, or page:line
- **Stay objective** — no legal conclusions; flag apparent evasion but let attorneys draw conclusions
- **Sufficient detail** — attorneys should be able to work from the summary without pulling underlying documents for routine tasks
- **Flag patterns** — systematic objection strategies, coordinated non-responses, recurring privilege claims
- **Navigation** — include a table of contents when materials span 3+ discovery categories or 10+ responses
