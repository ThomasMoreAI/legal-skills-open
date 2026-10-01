---
name: legal-readiness-broomva
title: Legal readiness
description: 'Build or adversarially audit an evidence-first legal-readiness system for a

  software product, SaaS, AI app, API, marketplace, or website. Inventory every

  public and contractual claim; determine jurisdiction, operator, customer,

  data-role, payment-channel, and product-behavior applicability; compare prose

  with repository, live, vendor, registry, contract, and operational evidence;

  close authorized code/documentation gaps; and leave counsel, tax, filing,

  entity, and external-account blockers explicit. Use when asked for a legal

  audit, legal shield, SaaS legal baseline, terms/privacy/consent/payment review,

  compliance gap analysis, legal readiness, legal standing setup, product-claim

  substantiation, or to make an app legally safer before launch. NOT FOR giving

  legal advice, declaring a product compliant or legally secure, forming an

  entity, filing registrations or taxes, signing contracts, inventing operator

  facts, or replacing licensed counsel.'
author: broomva
author_url: https://github.com/broomva/skills/tree/main/skills/governance/legal-readiness
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
sources:
- title: Issue Areas
  path: references/issue-areas.md
- title: Manifest Schema
  path: references/manifest-schema.md
---

# Legal readiness

Treat legal readiness as an evidence system, not a page-writing exercise. A
route, clause, checkbox, header, vendor, or incorporated entity is one control;
none proves overall compliance or guarantees a liability shield.

## Boundary

You may identify issues, implement authorized product controls, correct claims,
and organize evidence. You may not issue a legal opinion or represent that code
creates corporate legal standing. Formation, good standing, tax status,
registrations, enforceability, territorial scope, and final legal documents
remain factual and professional gates.

Do not commit legal advice, privileged communications, raw personal data, or
secrets into the manifest. Record a sanitized conclusion, confidential document
ID, digest, date, and authorized verifier; counsel decides what is privileged.

For current law, browse official primary sources. Treat blog posts, vendor
marketing, model memory, and prior audit prose as leads. Never hardcode a
jurisdictional conclusion without its factual predicate.

## Working modes

Choose the narrowest mode that covers the request:

1. **Inventory** — enumerate claims, surfaces, jurisdictions, roles, channels,
   and evidence without changing the project.
2. **Adversarial audit** — classify every claim and control; seek
   contradictions, bypasses, historical exposure, and off-repository unknowns.
3. **Remediate** — change only authorized repository/product controls, validate
   them, and keep external blockers open.
4. **Launch gate** — determine whether sales, processing, or public claims must
   remain disabled until facts, counsel, contracts, or operations are ready.

## Workflow

### 1. Freeze scope before conclusions

Record:

- exact operator name/type/status and evidence state;
- jurisdictions and the factual nexus for each;
- sales territories, customer types, supported ages, and channels;
- product behavior, AI roles, data roles, data flows, payments, and vendors;
- repository, live deployment, dashboards, contracts, registries, and counsel
  evidence that are in scope—and what is unavailable.

Unknown facts stay `unknown` or `unverified`. Do not convert them into assumed
obligations or reassuring negatives.

### 2. Build the complete claim universe

Inventory claims from public pages, pricing, checkout, onboarding, app UI,
machine-readable endpoints, docs, Terms, Privacy, security pages, sales decks,
contracts, handoffs, code comments, schemas, tests, and audit reports. Include
claims about what was audited, fixed, tested, merged, deployed, or verified.

Use the verdict set exactly:

- `supported`
- `qualified`
- `contradicted`
- `unverified`
- `not-audited`
- `not-applicable`

Distinguish claim type: factual, legal obligation, commercial, security
control, or recommendation. A useful recommendation is not automatically a
legal duty.

### 3. Determine applicability from predicates

For each jurisdiction and issue area, record the operator/customer/data/channel
facts that trigger or defeat applicability. Avoid universal “mandatory SaaS
requirements.” Load [`references/issue-areas.md`](references/issue-areas.md)
when building the matrix.

Use fresh official law/regulator sources and note retrieval time. Where legal
interpretation is material, set a counsel gate instead of silently deciding it.

### 4. Compare claims with enforcement and evidence

Trace each material promise to all relevant layers:

- public/contractual wording;
- UI and purchase flow;
- server/API authorization;
- database/storage behavior;
- vendor/dashboard settings and contracts;
- operational owner/runbook;
- retained evidence and historical state.

Test bypass paths: direct API calls, alternate auth, anonymous flows, legacy
tokens, background jobs, replayed webhooks, public-by-link storage, raw read
endpoints, and machine-readable docs. Future gating does not cure legacy data or
past invoices.

### 5. Close only the gaps within authority

Safe repository remediations often include truthful wording, conspicuous assent,
versioned receipts, authorization boundaries, billing launch gates, accurate
vendor disclosures, private storage, fail-closed writes, redacted public DTOs,
security headers, and removal/qualification of unimplemented benefits.

Do not fabricate operator identifiers, tax facts, contract execution, insurance,
registry status, vendor settings, audit reports, or counsel approval. Disable or
geofence a risky feature when its external prerequisites are unresolved and the
product can safely do so.

### 6. Create the evidence record

Initialize the bundled JSON contract:

```bash
python3 scripts/legal_readiness.py init legal-readiness.json
```

The initialized file is an intentionally failing template: it carries no
fabricated evidence and keeps launch blocked. Complete it using
[`references/manifest-schema.md`](references/manifest-schema.md), replace every
placeholder, remove `project.template_marker`, set `project.template` to
`false`, then run:

```bash
python3 scripts/legal_readiness.py check legal-readiness.json
```

The validator checks structure, provenance bindings, explicit coverage, and
bounded launch state—not evidence authenticity or legal correctness. It rejects
unsupported closure phrases, evidence-free supported/contradicted/inapplicable
claims, nonbinding legal-obligation support, unresolved applicability without a
next gate, unlinked P0 risks, future receipts, and lifecycle states without
digest-bound receipts. Supporting evidence and legal-source retrievals must be
re-observed within 370 days; the recorded observation date is the review date,
not an invitation to rewrite the artifact's original date.

The baseline coverage ledger is extensible: add `sector:<slug>` or
`custom:<slug>` rows for health, finance, employment, education, biometrics,
gaming, or another relevant regime. `not-applicable` is structured and
jurisdiction-linked. A `limited` launch requires implemented controls and
enforcement evidence for every open P0; a prose limitation cannot pass.

### 7. Probe declared public surfaces

Declare the routes and mechanical expectations in the manifest, then run:

```bash
python3 scripts/legal_readiness.py probe legal-readiness.json \
  --output legal-surface-receipt.json
```

This proves only reachability and declared status/header/content-type facts. It
does not prove the contents are sufficient or the system is compliant. Routes
must be same-origin; redirects are refused unless declared and remain
same-origin. Private/localhost targets are refused unless a trusted development
run explicitly adds `--allow-private-network`. Receipts bind the manifest and
expectations hashes and are not overwritten without `--force`. Connections are
pinned to the exact resolved addresses that passed the network-safety check so
DNS cannot change the destination between validation and use.

### 8. Validate proportionally

Run tests at each changed boundary: unit, route/action authorization, consent
withdrawal, billing role, webhook idempotency, storage access, policy-hash drift,
anonymous denial, and live interaction as applicable. Capture immutable commit,
PR, merge, deployment, and live-probe receipts before advancing lifecycle state.

Run an independent adversarial review. Require reviewers to attack:

- exact claim completeness;
- applicability assumptions;
- evidence provenance and freshness;
- UI/API bypasses and historical exposure;
- contradictions across pricing/docs/config/runtime;
- counsel/registry/vendor/dashboard unknowns;
- whether the cheapest path to pass the gate is deleting evidence.

### 9. Report the bounded outcome

Lead with what is supported, contradicted, and still blocking launch. Separate:

- implemented and interaction-verified controls;
- committed/merged/deployed lifecycle facts;
- counsel- and operations-dependent P0/P1 gates;
- not-audited domains;
- residual risks accepted by a named owner.

Use language such as:

> An adversarial issue-spotting and control-hardening pass was completed. The
> listed controls and receipts were verified at the stated lifecycle stage.
> Overall legal compliance is not claimed; unresolved operator, jurisdiction,
> counsel, contract, tax, vendor, and operational gates remain explicit.

## Stop conditions

Stop and escalate when:

- operator, jurisdiction, ownership, tax, registry, or authority facts are
  missing and would materially change the result;
- a legal interpretation is genuinely disputed or fact-dependent;
- closure requires signing, filing, accepting vendor terms, purchasing
  insurance, contacting people, or changing supported territories;
- remediation would hide or destroy evidence of historical processing;
- the requested statement would overstate the evidence.

## Anti-rationalization

| Temptation | Required correction |
|---|---|
| “The Terms page exists, so Terms are handled.” | Test identity, content, assent, versioning, evidence, and mandatory-law limits. |
| “The vendor says no training.” | Verify plan, route, provider, retention, contract, and dashboard settings. |
| “We use Stripe, so payments are compliant.” | Verify merchant identity, amount/currency/tax, renewal, refund, consent, receipt, cancellation, and webhook behavior. |
| “A disclaimer protects us.” | Treat it as disclosure/risk allocation, not immunity from contradictory or deceptive claims. |
| “The code is merged, so the gap is closed.” | Advance only to the lifecycle state supported by receipts; merge is not deploy or live verification. |
| “Counsel can clean this up later.” | Keep launch/sales/processing disabled where unresolved facts create a material legal gate. |
| “The checker passed, so we are compliant.” | The checker validates evidence structure; applicability and legal sufficiency remain latent judgments. |
| “The locator says counsel/registry, so it is authentic.” | A digest and verifier bind an assertion; independently authenticate the underlying artifact and authority. |

## Resources

- [`scripts/legal_readiness.py`](scripts/legal_readiness.py) — initialize,
  validate, and probe the deterministic evidence contract.
- [`assets/legal-readiness.example.json`](assets/legal-readiness.example.json) —
  neutral example manifest.
- [`references/manifest-schema.md`](references/manifest-schema.md) — field and
  closure semantics.
- [`references/issue-areas.md`](references/issue-areas.md) — jurisdiction-neutral
  issue-spotting matrix and official-source hierarchy.
