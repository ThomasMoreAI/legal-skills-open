---
name: public-sector-contracting-cure-consulting-group
title: Public Sector Contracting
description: 'Reviews government contract terms: liability, IP, termination, non-appropriation, insurance. Use when reading a municipal, state, or federal contract form or choosing exceptions.'
author: Cure-Consulting-Group
author_url: https://github.com/Cure-Consulting-Group/ProductEngineeringSkills/tree/main/skills/business/public-sector-contracting
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: government-contracts
language: en
---

# Public Sector Contracting

Review government contract forms for the risks that matter, and decide what to push back on.

**This is not legal advice.** The purpose is to identify what warrants counsel, what is standard and should simply be accepted, and where the negotiating room actually exists — so that legal review is spent on the two or three clauses that matter rather than the whole document.

The governing asymmetry: **government standard forms are drafted entirely for the buyer, and are usually presented as non-negotiable.** Some of that is real (statutory requirements cannot be waived). Some is convention that yields to a well-framed exception. Knowing the difference is the skill.

## Pre-Processing (Auto-Context)

Context (pre-filled in Claude Code; in other runtimes run these commands first):

- Contract documents: !`ls 00-source/*ontract* 00-source/*orm* 2>/dev/null || ls *.pdf 2>/dev/null | head`
- Extracted text: !`ls 00-source/extracted/*.txt 2>/dev/null | head`
- Insurance schedule present: !`grep -l -i "insurance" 00-source/extracted/*.txt 2>/dev/null | head`

## Step 1: Find the clauses that carry real risk

Grep the extracted contract text rather than reading linearly — the dangerous clauses are scattered and often buried in ordinal-numbered articles.

```bash
grep -niE "indemnif|hold harmless|defend|limitation of liability|consequential|work.?made.?for.?hire|intellectual property|terminat|appropriat|assign|subcontract|audit|insurance|liquidated|warrant" \
  00-source/extracted/*ontract*.txt
```

Then assess each against the checklist below.

## Step 2: The risk checklist

### 🔴 Liability — is there a cap?

Most municipal forms have **no limitation of liability, no consequential-damages exclusion, and no mutual indemnity.** The vendor indemnifies; the buyer does not.

Read the indemnity trigger precisely. There is a large difference between:

- "arising from Consultant's negligent performance" — defensible
- "arising **directly or indirectly** out of this Agreement" — nearly unbounded

A duty to defend is separate from and broader than a duty to indemnify: it attaches on **allegation**, not on fault, and the defense cost is yours from day one.

**Weigh exposure against the work.** Uncapped liability on a static website is theoretical. Uncapped liability on a platform routing health inquiries, emergency escalation, or benefits eligibility for a vulnerable population is a bet-the-firm term.

**Ask for:** liability capped at fees paid or a multiple; consequential damages excluded; duty to defend narrowed to claims arising from your negligence, willful misconduct, or breach.

### 🔴 Intellectual property — who owns what you build?

Look for "works made for hire," blanket assignment, and clauses making "all records and recorded data" buyer property.

Many forms contain **internally contradictory IP language** — a works-made-for-hire sentence next to a sentence preserving vendor title in software. That contradiction is your opening: propose language that resolves it in a way both sides can live with.

**The standard resolution:** vendor retains pre-existing and independently developed IP, frameworks, and tooling; buyer owns its data and buyer-specific configuration and receives a perpetual, irrevocable, royalty-free license to the delivered instance.

**Read the anti-lock-in requirements as leverage, not opposition.** When a solicitation demands open data export, non-proprietary data models, and exit plans, the buyer's actual concern is *not being trapped* — not owning your framework. A clean "you own your data and configuration, we own the framework, and here is your export path" answers the real concern and is usually acceptable.

### 🔴 Termination for convenience

Common terms allow termination on **5–30 days' notice** with payment only for services already rendered.

Combined with back-loaded milestone pricing, this is how a small firm eats a half-finished build. Check three things:

1. **Notice period** — five days is aggressive; thirty is normal
2. **What gets paid** — work performed, or work performed plus wind-down costs?
3. **Who decides the amount in dispute** — some forms make the buyer's own counsel the final arbiter, which is not a dispute-resolution mechanism at all

**Mitigate structurally rather than by negotiating:** align milestone value with delivered value so earned value tracks work performed. This protects you without requiring the buyer to change a word.

### 🔴 Non-appropriation

Government contracts are subject to annual budget appropriation. The buyer may typically terminate — or **renegotiate rates** — on release of a proposed budget, and non-payment is often not default until a stated date.

This is statutory in most jurisdictions and **not negotiable**. The correct response is not to fight it but to **model the contract as one year at a time**. A "three-year contract with two option years" is not five years of committed revenue.

### 🟡 Payment terms and audit rights

Watch for: net 30–60 (sometimes measured from acceptance rather than invoice), pre-payment audit rights with withholding, final payment withheld until full satisfaction, and acceptance of final payment operating as a release of claims.

**Plan 60–90 days of receivable float.** For a small firm on a multi-year build, working capital is a more common failure mode than any legal term.

### 🟡 Assignment and subcontracting

Usually prohibited without prior written consent, with subcontractors required to be **named in the proposal** along with qualifications and credit references. Approval creates no privity — you remain fully responsible for their performance and insurance.

**Practical consequence:** identify every specialist you will need *before* submitting. Adding a subcontractor post-award requires consent you may not get.

### 🟡 Insurance schedule

Check limits **and** endorsements. Both can be hard.

| Coverage | Typical municipal ask | Watch for |
|---|---|---|
| Commercial General Liability | \$1M occ / \$2M agg | Additional insured, primary and non-contributory |
| Professional Liability (E&O) | \$1M–\$5M per claim | Often far above commercial norms |
| Cyber Liability | \$1M–\$2M | **Municipal additional-insured endorsement is frequently refused by carriers** |
| Umbrella / Excess | \$1M–\$5M | "Follow the form" basis |
| Auto Liability | \$1M CSL | Owned, hired, and non-owned |
| Workers' Comp / Disability | Statutory | State-specific forms; exemption filings if no employees |

Also check: carrier rating floor (commonly A.M. Best A or better), state licensing, waiver of subrogation, notice-of-cancellation period, and who absorbs deductibles.

**Get written quotes before the go/no-go decision.** Insurance must typically be in force *before work begins*, and failure to maintain it is grounds for suspension or termination. An unobtainable endorsement is a hard stop, and discovering it in week three of a bid is a self-inflicted wound.

### 🟢 Standard, usually accept without comment

Non-collusion warranties · anti-discrimination and civil-rights flow-downs · EEO · prevailing wage where applicable · conflict-of-interest disclosure · independent contractor status · compliance with applicable law · certifications (state-specific divestment acts, fair-employment principles, debarment) · governing law and venue at the buyer's seat · buyer disclaims proposal preparation costs · governing-body approval required before any binding contract

Taking exception to these signals inexperience and costs credibility that you need for the exceptions that matter.

## Step 3: Public-records exposure

Proposals submitted to government are generally subject to public-records law (FOIA, FOIL, state equivalents), and **the accepted proposal is often incorporated into the resulting contract**.

Most solicitations offer a marking procedure for trade secrets and competitively sensitive information. Where offered, follow it **exactly** — typically a notice block at the front, page-level marking, and written justification per claim.

**Mark selectively.** Over-marking reads as evasive to evaluators and buyers often reject blanket claims anyway. The usual right answer: mark detailed pricing methodology and security architecture specifics; leave the narrative open.

## Step 4: Certifications and registrations

Long-lead items that gate submission. Start these before the bid, not during it.

| Item | Typical lead time |
|---|---|
| Portal registration (SAM.gov, state/regional systems, BidNet) | Days to weeks |
| State vendor registration / tax clearance | Days to weeks |
| Corporate disclosure questionnaires | Hours, but needs records |
| Notarization of certifications | Book in advance |
| MBE/WBE/SDVOB/small-business certification | **Months** |
| SOC 2 Type II | **6–12 months** |
| Bonding capacity | Weeks |

**Distinguish a goal from a requirement.** "The City's goal is to encourage participation by…" is aspirational. "Bidders must subcontract N% to certified firms" is a bar with real consequences.

## Step 5: Exceptions strategy

Most solicitations include an Exceptions section. **Silence is acceptance** — and the proposal typically becomes part of the contract, so an unstated objection is waived.

Rank exceptions by value and take only the ones worth the credibility cost:

| Tier | Take it? |
|---|---|
| Bet-the-firm terms — uncapped liability, IP that destroys your business model | **Yes.** Winning on these terms can be worse than losing |
| Structural economics — open-ended usage risk, unworkable payment timing | **Usually**, framed as clarifications |
| Preference items — venue, notice periods, minor process | **No.** Not worth the credibility |
| Statutory terms — non-appropriation, prevailing wage, civil rights | **Never.** They cannot be waived and asking signals inexperience |

**Framing matters more than substance.** Compare:

> ❌ "Consultant does not accept Article EIGHTH."
> ✅ "Consultant proposes the following clarification to Article EIGHTH, consistent with the City's data-portability objectives in T-13/T-14: …"

Offer the alternative language. An exception with proposed text is a negotiation; an exception without it is a refusal.

⚠️ **The real trade-off:** buyers may reject proposals that "do not conform in all material respects," and evaluators can read a long exceptions list as difficulty. Two or three well-framed exceptions read as a sophisticated counterparty. Ten reads as a problem.

## Step 6: Produce the review

Write `01-analysis/contract-risk-review.md`:

1. **🔴 High** — resolve before committing. Each with: what the clause says, why it matters *for this specific work*, and the ask
2. **🟡 Medium** — price it in. Each with the mitigation
3. **🟢 Low** — accept, with a one-line note
4. **Exceptions draft position** — ranked, with proposed language and an honest note on the credibility trade-off

Open with the disclaimer that it is not legal advice and mark what needs counsel.

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Reading the contract only after winning | Terms are set at submission; silence waives objections |
| Taking exception to statutory terms | Cannot be waived; signals inexperience |
| Taking no exceptions at all | Waives uncapped liability and IP assignment by default |
| Exceptions without proposed language | Reads as refusal, not negotiation |
| Assuming insurance is obtainable | Some endorsements are routinely refused by carriers |
| Treating a multi-year term as committed revenue | Non-appropriation makes it year-to-year |
| Ignoring the works-made-for-hire clause | Can transfer the IP your business model depends on |
| Over-marking as confidential | Reads as evasive; blanket claims get rejected anyway |

## Handoff

- Requirement extraction and compliance → `rfp-evaluation`
- Whether the risk profile justifies the pursuit → `bid-decision`
- Commercial contract review → the `contract-reviewer` agent (Claude Code), or a general contract review elsewhere
- Compliance program design → `compliance-architect`
