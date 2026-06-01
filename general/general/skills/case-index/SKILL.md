---
name: case-index
title: CSV 사건 인덱스 (case-index)
description: songmu-legal CSV 사건 인덱스 - JuriSupport MCP를 쓰지 않는 사용자를 위한 가벼운 사건관리. _index.csv 한 파일을 source of truth로 사용해 list/get/add/update/close 수행. JuriSupport 연동 시 보조 백업으로도 사용 가능.
author: jurisupport
author_url: https://github.com/jurisupport/jurisupport-plugins/tree/main/plugins/songmu-legal/skills/case-index
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: ko
---

# CSV 사건 인덱스 (case-index)

JuriSupport MCP가 없는 사용자도 가볍게 사건 목록을 관리할 수 있도록 CSV 한 파일로 사건 인덱스를 유지한다. 엑셀로 열어 직접 편집할 수도 있고, 본 스킬의 헬퍼 스크립트로 조작할 수도 있다.

## When to use

- 사용자가 JuriSupport MCP를 쓰지 않을 때 사건 목록·다음기일을 추적해야 하는 모든 상황
- "내 사건 뭐가 있지?", "이번 주 기일 있는 사건 알려줘", "○○사건 진행단계 바꿔줘"
- `/songmu-legal:brief-protocol` Phase 1 인테이크에서 사건 메타데이터 조회

JuriSupport MCP가 연동되어 있으면 JuriSupport가 정본이고 이 스킬은 선택. 사용자가 명시적으로 "CSV에 백업해줘" 하면 두 곳에 모두 기록.

## CSV 형식

위치: `<클라우드 사건폴더 경로>/_index.csv` (콜드스타트에서 사용자 입력. 기본 제안 예시는 `onedrive:진행중사건/_index.csv` 또는 로컬 미러)

컬럼 (고정 순서):

| 컬럼 | 설명 | 예시 |
|---|---|---|
| 사건번호 | 키, 중복 불가 | `2025가합10737` |
| 법원 | 관할법원·재판부 | `서울중앙지법 제50민사부` |
| 사건명 | 사건명 | `손해배상(기)` |
| 의뢰인 | 의뢰인 표기 | `최재혁` |
| 상대방 | 상대방 | `(주)○○` |
| 진행단계 | 단계 | `1심` / `항소` / `상고` / `변론종결` / `종결` 등 |
| 다음기일 | YYYY-MM-DD | `2026-06-12` |
| 비고 | 자유 메모 | |

인코딩: **UTF-8 with BOM** (한국어 엑셀 호환). 헬퍼가 자동 처리.

## 사용 방법

### 헬퍼 스크립트

플러그인 내 `case_index.py`. CSV 경로는 매번 `--csv` 로 지정.

```bash
PY=/Users/$USER/.claude/plugins/cache/jurisupport-plugins/songmu-legal/0.1.0/skills/case-index/case_index.py
CSV=<클라우드 사건폴더 경로>/_index.csv   # CLAUDE.md §5에 저장된 경로 사용

# 빈 인덱스 생성
python3 "$PY" --csv "$CSV" init

# 사건 추가
python3 "$PY" --csv "$CSV" add \
  --사건번호 2025가합10737 \
  --법원 "서울중앙지법 제50민사부" \
  --사건명 "손해배상(기)" \
  --의뢰인 "원고측" \
  --상대방 "주식회사 ○○" \
  --진행단계 "1심" \
  --다음기일 "2026-06-12"

# 목록 (전체)
python3 "$PY" --csv "$CSV" list

# 목록 (진행단계 필터)
python3 "$PY" --csv "$CSV" list --stage "1심"

# 목록 (앞으로 N일 이내 기일만)
python3 "$PY" --csv "$CSV" list --upcoming-days 14

# 단건 조회
python3 "$PY" --csv "$CSV" get 2025가합10737

# 갱신
python3 "$PY" --csv "$CSV" update 2025가합10737 \
  --진행단계 "변론종결" --다음기일 "2026-07-15"

# 종결 (진행단계=종결, 다음기일 비움)
python3 "$PY" --csv "$CSV" close 2025가합10737
```

### Claude가 자동 호출하는 패턴

| 사용자 발화 | 호출 |
|---|---|
| "내 사건 목록 보여줘" | `list` |
| "이번 주 기일 있는 사건" | `list --upcoming-days 7` |
| "2주 이내 기일" | `list --upcoming-days 14` |
| "○○사건 정보" | `get <사건번호>` |
| "○○사건 항소심으로 단계 바꿔" | `update <사건번호> --진행단계 "항소"` |
| "○○사건 종결됐어" | `close <사건번호>` |
| "새 사건 추가: ..." | `add ...` (사건번호 필수, 누락 시 사용자에게 묻기) |

## 동시 편집 주의

OneDrive·iCloud 등 동기화 폴더에 두면 여러 PC·세션이 동시에 수정할 수 있다. 본 스킬은 **원자적 임시파일 쓰기(temp → os.replace)** 로 단일 PC 안에서는 안전하지만, 두 PC가 동시에 쓰는 경우는 막을 수 없다. 다음을 권장:

- 동시 작업이 흔하면 git 저장소로 두고 push/pull
- 또는 JuriSupport MCP로 이전 권장

## JuriSupport와의 관계

- **JuriSupport 미연동**: 이 CSV가 정본. 모든 사건 메타데이터는 여기에.
- **JuriSupport 연동**: JuriSupport가 정본. CSV는 선택적 백업/오프라인 뷰. `list_cases` MCP 호출 결과를 CSV로 내보내는 export 용도로만 권장.

## 새 인덱스 시작하기

```bash
# 1. 템플릿 복사 (헤더만 들어있는 빈 CSV)
cp /Users/$USER/.claude/plugins/cache/jurisupport-plugins/songmu-legal/0.1.0/templates/_index.csv \
   <클라우드 사건폴더 경로>/_index.csv

# 또는 헬퍼로 직접 생성
python3 "$PY" --csv <경로>/_index.csv init
```

CLAUDE.md §5에 경로를 기록한다. 콜드스타트 인터뷰에서 묻는다.

## 한계

- CSV는 단순 평면 테이블. 사건 간 관계·증거·할일·문서 버전은 표현 못함.
- 대규모(수백 건↑) 또는 다중 사용자 동시 편집이 잦으면 JuriSupport 권장.
- 본 스킬은 기일 알림(notification)을 보내지 않음. `--upcoming-days` 필터로 사용자가 직접 조회.
