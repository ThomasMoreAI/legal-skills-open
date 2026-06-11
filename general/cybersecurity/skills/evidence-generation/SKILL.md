---
name: evidence-generation
title: Enterprise Evidence Pack Generation
description: Use this skill when generating ISO 27001 or NIST SP 800-53 audit evidence packs, compliance reports, evidence narratives, reviewer-ready control matrices, or when the user asks about audit evidence, compliance evidence, evidence packages, audit documentation, or ISO/NIST evidence.
author: allsmog
author_url: https://github.com/allsmog/shinsa-plugin/tree/main/skills/evidence-generation
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: cybersecurity
language: en
---

# Enterprise Evidence Pack Generation

## Purpose

Transform Shinsa assessment artifacts into an enterprise-grade evidence pack for Security and GRC reviewers. The pack must be defensible, reviewable, exportable, and honest about uncertainty. It supports an audit or control review; it does not replace a human auditor.

## Inputs

Read persisted artifacts first:

- `assessment-plan.md`
- `scope.md`
- `applicability.json` and `applicability.md`
- `domains/*.json` and `domains/*.md`
- `reviews/round-*/*.json` and `reviews/round-*/*.md`
- `synthesis/evidence-index.json`
- `synthesis/control-matrix.json`
- `shinsa-state.json` when present

Do not rescan the repository during synthesis unless the orchestrator explicitly asks for a reconciliation pass. The evidence pack should explain what the persisted artifacts support.

## Required Report Sections

The canonical report is `shinsa-output/runs/<assessment_id>/synthesis/compliance-report.md`. It must include these top-level sections:

1. `## Assessment Metadata`
2. `## Executive Summary`
3. `## Control Matrix`
4. `## Findings`
5. `## Evidence Index`
6. `## Reviewer Notes`
7. `## Unresolved Risks`
8. `## Limitations`
9. `## What To Do Next`
10. `## Human Sign-Off`

Assessment metadata must include:

- timestamp placeholder or ISO-8601 timestamp
- plugin version
- target path
- target commit placeholder or commit hash
- assessment mode
- standards assessed
- scope exclusions
- methodology
- raw artifact references

## Per-Control Requirements

Every control row and narrative must include:

- control ID and title
- status
- confidence score
- `confidence_rationale`
- `evidence_quality`
- `evidence_quality_rationale`
- `manual_evidence_needed`
- `manual_evidence_items`
- `reviewer_disposition`
- remediation priority
- ticket-ready action
- `grc_action`: `accept`, `reject`, `request_evidence`, or `create_remediation_ticket`
- evidence anchors with file paths and line numbers where code/config evidence exists

Do not mark a control `implemented` if `manual_evidence_needed` is true. Use `partially_implemented`, `not_implemented`, or `not_assessed` until the missing manual evidence is supplied.

## Evidence Quality Rules

- `strong`: direct source/config evidence supports the claimed control outcome, findings have file and line anchors, and no manual evidence is required for the claimed status.
- `partial`: evidence supports part of the control, but implementation gaps, reviewer concerns, or manual evidence needs remain.
- `inferred`: the claim depends on framework convention, absence of contrary evidence, or indirect evidence.
- `missing`: no reliable evidence was found.

Never use `strong` for a hybrid control when manual policy, approval, access review, incident, supplier, training, or production records are needed for full compliance.

## Manual Evidence Taxonomy

Use specific manual evidence items. Avoid vague text like "policy evidence needed".

Common manual evidence categories:

- policies and standards
- access reviews and privileged access approvals
- training records
- incident tickets and post-incident reviews
- vulnerability scan exports and remediation tickets
- supplier due diligence and contract clauses
- production configuration exports
- SIEM/log-retention evidence
- change approvals and release records
- risk acceptances and exceptions

## Tone And Uncertainty

Use factual, audit-support language:

- Prefer "evidence indicates", "the repository shows", and "the artifacts support".
- Avoid absolute claims such as "compliant" unless all required evidence is present.
- Separate code/config evidence from manual/process evidence.
- State limitations plainly.
- Keep GRC next actions operational: accept, reject, request named evidence, or open a remediation ticket.

## Reviewer Propagation

Reviewer concerns must not be buried. If any reviewer status is `changes_requested` or `unresolved`:

- mark affected control rows with the reviewer disposition
- include the concern in `## Reviewer Notes`
- include unresolved items in `## Unresolved Risks`
- make the `grc_action` reflect the unresolved state

## Good Evidence

Good evidence is anchored, scoped, and explains why it matters:

```markdown
`src/routes/auth.ts:7` shows the login handler executes password verification without rate limiting middleware. This supports a high-severity A.8.5 gap because repeated failed login attempts are not throttled in the assessed source.
```

Bad evidence is vague or unsupported:

```markdown
Authentication looks secure because the app uses a common framework.
```

## Gold-Standard Control Example

```markdown
| Control | Status | Confidence | Evidence Quality | Manual Evidence | Reviewer | GRC Action |
| --- | --- | --- | --- | --- | --- | --- |
| A.8.5 Secure Authentication | partially_implemented | 0.86 | partial | yes | approved | create_remediation_ticket |

Confidence rationale: Password hashing and session cookie evidence were present in source, but lockout, MFA policy, and access review records were not available.

Evidence quality rationale: The source anchors directly support bcrypt password verification and show missing rate limiting. The control remains partial because manual identity governance evidence is required.

Manual evidence items:
- Production MFA policy
- Access review records for privileged accounts
- Login lockout configuration export

Ticket-ready action: Add login throttling and collect production MFA/access-review evidence before claiming full implementation.
```

## Final Checklist

- [ ] All required sections are present.
- [ ] Assessment metadata names the target, mode, standards, scope exclusions, and raw artifacts.
- [ ] Every control has all enterprise trust fields.
- [ ] Every finding has file and line evidence.
- [ ] Manual evidence gaps are explicit and actionable.
- [ ] Reviewer unresolved items appear in Reviewer Notes, Unresolved Risks, and affected control rows.
- [ ] Human sign-off states Shinsa is assessment support, not auditor replacement.
