---
name: narrative
title: /narrative — Update All Project Narratives
description: Update project narratives from raw JSONL transcripts. Runs for all projects with unprocessed transcripts.
author: scottf007
author_url: https://github.com/scottf007/llm_memory/tree/main/skills/narrative
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# /narrative — Update All Project Narratives

Update project narratives by processing unprocessed JSONL transcripts into the
living narrative document. Works across all projects automatically.

One pipeline, no branching: each session becomes a structured delta
(`delta-extractor` agent), deltas merge into a per-project JSON state
(`merger.py`), and the state renders to markdown (`renderer.py`). The rendered
`~/.claude/memory/projects/{project}.narrative.md` file is the narrative.
Projects that don't yet have a state JSON are bootstrapped with an empty stub.

## Step 1: Discover work

Call `narrative_coverage(project=PROJECT)` for the current project first, then
for any other projects surfaced by the session_start hook. `narrative_coverage`
computes unprocessed transcripts by diffing on-disk main-session transcripts
against `{project}.json.sessions[]` (i.e. sessions already merged).

To enumerate all projects with session activity:

```bash
python3 -c "
import sys; sys.path.insert(0, '/home/scott/.claude/memory/lib')
from conversations import iter_sessions
seen = {fm.get('project') for fm in iter_sessions() if fm.get('project')}
for p in sorted(seen): print(p)
"
```

If `unprocessed` is empty for a project, skip it.

## Step 2: Process each project

**Cross-project parallelism**: different projects write to different state
files / narratives, so they can run simultaneously.

**Within-project sequential**: each session's merged state feeds the next
session's input. Never run two sessions for the same project in parallel.

**Bootstrap vs. incremental**: if `{project}.json` doesn't exist, create the
empty stub (below) and run `narrative_coverage` — it will report every
main-session transcript the project has ever had as unprocessed, because the
merged-sessions list in the JSON is empty. If `{project}.json` already
exists, `narrative_coverage` returns the usual incremental diff.

### 2a. Create `{project}.json` if it doesn't exist

- Write the empty stub to `~/.claude/memory/projects/<project>.json`:

```json
{
  "schema_version": "0.1",
  "project": "<project_name>",
  "last_updated": null,
  "summary": {},
  "operations": [],
  "decisions": [],
  "goals": [],
  "suggestions": [],
  "learnings": [],
  "done": [],
  "sessions": [],
  "narrative": {"rendered_at": null, "record_uuid": null, "drift_audit": null}
}
```

Then call `narrative_coverage(project=PROJECT)` — with an empty
`sessions[]`, it reports every main-session transcript as unprocessed. Use
that list.

After the bootstrap run finishes, `sessions[]` is populated and all
subsequent runs follow the normal incremental path automatically.

### 2b. Filter transcripts (applies to both paths)

Whichever list you picked in 2a (full history for bootstrap, or `unprocessed`
for incremental), keep only **main-session** transcripts. Skip any file
whose session_id starts with `agent-` — those are subagent transcripts and
must not trigger this pipeline. Sort the survivors chronologically by their
`started` timestamp (read the first JSONL record's `timestamp`, or derive
from file mtime if unavailable). Drop any entries whose
`~/.claude/memory/conversations/<session_id>.md` file is missing.

### 2c. For each main-session transcript, in order

1. **Check the delta cache** before spawning an agent:

   ```bash
   python3 ~/.claude/memory/lib/delta_cache.py check SESSION_ID ISO8601_START
   ```

   Prints `use_cache` or `reextract` on stdout; decision reason on stderr.
   Policy: exact hash match → always reuse; hash mismatch → re-extract with
   probability `exp(-age_days / 14d)`, deterministic per session_id; missing
   file → re-extract. If `use_cache`, skip step 2 and proceed to step 3.

2. **If `reextract`,** spawn the `delta-extractor` agent. Wait for it to
   finish and write its delta JSON, then stamp the current extractor hash
   into the file so subsequent runs can cache-hit it:

   ```
   Agent(
     description="Delta PROJECT: SESSION_ID",
     subagent_type="delta-extractor",
     prompt="""Project: PROJECT_NAME
   conversation_md_path: /home/scott/.claude/memory/conversations/SESSION_ID.md
   project_state_path:   /home/scott/.claude/memory/projects/PROJECT_NAME.json
   session_id:           SESSION_ID
   session_started_at:   ISO8601_START
   session_ended_at:     ISO8601_END
   output_path:          /home/scott/.claude/memory/deltas/SESSION_ID.delta.json

   Read the project state JSON and the conversation markdown. Produce the
   structured delta per your prompt spec and write it as JSON (only) to
   output_path. Do not modify the project state — the merger does that.
   Do NOT use worktree isolation. Do NOT commit anything.""",
     run_in_background=False
   )
   ```

   ```bash
   python3 ~/.claude/memory/lib/delta_cache.py stamp \
     ~/.claude/memory/deltas/SESSION_ID.delta.json
   ```

3. **Run the merger** on whichever delta is now on disk (cached or fresh):

   ```bash
   python3 ~/.claude/memory/lib/merger.py \
     ~/.claude/memory/projects/PROJECT_NAME.json \
     ~/.claude/memory/deltas/SESSION_ID.delta.json
   ```

   The merge must succeed before launching the next delta-extractor for this
   project — the next agent reads the updated `{project}.json` as input.

4. Before the first delta-extractor call for a run, ensure the deltas dir
   exists: `mkdir -p ~/.claude/memory/deltas`. The merger is idempotent
   per session_id; the cache is idempotent by `extractor_hash`. Leftover
   delta files are a feature, not debt — they act as the pre-processed
   cache so repeat runs skip LLM calls.

5. **If the delta-extractor's Write to `~/.claude/memory/deltas/...` fails
   or prompts repeatedly,** that's a missing permission, not a sandbox
   block. Do NOT reroute through `/tmp/` and `mv` — that just multiplies
   the prompts. Tell the user to add `Write(/home/scott/.claude/memory/**)`
   to `~/.claude/settings.json`'s `permissions.allow` (it ships in
   `settings.yaml` as of the post-2026-05-11 install; older installs need
   to re-run `install.sh` or add it manually) and stop.

### 2d. Render once per project

After all deltas for the project have merged:

```bash
python3 ~/.claude/memory/lib/renderer.py \
  ~/.claude/memory/projects/PROJECT_NAME.json \
  ~/.claude/memory/projects/PROJECT_NAME.narrative.md
```

The rendered `.narrative.md` file is the narrative — session_start + subagent_start
hooks read it directly. Nothing else to do; the pipeline ends here.

## Step 3: Summary

When all projects finish, emit a compact summary:

```
Narrative update complete:
  - PROJECT_A: N session(s) processed -> ~/.claude/memory/projects/PROJECT_A.narrative.md
  - PROJECT_B: M session(s) processed -> ~/.claude/memory/projects/PROJECT_B.narrative.md
  - PROJECT_C: no unprocessed transcripts
```

Do not reload full narratives — they load on next session start.

## When No Work Is Needed

If every project shows 0 unprocessed transcripts, say so and stop. Don't force
updates.

## Narrative Format Reference

Full spec: `docs/narrative-v2-format.md` in the llm_memory repo. Target ≤5,000
tokens. 8 required sections: The Idea, Approach, What's Done, What We've
Learnt, What We Want To Do, Suggested Work, Resuming, Source Transcripts.

Key principle: content dissolves from specific sections into standing
sections. Information changes form, never disappears.
