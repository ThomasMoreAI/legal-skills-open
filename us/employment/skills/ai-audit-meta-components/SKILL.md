---
name: ai-audit-meta-components
title: AI audit meta-components (Components 10–12)
description: 'Use when auditing the cross-cutting "meta" considerations of an AI/ML personnel assessment that apply across every other component — Components 10-12 of the Landers & Behrend (2023) framework: cultural context (power differentials, cross-cultural transfer, community participation), respect (conformance to accepted ethical standards — the Standards, SIOP Principles, OECD Principles, UGAI), and research designs (whether the studies behind every empirical claim are methodologically defensible). Triggers: "cross-cultural AI hiring", "power differentials in algorithm design", "ethical standards conformance audit", "are the studies behind the claims valid", "research design integrity of an AI audit", "community participation in AI design".'
author: OpenMatter-Network
author_url: https://github.com/OpenMatter-Network/agent-io-skills/tree/main/ai-personnel-assessment/skills/ai-audit-meta-components
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
tags: [community, io-psychology, ai-assessment, auditing]
---

# AI audit meta-components (Components 10–12)

These three components are **meta** because they must be considered **across all the other components**,
not as a separate stage. They ask: in what cultural and ethical context does this system operate, and
is the **evidence** behind every claim methodologically sound?

## Component 10 — Cultural context

**What it is:** the broader cultural setting in which the algorithm is used, and whether affected
communities had a voice in it.

**Questions to ask:** Has the broader **cultural context** been considered? Have **members of the
community participated** in the design of systems that will affect them?

**Apply it (focal example):** Do **power differentials** exist between designers, employers, and job
candidates? Have **cultural assumptions** been made? Will development decisions made **in one culture
be applied to another** — and if so, how has the development process been **adjusted to prevent
cross-cultural application challenges**?

**Audit emphases:**
- Name the **power asymmetry**: designers and employers hold power over candidates who often can't opt
  out, see their data, or contest a score.
- Flag **cross-cultural transfer**: a model trained/validated in one cultural or linguistic context
  and deployed in another (different dialects, norms, nonverbal behavior) without adjustment is a
  high-risk finding. Connects to feature-engineering choices (dialect/NLP) in
  `ai-model-development-audit` and to linguistic/cultural equivalence in
  `candidate-accommodations`.
- Ask whether affected **communities participated** in design — absence is itself a finding.

## Component 11 — Respect (conformance to ethical standards)

**What it is:** whether the algorithm is developed and used in conformance with **generally accepted
ethical standards.**

**Questions to ask:** Does its use conform to accepted ethical standards — e.g., the **Standards**, the
**SIOP Principles**, the **OECD Principles on AI**, and the **UGAI**?

**Apply it (focal example):** What ethical standards do the developers **claim** to have followed? Is
there **evidence of decisions actually made** following that framework? What evidence is there that
**individual fairness was a priority** during development?

**Audit emphases:**
- Distinguish **professed** standards from **demonstrated** adherence — require traceable decisions,
  not a values statement.
- For psychologists, the **APA Ethics Code** binds the work (beneficence/nonmaleficence,
  fidelity/responsibility, integrity, **respect for rights and dignity**, **justice/minimizing one's
  own bias**) — see `ai-fairness-lenses`, Lens 2.
- AI-specific codes (OECD, UGAI) reference fairness/reliability/validity but **don't define them
  precisely** — so "we follow UGAI" is not self-certifying; check what was actually done.

## Component 12 — Research designs

**What it is:** the **methodological quality of the studies** offered to support *any* claim — the
integrity check underneath everything.

**Questions to ask:** How do the **research designs** (sampling, experimental design, variable choices,
analysis, interpretation) of any supporting studies **affect the validity of the conclusions**?

**Apply it (focal example):** For **every claim that appears to rest on empirical observation**, does
the **study design support the claim**? Were all design decisions **defensible from the perspective of
modern methodological research**? What **impact** might they have had on the validity of the
conclusions?

**Audit emphases:**
- This is where the auditor applies standard **research-methods scrutiny** to the developer's own
  validation studies: sampling adequacy, confounds, appropriate analyses, defensible interpretation.
- It pairs with the **psychometric** evaluation in `ai-model-outputs-audit` — Component 12 asks whether
  the *study that produced* the validity/reliability evidence was itself sound.
- An audit's own credibility also rests here: **failing to articulate the standards** by which the
  audit was conducted can make its results uninterpretable.

## Pitfalls

- Treating culture/ethics/research-integrity as an afterthought instead of cross-cutting checks.
- Accepting a values statement as proof of ethical adherence.
- Missing cross-cultural transfer risk for a model moved between contexts.
- Auditing reported results without auditing the **design** that produced them.
- Ignoring power differentials that prevent candidates from contesting or understanding decisions.

## Checklist

- [ ] Power differentials among designers/employers/candidates named
- [ ] Cultural assumptions and cross-cultural transfer risks evaluated; adjustments verified
- [ ] Community participation in design assessed
- [ ] Claimed ethical frameworks (Standards/Principles/OECD/UGAI/APA Ethics) identified
- [ ] Demonstrated (not just professed) adherence evidenced via traceable decisions
- [ ] Every empirical claim's underlying study design scrutinized for methodological defensibility
- [ ] Audit's own fairness/measurement standards articulated for interpretability

## See also

`ai-fairness-lenses` (legal/ethical/moral lens) · `ai-audit-planning` · `ai-model-outputs-audit`
(psychometric counterpart to Component 12) · `ai-audit-reporting` ·
`candidate-accommodations` (linguistic/cultural equivalence)

*Source: Landers & Behrend (2023), Table 1 (Components 10–12, "Meta-components").*
