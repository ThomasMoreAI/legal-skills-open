# Playbook Authoring Contract

A **playbook** is a practice-area extension file (`PLAYBOOK-<name>.md`) that specializes the eight core dimensions in `CORE-DIMENSIONS.md` for a specific domain (PI/tort, commercial litigation, IP infringement, regulatory enforcement, criminal defense, etc.). Playbooks are loaded on demand during the **Diagnose practice area** step in `SKILL.md`.

A playbook must satisfy the contract below. Agents should treat any file not following it as malformed and fall back to core-only behavior.

---

## Required shape

```
# <Practice Area Name> Playbook

---
practice_area: <short slug — must match filename after PLAYBOOK- prefix>
triggers:
  filenames: [<filename substrings that signal this playbook fits>]
  content_signals: [<phrases/doc-types that signal this playbook fits>]
defers_to:
  - <sibling-skill-name>: <when to route to it>
---

## Dimension extensions

### <Core dimension name from CORE-DIMENSIONS.md>
<What this playbook adds to that dimension, if anything>

[Repeat for each dimension the playbook extends. Dimensions not listed are handled by the core only.]

## Queries

### <Core dimension name>
- `"<search query string>"`
- `"<search query string>"`

[Organized by dimension. Each query is a plain-text search phrase, independent of any specific backend's flags or modes.]

## Output sections

### <Section name> — slots into <Core skeleton section>
<Markdown template for the section. Use [brackets] for required fields and (parens) for optional>

[Each output section names the core-skeleton section it attaches to (VI Exposure/remedies, VII Defenses, etc.). Sections may add sub-sections; they may not remove or rename core sections.]

## Quality checklist additions

- [ ] <Item specific to this practice area>
- [ ] <Item specific to this practice area>

## Remedies / exposure methodology

<Short prose. What the typical monetary and non-monetary remedies are, what data are needed to compute each, and what the defensible evidence map looks like. Not a valuation — a methodology.>
```

---

## Rules

1. **Name convention.** Filename is `PLAYBOOK-<slug>.md`. Slug uses lowercase letters and hyphens only. Must match `practice_area` in the frontmatter.
2. **Triggers are unambiguous.** The agent uses `triggers.filenames` and `triggers.content_signals` during **Diagnose practice area**. Keep signals specific to the domain so modules don't spuriously fire.
3. **No core overrides.** A playbook extends; it never renames or replaces the eight core dimensions. A dimension that does not apply is noted "N/A — <reason>" in the output, not deleted.
4. **Backend-agnostic queries.** Queries are plain-text search phrases. Do not include CLI flags, backend method names, or tool-specific syntax. Backends consume the same query string through whatever mode (hybrid, semantic, entity, etc.) fits — see `BACKENDS.md`.
5. **Defer to siblings.** If a narrow document type has a dedicated sibling skill (deposition, medical records, discovery, lien correspondence), list it under `defers_to` and let the router handle delegation. Do not re-implement those summaries inline.
6. **Output sections slot, never float.** Every playbook output section names a core-skeleton section it attaches to. A reader of the final memo should always see the core skeleton; playbook sections are inserts, not replacements.
7. **Quality checklist items are falsifiable.** "Every asserted patent claim has an infringement chart" — yes. "The memo is thorough" — no.
8. **No hallucinated authority.** Statutes, rules, and case citations are marked `[VERIFY]` if the agent has not cross-checked them. This matches the convention in `demand-letter/SKILL.md` and `case-chronology/SKILL.md`.

---

## Minimal example

```markdown
# Regulatory Enforcement Playbook

---
practice_area: regulatory-enforcement
triggers:
  filenames: [CID, subpoena, NOV, NPDES, warning-letter, consent-decree]
  content_signals: [agency action, administrative proceeding, civil penalty, corrective action]
defers_to:
  - discovery-summary: when the corpus contains CID responses or interrogatories
  - lien-resolution-summary: if agency restitution or disgorgement liens appear
---

## Dimension extensions

### Claims & legal theories
The "claim" is the agency's charging instrument; elements are statutory violations. Map each cited violation to (a) the alleged conduct, (b) the statute/regulation, (c) the evidence.

### Exposure / remedies
Civil penalties (statutory minimums/maximums), disgorgement, restitution, debarment, consent-decree obligations, corrective-action plans, monitor-ship costs.

## Queries

### Claims & legal theories
- `"alleged violation section statute regulation"`
- `"civil penalty computation maximum"`

### Exposure / remedies
- `"consent decree corrective action plan"`
- `"debarment suspension exclusion"`

## Output sections

### Charging Instrument Analysis — slots into IV Claims & legal theories
| Allegation | Statute/Reg | Conduct | Evidence |
|---|---|---|---|

### Penalty Exposure — slots into VI Exposure/remedies
<Per-count minimum/maximum with citation; aggregate; credit for self-reporting>

## Quality checklist additions
- [ ] Every allegation mapped to the specific statutory or regulatory citation
- [ ] Penalty math shows per-count minimum, per-count maximum, and aggregation
- [ ] Consent-decree obligations (if any) tracked with deadlines

## Remedies / exposure methodology
<Two-paragraph narrative on how civil penalties accrue, how courts/agencies typically apply mitigation factors, and what documentation the memo must cite to support any range.>
```

An agent authoring a new playbook should check it against this example and against `CORE-DIMENSIONS.md` before asserting it is complete.
