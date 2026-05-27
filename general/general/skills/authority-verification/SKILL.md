---
name: authority-verification
title: Authority Verification with case.dev
description: Verifies legal citations and retrieves source material using the case.dev Legal Research API and CLI. Use when validating a citation, confirming a case exists, pulling source text, finding related authorities, extracting citations from a brief or opinion, or building a filing-ready authority check without branded citator terminology.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/authority-verification
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Authority Verification with case.dev

Use case.dev legal research endpoints to verify citations, retrieve source text, and expand to related authorities. Keep the language generic: "verified citation," "candidate authority," "related authority," and "manual treatment review."

## Quick Start

1. Verify the citation text with `legal.verify()` before citing it.
2. If verification is unclear, search by topic with `legal.find()` or `legal.research()`.
3. Pull the full document text with `legal.fullText()` once you have a verified source URL.
4. Expand outward with `legal.similar()` to find related authorities.
5. Format the result using [references/OUTPUT-TEMPLATE.md](references/OUTPUT-TEMPLATE.md).

Reference guide: [references/CASEDEV-WORKFLOW.md](references/CASEDEV-WORKFLOW.md)

Runtime and setup: [references/RUNTIME.md](references/RUNTIME.md)

Concrete scenarios: [references/EXAMPLES.md](references/EXAMPLES.md)

Lightweight eval set: [references/EVALS.md](references/EVALS.md)

Examples:

- Python: [scripts/verify_authority.py](scripts/verify_authority.py)
- TypeScript: [scripts/verify_authority.ts](scripts/verify_authority.ts)
- CLI: [scripts/verify_authority.sh](scripts/verify_authority.sh)

## Core Workflow

### 1. Verify the citation

Use `legal.verify()` with the citation text exactly as written.

- `verified` means the citation matched a real source in the database.
- `not_found` means likely typo, hallucination, or unsupported citation.
- `multiple_matches` means manual review is required before citation.

### 2. Retrieve the source text

If verification succeeds, use the returned case URL with `legal.fullText()` to inspect the opinion and optionally highlight the issue you care about.

### 3. Expand the authority set

Use `legal.similar()` on the verified source URL to find related authorities.

Use `legal.research()` when you need broader issue-based research with multiple phrasings of the same question.

### 4. Audit a document

If you are checking a brief, opinion, or article URL, use `legal.citationsFromUrl()` to extract cited authorities, then verify important citations individually.

### 5. Record the result

Always record:

- the exact citation checked
- verification status
- authoritative URL
- jurisdiction used for search
- date checked
- any manual review needed before filing

## Guardrails

- Do not say a case was "Shepardized," "KeyCited," or given a proprietary signal.
- Do not describe case.dev results as editorial treatment analysis unless you performed separate manual review.
- Say "verified citation" instead of "good law."
- Say "manual treatment review required" when the workflow does not establish precedential weight by itself.
- Search results are candidates, not filing-ready authorities, until verified.
- Re-run verification immediately before filing.

## Output Standard

Format the final work product using [references/OUTPUT-TEMPLATE.md](references/OUTPUT-TEMPLATE.md).

## Dependencies

Do not assume tools are installed. Check [references/RUNTIME.md](references/RUNTIME.md) before running any script.

## Pitfalls

- Verifying only the case name and not the reporter citation.
- Treating `legal.find()` results as verified authorities.
- Assuming related cases from `legal.similar()` are citing references or direct history.
- Skipping the full-text read after verification.
- Hiding uncertainty when the result is `multiple_matches` or `not_found`.
