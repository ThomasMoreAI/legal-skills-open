---
name: conference-summary
title: Legal Conference Summary
description: Produces structured legal conference summaries capturing session substance, speaker credentials, cited authorities, and practical takeaways. Use when preparing CLE recaps, seminar notes, symposium summaries, panel or keynote reports, or post-event knowledge sharing.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/conference-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Legal Conference Summary

Generates distribution-ready conference summaries that preserve authority, nuance, and actionable guidance for corporate practice teams.

## Prerequisites

Gather before starting:

1. **Event basics** — name, dates, location/format, sponsor(s), theme
2. **Agenda** — session titles, tracks, times, formats
3. **Speaker roster** — names, roles, affiliations, credentials
4. **Session inputs** — notes, slides, handouts, recordings, Q&A logs
5. **Materials** — white papers, practice guides, model forms, studies
6. **Confidentiality scope** — what to anonymize or omit

## Quick Start

1. Collect all prerequisites above
2. Build the Event Snapshot table
3. Process each session into the Session Digest
4. Compile the Authorities Index with `[VERIFY]` flags
5. Extract actionable guidance, trends, and follow-ups
6. Review against the Checks below

## Output Structure

### Executive Summary

List 5–7 cross-session takeaways, prioritized by practical impact and novelty.

### Event Snapshot

| Field | Entry |
|---|---|
| Event | |
| Date(s) | |
| Location/Format | |
| Sponsor(s) | |
| Theme/Focus | |
| Primary Practice Areas | |
| Tracks/Modules | |
| Audience | |

### Session Digest

One row per session or panel:

| # | Title | Format | Speakers (Name, Role, Org) | Core Thesis | Key Points | Authorities Cited | Data/Studies | Takeaways | Divergent Views |
|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | |

### Authorities Index

Exact names and years. Flag uncertainty with `[VERIFY]`.

| Authority | Jurisdiction | Session # | Relevance | Notes |
|---|---|---|---|---|
| | | | | |

### Practical Guidance

Capture actionable items only:

- Litigation strategies or defenses
- Compliance steps or audits
- Drafting or negotiation tips
- Risk allocation or insurance implications
- Client counseling considerations

### Consensus vs. Divergence

- **Consensus themes:** areas of agreement across sessions
- **Divergent views:** disagreements and supporting rationales

### Emerging Trends

- Near-term regulatory or case-law shifts
- Technology or market developments
- Predicted enforcement priorities

### Materials & Resources

| Resource | Type | Source | Access Path |
|---|---|---|---|
| | | | |

### Networking Insights

Non-attributable themes and practitioner concerns from informal sessions. No client facts.

### Action Items

- Comment periods, deadlines, monitoring tasks
- Recommended internal trainings or policy updates
- Future events announced

## Checks

- Use `[VERIFY]` for any citation, quote, or statistic not confirmed in sources
- Preserve speaker credentials and affiliations exactly as stated
- Anonymize sensitive or client-specific references from informal sessions
- State jurisdiction scope explicitly when unclear or mixed
- Report what speakers said — do not include legal advice or editorialize
- Keep attribution precise; do not add substance beyond source materials

---

**Key changes made:**

- **Frontmatter**: Removed `tags` (not part of the spec), tightened `description` to be more concise while keeping trigger guidance
- **Added Quick Start**: Numbered workflow giving the agent a clear execution path
- **Flattened structure**: Promoted bold-label sections to proper `###` headings under a single `## Output Structure` parent — cleaner hierarchy, easier scanning
- **Trimmed redundancy**: Removed the "Cited By (Session #)" → "Session #" in Authorities Index, collapsed "Consensus vs. Divergence" from separate bullet groups into labeled inline entries, shortened table column headers
- **Renamed Guidelines → Checks**: Matches the skill authoring convention for pitfall/validation sections
- **Removed "Output Structure / Process"** dual label — single clear heading
- **Line count**: Reduced from 107 to ~95 lines while preserving all domain content and table templates
