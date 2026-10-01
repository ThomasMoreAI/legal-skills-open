---
name: england-wales-pre-action-protocol-checker-rohasnagpal
title: England and Wales Pre-Action Protocol Checker
description: Checks the applicable pre-action protocol or Practice Direction requirements before civil proceedings in England and Wales. Use when the claim type, parties, facts and contemplated forum are known; do not use for Scotland or Northern Ireland.
author: rohasnagpal
author_url: https://github.com/rohasnagpal/legal-ai-skills/tree/main/plugins/vclo-by-rohas/skills/england-wales-pre-action-protocol-checker
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: litigation
language: en
---

# England and Wales Pre-Action Protocol Checker

Read and apply the [UK Counsel instructions](../../agents/uk-counsel.md) before substantive analysis or drafting.

## Jurisdiction gate

Confirm that UK law governs the issue and identify the relevant UK legal jurisdiction and forum.

If the matter is governed by another jurisdiction, or the governing jurisdiction is unclear, do not apply UK rules. Return it to vCLO for neutral intake or the appropriate jurisdiction counsel.

## Required inputs

Obtain the represented party, objective, material facts and dates, governing law, forum, procedural posture, available documents and intended deliverable. Do not silently supply a fact that changes applicability, deadline or outcome.

## Method

1. Identify the claim type, parties, relief, value, urgency, limitation position and contemplated court.
2. Determine whether a specific pre-action protocol or the general Practice Direction applies.
3. Map letter, response, disclosure, expert, ADR, timing and costs requirements to evidence and actions.
4. Flag urgent relief, limitation protective filing, sanctions risk and current-rule or court-specific checks.

## Output

Provide the requested analysis or draft with scope, supported facts, applicable authority, procedural or deadline position, practical actions, information gaps and verification status. Cite current primary sources with pinpoints where available and identify any point requiring qualified local counsel.

## Safeguards

Do not invent law, authority, dates, filings or source access. Do not call a document filing-ready while current forms, fees, rules, service and local practice remain unchecked. Distinguish facts, allegations, assumptions and analysis.
