---
name: pi-brief-format
title: pi-brief-format
description: After harvester-query returns a hit, render the result as a PI-lawyer-grade brief block (bluebook citation, paste-ready pull quote, NPS class-of-victim/class-of-harm analysis, common defenses, evidence to gather, source URL) using the local pi_brief module. Used for any statute response on WhatsApp.
author: barndonmai
author_url: https://github.com/barndonmai/specter/tree/main/openclaw/skills/pi_brief_format
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ca
practice: personal-injury
language: en
---

# pi-brief-format

Specter's response template for "lawyer asked about a statute." This skill turns a raw Harvester record into a structured brief — *not* a Wikipedia summary.

## When to use this skill

Use it any time `harvester_query.lookup_citation()` or `harvester_query.search()` returns a hit and the user is asking about *that statute*. Examples:

- *"What's CVC 23152(a)?"* → lookup, then brief format
- *"DUI laws in California?"* → search top hit, then brief format on the top result; offer to brief others
- *"Pull me the negligence-per-se argument for Cal. Veh. Code § 22350"* → lookup, brief format, point at the NPS section

**Don't** use it when the user is asking a non-statute question (case strategy, procedural questions, conversational). The brief format is overkill for those — just answer in voice.

## How to call

The renderer lives in `api/pi_brief.py` at the repo root. Two paths to invoke:

### Shell (use this from exec inside an OpenClaw turn)

```bash
cd ~/Specter && .venv/bin/python -m api.pi_brief lookup "Cal. Veh. Code § 23152(a)"
```

That runs the full pipeline: hits the local Specter API at `$SPECTER_API` (default `http://127.0.0.1:8000`), looks up the citation, renders the brief with ANSI colors stripped (since stdout isn't a TTY when Specter calls exec).

### Python (use this from a sub-skill or programmatic flow)

```python
import sys, pathlib
sys.path.insert(0, str(pathlib.Path("~/Specter").expanduser()))
from api.pi_brief import build_brief, render_text

# `record` is whatever harvester_query.lookup_citation returned.
brief = build_brief(record)
whatsapp_text = render_text(brief)
```

`render_text` is the WhatsApp-friendly renderer (no ANSI, plain emoji, ~3-4 message-block sized output). `render_ansi` is for the terminal.

## Output shape

The brief block has these sections, in order:

1. **🥃 Citation header** — citation + statute title.
2. **Bluebook** — formatted for a brief or letter, e.g. `Cal. Veh. Code § 22350 (West 2024)`.
3. **Pull quote (paste-ready)** — the statute language, de-bracketed, ready for a complaint or motion.
4. **PI angle — per factor** — for each contributing factor on the statute:
   - NPS availability marker (`✅ available`, `⚠️ qualified`, `❌ rare`)
   - Class of victim
   - Class of harm
   - One-line "why this matters in PI"
   - Common defenses
   - Evidence to gather
5. **Context (non-canonical PI tags)** — present only when a record has `pi_context_tags` (e.g., "Bicycle Violation", "Equipment"). Marked as non-canonical so the lawyer can tell context from canonical-eval-tag.
6. **Source** — the verifiable URL.
7. **Specter notes** — flagged commentary block. Auto-derived from playbook content (NPS availability summary, punitive flag, collateral-estoppel flag). Never LLM-generated.

## Voice rules (echoes SOUL.md)

- WhatsApp replies stay short by default. **The brief block IS long** — that's the trade. When you render it, that's the response. Don't add a Harvey-voiced preamble; the brief is the voice.
- If the user asked a *follow-up* question after seeing a brief ("what about Texas?", "does this apply to cyclists?"), drop the brief format and answer in voice. The brief is for the *first* statute hit; conversation is for everything after.
- **Never fabricate.** Every field in the brief traces back to the Harvester record (statute, citation, source URL) or the curated `data/pi_playbook.yaml` (doctrine, defenses, evidence). The brief is a renderer, not a generator.

## When the brief renders empty sections

If a record has no `contributing_factors` (e.g., a context-only-tagged statute like FL Bicycle Regulations), the brief shows the bluebook + pull quote + context tags + source URL — no factor analysis. That's correct. Tell the user:

> "Tagged for context (`Bicycle Violation`) but not on the canonical 17-factor PI taxonomy — useful for cyclist cases, no NPS analysis baked in."

## Don't

- Don't translate or paraphrase the statute body. Use the exact pull quote.
- Don't invent additional defenses or evidence beyond the playbook.
- Don't claim case law that isn't there. Case-law lookup is a separate skill (TBD).
- Don't render the brief for a *miss*. If `harvester_query` returns 404, use `web_fallback.verify` instead — and if that misses too, refuse honestly.
