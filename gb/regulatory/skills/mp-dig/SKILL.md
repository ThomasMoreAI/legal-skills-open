---
name: mp-dig
title: MP Dig
description: 'Investigate a UK Member of Parliament. Pulls financial interests, voting

  record, Hansard contributions, and cross-references with Companies House.

  Use when someone asks "dig into my MP", "what are their interests",

  "how did they vote on X", "who funds them", or names a specific MP.

  Requires UK Legal MCP and UK Due Diligence MCP servers.'
author: paulieb89
author_url: https://github.com/paulieb89/bouch-mcp-skills/tree/main/mp-dig
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: regulatory
language: en
---

# MP Dig

Investigate a UK Member of Parliament using official public registers. Financial interests, voting record, parliamentary contributions, and corporate connections.

The data here comes from the Parliament Members API, the Register of Members' Financial Interests, Hansard, Commons and Lords division records, and Companies House. Every finding is from a public register. Present facts, not opinions. The user draws their own conclusions.

## How to Work

**Find the member.** Use `parliament_find_member` with the MP's name and note the integer member ID. Everything else depends on it. If the user gives a constituency rather than a name, search more broadly — some members use informal names.

**Pull their interests.** `parliament_member_interests` with the member ID covers employment and earnings, donations and sponsorship, gifts and hospitality, overseas visits, land and property, and shareholdings. These are legally required disclosures. Group by category in your output.

**Check voting record if asked about a specific issue.** Use `votes_search_divisions` with a topic keyword, then check whether this member voted. Distinguish between "voted against", "voted for", and "no recorded vote" — absence is different from opposition.

**Search Hansard for what they've said.** `parliament_member_debates` with a topic filter shows their actual words in Hansard. Recent contributions carry more weight than old ones.

**Cross-reference company interests on Companies House.** When a company appears in the interests register, pull the profile: is it active? Are filings current? Who else is a director? Any Gazette notices?

## When Things Go Wrong

- **Member not found:** Try surname only, or the constituency. Some members use informal names (e.g. "Keir" vs "Sir Keir Starmer").
- **No interests registered:** Either genuine or not updated. Note which and check the date of last update if available.
- **No votes on topic:** The topic may not have come to a division, or the member may have been absent. State this clearly.
- **Company not on Companies House:** May be an overseas entity, a partnership, or a trading name rather than a registered company.

## Formatting

Full name with title on first mention. Party and constituency on first mention. Amounts in GBP. Dates as DD Month YYYY. Company numbers as 8-digit zero-padded. Neutral tone throughout. Always state: information from official public registers.

## Files in this skill

- `references/parliament-registers.md` — what each parliamentary data source covers and its limitations
- `assets/mp-report-format.md` — output format template with section structure and good examples
