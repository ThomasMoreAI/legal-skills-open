---
name: draft-nda-mutual-sboghossian
title: Mutual NDA (Confidentiality Agreement)
description: Use when drafting a mutual NDA between two parties exploring a transaction or collaboration, where both sides will disclose confidential information. Covers required inputs (via intake), document structure, jurisdictional notes for LB, KSA, UAE, DIFC/ADGM, and the drafting standard for complete, ready-to-execute output. Triggers on "nda", "mutual nda", "confidentiality agreement", "non-disclosure agreement", or "mnda" requests where both parties disclose.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-nda-mutual
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Mutual NDA (Confidentiality Agreement)

## When to use this

Use this skill when two parties are exploring a transaction, partnership, or collaboration and both sides will share confidential information. The symmetric nature of a mutual NDA — each party is both Discloser and Recipient — is appropriate for:

- M&A discussions (both sides share financials and strategy)
- Commercial partnership negotiations
- Joint venture explorations
- Technology evaluation or proof-of-concept discussions
- Any bilateral commercial negotiation involving sensitive proprietary information

When only one party is disclosing (investor pitch, vendor receiving customer data, employer sharing trade secrets with a new employee), use [[draft-nda-unilateral]] instead — asymmetric obligations are more appropriate.

## Required inputs

Collect via [[conversation-intake-nda]] before drafting. If not available, use these defaults.

| Input | Why it matters | Default |
|-------|---------------|---------|
| Party A name + entity type + address | Complete party identification | — must supply |
| Party B name + entity type + address | Complete party identification | — must supply |
| Purpose | Defines the Permitted Purpose; limits use of CI; scopes the entire agreement | "Evaluating a potential commercial transaction between the Parties" |
| Term of confidentiality obligation | Duration of the duty of confidentiality | 2 years from the date of each disclosure; trade secrets survive indefinitely |
| Governing law | Determines enforceability, remedies, liquidated-damages approach | Jurisdiction where both parties are incorporated, or neutral (DIFC/English if cross-border) |

## Optional inputs

- **Surviving obligations for trade secrets**: default — confidentiality obligations survive the term for information that constitutes a trade secret; confirm with user
- **Standard carve-outs**: default — independently developed; already public; lawful third-party receipt; required by court order or law (with advance notice). Any additions require explicit instruction.
- **Permitted recipients**: default — directors, officers, employees, and professional advisors on a strict need-to-know basis; each must be bound by equivalent confidentiality obligations
- **Return / destruction**: default — on demand, return or destroy all Confidential Information in tangible form; provide certification
- **Stand-alone agreement vs integrated**: if the parties will proceed to a principal agreement (MSA, JV, SHA), state whether this NDA merges into or survives alongside the principal agreement

## Document structure

### 1. Parties and recitals
Full identification of Party A and Party B (entity name, type, incorporation jurisdiction, registered address). Recitals: each party wishes to receive and share confidential information in connection with the Permitted Purpose; the parties enter this NDA to protect such information.

### 2. Definitions
- **Confidential Information**: all non-public information of a party, whether marked confidential or not, that a reasonable person would consider confidential given its nature and the circumstances of disclosure. Specifically includes: business plans, financial data, customer data, technical know-how, product roadmaps, pricing, personnel data, IP, and information concerning the existence and content of these discussions.
- **Permitted Purpose**: the specific activity stated in the recitals; no other purpose is permitted.
- **Representatives**: directors, officers, employees, professional advisors (lawyers, accountants, bankers) who need access on a need-to-know basis and are bound by equivalent confidentiality obligations.
- **Affiliates**: related companies (define by control); state whether they are included in the "Representatives" definition.

### 3. Confidentiality obligations (symmetric)
Each Party, acting as Recipient in relation to the other's Confidential Information, undertakes:
- To keep the Confidential Information strictly confidential
- To use it only for the Permitted Purpose
- Not to disclose it to any third party without the Discloser's prior written consent
- To disclose it to Representatives only on a need-to-know basis, and only after ensuring each Representative is bound by obligations equivalent to those in this NDA
- To take at least the same measures to protect the other party's Confidential Information as it uses for its own information of the same sensitivity (but in no event less than reasonable care)

### 4. Standard carve-outs (permitted disclosures)
The following are not Confidential Information (or disclosure is permitted):
1. Information that is or becomes publicly available through no breach by the Recipient
2. Information the Recipient can demonstrate was already in its possession before disclosure (not subject to existing confidentiality obligations)
3. Information the Recipient can demonstrate was developed independently without use of or reference to the Discloser's Confidential Information
4. Information received from a third party who was entitled to disclose it and did so without restriction
5. Disclosure required by applicable law, regulation, court order, or stock exchange rules — provided the Recipient gives the Discloser prompt prior written notice (to the extent legally permissible) and cooperates with the Discloser's efforts to obtain a protective order

### 5. Term and survival
- **Duration of disclosure window**: the agreement covers disclosures made during the period from the effective date until [12/24] months or until the parties execute a principal agreement (whichever is earlier), unless extended by written agreement
- **Confidentiality obligation term**: obligations apply to information disclosed during the window for [2] years from the date of disclosure
- **Trade secrets**: for information that constitutes a trade secret under applicable law, confidentiality obligations survive for as long as the information remains a trade secret

### 6. No license / no IP transfer
Nothing in this NDA grants the Recipient any license, right, or interest in the Discloser's Confidential Information, IP, or technology. All CI is provided "as is" — the Discloser makes no representation or warranty as to accuracy, completeness, or fitness for the Recipient's intended purpose.

### 7. No representation as to accuracy
The Discloser provides Confidential Information without any representation or warranty as to its accuracy, completeness, reliability, or fitness for the Recipient's purpose. The Recipient accepts full responsibility for its reliance on CI.

### 8. Remedies — injunctive relief
Each party acknowledges that a breach of this NDA would cause irreparable harm that monetary damages may be insufficient to remedy, and that the Discloser shall be entitled to seek injunctive relief or other equitable remedies in any competent court without the requirement of posting a bond or proving actual damage, in addition to all other remedies available at law.

### 9. Return or destruction
On the Discloser's written request, or on expiry / termination of the NDA, the Recipient will promptly:
- Return or destroy all Confidential Information in tangible or recorded form
- Delete electronic copies
- Provide a written certificate of destruction within [5] business days
Exception: copies in automated backup systems that are not reasonably recoverable, subject to ongoing confidentiality obligations.

### 10. Governing law and dispute resolution
- Governing law: [jurisdiction]
- Dispute resolution: see Jurisdictional notes below for jurisdiction-specific preferences

### 11. Boilerplate
- Entire agreement (this NDA supersedes all prior discussions on confidentiality)
- Amendment: only in writing signed by both parties
- Waiver: no waiver of any right constitutes a waiver of any other right
- Severability
- Notices
- Counterparts / electronic execution
- No obligation: nothing in this NDA obligates either party to proceed with any transaction
See [[draft-boilerplate-clauses]] for standard formulations.

## Jurisdictional notes

| Jurisdiction | Key considerations |
|---|---|
| **Lebanon (LB)** | Default to Beirut courts (Court of Commerce) unless parties agree to arbitration. Consider Tawqi3i (notarization) for execution if either party wants to be able to enforce before Lebanese courts without authentication challenges. Lebanese courts accept Arabic, French, or English agreements. |
| **KSA** | Avoid US-style liquidated damages clauses — structure any penalty for breach as "honest pre-estimate of loss" rather than as a deterrent penalty; Saudi courts may recharacterize punitive clauses. Governing law: Saudi law is common for onshore Saudi parties; parties may also agree to DIAC arbitration. |
| **UAE onshore** | Enforceability of liquidated damages is courts' discretion under UAE Civil Code Art. 390 — courts may reduce a disproportionate penalty. Govern by UAE law for UAE-onshore parties. Register/notarize if required by context (not standard for NDAs). |
| **DIFC / ADGM** | Full common-law NDA conventions apply. Injunctive relief standard applies as written. Arbitration at DIAC or ADGM Arbitration Centre is common for cross-border commercial NDAs. |
| **EU / GDPR** | If Confidential Information includes personal data (employee lists, customer data, user data), a DPA must accompany or be incorporated into the NDA — the NDA alone does not satisfy GDPR processor obligations. |

## Drafting standards

- **No `[INSERT X]` placeholders unless a template was explicitly requested.** If a value was not provided, use a clearly-labeled default and list it at the top of the output: *"Defaults used: Term = 2 years from disclosure; Governing law = [jurisdiction]; Carve-outs = standard 4."*
- Produce a **complete, ready-to-execute document** with a proper signature block (name, title, date, signature line) for each party.
- Mutual obligations must be genuinely symmetric — avoid language that accidentally imposes stricter duties on one party than the other.

## Common mistakes

- Using a unilateral NDA structure when both parties are disclosing — fails to protect the disclosing party in the "wrong" direction
- Omitting a definition of trade secrets for the survival clause — some jurisdictions define "trade secret" narrowly; confirm the applicable definition
- No injunctive relief provision — in civil-law jurisdictions, courts are less likely to grant ex parte injunctions without express contractual acknowledgment of irreparable harm
- Overly broad "Confidential Information" definition that sweeps up publicly known facts — weakens the agreement
- Failure to require Representatives to be bound — creates a gap through which CI flows without binding obligation

## Related skills

- [[draft-nda-unilateral]]
- [[review-nda-quick-check]]
- [[conversation-intake-nda]]
- [[draft-boilerplate-clauses]]
