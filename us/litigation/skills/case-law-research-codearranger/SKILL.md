---
name: case-law-research-codearranger
title: Case-Law Research (bundled MCP servers)
description: 'Use this skill whenever a matter needs LIVE legal research — case law, dockets, judges, or law outside the snapshotted corpora — via the bundled free CourtListener and Legal Data Hunter MCP servers, never from memory or generic web search. Triggers include "find case law", "cases on point", "is there precedent for", "what did the court hold in", "look up this opinion", "verify this citation", "is this case real", "cite-check", "is this still good law", "shepardize", "negative treatment", "who cites this case", "check the docket", "PACER", "RECAP", "research the judge", "oral argument recording", "foreign law", "law in [country]". Routes U.S. case law and dockets to CourtListener, non-U.S. and multi-jurisdictional law to Legal Data Hunter. Cardinal rule: never cite a case from memory — quote-check every holding against retrieved text.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/claude-legal-federal-laws/skills/case-law-research
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Case-Law Research (bundled MCP servers)

> **NOT LEGAL ADVICE.** This skill retrieves and organizes legal sources as a research and
> drafting aid. It does not evaluate whether an authority is good law on the user's facts and
> does not create an attorney-client relationship. Verify everything against the primary source
> before relying on or filing anything.

## Purpose

The marketplace deliberately snapshots **rules** (statutes, regulations, court rules) verbatim
in each plugin's references corpus, but **case law is never snapshotted** — it is too large and
moves too fast. This skill is the live-lookup layer. This plugin bundles two free remote MCP
servers (declared in [`../../.mcp.json`](../../.mcp.json)), and because every state plugin
depends on this plugin, they are connected anywhere any claude-legal plugin is installed:

| Server | Use it for |
|---|---|
| **CourtListener** (`https://mcp.courtlistener.com/`, Free Law Project) | U.S. case law (federal + all 50 states), RECAP/PACER federal dockets and filings, judges, oral arguments, citation verification |
| **Legal Data Hunter** (`https://legaldatahunter.com/mcp`) | Multi-jurisdictional research — statutes, regulations, case law, and doctrine across 100+ countries; jurisdictions or source types the snapshotted corpora and CourtListener don't cover |

**The cardinal rule: never cite a case from memory.** A case name + reporter cite produced
from the model's weights is a hallucination risk; courts sanction filers for it. Every cited
case must be retrieved through one of these servers (or a canonical fallback) and its
relevant language read before it goes into a draft.

## Research order of operations

1. **Snapshot first.** If the question is about a statute, regulation, or court rule already
   mirrored in an installed plugin's `references/` corpus (RCW, ORS, CCP, C.R.S., CPLR,
   Tenn. Code Ann., MCL, A.R.S., R.C., the federal corpora here, etc.), cite the verbatim
   snapshot — that's what it's for.
2. **CourtListener for U.S. case law and dockets.** Anything decided by a U.S. court.
3. **Legal Data Hunter for everything else** — non-U.S. law, jurisdictions not snapshotted,
   doctrine/commentary, or cross-border comparison.
4. **Canonical fallbacks** if a server is unavailable (see "If the tools are missing" below
   and the installed state plugin's `legal-data-apis.md`).

## CourtListener playbook

The server exposes search plus full REST-endpoint access. The high-value moves:

- **`search`** — the entry point. Collections: **opinions** (case law), **RECAP**
  (federal dockets/filings from PACER), **judges**, and **oral arguments**. Filter by court,
  date, and citation. Court identifiers are CourtListener court IDs (`scotus`, `ca1`–`ca11`,
  `cadc`, `cafc`, district courts like `wawd`, state courts like `wash` / `washctapp` /
  `cal` / `ny` / `ohio`); when unsure, discover them via the courts endpoint or the server's
  choices tool rather than guessing.
- **`read_document` / `search_document`** — read an opinion's or filing's text (paginated,
  greppable). Use these to quote-check; do not paste reporter quotes from memory.
- **Citation tools** — extract citations from a draft and look them up in bulk to confirm
  each resolves to a real case; use the citation network (what cites this case) as a
  first-pass treatment check.
- **Field discipline** — responses can be enormous; always restrict to the fields you need.
  Don't fetch PDFs; use the document-reading tools.
- **Linking** — cite retrieved cases with their `courtlistener.com` URL alongside the
  reporter cite so a human can verify in one click.

**Treatment caution:** CourtListener's citation network shows *who cites a case*, not
editorial negative-treatment analysis. It is **not** Shepard's or KeyCite. If a case is
load-bearing, say so and recommend the user confirm treatment in a citator before filing.

## Legal Data Hunter playbook

- **Discover before searching** — list available countries/sources/filters first when
  working outside familiar territory, then run hybrid semantic + keyword `search` scoped by
  country, source, and court level.
- **`get_document`** retrieves the full text; **`resolve_reference`** turns a bare citation
  into its document. Quote only from retrieved text.
- Best fits: foreign and comparative law, statutes/regulations of jurisdictions the
  marketplace doesn't snapshot, doctrine, and multi-jurisdiction surveys (e.g., "how do
  other states treat X").
- Cite **inline**, in the sentence where the claim appears, with the document link.

## Output discipline

- Every legal claim in the research output carries an inline citation to a retrieved
  document (CourtListener URL or Legal Data Hunter document link).
- Distinguish **holding** from **dicta** from **procedural posture**; quote the operative
  language rather than paraphrasing it.
- Flag confidence: **GREEN** (retrieved, read, supports the proposition), **YELLOW**
  (retrieved but support is partial/arguable), **RED** (could not retrieve — do not cite).
  Hand RED/YELLOW items to the state's `*-fact-check` skill before anything is filed.
- When research feeds a filing, repeat the NOT LEGAL ADVICE disclaimer in the deliverable.

## If the tools are missing

Both servers require a **one-time sign-in**: CourtListener uses OAuth with a free
CourtListener account; Legal Data Hunter uses GitHub/Google sign-in. If their tools are not
available in the session, tell the user to run `/mcp` in Claude Code and complete
authentication — do not silently fall back to memory. Hard fallbacks: CourtListener's REST
API (token-based) and the per-state `legal-data-apis.md` index of official sources.

## Composition

Composes with every state plugin's `*-fact-check` skill (this skill finds and verifies
authority; fact-check audits the finished draft), the `*-consumer-debt` and other
subject-matter bundles (which describe what to search for), the consumer FCRA skills in this
plugin, and `immigration-case-law` in `claude-legal-immigration-laws` (the
immigration-flavored counterpart).
