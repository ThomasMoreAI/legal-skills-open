---
name: hipaa-assessor
title: HIPAA Assessor
description: Assess a target system against HIPAA Privacy Rule, Security Rule, and Breach Notification Rule using the hipaa-foundation repository, including entity-role triage, addressable-spec handling, domain selection, evidence mapping, and structured draft output.
author: nickzren
author_url: https://github.com/nickzren/hipaa-foundation/tree/main/skills/hipaa-assessor
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: healthcare
language: en
---

# HIPAA Assessor

Use this skill to produce conservative draft HIPAA assessments of software systems.

This skill is the workflow layer only. It is not the knowledge base itself. The canonical corpus stays in the `hipaa-foundation` repository under `core/`.

For fast navigation inside this skill package, start with `START-HERE.md` and `references/index.yaml`. They point back to canonical files under the resolved foundation repo. They do not replace them.

## Source hierarchy

- `FOUNDATION_ROOT/core/regulations/*.yaml` `authoritative_text` — binding regulatory text
- `FOUNDATION_ROOT/core/guidance/*.yaml` — OCR guidance and interpretive context
- `FOUNDATION_ROOT/core/domains/*.yaml` and checklist files — non-authoritative assessment guidance
- target-system evidence — determines the actual finding

## When to use

Use this skill when:

- the user asks to assess, review, or evaluate a system against HIPAA
- the `hipaa-foundation` repository is available directly or through a separate checkout

## Prerequisites

Before starting, you need:

- a target system to assess
- enough repo-local evidence to begin answering the triage questions
- a resolvable `hipaa-foundation` repository

If the target system or foundation root cannot be identified, stop and ask for the missing path. Otherwise inspect the target repo first and ask follow-up questions only if the assessment is still blocked.

## Locate the foundation repo

Resolve the foundation root before reading any `core/` files.

Resolution order (implemented in `scripts/resolve-foundation-root.sh`):

1. `HIPAA_FOUNDATION_ROOT` environment variable (fail closed if set but invalid)
2. Cross-tool config file: `${XDG_CONFIG_HOME:-$HOME/.config}/hipaa-assessor/config` (single line, absolute path)
3. Well-known path: `$HOME/github/hipaa-foundation`
4. Current working directory if it is the foundation repo
5. Sibling of the target repo root (walk up to `.git`, check sibling)
6. Sibling of cwd (fallback if not inside a git repo)

Run `scripts/resolve-foundation-root.sh` from this skill package. Once resolved, treat that absolute path as `FOUNDATION_ROOT` and read all referenced files from there.

## Workflow

Before triage, explore the target repo directly. Use code, docs, infrastructure config, tests, and any in-repo architecture or procedural material as assessment evidence.

Ask follow-up questions only when a required decision cannot be derived from the reviewed corpus and the assessment would otherwise be blocked.

### Step 0 -- Check content policy

Read:
- `FOUNDATION_ROOT/core/provenance/content-policy.yaml`
- `FOUNDATION_ROOT/core/provenance/decision-log.yaml`

Do not use the repo in a way that violates the content policy.

### Step 1 -- Entity-role triage

Read:
- `FOUNDATION_ROOT/core/applicability/triage.yaml`
- `FOUNDATION_ROOT/core/applicability/triage-output-template.yaml`

Entity type must be determined from evidence in the reviewed corpus: governance documents, BAAs, formal scope statements, or explicit entity classification records. Do not infer entity type from system function, clinical branding, device names, or health-data content. If the corpus does not confirm entity type, use `tbd` with `low` confidence.

When `entity_type` is `tbd` and ePHI is clearly in scope, the usual `applicable_rules` posture is `security_rule`, `breach_notification_rule`, and `enforcement_rule`. Do not add `privacy_rule` unless entity status is confirmed from the corpus. Always include `enforcement_rule` for context.

Before selecting domains, produce a structured triage block.

At minimum include:
- `entity_type` (`covered_entity`, `business_associate`, `ba_subcontractor`, `not_regulated`, `tbd`)
- `covered_entity_type` (`provider`, `health_plan`, `clearinghouse`, `not_applicable`, `tbd`)
- `hybrid_entity_status` (`yes`, `no`, `tbd`)
- `entity_type_confidence` (`low`, `medium`, `high`)
- `phi_types_in_scope`
- `phi_scope_confidence` (`low`, `medium`, `high`)
- `evidence_basis` (`repo-only`, `repo-plus-external-evidence`, `repo-plus-runtime-or-interviews`)
- `assessment_confidence` (`low`, `medium`, `high`)
- `applicable_rules`
- `part_162_assessment_mode` (`not_in_scope_v1`, `applicability_only`, `full_module`)
- `state_law_overlay_status` (`out_of_scope_v1`, `identified`, `tbd`)
- `in_scope_domains`
- `excluded_domains`
- `open_decisions`

After producing the triage block:
- Apply `domain_selection_rules` from `triage.yaml` to populate `in_scope_domains`.
- Read only the domain files listed in `in_scope_domains`. Skip excluded domains entirely.
- Retain `entity-and-applicability` in working context throughout the assessment. It governs downstream scope judgments.
- If `entity_type` is `tbd`, read `FOUNDATION_ROOT/docs/example-assessment-entity-tbd.md` for patterns on handling unconfirmed entity type, excluded Privacy domains, and evidence-basis limitations.
- If `entity_type` is `business_associate` or `ba_subcontractor`, read `FOUNDATION_ROOT/docs/example-assessment-ba.md` for BA-specific assessment patterns.
- If `entity_type` is `covered_entity`, read `FOUNDATION_ROOT/docs/example-assessment.md` for covered-entity assessment patterns.

If `entity_type` is `not_regulated`, state why and stop.

### Step 2 -- Select domains

Read:
- `FOUNDATION_ROOT/core/index/domain-inventory.yaml`

Select domains from the canonical inventory based on entity type, applicable rules, and PHI scope.

### Step 3 -- Explore evidence

Read:
- `FOUNDATION_ROOT/core/checklists/evidence-map.yaml`

Use the evidence map while exploring:
- code
- infrastructure
- docs
- external governance evidence

Evidence basis branching:
- If `evidence_basis` is `repo-only`, read the `repo_only_notes` in each in-scope domain file's `assessment_guidance` before scanning. These notes identify which controls are typically organizational and should not be rated `Gap` on repo-only evidence alone.
- If `evidence_basis` includes external evidence, also consult the `external` evidence expectations in each domain's regulation files.

### Step 4 -- Assess each domain

Read:
- `FOUNDATION_ROOT/core/checklists/assessment-rubric.yaml`

For each in-scope domain:
1. Read the domain file (`review_questions`, `deep_assessment_probes`, `assessment_guidance`).
2. Read the domain's `regulation_files/standards` for orientation.
3. Read the domain's `regulation_files/implementation_specifications` for detail on each standard's required and addressable specs.

Read all listed regulation files for the current domain before moving to the next domain. Do not front-load regulation files for all domains at once. Work domain by domain.

For every in-scope domain:
- compare expected evidence to reviewed evidence
- separate missing evidence from observed gaps
- for Security Rule addressable specs, capture the disposition: `implemented`, `alternative`, `documented_exception`, or `not_evidenced`
- a documented exception backed by a risk analysis is `Adequate`, not a gap
- keep conclusions proportional to the evidence basis

Addressable-spec handling:
- `required` + implemented -> `Adequate`
- `required` + not implemented -> `Gap`
- `addressable` + `implemented` -> `Adequate`
- `addressable` + `alternative` (documented) -> `Adequate`
- `addressable` + `documented_exception` (documented risk basis) -> `Adequate`
- `addressable` + `not_evidenced` -> `Partial` or `Not assessed` depending on evidence basis

Repo-only realism rule:
Many HIPAA obligations are organizational. On repo-only evidence, the following should typically be `Not assessed` or `Partial`, not `Gap`:
- notices of privacy practices
- authorizations
- accounting of disclosures
- sanctions policy execution evidence
- executed BAAs
- training completion records
- breach investigation and notification workflow execution evidence

Domain severity anchors:
- For systems with strong technical controls but weak governance, default to `Minor` or `Observation`
- Escalate only with explicit rationale
- State the escalation rationale if overriding the domain default

### Step 5 -- Produce the assessment

Use:
- `FOUNDATION_ROOT/docs/assessment-output-template.md`

Every output must:
- begin with the exact disclaimer as the very first content: `This is a draft assessment for human compliance review. It is not a compliance determination and not a substitute for legal counsel.`
- end with the same exact disclaimer as the very last content
- include the triage block before findings
- include a domain ratings summary table with an `addressable_disposition` column for Security Rule specs
- include a detailed finding section for every row that is not `Adequate` or `Not applicable`
- show `basis_type` for each non-trivial finding

If `part11-foundation` is also being used:
- keep the same factual evidence across both assessments
- let `part11-foundation` own Part 11 record/signature scope and control ratings
- let `hipaa-foundation` own HIPAA Privacy/Security/Breach findings
- do not force identical labels when the repos are answering different questions

If `gamp5-foundation` is also being used:
- let `gamp5-foundation` own lifecycle, validation, and supplier methodology
- HIPAA risk analysis and GAMP risk assessment are related but distinct

### Step 6 -- Self-review

Run:
- `FOUNDATION_ROOT/core/checklists/assessment-self-review.md`

If any check fails, go back and correct the assessment.

## Output rules

- never present repo interpretation as binding regulatory text
- never hide uncertainty in prose
- never treat addressable specs as gaps without documenting disposition
- never collapse missing evidence and actual control gaps into one vague finding
- never produce findings for Part 162 in v1
- always keep the assessment usable as a draft review artifact for human compliance reviewers

## When information is insufficient

If the available information is not enough to answer a triage question or assess a domain:

- do not guess
- use `Not assessed` or `Partial`, whichever the rubric supports
- state what information is needed
- continue on assessable domains
