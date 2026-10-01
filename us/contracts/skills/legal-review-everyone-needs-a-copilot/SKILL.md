---
name: legal-review-everyone-needs-a-copilot
title: Legal Review Skill
description: Full contract review with risk scoring. Use for clause-by-clause RED/YELLOW/GREEN analysis covering payment, IP, indemnification, termination, liability, confidentiality, scope, compliance, and missing protections.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/legal-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
---

# Legal Review Skill

A contract review is not a reading comprehension exercise. It is an adversarial analysis: assume the other party's lawyer wrote every clause to protect their client and extract maximum value from yours. Your job is to find every place where that happened and fix it before your client signs.

---

## Contract Safety Score

Score the contract 1-100 before and after redlines:

| Range | Assessment |
|-------|-----------|
| 85-100 | Acceptable with minor modifications |
| 70-84 | Acceptable after negotiating flagged items |
| 50-69 | Significant risk; major renegotiation required |
| 30-49 | High risk; do not sign without substantial revision |
| Below 30 | Walk-away risk; escalate to human counsel |

Scoring deductions per risk level:
- Each RED clause: -10 to -15 points
- Each YELLOW clause: -3 to -5 points
- Each critical missing protection: -5 to -10 points

---

## Review Framework

### Phase 1: Quick Read (5 minutes)
Read the contract in full before flagging anything. Understand what the parties are agreeing to do before analyzing risk. Identify the operative obligations on each side.

### Phase 2: Clause-by-Clause Analysis
Work through every material clause. Apply the risk matrix below. Flag every non-standard term.

### Phase 3: Missing Protection Scan
Run the missing protections checklist (see below). Items that should be there but aren't are as dangerous as bad clauses.

### Phase 4: Score and Summarize
Calculate Contract Safety Score. Prioritize issues by risk level. Draft the negotiation agenda.

---

## Clause Categories and Risk Matrix

### Payment Terms
- **GREEN:** Net 30 from invoice date, monthly invoicing, interest on late payments at statutory rate
- **YELLOW:** Net 45-60, payment milestones vague, no late payment remedy
- **RED:** No payment terms, payment "at County's discretion," milestone payments tied to acceptance criteria not defined

### IP Assignment
- **GREEN:** Foreground IP to client, Background IP retained by contractor with license-back, derivative IP stays with contractor
- **YELLOW:** Broad work-for-hire language that could be narrowed by carve-out, IP to client with license-back to contractor
- **RED:** All work product and documentation owned by client, no Background IP exception, "all tools and methodologies become client property"

### Indemnification
- **GREEN:** Mutual indemnification, negligence standard, cap at fees paid
- **YELLOW:** One-sided indemnification, broad scope but not unlimited, contractor bears all third-party IP claims
- **RED:** Unlimited, one-sided indemnification, strict liability standard, no cap, survives termination without sunset

### Limitation of Liability
- **GREEN:** Cap at total fees paid, consequential damages waiver (mutual), carveouts for indemnification and confidentiality
- **YELLOW:** Cap at some multiple of fees (e.g., 3x), consequential damages waiver not mutual
- **RED:** No cap, unlimited liability, no consequential damages waiver

### Termination
- **GREEN:** T4C with payment for work performed through termination date, T4D with 30-day notice and 30-day cure period
- **YELLOW:** T4C with limited wind-down payment, T4D with notice but no cure period
- **RED:** Termination for cause with no notice or cure, no payment on termination for convenience, immediate termination at will

### Confidentiality
- **GREEN:** Mutual, clearly defined confidential information, standard exceptions (public domain, independently developed), 3-5 year term, return/destruction on termination
- **YELLOW:** One-sided, vague definition of confidential information, no CORA interaction clause (for government contracts)
- **RED:** No confidentiality provision, ENAC materials are public records with no trade secret protection

### Scope and Change Orders
- **GREEN:** Scope defined by reference to proposal/SOW, change order process defined, changes require written agreement
- **YELLOW:** Scope broadly defined, no change order process, client can expand scope unilaterally "as reasonably requested"
- **RED:** Scope undefined, contractor obligated to deliver undefined "satisfaction," no limit on scope expansion

### Governing Law and Dispute Resolution
- **GREEN:** Colorado law, venue in Adams County or Denver, escalation ladder (informal, mediation, arbitration/litigation)
- **YELLOW:** Colorado law, no venue specified, litigation only
- **RED:** Unfavorable jurisdiction, no dispute resolution process, contractor waives jury trial

---

## Missing Protections Checklist

Run this after the clause review. Flag anything absent:

- [ ] Payment terms (amount, schedule, invoice process, late payment remedy)
- [ ] Acceptance criteria (how is a deliverable "accepted"?)
- [ ] Change order process (how are scope changes authorized?)
- [ ] Background IP carve-out
- [ ] Limitation of liability cap
- [ ] Consequential damages waiver
- [ ] Termination for convenience with payment on wind-down
- [ ] Cure period for termination for cause
- [ ] Confidentiality obligations (both directions)
- [ ] Force majeure
- [ ] Governing law and venue
- [ ] Dispute resolution escalation ladder
- [ ] Insurance requirements (are they achievable and proportionate?)
- [ ] Assignment restrictions (can either party assign without consent?)

---

## Output Structure

1. **Contract Safety Score**: [X]/100 with brief rationale
2. **RED Items**: Numbered list, highest risk first. Each item: clause reference, what it says, why it is red, required redline language
3. **YELLOW Items**: Same format. What to negotiate if possible
4. **Missing Protections**: What is absent and suggested clause language
5. **GREEN Confirmation**: Items that are acceptable
6. **Negotiation Priority Order**: What to fight for first, what to concede last
7. **Walk-Away Assessment**: Would a competent attorney recommend signing after negotiating the reds?

---

## Anti-Generic Rules

- NEVER score a contract without reading it in full
- NEVER flag something as GREEN without confirming the specific language, not just the clause heading
- NEVER issue a "looks OK" verdict on IP without confirming a Background IP carve-out
- NEVER miss unlimited indemnity: it is the most common catastrophic clause in government contracts
- NEVER recommend "accept with a note to monitor" on a RED clause: negotiate it or escalate
