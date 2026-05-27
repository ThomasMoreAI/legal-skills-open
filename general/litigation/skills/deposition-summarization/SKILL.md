---
name: deposition-summarization
title: Deposition Summarization
description: Summarizes deposition transcripts with precise page:line citations. Supports sequential, topic-based, and strategic deep-analysis formats. Use when a user provides a deposition transcript and requests a summary, depo digest, testimony analysis, or impeachment identification.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/deposition-summarization
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Deposition Summarization

Produces citation-backed deposition summaries. Every summary statement must include a `pp. page:line` range. Default to Format A unless the user specifies otherwise.

## Quick Start

1. Receive transcript text or file.
2. Identify format: A (sequential), B (topic-based), or C (deep analysis).
3. Summarize with `pp. page:line-page:line` citations on every entry.
4. Note objections, stipulations, exhibit references, and confidentiality designations.

## Format A: Page-Line Summary

Sequential, transcript-order summary. Neutral language.

```
pp. 12:3-14:8 — Deponent described arriving at the facility at 8:30 AM
and meeting with [Name] in the conference room. [Ex. 3 marked and identified.]

pp. 14:9-16:22 — On cross-examination, deponent acknowledged signing the
memorandum (Ex. 4) but stated he did not read it before signing.
```

## Format B: Topic-Based Summary

Groups testimony by subject. Each topic: 2-3 sentence neutral summary with citations.

```
## Employment History
Deponent worked at [Company] from 2018-2022 as Senior VP of Operations
(pp. 8:12-9:4), reporting directly to the CEO (pp. 9:15-10:8).

## Knowledge of Transaction
Deponent first learned of the acquisition in January 2022 (pp. 22:3-22:18)
and attended three related board meetings (pp. 23:1-25:14, 31:8-33:2, 45:6-47:11).
```

## Format C: Deep Analysis

Includes Format A or B, plus these additional sections:

- **Admissions Against Interest** — Testimony harmful to deponent's party. Exact quotes with citations.
- **Inconsistencies** — Internal contradictions or conflicts with other testimony/documents.
- **Impeachment Opportunities** — Prior inconsistent statements, bias, lack of personal knowledge.
- **Key Exhibits** — Table format:

| Exhibit | Description | Pages Discussed | Authenticated? |
|---------|-------------|-----------------|----------------|
| Ex. 1 | [Description] | pp. 15:3-17:8 | Yes — pp. 15:10 |

- **Credibility Assessment** — Evasive answers, non-responsive testimony, "I don't recall" count with page ranges.

## Pitfalls

- Never summarize without a `pp. page:line` citation.
- Keep summary language neutral; reserve analysis for Format C sections only.
- Preserve exact quotes (in quotation marks) for admissions and key testimony.
- Note all objections and their basis inline.
- Flag confidentiality designations (Confidential, AEO) when present.
- If an exhibit is referenced but not provided, note: "[Exhibit not provided for review]".

---

**Key changes**: Removed `tags` from frontmatter (not in spec). Tightened the description. Added a Quick Start checklist for fast orientation. Consolidated the Guidelines section into a "Pitfalls" section. Trimmed redundant prose in format descriptions while keeping all three formats, their examples, and the exhibit table intact. Reduced from 76 lines to 62 lines with no domain content lost.
