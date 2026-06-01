---
name: legal-ko-search
title: Korean Law Search
description: 'Find Korean laws and articles by title search via legal-ko-cli. USE FOR: 법 찾기, 법률 검색, 법조항 찾기, find Korean law, what law applies. DO NOT USE FOR: legal advice, precedent search (use legal-ko-precedent), content search (use legal-ko-zmd).'
author: pastel-sketchbook
author_url: https://github.com/pastel-sketchbook/legal-ko/tree/main/.agents/skills/legal-ko-search
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: kr
practice: general
language: en
---

# Korean Law Search

**UTILITY SKILL** — INVOKES: `legal-ko-cli search|show|articles|navigate`

## Workflow

1. Map colloquial terms to formal law names (see `reference/TOPICS.md`)
2. Search: `legal-ko-cli search "<term>" --json --limit 20` (run 2-5 terms)
3. Read: `legal-ko-cli show "<id>" --json`
4. Articles: `legal-ko-cli articles "<id>" --json`
5. Present: summary, law table, key articles, disclaimer

> `search` matches **titles only**. Always run multiple keywords.

## Commands

| Command | Purpose |
|---------|---------|
| `search <q> --json` | Search by title |
| `show <id> --json` | Full law text |
| `articles <id> --json` | List articles |
| `navigate <id> --article "제N조"` | Open in TUI |
| `context --json` | Read TUI state |

ID format: `kr/{법령명}/{유형}` — e.g., `kr/민법/법률`

## Data Sources

Legalize-KR provides four public datasets:
- Laws: `legalize-kr/legalize-kr`
- Court precedents: `legalize-kr/precedent-kr`
- Administrative rules: `legalize-kr/admrule-kr`
- Local ordinances: `legalize-kr/ordinance-kr`

This skill searches laws only. Use `legal-ko-precedent` for precedents.

## TUI Context

`legal-ko-cli context --json` reads what the user is viewing.
See `reference/TUI.md` for JSON structure and navigate usage.

## Disclaimer

⚠️ 검색 결과이며 법률 자문이 아닙니다. 변호사와 상담하세요.
