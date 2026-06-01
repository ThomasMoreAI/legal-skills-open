---
name: search
title: Legislation Knowledge Search
description: Search legislation text and knowledge base using semantic similarity under any supported legislation
author: rob-otix-ai
author_url: https://github.com/rob-otix-ai/lexius/tree/main/plugin/skills/search
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# Legislation Knowledge Search

Search regulation text, obligations, and FAQ answers semantically across any supported legislation.

## Instructions

1. Determine the target legislation:
   - If `$ARGUMENTS` contains a legislation hint (e.g. "eu-ai-act", "cima-aml", "dora"), use that.
   - Otherwise, call `legalai_list_legislations` to retrieve the list of available legislations and ask the user which one to search, or offer to search across all of them.

2. Ask the user what they want to know. Accept natural language questions.

3. Determine the best search strategy:
   - If asking about a specific article number or reference, use `legalai_get_article` directly with the chosen `legislationId`
   - If asking a general question, first try `legalai_answer_question` with the chosen `legislationId` (FAQ search)
   - If FAQ doesn't match well, use `legalai_search_knowledge` with the chosen `legislationId` and the appropriate entity type:
     - "article" for regulation text
     - "obligation" for requirements
     - "faq" for common questions
     - "risk-category" for classification details

4. Present results with:
   - The matched content
   - Article references
   - Official source links (e.g. EUR-Lex for EU legislation, regulatory body publications for CIMA legislation) for verification
   - Similarity scores (for semantic results) to indicate confidence

5. If the user's question spans multiple topics, run multiple searches and synthesise the results.

6. Always encourage the user to verify against the official legislation text via the provided source links.

7. If the search reveals obligations or risk classifications relevant to the user's situation, offer to run `/lexius:classify` or `/lexius:compliance` for a deeper analysis.
