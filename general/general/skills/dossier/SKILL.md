---
name: dossier
title: Dossier
description: Use when investigating a topic that benefits from a reusable, citation-backed NotebookLM corpus—literature reviews, due diligence, regulatory/legal research, competitive intelligence, long-term personal knowledge queries, or any repeated deep-dive across the same body of material. Not for one-off web search, single-document reads, or code exploration.
author: wangbooth
author_url: https://github.com/wangbooth/dossier
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Dossier

Open a topic-scoped NotebookLM corpus (the "dossier"), let Claude orchestrate curation and reasoning, let NotebookLM serve citation-backed answers from within the dossier. The dossier persists—future questions on the same topic reuse it.

## When to use

- Reading 5+ papers/reports on one topic
- Pre-IPO / pre-deal due diligence on a company or sector
- Legal, regulatory, or compliance review across document sets
- Competitive analysis across multiple products/companies
- Long-term personal knowledge base queries (Obsidian/Readwise exports, meeting archives)
- Any task where answers must be traceable to source text

## When NOT to use

- One-off questions answerable from general knowledge or single web page — just ask Claude directly
- Codebase exploration or "jump to definition" — your agent's native file tools (Read/Grep/etc.) are stronger
- Real-time / freshly changing information — NotebookLM is static
- Tiny corpora (< 5k tokens) — fitting in Claude's context is simpler
- When speed matters over depth — NotebookLM is ~3× slower than direct chat

## Setup (first run in a machine)

Preflight has 4 steps. Only step 1 is read-only and always safe to auto-run. Steps 2–4 have side effects (disk writes, browser popups, skill directory changes) — **ask the user before each one**.

### Step 1 — Detect (auto, read-only)

```bash
# What CLI form is reachable?
if command -v notebooklm >/dev/null 2>&1; then
  NBLM="notebooklm"
elif python3 -m notebooklm --help >/dev/null 2>&1; then
  NBLM="python3 -m notebooklm"   # pip-installed but scripts dir not on PATH — common on macOS
else
  NBLM=""                        # not installed
fi

# Does the existing session work?
if [ -n "$NBLM" ] && $NBLM auth check 2>&1 | grep -q "Authentication is valid."; then AUTH_OK=1; else AUTH_OK=0; fi
# Note: matches the final verdict line — only appears when every sub-check
# passed. Matching "✓ pass" alone would false-positive when e.g. only
# "Storage exists" passed but SID/token checks failed.
```

### Step 2 — Install (only if `$NBLM` is empty) — **ASK FIRST**

Tell the user: *"I don't see `notebooklm-py` on this machine. May I install it with `pip install 'notebooklm-py[browser]'` plus Playwright Chromium (~150MB)?"*. Wait for an explicit yes, then:

```bash
pip install "notebooklm-py[browser]"
python3 -m playwright install chromium
NBLM="python3 -m notebooklm"
```

If the `notebooklm` binary lands outside `$PATH` (typical on macOS where `pip install` writes to `~/Library/Python/<ver>/bin/`), **don't try to patch PATH yourself** — just report it and continue using the `python3 -m notebooklm` form everywhere. It works identically.

### Step 3 — Authenticate (only if `AUTH_OK=0`) — **ASK FIRST, OPENS BROWSER**

`$NBLM login` opens Chrome for Google OAuth. Tell the user it'll pop a browser window before running.

### Step 4 — Install the low-level `notebooklm` skill (once per machine) — **ASK FIRST**

`$NBLM skill install` writes to `~/.claude/skills/notebooklm/` — it gives Claude direct knowledge of the raw CLI commands, which complements this `dossier` skill. Low risk but still a filesystem change; tell the user, then run.

## Routes — pick the right entry point

**First branch — does a dossier on this topic already exist?** Run `$NBLM list` before anything else.

- **Yes** (same or adjacent topic) → **Route D** (query / top-up / hygiene). Most time on any long-running topic is spent here, not in fresh builds.
- **No** → pick one of A/B/C below based on source-quality requirements. Default: **Route B**.

Always present the choice to the user before spending time.

| Route | When | Setup time | Claude tokens | Durability |
|---|---|---|---|---|
| **A. NotebookLM deep research** | Quick overview, one-shot curiosity | ~5 min | near-zero | ephemeral (dossier stays but seeded by auto-research) |
| **B. Claude-curated sources** ⭐ | Noisy topic, long-term reuse, authoritative-source requirement | 15–30 min | moderate (fetching/filtering) | persistent |
| **C. User-specified sources** | Strict source whitelist (specific authors, databases) | depends on list | moderate | persistent |
| **D. Existing dossier** | Continuing research on a topic that already has a dossier | near-zero | low (mostly Q&A, maybe small top-up) | persistent |

### Route A — NotebookLM auto-research

```bash
$NBLM create "dossier-<topic-slug>"
$NBLM use <notebook-id>
$NBLM source add-research "<search query>" --mode deep
```

NotebookLM's own research agent picks sources, imports them, and indexes. Claude then `ask`s questions. Source quality is opaque — good for exploration, risky for decisions.

### Route B — Claude-curated (recommended default)

**Steps:**

1. Claude searches authoritative sources (e.g. PubMed, Cochrane, ISSN, SEC EDGAR, primary sources for the topic — not random blogs or SEO pages)
2. Claude drafts a **source shortlist** with a one-line justification per source
3. **User confirms or edits the list** — never skip this step
4. Claude imports confirmed sources one by one (source type auto-detected from content):
   ```bash
   $NBLM source add "https://..."      # URL
   $NBLM source add ./paper.pdf        # local file
   $NBLM source add "pasted text" --title "My note"   # inline text
   ```
   All commands use the active dossier (set by `$NBLM use <id>`). Add `-n <id>` to override.
5. **Verify import quality** (see caveats below), fix any bad imports
6. Claude starts asking questions with `$NBLM ask --json "..."`

**Import caveats — read before step 4:**

- **Check every import.** Run `$NBLM source list` after a batch. If a title reads `Checking your browser - reCAPTCHA`, `Access denied`, or similar, NotebookLM's backend hit an anti-bot wall. One retry is fine; if still blocked, abandon the direct URL and go to the Jina fallback below — don't loop on retries.
- **Never batch-parallelize PubMed URLs.** `pubmed.ncbi.nlm.nih.gov` triggers reCAPTCHA extremely reliably under any concurrency, and even a 3-second serial delay isn't enough. Go straight to Jina Reader + DOI for PubMed.
- **Jina Reader fallback** — when a URL hits anti-bot walls, fetch it via Jina's proxy and ingest as a file. See "Jina key handling" below for how to obtain `$JINA_API_KEY`:
  ```bash
  curl -sL -H "Authorization: Bearer $JINA_API_KEY" \
    "https://r.jina.ai/<original-url>" -o /tmp/page.md
  $NBLM source add /tmp/page.md
  $NBLM source rename <source-id> "Author Year — descriptive title"
  ```
- **Prefer DOI over PubMed URL.** `https://doi.org/<doi>` redirects to the publisher. If it's MDPI / BMC / Frontiers / PLOS (open access), you'll get **full text**, which indexes 5–10× more useful content than a PubMed abstract page. Get the DOI from NCBI esummary: `curl "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=<PMID>&retmode=json"`.
- **`--title` only works for inline text.** When adding a file with `source add /path/file.md --title "..."`, the title is silently dropped and the filename becomes the title. Always follow a file import with `$NBLM source rename <id> "..."` to fix.

### Route C — User-specified

User provides the source list (files, URLs, or "only these authors"). Same commands and same caveats as Route B, just skip steps 1–3.

### Route D — Existing dossier (query / top-up / hygiene)

Pick this whenever `$NBLM list` shows a dossier on the same or adjacent topic. This is the default path for **continuing** research. It's not a build mode — A/B/C are for filling an empty dossier; D is for everything you do after.

Open the dossier, then branch into one of three sub-paths:

```bash
$NBLM list                        # find the dossier
$NBLM use <id>                    # activate it
$NBLM source list                 # remind yourself what's in here
```

#### D1. Query only

The dossier already covers the question — you just need an answer. Go straight to Ask, but respect **Working rule 10** (split or `-s`-scope wide questions before they time out).

#### D2. Top-up (incremental source add)

Q&A revealed a specific gap — one angle, a few missing sources. **Do not re-run Route B end-to-end.** Do a mini-curation instead:

1. Name the gap in one sentence (e.g. "no primary source on <X>'s 2024 pricing change")
2. Propose 1–5 new sources with one-line justifications, **user confirms**
3. Import with the same hygiene rules as Route B (check titles after add, use Jina/DOI fallback for anti-bot sites, rename files since `--title` is silently dropped on file imports)
4. `$NBLM source wait <id>` if the next ask is time-sensitive — otherwise NotebookLM may answer before the new source is indexed
5. Re-ask the gap question. If still unanswered, treat it as a real data problem (no public source exists, dossier source cap hit) rather than a curation problem — don't keep adding sources of diminishing quality

#### D3. Hygiene pass

Symptoms that trigger this: citations point to garbage titles (reCAPTCHA / access-denied), Ask returns "outside source material" for things you know are covered, duplicates after multiple top-up rounds, or the dossier has been idle for weeks. See **Source hygiene (ongoing)** below.

## Jina key handling (on-demand, only when a Jina fallback is actually needed)

Don't ask for a Jina key during preflight — most dossiers never need one. Only when a specific import hits an anti-bot wall and needs `r.jina.ai` does this flow run.

### Step 1 — Resolve the key (auto, read-only)

Try sources in this order; take the first non-empty:

```bash
CONFIG_FILE="${XDG_CONFIG_HOME:-$HOME/.config}/dossier/config.json"
JINA_API_KEY="${JINA_API_KEY:-}"    # 1. honor env var if already exported
if [ -z "$JINA_API_KEY" ] && [ -f "$CONFIG_FILE" ]; then
  JINA_API_KEY=$(python3 -c "import json; print(json.load(open('$CONFIG_FILE')).get('jina_api_key',''))" 2>/dev/null)
fi
export JINA_API_KEY
```

### Step 2 — If still empty, ask the user (don't save silently)

Say something like:

> "I need to fetch `<URL>` through Jina Reader because NotebookLM's direct fetch hit a reCAPTCHA wall. I don't see a Jina API key saved on this machine. You can get a free one at <https://jina.ai> (no credit card; click the big API key box on the homepage). Paste it in your next reply and I'll save it to `~/.config/dossier/config.json` with `chmod 600` so only you can read it. From then on it's automatic."

### Step 3 — When the user pastes the key, save it

Pass the key through a heredoc, **not argv** (argv ends up in shell history):

```bash
mkdir -p "${XDG_CONFIG_HOME:-$HOME/.config}/dossier"
python3 <<'PY'
import json, os
p = os.path.expanduser(os.environ.get("XDG_CONFIG_HOME", "~/.config") + "/dossier/config.json")
p = os.path.expanduser(p)
existing = {}
if os.path.exists(p):
    existing = json.load(open(p))
existing["jina_api_key"] = """<PASTE-USER-KEY-HERE>"""
os.makedirs(os.path.dirname(p), exist_ok=True)
json.dump(existing, open(p, "w"), indent=2)
os.chmod(p, 0o600)
print(f"Saved to {p}")
PY
```

After saving, do **not** echo the key back. Confirm with just: "Saved to `~/.config/dossier/config.json`. Continuing with the fetch."

### CI/CD / one-off overrides

Setting `JINA_API_KEY` in the environment always wins over the config file. Useful for:
- CI jobs that inject the key via secrets
- Testing with a temporary key without overwriting the saved one

## Source hygiene (ongoing)

Route B's "Import caveats" covers hygiene at *import time*. This section covers what to do **after** sources are in, because a dossier degrades over time — accumulated bad imports, URL rot, duplicates from top-up rounds.

### Spot-check what was actually indexed

A clean title in `source list` doesn't guarantee the content was ingested — NotebookLM occasionally indexes just a cookie banner or a single page of a multi-page article. When an Ask answer seems suspiciously thin on a source you added, verify:

```bash
$NBLM source fulltext <id> | head -100    # first 100 lines of actually-indexed text
$NBLM source guide <id>                    # AI summary + auto keywords — reveals what NotebookLM "sees"
```

If `fulltext` is tiny or the guide's keywords are off-topic, the source is effectively bad even if Ask answers look plausible (Ask is just leaning on other sources). Fix it before more Q&A.

### Delete-and-replace bad sources

```bash
$NBLM source delete -y <id>                 # by id (supports prefix match)
$NBLM source delete-by-title "Exact Title"  # errors if multiple match
```

**Always replace, don't just delete** — otherwise future Ask silently loses that angle. Replacement options:

- Refetch via Jina Reader (see Route B caveats) if original hit anti-bot
- Ingest the DOI / publisher URL instead of PubMed
- Add an **inline summary note** when no scrapable form exists — books you own offline, paywalled papers, Cloudflare-walled blog posts:
  ```bash
  $NBLM source add "<your summary text>" --title "<Author Year — topic> (notes)"
  ```
  Tag the title with `(notes)` or `(summary)` so later citations are unambiguous about what's primary vs. paraphrased.

### De-duplicate after top-ups

Top-ups often re-add the same paper via different URLs (PubMed ↔ DOI ↔ arXiv). Run `$NBLM source list` periodically and look for:

- Same author / year / title across different rows
- An abstract-only version and a full-text version of the same paper — keep full-text, delete abstract
- Same URL hostname cluster on overlapping topics (often indicates blog-post drift into the corpus)

### Refresh stale URL sources

URL and Drive sources can go stale when the upstream page changes:

```bash
if $NBLM source stale <id>; then
  $NBLM source refresh <id>
fi
```

Do a refresh pass before a new round of Q&A on a dossier that's been idle for weeks — cheaper than realizing mid-research that answers are from a cached old version.

## Working rules

1. **Check for existing dossier first.** Before creating a new one, run `$NBLM list` and scan for a dossier on the same or adjacent topic. If found, go to Route D — do not rebuild.
2. **Ask dossier before answering from memory.** Any claim about content inside the corpus goes through `$NBLM ask "..."`. Do not answer from LLM parametric knowledge when the dossier should know.
3. **Never paste source text into the Claude conversation.** The whole point is to keep bulk material out of Claude's context. If you find yourself about to quote a long PDF, stop — ask the dossier instead.
4. **Preserve citations, and resolve them.** The text answer contains `[1][2]` markers — those are only meaningful paired with the `references` array from `ask --json`. Always run `$NBLM ask --json ...` and map each citation number to its `source_id` + `cited_text` in the output. Bare `[1]` without resolution is misleading.
5. **If the dossier can't answer, say "dossier has no coverage" — do not extrapolate.** Listing unanswered questions is more useful than inventing answers.
6. **Curation is not optional in Route B/C.** Show the user the shortlist before importing. Bad sources poison every future query.
7. **One dossier per topic.** Don't mix "creatine research" and "Q4 earnings analysis" in one notebook — cross-contamination ruins citation quality.
8. **Clear conversation when changing subtopic.** `ask` defaults to continuing the last conversation (`is_follow_up=true`). When the user switches from one angle (e.g., safety) to another (e.g., dosage), run `$NBLM clear` first so the new question isn't biased by prior context.
9. **Honor NotebookLM's "outside the source material" layer.** When the answer contains phrases like "资料范围之外" / "outside the provided sources" / "not in the documents", NotebookLM is signaling speculation vs. sourced fact. Preserve this split in your output: put sourced content under `## Dossier says`, put speculation under `## Not covered by dossier` with an explicit "unverified" flag. Never merge the two.
10. **Split wide Asks; don't retry them.** NotebookLM can time out or return shallow answers when one `ask` spans too many sources (observed failures around 9+ sources in practice). When a question naturally crosses many sources, either split by angle (ask 2–3 narrower questions and synthesize) or use `-s <source_id>` (repeatable) to scope each ask to 1–5 sources. Never retry the same wide question more than once — split instead.
11. **Keep hygiene up to date — don't run on a dirty corpus.** When you spot a bad source mid-session (garbage title, suspiciously short `source fulltext`, duplicate of another source), stop and fix it before continuing. One bad source poisons every Ask that touches it, and hygiene debt compounds over top-up rounds. See **Source hygiene (ongoing)**.

## Output format

When delivering results to the user, structure as:

```markdown
## Dossier says
<facts from $NBLM ask, citations preserved>

## What I did
<commands run, files written, experiments executed>

## Conclusion
<your answer to the user's original question>

## Not covered by dossier
<questions the dossier couldn't answer — flagged for human follow-up>
```

## Quick command reference

```bash
$NBLM list                                      # list existing dossiers
$NBLM create "dossier-<slug>" --json            # new empty dossier, emit id as JSON
$NBLM use <id>                                  # set active dossier for session
$NBLM status                                    # show active dossier
$NBLM auth check                                # verify Google session still valid
$NBLM source add "https://..."                  # import URL (auto-detected)
$NBLM source add ./paper.pdf                    # import local file (auto-detected)
$NBLM source add-research "<query>" --mode deep # Route A auto-import
$NBLM source list                               # list sources in active dossier
$NBLM ask --json "<question>"                   # chat with active dossier — ALWAYS use --json to get citation→source mapping
$NBLM ask --json "..." -n <id>                  # chat with explicit dossier
$NBLM ask --json "..." -s <src1> -s <src2>      # source-limited ask (repeatable -s) — use to dodge timeouts and force focus
$NBLM source wait <id>                          # block until a newly-added source finishes indexing
$NBLM source fulltext <id>                      # dump NotebookLM's indexed text — verify what was actually ingested
$NBLM source guide <id>                         # AI summary + keywords for a source — quick sanity check
$NBLM source stale <id>                         # exit 0 if URL/Drive source needs refresh, 1 if fresh (shell-scriptable)
$NBLM source refresh <id>                       # re-fetch a stale URL/Drive source
$NBLM source delete -y <id>                     # delete source (use -y to skip confirmation)
$NBLM source delete-by-title "..."              # delete by exact title (errors if multiple match)
$NBLM generate audio --wait                     # podcast from dossier
$NBLM generate report --template study_guide    # markdown report
$NBLM summary                                   # AI-generated overview of dossier
```

Full CLI reference: `$NBLM --help` or `$NBLM <cmd> --help`.

## Known limitations

- **Unofficial API.** `notebooklm-py` uses reverse-engineered Google endpoints. Commands may break after Google backend changes — reinstall latest version if errors appear.
- **Session expires.** Re-run `$NBLM login` if calls start returning auth errors.
- **Route A source quality is opaque.** NotebookLM picks sources via web search; they may include blogs, wikis, or promotional pages. For high-stakes decisions, prefer Route B.
- **Notebook source cap.** Free tier 50 sources, Pro tier 300. Plan dossier scope accordingly.
- **Generation commands are slow.** `audio` / `video` take 5–10 min. Always use `--wait` when you need the artifact.
- **Single-ask source-count ceiling.** In practice, one `ask` over ~9+ sources frequently times out or returns shallow synthesis. Use `-s` to scope or split the query (see Working rule 10).

## Red flags — stop and reconsider

- About to paste a whole PDF into the Claude conversation → use `$NBLM source add --file` instead
- About to answer a factual question about the corpus from memory → use `$NBLM ask` instead
- Creating a new dossier because you forgot the old one existed → `$NBLM list` first
- Running Route B/C from scratch when `$NBLM list` already shows a relevant dossier → switch to Route D
- Skipping the shortlist-confirmation step in Route B to "save time" → bad sources will cost 10× more time later
- Asking a question that spans 6+ sources without `-s` scoping or splitting → timeout / shallow-answer risk
- Citations point to a source whose `source fulltext` is 50 lines of cookie banner → hygiene pass before more Q&A
- Dossier returns an answer without citations → something's wrong, re-check the query or source indexing
