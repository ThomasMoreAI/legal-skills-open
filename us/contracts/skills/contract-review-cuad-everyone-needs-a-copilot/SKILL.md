---
name: contract-review-cuad-everyone-needs-a-copilot
title: CUAD Contract Review Skill
description: Contract review using CUAD risk categories. Use for systematic clause coverage across commercial contracts, including assignment, change of control, competition, exclusivity, IP, liability, termination, and payment provisions.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/contract-review-cuad
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
---

# CUAD Contract Review Skill

The CUAD (Contract Understanding Atticus Dataset) represents 41 risk provision categories identified across 510 commercial contracts. This skill applies all 41 categories systematically to ensure no material provision is missed.

---

## How to Use This Skill

For each of the 41 categories below:
1. **Locate**: Does the contract address this category?
2. **Assess**: If present, is the language favorable, neutral, or unfavorable?
3. **Flag**: If absent, note whether absence is a risk (some categories are optional)
4. **Act**: For unfavorable provisions, draft a redline or note the negotiation position

---

## The 41 CUAD Categories

### Category 1: Parties
- Correctly identifies the contracting parties?
- Is ENAC named correctly (full legal entity name)?
- Are any affiliates or subsidiaries bound?

### Category 2: Effective Date
- Date the agreement becomes binding
- Are there conditions precedent to effectiveness?
- Does the term start on a specific date or upon execution?

### Category 3: Expiration Date / Renewal Term
- When does the initial term end?
- Is there automatic renewal (evergreen)? With what notice period to prevent renewal?
- Are renewal terms on the same terms or renegotiated?

### Category 4: Governing Law
- Which state's law governs?
- Is there a choice of venue?
- Is Colorado law specified? If not, flag.

### Category 5: Change of Control
- Does a change of control trigger any rights (termination, renegotiation)?
- If ENAC is acquired, can the client terminate?
- If the client is acquired by a competitor, can ENAC exit?

### Category 6: Non-Assignment
- Can either party assign the agreement?
- Assignment on change of control: automatic or requires consent?
- ENAC should ensure it can assign to an acquirer.

### Category 7: Notice Period to Terminate Renewal
- How much notice is required to prevent automatic renewal?
- Is the notice period reasonable (30-90 days)?
- Flag auto-renewal provisions with short notice windows (< 30 days) as YELLOW.

### Category 8: Post-Termination Services
- Are there obligations that survive termination?
- Transition assistance requirements?
- Duration and compensation for post-termination services?

### Category 9: Termination for Convenience
- Can either party terminate for convenience?
- Notice period required?
- Payment obligations upon T4C?
- Flag: no payment upon T4C is RED.

### Category 10: Covenant Not to Sue
- Does either party agree not to sue the other?
- Scope: what claims are waived?
- Does this affect ENAC's ability to assert IP rights?

### Category 11: License Grant
- What rights are granted (use, reproduce, distribute, modify)?
- Exclusive or non-exclusive?
- Field of use, territory, and duration restrictions?
- Does the license survive termination?

### Category 12: IP Ownership Assignment
- Is there an assignment of IP to the client?
- Is Background IP carved out?
- Is "all work product" defined to include pre-existing methodology?
- Flag: any IP assignment without Background IP carve-out is RED.

### Category 13: Intellectual Property: Unlimited License
- Does the client receive an unlimited license to all IP?
- Is the license limited to deliverables or broader?
- Flag: unlimited license to all IP (including methodology) approaches assignment risk.

### Category 14: Exclusivity
- Is ENAC restricted from working with the client's competitors?
- Geographic or industry exclusivity?
- Duration of exclusivity?
- Flag: exclusivity without significant premium compensation is YELLOW.

### Category 15: Non-Compete
- Post-term restrictions on ENAC's ability to compete?
- Colorado C.R.S. 8-2-113: non-competes are extremely limited
- Duration, geography, and scope?
- Flag: any non-compete for a small professional services firm in Colorado is YELLOW-RED.

### Category 16: Non-Solicitation
- Restriction on hiring or soliciting client personnel?
- Restriction on soliciting client's customers?
- Duration: 12 months post-termination is generally acceptable; longer is aggressive.

### Category 17: Non-Disparagement
- Restriction on making negative statements about the other party?
- Mutual or one-sided?
- Does this affect ENAC's ability to describe lessons learned?

### Category 18: Competitive Restriction Exception
- Are there carve-outs to non-compete or exclusivity provisions?
- Pre-existing clients carved out?
- Specific industries or services excluded?

### Category 19: Source Code Escrow
- Is source code escrow required? (Unlikely for ENAC's consulting services)
- Release conditions?
- Maintenance obligations?

### Category 20: Audit Rights
- Can the client audit ENAC's books and records?
- Scope and frequency of audits?
- Who bears audit costs?
- Flag: unlimited audit rights or "right to inspect AI systems" is YELLOW.

### Category 21: Most Favored Nation (MFN)
- Is ENAC required to offer the client its best pricing?
- Does this create a price reduction right if ENAC prices lower for another client?
- Duration of MFN obligation?
- Flag: MFN without a market definition is YELLOW (Adams County PSA §4.2.2).

### Category 22: Price Restriction
- Fixed pricing vs. adjustable?
- Price increase limitations?
- Inflation adjustments permitted?

### Category 23: Minimum Commitment
- Is there a minimum revenue commitment from the client?
- Is there a minimum hours or deliverables commitment from ENAC?
- What are the consequences of missing minimum commitments?

### Category 24: Volume Restriction
- Caps on services volume?
- Maximum hours or deliverable counts?
- What happens if ENAC exceeds limits?

### Category 25: Revenue / Profit Sharing
- Does ENAC share in client revenue or cost savings?
- Success-based fee components?
- How are shared amounts calculated and when are they paid?

### Category 26: ROFR / ROFO / ROFN
- Right of first refusal, first offer, or first negotiation on future work?
- How long must ENAC wait for a response before engaging others?
- Does this restrict ENAC's ability to respond to competing RFPs?

### Category 27: Warranty Duration
- Warranty on deliverables: how long?
- What is the standard of warranty (fit for purpose, professional standard)?
- Remedy for breach of warranty (re-do or refund)?
- Flag: unlimited warranty duration is YELLOW.

### Category 28: Insurance
- Required coverage types and limits?
- Additional insured requirements?
- Are limits achievable with ENAC's current program?
- Flag: requirements ENAC cannot meet are RED.

### Category 29: Indemnification
- Is indemnification one-sided or mutual?
- What standard of fault triggers indemnification (negligence vs. strict)?
- Is there a cap on indemnification obligations?
- Flag: unlimited one-sided indemnification is RED.

### Category 30: Limitation of Liability
- Is there a cap on total liability?
- Is there a consequential damages waiver?
- Are there carve-outs for indemnification and confidentiality?
- Flag: no liability cap is RED; no consequential damages waiver is YELLOW.

### Category 31: Uncapped Liability
- Any provision that explicitly removes or carves out the liability cap?
- For ENAC: uncapped liability for IP infringement, data breach, or confidentiality breach?
- Flag: uncapped liability for any category should be reviewed carefully.

### Category 32: Liquidated Damages
- Are there pre-agreed damages for specific breaches?
- Are they reasonable (not a penalty)?
- Do they apply to ENAC's failure to meet deadlines or SLAs?

### Category 33: Anti-Assignment / Third Party Beneficiary
- Does the agreement confer rights on third parties?
- Are there intended third-party beneficiaries (e.g., county employees)?
- Flag: broad third-party beneficiary provisions expand who can sue ENAC.

### Category 34: Confidentiality
- Definition of confidential information (broad enough)?
- Standard exclusions (public domain, independent development)?
- Survival period?
- CORA interaction clause (for government contracts)?

### Category 35: Third Party IP Indemnification
- Is ENAC required to indemnify the client for third-party IP claims?
- Is this limited to ENAC's deliverables or broader?
- Is there a cap on this obligation?
- Flag: unlimited IP indemnification is RED.

### Category 36: Data Privacy / Security
- Data handling obligations?
- Security standards required?
- Breach notification obligations?
- PII retention and disposal requirements?
- Flag: obligations ENAC cannot meet are RED.

### Category 37: Force Majeure
- Is there a force majeure clause?
- What events are covered?
- What are the obligations during a force majeure event?

### Category 38: Dispute Resolution
- Is there a dispute resolution escalation ladder?
- Is mediation required before litigation?
- Arbitration vs. litigation?
- Venue and governing law?

### Category 39: Amendment and Waiver
- How can the agreement be amended (writing + signatures)?
- Is there a non-waiver clause?
- Can silence constitute waiver?

### Category 40: Entire Agreement
- Does this agreement supersede prior negotiations?
- Are there exhibits or attachments that are part of the agreement?
- Conflict resolution between agreement and exhibits (which governs)?

### Category 41: Severability and Survival
- If one clause is unenforceable, does the rest of the agreement survive?
- Which clauses survive termination (confidentiality, IP, indemnification)?
- Is survival duration specified?

---

## Output Structure

1. **Categories 1-5 (Administrative)**: Summary, flag anomalies
2. **Categories 6-18 (Operational Restrictions)**: Each with risk rating and redline if needed
3. **Categories 19-28 (Commercial Terms)**: Each with risk rating and redline if needed
4. **Categories 29-36 (Liability and Risk)**: Full analysis; these are the highest-risk categories
5. **Categories 37-41 (Governing Provisions)**: Summary, flag anomalies
6. **Missing categories**: Categories not addressed in the contract; note risk of absence
7. **Priority redlines**: Top 5 issues requiring negotiation

---

## Anti-Generic Rules

- NEVER skip IP Ownership Assignment (Category 12): it is the most important category for ENAC
- NEVER skip Limitation of Liability (Category 30): it defines ENAC's financial ceiling
- NEVER skip Indemnification (Category 29): it defines ENAC's financial floor
- NEVER accept an MFN clause (Category 21) without understanding what pricing it triggers
- NEVER sign a contract with uncapped liability (Category 31) in any category without human counsel review
