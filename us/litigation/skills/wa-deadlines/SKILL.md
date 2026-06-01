---
name: wa-deadlines
title: Washington Case Deadlines
description: Use this skill whenever the user asks about timing or deadlines in a Washington civil case. Triggers include "when is my answer due", "when is the response brief due", "compute the deadline", "how many court days", "what's the reply deadline", "I was served — when do I have to answer", "when does my discovery response have to go out", "how long do I have to file a motion to vacate", "exemption claim deadline", "FDCPA statute of limitations", "is this deadline past". Computes court-day and calendar-day deadlines under CR 6 / CRLJ 6 using RCW 1.16.050 holidays (with Saturday→Friday / Sunday→Monday observed-day rule), and covers garnishment timing under RCW 6.27, post-judgment motion deadlines under CR 59 / CR 60 / RAP 5.2, and WA statutes of limitation at RCW 4.16. Deterministic date arithmetic is delegated to `scripts/case-calendar.py`, which is the **canonical source** for current day counts and holidays — this skill does NOT enumerate them. The substantive rules + RCW text
  live in `wa-law-references/references/court-rules/` and `wa-law-references/references/wa-rcw-debt/`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-deadlines
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Washington Case Deadlines

Compute and track deadlines for Washington civil cases. The agent
should invoke this skill automatically when the user asks a timing
question, without requiring an explicit command.

> **NOT LEGAL ADVICE.** Court-rule day counts and statute-of-
> limitation periods are amended by court rule or by the
> Legislature; the **canonical source** for current values is
> `scripts/case-calendar.py` (encoded named rules) plus
> `wa-law-references/references/court-rules/` (full rule text)
> plus `wa-law-references/references/wa-rcw-debt/` (statute text).
> This skill describes the workflow; it does not embed the
> specific day counts.

## How to answer a deadline question

1. **Identify the triggering event.** What happened? (e.g., "I was
   served on April 1", "the judge signed the order on March 15",
   "the garnishment writ was mailed yesterday").

2. **Identify the rule.** Name the controlling rule (CR 12(a),
   CRLJ 6(d), RCW 6.27, etc.) so the user knows what governs. If
   uncertain, read the rule text in
   `wa-law-references/references/court-rules/`.

3. **Compute the date** using the Python helper. The script
   encodes the current WA-state-holiday list (RCW 1.16.050 with
   the Saturday→Friday / Sunday→Monday observed-day shift) plus
   a catalog of named WA rules:

   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/scripts/case-calendar.py" \
     --from 2026-06-03 \
     --days -3 \
     --mode court
   ```

   Flags:
   - `--from YYYY-MM-DD` — triggering date
   - `--days N` — offset (negative = before; positive = after)
   - `--mode court|calendar` — court-day counting (skips weekends
     + WA state holidays) or calendar-day counting
   - `--rules` — list the named rules the script knows about
     (use this to discover the current day count for a specific
     rule rather than relying on memory)

4. **Report clearly.** Give the date, the day of the week, whether
   any intervening holiday pushed the count, and the rule
   citation.

## Optional — maintain a per-case calendar

If the user wants a tracked calendar for the case, store it at
`[case-folder]/CASE_CALENDAR.md` with this shape:

```markdown
# Case Calendar — [Case Name], Cause No. [number]

Court: [court]
Judge: [if known]
Defendant: [pro se]

## Events
- 2025-01-15: Summons served on Defendant
- 2025-02-14: Answer due (CR 12(a))
- 2025-03-01: First Discovery Request served
- 2025-03-31: Discovery responses due (CR 33/34)

## Completed
- [x] 2025-02-14: Answer filed

## Notes
[running notes]
```

When the user adds a new event, append to `## Events`, compute any
derived deadlines via the helper, and add those too.

## Court-day vs. calendar-day counting

- **Calendar days** — every day, including weekends and holidays
- **Court days** — excludes Saturdays, Sundays, and WA state legal
  holidays
- **CR 6(a)** governs which mode applies; periods of fewer than
  7 days typically count court days, longer periods typically
  count calendar days, but there are rule-specific exceptions.
  For the controlling text, see
  `wa-law-references/references/court-rules/CR.md` (CR 6).

## Categories of named WA deadlines (chapter pointers)

Rather than enumerating specific day counts (which drift), this
skill points at the rule sets that govern each category. The
helper script encodes the current values; the rule text lives in
the corpus.

| Category | Authority | Reference file |
|---|---|---|
| Pleading / answer deadlines | CR 12, CRLJ 12 | `court-rules/CR.md`, `CRLJ.md` |
| Reply to counterclaim | CR 12(a)(3) | `court-rules/CR.md` |
| Discovery responses | CR 33, 34, 36 | `court-rules/CR.md` |
| Motion practice (superior) | CR 6(d), CR 56(c) | `court-rules/CR.md` |
| Motion practice (district) | CRLJ 6(d) | `court-rules/CRLJ.md` |
| Reconsideration | CR 59 | `court-rules/CR.md` |
| Vacate judgment | CR 60 | `court-rules/CR.md` |
| Notice of appeal | RAP 5.2 | `court-rules/RAP.md` |
| Notice of appeal (district→superior) | RALJ 2.5 | `court-rules/RALJ.md` |
| Mail-service add-on | CR 6(e) | `court-rules/CR.md` |
| Exemption Claim Form | RCW 6.27 | `wa-rcw-debt/RCW-6_27.md` |
| Garnishment timing | RCW 6.27 | `wa-rcw-debt/RCW-6_27.md` |
| Satisfaction of judgment | RCW 4.56 | `wa-rcw-debt/RCW-4_56.md` |
| FDCPA SOL | 15 U.S.C. § 1692k(d) | `federal-debt-laws/FDCPA.md` |
| WA statutes of limitation | RCW 4.16 | `wa-rcw-debt/RCW-4_16.md` |

For the current day count on any specific rule, run
`python3 .../case-calendar.py --rules` (lists encoded named rules
with their current values) or read the relevant reference file.

## Common triggering events — workflow

When the user reports one of these, run the helper to derive the
specific deadlines:

- **"I was served with a summons"** → answer deadline (CR 12(a);
  check WA-resident vs. non-resident)
- **"I got a writ of garnishment"** → exemption claim deadline
  (RCW 6.27 — check the longer of mailing-vs-service variant)
- **"The judge ruled against me"** → reconsideration (CR 59) +
  appeal (RAP 5.2) deadlines
- **"Plaintiff served discovery"** → response due (CR 33/34/36;
  apply CR 6(e) if served by mail)
- **"I filed a motion to compel"** → opposing response + reply
  (CR 6(d) — different in superior vs. district court)
- **"The creditor sent me a validation notice"** → FDCPA dispute
  window (15 U.S.C. § 1692g)
- **"I'm being sued on an old debt"** → check the applicable WA
  SOL at RCW 4.16 against the date-of-default

## Washington legal holidays

The helper script observes the current RCW 1.16.050 holiday list
with the Saturday→Friday / Sunday→Monday observed-day shift.

**Federal court divergence**: federal courts do NOT observe every
WA-state holiday — check the local federal court calendar rather
than the WA-state list if the matter is federal.

**Local closures**: each court / chambers may declare additional
closures (inclement weather, administrative days). The helper
script does not know about these — check the court's website for
anything near a declared closure.

For the current legal-holiday list and the observed-day-shift
rule, see `wa-law-references/references/wa-rcw-debt/` or the
`case-calendar.py --rules` output.

## Output format (example)

```
Case: Velocity Investments LLC v. Doe
Today: 2026-04-23

UPCOMING DEADLINES:

🔴 Overdue:
   (none)

🟡 Within 7 days:
   - 2026-04-28 (5 days): Response to Motion to Compel — CRLJ 6(d)

🟢 Later:
   - 2026-05-29 (36 days): Reply brief — CR 6(d)
   - 2026-06-03 (41 days): Hearing on Motion to Compel
```

## Notes

- **Extensions** — CR 6(b) allows extensions for cause;
  stipulations of counsel are common. Update the calendar when
  granted.
- **Mail service adds time** per CR 6(e) — apply when the method
  of service is by mail. For the current add-on day count, see
  `court-rules/CR.md`.
- **Do not rely solely on this skill** — verify each deadline
  against the current rule text and the court's calendar for
  holidays and adjustments.
