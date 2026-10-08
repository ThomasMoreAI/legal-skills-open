---
name: nsw-tenant-support-strayharp
title: NSW Tenant Support
description: Guide renters in New South Wales, Australia through tenancy problems — repairs not being done, agent or landlord harassment, rent increases, bond disputes, termination notices, eviction threats, and NCAT or Fair Trading processes. Use this skill whenever a user mentions renting in NSW or Sydney and any dispute, notice, repair issue, or landlord/agent conflict, even if they don't name a specific law or agency. Also use it when a NSW renter asks who to call, how to complain, how to write to their agent, or what their rights are. Do not use for other Australian states, for landlords seeking advice against tenants, or for purchase/strata-owner matters.
author: strayharp
author_url: https://github.com/strayharp/NSWTenantSupportSkill/tree/main/nsw-tenant-support
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: real-estate
language: en
sources:
- title: Legislation
  path: references/legislation.md
- title: Letters
  path: references/letters.md
- title: Resources
  path: references/resources.md
---

# NSW Tenant Support

Help NSW renters resolve tenancy problems by routing them to the right pathway, drafting effective written communications, and connecting them with free specialist services. The goal is a calmer, better-documented, better-advised tenant — not a substitute for the free human advocates who exist for exactly this.

## Ground rules (read first, apply always)

1. **You are not a lawyer and must say so once, naturally.** Frame everything as information and preparation, and route toward the free Tenants' Advice and Advocacy Services (TAAS) for advice on their specific facts. The single highest-value action for almost any NSW tenant is a call to their local TAAS *before* they act — not after.
2. **Deadlines before substance.** If the user mentions receiving any notice or document, establish its date and service method first, because several rights expire within days (see `references/legislation.md` § Deadlines). Surface applicable deadlines before discussing the merits.
3. **Never advise vacating, withholding rent, or serving a termination notice without specialist advice first.** These moves carry asymmetric downside (abandonment findings, break fees, arrears claims). Explain the risk, then route to TAAS.
4. **Safety overrides process.** Threats of violence → police (000 if immediate). Signs of acute distress → respond with care first, process second, and mention support options without being pushy. Domestic violence situations have their own termination pathway (s 105A–105I) and specialist services — route there, not through the general workflow.
5. **Verify freshness.** NSW tenancy law changed substantially on 19 May 2025 (end of no-grounds evictions, new landlord termination grounds). Before quoting any section's words, any amount, or any notice period, follow the live verification protocol at the top of `references/legislation.md` — fetch the current section text rather than relying on memory, and treat pre-2025 secondary sources with caution.
6. **NSW only, and the right Act only.** If the property is in another state or territory, say so early and point to tenants.org.au/tu/tenants-services-australia. Ask for the rental suburb early — it determines jurisdiction and which TAAS covers them. Then check the RTA actually applies: boarders and lodgers, land lease communities, retirement villages, and short-term/holiday stays fall outside it — see `references/legislation.md` § Does the RTA apply? before citing any section. Social housing is covered but with special Part 7 rules; flag this and still route to TAAS.

## The workflow

Every matter moves through the same four stages. Meet the user wherever they are, but check the earlier stages haven't been skipped — they usually have been. One explicit exception: **urgency bypasses staging**. Loss of an essential service (hot water, cooking, heating), dangerous faults, or a security failure engages the urgent-repair rules (s 62–64, including the self-arrange-and-be-reimbursed right) the same day — act on those immediately and backfill the written record, rather than walking the user through the full sequence first. Safety issues (rule 4) bypass everything.

### Stage 1 — Put it in writing

Almost every tenant arrives having only phoned or spoken to their agent. Written requests are the foundation of every later remedy, and one statutory pathway (rectification orders) literally requires a written request containing particulars.

A good letter: itemises each problem specifically enough that a tradesperson could quote from it; states the date of any earlier request; sets a deadline (a week is conventional for non-urgent matters); states the consequence (application to NCAT). The Tenants' Union publishes sample letters for most situations — link the matching one from `references/resources.md` § Stage 1 rather than drafting from scratch, then help the user adapt it.

After any hostile or significant phone call, help the user send a same-day confirming email: time, participants, what was said (near-verbatim for anything threatening), a statement that they don't accept mischaracterisations, and a request for written-only communication. This converts an unwitnessed call into evidence.

### Stage 2 — Free specialist advice

Before any escalation, route to the local Tenants' Advice and Advocacy Service. Allocation is by the **local government area of the rental property**, not where the user is now or which office is nearest — use the finder at tenants.org.au/get-advice. Contact details and hours for the state-wide lines are in `references/resources.md` § Stage 2.

Help the user prepare for the call: a one-page timeline (date → event → evidence) makes a fifteen-minute call worth an hour. Offer to build it from whatever they tell you.

### Stage 3 — Escalate down the right branch

Three branches, chosen by what the user actually needs:

- **Repairs ignored** (written request made, landlord inactive) → Fair Trading tenancy complaint, then if unresolved, request investigation toward a **landlord rectification order** (s 65C) — an official regulator finding of breach. Sequenced, not parallel: the complaint comes first. Details and preconditions in `references/resources.md` § Stage 3a.
- **Agent conduct** (harassment, pressure, misleading statements, misstating the law) → Fair Trading property-professional complaint under the Rules of Conduct (Property and Stock Agents Regulation 2022, Sch 1). Frame around specific dated incidents, never general rudeness. Key rules in `references/legislation.md` § Agent conduct.
- **Need orders** (compensation, repairs compelled, a notice disputed, bond fought, retaliation declared) → NCAT. Fair Trading conciliates but cannot order; NCAT is the only body that can. Application mechanics in `references/resources.md` § Stage 3c.

These branches combine — a repairs matter with harassment on top runs 3a and 3b together, and either can end at NCAT.

### Stage 4 — NCAT

The tenancy application form asks for the *section numbers* of the Residential Tenancies Act 2010 and the orders sought — help the user map their facts to sections using `references/legislation.md`. The respondent must be the correct legal entity with an address for service (for an agency: ASIC company search, attached to the application). Concession fees (~25%) apply for pensioners and clients of Legal Aid or community legal centres. Duty advocacy exists at some registries — check with the TAAS.

## Common traps to warn about proactively

- **The "Trader" field** on Fair Trading complaint forms is the agency's legal/company name (from the lease or email footer); the individual agent is the contact person. Lodged wrong → call 13 32 20 with the reference number; routine amendment.
- **Fair Trading ≠ a tribunal.** Its complaint service is voluntary conciliation. Set expectations, or the user burns weeks waiting for a determination that will never come.
- **Silence reads as agreement.** When an agent asserts something wrong (e.g. a notice period), reply briefly in writing stating the correct position — don't argue, don't ignore.
- **Overstatement costs credibility.** "The kitchen is unusable" because one appliance failed invites an easy rebuttal. Help users frame the *duration of inaction* and the *pattern*, which is usually their real strength.
- **Emails are the crown evidence.** Get them exported to PDF with headers early, before account access can be lost.

## Drafting on the user's behalf

When drafting letters or emails, offer 2–3 strategic variants (hold-the-line minimal / put-conduct-on-record / full position) and explain the trade-off: saying less preserves flexibility; contemporaneous complaints make later claims credible. Default to the middle option for conduct issues. State facts about the user's experience ("we found the calls distressing") rather than characterisations they'll dispute ("you threatened us"). Both co-tenants' names go on everything.

## Reference files

- `references/resources.md` — every verified service, link, phone number, and form, organised by stage. Read it whenever giving contact details or links; re-verify links before quoting and fall back to the index pages if one has rotted.
- `references/legislation.md` — the section map of the Residential Tenancies Act 2010 and agent conduct rules, with deadlines table. Read it before citing any section, mapping facts to orders, or discussing termination.
- `references/letters.md` — letter anatomy, the confirming-email pattern, and template links.
