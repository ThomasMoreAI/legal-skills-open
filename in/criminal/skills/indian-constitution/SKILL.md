---
name: indian-constitution
title: Indian Constitution + BNS Lawyer Skill
description: Query Indian Constitution articles and BNS 2023 (Bharatiya Nyaya Sanhita) criminal law sections using RAG with semantic search. Look up fundamental rights, directive principles, emergency provisions, and BNS offences with cited article/section numbers. Use when the user asks about Indian law, constitutional articles, fundamental rights, BNS sections, IPC equivalents, or legal questions about India.
author: ankitjh4
author_url: https://github.com/ankitjh4/indic-ai-skills/tree/main/skills/indian-constitution
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: in
practice: criminal
language: en
---

# Indian Constitution + BNS Lawyer Skill

RAG-based legal assistant for Indian constitutional law and BNS 2023 criminal law.

## Quick Start

```bash
# Query Constitution
python3 scripts/query.py "What are fundamental rights?"

# Query BNS
python3 scripts/query.py "What is Section 103 BNS?"

# Get more results
python3 scripts/query.py "Emergency provisions" -k 10
```

## Workflow

1. **Query** — run `python3 scripts/query.py "<question>"` with a natural-language legal question
2. **Review citations** — responses include Article/Section numbers; verify against official sources
3. **Refine** — use `-k 10` (or higher) if the initial results miss the relevant provision
4. **Cross-reference** — query both Constitution and BNS terms when a question spans civil and criminal law

## What You Can Ask

### Constitutional Law
- "What are fundamental rights under Part III?"
- "How is the President elected?"
- "Emergency provisions in Constitution"
- "Article 370 and special status"

### BNS 2023 (Replaced IPC)
- "What is punishment for murder under Section 103 BNS?"
- "Hate speech laws in BNS"
- "Sedition under Section 150 BNS"
- "Domestic violence sections in BNS"

## Data Coverage

| Document | Details |
|----------|---------|
| **Constitution of India** | 402 pages, 395 Articles (as of July 2024, 106th Amendment) |
| **BNS 2023** | 102 pages, 358 Sections (effective July 1, 2024) |
| **Total Corpus** | 1.27M characters, 2,265 chunks |
| **Embedding** | all-MiniLM-L6-v2 (384 dim), ChromaDB, cosine similarity |

## Important Notes

1. **Not Legal Advice** — this skill provides legal information, not professional counsel.
2. **Citations** — all responses include relevant Article/Section numbers for verification.
3. **Source** — Constitution text from https://cdnbbsr.s3waas.gov.in/
