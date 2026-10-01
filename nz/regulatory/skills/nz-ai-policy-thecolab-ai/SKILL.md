---
name: nz-ai-policy-thecolab-ai
title: NZ AI Policy
description: Map and brief official New Zealand AI policy guidance — public-service AI framework, responsible GenAI guidance, procurement, privacy, algorithm governance, AI strategy, and source-backed agency checklists. Use when the task involves NZ public-sector AI policy citations, compliance review, proposal evidence, AI governance questions, or agency GenAI policy drafting.
author: thecolab-ai
author_url: https://github.com/thecolab-ai/.skills/tree/main/skills/nz-ai-policy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: nz
practice: regulatory
language: en
sources:
- title: Source Map
  path: references/source-map.md
---

# NZ AI Policy

## Goal

Provide a deterministic source-map, search helper, briefing generator, and checklist for official New Zealand public-sector AI policy and guidance material.

The skill is citation-first: it points to official sources, records fetched/access timestamps, and distinguishes guidance, templates, strategy context, regulator guidance, OIA releases, and algorithm-governance material.

## Use this when

- A user needs official NZ public-sector AI policy or guidance citations
- A proposal, review, or briefing asks for public-service AI governance, procurement, privacy, transparency, accountability, fairness, or records-management sources
- An agency wants a source-backed checklist for a generative-AI use policy
- A workflow needs a concise briefing on public-sector AI, AI procurement, privacy, or the Algorithm Charter
- Another agent needs JSON output listing official source URLs and source metadata

## Do not use this for

- Legal advice or a final compliance sign-off
- Private, unpublished, privileged, or authenticated policy material
- Claiming guidance is binding law unless the cited source says so
- Assuming public-service guidance applies unchanged to local government, Crown entities, schools, health organisations, council-controlled organisations, vendors, or private businesses
- Bypassing bot protection, CAPTCHAs, paywalls, authentication, or access controls

## Preferred workflow

1. Run `sources --json` to identify the relevant official source IDs and categories.
2. Use `briefing public-sector|procurement|privacy|algorithm-charter --json` for a concise cited summary.
3. Use `checklist agency-genai-policy --json` when drafting or reviewing agency AI-use policy controls.
4. Use `search QUERY --json` for source-map matches, or add `--live` when you need best-effort snippets from sources that permit direct HTTP.
5. Use `fetch SOURCE --json` for a live source preview or graceful blocked-source metadata.
6. Always cite source URLs and the command's fetched/generated timestamp in user-facing outputs.
7. Include the caveat that this is not legal advice and guidance changes over time.

## CLI

Run from the repo root:

```bash
python3 skills/nz-ai-policy/scripts/cli.py <command> [flags]
```

Commands:

- `sources [--category CATEGORY] [--json]` - list and categorise official sources
- `fetch SOURCE [--timeout SECONDS] [--max-chars N] [--json]` - fetch/source-preview one official page or PDF metadata
- `search QUERY [--limit N] [--snippets N] [--live] [--json]` - search source metadata and optionally fetched text snippets
- `briefing public-sector|procurement|privacy|algorithm-charter [--json]` - concise cited briefing
- `checklist agency-genai-policy [--json]` - source-backed agency GenAI policy checklist

Examples:

```bash
python3 skills/nz-ai-policy/scripts/cli.py sources --json
python3 skills/nz-ai-policy/scripts/cli.py briefing public-sector --json
python3 skills/nz-ai-policy/scripts/cli.py search "human oversight" --json
python3 skills/nz-ai-policy/scripts/cli.py search privacy --live --json
python3 skills/nz-ai-policy/scripts/cli.py checklist agency-genai-policy --json
python3 skills/nz-ai-policy/scripts/cli.py fetch privacy-ai --json
```

## Source coverage

The CLI source map covers Digital.govt.nz Public Service AI Framework, GCDO role, Responsible AI Guidance pages, the Public Service AI Work Programme and Toolkit, data.govt.nz Algorithm Charter and Algorithm Impact Assessment guide, the Office of the Privacy Commissioner AI page, MBIE AI Strategy/regulatory posture pages, and the Public Service Commission OIA AI-policy PDF.

Direct HTTP is preferred. Some Digital.govt.nz and data.govt.nz pages can return bot-protection HTML to plain `urllib`; the CLI reports `source_blocked_plain_http` instead of pretending content was fetched. Use the official URL in a browser where needed and keep the source-map/citation metadata.

## Resources

- CLI entrypoint: `scripts/cli.py`
- Smoke test: `scripts/smoke_test.py`
- Source-map notes and caveats: `references/source-map.md`

## Notes

- Python standard library only; no API key, login, browser session, or cache is required.
- The PSC PDF is reached as PDF metadata only; full PDF text extraction is not attempted without third-party dependencies.
- Briefings and checklists are source-backed orientation aids, not legal advice.
- Prefer current official-source wording over hardcoded summaries when precision matters.
