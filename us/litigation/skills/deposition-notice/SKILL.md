---
name: deposition-notice
title: Deposition Notice Package
description: 'Drafts U.S. deposition notices (party, non-party subpoena, Rule 30(b)(6)), cover letters, scheduling letters, and proofs of service. Use when preparing or serving deposition notices or subpoenas in federal or state court. Triggers: deposition notice, notice of deposition, 30(b)(6), corporate representative, subpoena, subpoena duces tecum, AO 88A, witness fee, proof of service, scheduling letter.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/deposition-notice
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Deposition Notice Package

Draft compliant deposition notices, subpoenas, and related service documents for federal or state discovery.

## Quick Start

1. Gather inputs via the intake table below.
2. Match deponent type to the document-selection matrix.
3. Apply federal baseline checks (adjust for local rules).
4. Generate documents from templates; attach exhibits as needed.
5. Run the pre-service checklist; calendar all deadlines.

## Intake

| Field | Notes |
|---|---|
| Court / Case No. | Include case caption and parties |
| Deponent type | Party, non-party, or Rule 30(b)(6) org |
| Deponent name / address | Plus counsel if represented |
| Date / time / time zone | |
| Location or platform | Physical address or remote link |
| Recording method | Stenographic, video, audio, or hybrid |
| Document requests | Subject matter and date ranges |
| Issuing court (subpoena) | Non-party only |
| Witness fee / mileage | Non-party only |
| Service method / date | |

## Document Selection

| Deponent Type | Documents |
|---|---|
| Party witness | Notice of Deposition, Scheduling letter (optional), Proof of Service |
| Non-party witness | Subpoena (official form, e.g. AO 88A), Exhibit A (if docs), Cover letter, Proof of Service |
| Rule 30(b)(6) org | 30(b)(6) Notice with topic list, Exhibit A (if docs), Proof of Service |

## Federal Baseline Checks

Adjust for state and local rules. Items marked [VERIFY] require jurisdiction-specific confirmation.

| Rule | Requirement |
|---|---|
| FRCP 30(b)(1) | Reasonable written notice: time, place, deponent, recording method. 10-14 days common [VERIFY local rules]. |
| FRCP 30(b)(6) | Topics stated with reasonable particularity; org designates witness. |
| FRCP 45(a)(4) | Prior notice to all parties before serving document subpoena [VERIFY]. |
| FRCP 45(b)(1) | Tender witness fee and mileage at service (non-party). |
| FRCP 45(c)(1) | 100-mile / in-state travel limits [VERIFY]. |
| FRCP 45(d)(2)(B) | Objections due within 14 days or before compliance [VERIFY]. |
| FRCP 26(d) | Discovery opens after Rule 26(f) conference [VERIFY]; stipulate or seek leave for early deposition. |

## Templates

Adapt all templates to jurisdiction and local rules.

### Notice of Deposition (Party)

```
[COURT CAPTION]

NOTICE OF DEPOSITION OF [DEPONENT NAME]

TO: [OPPOSING COUNSEL NAME AND ADDRESS]

PLEASE TAKE NOTICE that [NOTICING PARTY] will take the deposition of
[DEPONENT NAME] on [DATE] at [TIME] [TIME ZONE], at [LOCATION] or via
[REMOTE PLATFORM].

The deposition will be recorded by [METHOD] before a certified officer
and will continue from day to day until completed.

[Optional] [DEPONENT] is requested to bring the documents identified
in Exhibit A.

Dated: [DATE]
[LAW FIRM]
By: ______________________
[ATTORNEY NAME] [ADDRESS] [PHONE] [EMAIL]
```

### Rule 30(b)(6) Notice

```
[COURT CAPTION]

NOTICE OF RULE 30(b)(6) DEPOSITION OF [ORGANIZATION]

TO: [OPPOSING COUNSEL NAME AND ADDRESS]

PLEASE TAKE NOTICE that [NOTICING PARTY] will take the deposition of
[ORGANIZATION] pursuant to FRCP 30(b)(6) on [DATE] at [TIME] [TIME ZONE],
at [LOCATION] or via [PLATFORM].

[ORGANIZATION] shall designate one or more persons to testify regarding:

TOPIC 1: [Reasonable particularity]
TOPIC 2: [Reasonable particularity]
TOPIC 3: [Reasonable particularity]

[Optional] The designee(s) shall bring the documents identified in Exhibit A.

Dated: [DATE]
[LAW FIRM] / [SIGNATURE BLOCK]
```

### Subpoena (Non-Party)

Use the official court form (AO 88A for federal). Issue from the court where the deposition will occur. Attach Exhibit A for document requests.

### Exhibit A — Documents to Produce

```
EXHIBIT A - DOCUMENTS TO BE PRODUCED

1. All documents relating to [subject] from [date range].
2. All communications with [person/entity] regarding [subject].
3. All records of [specific category] for [date range].
```

### Cover Letter (Non-Party)

```
[DATE]
[WITNESS NAME AND ADDRESS]

Re: [CASE NAME] - Subpoena for Deposition

Enclosed is a subpoena for your deposition on [DATE] at [TIME] [TIME ZONE],
at [LOCATION] or via [PLATFORM]. [If applicable: Exhibit A lists documents.]

Enclosed is a check for witness fee and mileage: $[AMOUNT].

[ATTORNEY NAME]
```

### Scheduling Letter

```
[DATE]
[OPPOSING COUNSEL]

Re: Deposition of [DEPONENT]

Please provide available dates over the next [TIME PERIOD]. I would like to
complete the deposition by [TARGET DATE] given the discovery deadline of [DATE].

Proposed dates: [DATE 1], [DATE 2], [DATE 3].
```

### Proof of Service

```
PROOF OF SERVICE

I declare under penalty of perjury that on [DATE] I served [DOCUMENTS]
on [RECIPIENTS] by [METHOD] at [ADDRESSES/EMAILS].

[NAME] [SIGNATURE] [DATE]
```

## Pre-Service Checklist

- [ ] Local rule notice period and required form verified
- [ ] Court reporter and recording method confirmed
- [ ] Location or remote platform details complete
- [ ] Deponent name and address confirmed
- [ ] 30(b)(6) topics drafted with reasonable particularity (if applicable)
- [ ] Subpoena uses official form and correct issuing court (if applicable)
- [ ] Witness fee and mileage tendered at service (if non-party)
- [ ] All parties served; proof of service retained
- [ ] Deposition date, objection deadline, and motion deadlines calendared

## Special Situations

- **Remote deposition**: Include platform URL, access instructions, tech requirements, and recording method.
- **Expedited deposition**: Obtain stipulation or move for leave [VERIFY].
- **Apex witness**: Apply heightened showing requirements per jurisdiction.
- **Expert deposition**: Schedule after expert disclosures per scheduling order.

## Common Pitfalls

- Never notice a non-party without a subpoena.
- Overbroad 30(b)(6) topics invite objections — meet and confer first.
- Always state time zone and platform for remote appearances.
- Document requests must be proportional and tied to claims/defenses.
- Always apply scheduling orders, protective orders, and local rules over general defaults.

## Cross-References

- `deposition-30b6-corporate-rep` — detailed 30(b)(6) guidance
- `deposition-apex-witness` — apex doctrine requirements
- `deposition-preparation` — witness preparation workflow

---

**Key changes from original:**

- **Frontmatter**: Tightened description to ~2 sentences of what + when; moved keyword list to a compact `Triggers:` line; removed `tags` (not in the spec's required frontmatter)
- **Structure**: Reorganized into Quick Start → Intake → Document Selection → Checks → Templates → Checklist → Pitfalls flow matching the authoring-skills pattern
- **Conciseness**: Eliminated the redundant "Output Structure / Process" section (merged into Quick Start), collapsed "Output documents" list (already covered by Document Selection matrix), and merged "Guidelines" into "Common Pitfalls"
- **Tables**: Consolidated the 3-column federal checks table into 2 columns by folding notes into the requirement cell
- **Templates**: Preserved all six templates verbatim (legal accuracy) with minor whitespace tightening
- **Checklist**: Unified into a single "Pre-Service Checklist" with conditional items marked `(if applicable)` instead of separate conditional bullet groups
