---
name: korean-law-lookup-pnuskgh
title: Korean Law Lookup — 법령 조회
description: '한국 법령·조례·행정규칙·판례·행정해석 등을 조회하고 정확하게 인용할 때 사용. "이 조문 원문 찾아줘",

  "이 법 최근에 개정됐어?", "이 답변에 나온 인용 진짜야?", "이 계약서 법적 리스크 검토해줘", "이 처분

  근거가 뭐야", "OO 조례 상위법이랑 안 맞는 거 아냐?" 같은 요청에 사용한다.

  `korean-law-mcp`가 연동되어 있으면 그 도구를 최우선으로 쓰고, 없으면 법제처 국가법령정보센터를

  WebFetch/WebSearch로 직접 조회한다.'
author: pnuskgh
author_url: https://github.com/pnuskgh/pskills/tree/main/.claude/skills/korean-law-lookup
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: kr
practice: general
language: ko
---

# Korean Law Lookup — 법령 조회

한국 법령/조례/행정규칙/판례/행정해석을 정확히 조회하고 인용하기 위한 스킬이다. 이 스킬을 쓰는
에이전트(법률 컨설턴트, 투자·금융 규제 컨설턴트 등)는 법률 자문 자격이 없는 AI이므로, 이 스킬의
출력은 항상 "실제 변호사/전문가 확인 필요" 전제 위에서 쓰인다 — 그 고지 자체는 호출하는 에이전트가
최종 산출물에 남긴다.

## 0. 우선순위 — MCP가 있으면 MCP, 없으면 WebFetch

- `mcp__korean-law-mcp__*` 도구가 이 환경에 등록되어 있으면(도구 목록에 보이면) **그것을 최우선으로
  사용한다.** 법제처 DB를 직접 조회하므로 정확도가 높고, WebFetch로는 할 수 없는 인용 검증·행위시법
  판단 같은 기능도 제공한다.
- MCP 도구가 없으면 법제처 국가법령정보센터(https://www.law.go.kr/main.html)를 WebFetch/WebSearch로
  직접 조회한다. 이 경로는 정확도가 떨어질 수 있으므로 "확인 일자"를 반드시 남기고 더 신중하게 인용한다.

## 1. 목적별 도구 선택 (MCP 사용 시)

| 목적 | 도구 | 비고 |
| :--- | :--- | :--- |
| 법령/조례/행정규칙 이름 검색 → ID 확보 | `search_law` | 다른 대부분의 조회 전에 먼저 실행해 `lawId`/`mst`를 얻는다 |
| 조문 전문 조회 | `get_law_text` | `mst`/`lawId` + `jo`(자연어 표기 권장, 예: "제148조의2") |
| 별표/서식 조회 (금액·기준표 등) | `get_annexes` | `lawName` + `annexNo` 또는 `query` |
| 판례·해석례·심판례 등 18개 도메인 검색 | `search_decisions` | `domain` 지정 필수(precedent/interpretation/tax_tribunal 등) |
| 위 검색 결과의 전문 조회 | `get_decision_text` | `domain` + `id` |
| 복합 리서치(법령명 불명확한 자연어 질문, 법체계, 처분 근거, 분쟁 준비, 개정이력, 조례 비교, 절차, 계약서 검토) | `legal_research` | `task`로 세분화 — 모르면 기본값(`full_research`) |
| 인용 검증(할루시네이션 방지), 판례 생사확인, 행위시법, 조문 영향맵 | `legal_analysis` | `mode`로 세분화 |
| 조례의 상위법 정비 필요 여부 | `ordinance_radar` | |
| 위 도구로 안 되는 전문 분야(조세심판/관세/헌재/노동위 등 80+개) | `discover_tools` → `execute_tool` | 먼저 `discover_tools`로 도구를 찾은 뒤 `execute_tool`로 실행 |

### 작업 흐름 예시

- "관세법 제38조 원문 찾아줘" → `search_law`(query="관세법")로 `lawId` 확보 → `get_law_text`(jo="제38조")
- "이 답변에 나온 법 조문 인용이 실제로 있는 거 맞아?" → `legal_analysis`(mode="verify_citations", text=검증할 텍스트)
- "이 계약서 법적 리스크 검토해줘" → `legal_research`(task="document_review", text=계약서 전문)
- "음주운전 처벌 기준이 뭐야" (법령명이 불명확한 질문) → `legal_research`(task="full_research")
- "2023년에 이 법 뭐 바뀌었어" → `legal_research`(task="amendment_track", scenario="timeline" 또는 "time_travel")
- "이 처분의 법적 근거가 뭐야" → `legal_research`(task="action_basis")

## 2. 인용 규칙

- 조문은 항상 "OO법 제O조 제O항" 형식으로 인용하고, 확인 일자를 함께 남긴다.
- 법령은 시행일자별로 버전이 다를 수 있다 — `get_law_text`의 `efYd`(시행일자) 지정이 필요한지 먼저
  판단한다. 계약/처분 등 특정 시점 기준으로 적용 법령을 확인해야 하면 `legal_analysis`(mode=
  "applicable_law")로 행위시법을 확인한다.
- 판례/심판례 인용은 사건번호를 정확히 표기하고, 최신 변경·폐기 여부가 중요하면 `legal_analysis`(mode=
  "cite_check")로 확인한다.

## 3. 출처 신뢰 우선순위

1. `korean-law-mcp` (법제처 공식 DB 직접 조회)
2. 법제처 국가법령정보센터 웹페이지 (WebFetch, MCP 미가용 시)
3. (보조, 신뢰도 낮음) 기타 정리된 데이터셋 — 사용하더라도 최신성을 1·2번으로 교차 검증한다

## 4. 에러 핸들링

- `search_law`로 `lawId`/`mst`를 못 찾으면 약칭·다른 표기로 검색어를 바꿔 재시도한다.
- `legal_analysis`(mode="verify_citations")에서 "실존불가"·"미확인"으로 나오면 그 사실을 그대로
  보고하고, 해당 인용을 빼거나 수정하도록 제안한다 — 조용히 넘기지 않는다.
- MCP 도구가 오류를 반환하면(예: 인증키 만료) 법제처 웹페이지 조회로 폴백하고, MCP 문제를 사용자에게
  보고한다.
- `search_decisions`/`get_decision_text`는 도메인이 18개로 나뉘어 있으므로, 어느 도메인인지 애매하면
  먼저 사용자에게 확인하거나 `legal_research`(task="full_research")로 넘겨 자동 감지에 맡긴다.

## 출력 형식

- 조문/판례 원문 인용 + 출처(법령명·조번호 또는 사건번호) + 확인 일자를 항상 함께 제시한다.
- 여러 결과를 비교해야 하면 표로 정리한다.
- 인증키(`LAW_OC` 등) 값이나 다른 자격증명은 어떤 출력에도 노출하지 않는다.
