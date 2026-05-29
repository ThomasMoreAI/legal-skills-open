---
name: scope-change-controller-scott-margetts
title: Scope Change Controller
description: 'Scope management for legal matters — baseline capture, in-flight change control, OOS documentation, and scope retrospective. Use when asked to review scoping assumptions, assess whether work is in or out of scope, draft a scope change notice, track scope changes, prepare an OOS justification, run an OOS report, prepare a scope call agenda, or review what changed on a matter. Trigger on: ''scope change'', ''out of scope'', ''OOS'', ''scope creep'', ''is this in scope'', ''the client wants us to also'', ''additional work'', ''scope review'', ''what changed from the original scope'', ''we need to revisit the quote'', ''the budget assumed'', ''OOS report'', ''scope call with the client'', ''run a scope report''.'
author: Scott Margetts
author_url: https://lawve.ai/en/skills/scope-change-controller-scott-margetts
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Scope Change Controller

## Purpose

Manage scope across the lifecycle of a legal matter. Scope is the baseline that everything else references — status is progress against scope, risk is threat to scope delivery, budget is the price of scope. When scope is unmanaged, every other discipline is working against an unreliable target and the client gets surprised.

The fundamental problem: legal teams consistently fail to manage scope because it feels adversarial, it's perceived as the partner's job, and nobody established a simple mechanism for managing change at matter setup. The result is budget overruns, write-off conversations that could have been managed change conversations, and clients who conclude that external counsel never sticks to their budget.

Good scope management is a service to the client, not a confrontation. The client would rather have a managed conversation about additional costs mid-matter than a surprise invoice at the end. Framing scope change as professional and unemotional — an opportunity for both parties to deliver their sides of the bargain — is as important as the mechanics.

### Core design philosophy: automate capture, surface for confirmation

LPMs and attorneys know that recording scope changes is valuable. They won't consistently do it because the capture overhead exceeds the perceived value at the moment it needs to happen. "Another job to do" and "reporting" are the common dismissals — missing the big unlock, which is that contemporaneous data enables learnings which enable iterative improvement. But only if we make capture as close to zero-effort as possible.

The principle across this skill: **don't ask the human to create the record — create the record and ask the human to confirm it.** In manual mode, this means the skill produces the draft OOS entry, the draft communication, and the draft scope register update from the input provided. In connected mode, this means Claude detects the scope signal, drafts the entry with source evidence auto-linked, and surfaces it for confirmation. The difference between "log this" (15 minutes, doesn't happen) and "I've found this — confirm or dismiss?" (30 seconds, happens).

## Two layers — scale to the matter

Scope management must be proportionate. An overengineered process that nobody maintains is worse than a simple one that gets followed.

### Standard (every matter)

Three deliverables, each lightweight enough that a tired LPM at 7pm on a Thursday will actually do them:

1. **One-page scope summary** — the 3-5 key assumptions from the engagement letter, stated plainly, with the quantifiable parameter for each. Produced at matter setup. Takes 15 minutes. Shared with the delivery team with one instruction: "If anything changes from these, tell me."

2. **Simple OOS list** — when something comes up that's outside scope, log it: what it is, when it was identified, whether it's been raised with the client, and the outcome. One line per item. Could be a table in an email, a few rows in a spreadsheet, or a note on the matter file.

3. **Client communication draft** — when an OOS item needs raising with the client, the skill drafts the email for the partner. This is where the skill adds the most value — the LPM doesn't have to draft the awkward conversation from scratch.

The Sibelius €1.6m OOS recovery happened with basic tools and discipline. Spot it, flag it, track it, invoice it.

### Extended (large or complex matters)

Use when the matter economics justify the investment: £1m+ fees, 12+ month timeline, multiple jurisdictions, fixed or capped fee basis where scope sensitivity is high. The potential OOS recovery needs to exceed the overhead of maintaining the system.

Extended adds:

4. **Full scope register** — 10-15 items with structured fields. Maintained in an Excel workbook.

5. **Fortnightly scope pulse check** — a short, specific message to the delivery team referencing 3-4 highest-risk assumptions by name.

6. **Scope retrospective** — at matter close, analyse the delta between original and actual scope.

7. **OOS call agenda** — a structured document the partner walks into a client scope call with.

**The trigger for Extended isn't ambition — it's matter economics.** If the cap is £1.2m and potential OOS recovery is £100k+, the workbook pays for itself. If the cap is £50k on a 3-month matter, Standard is all you need.

## Step-by-step process

### Step 1: Determine what's needed

**How this skill gets invoked in practice:**

Scope management fails when it's positioned as a standalone activity. In reality, it works when it's embedded in workflows the LPM is already doing:

- **At matter setup:** Baseline capture as part of the matter setup process. The one planned, deliberate invocation.
- **During email batch review:** "Here are this week's emails on Redwood — flag any scope issues." LPMs already batch-process email for status reporting. Adding scope review to the same pass is low friction.
- **Before drafting the status report:** "Before I draft the status report, run the scope check on these emails." Makes scope review a precursor to an activity that's already happening.
- **Before billing:** "We're about to bill on Atlas. Are there any OOS items to raise first?" The billing cycle is a natural trigger point.
- **When another skill flags it:** The status-report-drafter or risk-and-issues-manager surfaces a scope signal. The LPM follows the handoff.
- **When the partner asks:** "Help me justify this overrun." Retrospective mode — always reactive, but still valuable.

In connected mode, the invocation model reverses: Claude monitors matter emails against the scope register and surfaces signals for the LPM to confirm or dismiss. The LPM doesn't invoke the skill — the skill invokes the LPM.

Common triggers:

- "Here's the engagement letter — what are the scoping assumptions?" → **Scope summary (Standard) or full register (Extended)**
- "Is this in scope?" / "The client wants us to also handle X" → **Scope assessment**
- "We've blown the budget — trace it back to the scope" → **Retrospective assessment**
- "Run an OOS report for the client call" → **OOS call agenda (Extended)**
- "The matter is closing — what changed?" → **Scope retrospective (Extended)**

If the user hasn't indicated the matter size, ask: "Is this a matter where a simple scope summary will do, or is it large enough to warrant the full scope register?"

### Step 2: Establish the baseline

Every scope assessment needs a baseline. Ask:

- "Do you have the engagement letter, scoping email, or fee proposal?"
- "What were the key scoping assumptions in the quote?"

If no baseline document exists, flag it: "Without a documented scope baseline, it's hard to assess what's in or out. Recommend establishing one — even a short email confirming the key assumptions."

### Step 3: Extract the scope baseline

Read the engagement document. Extract:

- **Quantifiable parameters:** Entity counts, document counts, jurisdiction lists, witness numbers, employee headcounts, lease counts. Most likely to break, easiest to track.
- **Scope inclusions:** What the engagement explicitly covers.
- **Scope exclusions:** What it explicitly does not cover. These define where OOS starts.
- **Implicit boundaries:** Things not mentioned that could be assumed either way. Ambiguity is a scope risk.
- **Fee basis:** Fixed, capped, hourly, blended, staged. Affects how scope changes are handled commercially.
- **Conditions and caveats:** "Based on information provided to date" / "subject to no material change" — scoping assumptions in disguise.

**Standard: extract 3-5 items. Extended: extract 10-15 items.** Each should be something the team would genuinely need to revisit the price on if it changed. Not an exhaustive hedge list — a focused set of material assumptions.

### Surfacing historical scope knowledge at point of capture

When creating scope assumptions for a new matter, the skill should prompt for historical context: "Have you run similar matters before? Which scope assumptions typically don't hold on this type of work?"

This is the learning loop that connects Mode 4 (retrospective) back to Mode 1 (baseline capture). Without it, retrospective lessons sit in a document and the same assumptions breach in the same ways on the next matter.

**In manual mode:** Ask the question. The LPM knows from experience that entity counts always grow, that data rooms are always late, that employee headcounts miss contractors. Making the question routine surfaces tacit knowledge that would otherwise stay in the LPM's head.

**With a pattern library (Extended):** Maintain a simple reference document — "Common scope assumption breaches by matter type" — built from past retrospectives and the LPM's experience. When the skill identifies the matter type during baseline capture, it checks the library and surfaces relevant warnings:

*"This is an acquisition matter. On similar matters, the following assumptions have historically been breached: entity count (average +25% vs scoped), data room readiness (average 2 weeks late), employee headcount (contractors frequently excluded from initial figures). Consider building buffers or unit-rate mechanisms for these parameters."*

The pattern library doesn't need to be sophisticated — a markdown file with 3-5 common breaches per matter type is enough. It grows each time a scope retrospective is completed.

**In connected mode:** Claude searches SharePoint for scope retrospectives from similar matter types, extracts breach patterns, and surfaces them automatically during baseline capture. The historical data does the prompting rather than the LPM's memory.

This is the recursive improvement loop: matters produce retrospectives, retrospectives produce patterns, patterns inform the next matter's assumptions, better assumptions produce fewer breaches. Each cycle makes the scoping more accurate.

**The balance between protection and credibility matters.** Too many exclusions signal low confidence or intent to upsell. The test: would the LPM be comfortable explaining every scope assumption to the client at the outset? If not, it's too aggressive.

**Be aware of the "buying work" pattern.** Pricing aggressively low, scoping aggressively tight, then enforcing OOS on every deviation. This skill is not designed to enable that. Legitimate scope management protects both sides. If the scope register reads like a trap, it's being used wrong.

### Step 4: Assess scope changes (in-flight)

When new work or a request arises, assess against the baseline:

1. **Explicitly in scope?** No action needed.
2. **Explicitly excluded?** Clear OOS. Document and raise.
3. **Reasonable extension of agreed scope?** Grey area. The question to surface for the partner: would a reasonable client expect this included in the price? The LPM presents the evidence — what the engagement says, what the request involves, how closely related it is to the agreed work. The partner answers the question based on their knowledge of the client. The LPM does not make this call definitively.
4. **New work not contemplated?** Clear OOS.
5. **Same scope, more volume?** Scope assumption breach. Commercial response may differ — unit-rate adjustment rather than new scope notice.

**Materiality test:** Would this change the fee estimate if the client asked? One extra call is variation. 15 additional entities is material. The LPM makes this judgment based on fee basis and matter economics.

**Two patterns:**

**Proactive** (the goal): divergence identified before or during the work. Client hears about it as a managed change.

**Retrospective** (reality): budget blown, need to trace back to root cause. Which assumptions were breached, what additional work resulted, can it be quantified? The output is an evidence trail — factual enough for a client fee conversation or an internal write-off discussion.

### Step 5: Produce the output

**Summary first** — what scope changes exist, estimated impact, what decisions are needed. Label this section "Summary" in the output, not "BLUF." BLUF is the internal design principle; the reader sees "Summary."

**Recommendation tone** — "Recommend raising with the client" not "you must notify." Surface the signal, don't determine the response. This extends to talking points and coaching notes for the partner — use collaborative framing ("I'd suggest we lead with the facts" not "lead with facts"; "we should be careful not to let this dominate the call" not "don't let this dominate the call"). The LPM is advising a peer, not instructing a subordinate.

#### Standard: one-page scope summary

| # | Assumption | Parameter | Fee impact if breached |
|---|---|---|---|
| 1 | Target group structure | ≤5 entities | +£X per additional entity |
| 2 | Completion timeline | 4 months | +£50-80k/month beyond |
| 3 | ... | ... | ... |

Plus: "If anything changes from these assumptions, tell me immediately."

#### Standard: simple OOS list

| OOS # | What changed | Date flagged | Source | Raised with client? | Outcome |
|---|---|---|---|---|---|
| 1 | 3 additional entities | 10 Mar | R. Tan email to S. Margetts, 10 Mar, "Atlas DD — entity structure issue" | Yes — 12 Mar | Approved, +£40-70k |
| 2 | Shanghai rep office | 5 Mar | M. Li email to S. Margetts, 5 Mar, "Shanghai — scope question" | Pending | Awaiting partner decision |

One line per item. The Source column is critical — capture the email reference (sender, date, subject line) at the point you identify the scope change, not retrospectively. Twenty seconds to note at the time; hours to reconstruct six months later when building an OOS recovery case. This is the single highest-value habit in scope management. Without source references, the OOS list is assertions; with them, it's evidence.

#### Standard: client communication draft

**Not:** "This is out of scope and we need to charge you more."

**Instead:** "During the course of the work, we've identified [X] which wasn't contemplated in the original scope. We're happy to handle this — it involves [brief description]. The estimated additional cost is [range]. We wanted to flag this transparently rather than include it in the next invoice without discussion. How would you like us to proceed?"

Key principles:
- Lead with what was found, not with the fee
- Reference the original scoping assumption ("our quote assumed 100 entities")
- Offer options where possible
- Frame as transparency, not a billing exercise
- Don't apologise — scope change is a fact of complex legal work
- Get agreement before doing the work where possible

#### Extended: full scope register

| Field | Content |
|---|---|
| ID | SC-[sequential number] |
| Assumption | Stated clearly, quantifiably where possible |
| Source | Engagement letter clause, fee proposal paragraph, email reference |
| Parameter | The quantifiable measure |
| Confidence | Low / Medium / High |
| Status | Untested / Holding / Under pressure / Breached |
| Variance | If under pressure or breached: actual vs assumed |
| Financial sensitivity | How this assumption affects the fee |
| Owner | Who monitors this assumption |

#### Extended: OOS register entry

| Field | Content |
|---|---|
| OOS-ID | OOS-[sequential number] |
| Description | What has changed |
| Type | Scope expansion / Scope reduction / Assumption breach / Ambiguity |
| Related SC-ID | Which scope register entry is affected |
| Date identified | When the change was spotted |
| Identified by | Who flagged it |
| Estimated impact | Hours, cost, timeline — as a range if uncertain |
| Fee basis implication | How this interacts with the fee arrangement |
| Raised with client? | Date notified, or "not yet" with recommended approach |
| Approval status | Identified / Assessed / Notified / Client response (Approved/Denied/Partially approved/Under discussion) / Fee agreed / Absorbed |

Once fee is agreed, the OOS item enters normal billing. Don't duplicate billing system tracking.

#### Extended: OOS call agenda

When the user says "run an OOS report for a client call," produce a structured document:

- Summary: number of OOS items, total estimated additional fees, number needing client decision
- Summary table of open OOS items
- Per-item discussion points (3-5 minutes each): what changed, why, impact, recommendation, decision needed
- Space for notes/outcomes during the call
- Next steps

#### Extended: scope retrospective

At matter close, analyse the delta:
- Original assumptions vs actual, with variance per item
- Financial impact: total OOS identified vs approved vs absorbed vs disputed
- Timing: for each breached assumption, when was the breach detected vs when did it occur? The gap is the cost of late detection.
- Lessons: specific, actionable recommendations for future scoping

### Extended: Excel workbook structure

Four tabs:

**Tab 1: README.** What the workbook is, how each tab works, what the status fields mean, who maintains it.

**Tab 2: Scope Register.** Current state of all SC-entries. Filter by Status for items needing attention.

**Tab 3: Change History.** Append-only log of status changes. Columns: SC-ID, Date, Previous Status, New Status, Reason, Updated By. Never overwrite — this is the retrospective data.

**Tab 4: OOS Register.** Every OOS entry with its lifecycle. Filter by Approval Status to see what's been raised and where it sits.

## Scope management — the operational knowledge

### Why scope management fails

1. **The scope document disappears.** Filed in the DMS, never referenced again.
2. **Associates don't spot or report creep.** They're focused on the legal work. The fix: brief them on 3-5 assumptions at kickoff, one instruction — "tell me if anything changes."
3. **"Couldn't say no."** The Sibelius lesson. Perceived as adversarial. In reality, the client respects the discipline.
4. **Creep is gradual.** Twenty small requests, each trivial. "While you're at it..." Only the LPM sees the pattern.
5. **The retrospective never happens.** Same assumptions fail on the next matter.
6. **Source evidence isn't captured at the time.** The scope change is spotted, maybe even flagged verbally, but nobody notes the email reference. Six months later when the partner needs to justify the overrun, the LPM or worse the partner spends hours searching Outlook for the contemporaneous evidence. This is dead time — expensive when it's the LPM's, unacceptable when it's a partner's. Capture the email reference (sender, date, subject line) when you log the OOS item. That's the difference between an OOS list and an OOS evidence file.

### Scope creep vs scope change

**Creep:** Gradual, unintentional. The "while you're at it" pattern. Detect the pattern, quantify cumulative impact, raise it.

**Change:** Explicit, identifiable. "Can you also handle Shanghai." Assess, document, agree.

### How fee basis affects scope discipline

**Fixed fee:** Maximum sensitivity. Every extra piece of work is absorbed unless agreed as OOS.

**Capped:** Changes count against the cap. Additional work reduces remaining budget.

**Hourly:** Lower commercial sensitivity but unexpected bills damage the relationship.

### Scope pulse check (Extended — fortnightly)

Short, specific, referencing 3-4 assumptions by name. Example:

*"Quick scope check on Atlas: (1) Entity count — still 5, or more in the data room? (2) Redundancies — still no plans? (3) Data room — complete and usable? One-word confirmation is fine if everything's holding."*

Quick to send, quick to answer. Non-response is a signal. Don't send if nothing to check. Don't make it a checklist.

*Future enhancement: Outlook Actionable Messages could embed response buttons per assumption. Not universally available — noted as a possibility only.*

## Input processing

Engagement letters, fee proposals, scoping emails, matter correspondence. Scope signals from risk-and-issues-manager and status-report-drafter.

Look for: quantifiable parameters, inclusions/exclusions, conditions/caveats, "while you're at it" patterns, references to unscoped work, cost complaints suggesting unmanaged scope.

File inputs: engagement letter (primary baseline), scope register (if exists), budget tracker (overrun may indicate scope issue), RAID log (assumption breaches may indicate unlogged scope changes).

## Cross-skill handoff points

- **From risk-and-issues-manager:** Scope signals from decision extraction. Assumption breaches.
- **From status-report-drafter:** Budget variance suggesting scope issue.
- **To budget-and-fee-manager:** Scope change assessed — needs financial impact analysis.
- **To timeline-generator:** Scope change affects timeline.
- **To continuous-improvement-engine:** Retrospective findings feed future scoping.
- **To risk-and-issues-manager:** New scoping assumptions should be logged as A-entries.

## LPM vs attorney boundary

This skill assesses whether work falls within the agreed scope — operational and commercial judgment, not legal.

**Surface the signal, don't determine the response.** If DD reveals an undisclosed liability, the LPM flags it as potentially material. The LPM does not say "this is a warranty issue" or "this needs to be in the SPA" — those are legal determinations. The LPM says: "An undisclosed liability has been identified. Recommend the legal team assess the implications."

The skill does not interpret engagement letter clauses, advise on enforceability, determine how findings should be addressed in transaction documentation, or assess whether client requests are legally necessary.

**Professional tone principle — client-facing outputs:** All client-facing drafts and communications use professional, respectful language throughout. Avoid any framing that positions the firm against the client, implies the client is acting in bad faith, or characterises a professional exchange as adversarial. Clients raising queries or requesting changes are almost always doing so in good faith. Respond accordingly.

**Named-firm attribution rule:** Never reference a named firm anywhere in skill output — in documents, tables, or conversational text. This includes attributing rates, policies, practices, or organisational structures to any named law firm. The skill does not know any firm's actual structure, rates, or policies. Use "confirm with Pricing", "confirm with Finance", or "firm policy — confirm before applying." The rule applies to everything this skill produces, not just formal documents.

---

## M365 Connected Mode — the auto-capture unlock

**Connected mode invocation rule:** Search connected systems (Outlook, SharePoint, Teams) when doing so adds value — not as a default first step when sufficient input is already in the prompt.

- **Sufficient input already provided:** User has pasted emails, documents, or data with full context. Engage with what is there. Do not search first — it adds friction without adding information.
- **Input is incomplete or proactive surfacing is warranted:** User references something that should be retrieved ("there's an invoice in Outlook", "it's end of month"), or connected mode is running in background/scheduled mode. Search proactively — this is the inverted invocation model and is the highest-value connected mode behaviour.

The distinction is whether the user has already provided what is needed. If yes, work with it. If no, or if proactive surfacing serves the LPM, search.

In manual mode, the LPM does everything: monitors emails, spots scope signals, logs them, captures the source reference, drafts the communication. The overhead is why scope management gets abandoned on most matters.

Connected mode fundamentally changes the model: **Claude detects and drafts, the LPM reviews and decides.** The LPM's time shifts from administrative capture to commercial judgment — which is where their value actually lies.

**What Claude can automate with M365:**

- **Scan matter emails for scope-relevant language.** Patterns like "can you also," "while you're at it," "the client wants us to," "we've found additional," or any reference to quantities that differ from the scope register baseline ("8 entities" when SC-005 says 5). This runs continuously, not just when the LPM remembers to check.
- **Auto-capture source references.** When Claude identifies a scope signal, it already has the message ID, sender, date, and subject line. The source column in the OOS list populates itself. Zero effort from the LPM.
- **Compare incoming information against the scope register.** If a scope register exists in SharePoint, Claude cross-references every matter email against the registered assumptions and flags discrepancies.
- **Draft pre-populated OOS entries.** All fields filled from the email — what changed, when, who said it, source link, estimated impact from the scope register's financial sensitivity data. The LPM reviews and confirms rather than creates from scratch.
- **Draft the partner notification and client communication.** Ready for review and sending.
- **Maintain the OOS list.** Add entries, link sources, update status as responses come in.

**What still requires the LPM's judgment:**

- Is this genuinely OOS or a reasonable extension of agreed scope?
- Is it material enough to raise?
- Is now the right time commercially?
- What's the approach — recover, absorb, negotiate?

**The practical impact:** The reason scope management gets abandoned isn't ignorance — it's overhead. Every LPM has thought "that might be OOS but I'll deal with it later." Later never comes. With auto-capture, "later" becomes "now — here's a draft OOS entry with the source linked. Confirm or dismiss?" The barrier drops from 15 minutes to 30 seconds.

Without the connector, paste documents, upload files, or describe the scope verbally. Manual mode works — it's just slower and depends on the LPM's discipline to capture consistently.
