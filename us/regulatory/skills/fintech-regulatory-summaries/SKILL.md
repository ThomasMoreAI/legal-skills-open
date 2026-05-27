---
name: fintech-regulatory-summaries
title: Fintech Regulatory Summaries
description: Generates structured regulatory summaries for fintech compliance covering crypto, payments, lending, mobile banking, and money transmission. Covers CFPB, SEC, CFTC, FinCEN, OCC, Federal Reserve, and state regulators with urgency triage and compliance deadlines. Use when compliance officers or legal teams need recent regulatory updates, agency guidance monitoring, or regulatory status reports.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/fintech-regulatory-summaries
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
---

# Fintech Regulatory Summaries

Produces structured regulatory updates for fintech compliance officers and legal counsel to identify critical developments, deadlines, and required actions.

## Quick Start

Gather before generating:

1. **Sectors** — crypto, payments, lending, mobile banking, regtech
2. **Time window** — default 90 days; adjust as needed
3. **Jurisdictions** — federal only, specific states, or multi-jurisdictional
4. **Business context** (optional) — company's regulated activities for materiality tailoring

## Output Structure

### 1. Executive Overview

3–5 bullets, each with:
- **What changed** — rule/guidance/enforcement action + agency
- **Who it affects** — specific fintech activity or model
- **Urgency** — `Immediate` / `Near-Term` / `Monitor`
- **Deadline** — effective date or comment period close

### 2. Detailed Analysis

Per development:

| Field | Content |
|---|---|
| **Source** | Agency, title, FR citation or docket no. `[VERIFY]` |
| **Effective/Comment Date** | Date or "Proposed — Comment by [date]" |
| **Sectors Affected** | Crypto exchanges / Processors / Lenders / MSBs |
| **Key Requirements** | Numbered compliance obligations from regulatory text |
| **Ambiguities** | Interpretive uncertainty or pending guidance |
| **Recommended Action** | Next steps: update policies, file comments, gap analysis |

### 3. Regulatory Overlap Map

Flag where multiple frameworks apply to one development (e.g., crypto custody implicating SEC + OCC + FinCEN). Note federal/state conflicts or gaps.

### 4. State Spotlight (if applicable)

Cover divergence in:
- Money transmitter licensing (MTL)
- State crypto/digital asset frameworks
- Consumer lending rate caps or disclosure rules

### 5. International Context (crypto/cross-border only)

Note alignment or divergence with EU MiCA, FATF guidance, or major foreign regulator actions material to U.S. multinationals.

## Agency Checklist

- [ ] CFPB — consumer protection, BNPL, open banking (1033)
- [ ] SEC — digital asset securities, broker-dealer
- [ ] CFTC — crypto derivatives, commodity tokens
- [ ] FinCEN/Treasury — AML/BSA, beneficial ownership, travel rule
- [ ] OCC — bank charter, crypto custody, fintech partnerships
- [ ] Federal Reserve — payments, FedNow, Reg E/Z
- [ ] State regulators — MTL, lending, state bank rules

## Pitfalls

- **Cite primary sources only** — Federal Register, agency releases, official guidance. Tag unconfirmed citations `[VERIFY]`.
- **Distinguish document types** — final rules, proposed rules, guidance/no-action letters, and enforcement actions carry different compliance weight.
- **Never conflate guidance with binding regulation** — flag where agency position lacks formal rulemaking.
- **Include comment deadlines for proposed rules** — note significant industry objections.
- **Urgency tiers** — Immediate: effective/past due. Near-Term: within 90 days. Monitor: proposed or 90+ days.
- **Acknowledge ambiguity** — do not assert false certainty on unsettled regulatory questions.
