---
name: prompt-pack-arbitration-cost-submission-sboghossian
title: Arbitration Cost Submission
description: Use when drafting a costs submission in an international arbitration proceeding seeking recovery of a party's legal fees, expert fees, arbitration institution costs, and other recoverable expenses. Arbitration practice area; covers DIAC, ICC, LCIA, SIAC, and CRCICA cost recovery principles with MENA-specific notes on cost allocation practices and tribunal discretion.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-arbitration-cost-submission
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: arbitration
language: en
---

# Arbitration Cost Submission

## When to use this

Use this skill when counsel needs to prepare a **costs submission** at the conclusion of an arbitration proceeding, seeking the tribunal's order that costs (legal fees, expert fees, arbitration costs) be borne by the opposing party.

Costs submissions typically arise:
- At the end of the hearing phase when the tribunal requests cost submissions
- After a separate procedural order or award has been issued
- In response to the opposing party's cost claim
- When a partial award on jurisdiction or liability invites cost submissions

The quality of a costs submission directly affects how much the tribunal orders in cost recovery — a well-structured, documented submission with clear cost recovery principles consistently wins more than a vague list of fees.

---

## Prompt template

> Draft a costs submission for [Party] in [Arbitration Case Reference] seeking recovery of legal costs and expenses. Include detailed breakdown of legal fees, expert fees, arbitration costs, and other expenses with supporting documentation and applicable cost principles.

Use [[conversation-clarifying-questions]] to elicit `[bracketed]` inputs before drafting.

---

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Party name and role (Claimant/Respondent) | The submission is party-specific |
| Arbitration case reference | Identifies the proceeding |
| Applicable institutional rules | Cost recovery principles differ by institution |
| Total costs claimed (with breakdown) | Core substantive content |
| Outcome of the arbitration | Cost recovery arguments are anchored to success/failure |
| Tribunal's procedural order on costs (if any) | Some tribunals issue specific guidance on the costs submission format |

---

## Document structure

### 1. Introduction
- Case reference and parties
- Brief statement of the outcome (Claimant/Respondent prevailed on all/most/some claims)
- Summary of total costs claimed
- Relief sought: "The Claimant respectfully requests that the Tribunal order the Respondent to bear the Claimant's costs of the arbitration in the amount of USD [X]."

### 2. Applicable legal principles on costs

Each institution's rules address cost recovery differently. Summarize the applicable rule and the tribunal's discretion:

| Institution | Cost rule |
|-------------|----------|
| ICC (2021 Rules Art. 38) | Tribunal shall fix costs; may allocate between parties as appropriate; considers outcome and other relevant circumstances |
| LCIA (2020 Rules Art. 28) | "Costs follow the event" as the starting point, unless the tribunal considers it inappropriate; recovery of reasonable legal costs |
| SIAC (2016 Rules Rule 35) | Tribunal has full discretion; considers the outcome and all relevant circumstances |
| DIAC (2022 Rules Art. 41) | Tribunal determines and allocates costs; considers all relevant circumstances |
| CRCICA (2011 Rules Art. 40) | Tribunal fixes and allocates costs in the award; considers outcome |
| UNCITRAL (2013 Rules Art. 42) | Tribunal fixes and allocates costs; "costs follow the event" principle referenced |

**General principle** (applicable across all institutions): a party that substantially prevails on the merits is ordinarily entitled to recover its reasonable costs, subject to the tribunal's discretion. Key arguments for full cost recovery:
- The Respondent's conduct made the arbitration necessary and/or prolonged it
- The Claimant succeeded on the main claim
- The costs claimed are proportionate to the amount in dispute and the complexity of the issues
- The costs were reasonably incurred

**Arguments for partial recovery** (to pre-empt if full recovery is sought):
- Success was partial — seek full recovery on issues won; accept reduced recovery on issues lost
- Proportionality: costs are proportionate to claims upheld

### 3. Cost schedule — legal fees

Present as a table:

| Timekeeper | Role | Hours | Rate (USD/hr) | Amount |
|-----------|------|-------|--------------|--------|
| [Lead counsel] | Partner | XX | USD X,XXX | USD XX,XXX |
| [Associate 1] | Senior associate | XX | USD XXX | USD XX,XXX |
| [Associate 2] | Associate | XX | USD XXX | USD XX,XXX |
| **Total legal fees** | | | | **USD XXX,XXX** |

Supporting documentation: attach time records (redacted for privilege where necessary but sufficiently detailed to show the work done and its connection to the arbitration).

**Reasonableness arguments**:
- Rates are consistent with the market for counsel of this experience level in this seat
- Hours are appropriate for the complexity and size of this dispute
- Each phase of work was necessary (reference major procedural steps: pleadings, document production, witness statements, expert reports, hearing preparation, post-hearing briefs)

### 4. Cost schedule — expert fees

| Expert | Expertise | Work done | Amount |
|--------|----------|----------|--------|
| [Expert 1] | Quantum/damages | Report + hearing attendance | USD XX,XXX |
| [Expert 2] | Technical | Report + concurrent evidence session | USD XX,XXX |
| **Total expert fees** | | | **USD XX,XXX** |

Supporting documentation: invoices; expert fee agreements; explanation of why each expert was necessary.

### 5. Cost schedule — arbitration institutional costs

| Item | Amount |
|------|--------|
| Filing fee | USD X,XXX |
| Administrative fee | USD XX,XXX |
| Arbitrators' fees (paid portion) | USD XX,XXX |
| **Total institutional costs** | **USD XX,XXX** |

Note: the final arbitrators' fees are typically set by the institution or tribunal after the award. This submission covers the costs already paid, with a note that the full arbitrators' fee will be known only at the time of the final award.

### 6. Cost schedule — other recoverable expenses

| Item | Amount |
|------|--------|
| Hearing room rental | USD X,XXX |
| Transcript | USD X,XXX |
| Travel and accommodation (hearing attendance) | USD X,XXX |
| Document production / e-discovery costs | USD X,XXX |
| Translation costs | USD X,XXX |
| **Total other expenses** | **USD X,XXX** |

### 7. Total costs claimed

| Category | Amount |
|---------|--------|
| Legal fees | USD XXX,XXX |
| Expert fees | USD XX,XXX |
| Institutional costs | USD XX,XXX |
| Other expenses | USD XX,XXX |
| **TOTAL** | **USD XXX,XXX** |

### 8. Conduct and efficiency arguments

This section strengthens the case for full recovery by showing the other party's conduct:
- Respondent's conduct that unnecessarily prolonged proceedings (late filings, excessive document requests, unfounded jurisdictional objections)
- Claimant's conduct that was efficient and proportionate
- Any unreasonable offers to settle that were rejected by Respondent (can support argument for full indemnity costs)

### 9. Relief sought

> For the foregoing reasons, [Party] respectfully requests that the Tribunal:
> 1. Order [Opposing Party] to pay [Party's] costs of the arbitration in the amount of USD [X], representing [Party's] legal fees, expert fees, institutional costs, and other expenses as set out above;
> 2. Order that interest at the rate of [X%] per annum shall accrue on such costs from the date of the award until payment; and
> 3. Grant such further or other relief as the Tribunal considers just.

---

## Jurisdictional and institutional notes

### DIAC / UAE
UAE arbitral tribunals have historically been somewhat restrained in cost awards compared to LCIA tribunals. A well-documented submission significantly improves recovery. Arbitrators' fees in Dubai are often higher per day than in London or Singapore but the total is usually lower due to shorter hearings.

### LCIA
LCIA tribunals apply "costs follow the event" most consistently. A party that wins on the merits can reasonably expect to recover 60–75% of reasonable legal costs. Document the rates paid by reference to the LCIA's own cost guidance notes.

### ICC
ICC tribunals have wide discretion. The ICC's administrative fee structure is relatively high; claiming recovery of the full ICC administrative fee is appropriate if the Claimant prevailed.

### KSA / SCCA
Saudi arbitral tribunals tend to order each party to bear its own costs, particularly in disputes involving Saudi government entities. Argue cost recovery on specific grounds (bad faith, clearly unmeritorious defences) rather than relying solely on "costs follow the event."

---

## Common mistakes

- Submitting costs without a time record — tribunals routinely deny unsubstantiated cost claims
- No proportionality argument — a USD 2M cost claim in a USD 5M dispute without proportionality argument will be reduced
- Failing to recover institutional costs actually paid — these are straightforwardly recoverable if the party prevailed
- No interest claim on costs — most institutional rules permit this; it is routinely ordered

---

## Related skills

- [[prompt-pack-arbitration-agreement-clause]] — the clause that governs costs recovery
- [[prompt-pack-arbitration-clause-comparison]] — institutional rules comparison including cost provisions
- [[prompt-pack-award-enforcement-application]] — enforcing the costs award
- [[kb-arbitration-mena]] — MENA arbitration law and practice reference
