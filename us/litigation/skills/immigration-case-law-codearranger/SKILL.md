---
name: immigration-case-law-codearranger
title: Immigration Case-Law Research (bundled MCP servers)
description: 'Use this skill for LIVE case-law or foreign-law research in immigration matters — routes to bundled free MCP servers (CourtListener and Legal Data Hunter) instead of citing from memory. Triggers: "find circuit case law on", "Ninth Circuit immigration", "petition for review precedent", "find BIA decisions", "Matter of", "verify this I&N Dec. cite", "asylum case law", "cancellation precedent", "particular social group cases", "find the federal docket", "country conditions law", "what is the law in [country]", "is [conduct] illegal in [country]", "foreign statute for my asylum claim". Routes circuit/Supreme Court/district-court authority and dockets to CourtListener; BIA precedent (I&N Dec.) to CourtListener + EOIR Virtual Law Library; AAO to USCIS reading room; country-of-origin law (100+ countries) to Legal Data Hunter. Enforces never-cite-from-memory and AG-certification check.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/claude-legal-immigration-laws/skills/immigration-case-law
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Immigration Case-Law Research (bundled MCP servers)

> **NOT LEGAL ADVICE.** This skill retrieves and organizes legal sources as a research and
> drafting aid; it does not evaluate whether an authority is good law on the user's facts and
> does not create an attorney-client relationship. Immigration consequences are severe and
> often irreversible — pair research with review by a licensed immigration attorney or
> EOIR-accredited representative.

## Purpose

This plugin snapshots the **rules** (INA, 8 CFR, 22 CFR, FAM) verbatim, but **case law is
on-demand** — [`../../references/legal-data-apis.md`](../../references/legal-data-apis.md)
indexes the sources, and the plugin bundles two free remote MCP servers (declared in
[`../../.mcp.json`](../../.mcp.json)) to serve that layer. **Never cite a case from memory**
— every cited authority must be retrieved and read before it enters a draft.

## Forum-aware routing

| Authority | Where to get it |
|---|---|
| **Circuit courts** (petitions for review under INA § 242 / 8 U.S.C. § 1252) and the **Supreme Court** | CourtListener MCP — court IDs `ca1`–`ca11`, `cadc`, `scotus`. The Ninth Circuit (`ca9`) carries the largest immigration docket; **circuit law is not uniform**, so always scope the search to the circuit where the petition lies (or the IJ sits) |
| **BIA precedent** (*Matter of …*, cited "I&N Dec.") | CourtListener indexes many BIA decisions (court ID `bia`); the **EOIR Virtual Law Library is the publisher of record** — confirm the precedent there, and check it has not been **certified to or overruled by the Attorney General** |
| **AAO** (USCIS appeals, non-precedent + adopted decisions) | Not on CourtListener — the USCIS decision reading room per `legal-data-apis.md` |
| **District courts** (habeas, APA / mandamus delay suits) and their **dockets** | CourtListener MCP — opinions + the RECAP/PACER docket collection (find the complaint, the government's response, the order) |
| **Country-of-origin law** — penal codes, statutes criminalizing the protected ground, family/nationality law, foreign case law | Legal Data Hunter MCP — multi-jurisdictional coverage of 100+ countries; often decisive for asylum (e.g., whether the applicant's conduct or identity is criminalized at home), and for nationality / statelessness questions |

## CourtListener playbook (immigration-flavored)

- **Search both section numbers.** Opinions cite the same provision as `INA § 240` or
  `8 U.S.C. § 1229a` inconsistently — search both forms (crosswalk in
  [`../../references/immigration-statutes/README.md`](../../references/immigration-statutes/README.md));
  never compute the offset.
- **Scope by court and date.** Pre-BIA-deference-era and pre-amendment cases mislead;
  filter by date when a provision was amended (e.g., post-REAL ID Act credibility law).
- **Read before citing** — use the document-reading tools to pull the opinion text and
  quote-check the holding; restrict response fields to what you need.
- **Citation verification** — run a draft's citations through the citation-lookup tools in
  bulk; the citation network (who cites this case) is a first-pass treatment check, **not**
  Shepard's/KeyCite. For load-bearing authority, recommend a citator check before filing.
- **Link** every retrieved case with its `courtlistener.com` URL next to the reporter cite.

## Legal Data Hunter playbook (country-of-origin law)

- Discover the country's available sources and filters first, then run scoped hybrid
  search; retrieve full text before quoting and cite inline with the document link.
- Pair foreign-law findings with the U.S. legal element they support (e.g., a penal-code
  section criminalizing the protected ground → the persecution / "particular social group"
  analysis; a nationality statute → derivative-citizenship or statelessness analysis).
- Foreign law in an asylum filing is **evidence**, not binding authority — present it as a
  documented country-conditions exhibit, translated where required, alongside (not instead
  of) State Department and NGO country reports.

## Output discipline

- Inline citation to a retrieved document for every legal claim; holding vs. dicta
  distinguished; operative language quoted, not paraphrased.
- Confidence flags: **GREEN** (retrieved, read, supports), **YELLOW** (partial/arguable
  support), **RED** (could not retrieve — do not cite). Hand the finished draft to
  `immigration-fact-check` for the four-pass audit before filing.
- Repeat the NOT LEGAL ADVICE disclaimer in any deliverable this research feeds.

## If the tools are missing

Both servers need a one-time sign-in (CourtListener: free account, OAuth; Legal Data
Hunter: GitHub/Google). If their tools are absent, tell the user to run `/mcp` and
authenticate — do not fall back to memory. Hard fallbacks: the REST sources indexed in
[`../../references/legal-data-apis.md`](../../references/legal-data-apis.md) and
[`../../references/online-sources.md`](../../references/online-sources.md).

## Composition

Finds and verifies authority for `circuit-petition-for-review` (circuit scoping +
exhaustion arguments), `bia-appeals` (BIA precedent + circuit law), `eoir-removal-defense`
(relief-eligibility case law + country-of-origin evidence), and
`eoir-motions-to-reopen-reconsider` (changed-country-conditions evidence). Runs before
`immigration-fact-check`, which audits the finished draft. The matter-neutral counterpart
for non-immigration research is `case-law-research` in `claude-legal-federal-laws`.
