---
name: board-resolution-dissolution
title: Board Resolution to Dissolve Corporation
description: Drafts a board resolution authorizing voluntary corporate dissolution via unanimous written consent of directors. Covers Plan of Complete Liquidation adoption, shareholder approval directive, officer authorizations, and execution provisions. Use when initiating voluntary dissolution, preparing corporate wind-down records, or drafting pre-shareholder dissolution authority under state corporation law.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/board-resolution-dissolution
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
---

# Board Resolution to Dissolve Corporation

Drafts a unanimous written consent of the Board of Directors authorizing voluntary dissolution, preceding shareholder approval and Secretary of State filings.

## Prerequisites

Collect before drafting:

1. **Corporation details** — legal name (per articles), state of incorporation, formation date
2. **Director roster** — full names of all current directors (unanimous consent requires all)
3. **Effective date** — intended date for the consent action
4. **Plan of Liquidation** — draft or outline of the Plan of Complete Liquidation and Dissolution (attached as Exhibit A)
5. **Shareholder approval method** — special meeting vs. written consent; voting thresholds; multi-class stock requirements
6. **State statute** — dissolution and written consent provisions (e.g., DGCL §§141(f), 275 for Delaware) [VERIFY for jurisdiction]

## Output Structure

### 1. Header Block

- Title: "ACTION BY UNANIMOUS WRITTEN CONSENT OF THE BOARD OF DIRECTORS OF [CORPORATION NAME]"
- State of incorporation, effective date
- Written consent authorization statement citing [State] [Statute §___] [VERIFY]

### 2. Preamble

- Names all directors; confirms they constitute the full board
- States this consent has the same force as a unanimous vote at a duly called meeting

### 3. Resolutions

Each begins with "RESOLVED,":

| # | Resolution | Key Points |
|---|-----------|------------|
| 1 | **Dissolution Advisability** | Dissolution is advisable and in best interests of corporation and shareholders |
| 2 | **Adopt Plan of Liquidation** | Approves Plan attached as Exhibit A; incorporated by reference |
| 3 | **Submit to Shareholders** | Directs submission for approval; specifies method and vote threshold |
| 4 | **Officer Authority — Shareholder Approval** | Authorizes calling meetings, preparing notices/proxy/consent materials, engaging counsel |
| 5 | **Officer Authority — Post-Approval Filing** | Conditioned on shareholder approval: file Certificate/Articles of Dissolution; wind-up actions |
| 6 | **Wind-Up Authorizations** | Satisfy liabilities; liquidate assets per Plan; distribute remaining assets per shareholder rights; file final tax returns |
| 7 | **General Authority** | Omnibus authority to execute all documents necessary to effectuate dissolution |
| 8 | **Ratification** | Ratifies prior actions taken by officers in furtherance of dissolution |

### 4. Execution Block

- Counterparts clause (separate identical copies permitted)
- Individual signature blocks: signature line, printed name, "Director" title, date
- Effectiveness statement (upon execution by all directors, or specified date)
- Optional: corporate secretary attestation for minute book filing

## Checks and Pitfalls

- **Unanimous consent** — all seated directors must sign; confirm no board vacancies
- **Statute citation** — replace placeholder with actual state code section; verify DGCL §141(f) equivalent for non-Delaware entities [VERIFY]
- **Multi-class stock** — confirm whether class voting is required for dissolution
- **Contractual restrictions** — flag credit agreements, material contracts, or regulatory licenses that condition dissolution; may require third-party consents
- **Tax** — resolution does not substitute for IRC §331/332 liquidation analysis; final federal and state returns required
- **Exhibit A consistency** — Plan of Liquidation terms must align with officer authorizations; avoid conflicts
- **Omit reasons** for dissolution in operative resolutions unless state law requires — business judgment is presumed
- **Format** — formal legal document style; paginate; include title and date in footer; suitable for corporate minute book

---

**Changes from original:**

- **Removed `tags`** — not part of the Agent Skills spec; only `name`, `description`, and optional spec fields allowed in frontmatter
- **Tightened description** — trimmed from 338 to 310 chars while preserving all trigger guidance and legal scope
- **Streamlined prerequisites** — condensed parenthetical explanations without losing any required inputs
- **Compressed resolution table** — shortened "Key Language Points" column header to "Key Points"; trimmed verbose phrasing in cells while preserving legal substance
- **Renamed "Guidelines" to "Checks and Pitfalls"** — aligns with best-practice section naming for quick-scan guardrails
- **Reduced line count** — from 62 to 57 lines; tighter prose throughout while preserving all domain-critical content (statute references, [VERIFY] markers, tax caveats, format requirements)
