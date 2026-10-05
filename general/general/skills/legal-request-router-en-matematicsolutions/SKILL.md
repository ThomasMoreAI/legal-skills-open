---
name: legal-request-router-en-matematicsolutions
title: Legal Request Router EN - triage for a legal request
description: 'Triage for a legal request. Looks at the question (and optionally the finished deliverable) and decides which verification path to run: plain answer, citation checking, adversarial review, or the full route. Scores complexity and risk and returns a routing decision with its reasoning and an ordered list of skills to run. A layer above the verification layer: it stops routine work from burning tokens on ceremony, and stops high-stakes work from shipping unchecked. Jurisdiction-neutral. Use when: "what should I do with this", "does this need a full review", "which path", "classify this request", "is this high-stakes", "triage", "routing" - at the start of a new legal request, before picking tools.'
author: matematicsolutions
author_url: https://github.com/matematicsolutions/awesome-matematic-skills-en/tree/main/verification-foundation/skills/legal-request-router-en
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Legal Request Router EN - triage for a legal request

## Why this exists

**Not every request deserves the same path.** Summarising a judgment does not need an
adversarial review. An opinion going to a client should not leave without its citations
checked. The router makes one decision at the start and picks a proportionate path: it
saves effort on routine work and forces control where the stakes are real.

This skill **does no legal work and no verification**. It classifies, and it names which
companion skills to run and in what order.

## Workflow

1. **Collect signals** - type of request, whether a deliverable already exists, whether it
   cites sources, who reads it (internal, client, court, regulator), and what a mistake costs.
2. **Classify** against the schema below. Return structure, not prose.
3. **Map to a path** using the decision table.
4. **Return** the decision, the reasoning, and the ordered list of skills.

## Classification schema

```json
{
  "task_type": "direct_answer | citation_check | adversarial_control | full_route",
  "complexity": "low | medium | high",
  "risk": "low | medium | high",
  "has_source_citations": true,
  "audience": "internal | client | court | regulator",
  "needs_citation_check": true,
  "needs_adversarial": false,
  "needs_privilege_preflight": true,
  "path": ["privilege-preflight-en", "citation-extraction-en"],
  "reasoning": "short: why this path"
}
```

## Decision table

`task_type` first, in rising order of control, mapped one-to-one onto a path:

| Input signal | `task_type` | Control path |
|---|---|---|
| No citations, internal reader, low risk | `direct_answer` | no verification |
| Cites sources (judgment, statute, contract), internal reader | `citation_check` | **citation-extraction-en** |
| Reader is client, court or regulator; risk medium or higher | `adversarial_control` | **citation-extraction-en** then **adversarial-legal-review-en** |
| Deliverable leaves the firm, risk high | `full_route` | citation check, then adversarial review, then **output-scoring-en** as the final gate |

Then two flags, independent of `task_type`:

| Signal | Flag | Skill |
|---|---|---|
| Input carries client-identifying facts or material under professional secrecy | `needs_privilege_preflight = true` | **privilege-preflight-en** BEFORE anything else |
| Deliverable leaves the firm, or risk is high | final quality gate | **output-scoring-en** last |

Optional substitutions, when the question is narrower than the whole deliverable:

| Question being asked | Reach for |
|---|---|
| How does this land on a sceptical judge reading it cold? | `judicial-first-impression-en` |
| What will the other side hit first? | `opposing-counsel-attack-en` |
| Does the reasoning actually hold as a syllogism? | `legal-syllogism-en` |
| Are the clauses complete against a checklist? | `clause-checklist-en` |
| Which authority outranks which, across EU sources? | `authority-triage-en` |

## Hard rules

- **Do not escalate routine work.** Low risk plus internal reader means no adversarial
  review, even when one would be possible. A cost gate works in both directions.
- **Do not shortcut high stakes.** A court or client reader plus citations makes the
  citation check mandatory, whether or not the user asked for it. If you decline to
  escalate, say so plainly in `reasoning`.
- **Citation check precedes adversarial review.** Debating unverified citations is
  worthless, so the checking step runs first.
- **Privilege preflight runs first of all.** Before anything reaches an external model.
- **Scoring runs last.** It grades what the earlier steps produced.

## What the router must not claim

`privilege-preflight-en` returns a verdict and can prepare a redacted draft, but it
**does not perform the final redaction** and it sends nothing. A `SAFE` verdict is an
assessment, not a guarantee, and this hub ships no pseudonymisation engine of its own.
Where the path calls for redaction, a human does it or supplies their own tool. The
router names the step; it must never report it as done.

## Output for the user

```
## Routing - <request name>

Type: full_route | Complexity: high | Risk: high | Audience: client

Path, in order:
  1. privilege-preflight-en     (client facts are present - check before any cloud model)
  2. <the legal work itself>    (outside this skill)
  3. citation-extraction-en     (3 case-law citations to verify)
  4. adversarial-legal-review-en (high stakes: opinion going to a client)
  5. output-scoring-en          (final gate before it leaves the firm)

Reasoning: an opinion citing case law, going to a client, high risk, so the full route.
```

## Data protection

The router works on metadata about the request - type, risk, audience - and does not need
to see the full privileged text. When a fragment containing client data is genuinely needed
to classify, run `privilege-preflight-en` on it first.

## AI Act

Picking a proportionate control path operationalises the risk-based approach. The explicit
`risk` value together with `reasoning` records why a given level of control was chosen, which
is the kind of trace that makes oversight by a person possible rather than nominal.

Scope note: Article 14 of Regulation (EU) 2024/1689 requires human oversight of **high-risk**
AI systems. Whether your use falls in that class depends on the deployment, not on this skill,
and this skill does not decide it. The pattern here is useful either way; it is not a claim
that running the router discharges an Article 14 obligation.

## Attribution

Routing pattern inspired by [AnttiHero/lavern](https://github.com/AnttiHero/lavern)
(Apache-2.0, RouterClassification). Schema, decision table and rules written from scratch
against this hub's inventory. English counterpart of `legal-request-router-pl`, rebuilt
rather than translated: the Polish version routes to Polish-law skills that do not exist
here, and this one routes only to skills this repository actually ships.
