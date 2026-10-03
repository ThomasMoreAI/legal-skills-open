---
name: nist-ai-rmf-legalquants
title: NIST AI Risk Management Framework
description: Apply the NIST AI Risk Management Framework (NIST AI 100-1 + the NIST AI 600-1 Generative AI Profile) to a specific AI system, governance question, or impact assessment. Three modes — consult, governance plan, full assessment — all cite Subcategories (`GOVERN 1.1`) and Profile Action IDs (`GV-1.2-001`) verbatim. Use when the user mentions the AI RMF, NIST RMF, NIST AI 100-1, NIST AI 600-1, GenAI Profile, the four functions (Govern / Map / Measure / Manage), the trustworthy AI characteristics, the 12 GAI risks (confabulation, harmful bias, information integrity, CBRN, data privacy, etc.), or asks "what does NIST say about X" for an AI system.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/nist-ai-rmf
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
sources:
- title: Readme
  path: references/README.md
- title: Functions
  path: references/core/functions.md
- title: Glossary
  path: references/core/glossary.md
- title: Govern
  path: references/core/govern.md
- title: Manage
  path: references/core/manage.md
- title: Map
  path: references/core/map.md
- title: Measure
  path: references/core/measure.md
- title: Trustworthy characteristics
  path: references/core/trustworthy-characteristics.md
- title: Crosswalk
  path: references/crosswalk.md
- title: Actions govern
  path: references/gai-profile/actions-govern.md
- title: Actions manage
  path: references/gai-profile/actions-manage.md
- title: Actions map
  path: references/gai-profile/actions-map.md
- title: Actions measure
  path: references/gai-profile/actions-measure.md
- title: Glossary
  path: references/gai-profile/glossary.md
- title: Risks
  path: references/gai-profile/risks.md
- title: Assessment
  path: references/templates/assessment.md
- title: Consult
  path: references/templates/consult.md
- title: Governance plan
  path: references/templates/governance-plan.md
---

# NIST AI Risk Management Framework

## What this skill does

Applies the NIST AI RMF — by name, by Subcategory, by Action ID — to whatever AI use case, governance question, or assessment the user brings. Three modes; pick one based on the user's question, default to **consult** if unsure.

1. **Consult** — fast lookup. "What should I do per the AI RMF for X?" Returns applicable risks (for GenAI) and the relevant Suggested Actions / Subcategories, quoted verbatim. Best for quick gut-check questions.
2. **Governance plan** — structured plan. "What should our governance plan include per the AI RMF?" Organized around the GOVERN function's Subcategories, with GenAI-specific actions layered in where applicable. Best for standing up or auditing an AI governance program.
3. **Assessment** — full impact assessment. "Run a NIST AI RMF impact assessment for X." Walks all four functions for one specific system. Best when the user wants a documented artifact.

All three modes share the same source-of-truth: verbatim NIST text in `references/`. Quote the files; don't invent or paraphrase.

## Source and scope

Two NIST publications underlie the skill. The verbatim extracted markdown ships in `references/`; the raw source HTMLs and maintainer-only re-extraction tooling live outside this distribution.

- **NIST AI 100-1 (AI RMF 1.0, January 2023)** — the Core framework. Applies to any AI system. Defines Govern, Map, Measure, Manage; their Categories and Subcategories; and seven Trustworthy AI characteristics. Extracted into `references/core/`.
- **NIST AI 600-1 (Generative AI Profile, July 2024)** — the GenAI-specific overlay. 12 enumerated GAI risks and 211 Suggested Actions coded `GV-X.Y-NNN` etc., each mapped to a Core Subcategory. Extracted into `references/gai-profile/`.

The Core applies to *any* AI system. The Profile is an *overlay* on top of the Core for generative systems. So:

- Non-GenAI system → Core only. Don't pull GAI Profile actions; many won't apply.
- GenAI system → Core for the framework + Profile for GenAI-specific risks and actions.
- Mixed pipeline → split per component.

Other NIST AI Profiles exist; they aren't loaded here. If the user asks about one, say so plainly.

## Provenance and decline pathways

This skill ships as a standalone skill. The provenance of every claim must be unambiguous to a reader who never saw the conversation.

**The skill will:**

- **Cite verbatim** every Subcategory ID and Action ID from `references/`. The wording in the output must match the file.
- **Mark model judgment inline.** Applicability calls ("this risk applies here"), operational glosses ("in practice this means…"), role-ownership recommendations, and the final assessment recommendation are model inferences, not NIST statements. Tag the first instance of each kind with `[model judgment — verify against system specifics]` (or the more specific variants in the templates).
- **Distinguish Core vs Profile.** Non-GenAI systems never pull `GV-/MP-/MS-/MG-` action IDs.

**The skill will decline to:**

- **Invent IDs.** If a Subcategory or Action ID doesn't appear in `references/`, it does not exist in NIST's framework. Say so plainly rather than fabricating one.
- **Paraphrase NIST text.** The framework's authority is the publication. Rewording strips the citation value.
- **Assess without input.** If the user's system description lacks the detail to assess a Subcategory, list it as an Open item — don't guess.
- **Substitute for counsel.** NIST is non-binding voluntary guidance. Mandatory regimes (EU AI Act, state AI laws, sector rules) impose actual obligations that may or may not track NIST. Flag the divergence, don't paper over it.

## Workflow

In order, every invocation:

1. **Read `references/README.md` first.** It's the routing index — it tells you which reference files to load for which question. Don't load files greedily.
2. **Gather the question.** Identify the AI use case, system, or governance question. If the user's prompt is vague ("what does NIST say about AI?"), ask one clarifying question before drafting — what system, what context, what decision.
3. **Decide the mode.** Consult / governance plan / assessment. Most queries are consult unless the user explicitly asks for a plan or an assessment.
4. **Decide GenAI or not.** Foundation models, LLMs, image/audio/video/text generators, RAG over a generative core — GenAI. Classifiers, regressors, recommenders, anomaly detectors, traditional ML — not GenAI (use Core only).
5. **Load only the reference files the question needs**, per `references/README.md`.
6. **Load the relevant output template** from `references/templates/<mode>.md` when drafting output.
7. **Produce output per the template** with verbatim citations and the provenance markers described above.

## Mode 1 — Consult

**When to use:** the user is asking "what should we do?" or "what does NIST say about?" with a specific system or scenario in mind. Fast turnaround. Not a deliverable artifact.

**Procedure:**

1. From the system description, identify:
   - System type (GenAI? non-GenAI? mixed?).
   - For GenAI: which of the 12 GAI risks plausibly apply. Use `gai-profile/risks.md` + `crosswalk.md`. Be honest — if a risk obviously doesn't apply (e.g., CBRN for a customer-service chatbot), say so and exclude it. Don't pad.
   - For any system: which of the Core Subcategories most directly apply. Usually 4–10, not all of them.
2. Pull the relevant Suggested Actions (GenAI) or Subcategory statements (non-GenAI) into a table. Group by function.
3. Surface 2–4 follow-up questions the user can't answer from the framework alone (e.g., "What's your incident response capacity?"). The framework points; the user fills in.

**Output template:** `references/templates/consult.md` — load when drafting.

## Mode 2 — Governance plan

**When to use:** the user is building or auditing an AI governance program, not assessing one specific system. They want structure, not a system-specific deep dive.

**Procedure:**

1. Bias toward the **GOVERN** function in the Core. Walk every Category (GOVERN 1–6). For each Category, list the Subcategories with one-sentence "in practice" annotations (operational glosses, marked accordingly per template).
2. Add MAP / MEASURE / MANAGE Subcategories that have clear governance-program implications (e.g., **MAP 1.5** "Organizational risk tolerances are determined and documented" — governance owns the tolerance definitions even though it's a MAP Subcategory).
3. If the org uses or plans to use GenAI, layer in the GAI Profile GOVERN actions per Subcategory.
4. Cross-reference the seven Trustworthy AI characteristics — most policies should commit to each by name.

**Output template:** `references/templates/governance-plan.md` — load when drafting.

## Mode 3 — Assessment

**When to use:** the user wants a documented artifact assessing one specific system end-to-end. Heavier than a consult. The output should be self-contained — a reader who never saw the conversation should understand it.

**Procedure:**

1. Confirm the scope: one system, one version, one deployment context. If the user is vague, ask before drafting.
2. Walk all four functions. For each function, identify the applicable Subcategories and (for GenAI) Action IDs. Cite verbatim.
3. For each Subcategory / action, write a one-paragraph assessment of *what we found about this system against this Subcategory*. Honest, specific. If you don't have the input to assess something, say so and list it as an open item — don't bluff.
4. Conclude with a recommendation: deploy / deploy with conditions / do not deploy. Conditions, if any, must reference specific Subcategories so they're verifiable.

**Output template:** `references/templates/assessment.md` — load when drafting.

## Output formatting

**Work-product header.** Default to `CONFIDENTIAL — Internal Use` at the top of every output. If the user is operating in a legal context and asks for an attorney-work-product header, switch to `ATTORNEY WORK PRODUCT. PRIVILEGED AND CONFIDENTIAL.` for that output.

**Markdown to stdout.** Don't write files. The output is markdown for the user to copy, edit, route, or save themselves.

**Citations.** Always include the Subcategory or Action ID as a clear citation (e.g., `**GOVERN 1.1**` or `` `GV-1.2-001` ``). The verbatim NIST statement goes right after. Never bury the citation in a footnote.

## What this skill is and isn't

**It is:** a way to apply the NIST AI RMF rigorously, with verbatim citations, to specific questions and systems. It saves a lawyer or governance professional from re-reading the full PDF every time.

**It isn't:**
- A substitute for legal counsel. NIST is non-binding. Mandatory regulatory regimes (EU AI Act, state AI laws, sector rules) impose actual obligations that may track to NIST or may not. Flag the divergence; don't replace the analysis.
- A compliance certification. Citing the framework is not the same as meeting it. The conditions in a Mode 3 recommendation should be auditable — but auditing is not what this skill does.
- A complete library of NIST AI publications. Only AI 100-1 and AI 600-1 are loaded. If the user asks about other Profiles, NIST AI Safety Institute publications, or NIST cybersecurity / privacy frameworks, say so.

## Limitations

- **Source dates.** AI 100-1 is from January 2023; AI 600-1 is from July 2024. The framework is intended as a living document; later revisions may exist. Treat the skill's content as a frozen snapshot.
- **Non-binding.** Suggested Actions and Subcategories are voluntary guidance. They become "what we did" only when the organization adopts them.
- **GenAI scope.** The Profile assumes generative AI. Applying its actions to a non-generative system creates noise — don't do it.
- **Verbatim citations only.** If a Subcategory or Action ID doesn't appear in `references/`, it doesn't exist (in NIST's framework). Don't invent.
