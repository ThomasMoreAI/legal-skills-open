---
name: legal-missing-everyone-needs-a-copilot
title: Missing Protections Skill
description: Identify missing contract protections. Use for payment protections, IP protections, limitation of liability, termination rights, confidentiality, change order process, acceptance criteria, and risk gaps.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/legal-missing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
---

# Missing Protections Skill

Bad contract clauses get noticed. Missing protections are invisible until something goes wrong: and then they are very expensive. This skill scans for what should be in a contract but is not.

---

## Why Missing Protections Are Dangerous

A contract's silence is not neutral. When a contract does not address a topic, the governing law fills the gap: and the law's default is rarely favorable to the smaller party. Worse, a contract dispute on an unaddressed topic means expensive litigation to determine what the parties intended. The answer to "what should the contract have said?" is always "put it in writing."

---

## Missing Protections Checklist

### Payment Protections

**Payment timeline**
- Why it matters: Without a defined payment timeline, "reasonable time" is the legal standard. In Colorado government contracts, this can mean 60-90 days before late payment remedies apply.
- Suggested language: "County shall pay each invoice within thirty (30) days of receipt. Invoices shall be submitted monthly in arrears. Amounts unpaid after thirty (30) days shall accrue interest at 1.5% per month."

**Invoice process**
- Why it matters: If the contract does not specify how invoices are submitted, the payment clock may never start.
- Suggested language: "Contractor shall submit invoices electronically to [billing contact] by the fifth business day of each month for services performed in the preceding month."

**Late payment remedy**
- Why it matters: Without a remedy, late payment is a breach with no practical consequence.
- Suggested language: "Contractor may suspend performance upon thirty (30) days written notice if County fails to pay an undisputed invoice within sixty (60) days of receipt."

**Suspension for non-payment**
- Why it matters: Contractor needs a right to stop working when payment is overdue, without breaching the contract.
- Suggested language: See above.

---

### IP Protections

**Background IP carve-out**
- Why it matters: Without an explicit carve-out, a work-for-hire or all-IP-assignment clause can transfer ownership of ENAC's pre-existing methodology to the client.
- Suggested language: See `background-ip-schedule` skill for the full carve-out language.

**Derivative IP ownership**
- Why it matters: Improvements to ENAC's methodology that happen during an engagement belong to ENAC: but only if the contract says so.
- Suggested language: "Any improvements, modifications, or derivative works of Contractor's Background IP developed during this engagement shall remain Contractor's property and are excluded from the definition of Foreground IP."

**Portfolio and case study rights**
- Why it matters: ENAC needs to be able to use de-identified client work for marketing. Without explicit permission, the confidentiality clause may prohibit it.
- Suggested language: "Contractor may reference this engagement in its marketing materials and portfolio using de-identified descriptions of services performed and methodologies applied, subject to the confidentiality provisions herein."

---

### Limitation of Liability

**Liability cap**
- Why it matters: Without a cap, ENAC's liability is theoretically unlimited for any breach.
- Suggested language: "Except for indemnification obligations and breaches of confidentiality, each party's total aggregate liability under this Agreement shall not exceed the total fees paid by County to Contractor in the twelve (12) months preceding the claim giving rise to liability."

**Consequential damages waiver**
- Why it matters: Lost profits, lost business opportunity, and reputational damage are consequential damages. Without a waiver, these are potentially recoverable against ENAC.
- Suggested language: "Neither party shall be liable to the other for any indirect, incidental, consequential, special, or punitive damages, including lost profits, even if advised of the possibility of such damages."

---

### Termination Rights

**Termination for convenience (contractor's right)**
- Why it matters: Contractors typically have no right to terminate for convenience in government PSAs. Without this, ENAC cannot exit a problematic engagement without breaching.
- Suggested language: "Either party may terminate this Agreement for convenience upon sixty (60) days written notice. In the event of termination for convenience, County shall pay Contractor for all services satisfactorily performed through the effective date of termination."

**Cure period for termination for default**
- Why it matters: Without a cure period, the client can terminate for any alleged deficiency without giving ENAC a chance to fix it.
- Suggested language: "Prior to terminating for default, County shall provide Contractor with thirty (30) days written notice specifying the alleged deficiency. Contractor shall have thirty (30) days to cure. If cured, the Agreement continues."

**Payment upon termination for convenience**
- Why it matters: Without explicit payment on T4C, ENAC may receive nothing for work already completed.
- Suggested language: "Upon termination for convenience, County shall pay Contractor for: (a) all services performed and accepted through the termination date; (b) reasonable wind-down costs incurred within thirty (30) days of the termination notice, not to exceed [X]."

---

### Confidentiality

**Mutual confidentiality**
- Why it matters: One-sided confidentiality protects only the client. ENAC shares confidential methodology and approach; that should be protected too.
- Suggested language: "Each party agrees to keep confidential the other party's Confidential Information and to use it only for the purposes of this Agreement."

**Trade secret protection for ENAC materials**
- Why it matters: ENAC materials submitted to a government client are subject to CORA. Without contractual protection, trade secrets may be disclosed in response to a CORA request.
- Suggested language: "County acknowledges that ENAC's methodologies, tools, and approaches submitted under this Agreement constitute trade secrets exempt from disclosure under C.R.S. 24-72-204(3)(a)(IV). County shall provide ENAC written notice before disclosing any ENAC Confidential Information in response to any public records request, and shall afford ENAC a reasonable opportunity to seek a protective order."

---

### Change Order Process

**Change order requirement**
- Why it matters: Without a defined change order process, scope expansion is uncompensated and potentially unlimited.
- Suggested language: "Any changes to the scope of services, deliverables, or schedule must be agreed upon in writing by both parties through a Change Order. Contractor is not obligated to perform services beyond the original scope without an executed Change Order specifying the additional services, fees, and schedule."

**Scope definition by reference to proposal**
- Why it matters: If the PSA contains scope language broader than the proposal, the PSA governs.
- Suggested language: "The Statement of Work / Proposal attached as Exhibit A governs the scope of services, fees, and schedule. In the event of a conflict between this Agreement and Exhibit A, Exhibit A controls for scope, fees, and schedule."

---

### Acceptance Criteria

**Defined acceptance standard**
- Why it matters: Without acceptance criteria, the client can claim deliverables are non-conforming and withhold payment indefinitely.
- Suggested language: "Deliverables shall be deemed accepted unless County provides Contractor written notice of specific deficiencies within fifteen (15) business days of delivery. County shall specify the deficiencies in reasonable detail. Contractor shall have fifteen (15) business days to correct identified deficiencies."

**Deemed acceptance**
- Why it matters: If the client does not respond to a deliverable, ENAC should not be in limbo.
- Suggested language: "Failure to provide written notice of rejection within the review period constitutes acceptance."

---

### Force Majeure

**Force majeure clause**
- Why it matters: Without one, ENAC may be in breach for events entirely outside its control.
- Suggested language: "Neither party shall be liable for delays or failures in performance resulting from causes beyond its reasonable control, including natural disasters, acts of government, pandemics, labor disputes, or internet infrastructure failures. The affected party shall provide prompt written notice and resume performance when the force majeure event ends."

---

### Governing Law and Dispute Resolution

**Governing law and venue**
- Why it matters: Without governing law, disputes about which state's law applies are expensive.
- Suggested language: "This Agreement is governed by the laws of the State of Colorado. Any legal action shall be filed in the district courts of Adams County, Colorado."

**Dispute resolution escalation**
- Why it matters: Litigation is expensive. An escalation ladder prevents disputes from going straight to court.
- Suggested language: "The parties agree to resolve disputes through the following escalation: (1) informal discussion between project leads within five (5) business days; (2) escalation to principals within fifteen (15) days; (3) mediation through a mutually agreed mediator before filing any legal action."

---

## Output Structure

1. **Missing Payment Protections**: Each item with why it matters and suggested language
2. **Missing IP Protections**: Each item with why it matters and suggested language
3. **Missing Liability Protections**: Each item with why it matters and suggested language
4. **Missing Termination Rights**: Each item with why it matters and suggested language
5. **Missing Process Provisions**: Change order, acceptance criteria, force majeure
6. **Missing Governing Framework**: Governing law, dispute resolution
7. **Priority Order**: Which missing items create the most acute risk

---

## Anti-Generic Rules

- NEVER report "contract is silent" without explaining what silence means legally
- NEVER skip the acceptance criteria check: it is the most common payment dispute trigger in professional services
- NEVER omit the change order process check: scope creep is the most common profitability killer
- NEVER assume a "professional services" label creates implied protections: it does not
- NEVER issue a missing protections report without suggested language for each gap
