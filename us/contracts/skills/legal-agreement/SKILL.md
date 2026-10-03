---
name: legal-agreement
title: Legal Agreement Skill
description: Business agreement generation for professional services. Use for contractor agreements, partnership agreements, SOWs, MSAs, task orders, payment, IP, confidentiality, acceptance, and termination provisions.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/legal-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
---

# Legal Agreement Skill

A well-drafted agreement prevents disputes by making the parties' expectations explicit before work begins. The goal is not to anticipate every possible dispute: it is to eliminate ambiguity on the issues that most commonly create them.

---

## Agreement Types

### Freelancer / Contractor Agreement
ENAC hiring an independent contractor for a specific engagement or ongoing work.
**Key risk:** IP assignment from contractor to ENAC, classification as employee vs. contractor.

### Master Services Agreement (MSA)
Framework agreement governing an ongoing relationship with a client or vendor. Specific engagements are then executed as SOWs or task orders under the MSA.
**Key advantage:** Negotiate terms once; reference them in every subsequent engagement.

### Statement of Work (SOW) / Task Order
Specific engagement document executed under an MSA, or as a standalone document.
**Key risk:** Scope ambiguity, missing acceptance criteria, undefined change order process.

### Partnership Agreement
Agreement between ENAC and another firm to co-deliver services or share revenue.
**Key risk:** IP ownership of jointly developed work, revenue sharing, client ownership, liability for partner's work.

---

## Required Sections: Professional Services Agreement

### 1. Scope of Services

The most important section. Ambiguous scope is the root cause of most professional services disputes.

**Required elements:**
- Specific description of what ENAC will deliver
- Reference to the proposal or SOW attached as an exhibit (which controls scope, fees, and schedule)
- Explicit statement that services beyond the scope require a written change order
- Named deliverables (reports, workshops, slide decks, etc.) with brief descriptions

**Sample scope definition:**
> "ENAC shall provide the consulting services described in Exhibit A (Statement of Work), which is incorporated by reference. Exhibit A governs the scope, deliverables, schedule, and fees for this engagement. Any work beyond the scope described in Exhibit A requires a written change order executed by both parties."

### 2. Acceptance Criteria

**Required elements:**
- How deliverables are submitted (email, shared folder, etc.)
- Review period: number of business days for client review (suggest 10-15 business days)
- Rejection process: written notice with specific deficiencies
- Cure period: ENAC's time to address identified deficiencies (suggest 10-15 business days)
- Deemed acceptance: if no written rejection within the review period, deliverable is accepted

**Sample acceptance clause:**
> "Client shall review each deliverable and provide written acceptance or written notice of specific deficiencies within fifteen (15) business days of delivery. If Client provides notice of deficiencies, ENAC shall have fifteen (15) business days to address them. If Client does not provide written notice within the review period, the deliverable is deemed accepted."

### 3. Payment Terms

**Required elements:**
- Fee amount (or reference to Exhibit A)
- Invoicing schedule (monthly in arrears is ENAC's standard)
- Payment timeline (Net 30 from invoice date)
- Late payment interest or remedy
- Expenses (reimbursable? At what rate? Approval required?)

**Sample payment clause:**
> "ENAC shall invoice Client monthly in arrears for services performed in the preceding month. Client shall pay each invoice within thirty (30) days of receipt. Invoices unpaid after thirty (30) days shall accrue interest at 1.5% per month on the outstanding balance. Approved travel and out-of-pocket expenses are reimbursable at cost with receipts."

### 4. Intellectual Property

**Required elements:**
- Foreground IP assignment to client (deliverables created under this engagement)
- Background IP carve-out (ENAC retains pre-existing methodology, tools, frameworks)
- Derivative IP stays with ENAC
- License-back to client: perpetual, non-exclusive, non-transferable license for internal use
- ENAC's right to use de-identified work for portfolio and case studies

**Sample IP clause:**
> "ENAC retains ownership of all Background IP, defined as pre-existing methodologies, frameworks, tools, templates, agent definitions, and know-how. Client receives a perpetual, royalty-free, non-exclusive, non-transferable license to use Background IP solely as embedded in the final deliverables for Client's internal business purposes. Final deliverables specifically created for Client are owned by Client, excluding embedded Background IP. ENAC may use de-identified descriptions of this engagement for portfolio and marketing purposes."

### 5. Confidentiality

**Required elements:**
- Definition of confidential information (broad, both parties)
- Standard exclusions (public domain, independent development, required disclosure)
- Required disclosure carve-out with notice requirement
- Survival period (3-5 years after termination; indefinite for trade secrets)

### 6. Term and Termination

**Required elements:**
- Term: Start date, end date or "until completion of deliverables"
- Termination for convenience by either party: 30-60 days notice; payment through termination date
- Termination for cause: 30-day notice + 30-day cure period
- Effect of termination: what is owed, what is returned

### 7. Limitation of Liability

**Required elements:**
- Cap at fees paid in the preceding 12 months
- Mutual consequential damages waiver
- Carve-outs for indemnification obligations and confidentiality breaches

### 8. Independent Contractor Status

**Required for contractor agreements:**
> "The parties acknowledge that ENAC / [Contractor] is an independent contractor and not an employee of [Client / ENAC]. Nothing in this Agreement creates an employment, joint venture, or partnership relationship. [Contractor] is responsible for its own taxes, benefits, and compliance with applicable law."

### 9. Governing Law and Dispute Resolution

**Standard:**
> "This Agreement is governed by the laws of the State of Colorado. The parties agree to attempt informal resolution of any dispute within fifteen (15) days of notice. If informal resolution fails, the parties shall submit the dispute to mediation before filing any legal action. Venue for any legal proceeding shall be Adams County, Colorado [or Denver, Colorado]."

---

## Colorado-Specific Contractor Agreement Provisions

For ENAC hiring a contractor:

1. **ABC test acknowledgment:** Include a representation by the contractor that they meet the Colorado ABC test for independent contractor status
2. **IP assignment:** Assign all work product created for the engagement to ENAC
3. **Background IP carve-out:** Contractor retains pre-existing IP brought to the engagement; grants ENAC a license for use in deliverables
4. **Non-compete:** Do not include: extremely limited enforceability in Colorado
5. **Non-solicitation of ENAC clients:** Narrow, time-limited (12 months), and only for clients the contractor directly worked with
6. **NDA:** Integrated or by reference to a separate NDA

---

## MSA + SOW Structure

For recurring client relationships:

**MSA covers:** Terms and conditions, IP ownership framework, confidentiality, liability, governing law, dispute resolution. Does not specify fees or scope.

**SOW covers (under the MSA):** Specific services, deliverables, fees, schedule, acceptance criteria. References and incorporates MSA terms.

**Advantage:** MSA terms are negotiated once. Each new engagement requires only a brief SOW, not a full contract negotiation.

---

## Anti-Generic Rules

- NEVER use a generic "services agreement" template without adding acceptance criteria and a change order clause
- NEVER draft a contractor agreement without addressing IP assignment and the ABC test
- NEVER omit a liability cap: it belongs in every professional services agreement
- NEVER use "Client satisfaction" as an acceptance standard without a defined process and timeline
- NEVER skip the Background IP carve-out in any agreement where ENAC is providing services using its methodology
