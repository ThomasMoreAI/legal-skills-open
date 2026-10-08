---
name: pa-workflow-inhouse-board-deck-legal-section-sboghossian
title: In-House — Board Deck Legal Section
description: Use when an in-house legal team needs to prepare the legal section of a board deck or board report. Covers litigation status, regulatory developments, compliance metrics, material agreements, and risk highlights — formatted for board-level consumption. Triggers when an in-house counsel asks for help preparing board materials, a legal update for the board, or a governance report for directors.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-inhouse-board-deck-legal-section
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# In-House — Board Deck Legal Section

Board members need to understand the company's legal exposure, not read a legal memo. The legal section of a board deck translates ongoing matters, regulatory developments, and risk into the board's language: materiality, probability, financial impact, and management action. This skill governs how an in-house team prepares that section with Claude's assistance.

## Purpose

Produce a board-ready legal section that covers five mandatory areas:
1. Litigation update (material matters only)
2. Regulatory and legislative developments
3. Compliance metrics
4. Risk register highlights
5. Material agreements signed or executed in the period

## Inputs

| Input | Why it matters |
|---|---|
| Current matter list | Source data for litigation update |
| Regulatory tracker | What regulatory developments occurred in the period |
| Compliance dashboard / metrics | Quantified compliance status |
| Risk register (if maintained) | Risk ratings for top items |
| Material agreements log | Contracts above the board's materiality threshold |
| Period covered | Quarter or specific period |

## Section structure

### 1. Litigation update

One row per material matter in a table. Board members do not need full case summaries — they need status, financial exposure, and the recommended reserve.

| Matter | Court / Jurisdiction | Status | Financial exposure | Reserve | Trend |
|---|---|---|---|---|---|
| Acme v. Company (contract dispute) | DIFC Courts | Pre-trial — hearing scheduled Q3 2026 | USD 2.5M claimed | USD 800K reserved | Stable |
| Regulatory investigation — DFSA | DFSA | Information requests ongoing | Fine: potential USD 500K | Nil (early stage) | Monitoring |
| Employment claim — [Name redacted] | UAE Labour Court | Conciliation failed — court hearing scheduled | AED 120K | AED 120K reserved | Stable |

**Format rules:**
- Include only matters above the board's materiality threshold (define in the intro: "matters with financial exposure > AED 500K or strategic significance")
- Do not include routine matters; aggregate those: "18 routine employment/commercial matters with aggregate exposure < AED 200K — all managed at GC level"
- Financial exposure: worst-case amount claimed, not the most likely outcome
- Reserve: amount provisioned in financial statements
- Trend: Improving / Stable / Deteriorating / Resolved

### 2. Regulatory and legislative developments

| Development | Jurisdiction | Effective date | Impact | Action required |
|---|---|---|---|---|
| UAE Digital Economy Law — data localisation provisions | UAE | 1 Jan 2027 | Requires server infrastructure changes | Tech team briefed; assessment in progress |
| DFSA crypto-asset framework update | DIFC | Already effective | New licensing requirement for [product] | External counsel engaged |
| KSA Employment Reform — HRSD update | KSA | March 2027 | Changes to gratuity calculation for KSA employees | HR + GC aligning |

Focus on developments that require management action or board decision. Exclude background regulatory changes with no company impact.

### 3. Compliance metrics

A single-page dashboard view:

| Metric | Status | Period trend |
|---|---|---|
| Contracts reviewed on time (< 5 business days) | 87% | ↑ from 78% last quarter |
| NDAs auto-processed (no legal review required) | 65% | ↑ new capability |
| Overdue legal holds | 0 | Stable |
| Training completion — AML/compliance | 94% of staff | ↑ |
| Data subject requests responded to within 30 days | 100% | Stable |

Include only metrics that the board has line-of-sight over. Do not include internal legal team process metrics.

### 4. Risk register highlights

Top 3–5 legal risks for board awareness. Format:

| Risk | Probability | Impact | Current mitigation | Owner |
|---|---|---|---|---|
| Regulatory non-compliance — new DFSA rule | Medium | High | External counsel engaged; project plan in place | GC + CTO |
| Concentration risk — single major commercial counterparty | Low | Very High | Contract review underway; diversification strategy | GC + CEO |
| IP exposure — competitor patent filing | Low | Medium | Freedom-to-operate analysis commissioned | GC + CTO |

### 5. Material agreements

| Agreement | Counterparty | Type | Value | Date signed | Notes |
|---|---|---|---|---|---|
| Software licence | Globex Corp | SaaS MSA | USD 1.2M / yr | March 2026 | 3-year term |
| Joint venture | ABC Holdings | JV Agreement | N/A | April 2026 | NewCo incorporated ADGM |
| Settlement | Acme (see Litigation) | Settlement deed | USD 350K | April 2026 | Full and final |

Include agreements above the board's pre-approved delegation of authority threshold.

## Board communication principles

- **Materiality over completeness**: boards cannot act on 40-page legal updates; synthesise to what matters.
- **Action-oriented**: every section item should end with a clear status (what management is doing) and whether board decision or awareness is needed.
- **No legal jargon**: "pre-trial interlocutory hearing" → "hearing before the main trial, scheduled Q3 2026".
- **Calibrated language**: avoid "might" and "could" when the probability is known — give the board the probability.
- **Forward-looking**: what is the expected development in the next quarter? Boards make decisions about the future, not the past.

## Jurisdiction-specific board governance notes

| Jurisdiction | Board legal section requirements |
|---|---|
| UAE (onshore, Dubai) | Companies Law (Federal Decree-Law on Commercial Companies) — directors have fiduciary duties; material litigation and regulatory matters are material disclosure items |
| DIFC | DIFC Companies Law — director duties include duty to exercise independent judgment; audit committee has oversight of legal risk |
| ADGM | ADGM Companies Regulations — similar to DIFC; audit committee role |
| KSA | Saudi Companies Law — board minutes must reflect material legal matters; SAMA/CMA regulated entities have specific disclosure requirements |
| Lebanon | Commercial Code — board disclosure requirements; less formalised than GCC |

## Related skills

- [[pa-workflow-inhouse-friday-newsletter-status-synthesis]]
- [[pa-workflow-inhouse-cross-functional-translation]]
- [[output-partner-memo-style]]
- [[output-table-of-comparisons]]
- [[output-timeline-builder]]
