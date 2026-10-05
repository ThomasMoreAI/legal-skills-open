# Staff-facing triage protocol

Use this sequence for every enquiry. The approved centre profile controls where
this protocol refers to a configured rule or pathway.

## 1. Run the preflight

Confirm all of the following before processing substantive facts:

- an authorised staff member is operating the workflow;
- the centre profile passes `validate_triage_profile.py --require-approved`;
- the proposed AI environment and data class are approved by the centre; and
- the input contains no unnecessary identifiers or third-party information.

Do not solve a missing profile by relying on general legal knowledge. When an
item fails, do not solicit further substantive facts. If facts already supplied
indicate apparent urgent risk, return `URGENT HUMAN ESCALATION` and direct the
staff member to the centre's authorised urgent procedure. Otherwise return
`HUMAN TRIAGE REQUIRED`.

## 2. Check urgency first

Ask only enough to identify an immediate threat to safety or liberty, a current
detention or custody issue, an imminent court or tribunal event, a limitation or
filing deadline, threatened homelessness, or another trigger expressly listed
in the profile.

Use the matching configured action. Record the trigger and policy ID. Return
`URGENT HUMAN ESCALATION` and stop ordinary triage when the profile requires
immediate escalation.

Do not invent emergency contacts. If an apparent urgent risk has no configured
pathway, return `URGENT HUMAN ESCALATION` and direct the staff member to the
centre's authorised emergency procedure.

## 3. Preserve the conflict boundary

Perform conflict checking only through the centre's authorised process and
outside the model. Do not put names or identifying particulars into the prompt.

Record only:

- status: `passed`, `pending`, `uncertain` or `not started`;
- the authorised system or role that performed the check; and
- the time of the check, if supplied by staff.

If the check is not passed, gather no more substantive information than is
necessary for urgency and safe routing. Return `HUMAN TRIAGE REQUIRED` unless an
urgent escalation takes priority.

## 4. Gather minimum triage facts

Ask one short question at a time. Prefer the person's own description and
record uncertainty instead of translating it prematurely into a legal claim.
Gather only what the centre profile requires, ordinarily:

- the broad problem and the help sought;
- the relevant State, Territory, Commonwealth or other forum connection;
- key dates, documents already received and the next listed event;
- the type of other party without identifying that party; and
- communication, interpreter, disability, cultural-safety or other access needs
  voluntarily identified by the person.

Do not ask for traumatic detail merely to improve a classification. Do not
infer protected attributes, family violence, disability, capacity or financial
circumstances. Ask an approved question directly when the profile makes it
necessary and explain why it is being asked.

## 5. Compare with configured rules

Compare each relevant fact with the exact service area, jurisdiction,
eligibility factor or exclusion in the profile. For each conclusion, record:

- supplied fact;
- configured rule and source policy ID;
- provisional assessment;
- missing fact or assumption; and
- human decision required.

Do not assess legal merits, credibility, prospects, evidence quality or whether
the centre should form a lawyer-client relationship.

## 6. Select the status

Apply this priority order:

1. `URGENT HUMAN ESCALATION` for a configured or unresolved immediate risk.
2. `HUMAN TRIAGE REQUIRED` for a failed preflight, incomplete conflict check,
   profile gap, ambiguity, complexity or required professional judgment.
3. `INSUFFICIENT INFORMATION` when a bounded factual gap prevents routing.
4. `PROVISIONAL SERVICE PATHWAY` when a configured service may fit, subject to
   human confirmation.
5. `OUTSIDE CONFIGURED SCOPE` when the supplied facts clearly do not match the
   approved profile, subject to human confirmation and referral review.

Never substitute `eligible`, `ineligible`, `accepted`, `rejected` or a merits
rating.

## 7. Prepare a safe pathway or referral

For a possible internal pathway, name the service type and the next staff step.
Do not promise an appointment or acceptance.

For a referral:

- use only a current profile entry;
- explain the verified scope and any known access method;
- state that availability and acceptance remain with the receiving service;
- obtain consent before a warm referral or information transfer; and
- avoid transferring the triage narrative unless authorised and necessary.

## 8. Hand the draft to staff

Use the result contract. Label the record `DRAFT - HUMAN CONFIRMATION REQUIRED`.
Ask the authorised staff member to confirm, vary or reject the proposed pathway
before any client-system entry, advice, appointment, rejection or referral.
