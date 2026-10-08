---
name: pa-workflow-inhouse-cross-functional-translation-sboghossian
title: In-House — Cross-Functional Translation
description: Use when an in-house lawyer needs to translate legal concepts, obligations, or risk assessments into the language of a specific non-legal audience — engineers, sales, executives, or the board. Each audience receives a framing tailored to their decision-making context and vocabulary. Triggers when a legal concept or contract obligation must be communicated to a non-lawyer stakeholder for action or decision.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-inhouse-cross-functional-translation
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# In-House — Cross-Functional Translation

The most important skill an in-house lawyer develops is translation — not between languages, but between the legal world and the world of the people whose decisions they support. An engineer does not think about rights and obligations; they think about specs and APIs. A salesperson does not think about indemnities; they think about commissions and close dates. A board director thinks about risk-adjusted returns, not legal standards. This skill governs how Claude assists in-house lawyers to communicate legal content appropriately to each audience.

## Purpose

Reframe legal concepts, obligations, or risk findings in the specific vocabulary and decision frame of four primary audiences:
1. Engineering team — rights, obligations, and constraints in technical terms
2. Sales / commercial team — contract terms in commercial, deal-impact terms
3. Executive team — risk-balanced decision framing
4. Board — governance, materiality, and fiduciary framing

## Inputs

| Input | Why it matters |
|---|---|
| Legal concept / clause / obligation | The specific thing to translate |
| Target audience | Determines vocabulary, level of detail, and framing |
| Decision required | What does the audience need to decide or do? |
| Urgency | Is this a blocking issue or an FYI? |
| Risk level | Informs how strongly to flag the issue |

## Translation by audience

### Engineering team

Engineers care about: what specifically are we required to do or not do, who is responsible, what happens if we fail, and can this be automated or monitored?

**Legal framing:** "Under the data processing agreement, we must implement appropriate technical and organisational measures to protect personal data in accordance with GDPR Article 32, including encryption and access controls."

**Engineering translation:**
- "Encrypt all PII at rest and in transit — AES-256 minimum."
- "Access controls: only authorised personnel can access personal data. Log every access."
- "We need an incident response plan in code: if a breach occurs, we must notify the DPA within 72 hours."
- "Document what measures we've implemented — we may need to show them to the regulator."

Key technique: convert legal obligations into specific technical requirements. Replace "appropriate measures" with the specific standard. Convert "in a timely manner" to a specific SLA in hours.

**What engineers need from a legal translation:**
- Concrete, measurable requirements
- A clear scope (which systems, which data, which users)
- The consequence of failure in engineering terms (service termination, liability, audit)
- Whether there is an existing technical standard that satisfies the legal obligation

### Sales / commercial team

Salespeople care about: can we close this deal, what is the risk to commission and deal closure, and what do I need to do right now?

**Legal framing:** "The customer's standard terms include an uncapped indemnity for IP infringement and a 24-hour cure period for service outages."

**Sales translation:**
- "This is a risk flag — it's not a deal blocker but we need legal to redline before you sign."
- "The IP clause means we'd cover all their legal costs if our product infringed someone's patent. That's potentially unlimited. We never sign uncapped. Tell them our cap is 12 months of fees."
- "The 24-hour cure period for outages is too tight — our SLA is 99.9% uptime with 72-hour remediation. Push back to 5 business days."
- "What you should say to the buyer: 'Our legal team has two changes to your standard terms — an IP indemnity cap and an adjusted cure period. Can your team turn these in 2 days so we don't delay the close?'"

Key technique: give the salesperson the specific words to say to the counterparty. They are not lawyers and should not be making legal arguments — but they need a clear commercial message.

**What sales needs from a legal translation:**
- Is this a deal blocker or a deal modifier?
- What specifically should I say to the customer?
- What is the commercial argument for the change we want?
- How urgently does legal need to be involved?

### Executive team

Executives care about: what is the risk, what is the cost or opportunity, what decision do I need to make, and what is the recommendation?

**Legal framing:** "The proposed acquisition target has three pending employment claims with aggregate exposure of AED 1.2M, one of which involves an allegation of workplace discrimination under UAE Federal Law 6/2010 that could attract regulatory attention."

**Executive translation:**
- "Deal risk: three employment claims, total potential cost AED 1.2M. Manageable if we price into the deal."
- "The discrimination claim is higher risk — it's the kind of matter that can escalate to a regulatory inquiry after closing. We recommend a price adjustment or escrow for this one specifically."
- "Decision needed: do we want to (a) accept and price in, (b) require the seller to resolve the discrimination claim before closing, or (c) walk away? I recommend (b) — the other two are standard and can be priced in."

Key technique: frame the legal issue as a business decision with specific options. Do not present the legal analysis without a recommendation.

**What executives need from a legal translation:**
- The headline risk in one sentence
- The financial or strategic magnitude
- The three options (always three — not "it depends")
- Legal's recommendation, clearly stated

### Board

Board directors care about: is this material, does it affect our fiduciary duties, what does management recommend, and do we need to disclose this?

**Legal framing:** A combination of the governance and materiality framing.

**Board translation:**
- "Directors' attention is drawn to [matter]. Management's assessment is that this is [material / not material to the financial statements / reportable to our regulator / a disclosable event]."
- "Management recommendation: [specific action]. No board resolution is required / The following board resolution is required: [...]."
- "If you have any questions on this item, GC will take questions at [agenda item number]."

Key technique: boards receive legal matters in the context of their specific duties. Directors want to know: (a) do I need to act, (b) am I personally exposed, and (c) what does management recommend?

**What boards need from a legal translation:**
- Is this material? (Financial, reputational, regulatory sense)
- Does it trigger any disclosure obligation?
- What is management doing about it?
- Is a board resolution required?

## Cross-cutting principles

**No false reassurance.** Each translation must preserve the risk level of the underlying legal issue. Translating "uncapped liability" into a commercial frame does not mean understating the risk.

**One recommendation per audience.** Each translated output ends with a single clear recommendation or action, not a list of options framed as "it depends."

**Calibrate urgency.** Not every legal issue is urgent. The translation should signal clearly: "action required today" vs "this is for awareness, no immediate action needed."

**Avoid jargon in both directions.** Do not use legal jargon in the plain-language version — and do not oversimplify to the point of inaccuracy.

## Related skills

- [[pa-workflow-inhouse-commercial-team-clause-explainer]]
- [[pa-workflow-inhouse-board-deck-legal-section]]
- [[output-mobile-friendly-short]]
- [[output-partner-memo-style]]
- [[conversation-uncertainty-language]]
