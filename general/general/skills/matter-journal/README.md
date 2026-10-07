# Matter Journal

A [Claude Code skill](https://docs.anthropic.com/en/docs/claude-code) that gives solo attorneys persistent, per-matter case files. Every client matter gets a `journal.md` that accumulates context across sessions — strategy, client preferences, opposing counsel behavior, negotiation history, deadlines, impressions — so you never have to re-explain anything.

## What it does

- **Creates matter journals** when you say "new client" or "new matter" — no structured interview, just extracts what you already said
- **Loads context automatically** when you mention a client or party name, so every task is informed by the full history
- **Auto-logs silently** after every task — drafting a letter, reviewing a contract, anything — appending a timestamped entry without interrupting your workflow
- **Accepts dictation** ("log this: just got off the phone with Chen...") and writes clean journal entries preserving your voice
- **Tracks all active matters** via `matters.json` — ask "what am I working on?" for a full status view
- **Daily reconciliation** captures calls, meetings, and emails that happened outside Claude

## File structure

```
Legal Matters/
├── CLAUDE.md              ← standing instructions (auto-generated during setup)
├── matters.json           ← index of all matters
├── Chen-Trademark-2026/
│   └── journal.md
├── Smith-BreachOfContract-2026/
│   └── journal.md
```

## Installation

Install the packaged skill:

```
claude install-skill matter-journal.skill
```

Or install from source:

```
claude install-skill ./matter-journal
```

Then open your legal matters folder in Claude Code and say **"set up matter journal"**. It creates `matters.json` and `CLAUDE.md` — you're ready to go.

## Usage

| You say | What happens |
|---|---|
| "New matter — Sarah Chen, trademark application" | Creates folder, journal, and index entry |
| "I'm working on Chen" | Loads the Chen journal as session context |
| "Draft a C&D to BigCo" (with journal loaded) | Drafts the letter informed by full matter history, then auto-logs it |
| "Log this: call with Chen, adding Class 9, budget is $15K" | Writes a timestamped journal entry |
| "What am I working on?" | Lists all active matters with last activity |
| "Close the Chen matter" | Marks it closed, writes a final log entry |

## Index sync

The `scripts/sync_index.py` script reconciles `matters.json` with journal files on disk — adding new journals, flagging orphaned entries, and updating metadata drift.

```
python scripts/sync_index.py /path/to/legal-matters-folder
```

## Skill contents

```
matter-journal/
├── SKILL.md             ← skill definition and behavior spec
├── reference/           ← journal template, CLAUDE.md template, scheduled task config
└── scripts/             ← sync_index.py
```

## License

MIT
