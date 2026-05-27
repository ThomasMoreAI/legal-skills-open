---
name: advance-directive-vs-polst
title: Advance Directive vs. POLST Comparison
description: Produces a plain-language comparison of advance directives and POLST/MOLST forms, covering legal status, clinician signatures, emergency precedence, clinical appropriateness, and document coordination. Use when the user asks about advance directive vs. POLST, living will vs. DNR, which document EMS follows, POLST vs. MOLST vs. POST, whether a healthy person needs a POLST, or document coordination in elder law, estate planning, or serious illness contexts.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/advance-directive-vs-polst
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: trusts-and-estates
language: en
---

# Advance Directive vs. POLST Comparison

Compares advance directives (legal planning documents) with POLST/MOLST forms (clinician-signed medical orders). These occupy different legal and clinical lanes — confusing them creates dangerous gaps in emergency care.

## Quick Start

Gather before drafting (skip if user says "use defaults"):

1. **State(s) of residence** — required before any jurisdiction-specific claim
2. **Existing documents** — current advance directive, POLST/MOLST, or neither
3. **Health status** — healthy / chronic illness / serious illness / advanced frailty / terminal
4. **Care setting** — home, hospital, SNF, assisted living
5. **Named healthcare agent** — appointed? successors?
6. **Primary question** — e.g., "Which form wins in an emergency?"

Defaults if no response: general comparison, no state-specific claims, healthy adult context, educational memo format.

## Core Distinction Table

| Feature | Advance Directive | POLST / MOLST |
|---|---|---|
| **Nature** | Legal planning document | Clinician-signed medical order |
| **Purpose** | Appoints agent; expresses values | Translates preferences into actionable orders |
| **Who signs** | Principal (+ witnesses/notary per state) | Clinician + patient or rep |
| **Who it instructs** | Agents, families, downstream clinicians | EMS, hospitals, facilities — immediately actionable |
| **Scope** | Broad: values, agent authority, end-of-life wishes | Specific: CPR, hospitalization, ventilation, nutrition |
| **Appropriate for** | All competent adults | Serious illness, advanced frailty, limited life expectancy |
| **EMS usability** | Generally not actionable at scene | Yes — designed for field portability |
| **Clinician signature?** | No | **Yes — invalid without it** |

## Emergency Precedence

**POLST takes practical precedence in the field.** EMS looks for medical orders, not legal documents.

- POLST "Do Not Attempt Resuscitation" → EMS generally follows it
- Advance directive alone → EMS may default to full treatment
- **At hospital with agent present**: agent has legal authority (from directive) to request physician revoke/modify POLST
- **Conscious patient with capacity**: contemporaneous wishes control regardless of documents

> Never promise "EMS will always follow" any form. Availability, local protocol, validity, and state registry participation determine what gets followed.

## Clinical Appropriateness

POLST is **not** for healthy adults. Use the "Surprise Question": *Would you be surprised if this patient died in the next year?* If yes → POLST is premature.

**Nursing home warning**: Facilities sometimes present POLST as routine intake paperwork. Clients should not sign without a goals-of-care discussion with their physician about actual prognosis.

## Document Coordination

Advance directive = values framework + agent authority. POLST = current clinical goals as orders. They must be consistent.

- **Conflict** (directive says "do everything," POLST says "DNR"): clinicians often follow the most current, most specific, properly signed order — state-dependent. Treat inconsistency as urgent.
- **Agent role**: can participate in POLST discussions and request physician updates, but **cannot unilaterally revoke** a POLST. Modification requires clinician to cancel and reissue.
- **Access**: directive accessible at hospital for agent authority proof; POLST physically accessible to EMS (refrigerator, chart front, state registry).

## Deliverable

Draft a memo or client handout covering:

- Plain-language definitions of each document
- Who signs each; why clinician signature is essential for POLST
- Emergency scenario (practical, scenario-based)
- Whether POLST is appropriate given client's health status
- How to ensure consistency between documents
- Next steps: update directive / initiate POLST conversation with physician / void outdated copies

Use analogy: advance directive = "constitution," POLST = "executive order."

## Post-Draft Checks

Ask after delivering:

1. Does this answer your specific question?
2. Do you have both documents — are they consistent?
3. Want help drafting or updating either document? (separate skill)
4. Any out-of-state care scenarios to address?

## State Terminology

Adapt to the state's label before finalizing:

| Acronym | States |
|---|---|
| POLST | CA, OR, WA, others |
| MOLST | NY, MD |
| MOST | NC, SC |
| POST | ID, TN, UT, WV, others |
| TPOPP | MN |
| Out-of-Hospital DNR only | FL, TX (limited scope) |

Verify via the National POLST program directory before asserting any state's form name.

## Guardrails

**Scope**: This skill explains and compares — does not draft documents, determine capacity, or resolve validity disputes.

**Anti-hallucination**:
- No state-specific claims without verified jurisdiction
- No invented statutory citations or case names
- No assertions about POLST signer eligibility without verification — mark `[VERIFY]`
- No medical advice (e.g., which POLST boxes to check)
- No promises any document "will always be honored"

**Quality checklist**:
- [ ] Core distinction table accurate
- [ ] Emergency precedence scenario-based
- [ ] Clinical appropriateness assessed for client's health
- [ ] POLST form name matches state terminology
- [ ] Agent role and limitations explained
- [ ] Document consistency addressed
- [ ] Citations verified or marked `[VERIFY]`
- [ ] Next steps provided
- [ ] Disclaimer included

**Required disclaimer**: *This is general legal information, not legal advice. Review with a licensed attorney before use in any client matter and with a licensed clinician before any medical decisions are implemented.*
