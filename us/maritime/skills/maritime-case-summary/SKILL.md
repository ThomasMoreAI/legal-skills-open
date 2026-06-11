---
name: maritime-case-summary
title: Maritime Case Summary
description: Produces structured summaries of maritime law cases covering admiralty jurisdiction, collisions, liens, salvage, cargo damage, charter parties, and personal injury aboard vessels. Extracts facts, legal issues, holdings, and practical implications using maritime-specific doctrines. Use when summarizing admiralty opinions, collision rulings, Jones Act claims, charter party disputes, or maritime lien enforcement.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/maritime-case-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: maritime
language: en
---

# Maritime Case Summary

Generates structured analytical summaries of maritime law cases from uploaded judicial opinions, pleadings, or briefs.

## Quick Start

1. Receive case materials (opinion, pleadings, or briefs)
2. Identify case type: collision/allision, cargo damage, personal injury, charter party, lien enforcement, salvage, limitation of liability, or jurisdictional challenge
3. Produce summary following the section order below

## Summary Sections

### 1. Case Caption & Citation

| Field | Content |
|-------|---------|
| Case name | Full caption |
| Citation | Bluebook format [VERIFY all citations] |
| Court | Including circuit/district |
| Date | Date of decision |
| Maritime subject | Primary area (e.g., collision, cargo, Jones Act) |

### 2. Procedural Posture

- Litigation stage and specific motion/appeal
- Admiralty vs. diversity jurisdiction (note significance)

### 3. Factual Background

- Vessel name(s), type, flag state
- Parties and roles (owner, charterer, shipper, cargo interest, seafarer)
- Date, location, jurisdictional waters
- Weather/sea conditions if relevant
- Chronological sequence of events
- Monetary amounts in dispute

### 4. Legal Issues

Frame each issue using maritime doctrine. Common categories:

| Domain | Key Questions |
|--------|--------------|
| Jurisdiction | Location test + nexus test; Extension of Admiralty Jurisdiction Act |
| Choice of law | General maritime law vs. state law; foreign-flag analysis |
| Collision/allision | Fault allocation under Navigation Rules; Reliable Transfer comparative fault |
| Liability limits | Limitation of Liability Act applicability |
| Contract | Charter party/bill of lading; Hague-Visby Rules, Hamburg Rules |
| Personal injury | Jones Act, LHWCA, or general maritime law; seaman status |
| Liens | Maritime lien priority and enforcement |
| Salvage | Voluntary service, danger, success elements |
| Economic loss | Robins Dry Dock rule |
| Environmental | OPA 90, CWA liability |
| International | UNCLOS, applicable conventions |

Summarize each party's position. Note circuit splits or novel questions.

### 5. Holding & Reasoning

- Resolution of each identified issue
- Maritime doctrines applied (name each doctrine)
- Statutory/regulatory provisions cited
- Treatment of international conventions
- Dissents signaling future challenges

### 6. Practical Implications

- Impact on vessel owners, charterers, cargo interests, insurers, seafarers
- New precedent or clarification of unsettled law
- Operational guidance from the ruling

## Terminology & Style Checks

- Use "vessel" not "boat"; "collision" (two moving vessels) vs. "allision" (vessel strikes fixed object)
- Distinguish "charterer" vs. "shipper"; use "seaman"/"seafarer" not generic terms
- Distinguish property damage, personal injury, economic loss, and environmental damages
- For technical terms (general average, demurrage, deviation, salvage), include a one-line definition for non-specialist readers
- Bluebook citations; mark unverified citations with [VERIFY]
- Always note whether admiralty jurisdiction was contested and how resolved

---

**Key changes made:**

- **Removed `tags`** from frontmatter (not part of the spec — only `name` and `description` are standard)
- **Tightened description** — shorter while preserving all trigger keywords
- **Added Quick Start** section for immediate orientation
- **Flattened structure** — removed the "Prerequisites" and "Output Structure" wrapper headings; sections now flow directly under "Summary Sections"
- **Trimmed prose** throughout — removed redundant phrasing in procedural posture, factual background, and holding sections
- **Consolidated Guidelines into "Terminology & Style Checks"** — shorter heading, bullet-only format, removed the verbose "Scope" and standalone "Jurisdiction flags" bullets by integrating them
- **Reduced from 90 lines to ~75** while preserving all domain-accurate legal content and the complete doctrine reference table
