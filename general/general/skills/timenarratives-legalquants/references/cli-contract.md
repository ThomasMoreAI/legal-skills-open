# Portable internal workflow contract

The host exposes one `/timenarratives` action. Derive the lawyer, matter and
source selection from the current conversation or the user's clear request.
The current conversation needs no upload; retrieve related conversations only
within that selection, following `conversation-context.md`. Do not ask the user or the model to invoke the packet compiler,
map validator, or renderer as separate commands.

Inside one owned temporary run directory, the host performs these stages as
in-process helpers or equivalent local operations:

1. Run `start_run.py --lawyer <name> --matter <matter> --source-root <folder>
   <selected paths…>` (add `--note` for an inline note and repeated
   `--conversation ID PATH` for captured conversation snapshots). The host
   prepares snapshots using `conversation-context.md`; preserve original text,
   roles and source IDs. It builds the request,
   creates the run directory as a new sibling of the source root, compiles the
   packet, and prints a plain summary. Do not write `request.json` by hand and
   do not choose a run directory. The compiler preserves source identity,
   bounded content, unreadable-source reasons, and packet digests without
   searching beyond the selected list.
   `--as-of` is an optional explicit observation clock for reproducible replay;
   omit it for the actual current clock. It does not establish an activity date
   or override the selected source-date bounds. Do not ask the lawyer for it.
   Repeated `--folder <relative folder>` options additionally expand expressly
   selected folders and their ordinary subfolders into the fixed file list;
   `--folder .` selects the root. The root alone never selects its contents.
   `document-context.md` specifies limits, link refusal and unsupported-file
   reporting. Files, folders, notes and snapshots can be combined in one run.
   Later additions require a fresh combined run and approval, not an amendment
   to an already approved map. Folder membership is not monitored after expansion.
2. Give the resulting packet to the model for the activity judgment. The
   model writes `draft-map.json`: the map shape, except that every atom carries
   a `quote` of the exact unit text and no `startByte`, `endByte` or
   `spanSha256`.
3. Run `anchor_map.py --packet <packet> --draft <draft-map.json>
   --source-root <folder> --out <map.json>`. It resolves each quote to its unique byte span, fills the span
   and hash, and validates the result against the packet in the same call.
   Correct the named fault (`quote_not_found` shows the nearest unit text;
   `quote_ambiguous` needs a longer quote) and rerun; never edit `startByte`,
   `endByte` or `spanSha256` by hand. Structural, provenance, privacy, and
   prohibited-output faults are deterministic; a fault makes the draft
   unvalidated and must be stated plainly.
4. For a first response, retain the emitted `mapDigest` with the displayed
   draft, before receiving approval. Render the validated map in memory as an unposted
   draft. Return that draft, the short “Needs your check” list, and the exact
   scope sentence from `SKILL.md`; do not publish a persistent artifact or ask
   the user to handle a token.

Only after the user approves the displayed draft does the host publish. Rerun validation and call the renderer with `--user-approved --reviewed-map-digest <retained mapDigest>`. The digest must be the one retained at display, not a fresh value computed after a correction. The renderer refuses a missing or mismatched reviewed digest, binds the session-recorded confirmation to the packet and map, rechecks source freshness, and publishes with the no-replace primitive. No token is shown to, or requested from, the user. For corrections, regenerate and validate the map, show any materially revised wording, retain its digest and obtain approval of that version. Generic approval does not resolve an unanswered factual question; exclude that activity from the approved map. A `--confirmation` file remains accepted for maintenance and test surfaces only.

The shipped helpers remain separately testable implementation modules:
`build_packet.py`, `validate_map.py`, and `render_deliverable.py`. Their
standalone command-line interfaces are maintenance and test surfaces, not a
user-facing workflow. Resolve their paths relative to the installed skill and
keep all intermediate extraction in the owned temporary directory. Delete the
temporary packet when the workflow completes.

The final publication boundary remains strict: the output directory must be a
new sibling outside the selected source root, contain the complete
`deliverable.json` and `narratives.md` pair under `artifacts/`, and be created
with the platform's exclusive no-replace operation. Existing targets,
symlinks, hard links, and linked ancestors are refused without replacement.
