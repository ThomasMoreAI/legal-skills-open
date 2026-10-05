---
name: fair-housing-overlay-theprosperityagent
title: Fair Housing Overlay
description: Foundational compliance skill. Enforces Fair Housing, TCPA, MLS-data-quality, and always-positive rules across every other skill in this repo. Load this skill alongside any other for compliance-first output. Use when ANY content is being generated for an audience the agent doesn't directly control (social, MLS, email, postcards, listing copy).
author: TheProsperityAgent
author_url: https://github.com/TheProsperityAgent/prosperity-real-estate-skills/tree/main/skills/fair-housing-overlay
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
---

# Fair Housing Overlay

The compliance foundation for every other skill in this repo. Load this and Claude will refuse to write copy that violates Fair Housing, TCPA, or MLS data-quality rules — even if the surrounding prompt forgets to mention them.

## When to use this skill

Always. Real estate is one of the most-regulated content categories in marketing. The Fair Housing Act, the Telephone Consumer Protection Act, state real-estate-license rules, and MLS data-quality penalties all overlap. A single offhand line in a listing description, social post, or email can trigger a complaint.

This skill is the always-on safety net. Load it once, and every skill that runs on top of it produces compliant output by default.

## What it does

Adds four rule sets to whatever prompt you run alongside it:

### Rule Set 1 — Fair Housing Act (federal, plus state extensions)

The skill **refuses** to generate any copy that:
- References schools by name, ranking, district, or perceived quality
- Describes a neighborhood by demographic (race, religion, family status, national origin, disability, gender identity, sexual orientation, source of income — covered classes vary by state, this skill uses the union of all federal + state-protected classes)
- Implies steering ("perfect for young professionals", "great for retirees", "ideal for families with kids", "safe neighborhood for kids", "walkable to your church")
- Uses coded language ("up-and-coming", "exclusive", "private", "tight-knit community", "family-friendly")
- Mentions any community amenity in a way that implies a protected-class preference

The skill **rewrites** these patterns into compliant alternatives:
- Schools → location/commute or specific drive times to employers
- "Family-friendly" → specific objective amenities (parks, sidewalks, lot size)
- "Quiet neighborhood" → "low-traffic street" (objective, measurable)
- "Safe area" → no replacement; this phrase is forbidden because safety perception varies by demographic

### Rule Set 2 — TCPA (Telephone Consumer Protection Act)

The skill **refuses** to generate:
- Cold-text or cold-call scripts targeting consumers without prior express written consent
- "Mass blast" SMS templates without an opt-in path
- Auto-dialer-friendly scripts (TCPA explicitly prohibits ATDS without consent)

The skill **redirects** to:
- Opt-in lead-magnet flows
- Owned-channel content (your social, your listings, your website)
- One-to-one personalized outreach (replies to inbound contacts)

### Rule Set 3 — MLS data quality

The skill **refuses** clichés that hurt feed quality and search rankings:
- "Must-see"
- "Won't last"
- "Act now"
- "Rare opportunity"
- "Once-in-a-lifetime"
- "Hidden gem"
- "Show stopper"
- "Priced to sell"

These phrases are filtered out of MLS feeds by major aggregators (Realtor.com, Zillow, Redfin) and reduce listing-page rank in search.

The skill **substitutes** with specific, objective, time-stamped facts: square footage, lot size, year built, school-distance-in-miles, commute-time-to-major-employer.

### Rule Set 4 — Always positive

Cross-platform brand rule. The skill **refuses** to generate copy that:
- Knocks a competing town, neighborhood, or builder
- Knocks a competing agent or brokerage
- Knocks a competing platform (Zillow, Redfin, etc.)
- Frames any market segment as a loser ("buyer's market" / "seller's market" comparisons must be neutral)

The reasoning: in small markets you'll work with the same 50 agents and 5 builders for 20 years. Burning bridges is bad business. The repo's voice is calm, specific, optimistic.

## How to load this skill

In Claude Code:
```
/skill load fair-housing-overlay
/skill load <other-skill-you-want>
```

Or paste the YAML frontmatter and rules above into your conversation as a system-message preamble before any prompt.

## Compliance citations

This skill encodes guidance from:
- [Fair Housing Act 42 U.S.C. 3601 et seq.](https://www.justice.gov/crt/fair-housing-act-1)
- [HUD Advertising Guidance for Real Estate Agents](https://www.hud.gov/program_offices/fair_housing_equal_opp/online-complaint)
- [TCPA 47 U.S.C. 227](https://www.fcc.gov/general/telemarketing-and-robocall-rules)
- [NAR Code of Ethics, Articles 10 and 12](https://www.nar.realtor/about-nar/governing-documents/code-of-ethics)

State-specific extensions (NC, FL, NY, CA) are noted inline in the rule sets above. If your state extends FHA further, add your state's protected classes to the union list.

## Companion content

YouTube Episode 2: [Why Claude Skills Change Real Estate Forever](https://youtube.com/@theprosperityagents)
This episode walks through the four rule sets with real-world before/after examples and explains why compliance is the moat for AI-assisted real estate work.

## Built by

Al & Victoria Pinder · The Prosperity Agent · ICON Agents, eXp Realty
