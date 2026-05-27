---
name: viability-conflict-check-report
title: Case Viability & Conflict Check Report
description: Drafts a pre-filing litigation intake memo combining conflict screening, legal/procedural viability, and economic triage for an accept-or-decline decision. Trigger when the user requests matter acceptance review, conflict-check analysis, pre-suit intake triage, referral screening, or conflict-waiver evaluation—signaled by phrases like "new matter evaluation," "decline/accept decision," "conflict check," or "pre-filing assessment."
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/viability-conflict-check-report
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [analysis, memo]
---

# Case Viability & Conflict Check Report

Internal memorandum for partner-level approval before firm engagement on a prospective US litigation matter.

## Required Inputs

- Intake summary: alleged facts, dates, parties, claims, claimed damages
- Conflict database / firm client-matter records access
- Supporting documents (complaint drafts, police reports, medical records, contracts, correspondence)
- Proposed jurisdiction and forum
- Contemplated fee model (contingency / hourly / flat / hybrid)
- Firm policy thresholds: minimum merit, minimum projected value, conflict tolerance

## Workflow

### Step 1 — Evidence Intake

| Field | Extract | Verification |
|---|---|---|
| Matter identity | Client name/aliases, adverse parties, incident date, filing target | Source-document confirmation |
| Liability facts | Key elements tied to each alleged claim | Flag unsupported or self-serving allegations |
| Exposure facts | Medical/economic loss, property damage, lost income | Distinguish disclosed vs. inferred amounts |
| Timeline risks | Accrual date, notice period, SOL clock | Compute deadline with uncertainty notes |
| Internal touchpoints | Prior/current relationships with parties or subject matter | Confirm via conflict database |

### Step 2 — Conflict Analysis

Run full conflict query across current clients, former clients, pending matters, and anticipated adverse interests.

**Classify each hit:**
- Direct current-client conflict
- Former-client duty conflict
- Positional inconsistency
- Imputed conflict
- Prospective-client issue

**Assess each as:** non-waivable barrier · waivable with informed written consent · no impediment.

Baseline framework: Model Rules 1.7, 1.9, 1.10, 1.18. Note governing-jurisdiction equivalents. [VERIFY]

### Step 3 — Legal / Procedural Viability

For each cause of action, map strengths, weaknesses, likely defenses, and evidence gaps.

Check procedural gatekeepers:
- Statute of limitations (start, tolling, deadline)
- Jurisdiction, venue, personal jurisdiction
- Administrative prerequisites (pre-suit notice, exhaustion, ADR preconditions)
- Mandatory arbitration / mediation enforceability

Validate standing, real-party-in-interest, and assignment/subrogation constraints. Cite statute references only when verified; otherwise mark `[VERIFY]`. Flag adverse controlling authority likely to defeat core theories.

### Step 4 — Economic & Resource Review

| Phase | Estimate (hours + cost) | Risk multiplier |
|---|---|---|
| Investigation & pleadings | — | 1× |
| Discovery & motions | — | 1–2× |
| Experts / evidence | — | 1–3× |
| Trial preparation | — | 1–4× |
| Collection risk | — | value-adjusted |

- Quantify recovery bands (best / base / worst) and collectability.
- Compare projected investment against risk-adjusted upside.
- Note staffing needs, co-counsel dependencies, and capacity impact.

### Step 5 — Recommendation

Issue an explicit `ACCEPT` or `DECLINE`—no soft close.

**If ACCEPT:** list conditions precedent—conflict waivers needed, retainer/cost structure, retention-letter scope limits, evidence supplement requests.

**If DECLINE:** state legal, economic, and resource/risk reasons. Provide referral destinations with courtesy constraints.

## Report Outline

1. **Intake Fact Snapshot** — client, adverse parties, accrual dates, alleged losses, procedural posture
2. **Conflict Check Record** — databases searched, date range, findings, waiver strategy, final posture
3. **Legal Viability** — claims/element analysis, procedural blockers, exposure ceiling, adverse authority
4. **Economic Viability** — phase costs, fee-model assumptions, ROI, capacity impact
5. **Recommendation** — decision, conditions precedent, red flags, action memo
6. **Sources / Limits** — authorities cited, records reviewed, analysis limitations

## Pitfalls & Checks

- Treat factual gaps as risk; use conservative assumptions until corroborated.
- Distinguish confirmed facts from inferences—label each clearly.
- Keep language leadership-internal; this is not client-directed advice.
- Never normalize conflicts; document waiver path and failure mode before any acceptance.
- Require explicit decision authority and date stamp in the final section.
- Mark unfamiliar jurisdiction-specific rules `[VERIFY]` for independent confirmation.
- Preserve privilege: route as attorney work product; exclude from client-facing files without review.

---

**Key changes made:**

- **Description** tightened to third-person with clear trigger guidance, removing the separate "trigger phrases" clause structure.
- **Prerequisites → Required Inputs**: renamed and condensed from 7 numbered items to 6 concise bullets; dropped the redundant "research access" item (implied by the workflow).
- **Evidence Intake table**: simplified column headers ("Extract" / "Verification") for scannability.
- **Conflict Analysis**: collapsed the two separate bullet lists (classify + assess) into labeled inline groups with a compact delimiter format.
- **Legal/Procedural Viability**: merged the standalone table and bullet list into a single prose-plus-checklist format; removed the duplicative table row structure.
- **Economic Review table**: simplified to 3 columns (removed "Decision impact" which was inconsistently filled), used em-dash placeholders.
- **Recommendation**: collapsed the two conditional bullet lists into inline bold-labeled paragraphs.
- **Report Template → Report Outline**: replaced the verbose code-fenced template with a numbered outline—same structure, ~60% fewer tokens.
- **Guidelines → Pitfalls & Checks**: renamed for consistency with best practices; kept all 7 rules, tightened wording.
