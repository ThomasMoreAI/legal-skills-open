---
name: legal-ko-precedent
title: Korean Precedent Search
description: 'Find Korean court precedents and cross-reference with statutes via legal-ko-cli. Searches by case name/number or 법조인 name. USE FOR: 판례 검색, 판례 찾기, 참조조문 찾기, 법조인 찾기, cases by judge. DO NOT USE FOR: legal advice, statute lookup (use legal-ko-search), content search (use legal-ko-zmd).'
author: pastel-sketchbook
author_url: https://github.com/pastel-sketchbook/legal-ko/tree/main/.agents/skills/legal-ko-precedent
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: kr
practice: general
language: en
---

# Korean Precedent Search

**UTILITY SKILL** — INVOKES: `legal-ko-cli precedent-search|precedent-show|precedent-laws|law-precedents|precedent-search-person`

## Workflow

1. Map topic to case type + search terms (see `reference/CASE_TYPES.md`)
2. Search: `legal-ko-cli precedent-search "<q>" --json --limit 30`
3. Read: `legal-ko-cli precedent-show "<id>" --json`
4. Cross-ref: `precedent-laws "<id>" --json` or `law-precedents "<law>" --article "제N조" --json`
5. Present: summary, precedent table, holdings, cited statutes, disclaimer

> Auto-falls back to 법조인 search if query looks like a Korean name.

## Commands

| Command | Purpose |
|---------|---------|
| `precedent-search <q>` | Search by case name/number |
| `precedent-show <id>` | Full ruling |
| `precedent-laws <id>` | Laws cited (4-approach fallback) |
| `law-precedents <law> --article` | Precedents citing a law |
| `precedent-search-person <name> --role` | Search by 법조인 |
| `precedent-persons <id>` | Extract persons |

ID format: `{사건종류}/{법원등급}/{법원명}_{선고일자}_{사건번호}` — e.g., `민사/대법원/대법원_2002-09-27_2000다10048`

Path pattern: `{case-type}/{court-level}/{court-name}_{decision-date}_{case-number}.md`
- Court levels: `대법원`, `하급심`, `미분류`
- Filename collisions add `_{판례일련번호}` suffix

## Data Sources

The precedent data comes from `legalize-kr/precedent-kr`. Related datasets:
- Laws: `legalize-kr/legalize-kr`
- Administrative rules: `legalize-kr/admrule-kr`
- Local ordinances: `legalize-kr/ordinance-kr`

## Disclaimer

⚠️ 검색 결과이며 법률 자문이 아닙니다. 변호사와 상담하세요.
