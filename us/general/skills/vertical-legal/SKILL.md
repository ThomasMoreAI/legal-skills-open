---
name: vertical-legal
title: /vertical-legal
description: Pre-configured legal vertical pack for the ai-brain-starter substrate. Ships typed-memory categories for matter management and privilege handling, retention defaults aligned with ABA Model Rule 1.15 and state-bar variations, and connector configurations for Clio, NetDocuments, and iManage. Use when onboarding a law firm, in-house legal department, or legal-ops team that needs the substrate to come pre-shaped to the work rather than starting from a blank vault.
author: adelaidasofia
author_url: https://github.com/adelaidasofia/ai-brain-starter/tree/main/skills/vertical-legal
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: general
language: en
---

# /vertical-legal

A pre-configured pack that turns the empty substrate into a legal-ready system in one install. The pack ships typed-memory categories that match how a matter actually moves, connectors for the three platforms most firms already pay for, retention defaults that map to the ABA Model Rules, and decision-audit patterns for privilege handling and conflicts checks.

## Why this exists

A blank install of the substrate forces every legal team to invent the same vocabulary on day one: what is a matter, what is a privileged document, what is a conflicts check, how long do we keep depositions. The vocabulary is not novel. Every firm in North America runs roughly the same primitives, with the same retention obligations, against roughly the same three document management platforms.

This pack ships the primitives so the firm can spend day one on what is actually theirs (their playbooks, their authority chain, their client list) instead of re-deriving the category structure.

## What this pack sets up

Run `/vertical-legal init` and the pack writes:

| Layer | What ships | Where it lands |
|---|---|---|
| Schema | 8 typed-memory categories with frontmatter contracts | `schema/typed-memory-categories.md` |
| Connectors | Clio, NetDocuments, iManage specs and OAuth flows | `connectors/*.md` |
| Retention | Per-category retention rules mapped to ABA Model Rule 1.15 and state variations | `retention/defaults.md` |
| Decision audit | Privilege-handling guardrails and conflicts-check pattern | `decision-audit/*.md` |

Nothing is auto-applied to a live install. The pack stages drafts under `drafts/` and prints the path; the firm reviews and accepts before merging into the production memory layer.

## Categories shipped

- matter
- client
- opposing-counsel
- privilege-tagged-doc
- retention-policy
- billing-event
- deposition-note
- court-deadline

See `schema/typed-memory-categories.md` for required and optional frontmatter on each.

## Connectors shipped

- `connectors/clio.md` — Clio API, OAuth2, per-firm key, sync cadence, write-back rules
- `connectors/netdocuments.md` — NetDocuments REST and ndOffice API
- `connectors/imanage.md` — iManage Work API and Work Server REST

## Retention defaults shipped

Mapped against ABA Model Rule 1.15 and the most common state-bar variations. See `retention/defaults.md` for the table. Highlights:

- Privileged matter documents: matter close + 7 years (most jurisdictions), longer in jurisdictions with extended client-property rules.
- Billing events: matter close + 7 years (federal tax baseline plus most state-bar minimums).
- Depositions and trial transcripts: matter close + 10 years (most appellate windows plus malpractice statutes of repose).
- Court deadlines: retained through matter close, then archived alongside the matter file.

## Decision-audit patterns shipped

- `decision-audit/privilege-handling.md` — privileged documents cannot leave the matter scope; any agent action that would expose privileged content blocks at write time and surfaces a recoverable error to the operator. Every privilege-related read and write is logged with the matter ID, the requesting role, and the disposition.
- `decision-audit/conflicts-check.md` — every new client adds to the conflicts graph; every new matter checks the conflicts graph at intake and blocks if a conflict is detected.

## When to use this pack

- A law firm or in-house legal team is installing the substrate for the first time.
- An existing install needs to bring on a legal practice as a new tenant or workspace.
- A firm wants the pack as a reference even if they intend to customize heavily; the categories and retention table are useful as a starting frame.

## When NOT to use this pack

- Pure compliance or regulatory-affairs work without matter management. Use the finance pack or roll your own categories.
- Government or public-sector legal work where FOIA and classified handling dominate. Use the public-sector pack instead, or layer this pack with the public-sector pack for a hybrid.
- Pure document-review or e-discovery work. The pack assumes matter management at its center; review-only workflows would use a thinner subset.

## Install

```bash
/vertical-legal init
```

The init command:

1. Verifies the substrate is installed and at a compatible version.
2. Stages all schema, connector, retention, and decision-audit files under `drafts/legal/`.
3. Prints a review checklist.
4. Stops. The firm reviews and merges manually.

## Status

```bash
/vertical-legal status
```

Reports which categories are live, which connectors have been configured with credentials, and which retention rules have been overridden locally.

## What this pack does NOT include

- Specific firm playbooks (every firm writes its own).
- Specific client or matter data (the pack is a schema, not a content set).
- Trust accounting workflows (out of scope for v1; the billing-event category is a hook for future trust accounting integration).
- E-discovery and review platforms (Relativity, Everlaw, Reveal). A future pack may layer on these; for v1, treat e-discovery as a downstream system that consumes from the matter scope.
- Practice management beyond the three connectors named. Firms on Smokeball, PracticePanther, MyCase, or CosmoLex can adapt the Clio connector spec as a starting point.

## Provenance

Every retention default in `retention/defaults.md` cites the rule it maps to. Every connector spec cites the official API documentation URL and the auth scheme. Every decision-audit pattern cites the regulatory or ethical rule it enforces. Drafts without provenance are a bug; surface them as gaps in the firm's review pass rather than guessing.
