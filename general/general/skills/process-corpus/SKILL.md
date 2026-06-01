---
name: process-corpus
title: Process corpus
description: Process the ARLIS legal corpus from raw JSONL to cleaned format. Use when preparing or updating the legal article dataset.
author: davitsargsyan0
author_url: https://github.com/davitsargsyan0/ar-lex_graph/tree/dev/.agents/skills/process-corpus
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

Process the ARLIS corpus:

1. Check data sources:
   - data/raw/arlis_docs.jsonl (full 23GB dump) OR
   - data/raw/arlis_docs_metadata.jsonl (metadata only)
   Report which is available and record count.

2. Run the processor:
   python scraper/corpus_processor.py

3. Run the amendment extractor:
   python scraper/amendment_extractor.py

4. Validate output:
   - Count articles in data/processed/statutes_clean.jsonl
   - Count relationships in data/processed/relationships.jsonl
   - Print hierarchy_level distribution
   - Print status distribution
   - Spot-check: print 3 random articles (title + first 100 chars)

5. Success criteria: ≥500 articles, ≥100 relationships

If criteria not met, diagnose which category is under-represented and suggest fixes.
