---
name: law-firm-wiki-compiler
title: Law Firm Wiki Compiler
description: Compile institutional PI practice knowledge from FirmVault activity logs into a structured Obsidian wiki using Karpathy's LLM Knowledge Base architecture. Use when adding new cases, recompiling, querying, or linting the law firm wiki.
author: Whaleylaw
author_url: https://github.com/Whaleylaw/Roscoe-hermes/tree/main/roscoe-state/skills/domain/law-firm-wiki-compiler
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
tags: [wiki, karpathy, firmvault, compilation, obsidian, knowledge-base]
---

# Law Firm Wiki Compiler

## When to Use

- Adding new cases or old case archives to the wiki
- Recompiling after activity log updates
- Querying the wiki for institutional knowledge
- Running lint/health checks on wiki articles
- Generating Hermes skills from wiki articles

## Excel Ingestion (FileVine Activity Exports)

When Aaron sends an Excel spreadsheet of activity logs from FileVine:

### Expected format
- Sheet columns: `Project Name | Note Text | Created At | (empty)`
- Project Name = "Client Name CaseType MM/DD/YYYY" (e.g., "Amy Stich WC 01/17/2024")
- Note Text = markdown-formatted activity notes (may contain FileVine links, strikethroughs)
- Created At = datetime

### Conversion steps
1. `pip install openpyxl` if needed
2. Load with `openpyxl.load_workbook(path, read_only=True)`
3. Slugify case names per FirmVault rules (lowercase, strip apostrophes/quotes, & → and, non-alnum → hyphens)
4. Group entries by case, then by date within each case
5. Write to `FirmVault/cases/<slug>/Activity Log/<YYYY-MM-DD>.md` with frontmatter:
   ```yaml
   schema_version: 2
   date: "YYYY-MM-DD"
   category: imported
   subcategory: settlement_activity_export
   ```
6. Use the `subcategory: settlement_activity_export` tag to identify imported-from-Excel cases later

### Multiple files in one session
Aaron often sends multiple Excel files in sequence. Process each one fully
(convert → batch → compile → rebuild index) before asking for the next.
The converter handles deduplication automatically — if a case dir already
exists, new logs append; if a log file for that date exists, it appends
an "Imported Entries" section.

### Sizing reference (2026-04-12 imports)
- File 1 (settlement_1): 17,639 rows → 198 cases → 6,221 log files (13.7 MB)
- File 2 (settlement_2): 22,182 rows → 169 cases → 7,341 log files (12.9 MB)
- File 3 (settlement_3): 688 rows → 8 cases → 158 log files (small)
- File 4 (closing): 9,363 rows → 125 cases → 2,924 log files
- Conversion takes ~2 seconds per file
- Duplicate detection: compare row count + first/last row to identify resends

### Batch size decisions
- **>50 cases**: 3 parallel subagents (split evenly by log count)
- **10-50 cases**: 1-2 subagents depending on log volume
- **<10 cases**: Single subagent with targeted article updates only.
  Do NOT have it read all existing articles — point it at the 5-6 most
  likely articles to update. Set max_iterations=30 to avoid running out
  of turns on reading.

### Reusable converter script
Save to /tmp/convert_excel.py, swap the path for each new file. The script:
- Uses openpyxl (pip install if missing)
- Slugifies per FirmVault rules
- Groups by case → date → writes markdown with frontmatter
- Reports new vs updated case dirs

## Architecture

Karpathy's 3-layer pattern: raw sources → LLM compiler → structured wiki

```
Layer 1: Raw (immutable)
  cases/*/Activity Log/*.md  — 21K+ activity logs
  cases/*/*.md               — case files
  
Layer 2: Wiki (LLM-maintained)
  wiki/
    Home.md          — Obsidian dashboard
    index.md         — master catalog
    log.md           — compilation history
    concepts/*.md    — atomic knowledge articles (63 as of 2026-04-12)
    connections/*.md — cross-cutting insights (26 as of 2026-04-12)
    AGENTS.md        — compiler schema (the spec)
    SPEC.md          — architecture doc
    
Layer 3: Consumers
  Hermes semantic skills, OpenClaw agents, Aaron via Hermes
```

## Compilation Process

### Batch Processing (for bulk cases)
1. Group cases into batches of ~80K tokens
2. Delegate 3 batches in parallel
3. Each subagent reads AGENTS.md, existing articles, case files + sampled logs
4. Subagents UPDATE existing articles (evidence_count++) or CREATE new ones
5. Do NOT let subagents rewrite index.md (race condition) — rebuild after
6. Rebuild index.md from all articles on disk after all batches complete

### Key Instructions for Compiler Subagents
- Read AGENTS.md for full schema
- Read ALL existing concept + connection articles before writing
- ANONYMIZE all PII (use "Case A", "Case B", etc.)
- UPDATE existing > CREATE new (upgrading confidence is the goal)
- Confidence: low (<5 cases), medium (5-9), high (10+)
- Use [[wikilinks]] between articles
- Append to log.md, do NOT rewrite index.md

### Sampling Strategy
- Large cases (400+ logs): first 40 + last 40 chronologically
- Medium cases (100-400): first 25 + last 25
- Small cases (<100): first 10 + last 10, or all

### Subagent Prompt Template
```
Law Firm Wiki compiler. Read /opt/data/FirmVault/wiki/AGENTS.md.
Read existing articles in wiki/concepts/ and wiki/connections/.
Compile cases: [LIST]. For each: read cases/<slug>/<slug>.md and
sample first N + last N activity logs. UPDATE existing articles
(increment evidence_count, upgrade confidence: 5=medium, 10=high).
CREATE new only for genuinely new patterns. ANONYMIZE PII.
Write to wiki/. Do NOT rewrite index.md. Append to wiki/log.md.
```

### Adapt prompts to data category
Different Excel exports contain different types of data. Add a focus hint:
- **Settlement files**: "Focus on: settlement patterns, negotiation tactics,
  treatment timelines, SOL management, adjuster behavior, lien resolution"
- **Closing files**: "These are CLOSING cases -- look especially for: case
  closure workflows, decline reasons, final disbursement, file archival,
  post-closing obligations, client termination patterns"
- **Intake files**: Focus on onboarding, insurance verification, initial
  treatment referrals
This dramatically improves pattern extraction quality.

### Index rebuild
Always rebuild index.md as a **separate delegate_task** after all compilation
batches complete. Even for small batches. The subagent just needs to parse
YAML frontmatter from all .md files in concepts/ + connections/ and generate
the index per the schema in AGENTS.md. Takes ~60 seconds, max_iterations=15.

## Obsidian Vault

The wiki/ directory IS an Obsidian vault:
- .obsidian/ config with graph colors (blue=concepts, orange=connections)
- Home.md as landing page
- [[wikilinks]] use slug names (NOT path-prefixed)
- Graph view shows article interconnections

### Wikilink Rules
- Use `[[slug-name]]` not `[[concepts/slug-name]]`
- Obsidian resolves by filename, paths break links

### Filtering Cases for Compilation

Two approaches — use the Excel file directly (preferred) or scan the vault:

**Preferred: Extract slugs from the Excel file itself**
```python
# Parse Excel → get unique Project Names → slugify → batch
wb = openpyxl.load_workbook(path, read_only=True)
cases = Counter(str(r[0]).strip() for r in list(wb.active.iter_rows(values_only=True))[1:] if r[0])
slugs = [{"slug": slugify(name), "logs": count} for name, count in cases.items()]
```
This is precise — only compiles what was just imported.

**Fallback: Scan vault by subcategory tag**
```python
for slug in os.listdir(cases_dir):
    for logfile in os.listdir(log_dir):
        if "settlement_activity_export" in open(logfile).read(200):
            new_slugs.append(slug)
            break
```

**Do NOT use mtime-based filtering** — it picks up every case in the vault
(including old ones whose dirs were touched during conversion).

## Pitfalls

1. Parallel subagents cause race conditions on evidence_count — accept ±3 variance
2. Don't let subagents rewrite index.md — rebuild it yourself after all batches
3. Large cases (1000+ logs) must be truncated — sample strategically
4. Wikilinks with path prefixes break in Obsidian — strip `concepts/` etc.
5. The compile.py script generates prompts but doesn't call the LLM directly — use delegate_task
6. Some articles reference aspirational links (articles not yet created) — that's OK, they'll be created as more cases are compiled
7. **mtime-based vault scanning doesn't work** for identifying "just imported" cases — conversion touches existing dirs too. Always extract the case list from the Excel file itself.
8. **Closing cases are mostly declines**, not post-settlement closures. The decline/close workflow gets the biggest evidence boost from closing data, not the settlement disbursement workflow.
9. **Small batches (<10 cases) exhaust subagent iterations** if you have them read all 89 articles. Point them at specific articles instead.

## Multiple-File Workflow

When user sends multiple Excel files, convert all first then compile:
1. Reuse /tmp/convert_excel.py — just patch the filename for each file
2. After all converted, batch the NEW cases only (use slugify + check existence)
3. Compile in 3 parallel batches, then rebuild index once at the end

## Duplicate Detection

User may send the same file twice (same name, different doc ID). Compare row counts + first/last row to detect dupes before converting.

## Sizing from Imports

- File 1 (settlement_1): 17.6K entries, 198 cases, 6.2K log files
- File 2 (settlement_2): 22.1K entries, 169 cases, 7.3K log files  
- File 3 (settlement_3): 688 entries, 8 cases (small — single-batch)
- File 4 (closing): 9.3K entries, 125 cases, 2.9K log files
- Files 5-7 (archived 2,3,4): 64.3K entries, 692 cases, 21K log files
Total ingested: ~114K entries, 1,170 cases, ~56K log files → 93 wiki articles

## Preferred Batching

- <20 cases: single subagent, no batching
- 20-300 cases: 3 parallel subagents
- >300 cases: 3 parallel subagents with aggressive sampling (first 10 + last 10)
- Always rebuild index.md AFTER all batches complete (never let subagents touch it)

## Pitfall: mtime-based filtering unreliable

Don't use file mtime to find "new" cases — convert_excel.py touches existing files too. Instead, extract case names from the Excel directly and slugify to get the target list.

## Files

- FirmVault: /opt/data/FirmVault
- Wiki: /opt/data/FirmVault/wiki/
- Schema: wiki/AGENTS.md
- Converter: /tmp/convert_excel.py (patch filename between runs)
- Article counts: 65 concepts + 28 connections = 93 total (as of 2026-04-12)
- Decisions: /opt/data/FirmVault/decisions/ (ADR-000 through ADR-006)
- Audit report: /opt/data/FirmVault/wiki/reports/workflow-vs-wiki-audit.md
- v2 proposal: /opt/data/FirmVault/wiki/reports/PHASE_DAG_v2_proposal.md

## Workflow Auditing

After a major compilation round, audit the wiki against the PHASE_DAG:

1. Read PHASE_DAG.yaml (prescribed workflow)
2. Read all wiki articles (observed reality)
3. Compare: contradictions, gaps, redundancies
4. Write audit report to wiki/reports/
5. If changes warranted, draft PHASE_DAG v2 proposal
6. Document decisions as ADRs in decisions/ (cherry-picked from stirps-ai/stirps-gov)

This audit is what turned 93 wiki articles into actionable architectural
decisions. The wiki is evidence; the ADRs are commitments.
