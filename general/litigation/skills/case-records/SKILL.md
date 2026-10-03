---
name: case-records
title: 사건기록 검색 스킬 (case-records)
description: 사무소 과거 사건기록과 작성서류를 로컬 FTS로 검색. 명시적으로 외부 임베딩을 허용한 환경에서는 하이브리드 검색도 가능. 주장서면·신청서면 위주로 "비슷한 사건이 있었나, 우리가 어떻게 주장했나, 어떤 신청을 했나"에 답한다. 사건 0건일 때는 검색 시도하지 말고 사용자에게 추가 안내.
author: jurisupport
author_url: https://github.com/jurisupport/jurisupport-plugins/tree/main/skills/case-records
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: general
practice: litigation
language: ko
---

# 사건기록 검색 스킬 (case-records)

## When to use

- "비슷한 사건 있었나?"
- "우리가 전에 이런 주장한 적 있어?"
- "상대측이 보통 뭐라고 반박하지?"
- "이 쟁점 법원은 어떻게 판단했어?"
- 의견서/준비서면 작성 시 과거 우리 서면의 표현·구성 참조
- 작성서류 폴더와 사건기록 폴더를 사건번호 기준으로 함께 검색해야 할 때

## legal-books와의 차이

- **legal-books** (포트 8766): 교과서 → "법리가 무엇인가"
- **case-records** (포트 8767): 사건기록/작성서류 → "우리가 어떻게 주장했고 어떤 신청을 했는가" (기본 로컬 FTS)
- 서면 작성 시 **둘 다 검색** 권장

## 저장·인덱싱 전략

- 원본 파일은 복사하지 않는다. DB에는 텍스트 청크, 원본 경로, 출처만 저장한다.
- `source_kind=record`: 사건기록 폴더(받은 자료, 상대방 서면 등)
- `source_kind=draft`: 작성서류 폴더(우리 주장서면, 의견서, 신청서 등)
- 기본 인덱싱 범위는 `doc_category=argument/application` 이다.
- 증거, 계약서, 등본, 영수증, 기일통지, 판결문 등은 기본 제외한다. 필요하면 `--doc-scope all`.

## 파싱 범위

- 기본 지원: PDF, DOCX, MD, TXT
- HWPX: zip/xml 구조를 로컬에서 직접 읽는다.
- DOC: macOS `textutil` 또는 `antiword`가 있으면 읽는다.
- HWP: `hwpjs`가 설치되어 있으면 읽는다. 없으면 건너뛴다.

## 사전 확인

```bash
curl -s http://localhost:8767/health
```

- 서버 미응답 → 사용자에게 실행 요청
- `cases: 0` → 사용자에게 사건 추가 안내 (`guides/03_case_records.md`)
- `cases: N>0` → 검색 진행

## 검색 API

```bash
~/case-records/scripts/search_case_records.py "검색어" --top-k 5 --doc-category argument
```

응답:
```json
{
  "query": "...",
  "results": [
    {
      "chunk_id": "2018가단11111_007_0023",
      "case_id": "2018가단11111",
      "case_name": "홍○○ 대여금",
      "doc_type": "준비서면",
      "doc_category": "argument",
      "source_kind": "draft",
      "doc_date": "2018-09-20",
      "author_role": "피고 대리인",
      "source_file": "/Users/me/작성문서/2018가단11111_홍○○_대여금/020_준비서면.docx",
      "chunk_text": "...",
      "score": 0.84
    }
  ]
}
```

## 인용 규칙

답변에 사용할 때:

1. **사건번호 + 사건명 + 문서종류 + 일자** 표기
2. **직접인용("...")**은 chunk_text와 글자 단위 일치 확인
3. 인용 후 "**그러나 현재 사건의 사실관계가 다를 수 있으니 직접 검토 필요**" 안내
4. "**판례**" 표현 금지 → "판결" 또는 "판단"

## 개인정보 보호

- 기본 인덱싱은 사건기록 본문을 외부 임베딩 API로 보내지 않는다.
- `--allow-external-embedding` 또는 `CASE_RECORDS_ALLOW_EXTERNAL_EMBEDDING=1`이 설정된 환경에서는 사건 본문 또는 검색 쿼리가 Gemini API로 전송될 수 있으므로, 사용 전 사무소 정책과 의뢰인 비밀유지 기준을 확인한다.
- `/search` API는 `~/.jurisupport/case-records.token`의 로컬 bearer token이 있어야 응답한다. 스킬은 `search_case_records.py` helper를 사용해 토큰을 자동으로 읽는다.

## 사건이 없을 때

> 현재 사건기록 DB가 비어 있습니다.
> `~/jurisupport-plugins/guides/03_case_records.md`를 참조하여 과거 사건을 인덱싱해 주세요.
> 5~10건 정도 추가하면 검색 결과가 의미 있어집니다.

## 추가 도구

- 사건 1건 추가: `~/case-records/scripts/ingest_case.sh`
- 사건폴더 일괄 인덱싱: `~/case-records/scripts/ingest_all.sh --root ~/사건`
- 사건기록+작성서류 동시 인덱싱: `~/case-records/scripts/sync_records.sh --record-root ~/사건기록 --draft-root ~/작성문서`
- 검색 helper: `~/case-records/scripts/search_case_records.py "검색어" --top-k 5`
- 서버 관리: `~/case-records/scripts/server.sh {start|stop|restart|status}`
- 가이드: `~/jurisupport-plugins/guides/03_case_records.md`
