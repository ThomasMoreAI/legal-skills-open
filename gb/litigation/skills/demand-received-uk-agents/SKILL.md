---
name: demand-received-uk-agents
title: /demand-received
description: Triage an inbound Letter Before Action or Letter of Claim — extract fields, cross-check the portfolio, assess merit, present response options with a recommendation, and hand off to matter-intake or demand-intake if escalation is warranted. Use when the user says "we got a Letter Before Action", "triage this demand", or shares an incoming letter to evaluate.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/litigation-legal-uk/skills/demand-received
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: litigation
language: en
---

# /demand-received

1. Read the incoming document from provided path.
2. Load `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/matters/_log.yaml` for portfolio cross-check.
3. Load `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md` → risk calibration, landscape, Letter Before Action practice.
4. Follow the workflow and reference below.
5. Extract fields; cross-check portfolio; assess merit; present options with recommendation.
6. Write `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/inbound/[slug]/triage.md`. Copy or link incoming to `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/inbound/[slug]/incoming.[ext]`.
7. Hand off per user choice:
   - Create matter → `matter-intake` pre-populated
   - Respond with counter-demand → `demand-intake` pre-populated
   - Link to existing matter → update `related_matters` in log
   - Standalone → no further action

---

# Demand Received

## Purpose

Inbound Letters Before Action and Letters of Claim are the bread and butter of an in-house litigation practice. A small fraction need escalation; most can be handled with a structured response or a holding letter. The failure mode is treating them all alike. This skill triages, cross-checks the portfolio, and produces options.

## Load context

- The incoming document (user provides path or drops it in-session)
- `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/matters/_log.yaml` — scan for related matters (same counterparty, overlapping counterparties via entity relationships, or matter type + recent date)
- `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md` → risk calibration (for merit assessment), landscape (is the sender a frequent adversary?), Letter Before Action practice (house tone and response defaults)

## Workflow

### Step 1: Read the demand

Extract from the incoming:

- **Sender** — entity, signer, solicitors (if signed by external firm)
- **Recipient** — which entity/person at our company
- **Delivery** — recorded post, email, courier (matters for limitation and pre-action protocol timeline calculation)
- **Date received** vs. **date signed**
- **Demand type** — payment, breach/cure, C&D, preservation, settlement, other
- **Specific asks** — what they want, by when
- **Facts alleged** — their version of what happened
- **Legal basis** — statutes, contract provisions, theories they cite (OSCOLA-tag each for verification)
- **Threats** — what they say they'll do if we don't comply (issue proceedings, seek injunction, etc.)
- **Settlement-communication framing** — is this marked "without prejudice" or "without prejudice save as to costs"? Note whether it is marked as such, but remember: protection attaches from conduct and context, not merely from labelling. Capture both the label (if any) and a first-pass read of whether the substance is in fact a compromise discussion.
- **Applicable CPR pre-action protocol** — does the demand purport to comply with a specific pre-action protocol? Note which one. Non-compliance with a protocol by either party can affect costs later.

### Step 2: Portfolio cross-check

Search `_log.yaml` for:

- **Direct match** — matter with same counterparty (their slug matches the sender)
- **Type match** — similar matter type with this counterparty in the past (closed matters count — they inform pattern)
- **Subject overlap** — matters where the subject might be the same dispute (e.g., same contract, same product, same project)

Present findings:

- If **direct match + active:** flag as almost certainly the same matter; recommend adding incoming to the existing matter, not opening a new one. Update `related_matters` if it's a tangent.
- If **direct match + closed:** flag — counterparty is back. May be a new dispute (open new matter) or a resurrected one (reopen or amend). User decides.
- If **type match:** note as precedent/context; probably distinct matter but inform the response strategy.
- If **no match:** novel. Treat as fresh.

### Step 3: Merit assessment

Not a legal opinion — a structured read:

- **Facts** — do the alleged facts align with what we know? Where's the disconnect?
- **Legal basis** — are the cited provisions/statutes actually applicable? (Flag cites for user verification — do not attempt to validate law autonomously.)
- **Strength on their side** — if they issued proceedings tomorrow, what's their story?
- **Strength on our side** — what are our likely defences?
- **Damages demanded vs. likely** — is the ask proportionate to what a court would award if they won?
- **Leverage and pressure** — are they credibly prepared to issue proceedings? Are they a repeat-litigant adversary per `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md`?

Output a triage rating: **substantial merit / debatable / weak / frivolous**. Be blunt. The user is triaging, not writing the skeleton argument.

### Step 4: Response options

Present 3-4 options with tradeoffs:

**Option A — substantive response**
- When: their demand has merit or is at least debatable; a reasoned reply protects the record and demonstrates pre-action protocol engagement
- Tradeoff: commits us to a position in writing
- Next step: `/demand-intake` with pre-populated fields for a counter-response letter

**Option B — holding letter**
- When: need time to investigate; don't want to concede anything or trigger their deadline math
- Tradeoff: doesn't resolve anything; buys 2-4 weeks; the pre-action protocol may require substantive engagement within a specified period — check the applicable protocol
- Next step: short acknowledgment draft noting we are investigating and will respond by a stated date

**Option C — settlement response**
- When: early resolution is cheaper than proceedings; willing to discuss without admitting
- Tradeoff: without-prejudice posture required — structure the response so the substance, not just the label, qualifies as a compromise discussion. Must be careful not to waive claims.
- Next step: `/demand-intake` with `type: settlement-response`

**Option D — ignore + preserve**
- When: demand is frivolous or the deadline doesn't create legal prejudice
- Tradeoff: silence can have consequences in some contexts; legal hold still required; pre-action protocol non-engagement may attract costs sanctions even if proceedings are unmeritorious
- Next step: issue legal hold via `/legal-hold --issue` if not already; log the demand and monitor

Recommend one. Be specific about why.

### Step 5: Deadline triage

- **Their stated deadline** — note it, and flag if it is shorter than the applicable CPR pre-action protocol period
- **Our internal deadline** — when we must decide (often: stated deadline minus 5 business days to draft + approve)
- **Legal deadlines** — limitation period (Limitation Act 1980 / Scottish Prescription and Limitation (Scotland) Act 1973), contractual cure periods, pre-action protocol compliance periods, any regulatory deadlines
- **Pre-action protocol check** — if the demand purports to follow a specific protocol, confirm their compliance (incorrect notice periods, missing information, etc. may affect their ability to issue without further steps or may affect costs)

Flag any legal deadlines that are tight. Calendar them.

**No silent supplement.** If the inbound demand cites rules, cases, or statutes that require verification, and a research query to the configured legal research tool returns few or no results for a given authority, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking.

**Source attribution.** Tag every citation carried into the triage — including the sender's cited authorities, our response-option rationales, and any research pulled for merit assessment — with where it came from: `[uk-legal MCP]`, `[BAILII]`, `[legislation.gov.uk]`, `[gov.uk]`, `[web search — verify]`, `[model knowledge — verify]`, or `[user provided]`.

### Step 6: Write triage

Output: `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/inbound/[slug]/triage.md`.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

> **LPP inheritance.** This triage is derived from the inbound demand and from the portfolio log, and it records our first-pass merit read and response posture. Those internal analyses are attorney-client and/or litigation-privilege material. Distributing this triage beyond the LPP circle — including forwarding it to the business lead without marking, sharing with the counterparty, or attaching to an insurance tender without scrubbing — can waive protection over both this document and the reasoning inside it. Store with privileged matter material, mark consistently with house LPP conventions, and make distribution decisions deliberately.

# Demand Received — Triage

> **READ FOR TRIAGE, NOT OPINION.** This document is an intake scan and an options analysis — not a legal merit opinion. The `Triage rating` below is a structured read to support the counsel's decision on how to route the demand. It is not a recommendation on the merits and does not substitute for case-specific legal analysis. Every cited statute, rule, or case is flagged for SME verification; every merit call is the counsel's, not this skill's.

**Slug:** [slug]
**Received:** [YYYY-MM-DD]
**Received by:** [entity / person]
**Incoming file:** [path]

---

## The demand

**Sender:** [entity, signer, solicitors]
**Demand type:** [type]
**Specific asks:** [list]
**Their stated deadline:** [date]
**Applicable CPR pre-action protocol:** [name / default PD / not identified — `[SME VERIFY]`]
**Settlement-communication framing:** [labeled / substantively / neither / ambiguous] — *protection turns on conduct and context, not the label; `[SME VERIFY]` against the applicable UK rule*

## Facts alleged

[their version, in one paragraph]

## Legal basis cited

[citations — each inline-flagged with `[SME VERIFY: applicability / currency / jurisdiction]` — do not rely on any citation here without independent check]

## Threats / next steps they state

[list]

---

## Portfolio cross-check

**Direct match:** [slug if exists, or "none"]
**Type match / precedent:** [list or "none"]
**Subject overlap:** [list or "none"]
**Recommendation:** [new matter / add to existing / link via related_matters / standalone inbound]

---

## Merit assessment

**Facts:** [alignment with our version; disconnects]
**Legal basis:** [applicability, with flags]
**Their case if proceedings issued:** [one paragraph]
**Our defences:** [one paragraph]
**Damages proportionality:** [assessment]
**Credibility of threat:** [will they issue proceedings? capacity? repeat litigant?]

**Triage rating:** [substantial / debatable / weak / frivolous] — *structured read for routing, not a merit opinion; `[SME VERIFY: counsel to confirm before relying on this]`*

---

## Response options

### A. Substantive response
[Rationale, tradeoffs, next step]

### B. Holding letter
[Rationale, tradeoffs, next step — including any pre-action protocol engagement obligation]

### C. Settlement response
[Rationale, tradeoffs, next step — without-prejudice framing required]

### D. Ignore + preserve
[Rationale, tradeoffs, next step]

**Recommendation:** [A/B/C/D] — [two sentences why] — `[SME VERIFY: counsel to confirm before executing]`

---

## Deadlines

- **Their stated deadline:** [date]
- **Our internal decision deadline:** [date]
- **Applicable pre-action protocol response period:** [date if identifiable — `[SME VERIFY]`]
- **Legal deadlines:** [limitation period, cure periods, procedural — with dates]

---

## Immediate actions

- [ ] Legal hold issued — [yes/no] — if no, run `/legal-hold [slug] --issue`
- [ ] Matter created in log — [yes/no/TBD]
- [ ] Solicitors/counsel assigned — [who]
- [ ] Insurance tendered — [yes/no/N-A]
- [ ] Internal escalation (GC/CFO/business lead) — [who/when]
```

### Step 7: Hand off

Based on recommendation and user confirmation:

- Matter creation → hand off to `/matter-intake` with: counterparty, type, `source: letter-before-action-inbound`, initial theory framed defensively, pre-populated.
- Counter-response as outbound demand → hand off to `/demand-intake` with: counterparty, context from triage, desired outcome as the response.
- Link to existing matter → update that matter's `related_matters` in `_log.yaml`; append event to its `history.md`.
- Standalone → leave in `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/inbound/`; no portfolio change.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customise the options to what this skill just produced.

## What this skill does not do

- **Validate cited law.** Flags cites for the user to run through the uk-legal MCP, BAILII, or legislation.gov.uk. Inventing legal analysis on inbound demands is a professional responsibility risk.
- **Send a response.** Drafts are drafted in `demand-draft`; this skill stops at the triage decision.
- **Decide merit definitively.** The rating is a read for triage; a formal merit opinion lives with external solicitors or more thorough analysis.
- **Make the matter-creation call.** Surfaces the recommendation; user decides.
- **Verify pre-action protocol compliance.** Flags whether the sender appears to have followed a protocol; confirming compliance (or arguing non-compliance) is for external solicitors.
