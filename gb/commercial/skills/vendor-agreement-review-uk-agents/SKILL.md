---
name: vendor-agreement-review-uk-agents
title: Vendor Agreement Review (UK)
description: 'Reference: review of an inbound vendor agreement against the team playbook in `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` under English contract law (with notes for Scots law / NI where the governing law requires). Flags deviations, assesses risk, generates specific redline language, and routes to the right approver. Loaded by /commercial-legal-uk:review when a vendor MSA, services agreement, or similar is detected.'
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/commercial-legal-uk/skills/vendor-agreement-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: commercial
language: en
---

# Vendor Agreement Review (UK)

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph. If enabled and there is no active matter, ask: "Which matter is this for? Run `/commercial-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/matters/<matter-slug>/`.

---

## Destination check

Before producing output, check where it's going. If the user has named a destination (a channel, a distribution list, a counterparty, "everyone"), ask whether it's inside the privilege circle. Public channels, company-wide lists, counterparty/opposing counsel, vendors, and clients (for work product) waive the protection. When the destination looks outside the circle, flag it and offer (a) the privileged version for legal only, (b) a sanitized version for the broader channel, or (c) both. See the canonical `## Shared guardrails → Destination check` in this plugin's CLAUDE.md.

## Purpose

Read a vendor agreement against the playbook this team actually uses (in `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`), find every term that deviates, and tell the solicitor what to do about each one — with specific redline language, not vague "consider revising."

This review applies **English contract law** as the default. Where the contract's governing law is Scots law or Northern Ireland law, the review notes applicable differences. Where the contract involves EU or other foreign law, the review flags cross-border issues.

The output is a review memo the solicitor can act on in one pass. Every issue has a severity, a business-impact explanation, a proposed fix, and an escalation call if one is needed.

## Precondition: load the playbook

**Before reading the contract, read `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`.** If it's missing or still has placeholders, surface this bounce:

> I notice you haven't configured your practice profile yet — that's how I tailor playbook positions, escalation, and house style to your practice.
>
> **Two choices:**
> - Run `/commercial-legal-uk:cold-start-interview` (2 minutes) to configure your profile, then I'll review tailored to YOUR playbook.
> - Say **"provisional"** and I'll review against generic defaults — English law, middle risk appetite, solicitor role, no playbook (flag all common vendor-contract risks from first principles) — and tag every output `[PROVISIONAL — configure your profile for tailored output]`.

### Provisional mode

If the user says "provisional," run the review using these generic UK defaults: middle risk appetite, solicitor role, English law, no playbook (flag common risks from first principles — uncapped liability, missing UCTA 1977 reasonableness language, no UK GDPR data processing terms, auto-renewal without adequate notice, etc.). Tag every finding `[PROVISIONAL]`.

**Which side?** Before applying the playbook, determine which side the company is on for this contract. Usually obvious: if the counterparty is a vendor/supplier, you're purchasing-side. If the counterparty is a customer, you're sales-side. If not obvious, ask. Read the matching playbook section. If the matching side is `[Not configured]`, stop and tell the user to run `/commercial-legal-uk:cold-start-interview --side <side>`.

The playbook in `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` is the source of truth. It tells you:
- What this team's standard positions are (not market standard — *their* standard)
- What fallbacks they've accepted before
- What they never accept
- Who approves what
- The one deal-breaker to check first

If the contract has the deal-breaker, flag it at the top of the memo and stop the detailed review.

## Workflow

### Step 1: Orient

Read the whole agreement once, fast. Answer:

| Question | Answer |
|---|---|
| What kind of agreement is this? | MSA / SaaS subscription / Professional services / Licence / Other |
| Who are we? | Customer / Vendor (this plugin assumes customer — flag if not) |
| Counterparty | Name, and are they a large corporate (less likely to negotiate) or an SME (more likely)? |
| Contract value | Annual / total contract value if stated (note in £ GBP or state currency) |
| Term | Length, renewal mechanics |
| Governing law | English law? Scots law? NI law? Foreign? |
| Is there a UK GDPR DPA? | Attached as schedule / referenced by URL / missing |
| Is there an order form? | Separate doc or integrated |
| UCTA applicability | B2B (UCTA 1977 reasonableness test) or B2C (Consumer Rights Act 2015)? |

**Contract value handling.** If the main agreement does not state a value (MSA sets terms but Order Form carries price), **stop and ask** before running escalation math or applying pound thresholds.

**DPA-by-reference handling.** If the main agreement incorporates a DPA "available at [URL]" or "as set forth at [URL]," note it explicitly:

> This agreement incorporates a DPA by URL reference at `[URL]`. The DPA carries the real data terms — sub-processor rights, breach-notification timing (72-hour obligation to the ICO under UK GDPR Article 33), data-return mechanics, international transfer mechanisms (IDTA or UK Addendum), audit rights. Without reading it, the data-protection analysis below is partial.

Do not silently proceed as if the DPA were absent when it is incorporated by reference.

### Step 2: Deal-breaker check

Check the "one thing" from `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` first. If present, flag it with the same structure as the US version and stop the detailed review.

### Step 3: Term-by-term comparison

For each playbook category, find the corresponding contract section and compare.

**For each deviation, produce:**

```markdown
### [Section X.X]: [Issue name]

**Playbook says:** [our standard position, quoted from `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`]

**Contract says:**
> "[exact quote from the contract]"

**Gap:** [Missing term | Weaker than standard | Weaker than fallback | Non-standard structure | Unacceptable]

**Legal risk:** 🔴 Critical | 🟠 High | 🟡 Medium | 🟢 Low
**Business friction:** 🔴 Blocks deals | 🟠 Slows deals | 🟡 Confuses customers | 🟢 Invisible

**Why it matters:** [one or two sentences in plain English — what goes wrong
for the business if this term stays as-is]

**Proposed redline:**
> "[the specific replacement language — ready to paste into a markup]"

**If they won't move:** [the fallback from `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`, or "escalate to [person]"
if no fallback exists]
```

**Severity calibration:**

| Level | Means |
|---|---|
| 🔴 Critical | Don't sign without fixing. A term on the team's "never accept" list, or a deal-breaker. |
| 🟠 High | Strongly push; escalate if they won't move. A term outside the playbook's stated fallback range. |
| 🟡 Medium | Push in first round; accept if it's the last open item. A term inside the fallback range but short of the standard position. |
| 🟢 Low | Note it, don't spend capital. A term the playbook explicitly tolerates, or a purely stylistic deviation. |

#### UK-specific liability cap decision procedure

**The cap amount is the least important part of the cap.** Work through the four dimensions below:

1. **Direct vs. indirect/consequential damages.** Does the cap apply to ALL liability, or only direct damages? State both treatments explicitly. Note: under UCTA 1977 s.3 (B2B, standard terms), excluding liability for negligence and breach must be reasonable. Under s.2(1), excluding liability for death or personal injury due to negligence is void. `[model knowledge — verify]`

2. **The cap base — quote it verbatim.** "12-month cap" could mean fees paid, fees payable, fees under current order, etc. If ambiguous, flag it.

3. **Cap-carveout interaction.** Enumerate what sits ABOVE the cap (carveouts), what sits BELOW (what's actually capped). Common UK carveouts: wilful misconduct, gross negligence, fraud, death/personal injury (void to exclude under UCTA), IP indemnity, data breach, confidentiality breach.

4. **Your playbook position per dimension.** Check against `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`.

#### UCTA 1977 / Consumer Rights Act 2015 check

For every limitation, exclusion, or indemnity clause, apply the applicable statute:

**B2B contracts (UCTA 1977):**
- s.2(1): Cannot exclude liability for death/personal injury from negligence — void. `[model knowledge — verify]`
- s.2(2): Exclusion of other negligence loss — valid only if reasonable. `[model knowledge — verify]`
- s.3: When contracting on standard terms — can only exclude/restrict liability for breach if reasonable. `[model knowledge — verify]`
- s.11 + Schedule 2 (reasonableness criteria): bargaining strength, alternatives, inducement, buyer's knowledge, practicability of compliance, special circumstances.

Flag: `[UCTA 1977 — reasonableness check required — [review]]`

**B2C contracts (Consumer Rights Act 2015):**
- Part 2: Unfair terms in consumer contracts — terms must be fair and transparent; core terms must be prominent.
- Schedule 2: Grey list of terms that may be unfair.

Flag: `[Consumer Rights Act 2015 — fairness review required — [review]]`

#### UK GDPR / DPA 2018 data terms check

Every vendor agreement touching personal data must have a compliant data processing agreement. Check:

- **UK GDPR Article 28 mandatory clauses** present? (processor obligations, sub-processors, data subject rights, deletion/return, audits, security measures) `[model knowledge — verify]`
- **Sub-processor regime:** prior written authorisation or current approved list + notice of changes?
- **International transfers:** IDTA or UK Addendum to EU SCCs in place for transfers outside UK/EEA? `[model knowledge — verify]`
- **Breach notification:** obligation to notify controller within 72 hours of becoming aware (Article 33 UK GDPR)? `[model knowledge — verify]`
- **DPIA:** if high-risk processing, is a DPIA required? UK GDPR Article 35. `[model knowledge — verify]`

Missing or non-compliant DPA terms: flag 🔴 Critical (UK GDPR violation risk).

#### Competition Act 1998 check

Flag any clauses that could constitute:
- Chapter I prohibition violations: price-fixing, market-sharing, output restrictions, collective boycotts, bid-rigging
- Vertical restraints raising concern: exclusive dealing (if market share threshold may be exceeded), resale price maintenance, territorial restrictions `[model knowledge — verify]`
- Chapter II prohibition concerns: exclusivity or tying arrangements if the contracting party has dominance in a relevant market `[model knowledge — verify]`

If any Competition Act exposure: flag `[Competition Act 1998 — CMA referral may be required — [review]]`

#### Late payment check

**Late Payment of Commercial Debts (Interest) Act 1998:** Check payment terms for implied interest-on-late-payment provisions. Statutory right to claim 8% above Bank of England base rate on late commercial debts; also £40–£100 fixed compensation. `[model knowledge — verify]`

If the contract attempts to contract out of the 1998 Act, flag unless the payment terms provided are "substantial" under s.9.

#### Jurisdiction delta check

**The playbook applies one governing-law preference globally. Check the contract's actual governing law against the top divergences:**

- **Governing law is Scots law:** no consideration requirement; different offer/acceptance rules; own frustration doctrine; different land law; Law Society of Scotland professional conduct rules apply.
- **Governing law is NI law:** many English statutes extend to NI with modifications — check extent notes.
- **Governing law is foreign (EU, US, etc.):** Rome I (retained UK version) governs choice of law; check that the choice is valid. Post-Brexit English court judgments may not be automatically enforced in EU Member States.
- **Non-solicits/non-competes:** enforceable in English law if reasonable in scope, duration, and geographic extent — but assessed on restraint of trade doctrine. Less strictly applied than US equivalents. `[model knowledge — verify]`
- **Liability exclusions:** UCTA reasonableness applies to B2B regardless of governing-law choice if the contract has a connection to England & Wales. `[model knowledge — verify]`
- **Confidentiality term:** English courts will enforce perpetual obligations for genuine trade secrets; mere confidential information may be limited to a reasonable period. `[model knowledge — verify]`

When the playbook position conflicts with the contract's governing-law enforceability, flag: "Your playbook prefers [X], but this contract is governed by [Y] law where [X] is [unenforceable / restricted / subject to statutory override]. `[jurisdiction — verify]`"

### Step 4: Favourable terms and gaps

**Better than our standard:** Terms where the vendor gave us more than we'd ask for. Note these — they're trade bait.

**Missing entirely:** Standard provisions that just aren't there. Most common in UK commercial contracts: assignment restrictions (LPA 1925 s.136 assignment rules), audit rights, force majeure (note: English law approach — clause must be express; common law frustration is very narrow), insurance requirements, step-in rights, TUPE notification obligations (if services agreement involving staff).

### Step 5: Escalation routing

Check the escalation matrix in `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` against:
- Contract value in £ GBP
- Presence of any 🔴 critical issues
- Any automatic-escalation triggers (unlimited liability, IP assignment, Competition Act exposure, ICO/FCA notification triggers)

State clearly who needs to approve:

```markdown
## Approval routing

Based on [contract value / issue severity], this agreement requires:

- [ ] **[Name/role]** approval — [reason]
- [ ] **Business owner sign-off** on [specific commercial term they should weigh in on]
- [ ] **CMA referral check** — [if competition concerns flagged]
- [ ] **ICO notification** — [if high-risk processing / data breach within 72 hours]

**Recommended next step:** [Send redlines to counterparty | Escalate to Head of Legal before
responding | Get business input on commercial term X before legal responds]
```

**Before proceeding to send redlines to the counterparty:** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`. If the Role is Non-lawyer:

> Sending redlines is a legal act — the counterparty will treat every edit as our negotiating position. Have you reviewed this with a solicitor? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: counterparty, agreement type, the specific redlines proposed, the playbook positions behind each, the fallbacks, and what to ask the solicitor before the package leaves.]
>
> If you need to find a solicitor or barrister: the Solicitors Regulation Authority (SRA) at sra.org.uk has a Find a Solicitor tool. The Law Society of Scotland (lawscot.org.uk) covers Scottish solicitors. The Bar Council (barcouncil.org.uk) has a Find a Barrister directory.

Do not proceed past this gate without an explicit yes.

## Redline granularity

**Edit at the smallest possible granularity.** A redline is a negotiation artefact, not a rewrite. Wholesale clause replacement signals "we threw out your drafting." Surgical redlines — strike a word, insert a phrase, restructure a subclause — signal "we have specific asks" and are faster to read, understand, and accept.

Default to the smallest edit that achieves the playbook position. Only replace a **whole clause** when the counterparty's version is so far from your position that surgical edits would be harder to read than a fresh draft — and when you do, say so in the transmittal.

### Step 6: Assemble the memo

Prepend the work-product header from `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` `## Outputs` (it differs by user role — see `## Who's using this`).

This memo and the underlying agreement may be subject to legal professional privilege. Distribute only within the privilege circle; mark and store it where privileged materials live; strip the work-product header before any external delivery.

The playbook positions applied below reflect the jurisdiction recorded in `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` → `Governing law and venue`. Legal rules and enforceability vary materially by jurisdiction across the UK nations and internationally. If this deal implicates a different governing law or a choice-of-law question, flag it in the memo.

> **No silent supplement.** If a research query to the configured legal research tool (uk-legal MCP, BAILII, or legislation.gov.uk) returns few or no results for a rule the memo needs, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking.
>
> **Source attribution.** Where the memo cites a statute, regulation, or case, tag the citation: `[uk-legal MCP]`, `[legislation.gov.uk]`, `[BAILII]`, `[govuk MCP]`, or `[statute / regulator site]` for citations retrieved in this session; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for citations recalled from training data; `[user provided]` for citations from the counterparty draft or house files.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

# Vendor Agreement Review: [Counterparty] [Agreement Type]

**Reviewed:** [date]
**Contract value:** £[amount] / [term]
**Our role:** Customer
**Governing law:** [English law / Scots law / NI law / other]
**UCTA applicability:** [B2B — UCTA 1977 / B2C — Consumer Rights Act 2015]

---

## Bottom line

[Two sentences. Can we sign this? What has to change first?]

**Issues (legal risk):** [N]🔴 [N]🟠 [N]🟡 [N]🟢
**Issues (business friction):** [N]🔴 [N]🟠 [N]🟡 [N]🟢

**Approval needed from:** [name]

---

## Deal-breaker check

[✅ Clear | ⛔ Present — see above]

---

## Issues by severity

[All the deviation blocks from Step 3, grouped Critical → Low]

---

## UCTA / CRA statutory flags

[Any clauses requiring reasonableness or fairness assessment]

## UK GDPR / DPA 2018 flags

[Any data processing gaps or missing Article 28 provisions]

## Competition Act 1998 flags

[Any potential Chapter I / Chapter II concerns]

---

## Favourable terms

[list]

## Missing provisions

[list — include TUPE, force majeure, step-in rights where relevant]

---

## Approval routing

[from Step 5]

---

## Redline package

[If requested: consolidated markup-ready language for all proposed changes]
```

## Integration: CLM

If a CLM MCP is connected, after the review:

- Check if this counterparty already has agreements with us
- Pull the workflow template that matches this agreement type
- Offer to create the CLM record with the review memo attached and approvers pre-routed

## Integration: DocuSign

If DocuSign MCP is connected and the agreement is ready to sign, offer to generate the envelope and route to signers in the right order per the escalation matrix.

**Before generating a signature envelope:** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md`. If the Role is Non-lawyer, gate on solicitor review before proceeding.

## Output formats

**Full memo (default):** As above.

**Slack-sized summary:** Two lines and a link.

```
[Counterparty] [type] — NEEDS WORK. 1🔴 (uncapped liability §8.2 — UCTA reasonableness concern), 2🟠. Full review: [link]. Needs [Head of Legal] approval.
```

**Redline doc:** If the user asks for it, output a .docx with tracked changes. Comments on each change cite the playbook position and applicable UK statute where relevant.

## Quality checks before delivering

- [ ] `~/.claude/plugins/config/uk-legal-plugins/commercial-legal-uk/CLAUDE.md` was loaded and quoted — not generic market positions
- [ ] Deal-breaker checked first
- [ ] Every issue has specific replacement language
- [ ] Risk levels are calibrated (not everything is Critical)
- [ ] Approver is named, not "escalate to legal"
- [ ] UCTA 1977 / CRA 2015 reasonableness/fairness assessed for all limitation/exclusion clauses
- [ ] UK GDPR / DPA 2018 Article 28 compliance checked
- [ ] Governing law confirmed; Scots law / NI law differences noted where applicable

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced. The tree is the output; the solicitor picks.
