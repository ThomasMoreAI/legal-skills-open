---
name: legal-framework-mapping-lsdisconzi
title: Legal Framework Mapping
description: Map each matter fact to each applicable legal article across all jurisdictions. Frameworks and articles are loaded from packs; optional argus-law / garage MCPs assist retrieval.
author: lsdisconzi
author_url: https://github.com/lsdisconzi/craudio-para-adevogados/tree/main/skills/legal-framework-mapping
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Legal Framework Mapping

Systematically maps matter facts to legal norms across every jurisdiction the matter declares. This is the foundational analysis that powers every other engine. It names no statute — frameworks, articles, and norm templates all come from packs.

## Inputs

- **Matter facts** — actions, evidence, and violation records from `{vault root}`.
- **Domain pack(s)** — `packs/domain/<id>/norm-templates.yaml` supplies normalized norm templates with `required_elements`.
- **Jurisdiction pack(s)** — `packs/jurisdiction/<id>/framework-index.yaml` lists each framework's statutes and articles.

## Running this skill

1. **Load configuration.** Read the configured matter profile and firm profile from the plugin config directory (see CLAUDE.md `## Configuration Location`). If a file is missing, or a critical field still shows `[PLACEHOLDER]`, STOP — tell the attorney: "This plugin needs setup. Run the `cold-start-interview` skill."
2. **Apply the frame.** The Plugin Operating Rules, Shared Guardrails, Decision posture, Jurisdiction recognition, Retrieved-content trust, and Ontology Governance sections of CLAUDE.md govern this skill. The workflow below is a FLOOR, not a ceiling.
3. **Resolve vault paths.** Every `{vault root}` reference resolves against `## Vault location` in CLAUDE.md. Never hard-code an absolute path.
4. **Determine active packs.** Read which domain and jurisdiction packs the matter declares (matter profile `## Packs`).
5. **Apply the work-product header** from CLAUDE.md `## Outputs` to every internal deliverable; suppress it on externally-facing output per Quiet mode.
6. **Run the workflow below.**
7. **Close** with the `⚠️ Reviewer note` block and the next-steps decision tree from CLAUDE.md `## Outputs`. Run the `ontology-validate` skill on the output before it reaches a court or counterparty.

---

## Workflow

### 1. Load frameworks
For each jurisdiction pack the matter declares, read `framework-index.yaml`. Where the `argus-law` MCP is connected, use it for full article text (`argus_framework_lookup`) and engagement detection (`argus_article_nexus`); where `garage` is connected, use RAG retrieval for on-demand article text.

### 2. Fact-to-article mapping
For each matter fact, identify the engaged articles. For each engaged article record: the article (from the jurisdiction pack), the nexus (why this fact engages this article), and the evidence anchor.

```
FACT: <fact statement> (<incident, date, time>)

Engaged articles:
├── <jurisdiction>.<framework>.<article> — <article title>
│   └── Nexus: <why the fact engages the article>
│   └── Evidence: <evidence anchors>
└── ...
```

### 3. Framework gap analysis
Identify gaps: an obligation exists in law but counterparty practice negates it; a state obligation exists but state conduct breaches it; a treaty obligation exists but domestic law provides no remedy; a protection exists in one jurisdiction but is absent in another.

### 4. Comparative framework analysis
Where the matter spans multiple jurisdictions, compare how the same fact is treated under each jurisdiction's framework (from the respective packs), respecting doctrinal differences between the legal systems.

### 5. Article text retrieval
Retrieve and verify the full text of every engaged article against official sources (via `garage` RAG where connected).

### 6. Output
- **Framework engagement matrix** — Fact × Article × Nexus × Evidence
- **Gap analysis report** — where law protects but practice negates
- **Comparative chart** — same fact, different legal treatment across jurisdictions
- **Article text reference** — complete text of all engaged articles

## Integration
- Foundation for `violation-analysis`, `claim-chart`, `cross-jurisdiction-nexus`.
- Run before any brief or demand drafting.
- Re-run when new jurisprudence or a pack update affects framework interpretation.

## Ontology graph vocabulary

This skill constructs the legal-domain layer of the graph (`core/ontology/graph-model.yaml`): `CONTAINS_ARTICLE` (Framework → LegalArticle), `VIOLATES_ARTICLE`, `HAS_APPLICABILITY_BASIS`, `GROUNDED_IN_ACTION`. A `LegalArticle`'s framework and jurisdiction must match its parent `LegalFramework`; no orphan articles.

## Guardrails
- Article text must be verified against official sources.
- Framework interpretations are analytical, not authoritative.
- Gap analysis identifies legal gaps, not advocacy opportunities.
- Comparative analysis respects doctrinal differences between legal systems.
- **Ontology compliance:** outputs must satisfy the litigation-relevant error codes in `core/ontology/error-catalog.md`. If an invariant violation is detected, flag with `[ONT-ERROR: <code>]` and do not produce confident output. I-1 is absolute: no conclusory language.
