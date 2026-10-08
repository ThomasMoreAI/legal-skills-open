---
name: research-deep-research-orchestrator-sboghossian
title: Deep Research Orchestrator
description: Use when a legal question requires multi-step, multi-source, multi-jurisdiction research equivalent to a senior associate's full memo — not a quick lookup. Triggers on "I need this for a memo," "for a client opinion," multi-jurisdictional questions, or when confidence on a high-stakes question is low. Orchestrates sub-agents for statute lookup, case-law search, regulator guidance, and amendments tracking; synthesizes into a structured legal memo with table of authorities. Slow and credit-intensive — always estimates cost upfront and confirms with user.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/research/research-deep-research-orchestrator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Deep Research Orchestrator

Multi-step, orchestrated legal research for complex questions requiring the equivalent of a senior associate's memo. This skill coordinates multiple sub-research agents — statute lookup, case law, regulator guidance, recent amendments — and synthesizes their outputs into a structured, footnoted legal analysis. It is explicitly **not** a quick-answer skill; use single-purpose research skills for fast lookups.

## When to invoke

Invoke this skill when **any** of the following apply:

1. The user explicitly asks for "thorough research," "a memo," "a client opinion," or "a comprehensive analysis."
2. The question spans multiple jurisdictions and the interaction between them is legally material.
3. A quick statute or case lookup returned ambiguous or conflicting results that require synthesis.
4. The question involves a recent regulatory change and the practitioner needs to know current law + transitional provisions + regulator guidance + case law interpreting the change.
5. The stakes are high (deal, litigation, regulatory filing) and confidence in a simple answer is below the threshold needed to act on it.
6. The user's question implies reliance on the answer for professional advice to a client.

**Do not invoke** for questions well-handled by:
- [[research-statute-lookup]] — when the user just needs the text of a specific article
- [[research-case-law-search]] — when the user has a specific legal issue in one jurisdiction and needs relevant precedents
- [[research-regulation-lookup]] — when the user needs the regulatory text only

Deep research consumes significantly more time and tokens than single-purpose skills. Triggering it unnecessarily wastes user credits and creates latency.

## Pre-flight: cost and time estimation

Before beginning, estimate and disclose:

```
Deep research on [topic] across [jurisdictions] will:
- Take approximately [3–8 minutes] (more for multi-jurisdiction work)
- Consume approximately [X] credits (based on expected sub-agent calls)
- Produce a [N-page equivalent] structured memo

Proceed? (yes / adjust scope / run quick-answer instead)
```

User must confirm before the orchestrator begins execution. Exception: if the user has pre-authorized deep research in their session settings.

## Step 1 — Question refinement

Restate the research question with precision:
- What is the legal issue? (not just the topic — the specific question in dispute)
- What is the applicable jurisdiction or jurisdictions?
- What is the user's position or perspective? (which side of the deal / dispute)
- What is the output to be used for? (memo, client advice, deal structure, court filing)
- Are there known constraints? (e.g., "assume Lebanese law applies; also note if OHADA would reach a different result")

If any of these are ambiguous, ask one clarifying question before proceeding.

## Step 2 — Decomposition

Break the research question into sub-questions, each answerable by a specific sub-agent. Example decomposition for "What are the limits on non-compete clauses in UAE employment contracts?":

1. What does UAE federal law (FDL 33/2021) say about non-competes? → [[research-statute-lookup]] (UAE)
2. What did courts say before and after the 2021 reform? → [[research-case-law-search]] (UAE onshore + DIFC)
3. What does MOHRE guidance say about enforcement? → [[research-regulator-guidance-lookup]]
4. Has anything changed since FDL 33/2021 took effect (Dec 2021)? → [[research-recent-amendments-tracker]] (UAE)
5. How does this compare in DIFC / ADGM? → [[research-jurisdiction-comparison]] (UAE federal vs DIFC vs ADGM)
6. What is the maximum enforceable duration and geographic scope? → Synthesize from steps 1–4

Document the decomposition in the memo's "Research plan" section so the user can see the methodology.

## Step 3 — Source plan

For each sub-question, identify the connector or tool to use:

| Sub-question | Primary source | Fallback |
|---|---|---|
| Statute text | [[connector-legal-data-hunter]], official gazette | [[research-statute-lookup]] |
| Case law | Jurisdiction-specific database (DIFC Courts portal, Najiz, etc.) | [[tool-web-search-orchestrator]] for recent decisions only |
| Regulator guidance | Regulator portals (DFSA, SAMA, MOHRE, etc.) | [[research-regulator-guidance-lookup]] |
| Recent amendments | Official gazette date-filtered | [[research-recent-amendments-tracker]] |
| EU / FR law | [[connector-eur-lex]], [[connector-legifrance]] | — |
| US law | [[tool-courtlistener-us]], USC/CFR | — |

Primary sources only. Commentary and secondary sources may be referenced for context but may not be cited as authority.

## Step 4 — Sequential execution

Execute sub-agent calls sequentially (or in parallel where independent), gathering:
- Statutory text with article numbers and effective dates
- Case summaries with verified citations (cite-or-bust rule applies to every citation)
- Regulatory guidance with issuance dates and supersession chain
- Recent amendment summaries with official gazette references

Log each source retrieved: `{ source, citation, asOfDate, confidence }`.

If a sub-agent returns no result (no statute found, no cases in jurisdiction on point), document the null finding. Do not speculate or fill gaps with training-data assumptions.

## Step 5 — Synthesis

Synthesize across all gathered sources using IRAC structure per sub-question, then aggregate:

### IRAC per sub-question
- **Issue**: the specific legal question
- **Rule**: the applicable legal rule from statute, case law, and/or guidance
- **Application**: how the rule applies to the user's facts (or the hypothetical presented)
- **Conclusion**: the legal position, with confidence level

### Conflict surfacing
Where sources conflict — e.g., a statute says one thing, a court interpreted it differently, and regulator guidance introduces a carve-out — surface the conflict explicitly rather than resolving it silently. State: "The statute as written appears to permit X; however, the [court / regulator] has taken the position that Y applies. The unresolved tension means the outcome is uncertain without further authority or professional advice."

## Step 6 — Output format

### Memo structure

```
MEMORANDUM

To:      [User / Matter reference]
Re:      [Legal question restated]
Date:    [ISO date]
Scope:   [Jurisdictions covered; assumptions]

EXECUTIVE SUMMARY
[3–5 bullet points: bottom-line conclusions, key risks, open issues]

ANALYSIS

[Section per sub-question, using IRAC]

1. [Sub-question heading]
   Issue: …
   Rule: …
   Application: …
   Conclusion: …

2. [Next sub-question]
   …

OPEN ISSUES AND ESCALATION POINTS
[Questions that require further facts, professional judgment, or jurisdiction-qualified advice]

TABLE OF AUTHORITIES
[All sources cited, grouped by type: statutes, cases, regulator guidance, other]

RESEARCH METHODOLOGY
[Which sub-agents ran; sources queried; date of research; confidence ratings]

DISCLAIMER
This memo is produced by an AI assistant for informational purposes and does not constitute legal advice. Verify all citations against primary sources before reliance.
```

## Latency and credit budget management

| Research scope | Estimated time | Estimated credits |
|---|---|---|
| Single jurisdiction, 1–2 sub-questions | 3–5 min | Low |
| Single jurisdiction, complex (4+ sub-questions) | 5–10 min | Medium |
| Multi-jurisdiction (2–3 jurisdictions) | 8–15 min | High |
| Multi-jurisdiction (4+ jurisdictions) | 15–25 min | Very high |

Cap the number of sub-agent calls at 12 unless the user has explicitly authorized an uncapped run. If the cap is reached, pause and report: "Research cap reached. X sub-questions remain unexecuted. Shall I continue (additional credits) or produce a partial memo with open issues flagged?"

## Anti-patterns

- Do not substitute training-data knowledge for actual retrieval — always fetch from authoritative sources.
- Do not cite commentary (law review articles, blog posts) as primary authority.
- Do not produce a confident conclusion on an issue where the retrieved sources are insufficient to support it — state the uncertainty.
- Do not run deep research when [[research-statute-lookup]] or [[research-case-law-search]] would suffice.
- Do not omit the disclaimer — this tool produces analysis, not legal advice.

## Related skills

- [[research-statute-lookup]]
- [[research-case-law-search]]
- [[research-recent-amendments-tracker]]
- [[research-regulator-guidance-lookup]]
- [[research-jurisdiction-comparison]]
- [[router-confidence-scorer]]
