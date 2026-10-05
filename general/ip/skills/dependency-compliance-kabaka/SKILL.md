---
name: dependency-compliance-kabaka
title: Dependency Compliance (license & SBOM mechanics)
description: Use when checking a dependency's license, license compatibility, copyleft obligations, generating or reading an SBOM, SPDX identifiers, or whether a package's provenance/existence is trustworthy before adding it. Covers permissive vs weak/strong copyleft tiers, Apache NOTICE/patent terms, AGPL's network reach, SPDX IDs, SBOM (SPDX/CycloneDX) over direct AND transitive deps, lockfile pinning and advisory/provenance hygiene, and the AI-specific risks of license laundering and hallucinated/typosquatted ("slopsquatted") packages. This skill owns LICENSING / SPDX / SBOM / copyleft COMPLIANCE mechanics. Do NOT use for vulnerability or threat assessment, CVEs, malicious packages, or supply-chain ATTACK — that is `security-review`. Mechanics only; not legal advice.
author: kabaka
author_url: https://github.com/kabaka/ai-dlc/tree/main/product/.claude/skills/dependency-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# Dependency Compliance (license & SBOM mechanics)

This skill is the **licensing / SBOM / copyleft compliance** lens for the
dependencies in your project. It describes the **mechanics** of evaluating a
package's license, compatibility direction, copyleft obligations, and provenance so
the human arbiter can make an informed call.

> **This is not legal advice.** License compatibility and AI-generated-code
> provenance are unsettled and contested areas of law; consult counsel for binding
> determinations. This skill describes **mechanics only**; the human arbiter
> decides what to ship. Never assert "license X is safe to combine with Y" as a
> conclusion — surface the obligations and let the arbiter (and counsel) decide.

## Boundary — what this skill is NOT

This skill owns **LICENSING / SPDX / SBOM / copyleft COMPLIANCE**. It is the
*obligations and provenance* lens.

- **Do NOT use for vulnerability or threat assessment — that is `security-review`.**
  CVEs, known-malicious packages, install-time exploit scripts, and supply-chain
  *attack* are exploitability questions owned by `security-review` and the
  `security` agent.
- The two lenses meet at "adding a dependency": ask **both** "may I legally use and
  combine this?" (here) and "could this be exploited or is it malicious?"
  (`security-review`). Run them as two separate passes; do not conflate them.

## License tiers (obligations rise left to right)

Compatibility is **directional and pairwise** — "A may include B" does not imply
"B may include A," and a verdict for one pair says nothing about a third package.
Always reason about a specific direction and the *combined* distribution.

| Tier | Examples | Core obligation (mechanics, not advice) |
| --- | --- | --- |
| **Permissive** | MIT, BSD-2/3-Clause, Apache-2.0 | Minimal: preserve copyright + license text. **Apache-2.0** adds an explicit **patent grant** and requires propagating any **`NOTICE`** file. |
| **Weak copyleft** | LGPL, MPL-2.0 | Obligations are **scoped to the licensed component/files**: changes to *that* component are shared back, but merely using/linking it generally does not subject your own code to copyleft. |
| **Strong copyleft** | GPL-2.0/3.0, **AGPL-3.0** | **Derivative-work source obligations**: distributing a work built on it can require offering the combined source under the same terms. **AGPL extends the trigger to network/SaaS use** — providing access over a network counts as conveying, so server-side use can carry the obligation. |

- "Compatible" means a specific combination's obligations can be simultaneously
  satisfied in a specific direction — it is a per-pair, per-direction question.
- Dual-licensed or `OR`-expression packages let the consumer pick a tier; record
  which option you are relying on.

## SPDX identifiers and the SBOM

- **SPDX license identifiers** are the machine-readable IDs for licenses (e.g.
  `MIT`, `Apache-2.0`, `AGPL-3.0-or-later`) plus expression operators (`OR`,
  `AND`, `WITH`). Prefer the SPDX ID over a free-text license name; it is what
  tooling and policy allowlists match on.
- An **SBOM** (Software Bill of Materials) is the inventory of every component and
  its license, in a standard format — **SPDX** or **CycloneDX**. A useful SBOM
  covers **direct AND transitive** dependencies; a transitive strong-copyleft or
  unknown-license package is the common surprise, so the full tree is the unit of
  analysis, not the top-level manifest.
- **Provenance / supply-chain hygiene** underpins trust in the SBOM (high level):
  **pin** dependencies via a committed lockfile; scan against advisory databases;
  and where available capture **provenance / SLSA** attestations tying an artifact
  to the source and build that produced it.

## AI-specific risks (why this matters in an AI workflow)

An AI-driven workflow introduces two failure modes a human-only one largely avoids:

- **License laundering.** An assistant can emit **near-verbatim snippets** of
  training-data code with the original attribution and license obligations
  **stripped**, so copyleft or attribution requirements silently ride into your
  codebase without an SPDX trail. Treat generated code that resembles a known
  project as a provenance question, not just a quality one.
- **Hallucinated / typosquatted ("slopsquatted") dependencies.** An assistant may
  confidently suggest a package that **does not exist** — or whose plausible name
  is **squatted** by a malicious lookalike. This is why an **automated
  license + existence check at dependency-add** matters specifically here:
  the human never typed the name, so "does this package actually exist, from the
  expected source?" must be verified before it lands.

## Recommended checks (two points, NON-BLOCKING)

> These are **recommended, non-blocking** checks. They inform the arbiter's
> decision at an **existing** gate; they do **not** add a gate of their own.
> **AI-DLC ships exactly four blocking arbiter gates** (Inception → Construction;
> the design fork; Construction → merge; → Operations deploy/release) and **these
> additions do not change that** — they are inputs inside the relevant checklist,
> surfaced for the human, never a blocker the tooling enforces.

1. **At dependency-add** — license + provenance + **existence** check against the
   project's policy **allowlist / denylist**: resolve the package's SPDX license,
   confirm it actually exists from the expected source/registry (counters
   slopsquatting), and surface any tier mismatch with policy. Nests inside the
   `security-review` supply-chain lens as a recommended item.
2. **Pre-release** — **SBOM generation** (SPDX or CycloneDX) + a **full-tree
   license scan** across direct and transitive deps, surfaced on the
   `delivery-operations` pre-deploy checklist.

The arbiter may still *choose* to treat a finding as decisive at an existing gate —
that is the human deciding, not a new automated gate.

## How to report

State, per dependency or per scan: the **SPDX license** (or expression), its
**tier**, the **specific obligations** triggered by *your* intended use and
distribution direction, **provenance/existence** status, and whether it matches the
project policy. **Surface obligations; do not pronounce legal verdicts.** End by
reminding the arbiter this is mechanics, and that combinability and AI-provenance
questions may warrant counsel.

## Cross-references

- **`security-review`** — the exploitability / threat lens (CVEs, malicious
  packages, supply-chain attack). The complementary pass at dependency-add; this
  skill does **not** cover it.
- `delivery-operations` — hosts the pre-release SBOM/license checklist item.
- `aidlc-workflow` — the four arbiter gates these checks feed (without adding one).
