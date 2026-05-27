---
name: telemedicine-consent
title: Telemedicine Consent and Policy Document
description: Drafts dual-purpose telemedicine consent and policy documents covering informed consent, HIPAA privacy architecture, prescribing limitations, clinical scope boundaries, and patient acknowledgment sections. Addresses federal and state telehealth regulations, DEA controlled substance rules, and Interstate Medical Licensure Compact requirements. Use when drafting telehealth consent forms, telemedicine informed consent, remote patient monitoring agreements, virtual care policies, RPM consent documents, or store-and-forward authorization forms.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/telemedicine-consent
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: healthcare
language: en
tags: [agreement, drafting, regulatory]
---

# Telemedicine Consent and Policy Document

## Why This Skill Exists

Telemedicine consent documents fail for two reasons: they omit jurisdiction-specific prescribing and licensure requirements (creating regulatory exposure), or they use boilerplate language that fails informed consent standards because patients don't understand the real limitations of remote care. A consent form that doesn't explain why a provider can't palpate an abdomen over video is legally insufficient. A policy that ignores DEA telehealth prescribing rules invites enforcement action.

This skill produces a dual-purpose document — informed consent instrument and operational policy framework — that satisfies HIPAA privacy requirements, state telehealth regulations, and DEA prescribing rules while remaining accessible to patients at varying health literacy levels.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Gather before drafting unless user says "use defaults":

1. **Provider identity** — legal entity name, professional designations, state licensure details
2. **Jurisdiction** — state(s) where patients are physically located during consultations
3. **Modalities** — synchronous video, asynchronous store-and-forward, RPM devices, mHealth apps
4. **Prescribing scope** — whether controlled substances will be prescribed; if so, which schedules
5. **Billing model** — insurance-based, self-pay, or hybrid
6. **Existing policies** — institutional consent forms, privacy notices, credentialing requirements
7. **Technology platform** — vendor names, encryption standards, BAA status

**Defaults if user doesn't respond**: synchronous video only; no controlled substance prescribing; insurance-based billing; standard HIPAA safeguards; single-state practice. Label all defaults clearly.

---

## Step 1: Draft Consent and Telemedicine Explanation

| Element | Requirements |
|---|---|
| Patient ID | Full legal name, DOB |
| Provider ID | Legal entity, designations, license number |
| Modalities | Enumerate each modality in use with plain-language definition |
| Benefits | Access, convenience, scheduling flexibility, reduced travel |
| Limitations | No physical exam, limited emergency response, technology dependency |

Use plain language — explain telemedicine without jargon while maintaining legal sufficiency for informed consent.

---

## Step 2: Draft Risk Disclosures

Patient must explicitly acknowledge each:

- Cannot perform hands-on examination or palpation
- Limited emergency response during/after sessions
- Transmission interruptions (audio/video)
- Potential unauthorized access despite encryption
- Technical failures requiring rescheduling
- Technology limitations may delay diagnosis

---

## Step 3: Draft Patient Responsibilities

- Private, quiet location free from unauthorized listeners
- Adequate bandwidth and device functionality; test in advance
- Backup communication method available
- Complete, accurate medical history, medications, allergies
- Emergency contact information readily accessible
- Understanding of when to call 911 vs. use telemedicine

---

## Step 4: Draft Privacy and Security (HIPAA)

| Topic | Required Content |
|---|---|
| Encryption | End-to-end for video; encrypted storage for recordings/transmitted data |
| Data retention | Duration, storage location, access controls |
| Session recording | Recording policy, pre-recording notification, patient copy rights |
| Security limits | No absolute guarantee despite administrative/physical/technical safeguards |
| Breach notification | Per HIPAA Breach Notification Rule, 45 CFR §§ 164.400–414 `[VERIFY]` |

---

## Step 5: Draft Regulatory Compliance and Licensure

- Confirm provider licensure in patient's physical location state
- If interstate: address Interstate Medical Licensure Compact or individual state licenses
- Telemedicine held to same standard of care as in-person
- Patient right to file complaints with state medical boards preserved
- If Medicare/Medicaid telehealth: verify current CMS coverage policies `[VERIFY]`

---

## Step 6: Draft Third-Party Participation

- Enumerate who may be present: family, caregivers, interpreters, students, residents, care team
- Patient informed of all participants; may object to any
- Interpretation services at no cost for LEP patients
- Right to refuse telemedicine at any time without prejudice to in-person care

---

## Step 7: Draft Prescribing Policy

| Constraint | Detail |
|---|---|
| Clinical discretion | All prescribing at provider's professional judgment |
| DEA controlled substances | In-person exam generally required for Schedules II–V; note exceptions under 21 USC § 831 `[VERIFY]` |
| State restrictions | Incorporate state-specific rules where more stringent than federal |
| Excluded categories | Medication classes requiring in-person evaluation (opioids, benzodiazepines, stimulants) |

DEA federal rules are the floor — state rules may be stricter. Adapt to jurisdiction.

---

## Step 8: Draft Clinical Scope Limitations

Conditions unsuitable for telemedicine (non-exhaustive):

- Acute chest pain, severe abdominal pain, significant trauma
- Altered mental status
- Conditions requiring palpation, manipulation, or other physical exam techniques
- Presentations requiring immediate diagnostic testing/imaging
- Any situation where standard of care cannot be met remotely

---

## Step 9: Draft Care Coordination and Billing

- Documentation standards match in-person visit requirements
- Records available to other providers with authorization
- Follow-up protocols: in-person triggers, lab/imaging result timelines
- Billing: telemedicine-specific CPT codes and modifiers (no dollar amounts — reference billing department)
- Patient responsible for copays, coinsurance, deductibles, non-covered services
- Cancellation/no-show policy

---

## Step 10: Draft Acknowledgment and Signatures

**Patient certification** — patient certifies:
- Read entire document (or had it read to them)
- Adequate opportunity to ask questions
- Understands nature, benefits, risks, and limitations
- Voluntarily consents
- Understands right to withdraw consent at any time

**Signature blocks**: Patient, guardian/legal representative (if applicable), witness (if required by state law), provider acknowledgment. Include date, printed name, and relationship/authority fields.

**Minor consent**: Require guardian signature; specify state-specific age-of-consent exceptions (reproductive health, mental health, substance abuse treatment) `[VERIFY per jurisdiction]`.

**Electronic signatures**: Must comply with ESIGN Act (15 USC § 7001) `[VERIFY]` and applicable state UETA adoption.

**Savings clause** — include verbatim:

> Execution of this consent does not waive any legal rights or remedies under federal or state law, does not limit the right to file complaints with medical licensing boards or privacy officers, and does not restrict the ability to pursue legal action. This document supplements rather than replaces other consent forms or agreements. In the event of conflict, the interpretation most protective of patient rights and safety prevails.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the draft, ask:

1. Does the prescribing policy match the provider's actual scope?
2. Are the modalities listed correct and complete?
3. Are there state-specific requirements not yet addressed?
4. Should the document be harmonized with existing institutional policies?

If user doesn't answer, recommend the highest-priority refinement and proceed if authorized.

---

## Quality Audit

Before finalizing, verify:

- [ ] Jurisdiction identified and licensure requirements addressed
- [ ] All modalities in use are enumerated and explained in plain language
- [ ] Risk disclosures explicit and formatted as patient acknowledgments
- [ ] HIPAA privacy section covers encryption, retention, breach notification
- [ ] Prescribing policy adapted to jurisdiction (federal floor + state overlay)
- [ ] Clinical scope limitations included with non-exhaustive list
- [ ] Savings clause included verbatim
- [ ] Signature blocks appropriate for context (including minor consent if applicable)
- [ ] Every statutory citation verified or marked `[VERIFY]`
- [ ] No fee schedules or specific dollar amounts
- [ ] No invented statutory language, regulatory citations, or jurisdiction-specific claims

---

## Guidelines

- Active voice throughout; plain language accessible to varying health literacy levels
- Define technical terms on first use
- Do not include fee schedules or dollar amounts — reference billing department
- Mark any unverified statutory citation with `[VERIFY]`
- Do not rely on memory for state-specific telehealth regulations — verify or flag
- Do not provide clinical advice — this is legal/regulatory structuring only
- **Attorney review required** — include disclaimer in final output
