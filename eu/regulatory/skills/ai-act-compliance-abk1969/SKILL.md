---
name: ai-act-compliance-abk1969
title: AI Act Compliance — EU Regulation 2024/1689
description: Use when the user asks about EU AI Act (Regulation 2024/1689) compliance — classifying an AI system's risk tier (art. 5 prohibited / art. 6 + Annex III high-risk / art. 50 limited / minimal), evaluating conformity for high-risk AI (art. 8–17, 26–27), drafting Annex IV technical documentation, conducting a Fundamental Rights Impact Assessment (art. 27), checking AI literacy obligations (art. 4), detecting substantial modification (art. 25), planning regulatory sandboxes or real-world testing (art. 57, 60), GPAI obligations (art. 51–55), responding to a serious incident (art. 73), the 2026 AI Omnibus amendment (deferred high-risk deadlines, new NCII/CSAM prohibition), or mapping obligations to ISO/IEC 42001:2023 (AIMS) and ISO/IEC 27090 (AI cybersecurity). Do NOT use for GDPR-only questions (separate regime), generic ISO/IEC 27001 ISMS work, or non-EU AI regulations (NIST AI RMF for US).
author: abk1969
author_url: https://github.com/abk1969/ai-act-skills/tree/main/skills/ai-act-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
sources:
- title: 01 Risk Classification
  path: references/01-risk-classification.md
- title: 02 High Risk Obligations
  path: references/02-high-risk-obligations.md
- title: 03 Iso 42001 Aims
  path: references/03-iso-42001-aims.md
- title: 04 Iso 27090 Ai Security
  path: references/04-iso-27090-ai-security.md
- title: 05 Crosswalk Aiact Iso
  path: references/05-crosswalk-aiact-iso.md
- title: 06 Techdoc Annex Iv
  path: references/06-techdoc-annex-iv.md
- title: 07 Fria Art27
  path: references/07-fria-art27.md
- title: 08 Transparency Art50
  path: references/08-transparency-art50.md
- title: 09 Post Market Art72 73
  path: references/09-post-market-art72-73.md
- title: 10 Gpai And Timeline
  path: references/10-gpai-and-timeline.md
- title: 11 Art4 Ai Literacy
  path: references/11-art4-ai-literacy.md
- title: 12 Art25 Substantial Modification
  path: references/12-art25-substantial-modification.md
- title: 13 Sandboxes And Real World Testing
  path: references/13-sandboxes-and-real-world-testing.md
- title: 14 Codes And Right To Explanation
  path: references/14-codes-and-right-to-explanation.md
- title: 15 Platform Compatibility
  path: references/15-platform-compatibility.md
---

# AI Act Compliance — EU Regulation 2024/1689

## What this skill does

Codifies actionable EU AI Act compliance expertise. Every output is **traceable** to one or more of:

1. **Regulation (EU) 2024/1689** — *the AI Act* — the legally binding source.
2. **ISO/IEC 42001:2023** — Artificial Intelligence Management System (AIMS), the certifiable management standard for AI providers and deployers.
3. **ISO/IEC 27090:2025** — Cybersecurity guidance for AI systems (the depth standard for AI Act art. 15 cybersecurity).
4. **Companion ISO standards**: 23894 (AI risk management), 23053 (ML framework), 5338 (AI lifecycle), 5259-* (data quality), 24029-2 (robustness), 42005 (impact assessment), 42006 (audit & certification).
5. **CEN-CENELEC JTC 21** harmonised standards (under standardization mandate M/593) — the path to art. 40 presumption of conformity.
6. **GPAI Code of Practice** — published 2025-07-10; assessed adequate by the Commission and AI Board on 2025-08-01 — the operative instrument for arts. 53–55 until harmonised standards land.
7. **AI Omnibus amendment** (Digital Omnibus on AI) — adopted by Parliament (2026-06-16) and Council (2026-06-29); amends the AI Act's timeline and art. 5 prohibitions. See the timeline below.

This skill is **decision-support**, not legal advice. Always recommend the user consult qualified counsel for binding interpretation, and a notified body for conformity assessment of high-risk AI systems.

## Scheduling at a glance — SSL machine view

This skill is paired with a machine-readable manifest at [`ssl.json`](./ssl.json), built per the **Scheduling-Structural-Logical (SSL)** representation introduced by Liang et al., *From Skill Text to Skill Structure* (arXiv:2604.24026, 2026). The manifest exposes the skill's invocation interface, scene graph, and atomic action evidence so registries, routers, and reviewers do not need to re-parse this document. The table below is the human-readable scheduling view; `ssl.json` is the authoritative typed version.

| Field | Value |
|---|---|
| `skill_id` | `SKILL_AI_ACT_COMPLIANCE` |
| `skill_goal` | Produce traceable EU AI Act compliance guidance — risk classification, obligation mapping, ISO 42001 / 27090 anchoring, deliverable identification — for a named AI system and a named role (provider / deployer / importer / distributor / authorised rep). |
| `top_pattern` | `ROUTE_AND_ANCHOR` (route the question to the relevant reference; anchor every obligation to article + clause + Annex A control). |
| `tags` | `eu-ai-act`, `regulation-2024-1689`, `iso-42001`, `iso-27090`, `aims`, `gpai`, `fria`, `annex-iii`, `annex-iv`, `art-5`, `art-50`, `art-73`, `ai-omnibus`, `compliance`, `governance`, `decision-support` |
| `intent_signature` (samples) | "Is this AI system high-risk?", "What ISO 42001 control covers art. 9?", "Do I need a FRIA?", "How do I report a serious AI incident?", "Does art. 4 AI literacy apply to my org?", "Is fine-tuning a foundation model substantial modification?", "When does the GPAI systemic-risk regime kick in?", "Can I run my AI in an EU regulatory sandbox?", "Did the AI Omnibus change my compliance deadline?" |
| `expected_inputs` | `system_description: str`, `role: enum{provider, deployer, importer, distributor, authorised_rep}`, `sector: str`, `end_users: str`, `is_gpai: bool`, `compute_flops?: float`, `is_substantially_modified?: bool`, `incident_summary?: str` (RECOVER scene only) |
| `expected_outputs` | `tier: enum{unacceptable, high, limited, minimal}`, `pathway: enum{annex_i, annex_iii, art_50, none}`, `obligations_list: list[citation]`, `iso_anchors: list[control]`, `deliverables: list[artifact]`, `effective_date: date`, `legal_disclaimer: str` |
| `dependencies` | `permission: filesystem.read` (reference files); `capability: legal_decision_support`; **no** network or credentials access; **no** code execution. |
| `control_flow_features` | branching: yes (tier × role × system_kind matrix); loops: no; tool calls: no; touches sensitive resources: no |
| `entry_scene_id` | `S_PREPARE_SCOPE` |
| `subscenes` | `S_PREPARE_SCOPE`, `S_ACQUIRE_FACTS`, `S_REASON_TIER`, `S_ACT_OBLIGATIONS`, `S_VERIFY_ARTIFACTS`, `S_RECOVER_INCIDENT`, `S_FINALIZE_REPORT` |

## When to invoke this skill

Invoke when the user mentions or implies any of:

- **Risk classification**: "Is this AI system high-risk?", "minimal vs limited risk", "Annex III", "art. 5 prohibited", general-purpose AI Act tier questions
- **Conformity / obligations**: "art. 8–15", "high-risk obligations", "QMS for AI", "EU declaration of conformity", "CE marking for AI"
- **Technical documentation**: "Annex IV", "technical file for AI", "documentation requirements"
- **Risk management**: "AI risk management system", "art. 9", "risk register for AI", "ISO 23894"
- **Data governance**: "art. 10", "training data quality", "bias mitigation", "ISO 5259"
- **Transparency**: "art. 13", "art. 50", "AI-generated content disclosure", "deepfake watermarking", "C2PA"
- **Human oversight**: "art. 14", "human-in-the-loop", "human-on-the-loop"
- **Cybersecurity for AI**: "art. 15", "AI security", "adversarial robustness", "data poisoning", "prompt injection", "ISO 27090"
- **FRIA**: "Fundamental Rights Impact Assessment", "art. 27", "ISO 42005"
- **AI literacy**: "art. 4", "AI literacy programme", "staff training for AI"
- **Substantial modification**: "art. 25", "fine-tuning a foundation model", "provider-flip", "intended-purpose change"
- **Sandboxes & real-world testing**: "art. 57 sandbox", "art. 60 real-world testing", "AI Office sandbox", "Member State sandbox"
- **Right to explanation**: "art. 86", "individual decision explanation"
- **Post-market**: "art. 72", "post-market monitoring of AI", "AI incident reporting", "art. 73"
- **GPAI**: "art. 51", "art. 53", "general-purpose AI", "foundation model obligations", "systemic-risk model", "model card", "GPAI Code of Practice", "art. 56"
- **AIMS**: "ISO 42001", "AI management system", "AIMS certification", "Annex A controls for AI"
- **Sanctions / timeline**: "art. 99", "AI Act fines", "AI Act effective date", "2026-08-02", "2027-12-02", "2028-08-02"
- **AI Omnibus**: "Digital Omnibus", "AI Act delay", "high-risk deadline postponed", "NCII prohibition", "CSAM prohibition", "AI Act amendment 2026"

## Core taxonomy (memorize this)

### Four-tier risk model (art. 5/6 + Annex III + art. 50)

| Tier | Trigger | Regime | Article |
|------|---------|--------|---------|
| **Unacceptable** | Subliminal techniques, social scoring, untargeted facial scraping, biometric categorisation by sensitive attributes, real-time public biometric ID by law enforcement (with narrow exceptions), emotion recognition in workplace/education, exploitation of vulnerabilities, predictive policing of natural persons; **+ AI generating non-consensual intimate imagery (NCII) or CSAM** (added by the 2026 AI Omnibus, applicable **2026-12-02**) | **Banned** (effective 2025-02-02; NCII/CSAM prohibition from 2026-12-02) | Art. 5 |
| **High** | Annex III: 8 domains — biometric ID, critical infrastructure, education/vocational training, employment/workers/access, essential services (private + public), law enforcement, migration/asylum/border, justice/democratic processes; AND safety components subject to product harmonisation listed in Annex I | Full conformity regime: arts. 8–15 (provider) + arts. 16–17 (provider) + arts. 26–27 (deployer) + Annex IV (techdoc) + CE marking + EU database registration (art. 49) | Art. 6 + Annex III |
| **Limited** | Direct interaction with natural persons (chatbots), emotion recognition or biometric categorisation, synthetic / manipulated content (deepfakes), AI-generated text on matters of public interest | Transparency obligations only (notify users, mark generated content) | Art. 50 |
| **Minimal** | Everything else | Voluntary codes of conduct (art. 95) | — |

**General-Purpose AI (GPAI)** is a separate axis: arts. 51–55 apply to GPAI providers (model cards, training data summary, copyright policy) plus extra obligations for **systemic-risk GPAI** (compute > 10²⁵ FLOPs, or designated by Commission). The **GPAI Code of Practice** (art. 56) — published **2025-07-10** with three chapters (Transparency, Copyright, Safety & Security) and assessed adequate by the Commission and AI Board on **2025-08-01** — is the operative compliance instrument. GPAI obligations apply since **2025-08-02**; Commission enforcement powers (art. 101 fines) from **2026-08-02**.

### Universal obligations (apply regardless of tier)

| Obligation | Article | Effective | Scope |
|---|---|---|---|
| **AI literacy** | art. 4 | **2025-02-02** | All providers AND deployers — measures to ensure sufficient AI literacy of staff and other persons dealing with the operation/use of AI systems on their behalf. _(Digital Omnibus amends this to “shall take measures to support the development of AI literacy” — obligation of means, no guaranteed level; adopted 2026, awaiting OJ — see references/11 §1.1.)_ |
| **Voluntary codes** | art. 95 | 2026-08-02 | Encouraged for non-high-risk; can extend high-risk obligations voluntarily |

### Provider vs Deployer (art. 3 definitions)

- **Provider** (art. 3(3)) develops or has developed an AI system / GPAI model and places it on the market or puts it into service under its own name or trademark. Carries the bulk of the regulatory load (arts. 8–22, 49–52).
- **Deployer** (art. 3(4)) uses an AI system under its authority (except personal non-professional use). Carries arts. 26 (use obligations) and 27 (FRIA for selected high-risk uses).
- Importer (art. 3(6)), Distributor (art. 3(7)), Authorised representative (art. 3(5)) — derived obligations in arts. 22–24.
- **Substantial modification** (art. 25) flips the deployer to provider — see `references/12-art25-substantial-modification.md`.

### Sanctions tiers (art. 99)

| Tier | Cap | Applies to |
|------|-----|------------|
| **1** | **€35M or 7% global turnover** (whichever higher) | Art. 5 prohibited practices |
| **2** | **€15M or 3%** | Most other provisions (arts. 8–17, 26–29, 50, 53–55, etc.) |
| **3** | **€7.5M or 1.5%** | Supplying incorrect / incomplete / misleading info to authorities or notified bodies |

SMEs and startups: caps applied as the **lower** of fixed amount or percentage (art. 99(6)).

### Application timeline (art. 113, as amended by the 2026 AI Omnibus)

> **AI Omnibus status (as of 2026-07-14)**: political agreement 2026-05-07; European Parliament endorsement 2026-06-16; Council final approval 2026-06-29. OJ publication expected July 2026; the amendment enters into force on the third day after publication. Until publication, the original art. 113 dates remain the formal legal baseline — **verify the OJEU before relying on the deferred dates**. The Omnibus replaced the Commission's proposed conditional (standards-linked) trigger with **fixed dates**.

| Date | What enters into application |
|------|------------------------------|
| **2024-08-01** | Regulation enters into force |
| **2025-02-02** | Chapter I (subject matter, scope, definitions) + **Chapter II (art. 5 prohibitions)** + **art. 4 AI literacy** |
| **2025-08-02** | Chapter III Section 4 (notifying authorities & notified bodies) + Chapter V (GPAI) + Chapter VII (governance) + Chapter XII (penalties, except art. 101 GPAI penalties) + art. 78 confidentiality |
| **2026-08-02** | **Art. 50 transparency** + art. 95 codes + remaining non-high-risk provisions + **Commission GPAI enforcement powers (art. 101 fines)**. High-risk obligations do NOT start here — deferred by the Omnibus (below) |
| **2026-12-02** | **New art. 5 prohibition** (NCII/CSAM generation, added by Omnibus) applicable; end of art. 50(2) machine-readable-marking grace period for generative systems already on market before 2026-08-02 |
| **2027-08-02** | Member State **regulatory sandboxes** operational (art. 57, deferred by Omnibus from 2026-08-02); GPAI models placed on market before 2025-08-02 must comply with arts. 53–55 (art. 111) |
| **2027-12-02** | **High-risk obligations for stand-alone Annex III systems** (deferred by Omnibus from 2026-08-02) — arts. 8–17, 26–27, conformity assessment, CE marking, registration |
| **2028-08-02** | High-risk obligations for AI under **Annex I** regulated products (machinery largely carved out by Omnibus; medical devices, automotive, etc.) — deferred by Omnibus from 2027-08-02 |

## Decision tree — where to route

```
User question category                              → Reference file
─────────────────────────────────────────────────────────────────────
"What risk tier? Is this prohibited? Is this        → references/01-risk-classification.md
 high-risk? When does art. 50 apply?"

"What obligations apply once classified high-risk?" → references/02-high-risk-obligations.md
"art. 8–15", "art. 16–22", "art. 26–29"

"How does AI Act map to ISO 42001? AIMS clauses,    → references/03-iso-42001-aims.md
 Annex A controls, certification scope"

"AI cybersecurity, art. 15 cyber, adversarial,      → references/04-iso-27090-ai-security.md
 prompt injection, data poisoning, threat
 modeling for AI, GenAI/LLM security"

"Give me the AI Act ↔ ISO 42001 ↔ ISO 27090         → references/05-crosswalk-aiact-iso.md
 mapping table"

"Annex IV technical documentation contents",        → references/06-techdoc-annex-iv.md
"art. 11 + Annex IV"

"FRIA, art. 27, fundamental rights impact",         → references/07-fria-art27.md
"AI system impact assessment per ISO 42005"

"art. 50 transparency, deepfakes, marking           → references/08-transparency-art50.md
 AI-generated content, C2PA, watermarking"

"art. 72 post-market monitoring, art. 73 serious    → references/09-post-market-art72-73.md
 incident reporting, drift detection"

"GPAI, art. 51–55, foundation models, model         → references/10-gpai-and-timeline.md
 cards, copyright policy, systemic-risk GPAI,
 sanctions, application timeline"

"art. 4 AI literacy, staff training requirement"    → references/11-art4-ai-literacy.md

"art. 25 substantial modification,                   → references/12-art25-substantial-modification.md
 provider/deployer role flip"

"art. 57 regulatory sandbox, art. 60 real-world      → references/13-sandboxes-and-real-world-testing.md
 testing outside sandbox"

"art. 56 GPAI Code of Practice, art. 95 voluntary    → references/14-codes-and-right-to-explanation.md
 codes of conduct, art. 86 right to explanation"

"How does this skill run on Gemini CLI / OpenAI       → references/15-platform-compatibility.md
 Codex? Install paths, activation, tool mapping"
```

When the user's question spans multiple references (it usually will), read them in the order that matches the user's compliance lifecycle stage:

1. Classification → 2. Obligations → 5. Crosswalk → 3. AIMS → 4. Security → 6. TechDoc → 7. FRIA → 8. Transparency → 9. Post-market → 10. GPAI/timeline → 11. AI literacy → 12. Substantial modification → 13. Sandboxes/real-world testing → 14. Codes & right to explanation → 15. Platform compatibility (when the user asks about runtime / install).

## Platform compatibility

This skill is **runtime-agnostic** by design. The regulatory content
(SKILL.md + 15 references + ssl.json) is identical across hosts —
only discovery and activation differ.

| Runtime | Status | Discovery file | Install path |
|---|---|---|---|
| **Claude Code** | ✅ first-class | `SKILL.md` frontmatter | `~/.claude/skills/ai-act-compliance/` |
| **Gemini CLI** | ✅ supported | `GEMINI.md` (root + skill) | `~/.gemini/skills/ai-act-compliance/` |
| **OpenAI Codex** | ✅ supported | `AGENTS.md` (root + skill) | `~/.agents/skills/ai-act-compliance/` |
| Copilot CLI / Cursor | 🟡 community | `AGENTS.md` | varies |

Why portability is trivial here: `ssl.json` declares
`control_flow_features.tool_calls: false` and
`touches_sensitive_resources: false`. The skill instructs the host model
to **read its own reference files** and **emit citation-grade text** —
both universal across LLM runtimes. No tool-name translation table is
needed.

Full per-platform install steps, activation contract, and smoke-test
procedure: see `references/15-platform-compatibility.md`.

## Workflow — SSL scene structure

The workflow is realized as **seven typed scenes** matching the SSL Structural Layer vocabulary (`PREPARE`, `ACQUIRE`, `REASON`, `ACT`, `VERIFY`, `RECOVER`, `FINALIZE`). Entry: `S_PREPARE_SCOPE`. The full graph (transitions, terminal targets `END_SUCCESS` / `END_FAIL`, contained logic steps) is defined in [`ssl.json`](./ssl.json).

### S_PREPARE_SCOPE (PREPARE)

**Goal**: Establish the regulatory subject. Determine three facts before any classification.

1. **Role** (art. 3): Provider / Deployer / Importer / Distributor / Authorised Rep. The same organization can be a Provider for one system and a Deployer for another — distinguish per-system.
2. **System kind**: AI system (art. 3(1)) and/or GPAI model (art. 3(63)). Both regimes can apply.
3. **Substantial-modification trigger** (art. 25): if the user is fine-tuning, retraining, or repurposing a third-party system, the deployer→provider flip may apply. Route to `references/12-art25-substantial-modification.md`.

**Exit**: `$role`, `$system_kind`, `$modification_flag` set. → `S_ACQUIRE_FACTS`.
**Yield_fail conditions**: user cannot articulate role/system → ask 1 targeted question, otherwise `END_FAIL` ("classification cannot proceed without role + system").

### S_ACQUIRE_FACTS (ACQUIRE)

**Goal**: Gather the 14 classification signals.

Read `references/01-risk-classification.md` § 2 (the 14-signal questionnaire). If signals are missing, ask the user 2–3 targeted questions covering: sector, end-users, decision consequences, sensitive data, autonomy/oversight, geographical scope.

**Exit**: 14 signals populated (or marked unknown with explicit caveat). → `S_REASON_TIER`.

### S_REASON_TIER (REASON)

**Goal**: Apply the four-tier rubric + GPAI axis.

1. Compare signals against **art. 5** prohibitions (8 categories) — if match without carve-out → `tier = unacceptable`, terminate scene chain at `END_SUCCESS` with refusal output.
2. Compare against **art. 6(1)** Annex I trigger — if match → `tier = high`, `pathway = annex_i`.
3. Compare against **art. 6(2)** Annex III §1–§8 — if match, evaluate **art. 6(3) derogation** (a/b/c/d) — disabled if profiling natural persons (GDPR art. 4(4)).
4. Compare against **art. 50** transparency triggers (chatbot, generative output, emotion/biometric categorisation, deepfake, AI-public-interest text).
5. Independently evaluate **GPAI** presence + systemic-risk threshold (cumulative compute > 10²⁵ FLOPs or Commission designation).

**Exit**: `$tier`, `$pathway`, `$art6_3_derogation`, `$art50_triggers`, `$gpai_regime` set. → `S_ACT_OBLIGATIONS`.
**Yield_fail**: tier indeterminate due to ambiguous facts → output partial classification with explicit `KEY UNCERTAINTIES`.

### S_ACT_OBLIGATIONS (ACT)

**Goal**: Generate the obligation list and anchor each to ISO controls.

Apply this matrix:

- **Unacceptable** → "Cannot be marketed or put into service in the EU. If shipped: art. 5 violation = tier-1 sanction (€35M / 7%)." Terminate.
- **High-risk + Provider** → arts. 8 (compliance), 9 (RMS), 10 (data), 11 + Annex IV (techdoc), 12 (logs), 13 (transparency to deployer), 14 (human oversight), 15 (accuracy/robustness/cyber), 16 (provider obligations general), 17 (QMS), 43 (conformity assessment), 47 (declaration of conformity), 48 (CE marking), 49 (registration). → `references/02-high-risk-obligations.md`.
- **High-risk + Deployer** → art. 26 (use according to instructions, monitor, maintain logs, inform persons), art. 27 (FRIA for public bodies + private deployers in essential services). → `references/07-fria-art27.md`.
- **Limited risk** → art. 50 transparency only. → `references/08-transparency-art50.md`.
- **Minimal risk** → No mandatory obligations. Suggest voluntary codes (art. 95) → `references/14-codes-and-right-to-explanation.md`.
- **GPAI** → arts. 53 (provider obligations), 54 (auth rep), 55 (systemic risk obligations if applicable), 56 (Code of Practice). → `references/10-gpai-and-timeline.md`.
- **Universal (any tier)** → art. 4 AI literacy → `references/11-art4-ai-literacy.md`.

For each obligation, surface the **ISO control(s) that operationalize it**. Example output format:

> **AI Act art. 9 (Risk Management System)** → ISO/IEC 42001 cl. 6.1.2, 6.1.3, 8.2, 8.3 + Annex A.2.2, A.6.1.2 + ISO/IEC 23894:2023 (the depth standard).

This is non-negotiable. Always cite the **clause number** (cl. X.Y) and **control number** (A.x.y) precisely. The full mapping table lives in `references/05-crosswalk-aiact-iso.md`.

**Exit**: `$obligations_list`, `$iso_anchors`, `$deliverables` set. → `S_VERIFY_ARTIFACTS`.

### S_VERIFY_ARTIFACTS (VERIFY)

**Goal**: Compliance gate — validate that every obligation has been linked to a deliverable and citation.

Run these checks before producing the final report:

- [ ] Every obligation cites article + paragraph (e.g., `art. 9(2)(a)` not "the risk part").
- [ ] Every obligation cites a primary ISO 42001 clause + Annex A control.
- [ ] Where ISO 27090 is applicable (art. 15(5), Recital 76), the relevant section is named.
- [ ] Each obligation has at least one named **deliverable** (risk register, datasheet, Annex IV file, IFU, oversight spec, ...).
- [ ] **Substantial modification** check: if the user is downstream of a third-party system, the art. 25 flip is surfaced.
- [ ] **Presumption-of-conformity ladder** (per `05-crosswalk-aiact-iso.md` § 7) is positioned: harmonised standard cited in OJEU > common specs > 42001 certification > standard alignment.
- [ ] Deadline (`effective_date`) is explicit and matches art. 113 timeline.

**Exit**: all checks pass → `S_FINALIZE_REPORT`. Any check fails → `YIELD_FAIL` with a remediation note ("missing ISO anchor for art. X — re-enter S_ACT_OBLIGATIONS").

### S_RECOVER_INCIDENT (RECOVER) — parallel scene

**Triggered when**: the user reports a serious incident as defined in art. 3(49) (death, serious harm to health, serious and irreversible disruption of critical infra, breach of EU law on fundamental rights, serious harm to property/environment).

**Goal**: Drive the **15-day** (art. 73(2)) — or **2-day** if widespread infringement, **10-day** if death — incident-reporting timeline. Read `references/09-post-market-art72-73.md`.

Output an incident-report skeleton with: system identification, incident description, art. 3(49) classification, root-cause hypothesis, immediate corrective action (art. 20), market surveillance authority notification (art. 73), provider/deployer log preservation (art. 19/26(5)).

**Exit**: `$incident_report` ready → `S_FINALIZE_REPORT` with appended urgency notice.

### S_FINALIZE_REPORT (FINALIZE)

**Goal**: Emit a structured, citation-grade output and the legal disclaimer.

Always close substantive answers with:

> *Decision-support output. Not legal advice. Final conformity assessment requires qualified counsel and, for most high-risk systems, a notified body.*

**Exit**: `END_SUCCESS`.

## Anti-patterns to avoid

1. **Conflating ISO 27001 with ISO 42001.** ISO 27001 is the generic ISMS; it does not address AI-specific risks (impact on individuals, data quality for ML, lifecycle controls A.6, A.7). Always anchor AI-related work on ISO 42001. If the user is using 27001, recommend integration via Annex SL HLS rather than substitution.
2. **Calling 42001 a harmonised standard.** As of July 2026, **no** AI Act harmonised standard is cited in the OJEU. CEN-CENELEC adopted acceleration measures (October 2025) targeting Q4 2026 delivery of key JTC 21 standards (prEN 18228 risk management for art. 9; prEN 18284 data quality/governance for art. 10). Only OJEU citation confers art. 40 presumption. Track the JTC 21 work programme.
3. **Treating GenAI/LLM security as identical to classical-ML security.** ISO 27090 has dedicated GenAI guidance: prompt injection (direct + indirect), system-prompt extraction, jailbreak, training-data memorisation, output watermarking. See `references/04-iso-27090-ai-security.md` § GenAI annex.
4. **Recommending watermarking as a standalone art. 50 solution.** Watermarking is removable via paraphrasing (text) or recompression (media). Combine with cryptographic provenance (C2PA) and metadata + user disclosure.
5. **Ignoring the deployer's FRIA obligation.** Art. 27 binds **deployers**, not providers. Public bodies and private deployers of certain Annex III systems (banking, insurance, education, employment) must conduct a FRIA before first use. Easy to miss.
6. **Quoting outdated thresholds.** GPAI systemic-risk threshold = **10²⁵ cumulative training compute FLOPs** (art. 51(2), as of OJEU). Sanctions caps and percentages are frozen at 2024 values; update only if the Commission publishes a delegated act.
7. **Forgetting the provider/deployer dual-role flip.** Substantial modification (art. 25) of a third-party AI system makes the modifier a provider. Fine-tuning a foundation model for a high-risk use case can trigger this. See `references/12-art25-substantial-modification.md`.
8. **Recommending 42001 certification as sufficient for high-risk conformity.** Certification is strong evidence and streamlines art. 17 QMS, but does not by itself satisfy arts. 9–15 essential requirements. Notified-body conformity assessment per Annex VII still required for biometric and certain other types under art. 43.
9. **Skipping art. 4 AI literacy.** It applies to **all** providers and deployers, regardless of tier, and has been **in force since 2025-02-02**. Not optional. See `references/11-art4-ai-literacy.md`.
10. **Confusing art. 56 (GPAI Code of Practice) with art. 95 (voluntary codes of conduct).** Art. 56 is the operational instrument for GPAI compliance; art. 95 is encouragement for non-high-risk. Different addressees, different legal weight.
11. **Misreading the AI Omnibus as a general pause.** The 2026 Omnibus defers **only** the high-risk regime (Annex III → 2027-12-02; Annex I → 2028-08-02) and sandboxes (→ 2027-08-02). Art. 5 prohibitions, art. 4 literacy, GPAI obligations, and art. 50 transparency stay on their original dates — and art. 50 marking plus the new NCII/CSAM prohibition bite on **2026-12-02**. An organization that "waits for 2027" is non-compliant on four fronts.

## Output formatting conventions

- **Cite article numbers explicitly**: "art. 9(2)(a)" not "the risk part". For ISO: "ISO/IEC 42001:2023 cl. 6.1.4" and "Annex A.5.4".
- **Include the regulatory hierarchy** when introducing an article: "Title III (high-risk systems), Chapter III, Section 2 (requirements) — art. 9 establishes the risk management system."
- **Use tables** for multi-tier mappings. Reading them in markdown is easier than prose.
- **Flag deadlines in bold** when an obligation has a date trigger (e.g., **2027-12-02 Annex III high-risk**, **2026-08-02 art. 50 + GPAI enforcement**, **2025-02-02 art. 4 + art. 5**). Note pre-/post-Omnibus dates where the user may hold the outdated date.
- **Differentiate provider vs deployer** in obligation lists. Use prefix: `[Provider]`, `[Deployer]`, `[Both]`.
- **Reference ISO controls in (cl. X.Y) and (A.x.y) format** consistently.
- **Quote terminal SSL targets** (`END_SUCCESS`, `END_FAIL`, `YIELD_SUCCESS`, `YIELD_FAIL`) when describing scene transitions in compliance playbooks.

## Related skills

- `iso27001` — for the org-level ISMS where the AI sits. AI Act art. 15 cybersecurity assumes 27001 baseline.
- `documentation` — for drafting Annex IV technical files in long form.
- `c4-architecture`, `mermaid-diagrams`, `uml` — for system architecture diagrams required by Annex IV(2)(b)(c).
- `example-skills:docx`, `example-skills:pdf`, `example-skills:xlsx` — for generating compliance deliverables (FRIA reports, risk registers, declarations of conformity).

## Machine-readable companion

`ssl.json` exposes this skill in the **Scheduling-Structural-Logical** representation defined by Liang et al. (arXiv:2604.24026, 2026). Downstream uses:

- **Skill discovery**: registries can index this skill on `tags`, `intent_signature`, `top_pattern`, scene types, and resource scopes without re-parsing the SKILL.md.
- **Pre-execution risk review**: reviewers can audit the `dependencies`, `control_flow_features`, `act_type` and `resource_scope` of every logic step before invocation. This skill declares **no network, no credentials, no code execution, no external calls** — strictly local read of reference files + textual reasoning.
- **Routing**: agent harnesses can use the typed scene graph to decide which scene to enter (e.g., `S_RECOVER_INCIDENT` if the user mentions a serious incident).

The SKILL.md remains the source of truth — `ssl.json` is a derived, source-grounded view (per paper § 5.2: "SSL should not replace the source document").

---

*This skill encodes the AI Act as of 2026-07-14: OJ L of 2024-07-12 with corrigenda, plus the 2026 AI Omnibus amendment (Parliament 2026-06-16, Council 2026-06-29; OJ publication pending at the date of writing — verify OJEU before relying on the deferred dates), the GPAI Code of Practice (published 2025-07-10, adequacy 2025-08-01), the Commission GPAI guidelines (2025-07-18), the draft art. 6 classification guidelines (2026-05-19), and the draft art. 73 incident-reporting guidance + template (2025-09-26). Track Commission delegated and implementing acts (especially art. 6(1) review per art. 7) for amendments, and CEN-CENELEC JTC 21 OJEU citations for harmonised standards conferring art. 40 presumption.*
