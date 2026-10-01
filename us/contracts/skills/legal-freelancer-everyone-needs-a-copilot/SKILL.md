---
name: legal-freelancer-everyone-needs-a-copilot
title: Legal Freelancer Skill
description: Contractor-perspective contract review. Use to flag IP assignment traps, unlimited liability, missing payment terms, scope creep, unilateral termination, non-compete overreach, and missing protections.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/legal-freelancer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
---

# Legal Freelancer Skill

When a client sends their paper, every clause was written by their lawyer to protect them. That is normal. Your job is to find the traps before you sign, and to distinguish between standard boilerplate (accept it) and genuine risk exposure (fix it).

---

## The Contractor Mindset

Small professional services firms reviewing client paper face asymmetric information: the client's lawyer has seen this contract hundreds of times; you are seeing it for the first time. The traps are in the definitions section, in what work product means, in the word "all," and in what the contract does not say about acceptance and payment.

Read for traps, not just for what sounds reasonable on the surface.

---

## The Seven Traps

### Trap 1: IP Assignment Trap

**Danger phrases:**
- "All work product created under this Agreement is owned by Client"
- "Work Product includes all deliverables, documentation, tools, methodologies, and materials"
- "Contractor agrees this is a work-made-for-hire arrangement"
- "Contractor assigns to Client all right, title, and interest in any intellectual property"

**Why it is dangerous:** These clauses, read literally, assign ENAC's pre-existing methodology, frameworks, and tools to the client. Every future engagement that uses the same methodology is now potentially infringing.

**What to look for:** Is there a Background IP carve-out? Does "work product" include pre-existing materials? Is "methodology" or "tools" in the definition of deliverables?

**Fix:** Insert the Background IP carve-out language from the `background-ip-schedule` skill. If the client refuses any carve-out: walk away.

---

### Trap 2: Unlimited Liability Exposure

**Danger phrases:**
- No limitation of liability clause
- "Contractor shall be liable for all damages arising from any breach"
- "Contractor shall indemnify Client against any and all claims"
- Indemnity that covers third-party claims without a negligence standard
- No consequential damages waiver

**Why it is dangerous:** Without a liability cap, a single engagement gone wrong can exceed the entire contract value many times over. A consequential damages exposure can include lost profits, lost business opportunities, and reputational harm: numbers disconnected from what ENAC was paid.

**What to look for:** Is there a liability cap? Is it at least equal to fees paid? Is there a consequential damages waiver? Is indemnification mutual or one-sided? Is there a negligence standard or is it strict liability?

**Fix:** Add liability cap at fees paid, mutual consequential damages waiver, negligence standard for indemnification.

---

### Trap 3: Missing Payment Terms

**Danger phrases:**
- No payment timeline specified
- "Payment upon acceptance of deliverables" (without acceptance criteria)
- "Payment at Client's discretion"
- No invoice process defined
- No late payment remedy

**Why it is dangerous:** ENAC completes the work and then waits. Without a payment timeline, "reasonable time" is the legal standard. Without acceptance criteria, the client controls when deliverables are "accepted" and therefore when payment is due.

**What to look for:** When does the payment clock start? Is invoicing defined? Is there an acceptance timeline or does the client have unlimited time to accept/reject?

**Fix:** Net 30 from invoice, monthly invoicing, deemed acceptance if no rejection within 15 business days, interest on late payment.

---

### Trap 4: Vague Scope That Enables Scope Creep

**Danger phrases:**
- "As may be reasonably requested by Client"
- "And such other services as may be needed"
- Scope defined by reference to a general description, not a specific deliverable list
- "Contractor shall ensure Client is satisfied with all deliverables"
- "Additional services shall be provided at no extra charge when related to the engagement"

**Why it is dangerous:** Every extra request becomes a contractual obligation. Without a defined scope and a change order process, ENAC works for free on everything the client calls "in scope."

**What to look for:** Is scope defined specifically? Is there a change order clause? Can the client expand scope unilaterally?

**Fix:** Define scope by reference to the proposal/SOW. Require a written change order for any scope expansion. State that additional work beyond scope will be invoiced at ENAC's standard rates.

---

### Trap 5: Unilateral Termination With No Pay-on-Completion

**Danger phrases:**
- "Client may terminate this Agreement at any time without cause"
- "Upon termination, Client owes no further amounts to Contractor"
- No termination for convenience payment
- Termination for cause with no notice or cure period
- "Client may terminate immediately upon notice"

**Why it is dangerous:** Work is completed but unpaid. ENAC has no right to be compensated for the value delivered before termination.

**What to look for:** Can the client terminate for convenience? If so, what does ENAC receive? Is there a cure period before termination for default? Is there a wind-down payment?

**Fix:** Payment for work performed through termination date plus reasonable wind-down costs. Cure period for T4D. T4C requires 30 days notice minimum.

---

### Trap 6: Non-Compete and Non-Solicitation Overreach

**Danger phrases:**
- "Contractor agrees not to provide similar services to any other client in [industry/geography] for [period]"
- "Contractor agrees not to solicit any Client personnel for [period]"
- "Contractor agrees not to hire Client personnel for [period]"
- Broad non-solicitation of Client customers or prospects

**Why it is dangerous:** ENAC serves multiple clients. A broad non-compete or non-solicitation can prohibit ENAC from doing its core business.

**What to look for:** Is there any restriction on ENAC's ability to work with other clients? What is the scope, geography, and duration? Is this even enforceable in Colorado (narrow restrictions only)?

**Fix:** Non-competes are extremely limited in Colorado (C.R.S. 8-2-113, 2022). Narrow non-solicitation of personnel is generally acceptable (not soliciting specific individuals during engagement and for 12 months after). Reject any restriction on serving other clients in the same industry.

---

### Trap 7: Missing Acceptance Criteria

**Danger phrases:**
- No acceptance process defined
- "Deliverables accepted when Client is satisfied"
- Client has unlimited time to accept or reject
- Rejection rights with no definition of what constitutes a deficiency
- "Client's reasonable satisfaction" as the acceptance standard

**Why it is dangerous:** The client can withhold payment indefinitely by refusing to accept deliverables. Without an objective acceptance standard and a timeline, ENAC has no legal basis to demand payment.

**What to look for:** Is there an acceptance process? Is there a timeline? Is there a deemed acceptance provision? Is the rejection standard objective or purely subjective?

**Fix:** Define acceptance criteria in the SOW. Add 15-business-day review period with written notice of specific deficiencies required. Deemed acceptance if no written rejection within the review period.

---

## Quick Review Workflow

1. Find the definitions section: read every defined term carefully
2. Find the IP and work product clauses: apply Trap 1
3. Find the indemnification and liability clauses: apply Trap 2
4. Find the payment section: apply Trap 3
5. Find the scope and services section: apply Trap 4
6. Find the termination section: apply Trap 5
7. Find any non-compete or restrictive covenant: apply Trap 6
8. Find the acceptance or deliverables section: apply Trap 7
9. Run the missing protections checklist from `legal-missing` skill

---

## Output Structure

1. **Trap findings**: Each trap identified with clause reference, specific danger language, and recommended fix
2. **Acceptance / Decline recommendation**: Sign as-is / Negotiate / Walk away
3. **Redline priority list**: What to fix first
4. **Non-negotiable items**: What ENAC will not sign under any version of this language

---

## Anti-Generic Rules

- NEVER skip the definitions section: most traps are hidden in how "work product" or "deliverables" is defined
- NEVER accept "work-made-for-hire" language without a Background IP carve-out
- NEVER accept no payment timeline for an engagement over $5,000
- NEVER accept unlimited liability without a cap: it is always negotiable
- NEVER sign a non-compete in Colorado without checking the 2022 C.R.S. 8-2-113 restrictions
