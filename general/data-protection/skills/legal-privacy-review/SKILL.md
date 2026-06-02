---
name: legal-privacy-review
title: Legal Lite Privacy Review
description: DPA, 개인정보 처리 활동, DSAR, PIA/DPIA, privacy policy 변경을 검토합니다. 사용자가 제공한 정책/문서/처리 설명을 기준으로 개인정보 리스크와 확인 질문, 초안 산출물을 만들 때 사용합니다.
author: arik08
author_url: https://github.com/arik08/MyHarness/tree/main/.plugins/claude-for-legal-lite/skills/legal-privacy-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: ko
---

# Legal Lite Privacy Review

## 목적

사용자가 제공한 개인정보 관련 문서나 처리 설명을 바탕으로 DPA 검토, 개인정보 영향 검토, DSAR 응답 초안, 정책 갭 분석 초안을 작성합니다.

## 전제

- 법령 최신성, 관할별 세부 요건, 감독기관 가이드는 `[법무 확인 필요]`로 표시합니다.
- 실제 정보주체 통지, 신고, 회신 발송은 명시 승인과 법무 검토 전 실행하지 않습니다.
- 원문 또는 처리 설명에 없는 데이터 범주, 보관기간, 수탁자, 국외이전, 법적 근거는 추정하지 않습니다.

## 입력 분류

- DPA/위탁 계약 검토
- 신규 처리 활동 triage
- PIA/DPIA 초안
- DSAR 접수/응답 초안
- privacy policy 또는 내부 정책 변경 검토

## 검토 체크리스트

- 개인정보 범주와 민감정보 여부
- 처리 목적, 법적 근거, 동의/계약/정당이익 등 근거
- 정보주체, 아동/직원/고객/잠재고객 여부
- 수탁자/재수탁자, 국외이전, SCC/이전 장치
- 보관기간과 삭제/반환 절차
- 보안조치, 사고 통지, 감사권
- DSAR 본인확인, 기한, 예외, 제3자 정보
- 고위험 처리, 자동화 의사결정, 프로파일링

## 출력 형식

```md
# 개인정보 검토 초안: [주제]

## 결론
- 상태: [진행 가능 / 조건부 / 보류]
- 핵심 리스크:
- 필요한 승인/확인:

## 처리/문서 요약
| 항목 | 내용 |
|---|---|

## 리스크 및 권고
| 우선순위 | 항목 | 문제 | 권고 | 확인 필요 |
|---|---|---|---|---|

## 추가 질문
-

## 법무/개인정보 담당자 확인 필요
-
```
