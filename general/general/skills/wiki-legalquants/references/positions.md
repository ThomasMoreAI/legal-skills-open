# Practical Position notes and stored wording

Keep the four existing note types. A Position may be a substantial Markdown
note. Use only the sections that help; this is an optional structure, not a
new mandatory schema:

- **Applicability:** generic circumstances, objectives, jurisdiction and date.
- **Approach:** the position and its basis: observed, candidate or approved.
- **Alternatives:** fallback variants and when each applies; no fixed tier count.
- **Rationale:** reusable commercial reasoning and dependencies.
- **Model wording:** exact source-backed blocks with their review status.
- **Escalation guidance:** user-supplied guidance, identified as such.

These conventions borrow the Playbook Builder distinction between observed
practice and approved positions. Repetition is not approval, and one negotiated
example does not establish market practice. Wiki stores reference knowledge;
it does not silently apply a stored preference as instructions to other work.

Preserve generic conditions such as “limited bargaining leverage” or “a
regulated counterparty.” Omit identifying deal details and distinctive
combinations of sector, size, date and anecdote. Generalize the rationale; do
not retain a matter's story or a link to its files. Different conditional
options can coexist without disputed status.

## Exact model blocks

Use source-backed, authorised non-matter wording only. Record the block in a
note body using unique, lowercase hyphenated identifiers:

```text

Exact source wording, including [placeholders], goes here.

```

The text between the marker lines, including its final newline, is the exact
block. In the note frontmatter add an optional `wording` list. Each record has
`id`, `source_id` (matching the note's sources), `status` (`observed`, `candidate`
or `approved`), and `sha256` of the block's UTF-8 bytes. Approved records also
carry `approved_by: human:<id>` and `approved_at` as an ISO date/time. Set those
only after the lawyer explicitly approves that exact block for storage. Do not
infer block approval from whole-note verification. Use the normal gated note
mutation and verification workflow; never bypass history to add these fields.

Before approving a block, compare it with the named source and pinpoint. A hash
proves unchanged text, not legal correctness or source authenticity. Whole-note
human review and block approval are separate. Changes to wording require a new
source check and explicit approval; never silently refresh its approval hash.

For Ask, the optional stdlib helper returns exact text and source/approval data:

```text
python3 scripts/wiki_wording.py --wiki /wiki/root --note topic/positions/note.md --block example-option
python3 scripts/wiki_wording.py --wiki /wiki/root --note topic/positions/note.md --block example-option --check /workspace/answer-block.txt
```

The helper is a private Ask reader, not a shareable export. It excludes pending,
unreviewed, non-stable or stale notes and unapproved/changed blocks. The check
compares the answer block byte-for-byte; no punctuation or whitespace folding.
Without scripts, read the delimited block and compare it directly. If exactness
cannot be verified, say so. Never reconstruct missing wording. Display the
source, approval status and applicability outside the quote. The existing
Position exclusion from Browse and shareable views remains in force.
