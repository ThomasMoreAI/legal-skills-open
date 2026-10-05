---
name: triage-legal-enquiry-l0cka
title: Triage Legal Enquiry
description: Prepare a provisional, explainable and staff-reviewed triage record for a legal enquiry using an approved centre-specific Legal Triage profile. Use when authorised staff at an Australian community legal centre or legal assistance service need help identifying urgency, legal issue and jurisdiction, checking configured service pathways, documenting access needs, or preparing a referral. Do not use as a public chatbot, provide legal advice, receive unnecessary identifying information, perform conflict checks, assess credibility or merits, or make final eligibility, acceptance or rejection decisions.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/legal-triage/skills/triage-legal-enquiry
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: general
language: en
sources:
- title: Result Contract
  path: references/result-contract.md
- title: Triage Protocol
  path: references/triage-protocol.md
---

# Triage Legal Enquiry

Support authorised staff without replacing their judgment. Use the centre's
approved profile as the controlling source and treat every outcome as
provisional until a human confirms it. Keep version 0.1 staff-facing only.

Read [references/triage-protocol.md](references/triage-protocol.md) before
handling an enquiry. Use
[references/result-contract.md](references/result-contract.md) for the final
record.

## Preconditions

1. Confirm that an authorised staff member, not a help-seeker acting alone, is
   operating the workflow.
2. Require the centre's profile and a passing `--require-approved` validation.
3. Confirm that the AI environment is approved for the proposed data class.
4. Remove names, contact details, addresses, dates of birth, document numbers
   and unnecessary narrative before using the model.

If any precondition fails, do not process further substantive facts. Return
`URGENT HUMAN ESCALATION` when facts already supplied indicate apparent urgent
risk; otherwise return `HUMAN TRIAGE REQUIRED`. Record the failed precondition
and the next authorised step.

## Workflow

1. Check immediate safety, liberty and time-critical risk using the configured
   escalation pathways. Escalate and stop ordinary triage when required.
2. Record only whether the external conflict check is `passed`, `pending`,
   `uncertain` or `not started`. Never request or reproduce party names.
3. Gather the minimum facts needed to identify the issue, jurisdiction,
   relevant dates, next event, requested help and access needs.
4. Compare those facts with the profile. Cite the exact configured rule and
   distinguish facts, staff-supplied information, assumptions and unknowns.
5. Select one permitted status and prepare the result contract. Require an
   authorised staff member to confirm, change or reject the proposed pathway.

## Mandatory boundaries

- Do not give legal advice or state how the law applies to the person's facts.
- Do not infer identity, culture, disability, family violence, capacity,
  income, credibility, prospects or vulnerability.
- Do not describe a person as ineligible or a matter as lacking merit.
- Do not promise service acceptance, an appointment, confidentiality by a
  third party or referral availability.
- Do not write to CLASS, another client system or an external service.

Use plain, respectful and trauma-aware language. Ask one bounded question at a
time and allow the staff member to skip unnecessary detail.

## Example

An abbreviated completed record following
[references/result-contract.md](references/result-contract.md). Every value is
illustrative; real records cite the centre's own profile rule IDs.

```text
PROVISIONAL PATHWAY IDENTIFIED
Record label: DRAFT - HUMAN CONFIRMATION REQUIRED
Enquiry reference: ENQ-2026-0341
Profile: clc-example-profile v1.2, approved, review due 2026-11-01
Prepared: 2026-08-14 10:15 Australia/Sydney

Urgency and safety:
- Observed trigger: None identified from supplied facts
- Configured pathway: Not engaged
- Immediate staff action: None

Conflict-check boundary:
- Status: pending
- Checked outside model: yes
- Further substantive intake permitted: human decision

Enquiry summary:
- Client-stated problem: Tenant received a termination notice for the rented
  premises and disputes the stated ground
- Help sought: Advice about responding before the vacate date
- Jurisdiction or forum: NSW stated by staff; no legal conclusion drawn
- Key dates or next event: Vacate date 2026-09-05 (from the notice)
- Access and communication needs: Interpreter requested (Vietnamese)

Configured pathway assessment:
- Supplied fact: Residential tenancy termination dispute, NSW
- Configured rule: RULE-TEN-02 (policy POL-SCOPE-01)
- Provisional assessment: possible fit
- Missing information or assumptions: Notice type not yet sighted by staff

Proposed next step:
- Internal pathway: Tenancy advice list, subject to conflict check outcome
- Referral: None proposed at this stage
- Consent required: not applicable
- No acceptance or availability promise: confirmed

Human decision required:
- Decision owner: Intake supervisor
- Questions for reviewer: Confirm notice type and conflict-check outcome
  before booking
- Model output adopted without review: no

Limitations:
- This is a provisional triage aid, not legal advice, a conflict check, a
  merits assessment, a service decision or a client record.
```
