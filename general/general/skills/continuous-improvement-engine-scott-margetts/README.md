# continuous-improvement-engine

**Plugin:** LPM Core Plugin (Skill 12 of 14)
**Part of:** [LPM Skills for Claude](https://github.com/legalopsconsulting/lpm-skills)

---

## What this skill does

Captures, structures, and recycles operational lessons from legal matters — in-flight, at phase gates, and at matter close. Converts what happened into something reusable on the next matter.

The standard lessons-learned process fails because lessons are captured too late (at close, not at the trigger event), formatted for filing rather than reuse, and have no feedback loop back into the templates and standing assumptions that would prevent recurrence. This skill is designed to fix all three: in-flight capture at the moment of maximum vividness, structured output formatted for the next scoping session, and explicit routing to the skills whose templates should be updated.

## Usage notes (v1)

**Mode 1 — pasted event documents:** When pasting a RAID update, scope change notice, billing variance, or LC performance issue directly, prefix it with `[LESSON TRIGGER]` before pasting. This tells the skill to extract the lesson rather than produce the downstream document (RAID update, OOS notice, etc.) that other skills handle.

Example: `[LESSON TRIGGER] R-003 has escalated — Dutch notary requires physical presence at signing, €8k unbudgeted.`

Without the tag, describe the situation in your own words: *"Our Dutch RAID risk R-003 has materialised — notary requires physical presence, €8k unbudgeted. Capture the lesson."*

**Mode 0 sidesteps this entirely.** In Mode 0, the skill does the detection and classification itself across the full weekly batch — no tag needed. Mode 0 is the architectural answer to ambiguous input classification.

---



| Mode | When to use |
|---|---|
| **Mode 1 — In-flight capture** | A trigger event has occurred: scope change, risk materialised, issue resolved, delivery problem, positive signal. Capture now, not at close. |
| **Mode 2 — Mid-matter review** | A phase has completed or a quarterly review point has been reached. |
| **Mode 3 — Matter close retrospective** | The matter is closing. Full retrospective with reuse package for the next matter of this type. |

**Mode 1 is the highest-value mode.** A lesson captured the week a scope change lands is ten times more useful than the same observation made at matter close.

---

## Trigger signals

The skill automatically classifies these inputs:

- Scope change notice or scope-change-controller output → Mode 1
- Risk materialised or RAID update → Mode 1
- Status report containing delay or missed milestone signal → Mode 1
- Phase gate or quarterly review → Mode 2
- Matter close or closing → Mode 3

---

## Key outputs

| Mode | Primary output |
|---|---|
| Mode 1 | Structured lesson entry with root cause, lesson statement, and named reuse target |
| Mode 2 | Mid-matter review with lessons table, patterns identified, and adjustments for next phase |
| Mode 3 | Full close retrospective + **Reuse Package** — a forward-facing briefing for the next LPM who picks up a matter of this type |

The **Reuse Package** (Mode 3) is the highest-value output of the skill. It is the section that gets used. The full retrospective is the record.

---

## Skills this one works with

| Skill | Relationship |
|---|---|
| scope-change-controller | Every OOS event → Mode 1 trigger; retrospective findings → Mode 3 input |
| risk-and-issues-manager | Every materialised risk / resolved issue → Mode 1 trigger; "Closed — lesson active" entries → structured capture |
| status-report-drafter | Delivery signals (delays, RAG deterioration) → Mode 1 trigger |
| local-counsel-manager | LC performance issues and scope disputes → Mode 1 trigger |
| matter-intake-scoping | Reuse packages and updated standing assumptions feed back into next matter scoping |
| risk-and-issues-manager | Pattern lessons → standard risk register update |
| scope-change-controller | Pattern lessons → scope baseline template update |

---

## Design principles applied

- **In-flight capture as the primary workflow** — lessons captured at the trigger event, not reconstructed at close
- **Format for reuse, not filing** — lesson entries formatted for scoping sessions; reuse packages formatted for template libraries
- **Explicit feedback loops** — every lesson routed to a named skill whose template it should update
- **Produce the output** — lesson entry produced immediately from available information; not withheld pending complete inputs
- **Template skeleton** — lesson entry, mid-matter review, and retrospective are structured templates the skill populates

---

## License

Apache 2.0. See [LICENSE](../../LICENSE).
