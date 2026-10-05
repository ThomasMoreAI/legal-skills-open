---
name: wiki-legalquants
title: Wiki
description: 'Build, explore, and maintain a lawyer''s personal legal wiki: linked, source-grounded Markdown notes that preserve reusable law and method, never matter facts. Use when the user wants to add trusted knowledge, ask what their wiki says, browse it, or check its health.'
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-plugin-oss/tree/main/plugins/legalquants-litigation/skills/wiki
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
sources:
- title: Automation
  path: references/automation.md
- title: Gate Prompts
  path: references/gate_prompts.md
- title: Getting Started
  path: references/getting-started.md
- title: Note Types
  path: references/note_types.md
- title: Okf Profile
  path: references/okf-profile.md
- title: Positions
  path: references/positions.md
- title: Source Policy
  path: references/source_policy.md
- title: Wiki Schema
  path: references/wiki_schema.md
---

# Wiki

Build a persistent, browsable legal wiki the lawyer owns. The wiki is ordinary
Markdown plus a small `.wiki/` sidecar: readable in any editor and useful
without a particular host, chat, or visual view.

The governing boundary is **record reusable law and method, never the matter**.
Do not store client or party facts, matter names or numbers, or matter-document
titles and paths. Do not treat an unsourced inference as authority.

## Start by finding the wiki

Resolve this skill's helper files relative to the directory containing this
loaded `SKILL.md`: [scripts/wiki.py](scripts/wiki.py) is the entry point and
`references/` contains its guidance. Use the absolute path derived from that
location when invoking a helper, preserving the task's working directory.
Commands below use `wiki.py` as shorthand for that entry point. Do not guess a
repository layout or search for a development checkout. The installed skill
directory contains tools; the user's wiki location comes from the registry
rules below. If local execution is unavailable, use the Markdown workflow.

Read [the wiki layout and registry contract](references/wiki_schema.md) before
changing files.

1. If the user named a wiki, use it.
2. Otherwise use the current folder's wiki manifest, then the registered
   default, then the sole registered wiki.
3. If a registered path is unavailable, say that it needs reconnecting; never
   create a replacement silently.
4. Ask setup questions only when no usable wiki is registered. Set up one
   default wiki unless the user asks for several.

The registry is operational metadata, not legal knowledge and not a playbook
preference. A new chat must read it before asking where the wiki lives.

## The four things a lawyer can do

Use the user's language; these are modes, not a command vocabulary they must
learn.

### Add

Add a trusted public source, an authorised non-matter local source, or a
reusable insight the user expressly wants saved. Read
[the note types](references/note_types.md) and [source policy](references/source_policy.md).

“Save the reusable lessons from this conversation” is an Add request. Use the
current context once to prepare eligible, source-grounded proposals for review.
Save no raw transcript. On a later request, check existing notes and proposals
before adding newly discussed knowledge to avoid duplicates.

- Classify the result as **new**, **update**, **disputed**, **no reusable
  knowledge**, or **matter-specific**.
- Link every load-bearing proposition to its source, pinpoint, and (where
  useful) a short supporting extract.
- Update related notes rather than producing near-duplicates. Do not resolve a
  genuine legal conflict silently; place it in the review queue.
- Return a short receipt: what changed, what was linked, and what needs review.

### Ask

Read the Wiki Home/index and search note titles, tags, source titles, and the
full text for useful synonyms before saying the wiki has no answer.

- Explain whether the response is a source-backed rule, analysis, an
  unverified note, a gap, or a disputed/outdated point.
- Link the underlying note and its safe source reference so the lawyer can
  check it.
- Asking is read-only. Save a new note, answer, or link only when the user
  asks to do so.

For “what am I missing?” or a draft comparison, identify the draft's main
claims, assumptions and decisions. Search the wiki separately for each, using
synonyms and adjacent concepts, then read the matching notes in full. Return
only supported omissions, contrary material, useful connections and conditional
alternatives, each linked to its note and source. Explain why each matters to
the draft. Distinguish a gap in this collection from absence of evidence in the
world. Keep the comparison read-only; the current draft is not wiki content.

Different positions may apply to different circumstances, objectives, dates or
jurisdictions. Explain those conditions before treating them as a conflict.
Reserve disputed status for incompatible guidance under comparable conditions.
Do not manufacture objections or analogies when the collection supplies none.

For stored model wording, follow [Position notes and wording](references/positions.md).
Quote the approved block exactly, including brackets, punctuation and line
breaks; keep explanation outside it. State source and approval status. If no
approved block exists, report the gap rather than composing replacement text.
Approval for storage does not establish suitability for this particular use.

### Browse

For **browse, open, show, or explore the wiki**, deliver an inline reader in
the same turn. Prefer the host's built-in visualization skill when available;
read and follow its current rendering, design and verification instructions.
Use another native artifact capability if needed, or Markdown links/a table
when visual rendering is unavailable. Do not merely offer a reader or return
only a file path. Opening a named note shows that note; **map relationships**
requests a relationship view grounded in the wiki's actual links.

Browse is read-only. Take the short path: resolve the wiki, obtain the eligible
payload once, compose the native reader, verify it, and deliver. When scripts
are available, use the browse helper; otherwise read the eligible Markdown
notes directly. Do not load mutation references or re-read source documents
unless needed to resolve a specific issue. Follow the visualization skill's
verification requirements; launch a separate preview only when those require
it or a concrete layout/runtime uncertainty warrants it. A standalone website
or export is a separate user request.

Build the browser from the **complete eligible wiki by default**. Use
`wiki.py browse --json` without `--topic` or `--note`. Narrow the dataset only
when the user explicitly requests a topic or note; a recent question, search
result, selected example or convenient sample does not define the browse scope.
Include every eligible note and its complete body, related notes and safe source
links. Search, filters and pagination may change what is visible, but must keep
the full eligible dataset accessible. Never silently truncate or summarise
away note content to fit a host's size or context limit; read in batches, or
explain the limit and provide access to the remaining content. Before
delivering, reconcile the reader's note IDs and count against the browse
payload and check that complete bodies and sources remain accessible. State
the scope and included count in the handoff.

The Wiki reader's default interaction includes **text search across note titles
and full bodies**. Add simple topic or note-type filters when the collection
has useful distinctions; omit redundant single-option filters. Start with an
empty search and all notes selected, show matching/total counts when narrowed,
and make returning to all notes straightforward. These are requested reader
capabilities; let the visualization skill choose the smallest fitting layout
and native controls. Do not add dashboards or custom application chrome by
default. A single-note view need not include collection search.

The visual is a view of canonical Markdown, not a second database, and must
not expose hidden matter metadata.

### Check

Check links, source references, duplicate candidates, stale material,
unsupported load-bearing propositions, and open conflicts. Repair only
mechanical defects such as generated indexes or clear broken internal links.
Put judgment calls in the review queue with a reason; do not rewrite a legal
conclusion as a maintenance operation.

## Automation is an optional enhancement

Manual add, ask, browse, and check are the complete normal product. Do not ask
about capture, hooks, matter labels, or automation during ordinary setup.

Automatic retrieval requires Codex lifecycle hooks.

In ChatGPT Work say: "Automation cannot be enabled in ChatGPT Work; use Codex."
In any other host without active lifecycle hooks, say that automation is
unavailable there. Do not offer to enable it or write automation playbook
entries; manual add, ask, browse, and check remain fully available.

Offer automation only after the current task has positively proved that its
lifecycle hooks are active and trusted. Otherwise explain that the hooks must
be trusted and a fresh task started. Automatic retrieval is off by default.
When it is off, do not read or log prompt text.

When the user asks to enable automation, follow
[automation settings](references/automation.md). Offer **Selected projects**
and **All projects** equally, with neither preselected nor recommended. The
feature is **Bring in relevant notes**. Show one compact scope-and-feature
preview and obtain explicit approval before saving. The short notice is: “Wiki
will bring in relevant notes in [chosen scope].” Include “You can change this
or turn it off through Wiki automation settings.”
The scope controls where these hooks run, not which folders to ingest.

If asked about automatic saving, explain: “Wiki saves when you ask it to. You
can save reusable lessons from the current conversation with one request.
Automatic retrieval can bring existing notes into your work.” Ordinary Wiki
use never enables automation.

For a first-use walkthrough or starter prompts, use
[Getting started](references/getting-started.md).

## Finish well

Regenerate the human-browsable Wiki Home after a change. Preserve history and
source references. State what is source-backed, what is analysis, and what
needs human review. If no reusable knowledge was found, say so plainly rather
than manufacturing a note.
