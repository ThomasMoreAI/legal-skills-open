---
name: prompt-pack-client-intake-form-sboghossian
title: Client Intake Form
description: Use when a law firm or in-house legal department needs to create or customise a client intake form for new matters. Captures client identity, matter description, conflict check data, document collection needs, urgency assessment, and initial budget estimate. Applicable across all practice areas and jurisdictions; includes MENA-specific KYC and beneficial ownership fields required under UAE, KSA, and Lebanese AML regulations.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-client-intake-form
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: general
language: en
---

# Client Intake Form

A client intake form is the operational foundation of every legal matter: it captures the minimum information needed to open a file, run conflicts, comply with AML/KYC requirements, and set client expectations. A well-designed form saves hours of follow-up and prevents the firm from inadvertently acting for a conflicted or non-compliant client.

## When to use this

- A law firm or legal department is creating or updating its standard intake form.
- A new client or new matter is being onboarded and a structured questionnaire is needed.
- The firm is implementing a matter management system and needs a standard data schema.
- A compliance audit has identified gaps in KYC or conflict-check data collection.
- The firm operates across multiple MENA jurisdictions and needs a form that captures the regulatory KYC fields required in each.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Law firm / legal department name | Branding and regulatory identification | Ask the user |
| Practice area(s) | Some fields are practice-specific (e.g., real estate requires title search authorization) | Ask the user |
| Jurisdiction(s) of operation | AML/KYC requirements differ materially across MENA | Ask the user |
| Matter type (advisory / contentious / transactional) | Shapes urgency, conflict-check, and budget fields | Ask the user |
| Whether the form is for individual or corporate clients (or both) | KYC fields differ substantially | Ask the user |

## Optional inputs

- Integration with the firm's practice management or CRM system (shapes field naming and data types).
- Whether e-signature or digital submission is supported.
- Whether the form doubles as an engagement letter trigger.
- Specific regulatory requirements (e.g., DFSA, ADGM FSR, UAE MoJ, Lebanon Bar Association rules).

## Form structure

### Section 1 — Client identification

**For corporate clients:**
- Full legal name of the entity (as registered).
- Jurisdiction and date of incorporation.
- Company registration / CR number.
- Registered address and principal place of business.
- Authorized signatory name, title, and authority document (board resolution / PoA).
- Ultimate Beneficial Owner(s) (UBO) — for MENA: UAE AML Law requires disclosure of UBOs with ≥25% ownership; KSA AML regulations require similar disclosure; FATF Recommendations 10 and 24 are the global baseline.
- Group structure chart (if the client is part of a corporate group).
- Tax identification number(s).

**For individual clients:**
- Full legal name (as on passport or national ID).
- Nationality and country of residence.
- Passport or national ID number and expiry date.
- Date of birth.
- Address.
- Source of funds / wealth (required for high-value or financial transactions under FATF standards).
- PEP (Politically Exposed Person) status — required under all GCC AML regulations.

### Section 2 — Matter description
- Brief description of the legal matter (in the client's own words).
- Parties involved (other than the client).
- Relevant contracts or documents already in existence.
- Applicable jurisdiction(s) and governing law.
- Whether the matter is contentious (dispute) or non-contentious (advisory / transactional).
- Any impending deadlines (court dates, regulatory filings, transaction closing dates).

### Section 3 — Conflict check information
This section is the most critical operationally. A conflict not caught at intake can disqualify the firm from acting entirely.
- Names of all parties adverse to the client (individuals and entities).
- Names of all counterparties, even non-adverse (e.g., in a transaction, all parties to the deal).
- Related entities and individuals (parent companies, subsidiaries, affiliates, key individuals).
- Prior involvement with this client or any party at this or any prior firm.
- Whether the matter involves a government entity or regulator (some jurisdictions prohibit acting against government bodies in certain capacities).

### Section 4 — Document collection authorization
- Authorization for the firm to obtain and review documents on behalf of the client.
- List of documents to be provided by the client at intake:
  - Corporate: Certificate of incorporation, MoA/AoA, CR extract, board resolution, UBO register.
  - Individual: Passport/ID copy, proof of address, source of funds documentation.
  - Matter-specific: Relevant contracts, correspondence, prior advice received.
- Acknowledgment that documents will be held in confidence and subject to the firm's data protection policy.

### Section 5 — Urgency and scope assessment
- Urgency: Standard / Expedited / Emergency (with definition of each).
- Estimated matter duration.
- Estimated number of hours / complexity band.
- Whether specialist counsel (local, foreign, or expert) will be needed.
- Whether the matter involves a regulated activity requiring specific authorization (e.g., DFSA-regulated financial advice, property brokerage under RERA).

### Section 6 — Budget and billing
- Client's indicated budget range (optional but recommended for matter scoping).
- Billing arrangement: hourly / fixed fee / retainer / success fee (where permitted).
- Billing contact and invoicing address (may differ from main contact).
- Preferred invoicing currency.
- Payment terms acceptable to the client.
- Whether the matter is covered by legal expenses insurance.

### Section 7 — Regulatory and compliance declarations
Client declarations (checkboxes with signature):
- [ ] The client is not on any applicable sanctions list.
- [ ] The client's funds are from legitimate sources (AML warranty).
- [ ] The client is not a PEP without prior disclosure.
- [ ] The client consents to the firm's data protection and privacy policy.
- [ ] The client confirms they have the authority to instruct the firm on behalf of the entity named above.

### Section 8 — Engagement terms acknowledgment
- Brief summary of the firm's standard terms of engagement (or cross-reference to the engagement letter).
- Signature line for the client representative.
- Date.

## Jurisdictional AML/KYC notes

| Jurisdiction | Key AML/KYC requirements |
|---|---|
| UAE (onshore) | AML Law (Federal Decree-Law No. 20 of 2018); legal professionals are DNFBPs; UBO threshold 25%; CBUAE supervision for financial matters; Ministry of Justice for lawyers |
| UAE (DIFC) | DFSA AML Rulebook; equivalent to FATF standards; CDD required for all clients |
| UAE (ADGM) | FSRA AML Guidance; equivalent requirements |
| KSA | AML Law (Royal Decree No. M/31, 2003, as amended); SAMA regulations for financial institutions; Bar Association guidance for lawyers |
| Lebanon | Law No. 318 of 2001 (AML); special investigation commission supervised by Banque du Liban; high-risk jurisdiction as of 2023 FATF status |
| Egypt | AML Law No. 80 of 2002; Financial Regulatory Authority and Central Bank supervision |

## Common mistakes

- Collecting only the name and email of the contact person — missing the UBO and conflict data that the form really needs.
- Using a generic template that does not capture MENA-specific AML fields (UBO at 25% threshold, PEP status, source of funds).
- Failing to link the intake form to a formal conflict-check process and sign-off procedure.
- Not including an urgency field — this is the single most common cause of mis-scoped matters and fee disputes.
- Omitting a data protection acknowledgment, which is required under UAE PDPL and DIFC/ADGM data protection law.

## Related skills

- [[prompt-pack-contract-playbook]]
- [[prompt-pack-delegation-of-authority-matrix]]
- [[prompt-pack-code-of-conduct]]
- [[prompt-pack-legal-engagement-letter]]
- [[prompt-pack-data-processing-agreement]]
