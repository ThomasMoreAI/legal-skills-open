---
name: beopgoeul-search
title: 법고을 자동 검색 스킬 (beopgoeul-search)
description: 법고을(대법원 도서관 lx.scourt.go.kr) 판례·법령 자동 검색. Selenium 기반으로 키워드 검색하여 사건번호·법원·선고일·PDF URL을 구조화된 데이터로 반환. 무료 공식 사이트. lbox 유료 계정 없는 경우 1차 검색 도구.
author: jurisupport
author_url: https://github.com/jurisupport/jurisupport-plugins/tree/main/skills/beopgoeul-search
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: kr
practice: litigation
language: ko
---

# 법고을 자동 검색 스킬 (beopgoeul-search)

> 무료 공식 판례 검색. `~/jurisupport-beopgoeul/` toolkit 설치 시 자동 작동.

## When to use

- "법고을에서 ○○ 판결 찾아줘"
- "이 쟁점 관련 판례 검색"
- "사건번호 2024다302217 정보 가져와줘"
- "이 키워드로 무료 판례 검색"

## 사용 방법

### Step 1. 검색 실행

```bash
~/jurisupport-beopgoeul/scripts/search.sh "검색어" --max 5 --format json
```

또는 사용자가 "법고을에서 검색해줘"라고 하면 클로드가 자동 호출.

### Step 2. 결과 활용

응답 예시 (text):

```
[1] 서울고등법원 2020. 5. 27. 자 2019라2172 결정 [소송비용액확정]
    법원        : 서울고등법원
    사건번호    : 2019라2172
    선고/결정일 : 2020.5.27. (결정)
    PDF URL     : https://lx.scourt.go.kr/data_lib/.../25d80f7b-...pdf
    요약        : [대상결정] 서울고등법원 ... [사안의 개요] ...
```

JSON 형식 (--format json):

```json
[
  {
    "title": "서울고등법원 2020. 5. 27. 자 2019라2172 결정 [소송비용액확정]",
    "court": "서울고등법원",
    "case_no": "2019라2172",
    "decided_date": "2020.5.27.",
    "decision_type": "결정",
    "case_name": "소송비용액확정",
    "pdf_url": "https://lx.scourt.go.kr/data_lib/.../...pdf",
    "summary": "[대상결정] ..."
  }
]
```

### Step 3. PDF 다운로드 (사용자 직접)

검색 결과의 `pdf_url`을 클로드가 다음과 같이 안내:

> 1번 판결이 가장 적합합니다. 다음 URL을 브라우저에서 클릭하여
> `사건폴더/06_참고판례/법고을/` 에 저장해 주세요.
>
> https://lx.scourt.go.kr/data_lib/.../25d80f7b-...pdf
>
> 저장 후 알려주시면 본문 분석해드립니다.

⚠️ PDF 자동 다운로드는 의도적으로 하지 않음 (사이트 부하 줄이기). 사용자가 한 번의 클릭으로 다운로드.

### Step 4. PDF 분석

사용자가 PDF 저장 후 알리면 클로드가 본문 읽어 본 사건 쟁점에 적용·정리.

## 호출 옵션

| 옵션 | 기본값 | 설명 |
|---|---|---|
| `--max N` | 5 | 최대 결과 수 (최대 20) |
| `--format text\|json` | text | 출력 형식 |

## 데이터 정확성 검증 (필수)

검색 결과를 인용하기 전에:

1. **사건번호** — 결과에 표시된 사건번호가 사용자에게 보여준 PDF URL의 사건번호와 일치하는지
2. **선고일** — title에서 파싱한 일자가 정확한지
3. **법원** — 사건번호로 법원 종류 일치 (예: 2019라2172 → 결정 → 고등법원·대법원)
4. **인용 시** 사건번호·선고일·법원명을 PDF 원문에서 한 번 더 확인
5. 본문 표현은 "**판결**" 사용 (`판례` 금지)

## 양심적 사용

- 대량 자동 호출 자제 (정부 사이트 부하)
- 같은 키워드 반복 호출 시 결과 캐싱하여 재사용
- 자동 PDF 다운로드 안 함 (사용자가 직접 한 번)

## fallback — lbox로 넘어갈 때

법고을 결과가 부족하거나 적합한 판결 없을 때:

```
법고을에 적합한 판결이 없으셨다면 lbox.kr에서 시도해 보세요.
다음 키워드를 추천드립니다.

(키워드 제안)

lbox는 자동화가 약관 위반이므로, lbox.kr 로그인 → 직접 검색 →
PDF 다운로드 → 06_참고판례/lbox/에 저장 후 알려주세요.
```

자세한 워크플로우: `guides/06_precedent_search.md` 참조.

## Skill 미설치 시

`~/jurisupport-beopgoeul/scripts/search.sh`가 없으면 본 스킬은 사용 불가. 사용자에게 다음 안내:

> 법고을 자동 검색 toolkit이 설치되지 않았습니다.
> 설치: `bash ~/jurisupport-plugins/toolkit/beopgoeul/install.sh`
>
> 또는 toolkit 없이 진행하시려면 검색 URL을 생성해드릴 테니
> 브라우저에서 직접 검색하시고 결과를 알려주세요.
