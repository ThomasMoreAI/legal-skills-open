---
name: bailii-case-law
title: BAILII Case Law Research
description: 'Search BAILII for UK case law and retrieve full judgment text. Use when

  someone asks to find a case, search for case law on a topic, read a

  judgment, or check how courts have ruled on an issue. Covers UKSC, EWCA,

  EWHC, Upper Tribunal, EAT, and more. Requires the BAILII MCP server

  running locally (BAILII blocks cloud IPs).'
author: paulieb89
author_url: https://github.com/paulieb89/bouch-mcp-skills/tree/main/bailii-case-law
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: litigation
language: en
---

# BAILII Case Law Research

Search UK case law on BAILII and retrieve full judgment text. Find how courts have ruled on a topic, extract key principles, and cite properly.

## Thinking Like a Researcher

The user has a legal question and needs to know what the courts have said. They might be a solicitor checking a point, a barrister preparing submissions, a paralegal building a research note, or a law student writing an essay. They want:

1. **Which cases matter?** Not every result is relevant. A Supreme Court decision outweighs a First-tier Tribunal case. Recent authority outweighs old unless it's a foundational case.
2. **What did the court actually say?** The ratio decidendi, not the full 50-page judgment. Extract the principle in 1-2 sentences.
3. **How does it apply to their question?** Connect the case to the issue. "This case established that..." not just "This case exists."

## Court Hierarchy

Weight results by court level:

- **UKSC / UKHL** — Supreme Court / House of Lords — binding on all lower courts
- **EWCA** — Court of Appeal — binding on High Court and below
- **EWHC** — High Court — persuasive, not binding on other High Court judges
- **UKUT** — Upper Tribunal — authoritative in its jurisdiction
- **EAT** — Employment Appeal Tribunal — authoritative for employment law
- **UKFTT** — First-tier Tribunal — lowest weight, useful for seeing how rules are applied in practice

A single UKSC decision is worth more than ten UKFTT decisions. Say so.

## How to Work

**Search first.** Use `bailii_search` with the legal topic. Be specific — "landlord HMO licensing rent repayment order" will give better results than just "landlord." If the first search is too broad, narrow it.

**Pick the best 3-5 cases.** Prioritise by court level, then recency. A 2024 Court of Appeal decision is more useful than a 2026 First-tier Tribunal decision on the same point.

**Pull the judgment** on the most important case using `bailii_get_judgment`. The full text will be long — don't reproduce it all. Read it, extract the key paragraphs, and summarise the ratio.

**Don't pull every judgment.** Full judgments are large (30-100KB each, 15-25K tokens). Pulling more than 2 will exhaust the context window before you can analyse anything. Pull 1 key judgment, summarise the rest from the search snippets and titles. The user can read the full text themselves via the BAILII URL.

**When you do pull a judgment,** focus on extracting the key sections (Summary, Held, Ratio, Conclusions) rather than reproducing the entire text in your response. The tool gives you the full text so you can read it — the user needs your analysis, not the raw judgment pasted into the chat.

## When Things Go Wrong

- **No results:** Try different search terms. Legal language is specific — "unfair dismissal" not "fired unfairly", "negligence" not "accident."
- **Too many irrelevant results:** Add court-specific terms or party names to narrow the search.
- **Judgment text is very long:** Focus on the Summary, Held, and Conclusions sections. Skip procedural history unless the user specifically needs it.
- **Old cases:** Still cite them if they're the leading authority. Note the date and whether the law has changed since.

## Good vs Bad Output

**Good:** Cites cases with neutral citations. States the court level. Extracts the ratio in 1-2 sentences. Notes whether the case is binding or persuasive. Provides BAILII URLs for the user to read the full text.

**Bad:** Lists every search result without filtering by relevance. Quotes paragraphs of judgment text without explaining why they matter. Misses the court hierarchy. Cites a tribunal case as if it were binding authority.

## Formatting

Neutral citations in square brackets: [2026] EWCA Civ 35. Court name in full on first mention, abbreviated thereafter. British spelling. Always include the BAILII URL so the user can verify. Always state: legal research, not legal advice.
