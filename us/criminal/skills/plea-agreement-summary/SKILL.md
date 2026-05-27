---
name: plea-agreement-summary
title: Plea Agreement Summary
description: Generates structured summaries of criminal plea agreements. Triggers when summarizing plea deals, preparing for plea colloquy, or creating quick-reference digests of negotiated resolutions in criminal defense matters.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/plea-agreement-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: criminal
language: en
tags: [litigation, summarization, summary]
---

# Plea Agreement Summary

Produces a structured quick-reference summary of a criminal plea agreement for attorneys, clients, and court personnel.

## Prerequisites

1. **Plea agreement** — executed or draft
2. **Original charging document** — complaint, indictment, or information (for charge comparison)
3. **Sentencing guidelines** — federal or state, if referenced

## Quick Start

1. Collect the plea agreement and original charging documents.
2. Walk through each output section below, extracting relevant terms.
3. Use tables for charges and sentencing; omit sections with no corresponding content.
4. Run the checklist under Critical Checks before delivering.

## Output Sections

### 1. Case Identification

| Field | Value |
|-------|-------|
| Defendant | Name, DOB, case number |
| Jurisdiction | Court, county/district |
| Prosecutor | Name, office |
| Defense Counsel | Name, firm |
| Date of Agreement | |

### 2. Charges Comparison

| # | Original Charge | Statute | Max Penalty | Plea Charge | Statute | Max Penalty | Disposition |
|---|----------------|---------|-------------|-------------|---------|-------------|-------------|
| 1 | | | | | | | Guilty/Nolo/Dismissed |

Note counts dismissed, reduced, or amended as part of the deal.

### 3. Factual Basis

Summarize defendant's admissions and stipulated facts per plea count. Flag disputed facts or reservations.

### 4. Sentencing Terms

| Term | Details |
|------|---------|
| Incarceration | Duration, concurrent/consecutive, time-served credit |
| Probation/Supervised Release | Duration, conditions |
| Fines | Amount, payment schedule |
| Restitution | Amount, recipients, schedule |
| Community Service | Hours, deadline |
| Special Conditions | Treatment, counseling, geographic restrictions |

- State whether **binding** (11(c)(1)(C)) or **advisory** (11(c)(1)(B)).
- Note joint recommendation vs. prosecution-only cap vs. open sentencing.

### 5. Waivers

Mark each as included or not:

- [ ] Jury trial
- [ ] Appeal conviction
- [ ] Appeal sentence (above/below stipulated range)
- [ ] Post-conviction/habeas relief
- [ ] Suppression motions
- [ ] Other (specify)

Note preserved rights or conditional waivers.

### 6. Cooperation Provisions

If applicable:

- Scope (testimony, debriefings, undercover work)
- Government obligations (5K1.1 motion, immunity, sentence reduction)
- Use limitations on statements (FRE 410 / FRCrP 11(f))
- Safety/protection arrangements

### 7. Collateral Consequences

Flag consequences **explicitly addressed**:

- [ ] Immigration (deportation, inadmissibility)
- [ ] Sex offender registration (tier, duration)
- [ ] Firearm prohibition
- [ ] Professional licensing impact
- [ ] Civil asset forfeiture
- [ ] Voting rights loss
- [ ] Other civil disabilities

### 8. Breach Provisions

- What constitutes breach (new offenses, cooperation failure, false statements)
- Government remedies (reinstate charges, withdraw recommendations, use statements)
- Notice/cure requirements

### 9. Special Provisions

Capture non-standard terms: deferred adjudication, conditional dismissal triggers, sealed provisions, co-defendant coordination.

### 10. Key Dates & Deadlines

| Event | Date/Deadline |
|-------|---------------|
| Sentencing hearing | |
| Restitution payments begin | |
| Compliance reporting | |
| Probation start | |

## Critical Checks

- **Binding vs. advisory** — the single most critical distinction for client counseling. Always state explicitly.
- **Exact figures** — monetary amounts, dates, and statutory citations must be verbatim; never round or paraphrase.
- **Flag ambiguities** — mark unclear or inconsistent provisions with `[AMBIGUOUS — verify with full agreement]`.
- **Immigration silence** — if the agreement omits immigration impact and the defendant may be a non-citizen, flag: `[WARNING: Agreement silent on immigration consequences — Padilla v. Kentucky requires advisement]`.
- **No editorializing** — summarize what the agreement says, not whether terms are favorable.
- **Plain language** — define legal terms parenthetically on first use; keep precise enough for practitioners.

---

**Key changes made:**

- **Description** — trimmed the long enumeration into a concise sentence with clear trigger guidance
- **Added Quick Start** — four-step workflow so the agent knows exactly how to proceed
- **Consolidated Guidelines → Critical Checks** — renamed and tightened into a scannable checklist at the end
- **Trimmed prose** — removed redundant phrasing throughout (e.g. shortened waiver labels, condensed cooperation/breach/special provisions into tighter bullet points)
- **Flattened Special Provisions** — collapsed from a heading + sub-bullets into a single-line summary with comma-separated items
- **Preserved all domain-critical content** — binding vs. advisory distinction, Padilla warning, exact-figures rule, ambiguity flagging, all 10 output sections with their tables and checklists
