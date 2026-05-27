---
name: suppress-evidence
title: Motion to Suppress Evidence
description: Drafts a Motion to Suppress Evidence for criminal defense, challenging admissibility under the Fourth, Fifth, or Sixth Amendment. Trigger when the user needs a suppression motion, exclusionary rule brief, or pre-trial evidence challenge involving warrantless searches, Miranda violations, consent disputes, warrant defects, or fruit of the poisonous tree.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/suppress-evidence
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: criminal
language: en
tags: [drafting, litigation, motion]
---

# Motion to Suppress Evidence

Draft a court-ready motion challenging admissibility of evidence obtained through constitutional violations.

## Prerequisites

1. **Discovery materials** — police reports, body cam transcripts, witness statements, warrant applications, chain-of-custody records
2. **Defendant account** — client's version of the law enforcement encounter
3. **Jurisdiction** — state, county, court division, local rule formatting
4. **Target evidence** — specific items, statements, or derivative evidence to suppress

## Quick Start

1. Analyze case materials and build a fact timeline
2. Identify constitutional grounds (Fourth / Fifth / Sixth Amendment, state analogs, fruit of the poisonous tree)
3. Draft the motion using the required structure
4. Construct legal arguments per ground
5. Apply formatting and citation checks

## Workflow

### Step 1: Case Analysis

Extract from uploaded materials:

| Element | Capture |
|---|---|
| Timeline | Timestamps from initial contact through seizure |
| Officer conduct | Justifications, actions, warnings given |
| Inconsistencies | Conflicts between reports, body cam, witness accounts |
| Custody indicators | Location, restraint, duration, freedom to leave |
| Miranda compliance | Language used, timing, defendant's response |
| Warrant details | Affidavit basis, scope, particularity, execution |
| Consent claims | Who consented, authority, voluntariness, scope |

Flag record gaps — these support arguments that prosecution cannot meet its burden.

### Step 2: Identify Constitutional Grounds

Select all applicable:

- **Fourth Amendment** — unreasonable search/seizure
- **Fifth Amendment** — self-incrimination / Miranda violation
- **Sixth Amendment** — right to counsel violation
- **State constitutional analog** — broader protections than federal
- **Fruit of the poisonous tree** — derivative evidence

### Step 3: Draft Structure

Follow this section order:

**Caption** — court, case number, parties with full legal names.

**Introduction** — moving party, specific evidence to suppress, constitutional grounds previewed. Example: "Defendant moves to suppress the [quantity/description] seized from [location] on [date], and all statements made following arrest, on grounds that [specific constitutional violations]."

**Statement of Facts** — strict chronological order; cite to record materials (report page, timestamp, exhibit); granular detail on each law enforcement action; frame favorably through fact selection, not legal conclusions; note disputed facts with competing source references.

**Legal Argument** — separate headed section for each ground.

**Conclusion** — synthesize arguments; restate specific evidence to exclude.

**Prayer for Relief** — itemize each evidence category; include derivative evidence request; request evidentiary hearing if warranted.

**Certificate of Service / Signature Block**

### Step 4: Legal Argument Construction

#### Fourth Amendment

**Warrant-based — attack on four fronts:**

| Vector | Analysis |
|---|---|
| Probable cause | Affidavit sufficient for neutral magistrate? |
| Particularity | Place and items described with specificity? |
| Scope | Execution exceed authorization? |
| Informant basis | If CI-based: reliability and basis of knowledge? (Illinois v. Gates [VERIFY] totality test) |

**Warrantless — negate each exception:**

| Exception | Elements to Negate |
|---|---|
| Consent | No actual/apparent authority; coerced; scope exceeded |
| Search incident to arrest | No lawful arrest; not contemporaneous; exceeded wingspan |
| Automobile | No probable cause for contraband/evidence |
| Exigent circumstances | No imminent destruction, hot pursuit, or safety threat |
| Plain view | Officer not lawfully present; incriminating nature not immediately apparent |
| Terry stop/frisk | No reasonable articulable suspicion; frisk exceeded pat-down |

#### Fifth Amendment / Miranda

Establish both elements:

1. **Custody** — reasonable person would not feel free to leave (location, officer count, duration, restraint, arrest statements)
2. **Interrogation** — words or actions reasonably likely to elicit incriminating response

Attack waiver validity: warnings incomplete/incomprehensible; waiver not knowing, intelligent, voluntary. Consider age, education, mental capacity, intoxication, LE experience.

#### Sixth Amendment

1. Right attached? (formal charges, preliminary hearing, indictment, arraignment)
2. Deliberate elicitation without counsel present?
3. Valid waiver absent?

#### Fruit of the Poisonous Tree

Trace causal chain from initial violation to each derivative item. Preemptively address:

- Independent source doctrine
- Inevitable discovery
- Attenuation (temporal distance, intervening events, voluntary acts)

#### Good Faith Exception

Preempt by showing officers knew or should have known conduct was unconstitutional, or no reasonable officer could have believed the search/seizure was lawful.

## Checks

- Name exact items, dates, locations, officers throughout — specificity over generality
- Facts section: describe conduct, never label it ("entered without announcing" not "illegal entry")
- Draw factual analogies to favorable precedent; distinguish unfavorable cases on facts
- Citation hierarchy: SCOTUS → Circuit → State high court; verify not overruled
- Bluebook format or jurisdiction-specific citation rules
- Local rules: page limits, font, margins, cover sheets, proposed orders
- Mark unverified citations with `[VERIFY]`
- Include full signature block: name, bar number, firm, address, phone, email
