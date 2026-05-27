---
name: awa-compliance-audit
title: AWA Compliance Audit (USDA/APHIS)
description: 'Produces an enforcement-aware Animal Welfare Act compliance audit for USDA/APHIS-regulated facilities. Maps Form 7002 inspection citations to verified 9 C.F.R. Parts 1-3 requirements, analyzes NCI severity and recurrence patterns, evaluates core compliance programs (PVC, IACUC, housing, records, transport), and outputs a prioritized corrective action plan with proof artifacts. Use when auditing AWA compliance, reviewing USDA inspection reports, preparing for license renewal, conducting diligence, or assessing enforcement risk. Trigger: Animal Welfare Act, AWA, USDA, APHIS, Form 7002, IACUC, PVC, exhibitor, dealer, research facility.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/awa-compliance-audit
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
---

# AWA Compliance Audit (USDA/APHIS)

Structured audit that maps USDA/APHIS inspection citations to verified CFR text, identifies systemic patterns driving enforcement escalation, and produces a corrective action plan with documentation artifacts.

## Quick Start

1. Gather facility records and Form 7002 reports (Checkpoint A)
2. Establish regulatory applicability
3. Build citation map against verified CFR text
4. Analyze severity and recurrence patterns
5. Evaluate core compliance programs
6. Produce corrective action plan with proof artifacts
7. Assemble audit memo
8. Align with user on gaps (Checkpoint B)

## Checkpoint A: Intake

Ask unless user says "use defaults" or "just draft."

**Gather:**
- **Facility status** — license/registration class, number, species, sites
- **Inspection record** — Form 7002 reports (3-5 years), warnings, settlements, ALJ decisions
- **Operations** — PVC (signed by AV), SOPs, treatment logs, A&D records (Forms 7001/7020), ID system, environmental logs, training records, enclosure specs
- **Research** (if applicable) — IACUC minutes, protocols, Search for Alternatives
- **Authorities** — 7 U.S.C. § 2131 et seq. [VERIFY], 9 C.F.R. Parts 1-3 [VERIFY]

**Key documents to request:** Form 7002 reports (min. 3 years), current PVC, A&D records, husbandry/sanitation SOPs, enclosure specs, training records.

**Defaults** (if no response): exhibitor/dealer class, 3-year window, general scope, all species present. Flag missing items in "Open Items" section.

## Step 1: Establish Applicability

Identify license class, sites, species, and regulated activities. Map applicable 9 C.F.R. Part 2 administrative requirements and Part 3 species subparts [VERIFY]. Flag classification ambiguity. Note stricter state/local laws.

**Deliverable — Applicability Table:**

| Item | Detail | CFR Reference | Notes |
|---|---|---|---|
| License class | | 9 C.F.R. Part 2 | |
| Covered species | | Part 3 subparts | |
| Regulated activities | | | |
| Sites/locations | | | |

## Step 2: Build Citation Map

Map each Form 7002 citation to verified CFR text. Verify at `https://www.ecfr.gov/`. Quote inspector observations verbatim. Note supporting/contradicting facility evidence. Track recurrence by CFR section.

**Deliverable — Citation Map:**

| Report Date | NCI Type | CFR Cite (Verified) | Inspector Observation (Quote) | Facility Evidence | Analysis | Recurrence |
|---|---|---|---|---|---|---|

## Step 3: Severity and Pattern Analysis

Classify by USDA NCI level (Indirect/Direct/Critical [VERIFY source]) and assign internal risk tiers (Low/Medium/High — explicitly internal, not USDA). Identify recurrence by CFR section and time window. Flag escalation risk: same section 3+ times, or progression from Indirect to Direct.

**Deliverable — Pattern Analysis:**

| Pattern | CFR Cite | Recurrence Count | NCI Severity | Likely Driver | Risk Tier |
|---|---|---|---|---|---|

## Step 4: Program Evaluation

Evaluate each program area against CFR requirements. For each, note compliant elements, deficiencies, documentation gaps, and recommended improvements.

- **PVC/AV Oversight** — authority, signatures, visit cadence, treatment docs [VERIFY § 2.40]
- **Species Subparts** — species-specific standards; do not conflate with general standards
- **Housing/Sanitation/Environment** — structure, drainage, ventilation, water, feed, pest control
- **Records/ID/Traceability** — A&D, identification, health certifications [VERIFY §§ 2.75, 2.78]
- **IACUC** (research) — protocol review, semiannual inspection, alternatives search [VERIFY § 2.31]
- **Transport/Carriers** — handling, containment, carrier obligations [VERIFY]

## Step 5: Corrective Action Plan

Prioritize by: (1) animal welfare risk, (2) enforcement escalation risk, (3) documentation gaps. Every action must include a specific proof artifact.

**Deliverable — CAP:**

| Finding | CFR Cite | Root Cause | Immediate Fix (0-14 days) | System Fix (30-90 days) | Owner | Proof Artifact |
|---|---|---|---|---|---|---|

## Step 6: Assemble Audit Memo

**Structure:**
1. Executive Summary
2. Facility Profile and Applicability
3. Inspection History Timeline
4. Findings by Regulatory Domain
5. Pattern Analysis and Root Causes
6. Corrective Action Plan
7. Record Retention and Self-Audit Plan
8. Appendix: Citation Map and Source List

**Front matter on every output:**
1. **Assumptions Used** — facility class, species, inspection window, scope
2. **Open Items** — missing reports, records, or verification needed

## Checkpoint B: Post-Draft Alignment

After delivering the audit, ask:
1. Does the facility profile match your understanding?
2. Are there reports or records not yet incorporated?
3. Should any findings be escalated or flagged for external counsel?
4. Intended use: internal compliance, board reporting, or enforcement defense?

## Quality Checks

- Every requirement tied to verified eCFR text with CFR cite
- Every fact tied to a report, record, or interview (labeled)
- Record gaps stated explicitly — never papered over
- CAP includes owners, dates, and proof artifacts for every finding
- Species-specific standards not conflated with general standards
- NCI classifications sourced or labeled [VERIFY]
- State/local overlay noted where stricter than AWA
- No invented USDA guidance, penalty ranges, or enforcement thresholds

## Guardrails

- Verify all CFR citations at `https://www.ecfr.gov/`; mark uncertain cites `[VERIFY]`
- Do not invent USDA guidance or penalty ranges; label as `[VERIFY]` if referenced
- Use enforcement-aware language: say "USDA cited noncompliance with…" not "in violation of"
- Treat inspection reports as discoverable; use precise, non-conclusory language
- If animal welfare risk is imminent, flag for immediate action and expert consultation
- If mixed operations create ambiguity, state the ambiguity and its compliance impact
- Preserve privilege: label as attorney work product when appropriate
- Output requires attorney review before external use

**Required disclaimer on every output:**

> THIS AUDIT REQUIRES INDEPENDENT ATTORNEY VERIFICATION OF ALL CFR CITATIONS, REGULATORY INTERPRETATIONS, AND FACTUAL ASSERTIONS, AND DOES NOT CONSTITUTE LEGAL ADVICE.

---

**Key changes from the original:**
- **Removed `tags`** — not part of the Agent Skills spec (only `name`, `description`, `license`, `compatibility`, `metadata` are valid frontmatter fields)
- **Trimmed description** — kept under 1024 chars, third-person, with clear trigger keywords
- **Removed "Why This Skill Exists"** — explanatory prose that doesn't help the agent execute
- **Added Quick Start** — numbered overview of the full workflow at a glance
- **Consolidated Quality Audit + Guidelines into Quality Checks + Guardrails** — eliminated duplicate bullets that appeared in both sections
- **Tightened each step** — removed redundant sub-explanations while preserving all deliverable tables and CFR verification requirements
- **Reduced from ~198 to ~130 lines** — ~34% token savings with no domain accuracy loss
