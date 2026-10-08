---
name: jurisprudence-search-lsdisconzi
title: Jurisprudence Search
description: Search jurisprudence databases for supporting precedent in each jurisdiction the matter declares. The jurisprudence source for each jurisdiction is named in its jurisdiction pack.
author: lsdisconzi
author_url: https://github.com/lsdisconzi/craudio-para-adevogados/tree/main/skills/jurisprudence-search
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Jurisprudence Search

Searches jurisprudence databases for supporting precedent. This is a retrieval engine — it names no court or case. For each jurisdiction the matter declares, it uses the jurisprudence source named in that jurisdiction pack (`pack.yaml` → `jurisprudence_source`: an MCP connector or web search).

## Inputs

- **Matter facts** — the violation(s) or legal question under research.
- **Jurisdiction pack(s)** — `courts.yaml` lists the court hierarchy; `pack.yaml` names the jurisprudence source and any known leading precedents.

## Running this skill

1. **Load configuration.** Read the configured matter profile and firm profile from the plugin config directory (see CLAUDE.md `## Configuration Location`). If a file is missing, or a critical field still shows `[PLACEHOLDER]`, STOP — tell the attorney: "This plugin needs setup. Run the `cold-start-interview` skill."
2. **Apply the frame.** The Plugin Operating Rules, Shared Guardrails, Decision posture, Jurisdiction recognition, Retrieved-content trust, and Ontology Governance sections of CLAUDE.md govern this skill. The workflow below is a FLOOR, not a ceiling.
3. **Resolve vault paths.** Every `{vault root}` reference resolves against `## Vault location` in CLAUDE.md. Never hard-code an absolute path.
4. **Determine active packs.** Read which jurisdiction packs the matter declares (matter profile `## Packs`).
5. **Apply the work-product header** from CLAUDE.md `## Outputs` to every internal deliverable; suppress it on externally-facing output per Quiet mode.
6. **Run the workflow below.**
7. **Close** with the `⚠️ Reviewer note` block and the next-steps decision tree from CLAUDE.md `## Outputs`. Run the `ontology-validate` skill on the output before it reaches a court or counterparty.

---

## Workflow

### 1. Resolve the search target
Identify the legal question(s) — typically the norm template(s) behind a violation under analysis, plus the damage type and the actor class (private party vs. public agent).

### 2. Search each jurisdiction
For each jurisdiction pack the matter declares:
- Read `pack.yaml` → `jurisprudence_source` and `courts.yaml` for the court hierarchy.
- Query the named source (jurisprudence MCP if connected; otherwise web search) at each court tier — apex/constitutional, uniformizing, and trial/appellate.
- Pull any leading precedents listed in the jurisdiction pack and run citation/relator analysis where the source supports it.
- If a jurisdiction pack names no jurisprudence source, fall back to web search and tag results `[web search — verify]`.

### 3. Search by theme
Build search terms per violation theme from the norm templates (in the language(s) the jurisdiction packs declare). Search both the substantive theme and the damage theme.

### 4. Output
- **Precedent digest** — organized by theme and court
- **Citation network map** — how precedents relate
- **Damage award table** — comparable awards
- **Precedent strength assessment** — binding vs. persuasive vs. distinguishable
- **Jurisprudence gap report** — questions with no direct precedent (novel issues)

## Integration
- Run after `violation-analysis` to find precedent for each violation.
- Feed findings into `claim-chart` for element support.
- Cite in `demand-draft` and `brief-section-drafter`.

## Guardrails
- All citations carry a session-provenance tag: `[juris-<jurisdiction>]`, `[web search — verify]`, or `[model knowledge — verify]`.
- Quote-to-proposition check: verify the citation supports the proposition as stated.
- Tool-vs-model conflict: surface both when a research tool conflicts with training knowledge.
- Precedent from a jurisdiction with no connected jurisprudence source is marked `[verify against primary source]`.
- **Ontology compliance:** outputs must satisfy the litigation-relevant error codes in `core/ontology/error-catalog.md`. If an invariant violation is detected, flag with `[ONT-ERROR: <code>]` and do not produce confident output. I-1 is absolute: no conclusory language.
