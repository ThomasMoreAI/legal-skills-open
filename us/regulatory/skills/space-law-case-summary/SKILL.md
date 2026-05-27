---
name: space-law-case-summary
title: Space Law Case Summary
description: Generates structured summaries of space law cases involving satellite deployment, space debris, orbital conflicts, launch licensing, and international treaty disputes. Synthesizes the Outer Space Treaty, Liability Convention, U.S. Commercial Space Launch Act, FCC/FAA regulations, and ITAR/EAR export controls. Use when summarizing space law disputes, debris liability claims, orbital slot conflicts, or regulatory matters.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/space-law-case-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
---

# Space Law Case Summary

Produces a structured summary of a space law matter for agencies, aerospace companies, satellite operators, and counsel.

## Prerequisites

- Case materials — pleadings, agency decisions, treaty interpretations, or regulatory filings
- Party identification — states, agencies, operators, launch providers, payload customers
- Technical context — orbital parameters, frequency bands, debris data, or launch specs (as available)

## Quick Start

Structure every summary using these sections in order:

1. **Executive Overview** — one-page table
2. **Factual Background** — chronology and technical context
3. **Legal Framework** — applicable treaties, statutes, and soft law
4. **Legal Analysis** — IRAC for each disputed issue
5. **Emerging Issues** — flag unsettled areas
6. **Practical Implications** — operational impact and risk mitigation

## Executive Overview

| Field | Content |
|-------|---------|
| Matter | One-line description |
| Parties | Names + roles (launching state, operator, claimant) |
| Core Legal Issue | Single sentence |
| Outcome / Status | Resolved, pending, or unsettled |
| Key Takeaway | Practical implication for space operators |

## Factual Background

Cover:

- Nature of activity (launch, deployment, on-orbit ops, reentry)
- Orbital regime (LEO, MEO, GEO, cislunar, deep space)
- Technical facts bearing on legal analysis (plain language for non-engineers)
- Chronology of relevant events

## Legal Framework

### International Treaties

Identify which apply; note customary international law where treaty gaps exist.

- **Outer Space Treaty (1967)** — Art. I (freedom of exploration), II (non-appropriation), VI (state responsibility), VII (liability), IX (harmful interference)
- **Liability Convention (1972)** — Art. II (absolute liability on surface/aircraft), III (fault-based in space), V (joint launches)
- **Registration Convention (1975)** — Art. II (registry obligations), VI (identification)
- **Rescue Agreement (1968)** — astronaut return obligations
- **Moon Agreement (1979)** — Art. 11 (common heritage; note limited ratification)

Flag state responsibility under OST Art. VI for private activities.

### National Legislation (U.S.)

- **Commercial Space Launch Act** (51 U.S.C. ch. 509) — launch/reentry licensing
- **FCC regulations** (47 CFR) — spectrum allocation, orbital slots, interference
- **FAA launch licensing** (14 CFR pt. 400+) — safety, financial responsibility
- **ITAR** (22 CFR pts. 120–130) — defense article export controls
- **EAR** (15 CFR pts. 730–774) — dual-use export controls

For non-U.S. matters, identify corresponding national frameworks.

### Soft Law

- UN COPUOS Space Debris Mitigation Guidelines
- ITU Radio Regulations (orbital slot coordination)
- IADC guidelines
- Relevant industry standards

## Legal Analysis

For each disputed issue, follow IRAC:

- **Issue** — one sentence
- **Rule** — treaty article, statute, or regulation with citation
- **Application** — how rule maps to facts
- **Competing positions** — strengths and weaknesses of each party
- **Conclusion** — likely outcome or range of outcomes

### Liability Checklist

```
- [ ] Identify "launching state(s)" per Liability Convention Art. I
- [ ] Classify damage: surface/aircraft (absolute) vs. outer space (fault-based)
- [ ] Assess joint/several liability for multi-party launches (Art. V)
- [ ] Review insurance requirements (national law + contractual)
- [ ] Check indemnification/cross-waiver provisions
```

### Jurisdiction

Address: diplomatic claims vs. domestic court vs. arbitration, forum selection, sovereign immunity, and applicable administrative bodies (FCC, FAA, ITU).

## Emerging Issues

Flag if the matter touches:

- Space resource extraction (Artemis Accords vs. Moon Agreement Art. 11)
- Mega-constellation regulation and orbital sustainability
- Space debris as environmental harm
- Space tourism passenger rights
- On-orbit servicing and active debris removal ownership

Present competing interpretations; do not pick a winner unless well-supported.

## Practical Implications

- Impact on future operations, licensing, or compliance
- Pending regulatory developments to monitor
- Risk mitigation recommendations

## Pitfalls and Guardrails

- Cite specific treaty articles, statute sections, and regulatory provisions — never general references
- Mark unverified citations with `[VERIFY]`
- Explain technical concepts (orbital mechanics, RF interference, delta-v) in plain language
- Maintain neutral, analytical tone — not advocacy
- Note where law is unsettled; do not overstate certainty
- Distinguish binding treaty obligations from non-binding soft law
- **Never reproduce ITAR-controlled technical data**
