---
name: pa-workflow-ip-prior-art-search-orchestrator-sboghossian
title: IP — Prior Art Search Orchestrator
description: Use when an IP attorney or patent agent needs a systematic prior-art search to assess novelty and non-obviousness before filing or during prosecution. Orchestrates searches across USPTO, EPO Espacenet, WIPO PatentScope, Google Scholar, industry publications, and open-source repositories, then synthesizes a structured novelty and non-obviousness assessment. Relevant for MENA filings (UAE, KSA, EG, GCC) as well as US, EP, and PCT national-phase proceedings.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-ip-prior-art-search-orchestrator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# IP — Prior Art Search Orchestrator

## Purpose

A structured prior-art search underpins every patentability opinion, prosecution response, and freedom-to-operate analysis. This workflow orchestrates parallel searches across the canonical databases, de-duplicates results, maps them against claim elements, and produces a novelty-and-non-obviousness assessment in a format usable by outside counsel or a patent committee.

## Inputs / Signals

| Input | Required | Notes |
|---|---|---|
| Invention disclosure or draft claims | Yes | Can be free text or formal disclosure form |
| Key technical terms + synonyms | Recommended | Inventor-supplied; reduces false negatives |
| International Patent Classification (IPC) codes | Optional | Narrows search; auto-suggest if not provided |
| Target filing jurisdictions | Optional | Defaults to US + EP + WO |
| Date range for prior art | Optional | Default: all dates; narrow to last 20 years for mature fields |
| Exclusions (known art, own prior filings) | Optional | Avoids re-surfacing known landscape |

## Search Methodology

### Pass 1 — Patent databases (parallel)

| Database | Coverage | Query type |
|---|---|---|
| USPTO Full-Text & Image (patents.google.com + USPTO) | US granted + published applications | Full text + classification |
| EPO Espacenet | EP, PCT, + 100+ patent offices worldwide | CPC classification + full text |
| WIPO PatentScope | PCT applications + national collections | Full-text + IPC |
| GCC Patent Office (GCCPO) | GCC granted patents | Title + abstract |
| National offices (SAIP, UAE MoE, EGYPO) | Country-specific | Abstract-level; limited full-text |

For each database: run claims as Boolean keyword queries; run IPC/CPC classification browse; run citation forward/backward walk on top hits.

### Pass 2 — Non-patent literature (NPL)

| Source | What to find |
|---|---|
| Google Scholar | Academic papers, conference proceedings, dissertations |
| arXiv, IEEE Xplore, ACM DL | Technical publications in CS, EE, engineering |
| Industry white papers / standards bodies | ETSI, IEEE, 3GPP, IETF RFCs |
| GitHub + open-source repositories | Code with timestamps that predates filing — functions as prior art for software claims |
| Product manuals, datasheets | Commercial prior art — publicly available before priority date |

### Pass 3 — Targeted inventor art

- Search inventor's own prior publications (conference papers, blog posts, GitHub commits) that could act as prior art under AIA §102(a)(1) or equivalents in non-grace jurisdictions
- Search co-inventor employment history for relevant work at former employers (ownership + novelty risk)

### Pass 4 — Synthesis

For each claim element, build a claim-chart matrix:

| Claim Element | Prior Art Reference | Publication Date | How it reads on the element | Materiality |
|---|---|---|---|---|
| Adaptive rate-limiting | US 10,xxx,xxx | 2019-03-12 | Discloses variable throttling, not adaptive | Low |
| Machine-learning feedback loop | CN 109xxx | 2020-07-01 | Discloses ML prediction but in different context | Medium |

## Output

```markdown
## Novelty Assessment

**Claim 1 (independent):** NOVEL — no reference discloses all elements in combination.
**Claim 2 (dependent):** LIKELY NOVEL — closest reference (US 10,xxx) discloses [X] but not [Y].
**Claim 5 (dependent):** AT RISK — EP 3,xxx,xxx discloses substantially the same method.

## Non-Obviousness Assessment

**Combination risk:** References A + B together suggest the invention might be obvious to PHOSITA.
**Teaching-away factor:** Reference B explicitly teaches away from [Y] — supports non-obviousness argument.
**Secondary indicia:** Commercial success of client's product using this method (to be documented).

## Recommendation
File with modified Claim 5 to differentiate from EP 3,xxx,xxx. Obtain inventor declaration on unexpected results for Claim 1 combination.

## Closest Prior Art
1. US 10,xxx,xxx — [title] — [summary of relevance]
2. EP 3,xxx,xxx — [title] — [summary of relevance]
3. arXiv:20xx.xxxxx — [title] — [summary of relevance]
```

## Jurisdictional Notes

### Grace Period Differences

| Jurisdiction | Inventor Grace Period | Notes |
|---|---|---|
| US (post-AIA) | 12 months | Applies to inventor's own disclosures only |
| EP | None | Any public disclosure before filing destroys novelty |
| UAE | None | Paris Convention member; strict novelty |
| KSA | None | SAIP follows international novelty standards |
| Egypt | None | EGYPO strict novelty |
| PCT / WO | None at international stage | National phase grace period varies |

### Software and Algorithm Claims

- **US**: Abstract ideas without "something more" fail Alice/Mayo. Method-of-operation framing helps.
- **EP**: Technical character required. Claims framed as technical means to solve a technical problem pass more reliably than pure algorithm claims.
- **MENA**: UAE, KSA, and EG patent laws generally follow civil-law traditions and do not grant patents for algorithms, business methods, or software per se. Technical-method claims (hardware + algorithm combination) are the most defensible path.

### Open-Source Prior Art

GitHub commits are prior art if the repository was publicly accessible before the priority date. For software inventions, always search GitHub for repositories with similar functionality and note the commit timestamp, not just the repository creation date.

## Limits and Escalation

- This workflow provides a preliminary patentability opinion. A **formal freedom-to-operate (FTO)** or **patentability opinion** for litigation or transactional purposes requires review by a registered patent attorney or patent agent.
- GCC national office databases (UAE, KSA, EG) have limited full-text searchability — a comprehensive search for those jurisdictions should include EPO's worldwide collection and PCT, which capture most substantive filings.
- Do not fabricate patent numbers. All references surfaced must come from the actual search query results.

## Related Skills

- [[pa-workflow-ip-patent-prioritization]]
- [[review-ip-freedom-to-operate]]
- [[kb-ip-patent-prosecution-mena]]
- [[draft-patent-claims]]
- [[pa-workflow-transactional-pia-privacy-impact-assessment]]
