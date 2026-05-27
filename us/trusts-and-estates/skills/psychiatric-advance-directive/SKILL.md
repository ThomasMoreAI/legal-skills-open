---
name: psychiatric-advance-directive
title: Psychiatric Advance Directive (PAD)
description: Drafts jurisdiction-specific Psychiatric Advance Directives (PADs) capturing treatment preferences, agent authority, and crisis plans for psychiatric incapacity. Trigger when the user mentions psychiatric advance directive, PAD, mental health advance directive, mental health treatment declaration, psychiatric crisis planning, Ulysses clause, psychotropic medication preferences, ECT consent planning, crisis activation plan, or mental health agent appointment.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/psychiatric-advance-directive
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: trusts-and-estates
language: en
tags: [agreement, drafting, regulatory, transactional]
---

# Psychiatric Advance Directive (PAD)

A PAD preserves autonomous psychiatric treatment choices across a capacity gap. It captures medication preferences, agent authority, de-escalation instructions, and crisis contacts in a clinically actionable format — with a first-page crisis summary for intake staff.

> **DRAFT FOR ATTORNEY REVIEW ONLY — Not legal advice. Not execution-ready without jurisdiction-specific verification of statutory formalities, citations, and Ulysses Clause availability.**

## Pre-Draft Intake

Gather before drafting (skip only if user says "use defaults"):

1. **Jurisdiction** — required; controls enforceability, formalities, Ulysses Clause availability. Flag portability limits for multi-jurisdiction use
2. **Clinical history** — diagnoses (with consent), prior hospitalizations, involuntary holds, current medications, allergies/adverse reactions
3. **Agent designation** — primary + alternate: full legal name, address, phone, email, relationship; identify conflicting statutory default surrogates
4. **Exclusions** — persons blocked from agent role or information access (protective/no-contact/restraining orders)
5. **Treatment preferences** — ECT, seclusion/restraint, psychotropic drug classes, de-escalation techniques, voluntary vs. involuntary admission, peer respite, law enforcement involvement
6. **Crisis activation** — early warning signs, sensory/trauma triggers, preferred first contacts
7. **Existing documents** — general AHCD, health care proxy, guardianship orders, prior PAD
8. **Execution logistics** — notary access, witness availability, statutory disinterest rules, agent acceptance requirement

**Defaults if no response:** General PAD framework without jurisdiction-specific formalities; primary agent + one alternate; standard medication structure; marked **NOT EXECUTION-READY**.

## Workflow

### 1. Build Document Architecture

**First-page crisis summary** (intake staff must find key info in <2 minutes):
- Agent name + 24/7 phone
- Top 3 crisis triggers / early warning signs
- Top 3 treatment preferences (including critical refusals)

**Section map:**

| Section | Content |
|---|---|
| Title & Purpose | PAD title; plain-language purpose; conflict-of-directives priority clause |
| Capacity Affirmation | Principal's voluntariness statement; optional clinician attestation |
| Agent Appointment | Primary + alternate with 24/7 contact; statutory incapacity standard; priority over default surrogates; HIPAA authorization |
| Exclusions | Named individuals barred from role or info access |
| Treatment Preferences | Medications, ECT, hospitalization, de-escalation (Step 2) |
| Ulysses Clause | Non-revocation during incapacity — include only if jurisdiction allows (Step 3) |
| Revocation & Updates | Standard revocation; annual review; supersession of prior PADs |
| Crisis Activation | Warning signs; contact ladder (≤2 contacts); what helps client accept care |
| Override Protocol | Facility obligations when PAD cannot be followed |
| Execution Blocks | Principal, 2 witnesses, notary (if required), agent acceptance (if required) |
| Distribution Log | Agent, alternates, providers, hospital systems, patient portals, state registry |

### 2. Draft Treatment Preferences

**Medication structure** — three categories:

- **PREFERRED:** Drug — reason (prior efficacy, tolerability)
- **CONDITIONAL:** Drug — when (specific circumstances only)
- **REFUSED:** Drug — reason (adverse reaction, date) — acceptable alternative

Pair every refusal with an alternative. Include rationale to reduce best-interests override risk.

**ECT:** Explicit consent/refusal/conditional consent with conditions stated.

**De-escalation:** Concrete staff behaviors that help; specific accommodations to try before restraint; trauma triggers.

**Override protocol:** If facility cannot follow PAD: (a) least restrictive alternative, (b) document deviation reason, (c) notify agent promptly, (d) re-review PAD once stabilized.

**HIPAA authorization:** Authorize agent to receive diagnoses, medications, treatment plans, discharge planning. Note: standalone HIPAA-compliant authorization (45 CFR § 164.502 `[VERIFY]`) may be required; state mental health confidentiality laws may impose higher protections.

### 3. Analyze Ulysses Clause

**Do not include if jurisdiction does not recognize non-revocable PADs.** Including in a non-recognizing jurisdiction risks the document being viewed as coercive or legally defective. If unclear, omit and flag for attorney verification.

Reference frameworks `[VERIFY all citations]`:

| State | Framework | Key Notes |
|---|---|---|
| North Carolina | N.C. Gen. Stat. § 122C-71 et seq. `[VERIFY]` | Specific statutory form; deviation may cause facility rejection |
| Texas | Tex. Civ. Prac. & Rem. Code Ch. 137 `[VERIFY]` | "Declaration for Mental Health Treatment"; expires 3 years |
| California | Probate Code § 4701 `[VERIFY]` | General AHCD framework; mental-health provisions appended |
| Virginia | Va. Code § 54.1-2981 et seq. `[VERIFY]` | Agent may overrule contemporaneous protest if PAD authorizes |

**No explicit PAD statute:** Title as "Mental Health Treatment Preferences and Appointment of Health Care Representative for Psychiatric Decisions"; recommend parallel general durable HCPOA.

### 4. Execution & Distribution

- [ ] 2 disinterested adult witnesses — verify statutory exclusions (not agent, not facility staff, not financial beneficiaries)
- [ ] Notarization — jurisdiction-specific
- [ ] Agent acceptance signature — jurisdiction-specific
- [ ] Copies to: agent, alternates, psychiatrist, therapist, case manager, hospital systems, patient portals
- [ ] Check for electronic advance directive registry
- [ ] Wallet crisis card referencing PAD existence and location
- [ ] Date all signatures; supersession clause for prior PADs
- [ ] Annual reaffirmation or review after any hospitalization

## Post-Draft Review

Confirm with user:

1. Medication preferences (preferred/conditional/refused) accurate with correct rationales?
2. Crisis activation section reflects actual warning signs and preferred contacts?
3. Ulysses clause inclusion confirmed with jurisdictional verification?
4. Facility-specific requirements (state hospitals, VA, specific health systems) addressed?

Default if no response: recommend reviewing medication refusal rationales (most common override point).

## Quality Checks

- [ ] First-page crisis summary present and scannable in <2 minutes
- [ ] Agent chain: primary + alternate with 24/7 contact info
- [ ] Medications structured preferred/conditional/refused with rationales
- [ ] Every refusal paired with acceptable alternative
- [ ] ECT position explicit
- [ ] De-escalation preferences concrete and operationally possible
- [ ] Ulysses clause only if jurisdiction supports (verified)
- [ ] Override protocol in cooperative tone
- [ ] HIPAA authorization included
- [ ] All citations verified or marked `[VERIFY]`
- [ ] No operationally impossible demands (convert to ranked preferences)
- [ ] Execution formalities match jurisdiction

## Guidelines

**Ethics:**

| Rule | Application |
|---|---|
| MR 1.14 | If client appears incapacitated at execution, stop |
| MR 1.1 / 1.4 | Research controlling PAD statute; counsel that emergency statutes may override preferences |
| MR 1.6 | Consider omitting diagnoses in favor of functional descriptions given wide distribution |
| MR 1.7 / 1.8 | Flag conflicts: paid caregiver, estranged spouse, financially interested agent |

**Anti-hallucination:**
- Verify every citation via official state code databases; mark unverified `[VERIFY]`
- Never assert "legally binding" without jurisdiction-specific verification
- Replace aspirational language with concrete operational instructions
- Keep preference rationales to 1–2 sentences
