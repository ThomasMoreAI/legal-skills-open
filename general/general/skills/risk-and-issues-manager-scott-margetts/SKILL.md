---
name: risk-and-issues-manager-scott-margetts
title: Risk and Issues Manager
description: 'RAID log methodology with decision extraction from emails and meeting notes. Use when asked to identify risks, log assumptions, track issues, extract decisions from correspondence, create or update a RAID log, escalate a risk to an issue, assess project risks, validate or challenge assumptions, or capture scope-relevant decisions. Also triggers when the user pastes email chains and asks what decisions were made, or needs to find buried decisions and untested assumptions in correspondence. Trigger on: ''risk report'', ''RAID log'', ''what are the risks'', ''what decisions were made'', ''update the risk register'', ''what assumptions are we making'', ''what could go wrong'', ''flag any issues'', ''extract decisions from these emails''.'
author: Scott Margetts
author_url: https://lawve.ai/en/skills/risk-and-issues-manager-scott-margetts
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Risk and Issues Manager

## Purpose

Maintain a structured RAID log (Risks, Assumptions, Issues, Decisions) for legal matters and extract structured data from unstructured correspondence. This skill operates in two modes: RAID log maintenance (creating, updating, and managing the log) and decision extraction (identifying decisions, risks, assumptions, and scope-relevant information buried in email chains and meeting notes).

The decision extraction mode is the highest-value function. Decisions get made in email constantly — "let's leave Germany out for now," "we'll use the existing holdco," "client says they don't need a valuation" — and they're never formally recorded. Six months later when scope is disputed, budget is blown, or a workstream is stuck, nobody can find the email where the decision was made. This skill catches those decisions at the point they're made and logs them with the metadata needed to make them useful later.

## Operating modes

### Mode 1: RAID log maintenance

Create, update, and manage the four components of the RAID log. This is the ongoing discipline — the log is a living document that's reviewed regularly and updated as the matter progresses.

### Mode 2: Decision extraction from correspondence

The user pastes an email chain, meeting notes, or call notes. The skill scans for:
- **Decisions** — explicit or implicit choices that affect the matter's direction, scope, budget, or timeline
- **Risks** — newly identified uncertain events that could affect objectives
- **Assumptions** — premises being relied upon that may not hold, particularly inherited assumptions from DD or prior phases
- **Issues** — problems that have materialised and need resolution
- **Scope signals** — language that suggests work is moving in or out of scope, even if not explicitly framed as a scope decision

Output: structured entries ready to add to the RAID log, with flags for items that need follow-up or escalation.

### Mode 3: Risk identification from context

The user describes a matter setup, and the skill identifies the key operational risks based on the matter type, jurisdictions, team structure, timeline, and commercial arrangements. This is proactive risk identification — catching risks at matter setup rather than discovering them mid-execution.

## Step-by-step process

### Step 1: Determine the mode

Ask the user what they need. Common triggers:

- "Here's an email chain — what decisions were made?" → **Mode 2 (decision extraction)**
- "Set up a RAID log for this matter" → **Mode 1 (create)**
- "Update the RAID log with this" → **Mode 1 (update)** — ask whether they have an existing log to upload
- "What are the risks on this matter?" → **Mode 3 (risk identification)**
- "This risk has happened" → **Mode 1 (escalation: risk → issue)**

If the user just pastes an email chain without specifying, default to Mode 2 (decision extraction) — this is the most common use case and the highest-value function.

### Step 2: Process the input

**For Mode 1 (RAID log maintenance):**

Confirm the matter name and whether an existing RAID log is available to update. If the user uploads an Excel RAID log, read it and use the existing structure, numbering, and categories. If creating from scratch, use the standard structure defined below.

**For Mode 2 (decision extraction):**

Read the entire email chain or notes carefully. Don't skim — decisions are buried in mid-chain replies, throwaway sentences, and implicit agreements. Look for:

**Explicit decisions:** Direct statements of choice. "We've decided to..." / "Let's go with..." / "Client has confirmed..." / "Agreed — we'll proceed on that basis."

**Implicit decisions:** Choices made by omission or assumption — but only where someone with authority has genuinely chosen between alternatives. "I'll leave Germany out of the next round" (scope decision — someone chose to exclude Germany). "We don't need to worry about the valuation" (scope reduction — someone chose not to pursue it). These are dangerous because the decision-maker may not realise they've made a decision. Log with status "Implied" and flag for confirmation. **Important: don't confuse routine activity with implicit decisions.** Someone doing something (chasing by email, starting a review) is not a decision unless they explicitly chose that approach over alternatives.

**Conditional decisions:** "If the regulator comes back clean, we'll proceed with Option A." Log these as decisions with conditions noted — they need monitoring.

**Reversed or contradicted decisions:** Earlier in the chain someone decided X, then later someone decided not-X. Both should be logged — the reversal is itself a decision, and the history matters for scope and accountability.

**Scope signals:** Any language that suggests work expanding or contracting. "Can you also look at..." (scope expansion). "We don't need that anymore" (scope reduction). "That wasn't in the original brief" (scope awareness). "While you're at it..." (scope creep). These may not be formal decisions but they need to be captured and flagged for the scope-change-controller skill.

**Risk signals:** Language suggesting uncertainty or concern. "I'm worried about..." / "What happens if..." / "The regulator might..." / "We're running out of time on..." Also watch for absence — if a critical topic isn't mentioned when it should be, that's a risk signal.

**Assumption signals:** Statements that take something for granted or rely on an untested premise. "The DD confirmed the entity structure is clean" (assumption — was this actually verified?). "We should have the client's approval by next week" (assumption about client decision-making speed). "The local team can handle this within the existing budget" (assumption about cost). "The regulatory process should take about 4 weeks" (assumption about timeline). Also watch for inherited assumptions — things the team is relying on from the DD, the pitch, or a prior phase that haven't been re-validated. These are the assumptions most likely to fail because nobody is actively monitoring them.

**For Mode 3 (risk identification):**

Gather the matter context: type of matter, jurisdictions involved, team structure, timeline, budget basis (fixed fee, capped, hourly), client relationship, and any known constraints. Then apply the risk identification framework below.

### Step 3: Produce the output

**Lead with the summary.** The first thing in the output should be the "Items Requiring Immediate Action" section — the 30-second version for the partner who won't read further. This is the management-by-exception headline: what's on fire, what needs a decision, what are we relying on that might not hold.

Then provide the full IRAD detail (Issues, Risks, Assumptions, Decisions) for the reader who wants the complete picture. The summary tells them what to care about; the detail tells them why.

**Output structure:**

1. **Items requiring immediate action** — prioritised summary with log IDs (Issues/Critical risks first, failed assumptions second, Implied/Pending decisions third, decisions needed fourth)
2. **IRAD counters** — open item counts per category with [NEW]/[UPDATED] indicators. No overall rating.
3. **Risk heatmap** *(optional — include when format supports it easily, e.g. Excel)*
4. **Scope signals** — anything that may change the agreed scope, flagged for scope-change-controller
5. **Full IRAD log entries** — Issues, Risks, Assumptions, Decisions in that order, each with the field structures below

### IRAD counters

Place the counters once, immediately after the BLUF summary and before the full log detail. Do not repeat them in headers, subheadings, or elsewhere — one instance only.

A single summary line or small table showing the count of open items per category, with new and updated items highlighted. Example:

| Issues | Risks | Assumptions | Decisions |
|---|---|---|---|
| 2 open (1 new) | 8 open (2 new, 4 updated) | 9 active (2 new, 3 updated) | 7 total (2 new, 4 confirmed) |

This immediately tells the reader whether the log is growing, shrinking, or stable — and where the activity is concentrated this period.

**Do not produce an "overall risk rating" or "overall exposure" score.** A single rating (e.g. "HIGH") is meaningless — it collapses a complex picture into a label that invites debate about the label rather than the items underneath it. The counters are the summary. They tell the reader the scale and shape of what they're dealing with. If there are 3 Critical items, the reader can see that from the counters and the BLUF — they don't need a single word to tell them the programme is in trouble.

**Risk heatmap (9-box) — optional, include when format supports it easily.** The standard probability × impact grid with risk IDs plotted in each cell. Colour the cells: red (top-right), amber (diagonal), green (bottom-left).

|  | **Low Impact** | **Medium Impact** | **High Impact** |
|---|---|---|---|
| **High Prob** | | R-004 | R-003, R-008 |
| **Medium Prob** | | R-007 | R-010, R-013 |
| **Low Prob** | R-005 | R-009 | R-012 |

The heatmap shows clustering at a glance. If the top-right cell is crowded, the conversation is fundamentally different from when risks are spread across the grid. Update the heatmap each period — movement of risk IDs between cells over time is itself a useful signal.

**Assumptions can use the same 9-box** with Confidence (High/Medium/Low) on one axis and Impact if Wrong (Low/Medium/High) on the other. Low confidence + High impact assumptions are the equivalent of the top-right cell — actively monitor and validate these first. Include when the heatmap is being produced; omit when counters alone are sufficient.

**In docx:** Produce the heatmap as a formatted table with cell shading (red/amber/green) and risk IDs as text within cells. The counters sit as a simple one-row table between the summary and the detail.

**In Excel:** Use conditional formatting for heatmap colours. The counters can be COUNTIF formulas on the active log tabs, updating automatically as entries change status.

**RAID log entries** should follow the IRAD presentation priority (Issues, Risks, Assumptions, Decisions) — but use the structures below for each component regardless of presentation order:

#### Issues

Use colour coding on the Severity field to draw the eye: **Critical** (red), **High** (amber/orange), **Medium** (yellow), **Low** (green). The same colour scheme applies to Risk Exposure below.

| Field | Content |
|---|---|
| ID | I-[sequential number] |
| Issue | What has happened — state as fact, not uncertainty |
| Impact | What effect this is having on the matter (timeline, budget, scope, quality) |
| Severity | Low / Medium / High / Critical |
| Related risk | If this was a previously identified risk, link to R-[number] |
| Resolution plan | What is being done to resolve it |
| Owner | Who is responsible for resolution |
| Escalation | Who has been informed / who needs to be informed |
| Status | Open / In progress / Resolved / Escalated |
| Date raised | When the issue materialised |
| Target resolution | When this should be resolved by |

#### Risks

| Field | Content |
|---|---|
| ID | R-[sequential number] |
| Risk Name | 2-5 word shorthand (e.g. "Regulatory delay — Germany") |
| Description | What could happen and why |
| Category | Operational / Commercial / Regulatory / Resource / Client / External |
| Probability | Low / Medium / High (with brief reasoning) |
| Impact | Low / Medium / High (with brief reasoning — what happens if this materialises?) |
| Exposure | Probability × Impact assessment (not arithmetic — judgment on the combination). Colour-code to match Issue severity: **Critical** (red), **High** (amber/orange), **Medium** (yellow), **Low** (green). |
| Mitigation | What can be done to reduce probability or impact before it happens |
| Contingency | What to do if it happens despite mitigation |
| Trigger | How will we know it's happened? What's the signal? |
| Owner | Who is responsible for monitoring and responding |
| Status | Open / Monitoring / Mitigated / Closed / Materialised (→ becomes Issue) |
| Date identified | When the risk was first logged |
| Review date | When to next assess this risk |

#### Assumptions

| Field | Content |
|---|---|
| ID | A-[sequential number] |
| Assumption | What is being assumed — state clearly (e.g. "Client will provide holdco structure by week 3") |
| Basis | Why this assumption was made (historical precedent, client commitment, standard practice, DD findings) |
| Impact if wrong | What happens to the matter if this assumption proves incorrect (timeline, budget, scope, quality) |
| Confidence | High / Medium / Low — how confident is the team that this assumption will hold? |
| Validation method | How and when will this assumption be tested or confirmed? |
| Trigger | What signal indicates this assumption has failed? |
| Owner | Who is responsible for monitoring and validating this assumption |
| Status | Untested / Validated / Failed (→ becomes Risk or Issue) / Superseded |
| Date identified | When the assumption was first logged |
| Review date | When to next assess this assumption |

#### Decisions

| Field | Content |
|---|---|
| ID | D-[sequential number] |
| Decision | What was decided — state clearly and unambiguously |
| Decision-maker | Who made or authorised the decision (by name) |
| Date | When the decision was made (extract from email date/meeting date) |
| Rationale | Why this decision was made (extract from context, or note "rationale not stated") |
| Source | Where the decision was recorded (email from X to Y dated Z, meeting notes from Z) |
| Scope impact | Does this expand, reduce, or change the agreed scope? If yes, flag for scope-change-controller |
| Downstream effects | What does this decision affect? Other workstreams, timelines, budgets, team composition |
| Conditions | Any conditions attached ("if X, then we'll do Y") |
| Status | Confirmed / Implied / Pending / Superseded / Reversed. **Confirmed** = explicitly made and acknowledged. **Implied** = appears to have been made but not formally confirmed — needs validation. **Pending** = decision needed but not yet made. **Superseded** = replaced by a later decision. **Reversed** = explicitly overturned. The distinction between Confirmed and Implied is the most important — an implied decision should be flagged for confirmation before the matter proceeds on an assumption. |
| Supersedes | If this reverses or replaces an earlier decision, link to D-[number] |

### Step 4: Write the immediate action summary (this goes FIRST in the output)

The summary is the document's lead. Write it as if the reader will stop here. Each item should include the IRAD log ID (e.g. I-002, R-010), a one or two sentence description of the situation, what's recommended, who should act, and by when. The log ID lets the reader jump to the detail — in docx, hyperlink the ID to the corresponding entry using internal bookmarks; in Excel, hyperlink to the cell.

Frame as recommendations — the LPM surfaces and analyses, the partner or client decides.

**Decisions needing confirmation:** Implied decisions (status: Implied) that should be formally confirmed with the decision-maker before the matter proceeds on an assumption. "This email implies Germany is out of scope, but it wasn't explicitly agreed. Recommend confirming with [person] before treating this as a firm decision."

**Decisions needed but not yet made:** Gaps where a decision is required but nobody has made one. These are NOT logged in the Decisions table (nobody made a call) — they're flagged here as action items. "No escalation strategy exists for the Bristol patent consent. If email chasing fails, what's the fallback? Recommend: formal decision on approach and escalation trigger by [date]."

**Scope signals for scope-change-controller:** Any decision or assumption that changes the agreed scope. "D-004 appears to expand scope to include [X]. If this wasn't in the original engagement, it should be processed through scope change control."

**Assumptions at risk of failure:** Assumptions with Low confidence or where the validation trigger is approaching. "A-003 assumes the client will approve the budget uplift before the steering committee meets. Confidence is Low given the client's track record on cost approvals. If this fails, the ERP rework is unfunded."

**Untested inherited assumptions:** Assumptions carried forward from DD, the pitch, or a prior phase without re-validation. "A-005 assumes the entity structure matches what was presented in DD. The ERP integration has already revealed that Nexus's SAP customisation was not accurately represented in DD — consider whether other DD assumptions need re-testing."

**Risks requiring immediate mitigation:** High-probability, high-impact risks that need action now rather than monitoring.

**Decisions that contradict each other:** Earlier and later decisions that conflict. "D-002 (dated 15 Feb) says Germany is in scope. D-005 (dated 28 Feb) implies Germany is out. Which is current?"

## RAID methodology — the operational knowledge

### Why most RAID logs fail

The log itself is easy. The discipline of maintaining it is hard. Most RAID logs fail not because of bad structure but because:

1. **They're created at matter setup and never updated.** A RAID log that reflects week 1 risks by week 12 is worse than no log — it creates false confidence. The log must be a living document reviewed at every status cycle.

2. **Risks are too vague.** "Regulatory risk" is not a risk. "BaFin may require additional documentation for the holding company restructure, adding 4-6 weeks to the German workstream" is a risk. Vague risks can't be assessed, mitigated, or monitored.

3. **Assumptions are made at setup and never revisited.** Every matter starts with assumptions — about timelines, costs, entity structures, regulatory processes, client decision-making speed. These are written into the budget, the plan, and the scope. Then nobody checks whether they're still valid. When an assumption fails six months in, the team acts surprised, but the assumption was never monitored. The RAID log should track assumptions with the same discipline as risks: what's the assumption, what happens if it's wrong, how will we know it's wrong, and who's watching it?

4. **Decisions aren't logged at all.** This is the biggest failure. Teams make decisions constantly in email and on calls, and nobody writes them down. When the decision is questioned later — by the client, by a new team member, by the partner — nobody can find it. The RAID log is the single source of truth for what was decided, when, by whom, and why.

5. **The distinction between risks and issues is blurred.** A risk is something that might happen. An issue is something that has happened. The response to each is fundamentally different. Risks need mitigation and monitoring. Issues need resolution and escalation.

The transition test: **"Is there still something we can do to prevent this, or are we now managing the consequences?"** If you're preventing, it's a risk. If you're managing consequences, it's an issue. A supplier who hasn't responded to two chasers is still a risk — they might respond tomorrow. A termination clause that has fired with no consent is an issue — the uncertainty is resolved and you're dealing with the outcome.

**Critical rule: silence is a risk, not an issue.** A team not responding, a counterparty going quiet, a regulator not acknowledging a filing — these are all concerning and may warrant urgent escalation, but they are not issues until the uncertainty is resolved. The problem may not exist. Something only becomes an issue when it's confirmed — a formal rejection received, a deadline passed without action, a counterparty explicitly refusing. Do not classify unconfirmed situations as issues regardless of how concerning the silence is. Rate the risk appropriately (silence on something time-critical can be High or Critical) and escalate the chase, but keep it in the Risks section until there's confirmation that the problem is real.

When a risk materialises, it should be formally converted to an issue — the risk entry is marked "Materialised" and a new issue entry is created, linked back to the original risk. This lifecycle tracking is valuable: it shows whether the risk was anticipated, whether the mitigation worked, and whether the contingency plan was adequate.

### Risk identification — what to look for

Risks on legal matters fall into predictable categories. When identifying risks proactively (Mode 3), work through each category systematically:

**Operational risks:** Team availability, key person dependency, jurisdiction complexity, language barriers, timezone conflicts, local counsel responsiveness, technology failures, document management issues, parallel workstream dependencies.

**Commercial risks:** Budget inadequacy, scope creep, fee dispute potential, write-off exposure, client payment terms, local counsel cost overruns, disbursement surprises (translation, notarisation, apostille, regulatory fees).

**Regulatory risks:** Approval timelines, regulatory change during the matter, novel issues without precedent, multi-regulator coordination, filing sequencing dependencies.

**Client risks:** Decision-making speed, internal politics affecting the matter, change of personnel mid-matter, unrealistic expectations, scope disagreements, information provision delays.

**Resource risks:** Staff turnover, leave during critical periods, skill gaps in specific jurisdictions, over-reliance on a single person, training needs for junior team members.

**External risks:** Counterparty behaviour, market conditions affecting timing, political events, force majeure, third-party dependencies (courts, registrars, government agencies).

Not all risks are equal. Focus assessment on risks that are both plausible and consequential. Levy's principle applies: ignore the trivial (someone's sick for a day) and the catastrophic-but-uncontrollable (global pandemic). Focus on the risks in between that you can actually mitigate.

### Risk assessment — probability × impact, but not arithmetic

Probability and impact are each assessed as Low / Medium / High. The combined exposure is a judgment, not a multiplication. Some principles:

- High probability + High impact = Critical. This needs immediate escalation and active mitigation. It's not a risk to monitor — it's a problem to solve.
- High probability + Low impact = Accept and monitor. It'll probably happen but it won't hurt much. Have a contingency plan but don't over-invest in mitigation.
- Low probability + High impact = The dangerous category. Unlikely but devastating if it happens. These are the ones that blindside projects. Ensure contingency plans are in place even if mitigation is light.
- Medium × Medium = The default category. Most risks sit here. The LPM's judgment is in deciding which of these deserve active mitigation versus monitoring.

The assessment should change over time. A risk that was Medium probability at matter setup may become High as the deadline approaches. Review and re-rate at every status cycle.

### Materiality — what warrants a RAID entry

On a large matter (30 jurisdictions, multiple workstreams, 18-month timeline), logging everything produces a RAID log that nobody reads. The log should capture items that could affect the matter at the programme level — its timeline, budget, scope, or quality as a whole. The materiality test:

- **Would this item, if it materialised or went wrong, change the programme's RAG status?** If yes, it's a RAID entry. If it's a jurisdiction-level admin delay that doesn't affect the critical path, it belongs in the workstream tracker, not the programme RAID log.
- **Would a partner or steering committee need to know about this?** If it would feature in a status report escalation, it belongs in the RAID log. If it's operational noise that the team resolves routinely, it doesn't.
- **Could this item affect multiple workstreams?** Cross-cutting risks and assumptions are always material — a failed assumption about DD accuracy can cascade across every workstream.
- **Is this a decision with scope or commercial implications?** Decisions that change what the firm is doing or what the client is paying are always logged. Routine operational decisions are not.

Err on the side of inclusion during matter setup (when you're identifying risks and assumptions proactively) and on the side of discipline during execution (when new items emerge weekly). A RAID log with 20-30 active entries is manageable. A log with 200 entries is a spreadsheet, not a management tool.

### Data storage vs reporting — where the RAID log lives

**The information flow:** Email and correspondence is always the input — that's where new risks, assumptions, issues, and decisions originate on legal matters. The skill processes unstructured input and produces two outputs: (1) the IRAD report (docx) for circulation, and (2) structured RAID log entries for storage. The SharePoint List or Excel workbook is the destination for processed entries, not a source of new information. The only time the skill reads from the stored log is when updating existing entries — checking what's already logged before adding or modifying items.

**Data storage (the log itself):**

The RAID log should live in a **SharePoint List** (preferred) or **Excel workbook** (fallback). These are filterable, sortable, and collaborative — essential for a log that accumulates hundreds of entries over the life of a multi-year matter.

- **SharePoint List:** Single list with a Category column (Issue/Risk/Assumption/Decision) and a Status column. Create saved views: "Active" (Status = Open/Monitoring/In Progress/Untested/At Risk), "Archive" (Status = Closed/Resolved/Superseded), "Critical items" (Exposure = Critical or High), "This period" (Date modified within reporting period). The LPM sees everything. The partner sees a filtered view. No items are deleted — closed items are just a different filter, not a different location.
- **Excel fallback:** Same structure with filtered views or separate Active/Archive tabs. Less collaborative but works when SharePoint isn't available.

**Reporting (the IRAD report):**

The IRAD report (docx) is an export of the active view plus the analytical layer the skill provides: BLUF summary, IRAD counters, commentary, risk assessment, cross-referencing, and recommendations. The report is what circulates to partners and stakeholders. The SharePoint List is what the LPM maintains.

In connected mode (M365), the skill can read the SharePoint List directly, identify what's changed since last report, and produce the IRAD report from the current data. In manual mode, the user exports or describes the current state and the skill produces the report.

**The active report stays tight.** Only live items appear in the circulated report. The SharePoint List holds everything — the report is a filtered, analysed snapshot. A report with 15-30 items is a management tool. A report with 150 items is a data dump that nobody reads. The full history lives in the List, accessible to anyone who needs it but not forced into every reader's attention.

**What stays in the active report with a note:** Items that are technically closed but carry forward lessons or residual risk that affects live items. Example: A-001 (DD accuracy on SAP) is Failed and its immediate consequences are managed, but the lesson — "DD assumptions may be unreliable across this programme" — informs other active assumptions. Mark these as "Closed — lesson active" and include a one-line note referencing the active items they inform. Move to the archive once the related active items are themselves resolved.

Assumptions are the premises the matter is built on. They're embedded in the budget, the timeline, the scope, and the team structure. When they hold, nobody notices them. When they fail, everything downstream breaks.

The Sibelius project is a textbook case: assumptions about client readiness, DD accuracy, entity status, and budget adequacy all failed, and each failure cascaded into cost overruns, timeline slippage, and scope disputes. None were tracked as assumptions. If they had been, the team would have had validation triggers and contingency plans.

**Where assumptions hide on legal matters:**

- **In the budget.** Every budget contains implicit assumptions about complexity, team leverage, local counsel costs, disbursements, and timeline. "We budgeted €200k for Germany" assumes a certain volume of work. When the entity structure turns out to be more complex, the budget assumption has failed — but nobody called it an assumption.
- **In the DD.** Due diligence findings are treated as facts, but they're snapshots. "The DD showed 3 entities" is an assumption that the DD was accurate and complete. The ERP integration on Phoenix proved this assumption wrong.
- **In the timeline.** "BaFin will process in 8 weeks" is an assumption about regulatory behaviour. "The client will make decisions promptly" is an assumption about client behaviour. Both are routinely wrong.
- **In the scope.** The engagement letter defines what's in scope, but it relies on assumptions about what the work will actually involve. "Standard filing in Singapore" assumes the filing is indeed standard. If it turns out to involve a novel classification, the scope assumption has failed.
- **In the team.** "The local team can handle this" assumes competence, capacity, and responsiveness. "The partner will be available for key decisions" assumes availability.

**Assumption lifecycle:**

An assumption starts as **Untested** — the team is relying on it but hasn't verified it. It moves to **Validated** when confirmed true ("client provided the holdco structure on schedule — assumption holds"). It moves to **Failed** when proved wrong, at which point it either generates a new **Risk** (if the impact is still uncertain) or a new **Issue** (if the impact is immediate and known). A failed assumption should be linked to the resulting Risk or Issue entry so the chain of causation is traceable.

The most dangerous assumptions are the ones nobody articulates. "Of course the DD is accurate." "Of course the client will respond promptly." "Of course the regulatory process hasn't changed since last year." Making these explicit — writing them down in the RAID log with a validation method and a failure trigger — is the single highest-value preventive discipline on a legal matter.

### The "D" in RAID — why decisions matter most

On most legal matters, the "D" component is the most neglected and the most valuable. Decisions drive everything — scope, timeline, budget, risk profile. An unrecorded decision is a future dispute.

What counts as a decision worth logging:

- **Scope decisions:** Anything that changes what's in or out of the engagement. Including the apparently minor: "We don't need to do X" is a scope decision that should be recorded in case X becomes relevant later.
- **Structural decisions:** How work will be organised, which entities are involved, which jurisdictions are active, which approach is being taken.
- **Commercial decisions:** Fee arrangements, budget allocations, write-off approvals, OOS fee agreements.
- **Timing decisions:** Deadline changes, phase sequencing, go/no-go decisions at gates.
- **Personnel decisions:** Team changes, role assignments, external counsel appointments.
- **Client instructions:** Anything the client has directed, particularly where it overrides professional advice or standard process.

What is NOT a decision — common misclassifications:

- **Someone doing something is not a decision to do it.** If David is chasing Bristol by email, that's not a RAID log entry of any kind — it's an operational task tracked in the status report or step plan. It only becomes a decision if someone explicitly chose email chasing over other escalation approaches. The absence of a formal decision about approach is a risk worth flagging ("no escalation strategy if chasing fails") and a gap to surface as "decision needed" — but don't log it as if someone made a deliberate call.
- **Routine operational activities** ("let's schedule the call for Tuesday") are not decisions.
- **Observations** ("the ERP integration is more complex than expected") are not decisions — they may indicate a failed assumption (A-entry: "assumed DD accurately reflected SAP customisation") which should be logged.
- **Recommendations** ("I think we should...") are not decisions until someone with authority confirms them.

The test is: "Did someone with authority make a choice between alternatives that affects the matter's direction?" If yes, log it as a decision. If the email reveals a premise being relied upon that hasn't been tested, log it as an assumption. If someone is just doing their job without an explicit choice being made, it belongs in the status report or step plan, not the RAID log.

What doesn't need logging: routine operational decisions ("let's schedule the call for Tuesday"), administrative choices, formatting preferences. The test is: "Would someone need to know this decision was made when reviewing the matter in six months?"

### Risk → Issue escalation

When a risk materialises, the process is:

1. **Update the risk entry:** Change status to "Materialised." Note the date and circumstances.
2. **Create a new issue entry:** Link back to the original risk ID. Assess the actual impact (which may differ from the estimated impact). Assign resolution owner and target date.
3. **Assess mitigation effectiveness:** Did the mitigation reduce the impact? Was the contingency plan adequate? This is learning that feeds back into future risk assessment on this and other matters.
4. **Escalate appropriately:** Apply the same three-tier model as status reporting — team level, matter-lead level, client level. The escalation level depends on the impact, not the existence of the issue.
5. **Produce an escalation brief if needed:** For issues requiring matter-lead or client escalation, produce a brief: what happened, what's the impact, what's being done, what options exist, what decision is recommended, and what the timeline is. Frame as recommendations with consequences — "Recommend [approach] because [reasoning]. If this isn't addressed by [date], the consequence is [impact]."

### LPM vs attorney boundary

This skill operates on the operational side of risk management. It identifies, structures, tracks, and escalates. It does not:

- Assess the legal merits of a regulatory risk (that's attorney work)
- Determine whether a contractual clause creates a risk (attorney work, but the LPM can flag that a clause exists and ask the attorney to assess it)
- Advise on risk appetite (that's a client/partner decision informed by legal advice)
- Make legal judgments about whether a decision was correct

The skill can identify that a decision was made ("client instructed us not to obtain a tax opinion for the German entity"), flag the potential risk ("this creates exposure if the German tax authority challenges the structure"), and log it for the record. But it cannot assess whether the client's instruction was legally sound.

When the skill encounters information that requires legal assessment, it should flag it: "This item requires legal assessment before it can be fully risk-rated. The operational risk (timeline/budget impact) can be assessed now; the legal risk needs attorney input."

## Input processing

### Text inputs

Email chains, meeting notes, call notes, verbal summaries. The same input types as status-report-drafter, but processed differently — the status report extracts progress; this skill extracts decisions, risks, and assumptions.

Watch for decisions buried in:
- Reply chains (mid-thread responses, not the most recent message)
- CC lines (someone was informed of a decision but didn't respond — silence may constitute agreement)
- Forwarded messages with brief annotations ("FYI — I've told them we're not doing this")
- Meeting notes that say "agreed" without specifying who agreed or what exactly was agreed
- Attachments referenced but not included ("as per the attached" — flag that the attachment should be reviewed)

### File inputs

- **Existing RAID log (Excel):** Read the current state, maintain the existing structure and numbering, add new entries and update existing ones. Don't renumber or restructure — the IDs are references used in other documents.
- **Step plan or timeline:** Cross-reference against the risk register. Risks should be assessed against specific milestones rather than in the abstract — "R-001 threatens the 15 March filing deadline" is more actionable than "R-001 could cause delay." Flag decisions that contradict the plan ("D-006 implies a 4-6 week ERP delay, but the step plan shows go-live on 15 April — these are inconsistent"). Identify milestones with no risk coverage — if the plan has 8 milestones but the risk register only covers 3, what about the other 5?
- **Engagement letter or scope document:** Essential context for scope signal detection. With the engagement scope defined, assessments move from inferential ("this might be out of scope") to precise ("the engagement covers X, Y, Z; this decision introduces W, which isn't covered"). Always ask the user whether a scope document is available when assessing scope signals.
- **Budget tracker:** Allows financial risk quantification. Without it, financial risks are estimated from email language ("another £60-80k"). With it, the skill can assess whether financial risks are proportionate to the budget position and flag where risk exposure exceeds remaining contingency.
- **Previous status reports:** May contain risk flags that should be in the RAID log but aren't. Extract and log them. Also useful for identifying risks that were flagged in a prior period but have no corresponding RAID entry — a discipline gap.

### Confirming the full picture

As with status reporting, ask about what's missing. "I've extracted [X] decisions, [Y] risks, and [Z] assumptions from this correspondence. Are there any verbal decisions, unwritten assumptions, or agreements not captured in writing that I should also log?"

## Cross-skill handoff points

- **Scope signals identified** → "This decision appears to change the agreed scope. Use the scope-change-controller skill to assess whether this constitutes an out-of-scope item and process it through change control."
- **Financial risk identified** → "This risk has budget implications. Use the budget-and-fee-manager skill for detailed financial impact assessment."
- **Timeline impact** → "This issue affects the project timeline. Use the timeline-generator skill to recalculate the critical path and identify downstream impacts."
- **Status report integration** → "The RAID log has been updated. The status-report-drafter skill can reference these entries when producing the next status report."
- **Stakeholder notification** → "This issue requires escalation to [level]. Use the stakeholder-comms-planner skill to determine the appropriate communication approach."

## Output format

### Presentation priority — management by exception

**BLUF — Bottom Line Up Front.** Every output from this skill follows the BLUF principle (US military communication doctrine): assume you get the reader for one minute or less, so the most important information goes at the top. The reader who stops after 30 seconds should have the critical items. The reader who continues gets progressively more detail. Nobody should have to scroll to find out what matters.

BLUF adapts to the audience. Internal BLUF is direct about the situation and frames the response as a recommendation: "Two workstreams are Red. Recommend partner-level engagement on the DataCore supplier termination before 22 March." Client-facing BLUF conveys the same information with managed confidence: "Two items require your input this period to maintain the programme timeline." Be direct about facts, recommend on responses — never directive. The LPM surfaces and analyses; the partner or client decides.

**Lead with the headline.** The immediate action summary comes first — before any detail. A stakeholder with 30 seconds gets the critical items. A stakeholder with a few minutes gets the visual summary and scope signals. A stakeholder with 5 minutes reads the full IRAD log.

**Tone: recommend, don't direct.** This is an internal report from an LPM to a partner or senior lawyer. The LPM's authority comes from the quality of the analysis, not from giving instructions. Use "Recommend briefing client today" not "Client must be briefed immediately." Use "Recommend decision on approach by end of business" not "Decision required by end of business." Present options, flag consequences, make clear recommendations — but frame them as recommendations. The partner decides.

**Unified log with change markers.** When updating an existing RAID log with new information, do not split the output into "new entries" and "updated entries" as separate sections. Produce one integrated IRAD log — the full current picture — where each entry is tagged: **[NEW]** for items appearing for the first time, **[UPDATED]** for items whose status, assessment, or content has changed since last review, or unmarked for items that haven't changed. This gives the reader one coherent document to scan, with changes visually highlighted, rather than a fragmented view that requires mental reassembly.

The acronym is RAID but the detail order is **IRAD** — prioritised by what needs attention now:

1. **Issues first** — these are happening. They need resolution, escalation, or both. The partner reading this report needs to see what's on fire before anything else.
2. **Risks second** — these might happen. They need mitigation decisions or monitoring. The second thing the partner needs to know is what could go wrong next.
3. **Assumptions third** — these are being relied upon but may not hold. Failed assumptions are the origin story of most risks and issues. Assumptions with Low confidence or approaching their validation date need active monitoring.
4. **Decisions last** — the record of what was decided. Essential reference material, but not action items unless their status is Implied (needs confirmation) or Pending (needs to be made). Implied and Pending decisions should be called out in the immediate action summary alongside Issues and high-exposure Risks.

### For decision extraction (Mode 2)

Lead with the immediate action summary (with log IDs hyperlinked to detail entries), then scope signals, then full IRAD detail. Format as a structured document that can be copied into an existing RAID log or used to create a new one. If producing a docx, use tables with consistent column widths optimised for the content in each column.

### Format-specific guidance

**Docx report output (the circulated IRAD report):**
- Use internal bookmarks on each log entry ID (I-001, R-001, A-001, D-001). Hyperlink the IDs in the summary section to the corresponding bookmark so the reader can click through to the detail.
- Active items only — no resolved/closed items. These live in the SharePoint List or Excel archive.
- Colour-code severity and exposure fields (Critical/red, High/amber, Medium/yellow, Low/green).
- Use strikethrough for changed values (e.g. ~~Medium~~ → **High**) to show movement.
- Heatmap is optional — include if the matter has enough risks to make clustering visible (roughly 6+). Otherwise the counters are sufficient.

**SharePoint List (the persistent data):**
- Single list with columns for: ID, Category (I/R/A/D), Description, Status, Severity/Exposure, Owner, Dates, and all other fields from the IRAD structures above.
- Saved views: Active, Archive, Critical, This Period, By Workstream, By Owner.
- No items deleted — status changes manage the lifecycle. The full history is always available.

**Excel fallback (when SharePoint isn't available):**
- Active and Archive on separate tabs or use filtered views on a single tab.
- Hyperlink IDs between related entries (e.g. R-002 links to I-001 when a risk materialises).
- Use conditional formatting on severity/exposure columns for colour coding.
- Include a Summary tab that mirrors the immediate action section with hyperlinks to detail rows.
- COUNTIF formulas on the Summary tab for auto-updating IRAD counters.

### For RAID log creation (Mode 1)

Lead with the immediate action summary, then the complete RAID log in IRAD order. Include a "review and maintenance" section reminding the user of the review cadence and update discipline.

### For risk identification (Mode 3)

Lead with the top 3-5 risks requiring immediate attention, then the full risk register by category. If any identified risks are already materialised (i.e. they're actually issues), call those out first. Include assumptions being relied upon that underpin the risk profile.

**Named-firm attribution rule:** Never reference a named firm anywhere in skill output — in documents, tables, or conversational text. This includes attributing rates, policies, practices, or organisational structures to any named law firm. The skill does not know any firm's actual structure, rates, or policies. Use "confirm with Pricing", "confirm with Finance", or "firm policy — confirm before applying." The rule applies to everything this skill produces, not just formal documents.

---

## M365 Connected Mode (Optional)

**Connected mode invocation rule:** Search connected systems (Outlook, SharePoint, Teams) when doing so adds value — not as a default first step when sufficient input is already in the prompt.

- **Sufficient input already provided:** User has pasted emails, documents, or data with full context. Engage with what is there. Do not search first — it adds friction without adding information.
- **Input is incomplete or proactive surfacing is warranted:** User references something that should be retrieved ("there's an invoice in Outlook", "it's end of month"), or connected mode is running in background/scheduled mode. Search proactively — this is the inverted invocation model and is the highest-value connected mode behaviour.

The distinction is whether the user has already provided what is needed. If yes, work with it. If no, or if proactive surfacing serves the LPM, search.

When the M365 MCP connector is enabled (Claude Team/Enterprise), this skill can:
- Search Outlook for matter emails containing decision language ("agreed," "confirmed," "decided," "approved," "instructed")
- Scan recent correspondence for risk signals (escalation language, concern language, deadline pressure)
- Pull the existing RAID log from SharePoint if one is maintained there
- Check Teams messages for informal decisions that may not be in email
- Cross-reference calendar for meeting dates when decisions were likely made

Without the connector, provide the same information by pasting email text, uploading files, or describing the situation directly.
