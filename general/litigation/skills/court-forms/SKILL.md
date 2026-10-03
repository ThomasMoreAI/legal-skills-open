---
name: court-forms
title: 법원 양식 검색 스킬 (court-forms)
description: 대한민국 법원 전자소송포털 공개 양식모음 DB를 검색하고 공식 HWP/PDF/DOC 양식을 다운로드해 서식 작성에 활용한다. 주소보정서, 소장, 답변서, 임차권등기명령신청서 등 법원 양식을 찾거나 사건 정보로 양식 작성 초안을 만들 때 사용.
author: jurisupport
author_url: https://github.com/jurisupport/jurisupport-plugins/tree/main/skills/court-forms
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: ko
---

# 법원 양식 검색 스킬 (court-forms)

## When to use

- "주소보정서 양식 찾아줘"
- "임차권등기명령신청서 양식으로 작성하자"
- "소송위임장 공식 양식 받아서 채워줘"
- 서면 작성 중 공식 법원 양식 여부를 확인해야 할 때

## 사전 확인

```bash
~/court-forms/scripts/court_forms.py info
```

- `forms: 0`이면 먼저 동기화:

```bash
~/court-forms/scripts/court_forms.py sync
```

- 스크립트가 없으면 설치:

```bash
~/jurisupport-plugins/toolkit/court-forms/install.sh
```

## 검색

```bash
~/court-forms/scripts/court_forms.py search "주소보정" --top-k 5
~/court-forms/scripts/court_forms.py search "임차권등기명령" --category 신청 --top-k 5
```

응답에는 `form_id`, 제목, 분야, 첨부파일 목록, 다운로드 URL이 포함된다.

## 다운로드

가능하면 검색 결과의 `form_id`로 정확히 받는다.

```bash
~/court-forms/scripts/court_forms.py download --form-id "<form_id>" --kind hwp --out-dir .
```

빠른 사용은 검색어로도 가능하다.

```bash
~/court-forms/scripts/court_forms.py download --query "주소보정" --kind hwp --out-dir .
```

`--kind`는 `hwp`, `hwpx`, `doc`, `docx`, `pdf`, `all` 중 하나다.

## 레포 자산화

공식 원본 파일까지 모두 레포에 넣어 검색·작성용 Markdown으로 만들려면:

```bash
~/court-forms/scripts/court_forms.py sync --download all --continue-on-error
~/court-forms/scripts/court_forms.py export-md \
  --output data/court-forms \
  --copy-files \
  --download-missing \
  --continue-on-error
```

생성 구조:

```text
data/court-forms/
  README.md
  forms.jsonl
  forms/<분야>/<form_id>_<제목>/index.md
  forms/<분야>/<form_id>_<제목>/original/<공식 원본 파일>
```

`index.md`는 검색·초안 작성용 파생물이다. 제출·편집 기준은 `original/`의 공식 HWP/PDF/DOC 파일로 둔다.

## 작성 워크플로우

1. 양식명·사건유형으로 검색한다.
2. 공식 HWP 또는 PDF를 다운로드한다.
3. 사건번호, 법원, 당사자, 대리인, 주소, 청구취지 등 사건 정보로 채울 항목을 추출한다.
4. HWP 편집 도구가 없으면 Markdown 작성 지시서와 입력값 표를 만든다.
5. 최종 제출 전 사용자가 전자소송 사이트에서 직접 확인·제출한다.

## 출처 표기

전자소송포털 저작권보호정책상 법원이 저작재산권 전부를 보유한 자료는 자유이용 가능하지만, 출처를 구체적으로 표시해야 한다.

산출물 또는 내부 DB 설명에 다음을 남긴다.

```text
출처: 대한민국 법원 전자소송포털 양식모음
```

## 주의

- 전자제출·전자서명은 자동화하지 않는다.
- 양식은 수시로 바뀔 수 있으므로 실사용 전 `sync`로 최신 메타데이터를 갱신한다.
- 대량 원본 다운로드는 `--download all`로 가능하지만 기본값은 메타데이터만 동기화다. 필요한 양식만 다운로드한다.
