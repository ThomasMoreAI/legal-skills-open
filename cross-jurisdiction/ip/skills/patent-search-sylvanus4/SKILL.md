---
name: patent-search-sylvanus4
title: Patent Search — Multi-Jurisdiction Prior Art Search
description: 'Multi-jurisdiction prior art search across Google Patents, USPTO PatentsView, KIPRIS/KIPO, Espacenet, WIPO Patentscope, and Semantic Scholar. Generates bilingual keyword sets (English + Korean), IPC/CPC classification codes, and applicant spelling variants. Outputs structured search results with jurisdiction coverage flags. Suggests accelerated examination suitability and examination request timing for Korean filings. Use when the user asks to "search prior art", "find similar patents", "novelty search", "prior art analysis", "freedom to operate search", "patent landscape", or "patentability search". Do NOT use for claim-vs-prior-art element mapping (use patent-claim-chart). Do NOT use for detecting patentable ideas in code (use patent-scanner). Do NOT use for drafting patent documents (use patent-us-drafting or patent-kr-drafting). Korean triggers: "선행기술 조사", "특허 검색", "신규성 조사", "선행기술", "FTO 검색".'
author: sylvanus4
author_url: https://github.com/sylvanus4/github-to-notion-sync/tree/main/.claude/skills/patent-search
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: ip
language: en
---

# Patent Search — Multi-Jurisdiction Prior Art Search

## Role

Expert patent search analyst who identifies relevant prior art across multiple
patent offices and academic databases, producing structured search reports with
bilingual keyword coverage and jurisdiction-specific metadata.

## Prerequisites

- WebSearch tool available for patent database queries
- WebFetch tool for retrieving patent document details
- Write tool for persisting results to `outputs/patent-search/{date}/`

## Workflow

### Step 0: Input Validation

Before Step 1, confirm and normalize inputs. Required:

1. **Technical field description** — domain and problem context (e.g., AI orchestration, distributed systems).
2. **At least three key technical features** — distinct mechanisms or structural elements (not marketing phrases).
3. **Target jurisdictions** — at least one of US, KR, EP, WO, or explicit “global”; default if unspecified: US + KR.

**Graceful degradation:**

- If the user provides **fewer than three features**, extract additional features from any attached documents, prior messages, or patent-scanner output before proceeding. If still fewer than three, ask the user to name missing differentiators.
- If **no technical details** are available (vague one-liner with no field, no features, no docs), **stop and ask** for field + three features + jurisdictions before running searches.
- If jurisdiction is vague (“worldwide”), treat as multi-source global search and include US + KR + WO minimum in coverage.

### Step 1: Understand the Invention

Collect from the user:
1. Technical field and problem being solved
2. Key technical features of the invention
3. Target jurisdictions (US, KR, or both — default: both)
4. Any known prior art references

If the user provides an existing draft or patent-scanner output, extract the
technical features from those files.

### Step 2: Generate Bilingual Keyword Sets

Produce a keyword matrix:

| Category | English Keywords | Korean Keywords | IPC/CPC Codes |
|----------|-----------------|-----------------|---------------|
| Core concept | ... | ... | ... |
| Variant terminology | ... | ... | ... |
| Component terms | ... | ... | ... |
| Effect/result terms | ... | ... | ... |

For Korean applicant/inventor names, generate multiple spelling variants:
- Romanization variants (e.g., Kim / Gim, Lee / Yi / Rhee, Park / Pak)
- Company name variants (e.g., Samsung Electronics / Samsung Elec. / 삼성전자)

### Step 3: Execute Multi-Source Search

Search these sources in parallel batches (max 4 concurrent):

| Source | URL Pattern | Coverage |
|--------|------------|----------|
| Google Patents | `patents.google.com/?q=...` | Global, full-text |
| USPTO PatentsView | `api.patentsview.org/patents/query` | US patents/applications |
| KIPRIS | `kipris.or.kr` | Korean patents/applications |
| Espacenet | `worldwide.espacenet.com` | EP, WO, JP, CN |
| WIPO Patentscope | `patentscope.wipo.int` | PCT applications |
| Semantic Scholar | `api.semanticscholar.org` | Academic publications |

For each source, use WebSearch with jurisdiction-specific query construction:
- US: English keywords + IPC/CPC + inventor/assignee
- KR: Korean keywords + English keywords + IPC/CPC + applicant spelling variants
- WO: English keywords + IPC + applicant

### Step 4: Analyze and Rank Results

For each result, extract and score:

| Field | Description |
|-------|-------------|
| `title` | Patent/paper title |
| `publication_number` | Document number |
| `filing_date` | Filing/priority date |
| `assignee` | Applicant/assignee name |
| `abstract` | Abstract text |
| `relevance_score` | 1-10 relevance to invention (LLM-assessed) |
| `overlap_elements` | Which invention features are disclosed |
| `kr_doc_included` | Whether KR document was found (boolean) |
| `jurisdiction` | US / KR / EP / WO / CN / JP |
| `ipc_codes` | IPC classification codes |

Rank by `relevance_score` descending. **Flag any result scoring 8+ as a potential
blocking reference** — these MUST appear in the `blocking_references` array in the
final JSON output. If no result scores 8+, `blocking_references` must still be
present as an empty array `[]`.

### Step 5: Generate Search Report

Write the report to `outputs/patent-search/{date}/search-results.json` with:

```json
{
  "search_date": "YYYY-MM-DD",
  "invention_summary": "...",
  "keywords": { "en": [...], "ko": [...] },
  "ipc_codes": [...],
  "results": [...],
  "blocking_references": [...],
  "coverage_summary": {
    "us_results": 0,
    "kr_results": 0,
    "ep_results": 0,
    "wo_results": 0,
    "academic_results": 0
  },
  "kr_filing_recommendations": {
    "accelerated_exam_suitable": true,
    "accelerated_exam_reason": "...",
    "recommended_exam_request_timing": "..."
  }
}
```

Also produce a human-readable summary at
`outputs/patent-search/{date}/search-summary.md`.

### Step 6: KR-Specific Recommendations

When Korean jurisdiction is included:
- Assess suitability for accelerated examination (가속심사) based on:
  - Green technology applicability
  - SME/startup status
  - Professional agency filing
  - Defense-related technology
- Recommend examination request timing within the 5-year window
- Note if prior art is predominantly in Korean (affects translation burden)

## Anti-Patterns (Common Mistakes)

1. **DO NOT** use generic keywords like “machine learning system” alone — always combine with specific technical mechanisms (e.g., routing graph, embedding index, scheduler policy).
2. **DO NOT** skip Korean keyword generation even when the user provides English-only input — always produce the Korean column in the keyword matrix.
3. **DO NOT** search only Google Patents and skip specialized databases — all six sources in Step 3 must be queried per run. A minimum of 4 out of 6 must return results; if a source is truly unreachable, document the skip with the reason. Fewer than 4 covered sources is a delivery failure.
4. **DO NOT** treat academic paper publication dates as patent filing dates — use patent filing/priority dates for patents; clearly label paper years separately.
5. **DO NOT** report results without **relevance_score** — every row must have a 1–10 score.
6. **DO NOT** omit `overlap_elements` from any result — every result must list which invention features are disclosed (use `[]` if none overlap).
7. **DO NOT** submit results without at least one IPC/CPC classification code in the keyword matrix — derive codes from the technical field even if the user does not provide them.
8. **DO NOT** forget the `blocking_references` array — any result with `relevance_score` ≥ 8 must be copied into this array; if none qualify, output `[]`.

## Worked Example (Test Invention Context)

**Invention:** LLM Agent Orchestration Platform that dynamically composes multi-agent workflows from a skill registry using semantic search-based routing, DAG-based execution ordering, and resource-aware model selection.

**Sample keyword matrix (excerpt):**

| Category | English Keywords | Korean Keywords | IPC/CPC Codes |
|----------|-----------------|-----------------|---------------|
| Core concept | multi-agent orchestration, skill registry composition, semantic routing LLM | 멀티에이전트 오케스트레이션, 스킬 레지스트리, 의미 기반 라우팅 | G06N 3/08, G06F 9/50 |
| Mechanism | DAG execution order, workflow DAG, topological task schedule | DAG 실행 순서, 워크플로우 그래프, 작업 스케줄 | G06F 9/48 |
| Resource | model tier selection, cost-aware LLM routing, latency SLO | 모델 티어 선택, 비용 인식 라우팅, 지연 목표 | G06N 20/00, G06F 9/455 |

Use this density of specificity — not generic “AI platform” terms alone.

## Pre-Delivery Check

Before presenting results or writing final artifacts, self-verify:

1. **Six sources, 4+ covered** — Google Patents, USPTO PatentsView, KIPRIS, Espacenet, WIPO Patentscope, and Semantic Scholar were all searched. At least 4 must have returned results (any skip is explicitly documented with reason). Fewer than 4 = FAIL.
4. **Blocking references** — the `blocking_references` array is present (populated with any result scoring ≥ 8, or `[]` if none qualify).
5. **Per-result fields** — every result in the JSON includes `relevance_score` (1-10) AND `overlap_elements` (list of invention features disclosed).
2. **Dual artifacts** — both `search-results.json` and `search-summary.md` paths are populated or explicitly waived by user.
3. **KR recommendations** — if KR jurisdiction was selected, `kr_filing_recommendations` is non-empty with accelerated exam and timing notes.
4. **Scores** — no result row has an empty or missing `relevance_score`.

If any check fails, fix or disclose before delivery.

## Output Artifacts

| Artifact | Path | Format |
|----------|------|--------|
| Structured results | `outputs/patent-search/{date}/search-results.json` | JSON |
| Human-readable summary | `outputs/patent-search/{date}/search-summary.md` | Markdown |

## Constraints

- Do NOT make legal conclusions about patentability — present evidence for
  human review
- Do NOT access paid patent databases that require subscriptions
- Always note that automated search cannot replace a professional patent search
- For KR results, note that KIPRIS search may require manual verification on
  the KIPRIS website

## Gotchas

- Google Patents search syntax differs from USPTO — use quotes for exact phrases
- KIPRIS romanization of Korean names is inconsistent — always search multiple
  spelling variants
- IPC and CPC codes overlap but are not identical — search both when available
- Academic papers may disclose prior art that predates patent filings — always
  include Semantic Scholar
- Filing dates vs publication dates: use filing/priority dates for novelty
  assessment, not publication dates
