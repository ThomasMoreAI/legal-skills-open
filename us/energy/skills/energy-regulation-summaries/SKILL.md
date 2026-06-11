---
name: energy-regulation-summaries
title: Energy Regulation Summary
description: Generates structured summaries of U.S. energy sector regulations and landmark cases with compliance-focused analysis. Use when summarizing FERC orders, state PUC decisions, renewable energy incentives, NEPA compliance, environmental review requirements, or energy case law for legal professionals, policymakers, or industry stakeholders.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/energy-regulation-summaries
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: energy
language: en
---

# Energy Regulation Summary

Produces structured regulatory intelligence covering U.S. energy regulations and case law, organized by utility regulation, renewable incentives, environmental compliance, and federal/state interactions.

## Quick Start

Gather before drafting:

1. **Scope** — time period, jurisdiction(s), topic focus (utility, renewables, environmental, or all)
2. **Sources** — specific regulations, orders, or case citations; if none provided, generate from general knowledge with `[VERIFY]` flags
3. **Audience** — legal/technical specialist or non-specialist stakeholder

## Output Structure

### 1. Executive Overview
- 3–5 most consequential developments in the period
- Key regulatory trends and directional signals

### 2. Utility Regulation

For each regulation, capture:

| Field | Content |
|-------|---------|
| Authority | Issuing agency (FERC, state PUC, etc.) |
| Effective Date | Precise date |
| Core Requirements | Rate-making, service obligations, grid modernization |
| Affected Parties | Regulated entities |
| Compliance Deadlines | Specific dates — never use "soon" |
| Pending Challenges | Litigation or rehearing status |

Topics: rate-making, service territory obligations, grid modernization, commission decisions, consumer protection.

### 3. Renewable Energy Incentives

| Mechanism | Status | Key Terms |
|-----------|--------|-----------|
| Federal tax credits (ITC/PTC) | | |
| Renewable Portfolio Standards | | |
| Feed-in tariffs / net metering | | |
| State incentive programs | | |

### 4. Environmental Compliance
- **NEPA** — EA vs. EIS triggers, applicable thresholds, recent guidance
- **State review** — analogous processes, coordination requirements
- **GHG regulations** — emission caps, reporting, intersection with siting
- **Permitting conflicts** — where environmental mandates constrain energy infrastructure

### 5. Significant Cases

Per case:
```
Court / Parties / Citation [VERIFY if uncertain]
Key Facts / Legal Issues / Holding / Reasoning
Industry Implications
```

### 6. Federal/State Interaction
- Preemption issues and jurisdictional conflicts
- Regulatory gaps or inconsistencies
- Cooperative federalism mechanisms

### 7. Compliance Action Items
- Required actions by entity type
- Documentation and reporting obligations
- Enforcement mechanisms and penalty exposure

### 8. Forward Look
- Pending rulemakings and proposed legislation
- Cases under appeal
- Emerging technology gaps (distributed generation, storage, hydrogen)

## Pitfalls and Checks

- Cite with CFR/USC references and reporter citations; flag uncertain citations with `[VERIFY]`
- Distinguish final rules from proposed rules and interim guidance
- Flag federal/state conflicts explicitly — do not gloss over them
- For non-specialist audiences, define technical terms (RPS, PURPA, FERC jurisdiction)
- Maintain neutral analytical framing — no policy preferences
- Scope is U.S. federal and state; note when analysis is limited to specific states
