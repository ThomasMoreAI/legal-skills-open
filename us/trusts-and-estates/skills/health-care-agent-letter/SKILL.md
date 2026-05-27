---
name: health-care-agent-letter
title: Instruction Letter to Health Care Agent
description: Drafts a non-binding instruction letter (values letter / legacy letter) from a client to their designated health care agent, translating personal values, quality-of-life thresholds, and scenario-based treatment preferences into operational bedside guidance for substituted judgment. Trigger when the user mentions values letter, legacy letter, instruction letter to healthcare proxy, substituted judgment guidance, supplementing an advance directive with personal guidance, or communicating treatment wishes to a designated agent. Also trigger for family conflict around medical decision-making authority.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/health-care-agent-letter
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: trusts-and-estates
language: en
tags: [drafting, letter, transactional]
---

# Instruction Letter to Health Care Agent

Non-binding, client-voiced letter that supplements formal advance directives with operational guidance a health care agent can use at the bedside. Not a legal document — the most important supplement to one. In "clear and convincing evidence" jurisdictions (e.g., New York), the letter also serves a critical evidentiary function.

**ATTORNEY REVIEW REQUIRED** — Draft must be reviewed by a licensed attorney before use.

## Quick Start

1. Run pre-draft intake (Checkpoint A)
2. Frame letter and harmonize with legal documents
3. Translate values into decision-making principles
4. Draft scenario-based treatment guidance
5. Address religious/spiritual/cultural commitments
6. Establish agent authority and conflict management
7. Draft closing and distribution plan
8. Run post-draft alignment (Checkpoint B)
9. Run quality audit

## Checkpoint A: Pre-Draft Intake

Gather before drafting (apply labeled defaults if user says "use defaults" or doesn't respond):

| Topic | Gather | Default |
|---|---|---|
| Executed documents | HCPOA/proxy, living will, POLST/MOLST, HIPAA auth, organ donation. If unavailable, frame letter as "pending harmonization with signed directives" | Supplement to existing directive |
| Identity & audience | Client name; primary agent + alternates (names, relationships); share now or upon incapacity | Primary agent audience |
| Medical context | Major diagnoses, chronic conditions, hospitalizations, cognitive baseline, formative experiences (e.g., caring for parent with dementia) | — |
| Values & tipping points | What makes life meaningful; independence definitions; cognitive thresholds; longevity vs. comfort; pain/sedation/dependence tolerance; home vs. facility | Comfort-focused |
| Treatment preferences | CPR, ventilator, dialysis, feeding tubes, antibiotics, major surgery, time-limited trials, palliative sedation | Moderate detail |
| Religious/spiritual/cultural | Rituals, sacraments, clergy contacts, dietary restrictions, modesty, doctrinal positions | — |
| Family dynamics | Likely objectors, communication wishes, conflict preferences, who to inform | — |
| Tone | Intimate, direct, spiritual, humorous, formal | Warm but direct |

## Step 1: Frame Letter and Harmonize with Legal Documents

| Element | Requirement |
|---|---|
| Governing documents | Identify by name and date (or `[DATE]` placeholder) |
| Non-binding statement | Letter supplements, does not supersede, formal directives |
| Substituted judgment | Tell agent: "You are being my voice, not making your own choice" |
| Terminology | Mirror client's executed forms (Health Care Proxy / Medical POA / Advance Health Care Directive) |

Template opening:

> "This letter is not a legal document and does not replace my [Health Care Power of Attorney / Advance Directive dated ______]. I wrote it to help you understand what matters most to me so that, if you ever have to speak for me, you can make decisions the way I would make them."

- Flag any discrepancy between letter and signed directives for attorney review
- Never present as binding instructions

## Step 2: Translate Values into Decision-Making Principles

Address the three functional thresholds driving most bedside decisions:

| Threshold | Question |
|---|---|
| Cognitive function | What level of awareness/recognition is essential? |
| Physical independence | What dependence is tolerable vs. unacceptable? |
| Pain experience | What is the comfort vs. alertness tradeoff? |

- Address dementia stages specifically — use plain language, not clinical scales
- Distinguish temporary impairment (post-surgical delirium) from permanent loss (advanced dementia)
- Pair every values statement with a concrete scenario

## Step 3: Draft Scenario-Based Treatment Guidance

For each category, state general preference + conditional scenarios:

| Category | Cover |
|---|---|
| CPR and intensive care | Frailty context vs. otherwise healthy |
| Breathing machines | Short trial vs. indefinite support |
| Feeding tubes | Temporary recovery aid vs. permanent dependence |
| Infections and antibiotics | Curative vs. comfort-only contexts |
| Pain control and sedation | Comfort priority even if life-shortening |
| Time-limited trials | Duration, reassessment criteria, who decides to stop |
| Hospice and care setting | Home vs. facility preferences |
| Sensory/environmental | Music, touch, outdoors, lighting |

- Frame as guidance ("If my doctors believe… then I would prefer…"), not rigid orders
- Empower agent to ask: "What are best/worst outcomes? What does recovery look like? What if we do nothing?"
- Never draft to resemble a POLST/MOLST — recommend as separate clinical/legal workflow

## Step 4: Address Religious, Spiritual, and Cultural Commitments

- State beliefs in client's own words
- Translate into concrete requests (clergy contacts, sacraments, dietary needs, modesty requirements)
- Address conscientious-objection scenarios: instruct agent on facility transfer if needed
- If religiously significant refusals exist (e.g., blood products), ensure documented in formal legal/medical forms, not just this letter

## Step 5: Establish Agent Authority and Conflict Management

Authorize the agent to:
- Request ethics consults, palliative care consults, family meetings
- Obtain second opinions
- Rely on treating team when consistent with client values
- Make decisions without unanimous family agreement

Template conflict language:

> "You do not need unanimous agreement from the family to follow my wishes. If there is conflict, request a family meeting with the medical team and, if helpful, an ethics consult."

- Name anticipated objectors and reinforce agent authority
- Do not create de facto co-agents by asking multiple people to "decide together"
- Address HIPAA information-sharing boundaries

## Step 6: Draft Closing and Distribution Plan

| Element | Include |
|---|---|
| Gratitude and reassurance | Thank agent; transfer moral responsibility back to client |
| Permission statement | "You are not 'doing this to me,' you are doing this for me" |
| Distribution | Who gets copies; share now or upon incapacity |
| Document location | Where formal legal documents are kept |
| Signature and date | Optional witness/notary for evidentiary weight |

## Checkpoint B: Post-Draft Alignment

Ask after delivering initial draft:

1. Does the letter reflect your voice — would the agent recognize this as you?
2. Are dementia-stage and cognitive-decline preferences correctly stated?
3. Is there anyone who might challenge the agent that we should address more directly?
4. Should this letter be shared now or sealed until incapacity?

If no answer, recommend reviewing dementia-specific guidance (most common gap).

## Quality Audit

- [ ] Governing documents identified correctly (or placeholders used)
- [ ] No contradiction with signed directives (discrepancies flagged)
- [ ] Values are operational — agent can answer: "What would you want if doctors say you won't recover?"
- [ ] No vague phrases ("no heroic measures," "vegetable") — replaced with functional descriptions
- [ ] All facts, dates, relationships are user-provided, not inferred
- [ ] Legal citations verified or marked `[VERIFY]`
- [ ] Dementia-specific guidance included
- [ ] Agent granted emotional/moral authority
- [ ] Adversarial review: no sentence easily weaponized out of context
- [ ] Written at accessible reading level in client's voice
- [ ] Family conflict management addressed
- [ ] Distribution plan included

## Guidelines

**Compliance:**
- **Rule 1.1**: Supplemental narrative only; never imply it changes legal rights
- **Rule 1.14**: If diminished capacity or coercion suspected, advise attorney-conducted capacity-sensitive interview
- **Rule 1.6**: Client decides recipients; warn that medical-record placement makes letter broadly accessible
- **Rules 1.7/1.8(f)**: Do not take instructions from agents or family; flag third-party steering

**Jurisdiction notes:**
- Match terminology to client's executed forms and local usage
- **NY** and "clear and convincing evidence" states (*In re Storar*, 52 N.Y.2d 363 (1981) `[VERIFY]`): draft with heightened specificity
- **CA, TX, FL** and states allowing form attachments: note letter may be incorporated by reference (attorney decision)
- **MAID jurisdictions** (OR, WA, CA, etc.): agent generally cannot request MAID for principal — flag as separate workflow; do not imply agent MAID authority

**Anti-hallucination:**
- Do not invent facts, diagnoses, family relationships, document dates, or religious beliefs
- Do not draft language resembling a POLST/MOLST or medical order
- Do not use legalese ("principal," "attorney-in-fact") in the client-facing letter
- Do not include medical statistics without a citable source
- Do not state the letter is "legally binding"
- Do not invent registry names; ask if a state registry is in use
