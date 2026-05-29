# risk-and-issues-manager

RAID log methodology for legal matters — risks, assumptions, issues, and decisions. Maintains the log, extracts buried decisions and assumptions from correspondence, and identifies operational risks from matter setup.

## What this skill does

Legal matters generate a continuous stream of decisions, commitments, and risk signals — spread across email chains, call notes, and informal communications — that rarely get captured anywhere structured. The result is assumptions that were relied upon but never recorded, decisions that can't be reconstructed when a dispute arises, and risks that were visible in the correspondence six weeks before they became issues.

The skill does two things: it maintains the RAID log as a living document, and it extracts the entries that should be in it but aren't — scanning correspondence for decisions, assumptions, risks, and scope signals that were communicated but never logged.

## Three operating modes

**Mode 1 — RAID log maintenance:** Create, update, and manage the four components of the RAID log. Add new entries, escalate risks to issues, close resolved items, and produce a current-state RAID report.

**Mode 2 — Decision extraction from correspondence:** Paste an email chain, meeting notes, or call notes. The skill scans for decisions, risks, assumptions, issues, and scope signals — including implicit ones — and produces structured entries ready to add to the log. This is the most commonly useful mode: finding the things that should have been logged at the time but weren't.

**Mode 3 — Risk identification from context:** Describe the matter setup and the skill identifies the key operational risks based on matter type, jurisdictions, team structure, timeline, and commercial arrangements. Proactive risk identification at matter setup rather than discovery mid-execution.

## The A in RAID is Assumptions

Assumption tracking is the most consistently underused component of RAID methodology on legal matters. Assumptions are premises being relied upon that may not hold — and on complex cross-border matters, a single failed assumption (regulatory approval timeline, entity structure validity, counterparty capacity) can reprogramme the entire execution plan.

The skill treats assumption tracking as a first-class output, not an afterthought. Assumptions captured here feed matter-intake-scoping's standing-assumptions register at matter close — building the calibration data that makes future scoping more accurate.

## Inputs

- Email chains, call notes, meeting notes (for decision extraction)
- Current RAID log (for maintenance and update)
- Matter setup description (for proactive risk identification)
- Scope summary from matter-intake-scoping (for assumption candidate list)

## Outputs

All outputs produced as .docx by default, with client name, client number, matter name, and matter number in the document header.

- RAID log (full four-component register)
- RAID report (management-by-exception summary — items requiring attention, recently escalated, recently closed)
- Structured entries from decision extraction (ready to add to log)
- Risk identification report (proactive, from matter setup)

## Cross-skill handoffs

- **Scope signal identified** → scope-change-controller to assess whether work is outside agreed scope
- **Financial risk identified** → budget-and-fee-manager for financial impact assessment
- **Timeline impact** → timeline-generator to recalculate critical path and downstream impacts
- **RAID log updated** → status-report-drafter can reference entries in the next status report
- **Stakeholder escalation** → stakeholder-comms-planner for appropriate communication approach
- **Assumption performance at close** → matter-intake-scoping standing-assumptions register for future scoping calibration
