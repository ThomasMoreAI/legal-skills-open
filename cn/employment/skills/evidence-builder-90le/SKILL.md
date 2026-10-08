---
name: evidence-builder-90le
title: Evidence Builder
description: Build worker-side evidence checklists, evidence gap plans, lawful preservation steps, and employer-controlled document requests for China labor disputes. Use when a user has layoff, dismissal, forced resignation, unpaid wages, salary cut, transfer, contract expiry, unsigned contract, or arbitration preparation facts and needs to know what evidence to preserve, collect, request, or verify.
author: 90le
author_url: https://github.com/90le/worker-rights-cn/tree/main/plugins/worker-rights-cn/skills/evidence-builder
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cn
practice: employment
language: en
---

# Evidence Builder

## Overview

Turn labor dispute facts into an evidence plan. Use source-card anchors and termination maps from `layoff-defense` when available, and label evidence strength without inventing facts.

## Workflow

1. Accept only normalized input supplied by the orchestrator and return only this skill's documented output. Do not ask the user to select or chain internal skills. Report missing facts to the orchestrator.
2. Consume the orchestrator-provided termination classification; if it is absent, return the missing input instead of invoking another skill.
3. Read `references/evidence-matrix.json` and select evidence bundles by `termination_map`, claim type, and source anchors.
4. Classify each evidence item as `available`, `missing`, `employer_controlled`, `third_party`, or `create_now`.
5. Prioritize collection as `P0_immediate`, `P1_core`, `P2_supporting`, or `P3_local_verify`.
6. Output lawful preservation steps and request language; do not suggest illegal data access or fabricated records.

## Evidence Status Rules

- `available`: the worker already has the item or can lawfully access it.
- `missing`: the item is needed but not yet located.
- `employer_controlled`: the employer likely controls the item; ask for it in writing or request production during arbitration.
- `third_party`: bank, tax, social insurance, housing fund, hospital, delivery platform, or government system may provide it.
- `create_now`: the worker should create a truthful timeline, written objection, preservation memo, or request based on existing facts.

## Output Format

Return:

- `case_evidence_summary`: short summary of what the evidence must prove.
- `termination_maps_used`: mapped categories such as `economic_layoff` or `constructive_dismissal`.
- `source_anchors`: source-card anchors supporting the evidence plan.
- `evidence_checklist`: grouped items with status, priority, purpose, lawful source, and collection note.
- `evidence_gaps`: missing or employer-controlled items that affect claim strength.
- `preservation_steps_24h`: immediate lawful steps for the next 24 hours.
- `request_to_employer`: concise wording for requesting documents or written reasons.
- `risk_flags`: signing risk, limitation risk, protected status, confidential data, group layoff, high-value claim, or lawyer review.
- `next_skill`: usually `compensation-calculator`, `agreement-review`, `arbitration-drafter`, or `layoff-defense`.

## Legal Safety

Do not advise the user to fabricate, alter, backdate, secretly take company data, bypass access controls, copy customer lists, export source code, leak trade secrets, or make false allegations. If a document is employer-controlled, say to request it lawfully or ask the arbitration tribunal to order production.

## Resources

Read `references/evidence-matrix.json` when building an evidence checklist, gap plan, or employer document request.
