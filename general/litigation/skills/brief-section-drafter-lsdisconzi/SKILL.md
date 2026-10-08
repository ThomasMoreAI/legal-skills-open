---
name: brief-section-drafter-lsdisconzi
title: Brief Section Drafter
description: Draft sections of legal briefs and petitions for the matter's forums. Produces jurisdiction-specific brief sections in the forum's language with evidence citations.
author: lsdisconzi
author_url: https://github.com/lsdisconzi/craudio-para-adevogados/tree/main/skills/brief-section-drafter
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Brief Section Drafter

Drafts court-ready brief sections for each forum the matter declares. Each section is jurisdiction-specific in language, format, and legal framework. This workflow names no court or party itself — forums come from jurisdiction packs, parties and facts from the matter.

## Running this skill

1. **Load configuration.** Read the configured matter profile and firm profile from the plugin config directory (see CLAUDE.md `## Configuration Location`). If a file is missing, or a critical field still shows `[PLACEHOLDER]`, STOP — tell the attorney: "This plugin needs setup. Run the `cold-start-interview` skill."
2. **Apply the frame.** The Plugin Operating Rules, Shared Guardrails, Decision posture, Jurisdiction recognition, Retrieved-content trust, and Ontology Governance sections of CLAUDE.md govern this skill. The workflow below is a FLOOR, not a ceiling.
3. **Resolve vault paths.** Every `{vault root}` reference resolves against `## Vault location` in CLAUDE.md. Never hard-code an absolute path.
4. **Determine active packs.** Read which jurisdiction packs the matter declares (matter profile `## Packs`); the forum, language, citation format, and filing requirements all come from them.
5. **Apply the work-product header** from CLAUDE.md `## Outputs` to every internal deliverable.
6. **Run the workflow below.**
7. **Close** with the `⚠️ Reviewer note` block and the next-steps decision tree from CLAUDE.md `## Outputs`. Run the `ontology-validate` skill on each draft.

---

## Workflow

### 1. Resolve the forum
For each forum the matter declares, read its jurisdiction pack: `courts.yaml` (the court and its e-filing system), `language-defaults.yaml` (language, register, address conventions), `citation-format.yaml` (how statutes and jurisprudence are cited), and `procedural-rules.yaml` (the procedure code and filing requirements).

### 2. Petition structure
Draft the petition in the forum's structure — a civil-law petition generally runs: court address; identification of the parties; statement of facts (chronological, with evidence citations); statement of law (engaged articles × facts × nexus reasoning, drawing on the `legal-framework-mapping` and `claim-chart` engine outputs); statement of damages (per the `prejudice-quantification` output); concrete prayers for relief; value of the claim; and the closing signature block. Use the forum's terms of art from its jurisdiction pack — never mix one jurisdiction's terminology into another's filing.

### 3. Evidence annex
Index all exhibits; authenticate each per the jurisdiction pack's authentication standards (via the `document-authentication` engine); prepare a hash manifest for digital evidence; obtain certified translations where the destination forum requires them.

### 4. Urgent / preliminary relief
Where immediate relief is warranted, draft the forum's interim-relief request (e.g. an urgency injunction, or a pre-suit measure to preserve evidence) per the jurisdiction pack.

### 5. Output
- **Full petition draft** in `.docx`, one per forum, in the forum's language
- **Evidence annex index** with authentication status
- **Filing checklist** — signatures, copies, costs, e-filing protocol (from the jurisdiction pack)
- **Translations** — between the forums' languages where evidence crosses a border

## Guardrails

- Brief sections are DRAFTS for attorney review — not filings.
- All cited evidence must be authenticated before filing.
- Spelling, grammar, and legal terminology must match the forum's jurisdiction — never mix terms across jurisdictions.
- Filing deadlines follow the jurisdiction pack's procedural code.
- Every legal assertion must carry a supporting article or precedent citation.
- A filing in a jurisdiction that requires local counsel must be routed to that counsel before filing.
- **Ontology compliance:** outputs must satisfy the litigation-relevant error codes in `core/ontology/error-catalog.md`. If an invariant violation is detected, flag with `[ONT-ERROR: <code>]` and do not produce confident output. I-1 is absolute: no conclusory language.
