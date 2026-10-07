# zmd Indexing Reference

## Prerequisites

`zmd` must be on `$PATH`. Verify: `zmd version`

## Collection Scope

| Collection | Default Scope | Files | Source |
|-----------|---------------|-------|--------|
| `laws` | 법률 (Acts) only | ~1,720 | `legalize-kr` — `kr/*/법률.md` |
| `precedents` | 민사 + 형사, 대법원 | ~43,500 | `precedent-kr` — `{민사,형사}/대법원/*.md` |
| `admrules` | All administrative rules (행정규칙) | ~21,000 | `admrule-kr` — `**/본문.md` |
| `ordinances` | All local ordinances (자치법규) | ~160,000 | `ordinance-kr` — `**/본문.md` |

Not indexed by default for precedents: 대통령령, 부령, 일반행정/세무/특허/가사/선거/기타, 하급심.

## Taskfile Tasks

| Task | Scope | ~Files |
|------|-------|--------|
| `task zmd` | Laws + default precedents | 45K |
| `task zmd:laws` | 법률 only | 1.7K |
| `task zmd:precedents` | 민사+형사 대법원 | 43K |
| `task zmd:precedents:all` | All 8 case types + all courts | 123K |
| `task zmd:precedents:민사` | Civil (대법원 + 하급심) | 42K |
| `task zmd:precedents:형사` | Criminal | 22K |
| `task zmd:precedents:일반행정` | Administrative | 45K |
| `task zmd:precedents:세무` | Tax | 10K |
| `task zmd:precedents:특허` | Patent | 3K |
| `task zmd:precedents:가사` | Family | 1.4K |
| `task zmd:admrules` | All 행정규칙 | ~21K |
| `task zmd:ordinances` | All 자치법규 | ~160K |
| `task zmd:all` | All 4 collections | ~226K |
| `task zmd:sync` | Pull + re-index | — |
| `task zmd:status` | Show status | — |
| `task zmd:reset` | Remove collections | — |

## CLI Subcommands

| Subcommand | Purpose |
|------------|---------|
| `query` | Native hybrid search (FTS5 + vec0 + RRF, ~410 ms) |
| `search` | Native FTS-only (~10 ms) |
| `similar` | Query → precedents → cited laws in one call |
| `laws` | Clone legalize-kr, stage, index |
| `precedents` | Clone precedent-kr, stage, index |
| `admrules` | Clone admrule-kr, stage 본문.md files, index |
| `ordinances` | Clone ordinance-kr, stage 본문.md files, index |
| `all` | All 4 collections |
| `sync` | Pull latest + re-index |
| `status` | Show repos, staged files, doc counts |
| `reset` | Remove collections (keeps repo clones) |

## How Indexing Works

1. Clone/pull upstream repo (shallow) into `~/.cache/legal-ko/zmd/repos/`
2. Stage matching files as hardlinks into `~/.cache/legal-ko/zmd/stage/`
3. Pre-filter by size + mtime — unchanged files skipped
4. Index changed files: hash (SHA-256), embed (fnv_embed), write to `.qmd/data.db`
5. FTS5 triggers dropped during bulk insert, rebuilt afterward

Re-runs with no changes: <2 seconds. Safe to interrupt and resume.

## Collection Paths

- Laws: `laws/kr/{법령명}/법률.md` (e.g., `laws/kr/민법/법률.md`)
- Precedents: `precedents/{사건종류}/{법원등급}/{법원명}_{선고일자}_{사건번호}.md` (e.g., `precedents/민사/대법원/대법원_2002-09-27_2000다10048.md`)
- Admin rules: `admrules/{부처}/{기관경로...}/{행정규칙종류}/{행정규칙명}/본문.md`
- Ordinances: `ordinances/{광역}/{기초}/{자치법규종류}/{자치법규명}/본문.md`

## Topic → Search Terms

| Topic | FTS Terms | Semantic Query |
|-------|-----------|---------------|
| 전세, 월세 | `임대차`, `보증금`, `주택` | "전세 보증금 반환 관련 법률" |
| 이혼, 양육권 | `이혼`, `양육`, `가사` | "이혼 시 양육권 관련 규정" |
| 부당해고 | `해고`, `근로`, `부당` | "직장에서 부당하게 해고당했을 때" |
| 교통사고 | `교통`, `손해배상` | "교통사고 피해자 보상 관련 법" |
| 사기, 횡령 | `사기`, `횡령`, `배임` | "사기 피해를 당했을 때 적용되는 형법" |
| 저작권 | `저작권`, `침해` | "블로그 글을 무단 복제한 경우" |
| 세금 | `부과처분`, `국세` | "세금 부과 처분에 이의 제기" |

## Combining with legal-ko-cli

| Task | Tool |
|------|------|
| Discovery by topic | `legal-ko-cli zmd query --json` |
| Keyword search | `legal-ko-cli zmd search --json` |
| Semantic reranking | `zmd query --rerank --json` |
| Structured metadata | `legal-ko-cli show --json` / `precedent-show --json` |
| Cross-reference | `legal-ko-cli precedent-laws` / `law-precedents` |
| Person search | `legal-ko-cli precedent-search-person` |
| TUI navigation | `legal-ko-cli navigate` |

## Error Handling

| Error | Resolution |
|-------|------------|
| `command not found: zmd` | Install zmd, add to `$PATH` |
| `Failed to open database` | Run `task zmd` to build initial index |
| No search results | Check `task zmd:status`; try broader terms |
| Stale results | Run `task zmd:sync` |
| Precedent not found | Expand scope: `task zmd:precedents:all` |
