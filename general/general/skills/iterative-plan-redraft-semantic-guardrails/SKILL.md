---
name: iterative-plan-redraft-semantic-guardrails
title: Iterative Plan Redraft Semantic Guardrails
description: Harden a repeatedly re-reviewed documentation/contract plan after adversarial reviewers keep finding semantic gaps despite new test rows.
author: vamseeachanta
author_url: https://github.com/vamseeachanta/workspace-hub/tree/main/.claude/skills/workspace-hub-learned/iterative-plan-redraft-semantic-guardrails
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
tags: [planning, adversarial-review, docs-contracts, semantic-guardrails, workspace-hub]
---

# Iterative Plan Redraft Semantic Guardrails

Use when a plan has already gone through one or more adversarial review waves and reviewers keep finding that the draft is still not approval-ready because the plan text is internally inconsistent or the proposed tests only prove word presence, not semantics.

## When this applies

Typical signals:
- the plan has been patched after review, but the `## Adversarial Review Summary` still says `FAIL` / `MAJOR` as if it applies to the new text
- reviewers say a requirement is "independently testable" only in the weak sense that it has its own test row, but the test is just a phrase-presence check
- documentation/contract plans add new docs without bringing them under existing stale-reference guardrails
- the plan cites a local artifact/report and reviewers flag ambiguity about whether it is canonical branch truth or only local attestation
- open questions remain in the Risks section even though TDD/acceptance criteria already assume the decision is settled

## Core lessons

1. Historical review state must be marked as historical
- If you materially patch a plan after a review wave, do NOT leave the body saying the draft currently `FAIL`s unless that still truly applies to the patched text.
- Rewrite the section so prior verdicts are labeled as historical/superseded.
- Add a current-state line like `PENDING RE-REVIEW` until the next rerun lands.

2. Exact pass conditions beat generic presence checks
For docs/contract plans, reviewers will often reject tests like:
- "requirement present"
- "daily cadence language present"
- "forbidden string absent"

Strengthen them into exact pass conditions such as:
- exact phrases that must appear
- required co-location rules (same section/paragraph)
- required companion obligations (for example, not just mention daily freshness, but also require refreshing a named artifact)
- exact field names
- exact allowed enum values
- minimum example counts (`>= 3` concrete signatures, not just "multiple")

3. Resolve open-vs-required contradictions
- If acceptance criteria or tests already lock a decision, do not leave the same question open under Risks/Open Questions.
- Either resolve the question in the plan or make the acceptance criteria conditional.
- Reviewers will mark this as a MAJOR internal contradiction.

4. Separate universal rule from local example
If a plan is trying to generalize a workspace-specific path or mechanism:
- define the universal concept first
- then name the current local implementation as an example only

Good pattern:
- universal rule = `repo-vs-bulk-artifact-store`
- current workspace example = `/mnt/ace/data`

5. Local attestation must not become canonical authority
If you cite a local report/artifact that may not be on `main`:
- say explicitly that it is local attestation only
- add a negative guard stating the deliverable must NOT depend on that artifact as required canonical authority
- if the same rule should apply to a class of artifacts, target the class, not one dated filename

6. Bring new docs under existing guardrails
When a plan adds new standards/docs files, check whether there is already an existing stale-reference or banned-reference guard.
If yes, the plan should usually include updating that guard/test so the new docs are covered too.

## Recommended redraft procedure

1. Re-read the latest review artifacts and extract only the still-live blockers.
2. Patch the plan body so historical verdicts are clearly marked as historical/superseded.
3. Replace vague acceptance/tests with exact pass conditions.
4. Resolve any open-vs-required contradictions.
5. Convert workspace-specific paths into universal-rule-plus-local-example form when needed.
6. Add explicit negative-authority language for any local-only evidence source.
7. Extend existing stale-reference/banned-reference guards when introducing new docs.
8. Refresh the review prompt from the patched plan text before rerunning reviewers.

## Good patch patterns

### A. Historical review summary
Instead of:
- `Overall result: FAIL`

Use:
- `Historical review results for the immediately previous draft revision are recorded below for traceability.`
- `Current draft state: PENDING RE-REVIEW`

### B. Exact wording guard
Instead of:
- `daily cadence language present`

Use:
- requires exact phrase `daily freshness review`
- requires either `every 24 hours` or `once per day`
- requires named refresh obligation for a specific artifact
- requires follow-through issue in the same section

### C. Checklist schema guard
Instead of:
- `required status fields present`

Use:
- exact field names: `repo_name`, `operator_map_status`, `registry_status`, `data_placement_status`, `evidence_source`
- exact allowed values: `present | partial | missing | not-applicable`

## Pitfalls

- Do not rerun review using a stale prompt file after patching the plan.
- Do not keep piling new tests onto a plan while leaving the narrative contradictory.
- Do not hardcode one dated report filename if the intended rule is about a whole artifact class.
- Do not assume reviewers accept a requirement merely because it has its own test row.

## Outcome expectation

This pattern does not guarantee APPROVE on the next wave, but it reliably converts vague, repetitive MAJORs into narrower MINORs or one final precise blocker that can be fixed directly.
