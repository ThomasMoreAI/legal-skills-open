# Note types — the legal profile

This page is the complete answer to "what exactly may enter this wiki."

The wiki is an **OKF v0.2 bundle** (Open Knowledge Format, an open standard for agent-maintained knowledge corpora: markdown files with YAML frontmatter, readable without tooling, diffable in git, openable in Obsidian). `/wiki` adds a small **legal profile** on top: four note types, six extension keys, and one hard exclusion rule. Extensions of this kind are explicitly allowed by OKF §4.1.

**Legal profile version 1.** The schema below is frozen. Changes since the profile was first drafted are recorded, dated, at the end of this page; anything later goes there too, never as a silent edit.

---

## The four note types

Legal knowledge first, method second, matter never:

| `type` | What it holds | Example |
|---|---|---|
| `Legal Insight` | A worked-out statement of the legal situation, with sources | What Art 28(4) GDPR requires for sub-processor flow-down, distilled from EDPB Guidelines 07/2020 |
| `Checklist` | How a kind of document or task gets checked, step by step | The DPA review checklist |
| `Trap` | What to verify before it hurts | Sub-processor lists that live on a URL and change silently |
| `Position` | A position or argument that held, and what it survived | A liability-cap carve-out that held in negotiation |

For optional practical sections and exact approved model blocks, see
[Position notes and wording](positions.md). Long-form notes are supported.

**`Position` stays local.** Position notes never leave the machine: `positions/` is excluded from every export path, from any map or artifact that could be handed on, and from every shipped fixture. They exist for the lawyer who wrote them and for nobody else.

## What never enters the wiki (the gate)

Parties, client facts, matter details, matter-document titles or paths, and
anything from which a matter could be reconstructed. The gate applies before a
note, history record, index entry, receipt, or visual view is written. Legal
knowledge is law, not client data, so the gate keeps only what travels. See
[source policy](source_policy.md) for the distinction between a public or
authorised local source and matter material.

---

## Frontmatter schema

OKF v0.2 standard fields plus the `/wiki` extension keys:

```yaml
---
# OKF v0.2 standard fields
type: Legal Insight            # one of the four profile types. REQUIRED
title: Sub-processor flow-down under Art 28(4) GDPR
description: One sentence. Used by the index and the retrieval preview; nothing re-summarizes it.
tags: [gdpr, dpa, sub-processors]
generated: { by: wiki/<model>, at: 2026-08-17T10:00:00Z }   # who wrote it, when
verified: { by: human:<id>, at: 2026-08-17T18:00:00Z }         # present once the lawyer confirmed or edited
status: stable                 # draft | stable | disputed | outdated | deprecated
stale_after: 2027-08-17        # legal knowledge ages; expiry queues a re-check
sources:
  - id: edpb-07-2020
    resource: https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-072020
    title: EDPB Guidelines 07/2020 on controller and processor
    author: team:edpb
    last_modified: 2021-07-07
# /wiki legal profile (extension keys, OKF §4.1)
practice_area: privacy         # which practice this belongs to
jurisdiction: EU               # where this statement of law holds
document_kind: dpa             # the document or task kind it attaches to
trigger: reviewing a data processing agreement   # what makes retrieval pull this note
origin: seeded                 # seeded | auto-built | accepted
---
```

### The standard fields, precisely

- **`type`** — REQUIRED on every note; exactly one of the four values above. A note with any other `type` is not a profile note.
- **`title`** — the note's human name; the index and every link use it.
- **`description`** — **one sentence** (OKF §4.1). The index quotes it and the retrieval preview shows it; nothing re-summarizes it, so it has to stand alone.
- **`tags`** — a flat list of scalars. Values are snapped to the wiki's canonical vocabulary on write, so "data protection" and "privacy" do not become two shelves.
- **`generated: { by, at }`** — who wrote the note and when. Every note carries it, including notes a lawyer typed, so the record is complete.
- **`verified: { by, at }`** — present once a human has confirmed or edited the note. **Set only by an explicit accept or verify act** — accepting a suggestion, or verifying a named note. It is **never inferred from disk edits**: an editor, a sync tool, or a bulk find-and-replace rewriting a file must not promote a machine-written note to human-reviewed. Drift is reported instead ("N notes changed on disk since last review, unreviewed"), so you see it rather than being credited with it. More than one verification may be recorded as a list (OKF §11).
- **`status`** — OKF's `draft | stable | deprecated`, plus the legal-profile
  review states `disputed | outdated`. **Absent means `stable`.** Disputed and
  outdated notes remain visible with an explicit warning but are never used by
  automatic retrieval. Deprecated notes keep their links working but are
  excluded from retrieval; nothing is destroyed merely to retire it.
- **`stale_after`** — a `YYYY-MM-DD` date (OKF §5.5). A note is **stale when today is on or after that date** — `stale_after == today` is stale, not "still good until midnight". Expiry queues a re-check rather than silently serving old law.
- **`sources`** — a list of records, each with `id`, `resource`, `title`, and optionally `author` and `last_modified` (OKF §5.2). A `resource` is a public URL or an authorised non-matter local path, never a matter path. Where the body makes a sourced claim it carries a **footnote key matching the source `id`**, so citation is per claim, not per note. See [source policy](source_policy.md).

### Extension keys — required by type

| Key | Required |
|---|---|
| `practice_area` | required on every note |
| `jurisdiction` | required on Legal Insight |
| `document_kind` | required on Checklist and Trap |
| `trigger` | required on Checklist and Trap |
| `origin` | required on every note, one of `seeded` \| `auto-built` \| `accepted` |
| `pending` | optional, allowed only together with `status: draft` |

Stated in one line: **`practice_area` — required on every note; `jurisdiction` — required on Legal Insight; `document_kind` and `trigger` — required on Checklist and Trap; `origin` — required on every note, one of `seeded | auto-built | accepted`; `pending` — optional, allowed only together with `status: draft`.**

A key that is not *required* on a type is still permitted wherever it applies — a Trap that only holds in one jurisdiction should say so. The conformance check enforces the required set and the allowed values; it does not forbid the rest.

### Trust tiers are derived, never stored

There is no `tier` key and there never will be one (OKF §5.3). The tier is read off the two provenance fields at the moment you look:

- no `verified` key ⇒ **unverified**
- `verified` by a non-human actor ⇒ **machine-confirmed**
- any `verified` entry naming `human:<id>` ⇒ **human-reviewed**

Because it is derived, it cannot drift out of step with the record, and it cannot be granted by editing a field. Every place a note is shown with a label — the index, a preview, a retrieval line — computes the label the same way from the same two fields.

---

## Dated amendments to the admitted schema (2026-08-19)

1. **Link form.** Body links are **document-relative markdown links** (`../traps/silent-subprocessor-lists.md`), never `/`-rooted. A leading slash resolves against the filesystem root or the site root, not the bundle: it breaks in editors, in Obsidian, and in web rendering of the wiki. The conformance check lints the form.
2. **Path resolution rule.** Frontmatter paths resolve **from the bundle root**; body links resolve **from the note's own directory**. The standard leaves this ambiguous; every sample bundle behaves this way, and this profile now says so out loud.
3. **`origin` key added** — values `seeded | auto-built | accepted`, required on every note. It carries the per-entry provenance line ("where did this come from") and it is the axis the quality metrics measure: how many machine-written notes survive contact with the lawyer.
4. **`pending` key added** — optional, only ever together with `status: draft`. It marks a note that markup mode has proposed but nobody has accepted. Pending notes are excluded from index counts and from any retrieval eligibility; they are visible in the wiki as drafts and nothing else.
5. **Review states added** — `disputed` and `outdated` are legal-profile status
   extensions. Manual Ask may show them only with a visible warning; automatic
   retrieval excludes them.

Amendments 3 and 4 are **additive extension keys under OKF §4.1**. Amendment 5
is a legal-profile vocabulary extension. A reader that knows nothing of this
profile still reads the notes; the four legal keys admitted with the data model
are untouched.

---

## Worked example

A Legal Insight as it lands from a DPA review, with the sub-processor trap linked:

```markdown
---
type: Legal Insight
title: Sub-processor flow-down under Art 28(4) GDPR
description: The same data-protection obligations must flow down to every sub-processor; general authorisation needs a real objection mechanism.
tags: [gdpr, dpa, sub-processors]
generated: { by: wiki/<model>, at: 2026-08-17T10:00:00Z }
status: stable
stale_after: 2027-08-17
sources:
  - id: edpb-07-2020
    resource: https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-072020
    title: EDPB Guidelines 07/2020 on controller and processor
    author: team:edpb
    last_modified: 2021-07-07
practice_area: privacy
jurisdiction: EU
document_kind: dpa
trigger: reviewing a data processing agreement
origin: seeded
---

Where a processor engages another processor, Art 28(4) GDPR requires the
same data-protection obligations to be imposed on that sub-processor by
contract.[^edpb-07-2020] Under a general written authorisation the
controller must be informed of intended changes and keep a genuine
opportunity to object.

What was checked last time: the flow-down clause, the notification
period for sub-processor changes, and whether the sub-processor list is
frozen in an annex or lives on a URL
(see [the trap](../traps/silent-subprocessor-lists.md)).

[^edpb-07-2020]: EDPB Guidelines 07/2020
```

Nothing in that note says which client, which counterparty, or which deal. That is the gate working, not the example being coy: the next DPA review starts with this note and the checklist that links it, and it is useful precisely because the matter has been taken out of it.

The index (OKF §8) and the log (OKF §9) are generated from notes like this one; the bundle root declares `okf_version: "0.2"` (OKF §12).

---

## Note filenames

Note paths follow the OKF path grammar (§11). Each path segment — every directory name and the filename itself — must match:

```
[A-Za-z0-9_][A-Za-z0-9_.\-]*
```

That is: start with a letter, digit, or underscore; continue with letters, digits, underscores, dots, or hyphens. No spaces, no leading dot, no leading hyphen.

Additionally, and beyond the standard: **never** `:` `*` `?` `"` `<` `>` `|` in any segment. Those characters are legal on some filesystems and fatal on others; a wiki is meant to be copied between machines, synced, and zipped without losing files on arrival.

House convention inside those rules: lowercase, hyphen-separated, named for the concept rather than the matter — `art28-flow-down.md`, `dpa-review.md`, `silent-subprocessor-lists.md`.
