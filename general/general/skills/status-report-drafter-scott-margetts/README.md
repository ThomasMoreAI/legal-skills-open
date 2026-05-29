# status-report-drafter

Transforms emails, call notes, and workstream updates into structured matter status reports — with RAG ratings, variance commentary, and escalation flags. Internal and client-facing formats.

## What this skill does

Status reporting on legal matters fails in two predictable ways: it either doesn't happen at all, or it produces reports that describe activity without conveying situation. "The team has been progressing the disclosure workstream" tells the reader nothing useful. Good status reporting applies management-by-exception logic — lead with what needs attention, compress what's on track, flag what needs a decision.

The skill takes whatever you have — an email chain, call notes, a rough update from a workstream lead — and produces a structured report in the appropriate format for the intended audience.

**Output follows the BLUF principle (Bottom Line Up Front):** the reader who stops after 30 seconds has the critical items. The reader who continues gets progressively more detail. Nobody should have to scroll to find out what matters.

## Three report formats

**Internal report:** Direct about the situation, frames the response as a recommendation. Written for partners and senior stakeholders who need to know what to act on.

**Client-facing report:** Conveys the same factual information with managed confidence. Professionally direct about facts; measured about responses. Does not use internal framing.

**Ad hoc update:** A shorter format for Slack, Teams, or quick email updates — current position, one-line workstream status, open items.

## Inputs

- Emails from workstream leads or counter-party
- Call or meeting notes
- Previous status report (to identify what has changed)
- WIP or billing data (for financial position)
- Any other correspondence or updates describing matter progress

The skill works with whatever is provided and flags where key information is absent.

## Outputs

All outputs produced as .docx by default, with client name, client number, matter name, and matter number in the document header.

- Internal status report (RAG by workstream, variance commentary, escalation flags, decisions required)
- Client-facing status report (same structure, audience-appropriate framing)
- Ad hoc update (short-form for messaging or email)

## Cross-skill handoffs

- **Scope concern identified** → scope-change-controller to assess whether work is outside agreed scope
- **Risk or decision extracted from correspondence** → risk-and-issues-manager to log in the RAID log
- **Financial variance suggesting scope issue** → budget-and-fee-manager for financial analysis; scope-change-controller for OOS assessment
- **Timeline impact identified** → timeline-generator to recalculate dependencies and programme impact
- **Stakeholder notification needed** → stakeholder-comms-planner for communication approach and timing
