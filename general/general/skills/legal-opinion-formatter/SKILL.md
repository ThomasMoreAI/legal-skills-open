---
name: legal-opinion-formatter
title: Legal Opinion Formatter
description: Format legal research output into a law-firm-grade formal opinion style, with clear issue framing, conclusions, risk grading, and citation-ready references.
author: kipeum86
author_url: https://github.com/kipeum86/game-legal-research/tree/main/.claude/skills/legal-opinion-formatter
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Legal Opinion Formatter

Use this skill during Step 8 (Output Generation) when the user asks for:
- "법률 의견서" (Korean: formal legal opinion letter)
- "legal opinion"
- "opinion letter"
- "formal opinion"
- "opinion memo"
- "law-firm style"
- polished DOCX memo/opinion formatting

## Inputs

- Step 6 analysis result
- User language and output format
- Jurisdiction scope and as-of date

## Output Goal

Produce a clean legal-opinion document with:
1. Cover/meta block
2. Executive summary
3. Opinion question(s)
4. Jurisdiction-by-jurisdiction analysis
5. Risk matrix and practical recommendations
6. Source/citation section with verification pointers
7. Disclaimer and uncertainty notes

Read `references/format-checklist.md` before formatting.

## Style Authority

Apply `docs/style-guides/legal-research-core-contract.md` plus the matching language
and mode files under `docs/style-guides/{en|ko}/` as the default style reference.
Use `docs/legal-writing-formatting-guide.md` only as a detailed fallback when the
split guide files do not answer a formatting question. This SKILL's directives take
precedence on conflict; otherwise follow the guide.

## Style Rules

1. Keep tone formal and precise; avoid conversational wording.
2. Use concise issue statements and explicit conclusions.
3. Separate "fact", "rule", "analysis", and "recommendation".
4. Mark uncertainty explicitly (`[Unverified]`, `[Unresolved Conflict]` when needed).
5. Keep citation identifiers consistent with project codes (`[P#]`, `[C#]`, `[A#]`, `[S#]`, `[T#]`).

## Sample Assets

Use sample files as visual references only:
- Files are located at the skill root (same level as `references/`).
- `test_output_english.docx`
- `test_output_korean.docx`

Do not copy sample facts verbatim into new outputs.
