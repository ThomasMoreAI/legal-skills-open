# Case Types, Topics & Parsing Reference

## Case Types (사건종류)

| Case Type | Count | Description |
|-----------|-------|-------------|
| 민사 | 42,016 | Civil |
| 일반행정 | 45,028 | Administrative |
| 형사 | 21,624 | Criminal |
| 세무 | 10,024 | Tax |
| 특허 | 3,371 | Patent/IP |
| 가사 | 1,387 | Family |
| 기타 | 11 | Other |
| 선거·특별 | 8 | Election/special |

## Court Levels

| Court | Count |
|-------|-------|
| 대법원 | 68,002 |
| 하급심 | 55,466 |

## Topic → Case Type & Search Terms

| Topic | Case Type | Search Terms |
|-------|-----------|--------------|
| 계약, 매매, 채권 | 민사 | `손해배상`, `계약`, `채무` |
| 부동산, 소유권 | 민사 | `소유권`, `등기`, `명도` |
| 불법행위, 사고 | 민사 | `손해배상`, `불법행위` |
| 이혼, 상속, 양육 | 가사 | `이혼`, `상속`, `양육` |
| 범죄, 폭행, 사기 | 형사 | `사기`, `폭행`, `횡령` |
| 세금, 부과처분 | 세무 | `부과처분`, `취소`, `경정` |
| 행정처분, 인허가 | 일반행정 | `처분취소`, `재량`, `인허가` |
| 특허, 상표 | 특허 | `특허`, `침해`, `무효` |

## Court Levels (법원등급)

| Directory | Description |
|-----------|-------------|
| `대법원` | Supreme Court |
| `하급심` | Lower courts (고등법원, 지방법원 등) |
| `미분류` | Unclassified (missing court type code) |

## Path Pattern

New format: `{case-type}/{court-level}/{court-name}_{decision-date}_{case-number}.md`
- Example: `민사/대법원/대법원_2002-09-27_2000다10048.md`
- Example: `가사/대법원/대법원_2003-11-14_2000므1257_본소_1264_반소.md`
- Collision suffix: `_{판례일련번호}` when composite key clashes

Filename parsing: first `_` separates court name, second `_` separates date (YYYY-MM-DD fixed format), remainder is case number.

## Case Number Prefix → Directory

| Prefix | Case Type | Directory |
|--------|-----------|-----------|
| 다, 그, 마, 카 | 민사 | `민사/` |
| 도, 모, 오, 초, 감 | 형사 | `형사/` |
| 두, 누 | 세무 or 일반행정 | `세무/` or `일반행정/` |
| 므, 스, 으, 즈, 브 | 가사 | `가사/` |
| 후, 허, 흐 | 특허 | `특허/` |

> When prefix is ambiguous (e.g., `두`), try both directories.

## Precedent Sections

| Section | Content | When to Read |
|---------|---------|-------------|
| 판시사항 | Legal points decided | Quick summary |
| 판결요지 | Holding / ratio decidendi | Statute interpretation |
| 참조조문 | Statutes cited | Which laws apply |
| 참조판례 | Other precedents cited | Citation chain |
| 판례내용 | Full ruling text | Full reasoning |

## 참조조문 Patterns

```
{법령명} 제{N}조                       → law + article
{법령명} 제{N}조 제{M}항              → + paragraph
{법령명} 제{N}조 제{M}항 제{K}호      → + item
[{번호}] {법령명} 제{N}조 / [...]     → numbered groups
```

Common law name → ID mappings:

| 참조조문 Name | Typical ID |
|--------------|------------|
| 민법 | `kr/민법/법률` |
| 형법 | `kr/형법/법률` |
| 상법 | `kr/상법/법률` |
| 민사소송법 | `kr/민사소송법/법률` |
| 형사소송법 | `kr/형사소송법/법률` |
| 근로기준법 | `kr/근로기준법/법률` |
| 헌법 | `kr/대한민국헌법/법률` |

## 법조인 Extraction

Persons are extracted from 판례내용 (full text), not metadata.

- **Judges**: `대법관 이름(재판장) 이름(주심) 이름 이름` at end of ruling
- **Attorneys**: `소송대리인 변호사 이름` in representation lines
- **Prosecutors**: `【검    사】 이름` (spacing varies)

First 법조인 search builds a cached index (~3 min, 50 concurrent fetches).
Subsequent searches are instant. Index: `~/.cache/legal-ko/person_index.json` (7-day TTL).

## Error Handling

| Error | Resolution |
|-------|------------|
| Empty results | Try shorter keywords; check topic map |
| HTTP 404 on precedent-show | Wrong case type directory — try alternative |
| HTTP 403 | Rate limit — wait or set `GITHUB_TOKEN` |
| Empty case_name in list | Normal — populates after `precedent-show` |
