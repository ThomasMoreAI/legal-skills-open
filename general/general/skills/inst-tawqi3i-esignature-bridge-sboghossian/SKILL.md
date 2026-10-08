---
name: inst-tawqi3i-esignature-bridge-sboghossian
title: Inst — Tawqi3i E-Signature Bridge
description: Use when a Lebanese legal document requires electronic signature or cross-border e-notarization via the Tawqi3i (توقيعي) platform operated by the Lebanese Ministry of Interior. Handles direct sign flows within Louis, apostille auto-request generation, and multi-jurisdiction recognition checks (Lebanon, KSA, UAE). Provides audit-trail documentation for signed documents. Critical for any Lebanese cross-border transaction where physical notarization is impractical.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/inst/inst-tawqi3i-esignature-bridge
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Inst — Tawqi3i E-Signature Bridge

## Purpose

**Tawqi3i** (توقيعي — "My Signature") is the Lebanese Ministry of Interior's official electronic authentication and e-notarization platform. It enables Lebanese residents and diaspora to sign and authenticate documents digitally, with the Ministry's digital seal acting as the notarial equivalent for participating document types and countries.

This skill integrates the Tawqi3i sign flow directly into Louis document workflows, handles apostille auto-request generation, verifies cross-border recognition in KSA and UAE, and preserves a complete audit trail for each signed document.

---

## When to use this

- A Lebanese document needs to be signed and notarized but the signer is abroad (diaspora use case)
- A power of attorney, contract, or affidavit drafted in Louis needs e-signature + Ministry authentication
- A cross-border transaction between Lebanon and KSA/UAE requires authenticated Lebanese documents
- A user asks whether Tawqi3i-signed documents are recognized in a specific destination country
- An apostille is needed for a Lebanese document destined for a Hague Convention member state (note: Lebanon is not a member, but Tawqi3i can facilitate the equivalent legalization chain)
- An audit trail of signature events is required for litigation or regulatory purposes

---

## Tawqi3i platform overview

| Attribute | Detail |
|---|---|
| Operator | Lebanese Ministry of Interior and Municipalities |
| Authentication method | Lebanese national eID card (biometric) or SMS/email OTP for diaspora |
| Legal basis | Lebanese Electronic Transactions Law (Law No. 81 of 2018) |
| Document types supported | Powers of attorney, affidavits, company resolutions, lease agreements, commercial contracts, personal declarations |
| Ministry seal | Attached digital seal equivalent to Notaire Public authentication for supported types |
| Language | Arabic and French interfaces |
| Diaspora access | Available to Lebanese diaspora via Lebanese embassies or remote authentication for certain document types |

---

## Integration workflow within Louis

### Step 1: Document preparation
1. Louis drafts the document (PoA, contract, declaration) in the appropriate language and format
2. Pre-signature checklist generated: confirm parties' identities, document completeness, correct template for Tawqi3i submission
3. User reviews and approves draft

### Step 2: Tawqi3i sign flow initiation
1. Louis generates a Tawqi3i-compatible document package (PDF/A format, correct field tagging)
2. System triggers Tawqi3i API handoff (or provides structured deep link if direct API unavailable)
3. Signer authenticates via eID or OTP
4. Ministry applies digital seal and timestamp
5. Signed document returned to Louis with Ministry authentication certificate

### Step 3: Apostille / legalization auto-request
If the signed document is destined for a country requiring further legalization:
- **Hague Apostille Convention members** (e.g., KSA joined 2012; UAE joined 2021): generate apostille request to Lebanese Ministry of Foreign Affairs + Emigrants (MOFA); note Lebanon is not an Apostille member so this goes through the MOFA certification chain
- **Non-Convention countries**: generate full chain legalization checklist: Ministry of Foreign Affairs (LB) → destination country Embassy in Beirut → destination country MOFA

### Step 4: Cross-border recognition check
Louis checks the recognition matrix:

| Destination | Tawqi3i-signed document recognized? | Additional steps needed |
|---|---|---|
| KSA | Generally yes with MOFA authentication chain | MOFA LB → Saudi Embassy Beirut → Saudi MOFA |
| UAE | Generally yes with MOFA authentication chain | MOFA LB → UAE Embassy Beirut → UAE MOFA |
| France | Subject to French consular verification | French Embassy Beirut confirmation |
| UK | Case-by-case; consular authentication often needed | — |
| US | Case-by-case; notarized translation often required | — |

### Step 5: Audit trail generation
Louis generates and stores:
- Signing event log: timestamp, signer identity method, IP (if available), document hash
- Ministry authentication certificate (attached to document)
- Legalization chain steps completed and pending
- Expiry flags: PoA validity period (Lebanese PoAs typically valid 1 year unless otherwise specified)

---

## Document type handling

| Document type | Tawqi3i supported | Louis template available | Notes |
|---|---|---|---|
| General Power of Attorney | Yes | Yes | Must specify scope; open-ended PoA disfavored by some MENA registries |
| Special Power of Attorney | Yes | Yes | For specific transaction; recommended for real estate |
| Affidavit / Declaration | Yes | Yes | Personal declarations, financial statements |
| Commercial contract | Yes (for authentication) | Yes | Tawqi3i certifies signatures, not contract terms |
| Lease agreement | Yes | Yes | Residential + commercial |
| Company board resolution | Yes | Yes | SARL / SAL resolutions for use abroad |
| Will / testament | No (civil wills not standard in LB) | Limited | Lebanese personal status law is confessional; civil wills limited |

---

## Limitations and failure modes

| Issue | Cause | Handling |
|---|---|---|
| Tawqi3i system downtime | Ministry platform maintenance | Alert user; advise physical notary as fallback; retry queue |
| eID authentication failure | Expired eID; diaspora without eID | Route to Lebanese Embassy e-authentication or physical notary abroad |
| Document type not supported | Tawqi3i scope limits | Route to physical Notaire Public; identify nearest Lebanese consulate |
| Destination country non-recognition | Some countries do not yet accept Tawqi3i | Advise physical notarization + full legalization chain |
| PoA scope disputes | Vague scope language | Louis flags vague scope at draft stage; recommends specific PoA |

---

## Privacy and security

- Document content transmitted to Tawqi3i is processed by the Lebanese Ministry — treat as non-confidential for privilege purposes
- Do not include client-identifying personal data beyond what is legally required for the instrument
- Audit trail stored per Lebanese data retention norms; user can request deletion of drafts not yet submitted
- For privileged communications, advise against using Tawqi3i — use physical notarization instead where confidentiality is paramount

---

## Related skills

- [[inst-notary-integration-mena]]
- [[inst-lb-bar-association-integration]]
- [[inst-ksa-moj-integration]]
- [[inst-uae-moj-integration]]
- [[draft-power-of-attorney]]
