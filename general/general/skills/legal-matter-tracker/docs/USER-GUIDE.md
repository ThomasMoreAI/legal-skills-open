# Legal Matter Tracker — User Guide

Practical scenarios for getting the most out of Legal Matter Tracker.

---

## Quick Start

1. Say: "Case timeline for [client or case name]"
2. The skill scans your workspace for matching files and builds a chronological timeline
3. Say "save" to export the report to `output/matter-timeline-[client]-YYYY-MM-DD.md`

---

## Situations

### Situation 1: Preparing for a client meeting

**Context:** You have a client call in 20 minutes. Your notes are scattered across several files — meeting notes, email summaries, and a contracts folder.

**What to do:**
1. Open your Cowork session with the project folder selected
2. Say: "Case timeline for Acme Corp"
3. The skill scans all matching files and returns a single chronological view of every significant event

**Expected result:** A timeline with dated entries from all matched files — contract dates, key decisions, open items — so you walk into the call with full context.

**Tip:** Name your note files after clients (`acme-notes.md`, `acme-meeting-2025-01.md`) — the skill matches by filename first, which is faster and more precise.

---

### Situation 2: Reconstructing a case history after a gap

**Context:** You returned from leave and need to catch up on a matter that progressed while you were away.

**What to do:**
1. Say: "Client history for Smith dispute"
2. The skill scans your workspace and returns all events it can find, sorted by date

**Expected result:** A full chronological view of what happened, with source references so you can open specific files for detail.

**Tip:** If the timeline is missing events you know exist, check that those files contain the client name in a heading or in the first 10 lines — the skill uses this to match content.

---

### Situation 3: Generating a status update for a client

**Context:** A client asked for a progress summary. You want to generate a timeline to use as the basis for a report.

**What to do:**
1. Say: "Matter report for Project Alpha — save"
2. The skill builds the timeline and immediately saves it to `output/matter-timeline-project-alpha-YYYY-MM-DD.md`
3. Open the file, clean up the language, and send to the client

**Expected result:** A structured report ready to be edited — sorted events, key facts summary, and source references you can strip before sending.

---

### Situation 4: Searching within a specific folder

**Context:** You have multiple clients with similar names, or you want to limit the search to a specific project folder.

**What to do:**
1. Say: "Case timeline for Alpha in `cases/alpha/`"
2. The skill scans only the specified folder

**Expected result:** A scoped timeline with a note in the header confirming the scan was limited to `cases/alpha/`.

---

### Situation 5: Conflicting information across files

**Context:** Two files contain different versions of the same fact (e.g., different contract amounts).

**What to do:**
1. Run the standard case timeline command
2. The skill flags the conflict in the timeline with a `⚠ Conflict` marker

**Expected result:** Both versions appear side by side in the timeline with their respective source references, so you can identify which file is authoritative.

---

## Tips

- **Name files after clients or cases:** `acme-corp.md`, `smith-ip-dispute.md` — the skill matches by filename first.
- **Use headings to structure notes:** Start files with `# Client Name` or `## Project Alpha` — the skill reads headings to confirm relevance.
- **Record dates explicitly:** Include dates in your notes (`2025-03-10:`, `March 10, 2025`) — the skill extracts these for chronological sorting.
- **Add action items inline:** Lines with `- [ ]` or `TODO:` or `?` are extracted as open items and surfaced in the Key Facts Summary.
- **Save every report:** Use the "save" command consistently — reports accumulate over time and give you version history of the matter's timeline.
- **Multiple matters at once:** Run the skill separately for each client/case — each run produces one focused timeline.
