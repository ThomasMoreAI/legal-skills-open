---
name: policy-application-checker-2
title: Policy & Application Checker
description: Read policies, application requirements, and forms, then turn them into a completeness checklist, risk list, and submission plan.
author: FDU-INS
author_url: https://github.com/FDU-INS/Insurance-Skills/tree/main/Skills/policy-application-checker-2
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Policy & Application Checker

## Purpose

Read policies, application requirements, and forms, then turn them into a completeness checklist, risk list, and submission plan.

## Trigger phrases

- 检查材料是否齐全
- application checklist
- 读政策做清单
- submission readiness
- requirements checklist

## Ask for these inputs

- policy text or form
- deadline
- applicant profile
- required attachments
- known blockers

## Workflow

1. Extract mandatory requirements, deadlines, and conditional branches.
2. Transform them into a checklist with evidence slots.
3. Flag ambiguous wording and missing proof.
4. Sequence tasks into a submission plan backward from the deadline.
5. Never assume a requirement is satisfied without evidence.

## Output contract

- completeness checklist
- risk list
- submission timeline
- evidence tracker

## Files in this skill

- Script: `{baseDir}/scripts/checklist_builder.py`
- Resource: `{baseDir}/resources/checklist_template.md`

## Operating rules

- Be concrete and action-oriented.
- Prefer preview / draft / simulation mode before destructive changes.
- If information is missing, ask only for the minimum needed to proceed.
- Never fabricate metrics, legal certainty, receipts, credentials, or evidence.
- Keep assumptions explicit.

## Suggested prompts

- 检查材料是否齐全
- application checklist
- 读政策做清单

## Use of script and resources

Use the bundled script when it helps the user produce a structured file, manifest, CSV, or first-pass draft.
Use the resource file as the default schema, checklist, or preset when the user does not provide one.

## Boundaries

- This skill supports planning, structuring, and first-pass artifacts.
- It should not claim that files were modified, messages were sent, or legal/financial decisions were finalized unless the user actually performed those actions.


## Compatibility notes

- Directory-based AgentSkills/OpenClaw skill.
- Runtime dependency declared through `metadata.openclaw.requires`.
- Helper script is local and auditable: `scripts/checklist_builder.py`.
- Bundled resource is local and referenced by the instructions: `resources/checklist_template.md`.
