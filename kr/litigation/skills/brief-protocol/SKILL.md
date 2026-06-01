---
name: brief-protocol
title: 준비서면 작성 표준 절차 (Brief Protocol)
description: 준비서면 작성 표준 절차 - 사건 인테이크부터 정본 등록·PDF 추출까지 일관된 오케스트레이션. brief-draft, korean-law, beopgoeul-search, JuriSupport(또는 MD) 스킬을 순서대로 호출하고 각 단계에서 사용자 승인을 받음. 판례 자동 검증은 korean-law 1차 + 법고을 2차 (lbox-search 스킬 자동 호출 안 함, lbox는 사용자 수동 검색용). 법원 전자제출 자체는 자동화하지 않으며 사용자가 직접 수행.
author: jurisupport
author_url: https://github.com/jurisupport/jurisupport-plugins/tree/main/plugins/songmu-legal/skills/brief-protocol
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: kr
practice: litigation
language: ko
---

# 준비서면 작성 표준 절차 (Brief Protocol)

## What this skill does

준비서면(또는 답변서·의견서·소장) 작성을 **인테이크 → MD 초안 → 인용 검증 → 정본 등록(JuriSupport 또는 MD) → PDF 추출** 5단계로 표준화한다. 각 단계에서 사용자 승인을 받고 다음으로 진행한다. **법원 전자제출(ecfs 등) 자체는 본 스킬의 범위에 포함하지 아니하며, 사용자가 직접 수행한다.**

## When to use

- "○○ 사건 준비서면 작성해줘"
- "○○ 사건 답변서 표준 절차로 작성"
- "/songmu-legal:brief-protocol" 직접 호출
- 사건번호 + 서면 유형 언급 시 자동 트리거

## Prerequisites

플러그인의 `CLAUDE.md` 플레이북이 채워져 있어야 한다. 비어있으면 `/songmu-legal:cold-start-interview` 먼저 실행.

## Workflow

### Phase 1: 인테이크 (Intake)

사용자로부터 다음을 수집:
- **사건번호 또는 사건명**
- **서면 유형**: 준비서면 / 답변서 / 의견서 / 소장 / 항소이유서 / 상고이유서 / 보정서 / 소송비용액확정신청서 / 검찰 기록열람등사 신청서 / 기타
- **제출 기한** (선택)
- **특별 지시사항** (선택)

> 의뢰인 서류 요청 시: 변호사가 직접 발급 가능한 공적 서류(등기사항증명서, 주민등록등본 등)는 의뢰인에게 요청하지 말고 주소/식별정보만 요청. 사실관계 미확인 항목은 의뢰인 확인 후 추가.

#### 사건 메타데이터 조회 (다음 순서)
1. JuriSupport MCP 연동 시: `get_case` / `list_cases` 로 사건 정보 확보
2. 미연동 또는 못 찾으면: **`case-index` 스킬** 로 CSV 인덱스 조회 — `case_index.py --csv <CSV 사건 인덱스 경로> get <사건번호>`
3. 두 곳 모두 없으면 사용자에게 직접 묻고, 확인된 정보는 CSV에 `add` 하거나 (JuriSupport 연동 시) `create_case` 호출

> **신규 사건이면**: JuriSupport 연동 사용자는 먼저 https://jurisupport.com/cases 에서 사건을 등록한 뒤 작업을 진행하시면 좋습니다.
> 전자소송 사건목록을 엑셀로 저장하여 업로드하면 사건이 자동으로 일괄 등록됩니다.
> 또는 사건번호만 있으면 `mcp__jurisupport__create_case` 로 즉시 등록 가능.

`hearing-check` 스킬(있다면) 또는 case-index의 `list --upcoming-days 14`로 임박 기일 확인:
- 2주 이내 기일이 있으면 알림
- 기한 역산 (제출 기한이 없으면 기일 5일 전 권장)

### Phase 2: 사건기록 분석 + 초안 (Draft)

`brief-draft` 스킬 호출 (기존 글로벌 스킬, `~/.claude/skills/brief-draft/`):
- Phase 1: 사건기록 탐색 (JuriSupport → 로컬 → OneDrive)
- Phase 2: 쟁점 추출
- Phase 3: 교과서 검색 (`legal-books` DB)
- Phase 4: 목차 작성 → **사용자 승인 대기**
- Phase 5: 초안 생성

추가 확장:
- 유사 사건이 있는지 `case-records` DB 검색 (538개 사건)
- 우리측 과거 서면 패턴 참조

### Phase 3: 인용 검증 (Verify)

**이 단계는 강제. 절대 스킵하지 않음.**

초안에서 다음을 추출하여 자동 검증:

#### 3-1. 법령 인용 검증
```
초안의 모든 "○○법 제○조" 패턴 추출
→ korean-law MCP get_law_text 호출
→ 조문 실존 + 텍스트 일치 확인
→ 불일치 시 사용자에게 보고
```

#### 3-2. 판례 인용 검증
```
초안의 모든 "대법원 0000. 0. 00. 선고 0000다00000 판결" 패턴 추출

[1차 검증 — korean-law MCP, 플러그인 기본 동작]
→ korean-law MCP search_precedents(query=판례번호 또는 키워드) 호출
→ 결과에 동일 판례번호가 있으면 ✅ 일치
→ get_precedent_text 로 본문 확보 후 인용구 글자단위 비교

[2차 검증 — 법고을(beopgoeul-search), 무료 공식 인프라]
→ 1차에서 못 찾은 판례만 beopgoeul-search 스킬로 재조회
  (대법원도서관 lx.scourt.go.kr, ~/jurisupport-beopgoeul/ toolkit)
→ 사건번호·법원·선고일·PDF URL을 구조화 데이터로 반환
→ beopgoeul-search 스킬이 없으면 이 단계는 자동 스킵

⚠️ lbox-search **스킬 자동 호출 금지** — 도구 불안정으로 결과 신뢰 불가.
   다만 lbox.kr 사이트 자체는 사용자가 직접 수동 검색해도 됨 (필요 시 사용자에게 안내).

[최종 처리]
→ 두 경로 모두 실패 → "(미확인)" 표시하고 사용자에게 보고
→ 사용자가 lbox.kr 등에서 수동으로 확인해 알려주면 그 결과를 반영
→ 절대 가짜 판례번호를 그대로 두지 말 것
```

#### 3-3. 직접인용 정확도 검증
```
초안의 모든 " " 따옴표 인용구 추출
→ 출처(판결문/법령/교과서) 원문과 글자 단위 비교
→ 불일치 시 간접인용으로 변환 제안
```

#### 3-4. 검증 리포트 출력
```
■ 인용 검증 결과
- 법령 인용: 12건 중 12건 일치 ✅
- 판례 인용: 5건 중 4건 일치, 1건 미확인 ⚠️
  - 대법원 2020. 5. 14. 선고 2020다12345 판결 → 검색 결과 없음
- 직접인용: 8건 중 7건 일치, 1건 불일치 ⚠️
  - "고의 또는 중대한 과실" → 원문 "고의 또는 중과실" (간접인용 권장)
```

사용자가 보고 수정 지시 → 반영 → 다시 검증.

### Phase 4: 정본 확정 (MD 유지)

**모든 단계의 정본은 MD 파일.** 자동으로 PDF·DOCX·JuriSupport에 올리지 않는다.

#### 4-1. MD 파일 위치 및 명명

```
저장 위치: <작성문서 디렉토리>/<사건번호>_<당사자>/<서면명>_<YYYYMMDD>.md
  (예: ~/작성문서/2025가단12345_홍길동/준비서면_1차_20260519.md)
버전 관리: 파일명 날짜 변경 또는 git 커밋
```

#### 4-2. 문서 전달 (Delivery)

사용자가 "이 서면 보여줘", "내용 줘봐" 등 문서 본문을 요청하면:
- **파일 첨부·외부 도구 변환이 아니라 MD 본문을 채팅에 출력**
- 사용자가 복사·붙여넣기 할 수 있도록 그대로 노출
- 양식(빈칸·서명란 등)이 필요한 경우에도 텍스트로 출력

#### 4-3. 공통 원칙

- 점(•) 글머리 기호 사용 금지 (들여쓰기+텍스트 prefix로 처리)
- **HWP 변환 경로는 사용하지 않는다** (한글 변환 품질 신뢰 어려움)

### Phase 5: 출력 형식 옵션 (사용자 명시 요청 시에만)

**기본은 MD까지로 종료.** 사용자가 "PDF로 뽑아줘", "docx로 출력해줘", "JuriSupport에 올려줘" 등 명시 요청한 경우에만 다음 옵션 중 선택:

| 옵션 | 용도 | 도구 | 비고 |
|---|---|---|---|
| **PDF** | 법원 제출·외부 전달 | `pandoc`(typst 엔진) / `kordoc` | 가장 범용. 서증 첨부 시 PDF merge |
| **DOCX** | 의뢰인 편집용·재단작성 | `pandoc` | 점(•) 금지, 들여쓰기+prefix |
| **JuriSupport** | 소송서류 정본 보관 | `create_legal_document` | **소송서류 한정**: 소장·답변서·준비서면·항소·상고이유서. 신청서·보정서·의견서 등은 PDF/DOCX만 선택 |

요청 형식이 모호하면 위 세 옵션을 사용자에게 제시하고 선택받기.

#### 5-A. PDF 출력

```
pandoc <md경로> --pdf-engine=typst \
  -V mainfont="Apple SD Gothic Neo" -V monofont="Apple SD Gothic Neo" \
  -o <md경로>.pdf
```

권장 파일명: `<사건번호>_<일자>_<서면명>_원고 대리인_<변호사명>.pdf`

서증 첨부 시:
- `list_case_evidence(caseId)` (JuriSupport 연동 시) 또는 사용자 직접 지정
- 신규 서증 외 재인용은 호증 번호만 본문 인용
- 신규 서증 PDF는 별도 파일로 함께 전달

#### 5-B. DOCX 출력

```
pandoc <md경로> -o <md경로>.docx
```

점(•) 글머리 기호 변환 시 들여쓰기+텍스트 prefix로 후처리.

#### 5-C. JuriSupport 등록 (소송서류 한정)

```
create_legal_document(
  title: <서면 제목>,
  documentType: complaint | brief | answer | appeal,
  content: <MD 본문>,
  caseId: <사건 UUID>,
  status: "draft"
)
→ 반환된 문서 ID 보관
```

등록 후 수정 사이클:
- 작은 수정: `inline_edit_legal_document(documentId, ...)`
- 대화형 수정: `chat_legal_document(documentId, ...)`
- 섹션 단위 교체: `update_legal_document(documentId, content: ...)`

> ⚠️ JuriSupport 등록 후에는 MD에서 다시 편집해 재업로드하지 말 것. 두 곳 동시 수정 시 정본 충돌.
> 증거 반복 인용은 `isReference` 방식 사용 (중복 등록 금지).

#### 5-D. 법원 전자제출 (자동화 안 함)

⚠️ 본 단계 이후 법원 전자제출(로그인·서명·제출)은 본 플러그인 책임 범위 외. 사용자가 ecfs.scourt.go.kr 등에 직접 접속하여 처리.

### Phase 6: 사용자 최종 확인

```
✅ 산출 완료 — 법원 제출은 사용자가 직접 수행
- 사건: <사건번호> <법원명>
- 서면: <서면 유형>, <분량>
- 정본(MD): <작성문서 디렉토리 경로>
- 선택한 출력 형식 산출물 (있는 경우만):
  · PDF: <경로>
  · DOCX: <경로>
  · JuriSupport: <document_id> (status: draft) — 소송서류만
- 신규 서증 (제출용 별도 파일이 있는 경우): <파일 목록>
- 재인용 서증: <갑X호증 등 번호 목록>

다음 단계는 사용자가 직접 수행:
1. 법원 전자제출 시스템(ecfs.scourt.go.kr 등)에 직접 접속
2. 사건 선택 → 서면(PDF 또는 직접 작성) + 서증 업로드 → 전자서명 → 제출
3. 제출 완료 후 알려주시면 사후 상태 갱신
```

### Phase 7: 제출 후 상태 갱신

사용자가 "제출 완료" 알림 → 다음 중 해당하는 항목만 수행:

- MD 파일명에 `_submitted_<YYYYMMDD>` suffix 추가 (rename)
- JuriSupport에 등록한 서면이 있다면: `update_legal_document(documentId, status: "submitted")`
- 관련 할일 완료 처리 (`update_task_status` — JuriSupport 연동 시)
- 사건 진행 메모 갱신: "<날짜> <서면 유형> 제출"
- 차회 기일·후속 할일 확인 (`hearing-check` 호출)
- CSV 사건 인덱스 사용 시: 진행단계 갱신

## 사용자 승인 게이트 (Hard Gates)

다음 지점에서 **반드시 사용자 승인**을 받아야 다음 단계로 진행:

1. Phase 2 → Phase 3: **목차 확인** 후
2. Phase 3 → Phase 4: **검증 리포트 확인** 후
3. Phase 4 → Phase 5: **MD 정본 확정** 후, "출력 형식 변환할까요? (PDF/DOCX/JuriSupport, 또는 건너뛰기)" 묻기
4. Phase 5 → Phase 6: **선택한 출력 형식 산출 완료** 후 (옵션 건너뛴 경우 즉시 진입)
5. Phase 6 → 종료: 사용자가 "전자제출 완료" 알려줄 때

각 게이트에서 AskUserQuestion으로 사용자에게 명시적으로 묻는다.

## 서면 유형별 분기

각 유형에 맞는 표준 구조는 플러그인 `CLAUDE.md` §8 참조.

- **준비서면**: `~합니다 / ~입니다` 경어체
- **소장**: `~합니다 / ~입니다` 경어체
- **답변서·의견서·신청서·보정서**: `~합니다 / ~입니다` 경어체
- **항소·상고이유서**: `~합니다 / ~입니다` 경어체, 항소·상고 이유 명확히 항목화

> 모든 소송서류는 `~합니다 / ~입니다` 격식체로 통일한다 (CLAUDE.md §9 참조).

## Notes

- 이 스킬은 **오케스트레이션 스킬**이다. 실제 작업은 글로벌 스킬·MCP에 위임한다.
- 검증 단계는 절대 스킵하지 말 것. OCR/hallucination 위험이 가장 큰 단계.
- 보정서는 갑호증 없이 **첨부서류(소명자료)**로만 구성. 서면 유형이 보정서일 때 갑호증 관련 로직을 건너뛴다.
- 증거조사 방법 제안 시: **사실조회보다 공적 기관 문서제출명령 우선** (확정일자, 매매계약서, 금융거래내역, 부동산 소유내역 등 공적 기관이 보유한 기록은 문서제출명령이 더 확실).
- JuriSupport 연동 시: **당사자 확인/등록 → 사건 확인/등록 → 본 업무(서면 작성)** 순서 준수. 누락 시 직접 등록 후 진행.
