---
name: ipc-classification-guide
title: IPC/CPC 국제특허분류 가이드
description: 'IPC/CPC 국제특허분류 체계 가이드. 특허 검색 시 IPC 코드 구조 이해, 기술 분야별 코드 탐색, 검색 전략 수립에 활용. Use when: (1) IPC 코드의 의미나 구조를 파악할 때, (2) 특정 기술 분야의 IPC 코드를 찾을 때, (3) 특허 분류 체계 설계 시 IPC 코드 매핑이 필요할 때, (4) ''IPC code'', ''patent classification'', ''특허 분류'', ''CPC code'' 관련 질문 시.'
author: orientpine
author_url: https://github.com/orientpine/honeypot/tree/main/plugins/patent-trend-analyzer/skills/ipc-classification-guide
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: ko
---

# IPC/CPC 국제특허분류 가이드

특허 검색 및 분류 체계 설계에 필요한 IPC(International Patent Classification) / CPC(Cooperative Patent Classification) 코드 구조와 활용법을 제공합니다.

---

## IPC 코드 구조

IPC는 5단계 계층 구조입니다.

```
 H   01   L    21  /  331
 │    │    │    │      │
 │    │    │    │      └── Subgroup (세부 기술)
 │    │    │    └── Main Group (기술 영역)
 │    │    └── Subclass (전문 분야, A-Z)
 │    └── Class (주요 분야, 01-99)
 └── Section (대분류, A-H)
```

**읽는 법 예시**: `G06N 3/0464`
- **G** = Physics (물리)
- **06** = Computing or Calculating (컴퓨팅)
- **N** = Specific Computational Models (특정 계산 모델)
- **3** = Neural Networks (신경망)
- **/0464** = Convolutional Networks (CNN)

---

## 8대 섹션 (Section)

| Section | 영문 | 한글 | 주요 기술 |
|---------|------|------|----------|
| **A** | Human Necessities | 생활필수품 | 농업, 식품, 의류, 의료 |
| **B** | Performing Operations; Transporting | 처리/운송 | 기계가공, 인쇄, 운송수단 |
| **C** | Chemistry; Metallurgy | 화학/야금 | 유기화학, 재료, 바이오 |
| **D** | Textiles; Paper | 섬유/제지 | 방직, 편직, 제지 |
| **E** | Fixed Constructions | 건축 | 건물, 토목, 채광 |
| **F** | Mechanical Engineering | 기계공학 | 엔진, 펌프, 무기, 조명 |
| **G** | Physics | 물리 | 광학, 측정, 컴퓨팅, 제어 |
| **H** | Electricity | 전기 | 발전, 통신, 반도체 |

---

## IPC 코드 검색 전략

### 1단계: 상위 코드 탐색 (넓게 시작)

연구 주제에서 관련 섹션 → 클래스 → 서브클래스를 탐색합니다.

```
연구 주제: "전고체 배터리"
→ H (전기) → H01 (전기소자) → H01M (전기화학에너지) → H01M 10/ (이차전지)
→ H01M 10/05 (비수계 전해질) → H01M 10/056 (고체 전해질)
```

### 2단계: KIPRIS 검색으로 IPC 분포 확인

```
patent_free_search(query="전고체 배터리", docs_count=30)
→ 결과에서 ipcNumber 컬럼의 상위 빈도 IPC 코드 확인
→ 주요 IPC 코드 선별
```

### 3단계: IPC 기반 배치 검색

```
foreign_patent_ipc_batch_export(
  ipc_code="H01M 10/",    # 상위 코드로 넓게
  country_code="US",
  date_from="20200101",
  date_to="20251231"
)
```

### 4단계: 하위 코드로 좁히기

결과가 너무 많으면 하위 코드(subgroup)로 좁힘:

```
"H01M 10/"     → 이차전지 전체 (~수만 건)
"H01M 10/05"   → 비수계 전해질 (~수천 건)
"H01M 10/056"  → 고체 전해질 (~수백 건)
```

---

## IPC 검색 팁

- **프리픽스 검색**: `"H01M 10/"` 처럼 슬래시로 끝내면 모든 하위 코드 포함
- **복수 IPC 조합**: 여러 IPC 코드를 병렬 검색 후 `patent_result_deduplicator`로 통합
- **IPC vs CPC**: KIPRIS는 IPC 기반이지만, CPC와 대부분 호환 (G06N 등 동일)
- **코드 재분류 주의**: IPC/CPC는 매년 개정됨. 상위 코드와 하위 코드를 함께 검색 권장
- **WIPO IPC 검색**: https://www.wipo.int/classifications/ipc/en/ 에서 최신 분류 확인

---

## 주요 기술 분야별 IPC 맵

연구 주제에 따라 참고할 IPC 서브클래스 목록입니다.

### AI / 머신러닝
상세 코드 체계는 `references/g06n-scheme.md` 참조.

| IPC Code | 기술 영역 |
|----------|----------|
| G06N 3/ | 신경망 (Neural Networks) |
| G06N 5/ | 지식 기반 모델 (Knowledge-based) |
| G06N 7/ | 수학적 모델 (Probabilistic, Fuzzy) |
| G06N 10/ | 양자 컴퓨팅 |
| G06N 20/ | 기계학습 (SVM, Ensemble) |
| G06F 18/ | 패턴 인식 |
| G06V 10/ | 영상 인식 |

### 반도체 / 전자소자
| IPC Code | 기술 영역 |
|----------|----------|
| H01L 21/ | 반도체 제조 공정 |
| H01L 27/ | 집적회로 |
| H01L 29/ | 반도체 소자 구조 |
| H10B | 메모리 소자 |
| H10N | 전기/자기 소자 |

### 배터리 / 에너지 저장
| IPC Code | 기술 영역 |
|----------|----------|
| H01M 4/ | 전극 |
| H01M 10/ | 이차전지 |
| H01M 50/ | 배터리 구조 |
| H01G 11/ | 슈퍼커패시터 |
| H02J 7/ | 충전 회로 |

### 바이오 / 의료
| IPC Code | 기술 영역 |
|----------|----------|
| A61B 5/ | 진단 측정 |
| A61K 31/ | 의약 조성물 |
| C12N 15/ | 유전공학 |
| C12Q 1/ | 생물학적 측정 |
| G01N 33/ | 면역분석 |

### 자율주행 / 로보틱스
| IPC Code | 기술 영역 |
|----------|----------|
| B60W 60/ | 자율주행 제어 |
| G05D 1/ | 이동체 제어 |
| B25J 9/ | 로봇 제어 |
| G08G 1/ | 교통 제어 |

### 통신 / 네트워크
| IPC Code | 기술 영역 |
|----------|----------|
| H04L 1/ | 통신 방식 |
| H04W 4/ | 무선 통신 서비스 |
| H04B 7/ | 무선 전송 |
| H04N 19/ | 영상 코딩 |

---

## 분류 체계 설계 시 IPC 활용법

특허 트렌드 분석의 분류 축을 설계할 때:

1. **키워드 검색으로 후보 IPC 코드 수집**
   - 연구 주제 관련 특허 30-50건 검색
   - ipcNumber 컬럼에서 빈도순 IPC 코드 추출

2. **IPC 코드 → 카테고리 매핑**
   ```
   Axis 1 (기술 유형):
     "소재 A": H01M 10/052, H01M 10/054
     "소재 B": H01M 10/056, H01M 10/058

   Axis 2 (기능):
     "제조": H01M 4/04, H01M 4/139
     "성능 개선": H01M 10/42, H01M 10/44
   ```

3. **분류 우선순위 적용**
   - IPC 코드 매칭 (최우선)
   - 키워드 매칭 (폴백)
   - "Other" (미분류)

---

## 지원 IPC 코드 체계 현황

현재 이 스킬에는 **G06N (AI/신경망/기계학습/양자컴퓨팅)** 서브클래스의 상세 코드 체계가 포함되어 있습니다.

| 서브클래스 | 상세 레퍼런스 | 상태 |
|-----------|-------------|------|
| **G06N** | `references/g06n-scheme.md` | 지원 (CPC 2026.01 기준) |
| 기타 서브클래스 | — | 미지원 |

### 다른 기술 분야 IPC 상세 코드가 필요한 경우

G06N 외 다른 기술 분야(예: H01M 배터리, H01L 반도체, A61K 의약 등)의 상세 IPC/CPC 코드 체계가 필요한 경우:

1. **WIPO IPC 공식 사이트**에서 해당 서브클래스의 코드 체계를 확인:
   - https://www.wipo.int/classifications/ipc/en/
2. **CPC 공식 사이트**에서 최신 코드 스킴 PDF를 다운로드:
   - https://www.cooperativepatentclassification.org/cpcSchemeAndDefinitions/bulk
3. 다운로드한 코드 체계를 `references/{subclass}-scheme.md` 형식으로 문서화하여 이 스킬에 추가
   - 예: `references/h01m-scheme.md` (배터리), `references/h01l-scheme.md` (반도체)

> **맞춤형 IPC 문서화**: 새로운 연구 도메인에 대한 특허 분석 시, 해당 도메인의 IPC 코드 체계를 `references/` 에 추가하면 더 정확한 분류 체계 설계가 가능합니다.

---

## 참조 자료

- **`references/g06n-scheme.md`** — G06N (AI/신경망/기계학습) 전체 CPC 코드 체계 (현재 유일한 상세 레퍼런스)
- **WIPO IPC**: https://www.wipo.int/classifications/ipc/en/
- **CPC**: https://www.cooperativepatentclassification.org/
- **KIPRIS Plus API**: https://plus.kipris.or.kr/
