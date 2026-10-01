---
name: government-contracts-everyone-needs-a-copilot
title: Government Contracts Skill
description: Government procurement and RFP analysis. Use for compliance matrices, FAR or DFARS awareness, state and local procurement, bid protests, federal flow-downs, scope risk, and public-sector contract review.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/government-contracts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: government-contracts
language: en
---

# Government Contracts Skill

Government procurement is different from commercial contracting in three critical ways: sovereign immunity limits what the government can promise, appropriations limit what the government can spend, and procurement codes define a process that must be followed exactly. Understanding all three is the starting point for every government engagement.

---

## RFP Compliance Matrix

The compliance matrix is the backbone of any RFP response. It proves that your proposal addresses every requirement. Government evaluators check compliance before they evaluate quality. Missing a requirement can be a fatal deficiency.

### How to Build the Matrix

1. Read the RFP in full: every section, including the boilerplate
2. Extract every requirement (mandatory "shall" language, submission requirements, evaluation criteria)
3. Map each requirement to the proposal section that addresses it
4. Note confidence level: fully addressed / partially addressed / needs attention

**Matrix format:**

| RFP Section | Requirement | Proposal Section | Status |
|-------------|-------------|-----------------|--------|
| Section 2.1 | Vendor must have 5 years experience in organizational consulting | Section 3, Firm Overview | Fully addressed |
| Section 3.2 | Three references from government clients | Appendix A | Fully addressed |
| Section 4.1 | Detailed project approach with milestones | Section 4 | Partially addressed: add milestones |

**Flag any requirement ENAC cannot fully address.** Evaluate whether partial compliance is acceptable or whether to decline to respond.

---

## Proposal Requirements Checklist

Most government RFPs require the same administrative items. Check for each:

- [ ] Cover letter with required certifications
- [ ] Certificate of liability insurance (verify limits match RFP requirements)
- [ ] W-9 or vendor registration in government system
- [ ] References (count, format, recency requirements)
- [ ] Project team resumes or qualifications
- [ ] Subcontractor disclosure (including small business status if required)
- [ ] Pricing in the required format (separate from technical proposal if required)
- [ ] Immigration certification (Colorado: C.R.S. § 24-74-105)
- [ ] EEO certification
- [ ] Conflict of interest disclosure
- [ ] Signature authority (ensure signer has authority to bind ENAC)
- [ ] Page limits, font requirements, file format requirements

---

## Scope Risk Flags in RFPs

Before submitting a proposal, flag these scope risks:

**Vague deliverables:** "Reports as needed," "such other services as directed": these are unlimited obligations. Request clarification or scope them explicitly in the proposal.

**Unrealistic timelines:** If the timeline cannot be met at the proposed fee, flag it. Government clients often accept timeline modifications if raised professionally before award.

**Staffing requirements:** Specific named individuals required? Key person clauses? What happens if that person is unavailable? Negotiate substitution rights.

**Emergency services:** "Emergency support as needed" or "available 24/7": define what emergency means, what response time is required, and whether emergency work is priced separately.

**Acceptance not defined:** If the RFP does not define what constitutes an accepted deliverable, add your acceptance process in the proposal. Get the government to agree to your acceptance criteria before award.

---

## FAR / DFARS for Federally-Funded State Programs

Many state and local government contracts are funded by federal grants (HUD, FEMA, HHS, DOL, DOE, DOT). When federal money flows through, federal acquisition regulations may flow down.

**Key flags when federal funding is involved:**
- Ask: Is this contract funded by federal grants?
- If yes: request the full list of federal flow-down provisions
- Common flow-downs: EEO, wage requirements, record retention, audit rights, federal agency access to records

**FAR 52.227-14 (Rights in Data):** For federally-funded R&D or services contracts, the government may claim rights to all data produced. Three tiers:
- Unlimited rights: government can use, modify, disclose without restriction
- Limited rights: certain commercial items are protected
- Restricted rights: software protection

**For ENAC's AI tools and methodology:** Assert "limited rights" or "restricted rights" for Background IP. The Background IP carve-out in the contract is your protection.

**GSA GSAR 552.239-7001:** Proposed federal clause (March 2026 draft) attempting to vest government ownership of all AI inputs/outputs on federally-funded contracts. Not yet final. Escalate to `@legal-ai-gov` for any contract where this clause appears.

---

## Sovereign Immunity and Indemnification

The Colorado Governmental Immunity Act (CGIA, C.R.S. 24-10-101) gives counties broad immunity from suit. This has three practical consequences:

**1. Asymmetric indemnification is normal and expected.**
The county will not agree to indemnify ENAC the same way ENAC is asked to indemnify the county. The county cannot waive immunity by contract. The negotiating goal is not mutuality: it is a reasonable cap on ENAC's obligations.

**2. The county cannot waive its sovereign immunity by contract.**
Any clause in a government contract that purports to bind the county in ways that conflict with CGIA is unenforceable against the county. Do not build your negotiating strategy on enforcement of such clauses.

**3. Litigation against a government entity requires specific procedures.**
Filing suit against Adams County requires following CGIA notice requirements and the Colorado Governmental Claims Act. Know this before you threaten litigation. The process is different from commercial litigation.

**Practical implications for indemnification negotiations:**
- Accept that you will provide some indemnification to the government
- Fight for: negligence standard (your negligence, not strict performance), fee cap, specific scope of claims covered
- Do not fight for: mutual indemnification: you will not win this, and it wastes negotiating capital

---

## Non-Appropriation Clause Risk

Government contracts are subject to legislative appropriation of funds. If the legislature does not appropriate funds for a multi-year contract, the government can terminate the contract without payment beyond the appropriated amount.

**Risk management:**
- Understand the appropriation structure for the engagement (annual appropriation, multi-year grant, capital project)
- For multi-year contracts: include non-appropriation clause language that ensures payment for work performed through the termination date, not just through the appropriation period
- Price multi-year contracts with this risk in mind: front-load deliverables where possible
- Do not commit to major upfront investments (custom software, specialized equipment) on multi-year government contracts without discussing non-appropriation risk

---

## Bid Protest Procedures

If ENAC loses an RFP award it believes was procedurally improper:

**State agency (C.R.S. 24-109-101 et seq.):**
- Protest to the Chief Procurement Officer within 7 days of receipt of award notice
- Grounds: violation of procurement code or solicitation requirements
- Escalation: State Board of Contract Appeals

**Adams County (local procurement rules):**
- Check Adams County Purchasing Policy for specific protest procedures
- Deadlines are typically 7-10 days and are jurisdictional
- Miss the deadline: protest is waived

**Federal programs:**
- Protest to the awarding agency's contracting officer
- May also protest to GAO (within 10 days of award) or agency IG
- Court of Federal Claims for significant awards

**Before filing a protest:**
- Request a debriefing to understand why ENAC did not win
- Evaluate whether the grounds for protest are procedural (strong basis) or substantive (weak basis)
- Weigh the cost of the protest against the value of the contract and the relationship with the agency

---

## Cooperative Purchasing Provisions

Many Colorado government contracts include a cooperative purchasing provision allowing other state and local entities to purchase from the same contract without a separate procurement.

**For ENAC, this is both opportunity and risk:**

**Opportunity:** If ENAC wins an Adams County contract with cooperative purchasing rights, other Colorado counties, municipalities, and state agencies can contract directly. This is a growth channel.

**Risk:** Cooperative purchasing exposes ENAC to price pressure. Any entity purchasing under the cooperative can claim the same rates. If ENAC later offers lower rates to another client, it may trigger an MFN obligation.

**Strategy:**
- Price cooperative purchasing contracts at rates sustainable for the volume
- Include a "most favored pricing" carve-out for different service scopes (a full organizational assessment is different from a workshop)
- Monitor which entities use the cooperative and proactively engage them

---

## Output Structure

1. **RFP compliance matrix**: Every requirement mapped to proposal section with status
2. **Scope risk flags**: Vague or risky RFP requirements requiring clarification or mitigation
3. **Administrative checklist**: Every required submission item confirmed
4. **Federal flow-down analysis**: If federally funded, which provisions apply
5. **Sovereign immunity and indemnification strategy**: What to accept, what to fight for
6. **Non-appropriation risk assessment**: For multi-year contracts
7. **Cooperative purchasing analysis**: Pricing and growth implications

---

## Anti-Generic Rules

- NEVER submit an RFP response without a completed compliance matrix
- NEVER ignore federal flow-down clauses: they can include IP rights provisions that override the prime contract
- NEVER build a negotiating strategy around forcing the government to waive sovereign immunity
- NEVER miss a bid protest deadline: they are jurisdictional and cannot be waived
- NEVER price a multi-year government contract without factoring in non-appropriation risk
