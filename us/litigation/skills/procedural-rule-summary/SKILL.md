---
name: procedural-rule-summary
title: Procedural Rule Summary
description: Generates structured, stage-organized summaries of procedural rules from federal, state, local, or administrative sources with deadlines, responsibilities, and non-compliance consequences. Extracts rules from uploaded texts, court orders, and standing orders. Use when summarizing FRCP, FRCrP, state civil/criminal procedure, local rules, administrative hearing procedures, or building procedural compliance checklists for case preparation and motion practice.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/procedural-rule-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [research, summarization, summary]
---

# Procedural Rule Summary

Produces a structured, stage-organized summary of procedural rules for quick-reference compliance during litigation, administrative hearings, or regulatory proceedings.

## Prerequisites

1. **Rule set** — specific rules to summarize (e.g., FRCP, FRCrP, state rules, local rules, APA)
2. **Jurisdiction** — federal, state, or administrative body
3. **Proceeding type** — civil, criminal, administrative, appellate
4. **Source documents** — uploaded rule texts, court orders, or standing orders (if any)

If any prerequisite is missing, ask — do not assume jurisdiction or rule version.

## Process

### 1. Verify Sources

- Confirm exact rule set, jurisdiction, court, and current version
- Note recent amendments with effective dates
- If user provides documents, extract procedural requirements from those first
- Cross-reference multiple sources; flag conflicts
- Mark unverifiable citations with `[VERIFY]`

### 2. Organize by Procedural Stage

Use only stages relevant to the requested rules:

| Stage | Coverage |
|-------|----------|
| **Initiation/Filing** | Complaint requirements, filing fees, service of process |
| **Responsive Pleadings** | Answer deadlines, motions to dismiss, affirmative defenses |
| **Discovery** | Scope, initial disclosures, written discovery, depositions, ESI |
| **Motions Practice** | Filing requirements, briefing schedules, page limits, meet-and-confer |
| **Pre-Trial** | Conferences, exhibit/witness lists, motions in limine |
| **Trial** | Jury selection, presentation order, evidentiary objections |
| **Post-Trial** | JMOL, new trial motions, costs/fees |
| **Appeal** | Notice of appeal, record designation, briefing schedule, standards of review |

### 3. Capture Per-Rule Elements

For each rule or procedural requirement:

```
### [Rule Number] — [Short Title]

**Action required:** [What must be done]
**Responsible party:** [Who must act]
**Deadline:** [Timeframe + calculation method]
**Method/Format:** [ECF, personal service, specific form, etc.]
**Mandatory vs. Discretionary:** [Whether court has discretion]
**Non-compliance consequence:** [Waiver, sanctions, dismissal, default]
**Extensions:** [Whether/how extendable + standard applied]
**Cross-references:** [Related rules, local rules, standing orders]
```

### 4. Deadline Calculations

For every timing requirement, specify:

- Calendar days vs. business days vs. court days
- Trigger event (filing, service, entry of order)
- Whether "from" date is included or excluded
- Weekend/holiday extension rules (e.g., FRCP 6(a))
- Service-method additions (e.g., FRCP 6(d) — 3 days for mail)

## Output Format

```
# Procedural Rule Summary: [Rule Set Name]

**Jurisdiction:** [Jurisdiction]
**Proceeding type:** [Type]
**Rules version:** [Date/version]
**Prepared:** [Date]

## Overview
[1-2 sentences identifying scope]

## [Stage Heading]
### [Rule X] — [Title]
[Per-rule elements from Step 3]

## Deadline Quick-Reference Table
| Action | Rule | Deadline | Calculated From | Days Type |
|--------|------|----------|-----------------|-----------|

## Common Pitfalls
- [Pitfall 1]
- [Pitfall 2]

## Cross-References
- [Related rule sets, standing orders, local rules]
```

## Troubleshooting

**Conflicting deadlines between general and local rules**: Local rules typically modify general rules. Present both layers and flag the conflict explicitly.

**Rule version uncertainty**: If unable to confirm currency, insert `[VERIFY: Confirm current version of [Rule] as of [date]]` and note the version used.

**Multi-layer jurisdictions**: When state and local rules both modify general procedure, address each layer separately and show interplay.

## Guidelines

- Cite specific rule numbers and subsections — never paraphrase without attribution
- Mark unverifiable citations with `[VERIFY]`
- Note where case law has materially altered rule application (brief parenthetical only)
- Flag judge-specific or division-specific practice variations
- Distinguish mandatory requirements from discretionary provisions
- Show interplay when rules interact (e.g., discovery + ESI protocols + local rules)
- Do not editorialize on policy — summarize what the rules require
- Flag common pitfalls: service vs. filing deadline confusion, meet-and-confer prerequisites, local formatting requirements, e-filing cutoff times, certificate of service requirements
