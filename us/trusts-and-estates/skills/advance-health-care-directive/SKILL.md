---
name: advance-health-care-directive
title: Advance Health Care Directive
description: Drafts jurisdiction-specific Advance Health Care Directive packages with agent appointment, living will instructions, HIPAA authorization bridge, organ donation preferences, and execution compliance checklists. Trigger when the user mentions advance directive, healthcare proxy, living will, health care agent, HIPAA authorization, medical power of attorney, end-of-life planning, capacity trigger planning, state-specific directive forms, witness/notary requirements for healthcare documents, or cross-state directive portability.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/advance-health-care-directive
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: trusts-and-estates
language: en
tags: [agreement, drafting, transactional]
---

# Advance Health Care Directive

Produces a jurisdiction-aware, clinically actionable directive package — agent appointment, treatment instructions, HIPAA bridge, execution checklist — that an ER team can parse in under 60 seconds and that survives legal challenge. Grounded in state probate/health codes with HIPAA (45 C.F.R. § 164.508) overlay.

Directives fail when they lack state-specific execution formalities (legally void) or use vague language like "no heroic measures" (clinically useless). This skill eliminates both failure modes.

## Quick Start

1. Gather intake (Checkpoint A)
2. Map state law and validate inputs
3. Draft directive sections in fixed order
4. Verify execution compliance
5. Produce final package with front matter
6. Confirm alignment (Checkpoint B)

## Checkpoint A — Pre-Draft Intake

Gather every time unless user says "use defaults" or "just draft":

1. **Jurisdiction** — primary residence state, expected care states, portability needs
2. **Draft scope** — directive + agent + living wishes + revocation + execution; confirm attorney review required
3. **Capacity context** — contested capacity concerns → flag for contemporaneous capacity memo
4. **Client identity** — legal name, DOB, aliases, contact, diagnosis context
5. **Agent architecture** — primary + alternates with contact, availability, conflicts, consent to serve
6. **Treatment preferences** — CPR, ventilation, feeding/hydration, hospitalization goals, comfort care, palliative sedation, religious/cultural restrictions
7. **Existing documents** — prior directives, POLST/MOLST, donor registry, POAs, guardianship orders
8. **Execution logistics** — signing location, notary availability, witness constraints, facility rules, spouse/relative limitations
9. **Conflict screening** — family tensions, beneficiary pressure, undue influence indicators → flag to attorney

**Request**: prior directives, POLST/MOLST, POAs, guardianship orders, organ donation registrations, relevant medical records. If missing, flag explicitly and proceed with labeled assumptions listing "Open Items / Needed Inputs."

**Defaults** (if no response): immediate-authority directive; primary agent + one alternate; comfort-focused treatment; forum-neutral template with state execution formalities marked `[VERIFY JURISDICTION]`; standard HIPAA authorization bridge.

## Step 1 — Validate Intake and Map State Law

Build the jurisdictional scaffold before drafting.

### Intake Validation Table

| Data Block | Required Fields | Verification |
|---|---|---|
| Client profile | Name, DOB, aliases, residence, contact | Spelling consistency across blocks |
| Jurisdiction | Primary state, secondary care states, portability | `[VERIFY]` execution/effectiveness rules per statute |
| Capacity posture | Red flags, physician assessment needs | Flag for contemporaneous memo if risk present |
| Agent chain | Primary + up to 2 alternates, relationships, contact, disqualifications | No disqualified classes under local statute |
| Treatment values | Scenario-based preferences, values hierarchy, palliative directives | No contradictory instructions |
| Legal/medical interfaces | POLST/MOLST, donor registry, prior directives | Reconcile conflicts; harmonized set |
| Execution logistics | Witness sources, notary method, facility constraints | Jurisdiction-specific affidavit/attestation language |
| Delivery plan | Copy recipients (agent, PCP, facilities, portal) | Distribution checklist |

### State-Law Scaffold

| Topic | Confirm |
|---|---|
| Governing statute | Controlling statute + official form/guidance URL |
| Formalities | Witness vs. notary options, count, disqualifications, facility add-ons |
| Trigger mechanics | Springing vs. immediate; incapacity standard; certifying clinician count |
| Substantive scope | Definitions: terminal, incurable, persistent unconsciousness |
| Limitations | Pregnancy restrictions, mental health authority, substance/HIV record limits |
| Revocation | Permitted methods and effective timing |
| Provider protection | Reliance rights for copies/electronic versions; good-faith immunity |

## Step 2 — Draft Directive Sections

Use this fixed section order with clinically interpretable language throughout:

1. **Purpose statement** and effective date
2. **Health care agent appointment** — trigger and scope
3. **Successor agent ladder** — availability/unavailability conditions
4. **Written values statement** and decision-making hierarchy
5. **Treatment instruction matrix** — scenario-based, not abstract
6. **HIPAA authorization bridge** — effective immediately unless state requires otherwise
7. **Organ donation / disposition-of-remains**
8. **Revocation, supersession, and severability**
9. **Provider reliance and transfer obligations** (if conscience objection possible)
10. **Execution block** — signature/witness/notary/acceptance

### Key Drafting Patterns

**Agent appointment**: identify client, appointed agent with relationship and full contact, trigger condition per state law, scope of authority (consent/denial, admission/discharge, transfer, record access). Written instructions control over discretionary choices; unspecified matters use stated values and substituted-judgment standard.

**Successor agents**: each assumes authority only when all prior agents are unavailable/unwilling/disqualified per state rules.

**HIPAA bridge**: authorize agent and alternates to access all PHI immediately upon execution for incapacity determination and care coordination. Scope covers all providers, facilities, labs, insurers. Mark `[VERIFY: 45 C.F.R. § 164.508 and state/Part 2 overlays]`.

**Treatment preferences**: state goals (comfort/pain control, loved-one contact, avoid futile prolonged treatment), then specific positions on CPR, ventilation, artificial nutrition/hydration, hospitalization, comfort care with explicit palliative direction.

**Revocation**: revocable while capable by state-authorized methods; latest version governs; severability clause; copies/electronic versions per state law.

## Step 3 — Execution Compliance Verification

| Item | Required Output |
|---|---|
| Witnessing | Correct count, disqualification screening completed |
| Notary | Form matches state-prescribed language |
| Facility patients | Facility-specific add-ons satisfied (ombudsman/patient advocate) |
| Agent acceptance | Optional acceptance statement included |
| Usability | Key instructions identifiable in <60 seconds (ER context) |
| Internal consistency | No contradiction between agent powers and treatment instructions |
| Review tags | Every statutory claim marked `[VERIFY]` unless confirmed by statute URL |

### State-Specific Flags

- Use state templates/forms where required or recommended
- Flag for attorney: CA facility witness/ombudsman rules, FL witness composition, NY split-instrument systems, TX hospital review for withdrawal over family objections
- Pregnancy limitations and mental-health authority are state-sensitive and case-law unstable

## Step 4 — Produce Final Package

Every output begins with mandatory front matter:

1. **Assumptions Used** — jurisdiction, trigger type, agent chain, treatment posture, key facts
2. **Open Items / Needed Inputs** — missing documents, unresolved questions, unverified citations

### Deliverables

1. Complete advance health care directive document
2. Execution compliance checklist (filled)
3. Distribution plan with recipient list
4. State-specific notes and `[VERIFY]` items for attorney review

## Checkpoint B — Post-Draft Alignment

Ask after delivering the initial package:

1. Does the agent chain and trigger mechanism match client intent?
2. Are treatment preferences correctly stated — especially CPR, ventilation, feeding/hydration?
3. Any family members or situations needing special handling in the values statement?
4. Should the directive harmonize with an existing or new POLST/MOLST?

If no response, recommend next best refinement and proceed if authorized.

## Quality Audit

- [ ] Jurisdiction identified and state-law scaffold completed
- [ ] Agent chain: primary + at least one alternate with full contact
- [ ] Treatment preferences are scenario-specific (no "no heroic measures")
- [ ] HIPAA authorization bridge included with confirmed effective date
- [ ] No contradiction between agent powers and treatment instructions
- [ ] Execution formalities match state requirements (witness count, disqualifications, notary)
- [ ] Portability addressed if multi-state care
- [ ] Every statutory citation verified or marked `[VERIFY]`
- [ ] Assumptions and open items in front matter
- [ ] Key instructions locatable in <60 seconds
- [ ] No invented facts, diagnoses, relationships, or statutory language

## Guidelines

- Never rely on memory for state execution formalities — require statute URLs or official guidance
- Mark unresolved jurisdictional questions `[VERIFY]`; never finalize as final legal language
- Use scenario-specific, clinically interpretable wording; ban vague slogans
- Client instructions override broad surrogate discretion (values hierarchy)
- Treat portability as a design requirement, not a footnote
- Legal structuring only — do not advise on clinical decisions
- Refuse fraud, backdating, or fabrication requests
- **Attorney review required** — include disclaimer and execution-readiness statement
- **Ethics**: Model Rules 1.1 (competence), 1.14 (diminished capacity), 1.6 (confidentiality)
