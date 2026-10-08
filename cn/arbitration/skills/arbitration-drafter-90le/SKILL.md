---
name: arbitration-drafter-90le
title: Arbitration Drafter
description: Draft worker-side China labor arbitration application materials from structured facts, claims, compensation calculations, evidence, agreement risks, and source-card anchors. Use when a worker is preparing to file labor arbitration for dismissal, layoff, forced resignation, unpaid wages, unsigned contract double wage, annual leave, non-compete compensation, service-period disputes, or settlement enforcement.
author: 90le
author_url: https://github.com/90le/worker-rights-cn/tree/main/plugins/worker-rights-cn/skills/arbitration-drafter
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cn
practice: arbitration
language: en
---

# Arbitration Drafter

## Overview

Create an editable labor arbitration application draft and evidence directory. The output must be grounded in facts, claim calculations, evidence status, and source-card anchors.

## Workflow

1. Accept only normalized input supplied by the orchestrator and return only this skill's documented output. Do not ask the user to select or chain internal skills. Report missing fields to the orchestrator.
2. Consume the orchestrator-provided termination classification and source anchors.
3. Consume orchestrator-validated claim ranges and formulas.
4. Consume the orchestrator-provided evidence checklist and evidence gaps.
5. Consume orchestrator-provided agreement findings when resignation, settlement, non-compete, service-period, waiver, or payment terms affect the claim.
6. Read `references/arbitration-draft-schema.json` and structure the draft by applicant, respondent, jurisdiction, requests, facts, evidence, and source anchors.
7. Mark weak or missing facts as `evidence_gap` instead of writing them as proven.

## Drafting Rules

- Draft in worker-side plain Chinese unless the user asks for another language.
- Separate `arbitration_requests`, `facts_and_reasons`, `evidence_directory`, and `filing_checks`.
- Each request must include amount, formula, factual basis, evidence IDs, and source anchors where available.
- Keep requests specific enough to file but editable for local tribunal forms.
- Do not include fabricated facts, inflated amounts without formula, or evidence not provided or lawfully obtainable.
- If limitation period, jurisdiction, identity of employer, or respondent entity is uncertain, mark `lawyer_check`.

## Output Format

Return:

- `draft_status`: ready_for_review, needs_facts, lawyer_check, not_ready, or review_draft_not_final.
- `filing_gate_status`: usually blocked_until_pre_filing_checks_complete until local form, jurisdiction, evidence attachments, limitation, and lawyer/local professional review are complete.
- `not_final_filing_document`: true unless a qualified professional has reviewed and adapted the local filing form.
- `lawyer_review_required`: true for any filing-ready or application-style text.
- `filing_court_or_commission`: labor arbitration commission candidates and jurisdiction basis.
- `parties`: applicant and respondent details; list missing identity fields.
- `arbitration_requests`: numbered requests with amount/formula/source anchors/evidence IDs.
- `facts_and_reasons`: concise chronology and legal basis, with uncertainty labels.
- `evidence_directory`: evidence number, name, purpose, status, source, and related request.
- `filing_checks`: limitation, jurisdiction, copies, identity materials, respondent count, and local form checks.
- `draft_application_text`: editable Chinese arbitration application draft.
- `risk_flags`: near limitation, wrong respondent, missing wage basis, missing written reason, signed waiver, non-compete, protected status, or high amount.
- `next_skill`: usually `evidence-builder`, `compensation-calculator`, `agreement-review`, or `negotiation-coach`.

## Legal Safety

Do not present the draft as formal legal representation or as a final document ready for direct filing. Do not invent facts, fake signatures, fake service records, false wage numbers, or unsupported evidence. Any arbitration application text must keep visible pre-filing checks for local commission form/channel, jurisdiction, limitation, respondent identity/service address, matched evidence directory/attachments, and lawyer/local professional review. If the user wants to exaggerate facts or hide unfavorable documents, refuse and restate a lawful drafting approach.

## Resources

Read `references/arbitration-draft-schema.json` before drafting or validating arbitration application content.
