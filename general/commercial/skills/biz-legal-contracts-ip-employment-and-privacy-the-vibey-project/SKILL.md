---
name: biz-legal-contracts-ip-employment-and-privacy-the-vibey-project
title: 'Business, Marketing, Sales and Law: Commercial Law — Contracts, IP, Employment, Privacy, and Disputes'
description: 'Use when orienting on a commercial legal question before taking it to counsel: the scope note on what this material is and is not, how legal risk actually materializes, contracts including the clauses that matter and the ones that are negotiated theatre, intellectual property across copyright, trademark, patents and trade secrets, employment and contractor classification, privacy and data obligations, consumer protection and marketing law, and disputes and their realistic costs. Orientation, not legal advice.'
author: the-vibey-project
author_url: https://github.com/the-vibey-project/vibey/tree/develop/src/vibey_tools/skills/plugins/business-marketing-sales-law/skills/biz-legal-contracts-ip-employment-and-privacy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: commercial
language: en
---

# Business, Marketing, Sales and Law: Commercial Law — Contracts, IP, Employment, Privacy, and Disputes

> **Part 4 of 5** of the *Business, Marketing, Sales and Law* reference (plugin `business-marketing-sales-law`), covering §14–§21. Sibling skills: `biz-models-strategy-operations-and-financing` (§0–§4), `biz-marketing-evidence-brand-and-attribution` (§5–§9), `biz-sales-process-qualification-and-negotiation` (§10–§13), `biz-reference` (§22–§26). Section numbers are shared across the set; a reference written as §N → `skill` points into that sibling skill.
>
> **Currency:** Strategy frameworks, contract doctrine and the marketing evidence base are stable. Two areas moved. See §22 → `biz-reference` for marketing measurement after the cookie reversal and the US state privacy patchwork.

> **⚠️ Scope.** Complements an economics/accounting/tax reference (which covers economics,
> financial statements, and tax structure). **This is the operating layer.**
> ⚠️ **Part IV is legal orientation, not legal advice** — §15 says exactly what that
> distinction means and where it binds.
>
> **⚠️ GOTCHA** boxes mark received wisdom that the evidence contradicts.
>
> **The three ideas that organize all four domains:**
> 1. **⚠️ A business is a repeatable system for creating more value than it consumes.**
>    Everything else — strategy, marketing, sales — is a mechanism for that, and unit
>    economics is where you find out whether it's true (§1 → `biz-models-strategy-operations-and-financing`).
> 2. **⚠️ Most marketing folklore is contradicted by the evidence, and the contradictions
>    are consistent across decades and categories.** Loyalty, targeting, differentiation
>    and brand purpose all mean something different empirically than they do in the trade
>    press (§6 → `biz-marketing-evidence-brand-and-attribution`).
> 3. **⚠️ Legal risk is mostly boring and preventable.** Contracts nobody read, IP nobody
>    assigned, contractors who were employees, and privacy obligations nobody checked.
>    **The expensive failures are almost never novel** (§15).

---

## §14. ⚠️ Scope: What This Section Is and Isn't

> **⚠️ This is orientation, not legal advice, and the distinction is substantive rather
> than a disclaimer.** ⚠️ **Law is jurisdiction-specific, fact-specific, and changes.**
> **What follows is intended to help you recognize which issues exist, use the right
> vocabulary, and know when the answer is "ask a lawyer" — which for anything with real
> money, real risk, or a deadline, it is.**
>
> **⚠️ The economics of this are worth stating plainly**: **a few hours of legal advice
> before signing costs a fraction of litigating afterwards, and the failures in §15 are
> almost all cheap to prevent and expensive to fix.**

---

## §15. How Legal Risk Actually Materializes

**⚠️ The expensive failures are boring and repetitive:**
```
⚠️ IP that was never assigned — a contractor who wrote code owns it by default in
   many jurisdictions unless there's a written assignment
⚠️ Contractors who were legally employees — misclassification, back taxes, penalties
⚠️ Founder equity with no vesting — a co-founder leaves in month four with 50%
⚠️ Terms nobody read — auto-renewal, unlimited liability, exclusivity, IP grants
⚠️ No written agreement at all with the person you trust most
⚠️ Privacy obligations nobody checked (§19)
⚠️ Marketing claims that can't be substantiated (§20)
⚠️ Using a name someone else has rights to
```
**⚠️ The pattern**: **risk enters through relationships that were friendly when they
started.** **Write it down while everyone agrees — that is what the document is for.**

---

## §16. Contracts

**⚠️ Formation requires offer, acceptance, consideration, capacity and legality.**
⚠️ **In many common-law jurisdictions, contracts need not be written to be binding** —
but **evidence is everything, and some categories (real property, guarantees, certain
durations) must be written.**

**⚠️ The clauses that determine outcomes when things go wrong:**
```
SCOPE / DELIVERABLES     ⚠️ vagueness here causes most disputes
PAYMENT TERMS            timing, late fees, ⚠️ and what triggers the obligation
IP OWNERSHIP             ⚠️ who owns what is created — never leave this implicit
CONFIDENTIALITY          mutual or one-way, duration, carve-outs
WARRANTIES / DISCLAIMERS
⚠️ LIMITATION OF LIABILITY   often THE most economically significant clause —
                          a cap, and exclusion of consequential damages
INDEMNIFICATION          ⚠️ who defends whom, and this can be unlimited
TERMINATION              for cause, for convenience, notice, and what survives
⚠️ GOVERNING LAW / VENUE  where a dispute is heard, which can determine whether
                          it's economic to pursue at all
DISPUTE RESOLUTION       ⚠️ arbitration vs courts; arbitration is private and
                          usually not appealable
ASSIGNMENT / CHANGE OF CONTROL · FORCE MAJEURE · ENTIRE AGREEMENT
```
> **⚠️ GOTCHA — the two clauses to read first in any contract you're asked to sign are
> limitation of liability and indemnification.** ⚠️ **Uncapped liability or a broad
> indemnity can exceed the entire value of the deal by orders of magnitude**, and they are
> routinely buried and routinely accepted unread.
> **⚠️ Also check auto-renewal and notice periods** — **a contract that renews unless you
> cancel 90 days ahead will renew** (see a reporting reference §6 for why nobody catches
> this).

**⚠️ Practical points**: **the party who drafts sets the defaults**; **standard terms are
negotiable more often than people assume**; **and ambiguity is generally construed against
the drafter (contra proferentem)** — ⚠️ **which is a reason to draft clearly rather than
cleverly.**

---

## §17. Intellectual Property

```
COPYRIGHT   ⚠️ automatic on creation; expression not ideas; software is covered
            Registration adds remedies in some jurisdictions
TRADEMARK   ⚠️ source identifiers; rights from USE in some systems and REGISTRATION in
            others; classes; and they must be defended or weakened
PATENT      ⚠️ novel, non-obvious, useful; 20 years; expensive; PUBLIC DISCLOSURE
            BEFORE FILING can destroy novelty in many jurisdictions
TRADE SECRET ⚠️ protected only while kept secret; no expiry; requires actual
            protective measures to qualify
```
**⚠️ Work-for-hire and assignment is the one that bites startups**: ⚠️ **employees'
work-related creations typically vest in the employer by default; CONTRACTORS' generally
do NOT without a written assignment.** **This is the most common expensive IP mistake, and
it surfaces at due diligence when it's least convenient.**
**⚠️ Open source licensing is a real obligation**: **permissive (MIT, Apache) vs copyleft
(GPL, AGPL)**, and ⚠️ **AGPL's network clause reaches SaaS use.** **Know your dependency
licences before an acquirer does.**
**⚠️ AI and IP is genuinely unsettled** — **training data, output ownership and
infringement are being actively litigated, and anyone telling you it's resolved is
overstating.**

---

## §18. Employment

**⚠️ Employee vs contractor is a legal test, not a label you choose** — **control,
integration, economic dependence, and the tests differ by jurisdiction.**
⚠️ **Misclassification exposes you to back taxes, benefits, penalties and interest, and
the liability is usually the engager's.**
**Key areas**: at-will vs protected employment, **wage and hour** (⚠️ **overtime
exemptions are frequently misapplied**), **anti-discrimination**, **accommodation
obligations**, **leave**, **health and safety**, and **termination process.**
**⚠️ Restrictive covenants** — non-compete, non-solicit, confidentiality — ⚠️ **vary
enormously in enforceability by jurisdiction and have been substantially restricted in
several.** **Assume a non-compete may be unenforceable where you are, and that
confidentiality and non-solicit generally hold up better.**
**⚠️ Equity for employees**: **options vs RSUs, vesting and cliffs, exercise windows**
(⚠️ **a 90-day post-departure exercise window plus an illiquid share is a well-documented
trap for employees**), **and the tax treatment differs sharply by instrument and
jurisdiction** (see an accounting reference §17).

---

## §19. Privacy and Data

**⚠️ If you collect personal data, this applies to you, and the thresholds are lower than
most small businesses assume.**
**GDPR concepts that have become the global vocabulary**: **lawful basis** (⚠️ **consent
is only one of six, and it's often the wrong one — legitimate interest and contractual
necessity are frequently better fits**), **data subject rights**, **controller vs
processor**, **DPAs**, **breach notification**, **DPIAs**, **international transfers.**
**US**: ⚠️ **no comprehensive federal law; a state patchwork — §22.2 → `biz-reference` for the current
picture** — **plus sectoral laws (HIPAA, GLBA, COPPA, FERPA).**
**⚠️ Practical baseline that serves you regardless of which law applies**: **know what you
collect and why; collect less; have a real privacy policy that matches actual practice
(⚠️ a policy that describes something you don't do is itself a violation); honour deletion
and access requests; have a breach plan; put DPAs in place with vendors; and
⚠️ honour Global Privacy Control signals, which regulators can test trivially** (§22.2 → `biz-reference`).

---

## §20. Consumer Protection and Marketing Law

**⚠️ Advertising claims must be substantiated BEFORE you make them, not defended
afterwards.** **Express and implied claims both count, and the implied one is what
enforcement usually targets.**
**⚠️ Specific areas that catch marketers:**
- **Endorsements and testimonials** — ⚠️ **material connections must be disclosed clearly
  and conspicuously; "clearly" means a viewer actually sees it.**
- **⚠️ Dark patterns and negative-option billing** — **auto-renewal disclosure and easy
  cancellation are increasingly mandated, and enforcement here has been active.**
- **Email and messaging** — ⚠️ **CAN-SPAM, GDPR/PECR consent, TCPA for SMS and calls**,
  and **TCPA in particular carries statutory damages per message that make class actions
  economic.**
- **Pricing** — reference-price and "was/now" claims, drip pricing, all-in pricing rules.
- **Comparative advertising** and **influencer disclosure.**
- **⚠️ Accessibility** — website accessibility litigation is common in some jurisdictions.

---

## §21. Disputes

**⚠️ Litigation is slow, expensive, public and uncertain, and those four things shape
every rational decision about it.**
**Escalation ladder**: direct negotiation → **demand letter** → mediation (⚠️ **non-binding
and often effective**) → arbitration (⚠️ **binding, private, limited appeal**) → litigation.
**⚠️ Practical realities**: **legal costs frequently exceed the amount in dispute for small
claims**; **a judgment is not money — collection is a separate problem**; **and the time
and attention cost to a small business is usually larger than the legal fees.**
**⚠️ Preserve evidence early** — **document retention obligations attach once litigation
is reasonably anticipated, and destroying relevant material afterwards is far worse than
the underlying dispute.**
**Insurance** — ⚠️ **general liability, professional indemnity/E&O, D&O, cyber** — **and
the time to read the policy is before you need it.**
