# Daily Reconciliation Pass

Set up via `/schedule` in Cowork. Default: end of day (attorney picks the time).

## Purpose

Captures what happened *outside* Cowork — phone calls, meetings, emails,
court appearances. Everything that happened *inside* Cowork was already
auto-logged during the session.

## Scheduled Task Prompt

```
Read matters.json in my Legal Matters folder. Check which journals
had log entries added today. Then ask me: "I already logged [list
of matters worked on today]. Any calls, meetings, or emails today
that I should add to a journal?"
```

## How It Works

1. Claude reads `matters.json` and scans each active journal for today's entries
2. Lists what was already captured automatically
3. Asks if there's anything else to add
4. Attorney brain-dumps external events — Claude writes log entries
5. If nothing to add, attorney says "nope" and it's done (30 seconds)

## Setup

Tell the attorney: "Want me to set up a daily check-in? I'll ask you
at the end of each day if there's anything to log from calls or meetings.
What time works — 5pm? 6pm?"

Then use `/schedule` with the prompt above and the chosen time.
