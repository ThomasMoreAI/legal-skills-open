---
name: audit-archive
title: 'Phase 6: Archive'
description: Archives non-permanent URLs in legal document footnotes using the perma.cc API, then writes the resulting perma.cc links back to the DOCX file. Use this during a Bluebook audit workflow after footnote data has been extracted.
author: edwinhu
author_url: https://github.com/edwinhu/workflows/tree/main/skills/bluebook-audit/skills/audit-archive
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Phase 6: Archive

Archive all non-permanent URLs in footnotes via perma.cc API.

## What This Phase Does

1. Extract URL inventory from footnotes data
2. Deduplicate URLs (same URL across multiple footnotes)
3. Archive each URL via perma.cc API
4. Write perma.cc links back to DOCX footnotes
5. Save progress after each successful archive

## Prerequisites

- Perma.cc API key in `.env` file (project-level or user home directory)
- For institutional accounts: organization folder ID (unlimited archives)
- Free accounts: 10 links/month limit

## Script

```bash
uv run python3 "${CLAUDE_SKILL_DIR}/../../../../skills/bluebook-audit/scripts/permacc_archive.py" --docx <path> --data scratch/footnotes_data.json
```

## Institutional Account Setup

```bash
# Find your organization and folder ID
curl -H "Authorization: ApiKey YOUR_KEY" https://api.perma.cc/v1/organizations/
```

Use the `folder` parameter when creating archives:
```python
requests.post("https://api.perma.cc/v1/archives/", json={
    "url": url,
    "folder": FOLDER_ID,  # enables institutional limits
})
```

## Gate: Exit Archive

- [ ] All non-perma.cc URLs archived
- [ ] perma.cc links written to DOCX
- [ ] `scratch/permacc_archives.json` contains all mappings

## Next Phase

Read `${CLAUDE_SKILL_DIR}/../../../../skills/bluebook-audit/skills/audit-crossrefs/SKILL.md` and follow its instructions.
