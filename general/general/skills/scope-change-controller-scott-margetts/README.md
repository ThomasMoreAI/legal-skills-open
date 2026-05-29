# scope-change-controller

Scope management across the lifecycle of a legal matter — from baseline capture at matter setup through in-flight change control, out-of-scope identification and documentation, and retrospective at close.

## What this skill does

Scope is the baseline everything else references. Status is progress against scope. Risk is threat to scope delivery. Budget is the price of scope. When scope is unmanaged, every other LPM discipline is working against an unreliable target and the client gets surprised.

The skill operates at two levels scaled to matter complexity:

**Lightweight:** A scope summary, a simple change log, and a standing instruction to flag OOS signals as they arise. Appropriate for straightforward matters where full change control would be disproportionate.

**Full change control:** Formal scope register, structured OOS assessment workflow, change notices with financial and timeline impact, OOS report for write-off or additional fee conversations, and a scope retrospective at close.

**Core design principle:** Don't ask the LPM to create the record — create the record and ask the LPM to confirm it. In manual mode this means the skill produces the draft OOS entry, the draft client communication, and the draft scope register update from the input provided. In M365 connected mode, it detects scope signals in correspondence, drafts the entry with source evidence, and surfaces it for confirmation. The difference between "log this" (15 minutes, doesn't happen) and "I've found this — confirm or dismiss?" (30 seconds, happens).

## Relationship with matter-intake-scoping

These two skills are designed to work in sequence. matter-intake-scoping Mode 2 (quick intake) produces a structured scope summary — inclusions, exclusions, assumptions, constraints, milestones, fee basis — that is the baseline scope-change-controller manages for the life of the matter.

If you are installing scope-change-controller without matter-intake-scoping, the skill will prompt you to establish a scope baseline before change control can begin. You can provide this manually.

## Inputs

- Scope summary from matter-intake-scoping (or a manually defined scope baseline)
- Emails, call notes, correspondence containing scope signals
- Client requests or instructions that may constitute additional work
- WIP or billing data suggesting work outside original parameters

## Outputs

- OOS identification notices (internal)
- Scope change notices (client-facing)
- Scope register (live record of agreed scope and changes)
- OOS log (record of all OOS items identified, assessed, and resolved)
- OOS report (summary for write-off justification or additional fee conversation)
- Scope call agenda (for structured conversation with client about scope changes)
- Scope retrospective (at matter close — what was scoped, what changed, and why)

## Cross-skill handoffs

- **From matter-intake-scoping:** Scope summary is the baseline this skill manages
- **From risk-and-issues-manager:** Scope signals from decision extraction; assumption breaches
- **From status-report-drafter:** Budget variance suggesting a scope issue
- **To budget-and-fee-manager:** Scope change assessed — needs financial impact analysis
- **To timeline-generator:** Scope change affects programme timeline
- **To risk-and-issues-manager:** New scoping assumptions logged as A-entries in RAID log
- **To continuous-improvement-engine:** Retrospective findings feed future scoping calibration
