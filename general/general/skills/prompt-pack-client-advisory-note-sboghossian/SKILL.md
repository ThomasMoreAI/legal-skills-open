---
name: prompt-pack-client-advisory-note-sboghossian
title: Client Advisory Note
description: Use when a lawyer needs to draft a professional advisory note explaining the tax implications, compliance requirements, and legal risks of a proposed transaction to a business client. Covers VAT/tax analysis, regulatory compliance, and risk disclosure across MENA jurisdictions (UAE, KSA, LB, EG), DIFC/ADGM, and other applicable legal systems. Calibrated for delivery to sophisticated non-lawyer recipients — clear, structured, no jargon.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-client-advisory-note
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Client Advisory Note

A client advisory note is a written legal communication that distils the lawyer's analysis of a specific transaction or issue into a form the client can act on. It differs from a full legal opinion in scope and formality — it is faster to produce and targeted at the business decision the client faces.

## When to use this

- A client is about to sign, execute, or close a transaction and needs a written summary of the key legal, tax, and regulatory considerations before proceeding.
- The in-house team needs a note they can share internally with finance, compliance, or the board without circulating a full opinion letter.
- A client has asked "what are the tax implications of X?" or "what do we need to comply with before doing Y?" — a structured advisory note is the appropriate output.
- Post-transaction, to document the advice given (important for professional liability and audit trail purposes).
- Responding to a regulatory inquiry that requires documented legal analysis.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Description of the transaction or issue | Defines the scope of the note | Ask the user to describe in commercial terms |
| Jurisdiction(s) | Tax and compliance rules are jurisdiction-specific; do not assume | Ask the user |
| Client type (corporate, individual, regulated entity) | Some rules differ for individuals vs. companies, or for regulated vs. non-regulated entities | Ask the user |
| Key concern (tax / compliance / regulatory / all three) | Focuses the note and avoids scope creep | Ask the user; default to "all three" if unclear |
| Intended recipients | Determines technical depth and language calibration | Ask the user: board / finance / CEO / legal team |

## Optional inputs

- Relevant contracts or transaction documents (to anchor the note in specific terms rather than generic analysis).
- Prior advice given by another firm or jurisdiction (to address contradictions).
- Whether the client wants a recommendation or analysis only (some clients want the lawyer to conclude; others want options).
- Urgency / decision deadline.

## Document structure

### 1. Header
- Client name, matter reference, date, author, confidentiality classification.
- One-line subject description (e.g., "Advisory Note: Tax and Regulatory Implications of [Transaction Description], [Jurisdiction]").
- "Privileged and Confidential — Legal Advice" designation.

### 2. Purpose and scope
One short paragraph stating what the note covers and (equally important) what it does not cover. Scope limitations protect the firm from claims that the note addressed issues it did not.

Example: "This note addresses the VAT treatment and Central Bank licensing requirements applicable to the proposed acquisition described below under UAE federal law. It does not address income tax, KSA regulatory requirements, or employment matters."

### 3. Summary of the transaction
2–4 sentences describing the transaction in the client's own commercial terms, so the client can confirm the note is addressed to the right fact pattern.

### 4. Tax implications
Structure by tax type and jurisdiction:

**4.1 VAT / GST / Indirect taxes**
- Is the transaction subject to VAT? At what rate?
- Is a zero-rate, exemption, or non-supply treatment applicable?
- VAT registration or group-registration implications.
- Timing of supply and cash-flow considerations.
- MENA note: UAE VAT is 5% (Federal Decree-Law No. 8 of 2017); KSA VAT is 15%; EG VAT is 14%; LB abolished VAT in practice but retains a version of the Built-In Value Tax. Qatar has no VAT. DIFC and ADGM entities are within the UAE VAT territory.

**4.2 Withholding taxes**
- Are payments under the transaction subject to withholding at source?
- Does a double tax treaty reduce the withholding rate?
- In KSA, withholding applies to payments to non-residents on a range of services; rates vary by treaty.

**4.3 Corporate income tax / Zakat**
- UAE: Federal Corporate Tax (9% on taxable income above AED 375,000, effective from June 2023). Free zone entities with qualifying income may be subject to 0%.
- KSA: Zakat at 2.5% for Saudi-owned entities; corporate income tax at 20% for foreign-owned portions.
- LB: Standard CIT 17%; specific regimes for certain industries.
- EG: CIT 22.5% standard rate.
- Stamp duty on documents: Lebanon levies stamp duty on notarized contracts; Egypt levies stamp duty on various transactions.

**4.4 Transfer pricing**
- If the transaction is between related parties, transfer pricing rules in KSA, UAE, and EG require arm's-length pricing and contemporaneous documentation.

### 5. Compliance requirements
List each compliance obligation the client must discharge before or after the transaction:
- Regulatory registrations, notifications, or approvals required.
- KYC/AML requirements for financial transactions (UAE AML law, FATF standards applicable in GCC).
- Corporate records updates (amendments to memorandum, board resolutions, share register).
- Employment notifications if the transaction affects employees.
- License renewals or new license applications triggered by the transaction.

### 6. Risks and recommendations

| Risk | Likelihood | Impact | Recommended action |
|---|---|---|---|
| [Describe risk 1] | High / Medium / Low | High / Medium / Low | [What the client should do] |
| [Describe risk 2] | — | — | — |

Provide a clear bottom-line recommendation: "Proceed on the following conditions," "Do not proceed until X is resolved," or "Proceed with the following mitigation steps."

### 7. Next steps
A numbered action list with owners and deadlines:
1. Client obtains [specific approval / registration].
2. Lawyer drafts [specific document].
3. Tax advisor confirms [specific filing].

### 8. Limitations
Standard limitation paragraph: "This note is based on the information provided to us as at [date]. Laws and regulations are subject to change. This note is not a substitute for a full legal opinion and does not create a solicitor-client / attorney-client relationship with any party other than [Client]."

## Drafting standards

- Write for the client, not for a court. The recipient is a business person; avoid Latin and unexplained jargon.
- Lead with the conclusion ("The transaction is subject to UAE VAT at 5%") before the analysis.
- Short paragraphs (3–5 sentences maximum).
- Use bullets and tables for complex multi-point analyses; prose for narrative and recommendation.
- Every section that contains a risk must also contain a recommended action — clients need to know what to do, not just what to worry about.

## Common mistakes

- Failing to scope-limit the note — leads to claims that the advice covered issues it did not.
- Using generic US-law boilerplate in a MENA or civil-law context (e.g., referencing "§ 409A" or "ERISA" when the matter is in the UAE).
- Omitting the "next steps" section — clients read the summary and then need actionable guidance.
- Using hedging language so extreme that the note communicates nothing useful. Be clear about what is likely, what is uncertain, and what must be verified.

## Related skills

- [[prompt-pack-complex-law-simple-summary]]
- [[prompt-pack-contract-summary-for-executives]]
- [[prompt-pack-case-assessment-memo]]
- [[prompt-pack-legal-opinion]]
- [[prompt-pack-corporate-governance-policy]]
