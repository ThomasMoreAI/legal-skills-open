# ROPA Template (Article 30)

The Record of Processing Activities is the controller's (or processor's) inventory of processing operations. Required for organisations with ≥250 employees and most that process special category data, monitor systematically, or process at scale.

## Controller ROPA — required fields (Art. 30(1))

| Field | Notes |
|---|---|
| Name and contact details | Controller; joint controllers; DPO; representative in EU (if applicable) |
| Purposes of processing | One ROPA entry per purpose, not per system |
| Categories of data subjects | E.g., customers, employees, prospects, end-users-of-customers |
| Categories of personal data | E.g., identity, contact, behavioural, location, special category |
| Categories of recipients | Internal teams; processors; third parties; international recipients |
| Transfers to third countries | Country, transfer mechanism, safeguards (SCCs, BCR, adequacy) |
| Retention periods | By data category and purpose |
| Technical and organisational security measures | High-level summary; cross-link to ISMS/SoA |

## Processor ROPA — required fields (Art. 30(2))

| Field | Notes |
|---|---|
| Name and contact details | Processor; controllers on behalf of whom; DPO; representative |
| Categories of processing carried out on behalf of each controller | E.g., hosting, support, analytics |
| Transfers to third countries | Country, transfer mechanism |
| Security measures | High-level summary |

## Single ROPA entry — example (controller)

| Field | Value |
|---|---|
| Activity | Customer support ticketing |
| Purpose | Respond to customer support requests; service improvement |
| Lawful basis | Art. 6(1)(b) — performance of contract |
| Data subjects | Customer end-users |
| Personal data categories | Identity (name, email), interaction content (ticket text, attachments), device/log metadata |
| Special category | None expected; user-submitted content may incidentally contain it — mitigation: filtering and training |
| Recipients | Internal support team; processor X (Zendesk-equivalent); processor Y (transactional email) |
| Cross-border transfers | US (processor X) — SCCs (2021/914) Module 2 + Transfer Impact Assessment (`tia-zendesk-2026-04.md`) |
| Retention | Active tickets: 24 months after closure; deletion via scheduled job |
| Technical/organisational measures | Encryption in transit (TLS 1.2+) and at rest (AES-256); RBAC; quarterly access review (A.5.16); annual processor audit; signed DPA |
| Linked DPIA | None (low risk); reassess if scope expands to AI-powered triage |
| Owner | Head of Customer Support |
| Last reviewed | 2026-04-15 |

## Maintenance discipline

- Review at least annually.
- Update on material change (new vendor, new data category, new geo).
- Pair with the vendor onboarding workflow — new vendor cannot go live until ROPA is updated.
- For processor ROPA, keep a per-controller view (multi-tenant SaaS especially).

## Relationship to other artifacts

| Artifact | Relationship |
|---|---|
| DPIA | One DPIA per high-risk processing activity; cross-reference both ways |
| Privacy notice | Public-facing version of subset of ROPA fields |
| DPA with processors | Each processor in ROPA must have a signed Art. 28 DPA |
| ISMS / SoA | Security measures cross-link to applied controls |
| TIA | One TIA per third-country transfer mechanism + recipient |
