---
name: draft-notice-of-arbitration-sboghossian
title: Notice of Arbitration / Request for Arbitration
description: Use when drafting a notice of arbitration or request for arbitration to commence institutional or ad-hoc arbitral proceedings. Covers the required content under LCIA, DIAC, ICC, SCCA, UNCITRAL, and DIFC-LCIA (now DIAC) rules, with tactical guidance on claim preservation, parallel court relief, time-bar verification, and filing checklists. Triggers on "notice of arbitration", "request for arbitration", "commence arbitration", or "initiate arbitral proceedings" requests.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-notice-of-arbitration
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: arbitration
language: en
---

# Notice of Arbitration / Request for Arbitration

## When to use this

Use this skill when a claimant has a dispute and wishes to initiate arbitral proceedings under an arbitration clause in a contract or a standalone arbitration agreement. The notice of arbitration / request for arbitration is the founding document of the arbitration: it starts the proceedings, preserves claims, triggers the time-bar cutoff, and initiates the tribunal formation process.

Before drafting:
1. Verify the arbitration agreement exists and is valid in the governing law
2. Confirm any condition precedent to arbitration has been satisfied (escalation clause, mediation obligation — see [[draft-mediation-agreement]])
3. Confirm the applicable limitation period has not expired (or that this filing stops it)
4. Identify the applicable institutional rules or ad-hoc rules
5. Calculate and arrange the filing fee payment

## Required content (most institutional rules)

All major institutional rules require the following minimum content:

| Element | Notes |
|---------|-------|
| Claimant's full name + address + contact | Include counsel details if filing through counsel |
| Respondent's full name + address | Accurate address critical for notification by the institution |
| Reference to the arbitration agreement | Identify the clause and the contract; attach a copy |
| Reference to the contract giving rise to the dispute | Identify and attach |
| Description of the nature and circumstances of the dispute | Factual narrative; sufficient to identify the controversy |
| Statement of relief sought | Including quantification of monetary claims where possible |
| Proposal (if not already fixed) on: number of arbitrators; seat; language | Many clauses fix these; if not, propose |
| Filing fee payment | Each institution has a fee schedule; payment must accompany filing |

## Institution-specific requirements

### LCIA (London Court of International Arbitration) — Art. 1 of LCIA Rules 2020
- Written **Request for Arbitration** submitted via LCIA Casework Portal
- Must include: the LCIA's registration fee; a soft copy of all documents referred to; confirmation of compliance with any multi-tier ADR obligation
- LCIA Rule 1.1 specifies each required element
- Response from Respondent due within 28 days of LCIA notification
- LCIA registered office: London; proceedings may proceed in any seat

### ICC (International Chamber of Commerce) — Art. 4 of ICC Rules 2021
- **Request for Arbitration** filed with ICC Secretariat (Dispute Services)
- Must include: filing fee (per ICC schedule, based on amount in dispute); list of all parties (multi-party cases); brief description of the dispute; relief sought; any information relevant to number/appointment of arbitrators
- Response from Respondent (Answer) due within 30 days
- ICC confirms filing once all requirements satisfied; date of receipt by ICC Secretariat is the commencement date for limitation purposes

### DIAC (Dubai International Arbitration Centre) — Art. 4 of DIAC Rules 2022
- **Request for Arbitration** filed electronically on DIAC online portal
- Must include all elements above + any DIAC emergency arbitrator request (if interim relief urgently needed)
- DIAC replaced DIFC-LCIA in 2021; existing DIFC-LCIA clauses are now administered by DIAC unless parties agree otherwise
- Commencement date: date DIAC receives the complete Request; important for limitation period purposes

### SCCA (Saudi Center for Commercial Arbitration) — SCCA Rules 2023
- **Request for Arbitration** per SCCA Rules Art. 3; filed via SCCA online portal
- SCCA is the preferred institution for disputes involving Saudi parties or Saudi law
- Arabic-language proceedings available and common
- SCCA emergency arbitrator mechanism available

### UNCITRAL (Ad-hoc) — Art. 3 of UNCITRAL Arbitration Rules 2013
- **Notice of Arbitration** sent directly to Respondent (no institution receives it unless an appointing authority has been designated)
- Must include: invitation to designate appointing authority (if not agreed); proposed seat and rules for appointment if no arbitration agreement on point
- UNCITRAL arbitrations are flexible but require more procedural management by the parties; commonly used in investor-state arbitrations (ISDS)

### DIFC Courts Small Claims Tribunal (SCT)
Not arbitration, but note: for DIFC-nexus claims under USD 200,000, the DIFC SCT offers a faster resolution path; no arbitration required.

## Content of the notice — drafting guidance

### 1. Introduction paragraph
State the commencement in plain language: "Pursuant to [Article X] of the [Arbitration Agreement / Contract], [Claimant] hereby commences arbitration against [Respondent] in accordance with the [DIAC/ICC/LCIA] Rules."

### 2. Parties
Full legal name, entity type, registration number, address, email, and counsel details for each party. For corporate parties: confirm which entity entered the arbitration agreement (entity naming is a common trap — verify the contracting entity against the exact language of the arbitration clause).

### 3. Arbitration agreement and contract
- Identify the contract by full title, date, and parties
- Quote the arbitration clause verbatim in the notice (or attach the relevant page)
- If the dispute involves multiple contracts (or a question of whether the clause covers this dispute), address this proactively

### 4. Summary of the dispute
A neutral-to-claimant factual narrative. Be sufficient to establish the nature of the dispute and the relevant time frame. This is not the full statement of claim — keep it concise (2-5 pages maximum for most disputes at this stage).

Avoid over-disclosing legal strategy or evidence at this stage. The full statement of claim comes later in the proceedings.

### 5. Claims and relief sought
- State every claim you intend to pursue: breach of contract, fraud, negligence, unjust enrichment, specific performance, etc.
- Quantify each head of loss where possible (even if subject to refinement)
- Include: principal amount, interest (rate and period), costs
- Reserve the right to amend, expand, or refine claims as the proceedings develop
- "Claimant reserves the right to supplement or amend this Notice as additional information becomes available and as discovery / disclosure progresses"

**Important**: claims not raised at this stage may still be added later under most rules (with leave), but the commencement date for limitation purposes is the date of this notice. File broadly to protect all potential claims.

### 6. Proposed arbitration mechanics (if not fixed)
If the arbitration clause does not specify:
- **Number of arbitrators**: propose 1 (simpler / smaller disputes) or 3 (complex / high-value disputes)
- **Seat**: proposed seat determines the supervisory court and the curial law of the arbitration
- **Language**: proposed language(s) of proceedings
- **Appointment mechanism**: if sole arbitrator, propose a method; if three arbitrators, confirm that each party nominates one and the two nominees choose the third (standard)

## Tactical considerations

### Preserve all claims — file broadly
The notice is the last moment before the limitation period is conclusively stopped (in most systems). File broadly:
- Include all causes of action, including those requiring further investigation
- Include all parties who may be liable, even if you are uncertain (and you can discontinue against them later)
- Include all heads of loss, even provisional estimates

### Do not over-disclose strategy
The notice is not a full memorial or statement of case. Avoid:
- Disclosing your evidence strategy
- Disclosing documentary evidence not needed to establish the claim
- Detailed legal arguments (save for the memorial or statement of case)

A Respondent who reads your notice should understand the dispute but not know your theory of the case.

### Time-bar / limitation verification
Before filing, confirm the applicable limitation period and that it has not expired:
- Under the contract (contractual limitation periods)
- Under the governing law of the contract (statutory limitations)
- Under the law of the seat (some laws impose separate limitation periods on arbitration proceedings)
In MENA:
- UAE: generally 10 years for civil/commercial; shorter for specific claim types
- KSA: 5 years for commercial; 1 year for some labor and insurance claims
- LB: 10 years for most obligations; shorter for specific categories
- DIFC: 6 years for contract; 6 years for tort

### Parallel court action for interim relief
Filing the notice of arbitration does not prevent seeking urgent interim relief from a court (injunction, freezing order, attachment of assets). Many institutional rules expressly preserve this right. Consider:
- Whether assets are at risk of dissipation before an award is obtained
- Whether the arbitration clause allows for interim relief before tribunalconstitution
- In UAE: DIFC and onshore courts can grant provisional attachments concurrently with arbitration proceedings

## Post-filing checklist

- [ ] Notice / Request filed with institution (or sent to Respondent for UNCITRAL)
- [ ] Filing fee paid and payment confirmed
- [ ] Arbitration agreement and contract attached
- [ ] Copy of notice served on all Respondents
- [ ] Internal calendar: Response deadline from Respondent (typically 28-30 days)
- [ ] Arbitrator nomination prepared (if party-nomination required)
- [ ] Consider interim relief application (court or emergency arbitrator)
- [ ] Preserve and organize document evidence
- [ ] Notify relevant insurers if D&O, E&O, or litigation funding involved

## Related skills

- [[draft-litigation-complaint]]
- [[draft-mediation-agreement]]
- [[review-arbitration-clause]]
- [[draft-statement-of-defense]]
