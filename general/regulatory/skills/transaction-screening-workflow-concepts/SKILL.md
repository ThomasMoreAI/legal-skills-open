---
name: transaction-screening-workflow-concepts
title: Transaction screening workflow (concepts)
description: Educational map of transaction-centric compliance screening—transfer as the atomic unit, deposit vs withdrawal direction, single and CSV import, transaction list and detail views, per-transfer screening, rescreen, and STR-style exports. Use when the user asks how monitoring UIs treat tx hashes, directions, or regulatory reporting hooks—not for legal filing advice or evading reporting.
author: NeverSight
author_url: https://github.com/NeverSight/learn-skills.dev/tree/main/data/skills-md/agentic-reserve/blockint-skills/transaction-screening-workflow-concepts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# Transaction screening workflow (concepts)

**Educational reference only.** Limits (batch sizes, engines, STR formats) change by **product** and **jurisdiction**—confirm in **phalcon-compliance-documentation** and your compliance program. Pair with **address-screening-workflow-concepts** (wallet inventory) and **risk-exposure-screening-concepts** (how **direction** affects participant and flow rules).

## Unit of analysis

- The **smallest** screening unit is often a **single transfer** (asset movement from **from** → **to** within a tx).
- One **transaction** (one hash) may contain **many** transfers. Products may let you screen **each** transfer, **subset**, or roll up to **transaction-level** risk—behavior varies by vendor.

## Direction (deposit vs withdrawal)

Setting **Deposit** vs **Withdrawal** steers **which** rules and **which** side of the flow the engines emphasize:

| Direction | Typical screening focus |
|-----------|-------------------------|
| **Deposit** | **Inflow** to the platform/customer relationship—provenance of funds **arriving**. |
| **Withdrawal** | **Outflow** and **destination**—where funds **leave** toward. |

Common product behavior (verify in docs):

- Rules can be **scoped** to one direction (for example deposit-only policies do **not** run on withdrawal-labeled items).
- If **no** direction is set, some products default to **running both** deposit- and withdrawal-oriented passes to reduce misconfiguration.
- Correct direction is used to **tune** rules and **reduce false positives**—it is an **operational** control, not a legal classification.

This aligns with participant/flow screening notes in **risk-exposure-screening-concepts**.

## Labels

**Labels** are user-defined strings for **organization** and **case context** on a **transaction** or **transfer** (distinct from address **tags/markers** in **address-screening-workflow-concepts**).

## Import methods

1. **Single transaction hash** — Paste a hash; the product **fetches** parsed transfers; you **select** which transfer(s) to screen and attach **direction**, **labels**, and **customer** linkage.
2. **Bulk CSV** — Template-driven import of many rows (batch size caps are **product-specific**—on the order of **hundreds** per file in some docs).

Typical **CSV-style** columns (names vary):

| Field | Purpose |
|-------|---------|
| Chain | Network identifier per template |
| Transaction hash | On-chain tx id |
| Label | Optional private label |
| Direction | Optional `Deposit` / `Withdrawal` |
| Customer ID | Optional internal customer key |
| Transfer From / Transfer To | Optional pair to **disambiguate** one transfer inside a multi-transfer tx |

Review **per-row** import outcomes in the UI.

## Transaction list

Lists commonly show: hash, **risk summary**, **screening direction**, **open alerts**, **last screened**, **notional** (often USD), **token amount**, **asset**, **from/to**, **timestamp**, **customer**, **labels**, **added** time. Multi-transfer rows may **collapse** with **expand** to child transfers.

## Transaction details page

Typical sections:

- **Basic information** — Asset, time, labels, customer, etc.
- **Risk summary** — Rolled-up alert view.
- **Risk overview** — Finer breakdown: risk categories, exposure-style charts, exposed address lists, **fund-flow** narrative; products may link to an **external graph** or **trace** tool where integrated.
- **Token transfers** — **Graph** plus **tabular** list of each transfer; **per-transfer** alerts; **unscreened** legs may be screenable on demand.
- **Transfers overview** — Compact index with shortcuts into each transfer.
- **Alerts** — Filterable list.
- **Audit log** — **Comments** and **system events** (same idea as address workflow).

**Rescreen** — Re-run screening for the **whole** transaction or a **specific** transfer; **direction** may be set per run.

## STR-style and regulatory exports

Some products expose **Suspicious Transaction Report (STR)** or regional equivalents:

- **Region** selection matters—**formats** and **fields** differ by jurisdiction.
- **Direction** is often a **prerequisite** for valid STR generation in the product model.
- Reports may be generated **per transfer** when policy requires **transfer-level** suspicious activity narratives.

**Not legal advice.** STR obligations depend on **local law** and **institutional** policy; use qualified **compliance** and **legal** review for filings.

## Deleting a transaction

Removing a transaction record typically deletes **associated transfers** and **expires** related **alerts** **in the product**. Public-chain data **remain** on explorers.

## Guardrails

- **Do not** paste **live** production tx hashes tied to identifiable customers into **public** channels.  
- **Do not** assist with **structuring** flows to **evade** monitoring or **mis-labeling** direction.  
- STR and **travel rule** questions need **program-specific** guidance beyond generic skills.

## See also

- **address-screening-workflow-concepts** — wallet inventory, tags/markers, blacklist/whitelist.  
- **behavioral-risk-screening-concepts** — velocity and amount heuristics that may surface at transfer level.

**Goal:** a portable mental model of **transaction** screening UIs and **direction** semantics aligned with common compliance products, without binding a specific **vendor** implementation.
