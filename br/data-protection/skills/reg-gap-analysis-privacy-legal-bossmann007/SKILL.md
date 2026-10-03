---
name: reg-gap-analysis-privacy-legal-bossmann007
title: /reg-gap-analysis
description: Diff a new or changed regulation against current privacy policy and practice — outputs a gap list and a remediation plan with owners and dates. Use when a new reg drops, the user asks "does [regulation] affect us", "gap analysis for [new Resolução CD/ANPD or sectoral rule]", "compliance check against [reg]", or pastes regulatory text.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/privacy-legal/skills/reg-gap-analysis
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: en
---

# /reg-gap-analysis

1. Load `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → privacy policy commitments, regulatory footprint, DSAR systems.
2. Run the workflow below.
3. Scope: does the regulation apply? (jurisdiction, thresholds, sector)
4. Extract requirements → diff against current state → gap list.
5. Remediation plan with owners, dates, prioritization.
6. Save dated doc. Even "no gaps" gets documented.

```
/privacy-legal:reg-gap-analysis "Resolução CD/ANPD nº 15/2024"
```

```
/privacy-legal:reg-gap-analysis
[paste guidance / reg text]
```

---

# Regulation-to-Policy Gap Analysis

## Purpose

The ANPD issues new guidance or a Resolução CD/ANPD. A sectoral regulator (BCB, ANVISA, ANS) finalizes a rule touching personal data. The ICO or another foreign DPA issues guidance relevant to a cross-border footprint. Something moves — and now you need to know what, if anything, you have to change.

This skill diffs the new requirement against what you currently do (per `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → Privacy policy commitments + the practices documented in PIAs) and produces a gap list with a remediation plan.

## Load current state

Read `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md`:
- `## Privacy policy commitments` — what you've publicly promised
- `## Regulatory footprint` — what already applies
- `## DSAR process` → systems list — what you actually do operationally

If the regulation doesn't apply to you (wrong jurisdiction, below threshold, different sector), the gap analysis is one line: "Doesn't apply. Here's why: [reason]. No action needed."

## Workflow

### Step 1: Scope the regulation

Before diffing, answer:

- **Does it apply?** Jurisdiction (do you have data subjects there?), threshold (revenue, user count, data volume), sector carve-outs
- **When?** Effective date, enforcement date (often later), any phase-in
- **What's actually new?** Brazil has a single national framework (LGPD), not a state-by-state patchwork — a simpler regulatory map than jurisdictions with dozens of overlapping state laws. Most "new" developments are ANPD Resoluções refining an existing LGPD provision, or a sectoral regulator (BCB, ANVISA, ANS) layering a rule on top of LGPD, not a wholesale new regime. Identify the delta from what you already comply with under LGPD, not the full text.

### Step 2: Extract requirements

Read the regulation (or summary/guidance). List every substantive requirement as a discrete item:

| # | Requirement | Citation | Category |
|---|---|---|---|
| 1 | [requirement as stated] | [section] | [Notice / Rights / Security / Vendor / Other] |

**Categories:**
- **Notice** — what you have to tell users (privacy policy content)
- **Rights** — what users can ask for (DSAR-adjacent)
- **Security** — technical/organizational measures
- **Vendor** — what you have to flow down to processors
- **Consent** — opt-in/opt-out mechanics
- **Governance** — DPO, impact assessments, record-keeping

### Step 3: Diff against current state

For each requirement:

```markdown
### [Requirement #N]: [short name]

**Regulation says:** [requirement, quoted or paraphrased]

**We currently:** [what the config CLAUDE.md / privacy policy / practice shows]

**Gap:** [None | Partial | Full]

**If partial/full gap — what's missing:** [specific]

**Effort to close:** [Policy update only | Product change | Vendor renegotiation |
New process]

**Risk of non-compliance:** [regulatory penalty range, enforcement likelihood,
reputational]
```

### Step 4: Prioritize

Not every gap is equal. Sort by:

1. **Hard deadline with teeth** — effective date + active enforcement + real penalties
2. **Effort-to-impact ratio** — policy language update is cheap; product rebuild is not
3. **What you've already half-done** — if you're 80% there for GDPR, the LGPD delta may be small (and vice versa — the two regimes overlap substantially)

### Step 5: Remediation plan

Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` `## Outputs` (it differs by user role — see `## Who's using this`).

> **Research-connector pre-flight.** Before emitting the remediation plan, check whether a legal research connector is reachable for this session — JusBrasil, Escavador, PJe, gov.br/anpd, an EUR-Lex / regulator-site connector, or any firm-configured research MCP. Collect this into the reviewer note per CLAUDE.md `## Outputs`: if no connector returns results in Step 2 or the Common regulation categories research step (or none is configured at run time), record it in the **Sources:** line of the reviewer note — e.g., `not connected — cites from training knowledge; the highest-fabrication items in privacy gap analyses are new Resolução/regulatory effective dates, enforcement-begins dates, and article/section pinpoints — spot-check those first`. Per-citation `[model knowledge — verify]` tags remain inline. Do not emit a standalone banner above the output.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

## Remediation Plan: [Regulation name]

**Effective date:** [date]
**Enforcement begins:** [date]

### Must-do before enforcement

| Gap | Fix | Owner | Due | Status |
|---|---|---|---|---|
| [gap] | [specific fix] | [name] | [date] | [ ] |

### Should-do (lower risk, not blocking)

[same table]

### Already compliant

[list of requirements where gap = None — useful for the "we're mostly fine" message]

### Accepted gaps (risk-accepted, not fixing)

[if any — with documented rationale and who accepted the risk]
```

## Common regulation categories

When scoping the delta, it helps to place the new regulation into a rough category and then research the specifics:

- **Baseline data-protection / privacy law** — broad coverage of a jurisdiction's personal data practices
- **Sector-specific overlay** — health, finance, children, education, employment, etc.
- **AI-specific regime** — transparency, impact assessments, or governance for automated decision-making
- **Data broker / ad-tech regime** — registration, opt-out, deletion mechanisms
- **Breach-notification regime** — standalone or embedded in a broader law
- **Cross-border transfer regime** — adequacy, mechanism, and assessment requirements

For each category relevant to the new regulation, **research the currently operative requirements** before drafting the gap analysis. Cite primary sources. Verify currency — ANPD publishes new Resoluções and interpretive guidance on an ongoing basis (track via gov.br/anpd), and sectoral regulators (BCB, ANVISA, ANS) do the same for their verticals; do not rely on a static checklist. Flag uncertainty for attorney verification rather than assert a rule you haven't confirmed.

> **No silent supplement.** If a research query to the configured legal research tool (JusBrasil, Escavador, PJe, or firm platform) returns few or no results for a regulation, guidance document, or enforcement action, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [regime / topic]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against the issuing authority (gov.br/anpd or the relevant sectoral regulator) before relying, or (4) flag as unverified and stop. Which would you like?" A lawyer decides whether to accept lower-confidence sources.
>
> **Source attribution tiering.** Tag every citation in the gap analysis with its source. For model-knowledge citations, use one of three tiers rather than a single blanket "verify" tag:
>
> - `[settled]` — stable, well-known statutory and regulatory references unlikely to have changed (e.g., LGPD art. 46 on security measures, GDPR Art. 33, ANPD's core sanctions framework at LGPD arts. 52-54). Still verify before filing, but lower priority.
> - `[verify]` — model-knowledge citations that are real but should be verified: specific implementing regulations, agency guidance, case holdings, thresholds, effective dates, newly enacted state statutes.
> - `[verify-pinpoint]` — pinpoint citations (specific subsection letters, volume/page numbers, paragraph numbers, regulatory subpart references) carry the highest fabrication risk and should ALWAYS be verified against a primary source.
>
> Tool-retrieved citations keep their source tag (`[JusBrasil]`, `[issuing authority site]`, or the MCP tool name); web-search citations remain `[web search — verify]`; user-supplied citations remain `[user provided]`. The tiering surfaces the real verification work — a reader who verifies everything verifies nothing. Never strip or collapse the tags.

## Integration with other skills

**From PIA generation:** PIAs flag privacy policy inconsistencies → those feed here as known gaps.

**To the regulatory-legal plugin (if installed):** This skill is the manual version. The monitor plugin watches feeds and triggers this analysis automatically when something changes.

## Output

Save as a dated markdown doc. The remediation plan table becomes a tracker — update status as items close.

If the gap analysis concludes "no gaps, we're compliant," still write the doc — it's useful evidence later that you looked.

**Close with a citation-verification note:**

> Citations in this output were generated by an AI model and have not been verified against a primary source. Before relying on any regulation, statute, guidance, or enforcement action, check it against a legal research tool (JusBrasil, Escavador, PJe, your firm's research platform, or the issuing authority's website — gov.br/anpd for ANPD matters) for accuracy and current status. AI-generated citations are sometimes fabricated or misquoted. Source tags on each citation (e.g., `[web search — verify]`) show where it came from; `verify` tags carry higher fabrication risk and should be checked first.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- It doesn't interpret ambiguous regulatory language authoritatively. When the reg is unclear, say so: "Section X could be read as [A] or [B]. [A] is the conservative read. Suggest outside counsel if this is material."
- It doesn't track regulatory changes proactively. It runs when you point it at a change. For proactive monitoring, see the regulatory-legal plugin.
- It doesn't implement fixes. It plans them.
