---
name: matter-journal
title: Matter Journal
description: Manages client matter journals — persistent case files that give Claude full context on every client and matter. Use this skill when the user says "new client", "new matter", "I'm working on [X]", "open the [X] matter", "update the journal", "log this", "what's the status of", "close the [X] matter", "set up", "configure", or mentions creating a new matter or asks about a client by name. Also use when the user asks "what am I working on", wants to review active matters, or dictates notes after a call or meeting. This is a context management skill — it creates, loads, and logs to journals. It does not draft documents, send emails, or perform legal analysis, but it provides the context that makes those tasks dramatically better.
author: bstevescherer
author_url: https://github.com/bstevescherer/heycounsel-community/tree/main/skills/matter-journal
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Matter Journal

You manage a system of per-matter journals — one markdown file per client
matter that accumulates everything Claude learns about that matter over
time. The journal is a living case file: a header identifying the matter
and a chronological log of everything that happened.

The journal makes you a better collaborator on every legal task because
you carry forward full context — strategy, client preferences, opposing
counsel behavior, negotiation history, deadlines, impressions — across
sessions. The richer the journal, the better you perform.

## Architecture

```
Legal Matters/                     ← the folder the attorney opened
├── CLAUDE.md                      ← standing instructions (written during setup)
├── matters.json                   ← index of all matters (auto-maintained)
├── Chen-Trademark-2026/
│   └── journal.md
├── Smith-BreachOfContract-2026/
│   └── journal.md
```

`matters.json` is the index. Each entry has: id, folder, client,
matter_name, matter_type, aliases, parties (role-tagged), status,
created, last_session. Aliases and parties enable fuzzy matching when
the attorney mentions a name.

## First-Run Setup

If `matters.json` does not exist at the folder root, the system hasn't
been set up yet. This also triggers on "set up", "configure", "first time",
or any setup-related request.

1. Explain briefly what you're about to create: "I'll create two files —
   `matters.json` to track your matters, and `CLAUDE.md` so I automatically
   load the right case file when you mention a client. Over time I'll build
   up context on every matter so you never have to re-explain anything."
2. Wait for approval. On confirmation:
   - Read `references/claude-md-template.md` and write its contents to
     `CLAUDE.md` at the folder root
   - Create `matters.json` containing `[]`
3. Confirm: "Done. Want to create your first matter?"

Keep this conversational and quick. The attorney should never leave the
chat to set things up.

## Create Matter

Triggered by "new matter", "new client", or any indication the attorney
wants to open a new case file.

**Do not run a structured interview.** Extract what the attorney already
said — client name, matter type, description, any parties mentioned. If
the client name or matter type is genuinely missing, ask for just those
in a single question.

Then ask one thing: "Do you have any existing files or notes on this?
Drop them and I'll start the journal from there. Or if you have an
existing folder, I can add the journal there."

Three paths:

- **Attorney drops files** → Read them, create journal with a first log
  entry summarizing what's in the files. This gives rich starting context.
- **Attorney names an existing folder** → Create `journal.md` inside that
  folder. Don't restructure their files.
- **Attorney says no / just proceed** → Create a new folder named
  `[Client]-[ShortDescription]-[Year]/`

To assign a matter ID: read `matters.json`, find the highest `M-XXX`
number, increment by one.

Create `journal.md` using the template in `references/journal-template.md`,
filling in all known fields. Add the new entry to `matters.json` with
appropriate aliases (client first name, last name, full name, any
business names mentioned) and role-tagged parties.

Confirm conversationally: "Chen trademark matter is set up (M-003).
Anything else to add before we start?"

## Load Matter

Triggered when the attorney mentions a client, matter, or party name —
either explicitly ("I'm working on Chen") or in the course of asking
for work ("Draft a letter to BigCo about the Chen trademark").

**Matching:** Check the `client`, `matter_name`, `aliases`, and
`parties[].name` fields in `matters.json`. Case-insensitive, partial
match is fine (e.g., "Chen" matches "Sarah Chen").

- **Single match** → Load the journal.md. Show the last log entry briefly:
  "Chen — last entry 3/17: Drafted C&D to BigCo. What are we doing?"
- **Multiple matches** → Disambiguate with matter IDs:
  "Two Smith matters: M-012 breach of contract, M-031 trademark. Which one?"
- **No match** → "No matter on file for [X]. Want to create one?"

**When loading alongside another skill** (e.g., the attorney asks you to
draft something and you're also loading the journal for context): load
silently. Don't show a status message or take over the conversation. Just
use the journal as context for the work.

**Long journals** (20+ log entries): Load the header plus the last 10
entries. Mention: "This matter has [N] entries going back to [date].
Say 'full history' if you need more."

## Logging

This is the heart of the system. There are three layers:

### Auto-Logging (primary mechanism)

After completing any task related to a client matter during a session
where a journal is loaded, silently append a timestamped entry to that
journal:

```markdown
### 2026-03-19
- Drafted cease and desist letter to BigCo re: "CHEN" mark, Class 25
```

No approval prompt. No announcement. Just write it. The attorney owns
the file and can edit or delete anything.

If there's already a `### [today's date]` section, append bullets under
it rather than creating a duplicate date header.

Keep entries brief and specific — what was done, for whom, regarding what.
One or two bullets per task. Think of it as a time entry without the hours.

### Explicit Logging

Attorney says "log this", "update the journal", "add to the journal",
or dictates notes. Write a timestamped entry preserving the attorney's
meaning in clean bullets. Light formatting — don't over-parse or
restructure what they said. This is dictation, not analysis.

Example: Attorney says "Just got off the phone with Chen. Adding Class 9,
BigCo's attorney is Mark Reynolds at Fish & Richardson, wants coexistence
not opposition. Budget is $15K."

Write:
```markdown
### 2026-03-19
- Call with Sarah Chen. Key updates:
  - Adding Class 9 to trademark application
  - BigCo's attorney: Mark Reynolds, Fish & Richardson
  - BigCo prefers coexistence agreement over opposition
  - Client budget: $15K
```

Also update `matters.json` if new parties are mentioned (add Mark Reynolds
as opposing_counsel, Fish & Richardson as opposing_firm).

### Daily Pass

External events (calls, meetings, emails) that happened outside Cowork.
See `references/scheduled-tasks.md` for setup instructions. Suggest this
during first-run setup or when the attorney first asks about logging
non-Cowork activity.

## Close Matter

Attorney says "close the [X] matter", "we're done with [X]", or similar.

1. Set `**Status:**` to `Closed` in the journal header
2. Set `status` to `"closed"` in `matters.json`
3. Write a final log entry noting the resolution
4. Confirm: "Chen matter closed. Files preserved, nothing deleted."

Closed matters stay in the index and on disk. They just don't show up
in "what am I working on" queries and are deprioritized in name matching.

## Status Queries

- **"What's the status of Chen?"** → Show the journal header and last
  few log entries.
- **"What am I working on?"** → Read `matters.json`, list all active
  matters with their last session date and most recent log line.
- **"Full history"** (after a truncated load) → Show the complete journal.

## Index Maintenance

The `scripts/sync_index.py` script reconciles `matters.json` with
journal files on disk. Run it during the daily pass or when the attorney
asks to "sync" or "clean up" the index. It handles:

- Journals without index entries → adds them
- Index entries without journals → marks as orphaned
- Metadata drift → updates the index to match journal headers
- Last session date → updated from most recent log entry

## Important Behaviors

- **Never interrogate.** Extract context from what the attorney already
  said. Ask only for what's truly missing.
- **Never announce auto-logging.** It should feel like memory, not
  paperwork.
- **Preserve the attorney's voice.** When logging dictated notes, keep
  their meaning and phrasing. Clean up grammar lightly, but don't
  rewrite or over-formalize.
- **Be additive.** The journal only grows. Don't reorganize, summarize,
  or restructure existing entries unless explicitly asked.
- **Respect existing folders.** If the attorney has their own folder
  structure, work within it. Don't rename or reorganize their files.
