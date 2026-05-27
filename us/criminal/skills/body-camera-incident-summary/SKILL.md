---
name: body-camera-incident-summary
title: Body Camera Incident Summary
description: 'Transforms police body camera transcripts into structured 10-section legal summaries with timestamp-cited verbatim statements, constitutional issue spotting, evidence inventory, and probable cause articulation. Maintains strict neutrality for all parties. Use when analyzing BWC footage for discovery, pre-trial prep, or trial. Trigger: body camera, BWC, body worn camera, officer footage, use of force review, incident summary.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/body-camera-incident-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: criminal
language: en
---

# Body Camera Incident Summary

Produces a neutral 10-section legal summary from police body camera transcripts. Every factual claim cited `[HH:MM:SS]`. All dialogue verbatim — never paraphrase. Flag recording gaps at point of occurrence.

## Prerequisites

1. **Transcript(s)** — complete BWC transcript(s); load all officer feeds if multiple
2. **Supplemental materials** (optional) — incident reports, dispatch logs, officer statements
3. **Matter phase** — discovery, pre-trial, or trial (affects emphasis)

## Quick Start

1. Ingest all BWC transcripts and supplemental materials
2. Produce sections 1–10 in order below
3. Cite every factual claim `[HH:MM:SS]`; cross-reference timestamps across camera angles for force/search events
4. Flag issues in Section 10 with category tags and recommended next steps

## Output Sections

### 1. Case Information

| Field | Content |
|-------|---------|
| Date/Time | Recording start with time zone |
| Officers | Name, badge, role (primary/backup/supervisor/K-9/FTO) |
| Location | Address or intersection, city, county, state |
| Tracking IDs | Case no., incident no., CAD no. |
| Duration | Final timestamp; note late start or early cutoff |
| Technical deficiencies | Muted segments, obstructed views, interrupted recording |

State absent info explicitly — never infer.

### 2. Executive Summary

4–6 sentences: initiating event (traffic stop, Terry stop, dispatch, warrant, community caretaking), escalation/de-escalation arc, disposition (arrest/cite/release), primary legal issues (4A stop/search, Miranda, Graham v. Connor, qualified immunity).

### 3. Participant Identification

- **Subjects**: name/alias `[timestamp]`, warrants, probation/parole, medical/intoxication indicators
- **Officers**: name, badge, role; FTO/trainee relationship
- **Third parties**: relationship to subject; detained, questioned, or released

### 4. Chronological Timeline

Strict `[HH:MM:SS]` narrative at each inflection point:

| Milestone | Document |
|-----------|----------|
| Initiating event | Articulated basis — violation, RS factors, dispatch info |
| Search discussions | Complete officer dialogue revealing legal theory |
| Detention → arrest | PC statement; formal arrest language |
| Miranda | Verbatim warnings + subject response to each component |
| Each search | Scope, justification, temporal relation to consent/PC |
| Use of force | Commands (exact) → subject response type → force applied → interval → injury/medical |
| Contraband | Legal basis (plain view/consent/SITA/other); ownership claims verbatim |
| Database/dispatch | Warrant hits, effect on PC development |
| Supervisor arrival | Timestamp, stated purpose |
| Evidence collection | On-scene chain of custody actions |

### 5. Constitutional & Procedural Analysis

**4th Amendment**
- Stop validity: traffic (*Whren*), Terry (*Terry v. Ohio*), extension (*Rodriguez*)
- Consent: exact language + response; voluntariness (*Schneckloth v. Bustamonte*)
- PC warrantless: *Carroll* (vehicle); inventory pretext analysis
- SITA: *Gant* (vehicle), *Riley* (cell phone)
- K-9: sniff justification, detention duration, alert description, *Florida v. Harris*

**5th Amendment / Miranda**
- Custody attachment moment; verbatim warnings; flag deviations
- Waiver: knowing/voluntary/intelligent (*Colorado v. Connelly*)
- Invocations: exact language; *Edwards* / *Davis* compliance
- Post-invocation questioning → suppression flag

**Use of Force — Graham v. Connor**
- Severity of crime; immediate threat; active resistance/flight
- Force proportionality; temporal gap (compliance → continued force)
- Contemporaneous justification verbatim; flag post-hoc rationalization

**Arrest Authority** — PC articulation; warrant or warrantless analysis

**Additional**: 1A (recording police), 6A (counsel invocation), state constitutional provisions, *Brady/Giglio* disclosure

### 6. Physical Evidence Catalog

Table per item: description, discovery timestamp, location, legal basis, ownership claims, chain of custody actions.

Detail by type:
- **Controlled substances**: type, form, packaging, field test, weight, use vs. distribution indicators
- **Firearms**: type, make/model, loaded status, serial
- **Currency**: denominations, total, forfeiture warnings
- **Paraphernalia**: items, residue, usable quantities

### 7. Verbatim Statements & Legal Admissions

Format: `"[exact quote]" — [SPEAKER] [HH:MM:SS]`

Organize by category: admissions/inculpatory, exculpatory/denials, rights invocations (note officer response), inconsistent statements (chronological), excited utterances, third-party statements, comprehension/capacity disclosures.

Excerpt lengthy statements with ellipses. Never paraphrase statements bearing on legal interpretation.

### 8. Officer Observations & PC Articulation

| Type | Capture |
|------|---------|
| Olfactory | Odor description, source, fresh vs. burnt; alcohol breath vs. vehicle |
| Visual | Furtive movements, plain view items, impairment indicators |
| Auditory | Slurred speech, concealment sounds, overheard conversations |
| Training/experience | Verbatim interpretations |
| Standardized tests | FSTs, PBT result, DRE findings, refusals |
| Threat/safety | Weapon bulges, posturing, environmental factors |

Reproduce RS/PC articulation verbatim. Flag post-hoc rationalization.

### 9. Disposition & Post-Arrest

- **Arrests**: charges (felony/misdemeanor), enhancements
- **Citations**: violation, court date
- **Releases**: stated reason (may reveal evidentiary weakness)
- **Vehicles**: impound basis, inventory procedures, third-party release
- **Evidence**: lab submissions, safekeeping, currency forfeiture
- **Transport**: destination, medical clearance
- **Post-arrest statements**: Miranda status; patrol vehicle admissions
- **Victims/witnesses**: contact info, injury documentation, protective orders

### 10. Critical Issues for Further Review

Flag each with category tag, specific facts, legal framework, and recommended next step.

| Tag | Issue |
|-----|-------|
| `[SUPPRESS]` | 4A/5A violation → suppression motion |
| `[MIRANDA]` | Equivocal invocation; post-invocation questioning |
| `[FORCE]` | Disproportionate force; Graham excessive force claim |
| `[GAP]` | Audio/video deficiency at critical moment |
| `[CONFLICT]` | Timestamp/narrative inconsistency |
| `[DISCOVERY]` | Brady/Giglio material; informant disclosure |
| `[POLICY]` | Department policy deviation; municipal liability |
| `[WITNESS]` | Bystander location; chain of custody deficiency |
| `[EXPERT]` | Training/certification requiring review |

## Pitfalls

- **Neutrality**: Document inculpatory and exculpatory evidence with equal precision
- **Absent info**: Affirmatively state when data is missing — never infer or speculate
- **Verbatim standard**: Never paraphrase rights invocations, consent exchanges, or admissions
- **Multiple feeds**: Cross-reference timestamps across camera angles for force and search events
- **Jurisdiction**: US federal floor; note state provisions providing greater protection
- **Uncertain citations**: Mark with `[VERIFY]`
