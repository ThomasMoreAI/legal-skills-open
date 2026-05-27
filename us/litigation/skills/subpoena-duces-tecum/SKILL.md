---
name: subpoena-duces-tecum
title: Subpoena Duces Tecum
description: Drafts a Subpoena Duces Tecum compelling document production without testimony under Federal Rule 45 or state equivalents. Covers recipient designation, records scoping, production format, privilege notices, and service certification. Trigger when drafting records-only subpoenas, third-party document discovery, or duces tecum commands in litigation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/subpoena-duces-tecum
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [drafting, pleading]
---

# Subpoena Duces Tecum

Drafts an enforceable subpoena compelling production of documents or records from a party or non-party, without requiring personal appearance.

## Required Inputs

1. **Case identifiers** — party names (as captioned), case number, court with division/judge
2. **Recipient** — full legal name, title, service address; for entities: custodian of records or registered agent
3. **Target records** — document categories, date ranges, identifying details (account numbers, transaction dates, names)
4. **Jurisdiction** — federal (Rule 45) or state rules; applicable local rules
5. **Special considerations** — HIPAA-covered entities, financial institution privacy rules, government agency protocols, out-of-state service

## Workflow

### 1. Court Header and Caption

- Full court name with division
- Caption matching operative pleadings exactly
- Case number with judge/division designation
- Formatting per local rules (font, margins, spacing)

### 2. Issuing Attorney Block

- Name, firm, address, phone, email, bar number
- Authorizing rule citation (Fed. R. Civ. P. 45 or state equivalent)
- Confirm whether jurisdiction requires clerk issuance vs. attorney issuance

### 3. Recipient Designation

- Complete legal name and title/position
- Entity recipients: custodian of records or designated agent with registered entity name
- Service address verified against case documents and public records

### 4. Command Language

Draft command that compels production **without personal appearance** and specifies:

- **Production method** — physical delivery (address, access instructions), electronic transmission (secure method, format: native/PDF/TIFF, metadata preservation), or on-site inspection (location, hours, copying arrangements)
- **Organization** — records labeled by request category; Bates numbering if appropriate

### 5. Records Description

For each category specify:

- Date range (exact start and end dates)
- Subject matter with specific description
- Identifying details (account numbers, names, transaction IDs)
- Format (paper, ESI, native files)

**Per-category checks:**
- Time-bounded with exact dates
- Specific enough for recipient to identify responsive records
- Not so broad as to invite overbreadth objection
- Covers "possession, custody, or control"
- ESI addressed explicitly if applicable (emails, texts, databases, deleted files, backups, metadata)

### 6. Compliance Terms

- **Production date** — minimum notice period (14 days under Rule 45; verify state equivalents)
- **Production location/method** — full address or electronic delivery instructions
- **Contact** — issuing counsel's phone and email
- **Accommodation** — alternative methods or rolling production for voluminous records

### 7. Rights and Obligations Notice

- Objection right with deadline per applicable rule
- Motion to quash/modify procedure and court
- Privilege assertions (attorney-client, work product, physician-patient) with privilege log requirements and in camera review option
- Protective order availability for confidential/proprietary information
- Preservation duty upon receipt regardless of intent to object
- Non-compliance consequences: contempt, sanctions, compelled compliance, adverse inferences

### 8. Execution Block

- Signature line: attorney name, date, bar number, firm, full contact
- Certificate of service: method, date, recipients; jurisdictional certification compliance
- Verify acceptable service methods (typically personal service by non-party 18+, notice to all parties)

## Pitfalls and Checks

- **Records only** — exclude any appearance or deposition language; this is not an ad testificandum subpoena
- **Scope discipline** — each category must tie to a specific claim or defense; avoid fishing expeditions
- **Anticipate objections** — draft descriptions that survive overbreadth, undue burden, and relevance challenges; reference specific case events where possible
- **Rule 45 compliance** — verify current rule text for geographic reach limits, notice requirements, and issuing-court rules [VERIFY exact current amendments]
- **HIPAA/financial records** — include authorization forms or statutory basis when subpoenaing medical or financial records
- **Party notice** — most jurisdictions require advance notice to all parties before or concurrent with service on non-party recipients
- **Consistency** — party names, case numbers, and dates must be identical throughout
- **Tone** — authoritative but not adversarial
