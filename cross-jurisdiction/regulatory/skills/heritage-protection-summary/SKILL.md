---
name: heritage-protection-summary
title: Cultural Heritage Protection Legal Summary
description: Generates structured legal briefings on cultural heritage protection developments. Synthesizes judicial decisions, legislation, treaty updates, and regulatory changes across repatriation, trafficking, armed conflict, underwater heritage, intangible cultural heritage, and indigenous rights. Trigger when producing periodic briefings, policy digests, or thematic research for governments, NGOs, cultural institutions, or international organizations working in cultural property law.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/heritage-protection-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: regulatory
language: en
tags: [research, summarization, summary]
---

# Cultural Heritage Protection Legal Summary

Produces structured briefings on cultural heritage law developments for institutional stakeholders.

## Quick Start

1. **Define scope** — jurisdiction(s), date range, thematic focus (repatriation, trafficking, armed conflict, etc.)
2. **Identify audience** — legal advisors, policy makers, enforcement officials, or repatriation advocates
3. **Gather sources** — case decisions, legislative texts, treaty updates; conduct independent research if none provided

## Workflow

### Step 1: Executive Overview

Open with a ½–1 page summary:
- 3–5 most significant developments in the period
- Jurisdictional snapshot (international / regional / national)
- Emerging conflicts or trends requiring immediate attention

### Step 2: Thematic Sections

Include only sections with material developments:

| Section | Scope |
|---|---|
| Repatriation & Restitution | Artifact return decisions; provenance disputes; good-faith purchaser conflicts |
| Armed Conflict & Emergency | 1954 Hague Convention enforcement; UNSC resolutions; destruction as war crime |
| Illicit Trafficking | Prosecutions; customs seizures; import/export controls; market-state vs. source-state |
| Underwater Heritage | 2001 UNESCO Convention; salvage law conflicts; maritime jurisdiction |
| Intangible Cultural Heritage | 2003 UNESCO Convention; traditional knowledge; IP interface |
| Indigenous Cultural Rights | UNDRIP applications; NAGPRA enforcement [VERIFY recent amendments]; patrimony claims |
| Legislative & Regulatory | New statutes, amendments, administrative regulations |

### Step 3: Case Entries

Per decision, use this structure:

- **Case** — style of cause
- **Court/Tribunal** — name, date, jurisdiction
- **Heritage at Issue** — artifact / site / intangible property
- **Legal Framework** — UNESCO 1970 / Hague 1954 / UNIDROIT 1995 / national law
- **Key Question** — central legal issue
- **Holding** — court's determination
- **Practical Significance** — impact on practice or policy
- **Cross-Jurisdictional Note** — if decision may influence other systems

### Step 4: Trends & Recommendations

- Pattern analysis across developments
- Anticipated litigation or legislation
- Actionable recommendations for stakeholders

## Pitfalls & Checks

- **Flag uncertain citations** with `[VERIFY]` — exclude decisions lacking confirmed dates or courts
- **Do not conflate frameworks** — each has a distinct scope:
  - 1970 UNESCO → illicit trade
  - 1954 Hague → armed conflict
  - UNIDROIT 1995 → private law restitution
  - 2001 UNESCO → underwater heritage
- **Distinguish hard law from soft law** — mark resolutions, guidelines, and model laws vs. binding instruments
- **Flag CIL formation** — note decisions or state practice contributing to emerging customary international law
- **Non-trafficking destruction** — capture heritage loss from development, extractive industry, or climate events
- **Target length** — 3–7 pages; executive overview always leads
