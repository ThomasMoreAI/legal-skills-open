---
name: privacy-law-updates
title: Privacy Law Updates
description: Generates structured privacy and data protection law briefings across US, EU, UK, and other jurisdictions. Organizes by jurisdiction with compliance deadlines, enforcement actions, and legislative changes. Use when preparing privacy law briefings, compliance updates, regulatory change summaries, or data protection landscape reviews.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/privacy-law-updates
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: en
---

# Privacy Law Updates

Produces a structured briefing on recent privacy and data protection developments, oriented toward compliance planning and executive decision-making.

## Quick Start

Confirm before generating:

1. **Reporting period** — default: past 12–18 months
2. **Jurisdictions** — default: US federal + state, EU/EEA, UK
3. **Industry context** — platform type, data categories, cross-border transfers
4. **Audience** — legal/compliance, executive, or both

## Output Workflow

### Step 1: Executive Overview

| Element | Content |
|---|---|
| Critical deadlines | Compliance dates requiring immediate action |
| Major enforcement | Fines/orders signaling regulatory priorities |
| New obligations | Requirements not previously in effect |
| Strategic flags | Developments affecting product roadmap or vendors |

### Step 2: Jurisdiction Developments

For each jurisdiction, use this entry template:

```
### [Jurisdiction]

#### [Development Title]
- **Type**: Legislation | Guidance | Enforcement | Court Decision
- **Effective date**: [date or timeline]
- **Scope**: [entities, data types, activities covered]
- **Key requirements/holdings**: [bullet list]
- **Delta from prior law**: [what changed]
- **Operational impact**: [systems, processes, documentation affected]
- **Penalties**: [non-compliance consequences]
- **Exemptions/safe harbors**: [if any]
```

### Step 3: Cross-Cutting Topics

Cover only topics with material developments:

| Topic | Capture |
|---|---|
| Cross-border transfers | New mechanisms, adequacy decisions, SCCs updates |
| Consent & notice | Changed standards, dark-pattern enforcement |
| Data subject rights | Access, deletion, portability changes |
| Breach notification | Amended timelines, reporting thresholds |
| AI governance | Automated decision-making rules, transparency mandates |
| Children's privacy | Age verification, parental consent, design codes |
| Biometric data | New state/national laws, consent requirements |

### Step 4: Forward-Looking

- Pending legislation with expected timelines
- Open regulatory consultations
- Announced DPA enforcement priorities
- Areas of legal uncertainty warranting monitoring

## Checks and Pitfalls

- **Jurisdiction-first organization** — cross-reference in cross-cutting section; never repeat the same development twice
- **Cite primary sources** — statute sections, regulation articles, case names, DPA decisions
- **Mark unverified citations** with `[VERIFY]`
- **Distinguish enacted law from proposals** — clearly label pending/proposed items
- **Flag jurisdictional conflicts** where requirements create operational tension
- **Include enforcement amounts** — fines contextualize regulatory seriousness
- **No editorializing** on political likelihood; state procedural status only
- **Note sector carve-outs** (HIPAA, GLBA, COPPA, ePrivacy) where they interact with general frameworks
- **Dual-audience tone** — precise for compliance implementation, clear for executive briefing
