# Triage result contract

Lead with one permitted status and the label `DRAFT - HUMAN CONFIRMATION
REQUIRED`.

```text
Status: <permitted status>
Record label: DRAFT - HUMAN CONFIRMATION REQUIRED
Enquiry reference: <centre-safe reference; no client name>
Profile: <profile ID, version, status and review due date>
Prepared: <date, time and Australian timezone>

Urgency and safety:
- Observed trigger: <fact or none identified>
- Configured pathway: <pathway and policy ID, or gap>
- Immediate staff action: <action or none>

Conflict-check boundary:
- Status: <passed / pending / uncertain / not started>
- Checked outside model: <yes / not confirmed>
- Further substantive intake permitted: <yes / no / human decision>

Enquiry summary:
- Client-stated problem: <de-identified summary>
- Help sought: <client's requested help>
- Jurisdiction or forum: <supplied facts; do not give a legal conclusion>
- Key dates or next event: <dates and source>
- Access and communication needs: <voluntarily supplied needs>

Configured pathway assessment:
- Supplied fact: <fact>
- Configured rule: <rule ID and source policy ID>
- Provisional assessment: <possible fit / possible mismatch / unresolved>
- Missing information or assumptions: <items>

Proposed next step:
- Internal pathway: <service and staff step, if any>
- Referral: <current profile entry, scope and verification date, if any>
- Consent required: <yes / not applicable>
- No acceptance or availability promise: confirmed

Human decision required:
- Decision owner: <configured role>
- Questions for reviewer: <bounded questions>
- Model output adopted without review: no

Limitations:
- This is a provisional triage aid, not legal advice, a conflict check, a
  merits assessment, a service decision or a client record.
```

## Evidence rules

- Cite profile rule IDs and source policy IDs, not generic legal knowledge.
- Separate the person's account, staff-supplied information, system status,
  model inference and unresolved uncertainty.
- Do not include names, contact details, addresses, dates of birth, document
  numbers or unnecessary third-party information.
- Do not state that no legal right, remedy or service exists merely because the
  configured profile has no matching pathway.
- Do not convert the draft into a client record or send a referral.
