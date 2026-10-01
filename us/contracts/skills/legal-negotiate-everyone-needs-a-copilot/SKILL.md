---
name: legal-negotiate-everyone-needs-a-copilot
title: Legal Negotiation Skill
description: Counter-proposal and negotiation language generation. Use to create ideal, acceptable, and walk-away positions for problematic clauses with concrete replacement language and negotiation rationale.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/legal-negotiate
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
---

# Legal Negotiation Skill

Every negotiation has three positions. Know all three before you start. The party that enters a negotiation knowing only their ideal position is the one that makes concessions they did not plan to make.

---

## Three-Position Framework

For every clause requiring negotiation:

**Position 1: Ideal:** What ENAC asks for in the first redline. The position that fully protects ENAC's interests. Send this without apology; this is a starting position, not an overreach.

**Position 2: Acceptable:** What ENAC will accept after negotiation. Protects the core interest even if not the full position. Know this before sending Position 1.

**Position 3: Walk-Away:** The line below which ENAC signs nothing. If the other party will not move above this line, the deal is dead. Be certain about this before entering the negotiation.

---

## Applying the Framework

For each problematic clause, document:

```
Clause: [Section X.X: Clause title]
Current language: [Exact text from the contract]

Position 1 (Ideal):
Language: [Specific replacement text]
Rationale: [Why this protects ENAC; what risk it eliminates]

Position 2 (Acceptable):
Language: [Modified replacement text]
Rationale: [What ENAC gives up vs. Position 1; what risk remains but is manageable]
Condition: [What must be true for Position 2 to be acceptable, e.g., liability cap in place]

Position 3 (Walk-Away):
Language: [Minimum acceptable text]
Rationale: [Below this, the risk is not acceptable; explain why]
If rejected: [Escalate to GC / decline the engagement / require human counsel review]
```

---

## Standard Negotiation Positions for ENAC

These are pre-built positions for the clauses ENAC encounters most often in Colorado government contracts.

### Indemnification

**Current (Adams County PSA §7.1 typical):** "Contractor shall defend, indemnify, and hold harmless County from any and all claims arising from or related to Contractor's performance under this Agreement."

**Position 1 (Ideal):**
"Each party shall defend, indemnify, and hold harmless the other party from claims arising from the indemnifying party's own negligence or willful misconduct in the performance of this Agreement. Contractor's total aggregate liability under this Agreement shall not exceed the total fees paid by County to Contractor in the twelve months preceding the claim."

**Position 2 (Acceptable):**
"Contractor shall indemnify County for claims arising from Contractor's negligence in performance of this Agreement. Contractor's total liability shall not exceed the total fees paid under this Agreement."

**Position 3 (Walk-Away):**
"Contractor's liability under this Agreement shall not exceed the total fees paid under this Agreement." (Cap only: no mutual indemnification but at least the liability is capped.)

### IP Assignment

**Current (Adams County PSA §12.12 typical):** "All documentation, reports, and work product created under this Agreement shall become the property of the County."

**Position 1 (Ideal):**
Full Background IP carve-out language from `background-ip-schedule` skill. Contractor retains Background IP, County receives license to use in deliverables for internal purposes.

**Position 2 (Acceptable):**
Foreground IP (deliverables) assigned to County, Background IP retained by Contractor with explicit license-back. Contractor retains right to use de-identified learnings.

**Position 3 (Walk-Away):**
Any carve-out that explicitly preserves ENAC's pre-existing methodologies and tools: even if the language is less comprehensive than Position 1. Zero carve-out is a walk-away.

### Termination for Cause (No Cure Period)

**Current (Adams County PSA §11.1 typical):** "County may terminate for cause immediately upon written notice if Contractor fails to perform."

**Position 1 (Ideal):**
"County may terminate for cause upon thirty (30) days written notice specifying the alleged deficiency. If Contractor cures the deficiency within thirty (30) days of such notice, the Agreement shall continue in full force. If not cured within such period, termination shall be effective on the thirtieth day following the cure period."

**Position 2 (Acceptable):**
"County may terminate for cause upon fifteen (15) days written notice. Contractor shall have fifteen (15) days to cure any material breach before termination is effective."

**Position 3 (Walk-Away):**
Any notice period with any cure period, even if shorter than preferred. Zero notice + zero cure is the walk-away.

### Payment Terms (Missing)

**Position 1 (Ideal):**
"County shall pay Contractor within thirty (30) days of receipt of each invoice. Contractor shall invoice monthly in arrears for services performed in the preceding month. Invoices not paid within thirty (30) days shall accrue interest at the rate of 1.5% per month on the unpaid balance. Contractor may suspend performance upon sixty (60) days written notice if payment is more than sixty (60) days overdue."

**Position 2 (Acceptable):**
Net 30 from invoice receipt, monthly invoicing, interest on late payments at statutory rate, no suspension right.

**Position 3 (Walk-Away):**
Any defined payment timeline. No defined payment terms is a walk-away for engagements exceeding $25,000.

---

## Negotiation Tactics for Government Contracts

**What typically moves:**
- Liability caps (government lawyers often accept "fees paid" cap; it is a reasonable ask)
- Cure periods for T4D (standard professionalism expectation)
- Payment terms (procurement officers can often accept Net 30 if asked)
- Background IP carve-outs (especially if ENAC comes in with specific Schedule language)

**What typically does not move:**
- Governing law (Colorado, period)
- CORA obligations (the government cannot contract away statutory duties)
- Sovereign immunity / CGIA (the government cannot waive immunity by contract)
- EEO and nondiscrimination flow-downs (federal requirement in most programs)
- Immigration certification (statutory requirement)

**How to frame the asks:**
- Lead with reasonableness: "This is the standard we use with all our government clients."
- Provide the language: Do not ask them to draft it. Provide your redline.
- Separate the issues: Present IP, indemnity, and payment as independent asks. Don't bundle them.
- Acknowledge their constraints: "I understand you cannot waive immunity: we are not asking you to. We are asking that our liability be capped at the fees paid."

---

## Anti-Generic Rules

- NEVER enter a negotiation with only one position: know all three before the first call
- NEVER send a redline without specific replacement language: vague objections are ignored
- NEVER concede a RED clause without getting something in return
- NEVER negotiate against yourself: send Position 1 first and wait for their response
- NEVER accept the government's "non-negotiable" claim at face value on liability caps and cure periods: these are routinely negotiated
