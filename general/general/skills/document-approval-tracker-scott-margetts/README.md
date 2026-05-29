# document-approval-tracker

**Plugin:** LPM Core Plugin (Skill 14 of 14)
**Part of:** [LPM Skills for Claude](https://github.com/legalopsconsulting/lpm-skills)

---

## What this skill does

Designs and tracks multi-stakeholder document approval workflows — defining review sequences, monitoring document position in the cascade, chasing overdue reviewers, coordinating version control, and mapping cross-jurisdiction document dependencies.

Document approval is the invisible critical path on most legal matters. Partners and clients know what documents need to exist; nobody tracks where they are in the review chain until a deadline appears. This skill is designed to make the cascade visible before the deadline, not after.

---

## Modes

| Mode | When to use |
|---|---|
| **Mode 1 — Cascade design** | Defining who reviews a document and in what sequence, at matter setup |
| **Mode 2 — Position tracking** | A document is in circulation — tracking where it is and how long it's been there |
| **Mode 3 — Overdue chasing** | A reviewer is overdue — produce the chasing email at the correct escalation stage |
| **Mode 4 — Version control** | A reviewer is on the wrong version, or version control has broken down |

---

## Key design principles encoded

**Define the cascade before the first draft, not when it's ready.** The approval sequence must be agreed at matter setup — not improvised when the document is circulated.

**Client-side opacity is the hardest problem.** Ask for the client's internal cascade and a named turnaround before first circulation. "We'll review and revert" is not a commitment.

**Email carries the notification; the matter site carries the document.** Every email attachment creates a version risk. Single source of truth in SharePoint; email for notification only.

**State the deadline. Don't soften it.** "When you get a chance" teaches reviewers that deadlines are flexible. The chasing email states the date, the reason, and stops.

**Flag at 80% of SLA — not at expiry.** A partner who has had a document for 2.5 days against a 3-day SLA needs a flag now.

**Map cross-document dependencies at cascade design.** The Netherlands SPA blocked by the German tax opinion is a dependency that should be visible on day one — not discovered when the first document is ready to circulate.

---

## Outputs

| Mode | Primary output |
|---|---|
| Mode 1 | Approval cascade document — review sequence, client-side cascade, dependencies, gaps checklist |
| Mode 2 | Position tracker table — current holder, days at step, SLA flags, next action |
| Mode 3 | Chasing email at correct escalation stage (produced immediately, no identifier gate) |
| Mode 4 | Version status table + recall email draft + prevention protocol |

## Usage notes (v1)

**Mode 2/3 — forwarded emails:** When pasting a forwarded "FYI" email describing an overdue document situation, prefix it with `[APPROVAL TRACKER]`. Even with the tag, this prompt pattern may produce general advisory output rather than a position tracker and chasing email. For reliable routing, describe the situation directly: *"The NDA has been with [Partner] for 4 days against a 3-day SLA. Draft me a chasing email."*

**Mode 1 — cascade design:** Produces a cascade document, not advisory prose on review sequence. If prose appears instead, restate: *"Produce the approval cascade document for [Document name] on [Matter]."*

---



- **Legal review of documents** — the LPM tracks position in the cascade; the attorney decides whether a step is complete
- **Document drafting or redlining** — this skill coordinates the workflow around documents, not the documents themselves
- **Execution logistics** — wet ink signatures, notarisation, apostille chains — those are handled by execution-and-signing-manager (LPM for M&A Plugin, Skill 19)

---

## Skills this one works with

| Skill | Relationship |
|---|---|
| matter-plan-builder | Document production tasks → cascade design trigger |
| timeline-generator | Critical path identification → accelerated chasing for on-path documents; approval delays → timeline impact |
| local-counsel-manager | LC-delivered documents enter the cascade on receipt |
| stakeholder-comms-planner | Client-side contacts and approval authority → client cascade inputs |
| status-report-drafter | Overdue documents and cascade blockers → risks and issues section |
| continuous-improvement-engine | Version control failures and cascade gaps → lesson capture triggers |

---

## License

Apache 2.0. See [LICENSE](../../LICENSE).
