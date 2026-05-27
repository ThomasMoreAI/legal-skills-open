---
name: certificate-of-withdrawal-foreign-corp
title: Certificate of Withdrawal — Foreign Corporation
description: Drafts a Certificate of Withdrawal for a foreign corporation surrendering its authority to transact business in a US state. Use when a foreign corporation is withdrawing its certificate of authority, ceasing in-state operations, or completing dissolution in a non-home jurisdiction.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/certificate-of-withdrawal-foreign-corp
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [drafting, research]
---

# Certificate of Withdrawal — Foreign Corporation

Statutory filing by which a foreign corporation surrenders its authority to transact business in a US state jurisdiction.

## Required Inputs

1. **Corporation details** — legal name (exactly as on certificate of authority), home state/country, incorporation date
2. **Certificate of authority** — authorization date, certificate number (if applicable), any DBAs
3. **Registered agent** — name and address in the withdrawal state
4. **Tax clearance status** — whether the state requires a clearance certificate or final returns
5. **Authorizing resolution** — board consent or resolution authorizing withdrawal
6. **Withdrawal state** — requirements vary significantly by jurisdiction

## Workflow

### 1. Gather & Verify State Requirements

Check the withdrawal state's Secretary of State website and statutes. Do not assume uniformity across states.

### 2. Draft Certificate

**Header:** "Certificate of Withdrawal of [Corporation Name]" — identify filing jurisdiction and home jurisdiction.

**Corporate identity block:**

| Field | Source |
|---|---|
| Full legal name | Exactly as on certificate of authority |
| Home jurisdiction | State/country of incorporation |
| Authorization date | Date authority was granted |
| Certificate of authority no. | If required by state |
| Principal office address | Home jurisdiction address |
| Registered agent | Name and street address in withdrawal state |

**Withdrawal declarations** (adapt to state-specific statutory language):

- Corporation surrenders its certificate of authority in [State]
- Corporation has ceased transacting business in [State]
- All state taxes and fees paid or provided for
- All known debts/obligations in [State] satisfied or provision made
- Corporation consents to service of process for proceedings arising from in-state business, designating [Secretary of State / specific agent]

> Some states require verbatim statutory language for service-of-process consent — verify before finalizing.

**Effective date:** Upon filing (default) or a future date if permitted by state law.

**Execution block:** Signature line for authorized officer, typed name/title, date, notarization block (if required), corporate seal/attestation (if mandated).

### 3. Assemble Attachments

| Attachment | When Required |
|---|---|
| Tax clearance certificate | Many states (CA, NJ, PA, etc.) |
| Home-state good standing certificate | Some states |
| Evidence of publication | Rare — states requiring newspaper notice |
| Final tax returns / annual reports | Varies |

Reference each attachment by label in the certificate body.

## Pitfalls & Checks

- **Name match** — corporate name must exactly match the original certificate of authority throughout
- **Tax clearance lead time** — some states (e.g., CA) have lengthy clearance timelines; advise early
- **Liability survives withdrawal** — note in any cover memo that existing obligations are not extinguished
- **Cite statutes** — reference the applicable withdrawal statute where required (e.g., "Pursuant to [State] Corp. Code § [VERIFY]")
- Use `[VERIFY]` for any statutory citation not confirmed against current law
- Format for direct submission to Secretary of State (standard filing margins/spacing)
