---
name: legal-nda-everyone-needs-a-copilot
title: NDA Skill
description: NDA generation and review. Use for mutual NDAs, one-way NDAs, employee or contractor NDAs, vendor NDAs, multi-party NDAs, confidentiality clauses, CORA carve-outs, and trade secret protection.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/legal-nda
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
---

# NDA Skill

An NDA is not a formality. It is the legal foundation for sharing confidential information. Done right, it allows both parties to have a real conversation. Done poorly, it either exposes confidential information or creates obligations so broad they cannot be met.

---

## NDA Types

### Mutual NDA
Both parties share confidential information. Both parties are bound by the same obligations.
**Use when:** Starting a new client relationship, entering a partnership, beginning substantive discussions with any party.
**Default for ENAC.** Use this unless there is a specific reason for one-way.

### One-Way NDA: ENAC as Discloser
ENAC shares; the other party receives and protects.
**Use when:** Sharing ENAC methodology with a vendor, showing proprietary tools to a potential hire before an offer, demonstrating product to a prospect who is not yet sharing anything in return.

### One-Way NDA: ENAC as Recipient
The other party shares; ENAC receives and protects.
**Use when:** A client shares confidential information before a mutual NDA is in place. Rare: default to mutual.

### Employee/Contractor NDA + IP Assignment
Signed by all personnel before any access to ENAC or client confidential information. Combines NDA obligations with IP assignment.
**Use when:** Every new hire or contractor, before engagement starts.

### Vendor NDA
For vendors who will have access to client data or ENAC confidential information in the course of providing services.
**Use when:** Any vendor handling client data, accessing ENAC systems, or exposed to proprietary methodology.

### Multi-Party NDA
Three or more parties: ENAC, a subcontractor, and a government client.
**Use when:** A subcontractor will be present in client meetings or working with client data.

---

## Key Provisions

### Definition of Confidential Information

**Scope:** Be specific but comprehensive. Vague definitions are weaponized by both sides in disputes.

Standard definition:
> "'Confidential Information' means any non-public information disclosed by a party (the 'Disclosing Party') to the other party (the 'Receiving Party') in connection with [the purpose], whether in written, oral, electronic, or other form, that is designated as confidential or that reasonably should be understood to be confidential given the nature of the information and circumstances of disclosure. Confidential Information includes, without limitation, business plans, financial data, customer lists, methodologies, frameworks, tools, software, AI systems and prompts, pricing, and proposals."

**ENAC-specific additions:** Always include in the definition: "AI agent definitions, prompt libraries, workflow automation, methodology frameworks, and proprietary consulting approaches."

### Standard Exclusions

These are non-negotiable: they represent information that cannot practically be kept confidential:

1. Information that was already publicly available at the time of disclosure
2. Information that becomes publicly available through no fault of the Receiving Party
3. Information the Receiving Party can demonstrate was independently developed without reference to the Confidential Information
4. Information received from a third party without restriction
5. Information required to be disclosed by law, court order, or government regulation (with notice requirement: see below)

### Required Disclosure Carve-Out

Include this in every NDA:
> "If the Receiving Party is required by law, regulation, or court order to disclose Confidential Information, the Receiving Party shall, to the extent legally permitted: (a) provide the Disclosing Party with prompt written notice of such requirement before disclosure; (b) cooperate with the Disclosing Party in seeking a protective order or other appropriate remedy; and (c) disclose only such Confidential Information as is legally required."

### Permitted Disclosures

Define who can receive confidential information on the Receiving Party's side:
> "The Receiving Party may disclose Confidential Information only to its employees, contractors, and advisors who have a need to know for the purpose of this Agreement and who are bound by confidentiality obligations at least as protective as those in this Agreement."

### Term

**Recommended term for ENAC:**
- NDA term: Duration of the business relationship plus [2-3] years after termination
- Confidentiality obligations: Survive termination for [3-5] years for most information; indefinite for trade secrets

**Government contracts:** If a government party is signing, they cannot agree to keep information confidential beyond their legal authority. Government NDAs are limited by CORA. Handle this by:
1. Relying on CORA's trade secret exemption (C.R.S. 24-72-204(3)(a)(IV)) rather than a contractual confidentiality obligation
2. Including the CORA notice + protective order language in the NDA

### Return and Destruction

> "Upon request or termination of this Agreement, Receiving Party shall promptly return or destroy all Confidential Information and certify in writing that it has done so. This obligation does not apply to Confidential Information retained pursuant to a legal hold or as required by law."

### Remedies

> "The parties acknowledge that breach of this Agreement may cause irreparable harm for which monetary damages would be an inadequate remedy, and that injunctive relief may be sought without bond or proof of damages. This provision does not waive any other remedy available at law or equity."

### Governing Law

> "This Agreement is governed by the laws of the State of Colorado, without regard to conflicts of law principles. Any dispute shall be resolved in the courts of [Adams County / Denver, Colorado]."

---

## Colorado-Specific CORA Interaction

Any NDA involving a government entity must address CORA:

**What government entities cannot promise:** A Colorado government entity cannot contractually bind itself to keep information confidential if it is legally required to disclose under CORA. Any NDA term that says "County agrees to keep this confidential in all circumstances" is unenforceable against the county.

**What works instead:**
1. Rely on the trade secret exemption: CORA exempts confidential commercial and financial information and trade secrets (C.R.S. 24-72-204(3)(a)(IV)). Mark all ENAC materials "Confidential: Trade Secret."
2. Require notice: County agrees to provide ENAC written notice before disclosing any ENAC Confidential Information in response to a CORA request.
3. Protect the right to seek relief: County agrees not to oppose ENAC's application for a temporary restraining order or protective order in response to a CORA request.

**Language:**
> "Notwithstanding anything to the contrary, County's confidentiality obligations under this Agreement are subject to applicable Colorado law, including the Colorado Open Records Act (C.R.S. 24-72-201 et seq.). County acknowledges that ENAC's methodologies, tools, and proprietary materials constitute trade secrets exempt from disclosure under C.R.S. 24-72-204(3)(a)(IV). Prior to disclosing any ENAC Confidential Information in response to any public records request, County shall: (a) provide ENAC written notice within five (5) business days of receiving such request; and (b) afford ENAC a reasonable opportunity to seek a protective order or other appropriate relief."

---

## Quick NDA Review Checklist

When reviewing an NDA ENAC receives:

- [ ] Definition of Confidential Information broad enough to include ENAC's methodology and tools?
- [ ] Standard exclusions included (public domain, independent development, third party)?
- [ ] Required disclosure carve-out with notice requirement?
- [ ] Permitted disclosures limited to need-to-know?
- [ ] Obligations survive termination for adequate period?
- [ ] Return/destruction obligation included?
- [ ] Colorado governing law?
- [ ] CORA interaction addressed (for government-related NDAs)?
- [ ] IP assignment absent or clearly limited? (An NDA should not contain IP assignment)
- [ ] No non-compete or non-solicitation buried in the NDA?

---

## Anti-Generic Rules

- NEVER use an NDA that has no definition of Confidential Information
- NEVER sign an NDA that does not include the required disclosure carve-out with notice
- NEVER allow an NDA to inadvertently contain IP assignment language
- NEVER use a mutual NDA with a government party that does not include CORA interaction language
- NEVER skip the survival period: confidentiality obligations that expire at termination protect nothing
