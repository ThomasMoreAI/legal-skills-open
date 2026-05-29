# Standing Assumptions Register

**Maintained by:** [Firm / Practice Group / LPM team]
**Last reviewed:** [Date]
**Review cadence:** Recommend quarterly, or after any matter where an assumption breach caused material impact

---

## Purpose

A curated register of assumptions by matter type, capturing which assumptions hold consistently, which breach, and with what consequence. Used by matter-intake-scoping to calibrate the assumptions candidate list at the start of each new matter.

This file is maintained by the deploying firm. It is populated over time from two sources:
1. **Deliberate review** — periodic assessment by a senior LPM or practice group head
2. **Continuous-improvement-engine output** — assumption performance data captured at matter close, surfaced here for review and incorporation

The goal is a living record, not a static list. An assumption that was reliable three years ago may not be reliable now. A pattern that appeared on two recent matters should be captured before it appears on a third.

---

## How to use this file

When matter-intake-scoping runs pre-engagement mode, it consults this file for the relevant matter type and uses the performance data to calibrate the assumptions candidate list. The output is not "here are our standard assumptions" — it is "here are our assumptions, calibrated against what we know about how they perform."

When continuous-improvement-engine completes a matter retrospective, it identifies which assumptions held, which breached, and what the impact was. That data should be reviewed and incorporated here at the next review cycle.

**What to do with an assumption that keeps breaching:**
- Make it more precise — vague assumptions breach because they're easy to interpret generously
- Lower the deviation threshold — flag earlier, before the breach becomes costly
- Split it — one assumption may be covering two separate risks
- Promote it to a standing risk — if an assumption is breaching more often than it holds, it's not an assumption, it's a known risk

**What to do with an assumption that consistently holds:**
- Keep it, state it with confidence in proposals
- Note the conditions under which it holds — so you know when those conditions don't apply

---

## Register format

Each entry follows this structure:

```
### [Assumption statement]

Matter type: [Which matter types this applies to]
Category: [Quantitative / Regulatory / Client-side / Counterparty / Data quality / Resource]
Status: [Reliable / Variable / High-failure / Deprecated]

Performance history:
- Held: [X instances]
- Breached: [Y instances]
- Typical breach pattern: [What usually causes it to fail]
- Typical breach impact: [Scope / fee / timeline / relationship consequence]

Conditions: [When this assumption is most likely to hold / fail]
Time-sensitive: [Yes / No — if Yes, verify at each matter setup]
Last updated: [Date] | Source: [Matter retrospective / Review cycle]

Recommended handling: [How to present this in a proposal / what to flag]
```

---

## Matter Type: [Template — replace with actual matter type]

*This section is unpopulated. To begin building the register for this matter type, I'd suggest capturing assumption performance data from the next three to five matters of this type and reviewing at the end of each.*

### [Assumption 1 — placeholder]

Matter type: [Type]
Category: [Category]
Status: [Status]

Performance history:
- Held: —
- Breached: —
- Typical breach pattern: Not yet captured
- Typical breach impact: Not yet captured

Time-sensitive: [Yes / No]
Last updated: [Date — initial entry] | Source: [Source]
Recommended handling: [To be populated after first review cycle]

---

## Deprecated assumptions

Assumptions removed from active use, with the reason. Retained here as a record of what was tried and why it was retired.

| Assumption | Retired | Reason |
|---|---|---|
| [Statement] | [Date] | [Why deprecated — e.g., consistently breached, superseded by more precise version, no longer relevant to matter type] |

---

## Review log

| Date | Reviewer | Changes made | Trigger |
|---|---|---|---|
| [Date] | [Name] | [Summary of changes] | [Quarterly review / matter retrospective / CIE output] |

---

*This file is the property of [Firm]. Content reflects firm-specific operational experience and is not part of the published LPM skills methodology. The structure is provided by the matter-intake-scoping skill; the content is maintained by the firm.*
