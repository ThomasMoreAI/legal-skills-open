---
name: daily-briefing
title: daily-briefing
description: Produces a portfolio-level morning briefing for an LPM running two or more active matters. Reads email, call notes and matter state across the portfolio and produces a triage surface structured around meetings (today and this week), deliverables (what is due, when, to whom), issues (current problems requiring action), and risks (plausible future problems requiring monitoring). Also reads Outlook Calendar to surface upcoming matter-relevant meetings and to flag past meetings where no follow-up correspondence has been identified. Use when the user asks "run my daily briefing", "portfolio briefing", "what do I need to know today", "what's landed overnight", "Monday sweep", "pre-09:00 briefing", "weekend catchup", or pastes correspondence spanning two or more matters. Not for single-matter briefings (use matter-drill-down) or for audience-facing status reports (use status-report-drafter). Produces a .docx working surface for the LPM's own consumption, not distribution.
author: legalopsconsulting
author_url: https://github.com/legalopsconsulting/lpm-skills/tree/main/skills/daily-briefing
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# daily-briefing

Portfolio-level triage surface for an LPM running two or more active matters. The skill reads correspondence, matter state, and calendar data across the portfolio and produces a morning briefing structured around four primary elements: meetings, deliverables, issues, and risks. Supporting context orients the reader enough to form questions of others — it does not try to answer every question itself.

The discipline the skill encodes is cross-matter ranking. An LPM running a portfolio does not read their matters sequentially. They rank across the book — a Green matter with a client call at 10:00 today beats a Red matter in steady state. This skill makes that ranking discipline explicit and reproducible.

## When to use this skill

- The user pastes correspondence spanning two or more matters and asks for a briefing
- The user asks "what do I need to know today/this week across my portfolio"
- The user invokes a scheduled Monday sweep or weekend catchup
- The user asks for a pre-09:00 triage across their active book

For a single matter zoom-in, use `matter-drill-down`. For an audience-facing status report on one matter, use `status-report-drafter`.

## Input Classification (apply before mode selection)

Classify the input before selecting a mode. The cost of misclassification (running the wrong mode) is higher than the cost of the classification step.

**Step 1 — Matter count.** Scan inputs for matter identifiers, client names, or matter-specific context.
- If inputs span two or more matters → this skill applies. Proceed to Step 2.
- If inputs are about a single matter → **Hard gate. Stop. Do not produce any briefing content from this skill.** Route to `matter-drill-down` using the exact handoff response specified in the Boundary section below. This is not a suggestion or a preference. Producing a portfolio-framed document on a single-matter input — including any hybrid labelled "Mode 1 — Portfolio briefing (single-matter input)" or similar — is a skill failure, not a graceful degradation. The pedantic response is the correct response.

**Step 2 — Timeframe.** Identify the timeframe the user has specified or implied.
- "Monday sweep" or "weekend catchup" → Mode 3
- "Last X hours/days" or a specific date range → Mode 4
- No timeframe specified → Mode 1 (default)
- "Drill into [matter]" or "focus on [matter]" → route to `matter-drill-down`

**Step 3 — Input tagging.** If the user has tagged inputs by source (`[FROM LC]`, `[INTERNAL]`, `[CLIENT]`), use those tags to route attribution in the output. Do not strip them.

**Step 4 — Matter silence detection.** After confirming multi-matter input, check each matter on the portfolio roster against correspondence provided.
- For each silent matter (on roster, no correspondence): note the matter as silent at this step.
- Do not treat roster entries as substantive input. A roster tells you the matter exists, its RAG, partner, LPM, fee model, and WIP. It does not tell you what is happening on the matter this week.
- For silent matters, the only permitted content in the briefing is: (a) one-line mini-briefing stating "no substantive update this period's inputs"; (b) the matter's roster facts (lead partner, LPM, RAG, phase) if explicitly needed for a handoff or partner attention reference; (c) inclusion in the Information Gap Flag in the Summary if three or more matters are silent.
- A calendar entry for a silent matter does not convert it to active status. Record the meeting in the MEETINGS section but hold the silence discipline everywhere else in the briefing.
- If three or more matters on the portfolio roster are silent, this is a portfolio-level signal — see Summary section instructions.

## Before Starting Any Mode

Before producing any briefing, check:

**Portfolio roster.** Inputs must identify the matters in the portfolio. Look for a roster (matter names + identifiers + lead partner + lead LPM + RAG) at the top of the input, or infer from matter-specific correspondence. If no roster is provided and cannot be inferred, ask once: *"What matters are in scope for this briefing?"* Do not proceed without a roster.

**Timeframe.** State the timeframe explicitly in the output header. Inferred from user language or inputs, not assumed.

**Owner.** State the LPM's name in the output header. If not provided, use a placeholder `[LPM NAME]` — do not assume.

**Identifiers.** The briefing references multiple matters. Each matter mini-briefing includes matter name and matter number in its heading. Matter numbers use placeholder `[M-NUMBER]` if not provided in inputs.

## Boundary

This skill produces a **portfolio-level triage surface for the LPM's own consumption**. It does not:

- Produce status reports for distribution (use `status-report-drafter`)
- Produce single-matter zoom-in (use `matter-drill-down`)
- Update RAID logs (use `risk-and-issues-manager`)
- Draft scope change memos (use `scope-change-controller`)
- Produce budget variance analysis (use `budget-and-fee-manager`)

The briefing surfaces triggers that invoke those skills. It does not do their work.

If the user pastes single-matter content and asks for a briefing, **stop**. Do not produce any content beyond the routing response. The response is literally:

> *"Single-matter input detected (matter: [matter name]). The daily-briefing skill produces portfolio-level views across two or more active matters. Run `matter-drill-down` on [matter] for a focused single-matter working view. No briefing produced from daily-briefing."*

Do not produce a "matter-level briefing structured to the template where possible". Do not produce a "Mode 1 — Portfolio briefing (single-matter input)" hybrid. Do not produce "a useful output rather than being pedantic". The pedantic response is the correct response. Producing a portfolio-framed document on a single matter is a failure mode, not a graceful alternative. The template is designed for cross-matter ranking; a single-matter input cannot be ranked, and cross-matter patterns cannot be assessed from one matter. Reshaping the template for single-matter use produces a document that looks like a briefing and fails at the primary job of the skill.

## Operating Modes

### Mode 1 — Portfolio briefing (default)

**Fires when:** User requests a briefing across the portfolio with no specific timeframe, or when inputs span multiple matters without timeframe context.

**Input:** Correspondence, call notes, matter baseline, and calendar data (if available) across the portfolio.

**Output:** Portfolio briefing using the standard template (below).

### Mode 2 — Single-matter routing

**Fires when:** User requests a zoom-in from portfolio context — "drill into [matter]", "focus on [matter]" — but has not invoked `matter-drill-down` directly.

**Handoff rule:** If the user wants a working view on a single matter, route to `matter-drill-down`. Do not produce a single-matter briefing from this skill.

*"You want the working view on [matter]. Invoke `matter-drill-down` for the full view. If you want a one-paragraph position summary of that matter within today's portfolio briefing, I can include it in a Mode 1 output."*

### Mode 3 — Monday sweep

**Fires when:** User asks for "Monday sweep", "weekend catchup", "what landed over the weekend", or the monday-sweep scheduled Routine invokes the skill.

**Input:** Correspondence spanning Friday 17:00 through Monday 07:00 (or equivalent weekend window), plus matter baseline. Calendar past window extended to Friday 17:00 to cover weekend meetings.

**Output:** Standard briefing template (below) with one addition:
- **Weekend developments** section (items that landed between Friday close and Monday open)

### Mode 4 — Ad-hoc timeframe

**Fires when:** User specifies a timeframe — "last 48 hours", "since Wednesday", "this morning".

**Input:** Correspondence bounded to the specified window.

**Output:** Standard briefing template scoped to the timeframe. Calendar retrieval uses standard windows (past 7 days, week ahead) regardless of correspondence window. Flag explicitly where matter state precedes the timeframe and remains relevant.

## Standard Template (Modes 1, 3, and 4)

Produce the template sections in this exact order. Do not reorder. Do not omit. If a section has no content, state "No items this period" and move on.

```
DAILY BRIEFING — [LPM Name]
Prepared: [Date and time]
Mode: [1 / 3 / 4 — name]
Portfolio: [Matter count — short names]
Timeframe: [Start through End]
LPM ownership: [Which matters user leads vs oversees]

SUMMARY
[3–5 lines. Cross-matter framing, not sequential matter summaries.
Name the portfolio-level signal in one sentence. Identify the one or
two items that shape the day. State what needs attention before 09:00.
Where a meeting today is the primary constraint on how the rest of
the briefing reads, name it here — e.g. "Client call on Meridian
at 10:00 is today's primary constraint."

Information Gap Flag when applicable: if three or more matters on
the portfolio roster are silent in the input, name this explicitly
in the Summary as a portfolio-level signal. Example:
"Three of six matters (Aldwych, Nexus, Hartwick) are silent in this
period's inputs — briefing covers the three matters with
correspondence received. Confirm status on the silent three before
acting on this briefing alone."
The purpose is to alert the reader that the briefing is partial,
not to fabricate content to fill the gap.]

[Mode 3 only:]
WEEKEND DEVELOPMENTS
- [Item with matter, source, and one-line summary]
- [...]

MEETINGS — TODAY AND THIS WEEK
Upcoming matter-relevant calls and meetings for the week ahead,
ranked by imminence. Past meetings (last 7 days; Mode 3: since
Friday 17:00) noted where no follow-up correspondence has been
identified — for the LPM's awareness, not as a directive.

Upcoming:
| # | When | Matter | Meeting | Attendees | Notes |
|---|---|---|---|---|---|
| 1 | [Day, time] | [...] | [...] | [...] | [...] |

Past — no follow-up identified (soft flag only):
| Matter | Meeting | Date | Note |
|---|---|---|---|

If no calendar data is available: state "Calendar not retrieved
this session — paste calendar entries or connect M365 Calendar
to populate." Do not invent meetings. Do not infer meetings
from correspondence references. If calendar is empty or
unavailable, this section states so and stops.

DELIVERABLES — DUE TODAY OR THIS WEEK
Ranked across the portfolio by urgency and impact, not within matters.
Maximum 8 items. If more than 8 genuinely qualify, flag capacity
pressure in the SUMMARY and rank the top 8.

| # | Matter | Deliverable | Owner | By when | Why this matters |
|---|---|---|---|---|---|
| 1 | [...] | [...] | [...] | [...] | [...] |

ISSUES — CURRENT
Problems requiring action. Each with status and enough context for
the reader to act or to form questions.

| Matter | Issue | Status | Context for action |
|---|---|---|---|

RISKS — PLAUSIBLE FUTURE
Problems that may materialise. Each with probability/timing signal
and mitigation context.

| Matter | Risk | Signal | Mitigation context |
|---|---|---|---|

CROSS-MATTER PATTERNS
Signals that appear only when matters are viewed together. Name the
dynamic, not just the items. Examples: partner load pressure, LPM
load pressure, fee-structure exposure wave, shared-client overlap,
regulatory-driven disruption. If no patterns present, state
"No cross-matter patterns identified this period".

PARTNER ATTENTION — PORTFOLIO VIEW
Items requiring a lead partner's decision, response, or action.
Referenced by deliverables or issues section number, not duplicated.

| Matter | Partner | Item | Urgency | Reference |
|---|---|---|---|---|

MATTER MINI-BRIEFINGS
Length varies with matter weight. A matter in steady state gets
1–2 lines. A matter in active flux gets a paragraph. Do not
normalise length.

### [Matter 1 name] ([Matter number])
RAG · Phase · Lead Partner · Lead LPM · Fee model · WIP/Budget
[1–5 lines: current position, what is shaping the week, watch items.]

### [Matter 2 name] ([Matter number])
[...]

READING LIST — WHAT TO OPEN FIRST
Triage judgment. Max 5 items. Each item is something that would
most change the reader's day if read first. Not a summary of
content elsewhere in the briefing. Read times included.

| # | Source | Matter | Why this first | Read time |
|---|---|---|---|---|

HANDOFFS FLAGGED
Single-matter skills to invoke as follow-through. Each row names
the matter and the specific trigger.

| Skill | Matter | Trigger | Priority |
|---|---|---|---|

End of briefing.
```

**Output rule:** Produce from available information. Use placeholders for unknowns (e.g. `[DATE TBC]`, `[LPM NAME]`). Do not withhold pending complete data. Do not ask questions before producing. Do not end with "want me to produce this as a .docx?" — produce the .docx.

**Attribution rule:** When a named individual in the inputs has produced substantive analysis or a recommendation (financial variance call, LC silence escalation judgment, scope framing recommendation), attribute it by name in the relevant section. Do not generalise to "the team" or "the matter".

## Domain Knowledge

### Cross-matter ranking discipline

Portfolio briefings are not matter reports stacked end to end. An LPM does not read matter by matter — they rank across the book. A Green matter with a client call at 10:00 today genuinely beats a Red matter in steady state. RAG is a trailing indicator of matter health; meeting imminence and deadline urgency are the leading indicators of today's action requirement. The two are different axes.

**In the Deliverables section, rank across matters. Do not group by matter.**

### Calendar and meetings

**Meeting imminence as a ranking signal.** A matter with a client call or partner decision meeting today shapes how the rest of the briefing reads. Name the meeting in the SUMMARY when it is the day's primary constraint. The MEETINGS section surfaces it for planning; the SUMMARY contextualises it so the reader knows what is shaping the day before reading anything else.

**Past meeting gap detection — judgment, not compliance.** When a past meeting appears in the calendar record and no follow-up correspondence is identifiable, flag it softly in the past-meetings table. The question is not "was there a follow-up?" as a rule — it is "was this the type of meeting where a follow-up would be expected?" Apply this distinction:

- Client calls with substantive agenda → soft flag if no follow-up email, action note, or instruction identified
- Partner decision meetings → soft flag if no decision record or follow-on instruction identified
- LC calls → soft flag if no instruction email or written confirmation follows
- Internal team check-ins → judgment call; routine standups do not require follow-up; a review meeting where decisions were expected does
- Admin or scheduling calls → no flag expected

The flag is for the LPM's awareness only. Use the language "no follow-up correspondence identified" — not "follow-up overdue" or "action required". The LPM decides whether to chase. Do not escalate a past meeting to the ISSUES table solely because no follow-up was found; independent evidence of a problem is required to promote it beyond the soft flag.

**Calendar matching to matters.** Use the shortest distinctive keyword from each matter name as the search term — "Project Meridian" → search for "Meridian". Match calendar entries to matters by subject line keyword, meeting organiser, or attendee list (partner name, LC name, matter-specific contacts). Flag any entry that appears matter-relevant but cannot be matched to a specific matter — the LPM may know the context.

**A calendar entry for a silent matter.** Record the meeting in the MEETINGS upcoming table. A scheduled call on a quiet matter is a legitimate meeting requiring preparation. It does not promote the matter to active status in Deliverables, Issues, Risks, or Mini-Briefings. The silence discipline holds everywhere except the MEETINGS section.

**Do not invent meetings.** If calendar data is absent or connected retrieval returns nothing, state so and leave the section empty. Do not infer meetings from correspondence (an email referencing "our call on Tuesday" does not populate the MEETINGS table — only confirmed calendar entries do).

### Restraint on steady-state matters

A matter in steady state with no live items gets 1–2 lines in the mini-briefing section and no appearance in Deliverables, Issues, or Risks. Padding a steady-state matter to match an active matter's content is the failure mode that destroys the reader's trust in the skill within two uses. If a matter is quiet, say so in one line and move on.

### Silence is a legitimate output

If an input is silent on a matter in the portfolio roster, report that matter as "no substantive update this period" and move on. Do not invent state, infer positions from matter-type stereotypes, or fill gaps with generic commentary. The reader will chase.

### Issues vs risks — the taxonomy matters

- **Issues** are confirmed problems requiring action. Deadline missed. Counterparty rejected. Budget breached. These need owners and mitigation now.
- **Risks** are plausible future problems requiring monitoring. Counterparty silent for N days. Regulatory regime under review. LC capacity signals thin. These need watch status and mitigation room.

**Silence on its own is a risk, not an issue.** LC has not responded for 8 days — risk (ratcheting toward issue). LC has formally rejected the instruction — issue. Do not promote risks to issues without confirmation.

Past meetings with no identified follow-up sit in the MEETINGS past-meetings table as soft flags. They are not risks and not issues unless independent evidence of a problem exists beyond the absence of a follow-up email.

### Cross-matter patterns

The skill must actively look for patterns. Named patterns to check against every briefing:

- **Partner load pressure** — same partner lead on 3+ matters with simultaneous critical items
- **LPM load pressure** — same LPM on 2+ matters where both are generating urgent work
- **Fee-structure exposure wave** — 2+ matters with active fee-structure pressure (approaching cap, structural variance, fixed-fee on a newly-disputed matter)
- **Scope expansion wave** — 2+ matters with active scope signals
- **Shared-client overlap** — same client across 2+ matters
- **Regulatory-driven disruption** — 2+ matters affected by the same external regulatory change

Name the dynamic, not just the items. "Same LPM on both Amber matters" is descriptive. "LPM load pressure — both Amber matters assigned to the same LPM, both generating today-urgent work with no natural buffer between" names the pattern.

### Reading list triage

The reading list is not a summary of content elsewhere in the briefing. It is the reader's question: *"If I only have 15 minutes before the first call, what would most change my day if I read it first?"* Each item earns its place by being decision-changing, not by being important in general.

### Attribution to named individuals

When a named human in the inputs has produced substantive operational judgment — a fee-variance analysis, a scope-framing recommendation, a tactical observation on how to handle a difficult client call — the briefing surfaces that judgment and attributes it by name. Generic attribution to "the team" is the failure mode. Senior LPM reasoning is valuable and named.

## Output Format

**.docx by default.** All outputs from this skill are produced as .docx files unless the user explicitly requests markdown output.

**Produce, do not ask.** Produce the .docx on invocation. Do not end output with "want me to produce this as a .docx?" or similar conditional offers. The skill produces the output; the user asks for variations if needed.

**Label is "SUMMARY", not "BLUF".** Reader-facing outputs use plain language section labels.

**No preamble.** The output opens with the identifier header. No "Here is your briefing..." or "I've analysed the inputs and..." preamble.

**Anti-pattern: single-matter rescue.** When input is single-matter, do not attempt to reshape the portfolio template for single-matter use. Do not produce a "Mode 1 (single-matter input)" hybrid. Do not add notes like "Cross-matter patterns cannot be assessed from a single matter" in a section that then retains the portfolio structure. Route and stop. The Boundary section specifies the exact routing response — use it verbatim.

**Silent matters rule.** A matter with no correspondence in the input has only two permitted appearances in the briefing: (a) its one-line mini-briefing stating "no substantive update this period's inputs"; (b) its roster-level facts (partner, LPM, RAG, phase) if referenced in a handoff or partner attention item. Do not produce deliverables, issues, risks, cross-matter pattern content, reading list items, or operational specifics for silent matters. Do not invent step plan deadlines, pricing queries, partner touchpoints, associate names, client names, deliverable dates, or any specific operational content. If a cross-matter pattern would require populating a silent matter to justify, either drop the pattern or name it at roster-level only (e.g., "Ben Okonkwo is lead LPM on one Red matter with active correspondence and one Green matter silent this period — monitor bandwidth allocation"). Under no circumstances fabricate content for silent matters from the roster, from training data, or from domain knowledge about similar matter types. The roster is not a licence to populate matters from general reasoning.

**Acknowledgment-then-violate anti-pattern.** If you have written in the Summary that a matter is silent, you must not then produce operational content for that matter anywhere else in the briefing. Acknowledging silence does not license populating content downstream. The Information Gap Flag in the Summary, the mini-briefing for each silent matter, any cross-matter pattern reference, and any handoffs or partner attention references must all be consistent. A silent matter is silent across the whole document.

Specific prohibited moves:
- Summary flags matter as silent, mini-briefing then contains substantive content → violation
- Mini-briefing says "no substantive update this period's inputs", cross-matter pattern section then adds "(with a pricing query pending)" or "(with X open point)" → violation; the parenthetical is the fabrication path
- Mini-briefing is silent, but deliverables/risks/handoffs/reading list tables contain matter-specific items → violation
- LPM load pattern requires saying something about a silent matter: state at roster level only ("silent this period — monitor bandwidth allocation"). Do not add operational detail to make the pattern feel substantive.

The test to apply: if the Summary has acknowledged a matter as silent, could the briefing be shown to the matter's lead partner without any content in it being unfamiliar to them? If not, fabrication has occurred. The skill must hold the silence line consistently.

**Produce from available information.** Placeholders for unknowns, not questions. If the LPM name is not in the inputs, use `[LPM NAME]`. If a matter number is not known, use `[M-NUMBER]`. Flag placeholders in an "Information to confirm" line at the end of the document, not at the start.

## LPM vs Attorney Boundary

The briefing is an LPM triage surface. It surfaces matters requiring attorney attention but does not opine on legal strategy or client advice. Where a matter's critical item involves attorney judgment (legal risk assessment, client advice framing, privileged communications), the skill references the item and routes it to the lead partner for decision — it does not offer legal analysis.

## Cross-Skill Handoffs

The daily-briefing skill is the highest-level LPM skill. It consumes nothing from other skills; it surfaces triggers that invoke them. Standard handoffs (produced in the "Handoffs flagged" section of the output):

- Scope signal requiring formal assessment → `scope-change-controller`
- RAID update required (risk, issue, decision, assumption) → `risk-and-issues-manager`
- Single-matter status report for distribution → `status-report-drafter`
- Single-matter deep drill-down or handoff briefing → `matter-drill-down`
- Local counsel non-response or escalation → `local-counsel-manager`
- Budget variance analysis, forecast-to-complete → `budget-and-fee-manager`
- Resource or capacity conflict → `resource-planner`
- Stakeholder comms plan update → `stakeholder-comms-planner`

Each handoff row in the output includes matter, trigger, and priority.

## M365 Connected Mode

**Calendar retrieval (all modes).** When the M365 Calendar connector is available, query `outlook_calendar_search` for each matter in the roster using the shortest distinctive matter name keyword. Run two windows per matter:
- **Future:** today through end of current week
- **Past:** last 7 days (Mode 3 Monday sweep: Friday 17:00 through Monday morning)

Cross-reference past calendar entries against retrieved email correspondence to identify meetings with no follow-up. Surface results in the MEETINGS section. Do not query calendar before checking whether the connector is available — if unavailable, state so in the MEETINGS section and proceed.

**Mode 1 (Portfolio briefing).** Connected mode enables the skill to query Outlook for matter folders identified in the roster, retrieve correspondence in the specified timeframe, query Calendar for the week ahead and the past 7 days, and produce the briefing without user paste.

**Mode 3 (Monday sweep).** Connected mode enables scheduled invocation via the monday-sweep Routine. Default correspondence window: Friday 17:00 → Monday 06:00. Calendar past window extends to Friday 17:00 to cover weekend meetings. The Routine queries all matter folders identified in the user's portfolio roster (persisted as Project Memory or stored artefact).

**Mode 4 (Ad-hoc timeframe).** Connected mode retrieves correspondence within the user-specified window. Calendar retrieval uses the standard windows (past 7 days, week ahead) regardless of the correspondence window.

**Manual mode fallback.** All four modes operate fully on pasted input. Calendar entries can be pasted directly alongside email and call notes; if so, process them using the same matching logic as connected mode. If no calendar data is provided and connected retrieval is unavailable, state "Calendar not retrieved this session" in the MEETINGS section and proceed with email and correspondence inputs only.

**Future connectors.** A DMS or practice management system connector would enable matter baseline retrieval (phase, fee model, WIP) from the system of record rather than from user-pasted roster. Deferred.

## Time-Sensitive Assumptions

- Portfolio roster format assumes matter identifiers from Intapp Open or equivalent practice management system. Firms using different systems will require a roster format adjustment.
- Connected mode patterns assume M365/Outlook as the email and calendar environment. Firms on Google Workspace or other platforms will require connector-specific adjustment.
- The "monday-sweep" Routine schedule (Mondays 06:00 local) is Europe/London default. User-customisable.
