---
name: legal-profile-setup
title: Legal Lite Profile Setup
description: Claude for Legal Lite 스킬들이 로컬 회사 기준으로 작동하도록 `.myharness/claude-for-legal-lite/profile.md` playbook을 만들거나 업데이트합니다. 계약 기준, 개인정보/AI 정책, 승인 매트릭스, 출력 스타일을 정리할 때 사용합니다.
author: arik08
author_url: https://github.com/arik08/MyHarness/tree/main/.plugins/claude-for-legal-lite/skills/legal-profile-setup
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: ko
---

# Legal Lite Profile Setup

## 목적

반복 검토 품질이 유지되도록 프로젝트 로컬 playbook을 정리합니다. 기본 위치는 `.myharness/claude-for-legal-lite/profile.md`입니다.

## 원칙

- 사용자가 제공한 기준만 기록합니다.
- 불확실한 기준은 `[미정]`으로 남깁니다.
- 법무팀 확인 전에는 “회사 정책”처럼 단정하지 않습니다.
- 기존 프로필이 있으면 보존하고, 필요한 항목만 제안합니다.

## 진행

1. 기존 `.myharness/claude-for-legal-lite/profile.md`가 있으면 읽습니다.
2. 없으면 `references/profile-template.md` 구조를 참고해 초안을 제안합니다.
3. 다음 범위 중 필요한 것만 묻습니다.
   - 계약: 절대 불가 조항, 책임 제한, 자동 갱신, 데이터/IP, 승인 기준
   - 개인정보/AI: 적용 관할, 고위험 처리, 금지/조건부 허용 AI 사용, 벤더 기준
   - 제품/마케팅: 금지 표현, substantiation이 필요한 claim
   - 고용/HR: 고위험 인사조치, 승인자, 관할
   - 출력: 내부 메모, 사업부 요약, 외부 전달 톤
4. 사용자가 파일 생성을 원하면 UTF-8로 작성합니다.

## 출력

프로필을 바로 저장하지 않는 경우, 사용자가 검토할 수 있게 Markdown 초안을 제공합니다.

```md
# Claude for Legal Lite Profile

## 기본 정보
...
```
