---
name: cost-baseline-jpp-law-2026
created: 2026-04-25
retrieved: 2026-04-25
valid_through_suggestion: 2027-04-25
sources:
  - https://seedlegals.com/pricing/
  - https://www.jpplaw.co.uk/sectors/fixed-fee-startup/
status: stable — publicly auditable mixed baseline (SeedLegals subscription tiers + JPP Law solicitor-quote-on-request)
purpose: |
  UK cost baseline for ROI claims in advisor-skill outputs. Uses SeedLegals'
  publicly-priced subscription tiers as the "templating service" anchor (GBP
  figures public on https://seedlegals.com/pricing/), and JPP Law as the
  "engage-a-solicitor" anchor (firm publishes service availability publicly
  but not specific GBP figures — founder requests a quote at first-use and
  records below).
pricing_provenance: mixed-public-and-quote-pending
---

# UK cost baseline (mixed public + quote-pending)

> Retrieval date: **2026-04-25**.
> Sources:
> - SeedLegals subscription pricing (publicly retrievable): https://seedlegals.com/pricing/
> - JPP Law fixed-fee startup services (publicly listed, GBP figures by quote): https://www.jpplaw.co.uk/sectors/fixed-fee-startup/

## Provenance note (load-bearing)

The original Runbook A design anchored ROI claims to a single firm's fixed-fee price list. Russell Cooke (initial dossier choice) was rejected because their 2026-27 list is not publicly retrievable. JPP Law was the swap. Combined critique f2 (post-execution): JPP Law's fixed-fee startup page lists service availability but does NOT publish specific GBP figures — turning the file's price column into perpetual placeholders.

This file pivots to a **mixed baseline** instead:

1. **SeedLegals subscription tiers** (public, retrievable) provide a templating-service price floor — what a founder would pay for a self-serve subscription that gives them template access without solicitor review.
2. **JPP Law (or any other UK fixed-fee firm)** provides the engage-a-solicitor anchor — but founders MUST request a specific quote at first-use and record the figures in the "Your firm" section below. The quote is private (firm-specific) and changes annually.

Advisor-skill outputs cite EITHER the SeedLegals figure (always available) OR the founder's quoted figure (when populated). The artifact's `cost_baseline_ref` frontmatter records which source applied.

## SeedLegals subscription tiers (publicly priced — 2026-04-25)

| Item | Price (GBP, ex VAT) | Source |
|---|---|---|
| **Access** (templates only, no funding round tooling) — monthly | £75 / month | https://seedlegals.com/pricing/ |
| **Access** — annual | £590 / year | https://seedlegals.com/pricing/ |
| **Funding — Start** (up to £100k/year of funding) | £1,490 / year | https://seedlegals.com/pricing/ |
| **Funding — Raise** (up to £250k/year of funding) | £2,790 / year | https://seedlegals.com/pricing/ |
| **Funding — Scale** (up to £500k/year of funding) | £4,990 / year | https://seedlegals.com/pricing/ |
| **Options scheme** — annual | £2,490 / year | https://seedlegals.com/pricing/ |
| **SEIS/EIS Advance Assurance** (one-off, pay-as-you-go) | £390 | https://seedlegals.com/pricing/ |
| **SEIS/EIS Compliance** (one-off) | from £490 | https://seedlegals.com/pricing/ |
| **SeedFAST** (one-off, per advance subscription) | £100 | https://seedlegals.com/pricing/ |
| **Seed & Series A Round** (one-off) | £1,990 | https://seedlegals.com/pricing/ |
| **R&D Tax Relief** (one-off) | £1,490 opening + 5% closing fee | https://seedlegals.com/pricing/ |
| **General Counsel** (10-hour engagement) | from £2,999 | https://seedlegals.com/pricing/ |
| **Exit** (one-off engagement) | £690 + from £1,990 | https://seedlegals.com/pricing/ |

**All prices ex VAT.** Retrieval date stamped above; SeedLegals revises annually.

## Your firm (engage-a-solicitor anchor — populate at first-use)

A founder running advisor-skill `draft` modes against real engagements should request a fixed-fee quote from their chosen UK solicitor (JPP Law, Russell Cooke, or any firm) and record the figures here. Once populated, advisor-skill ROI blocks cite these figures preferentially over the SeedLegals proxy.

```yaml
# Replace this section with your firm's quote at first-use of /slo-legal draft.
# Once populated, change pricing_provenance in this file's frontmatter to
# `solicitor-quoted` and run cargo test -p sldo-install --test e2e_biz_followup_m1
# to confirm the structural-contract test passes.

your_firm:
  name: <e.g., JPP Law>
  contact_url: <e.g., https://www.jpplaw.co.uk/sectors/fixed-fee-startup/>
  quoted_on: <YYYY-MM-DD>
  quoted_by: <name of partner / associate who provided the quote>
  fees:
    nda: <GBP, ex VAT>
    contractor_sow: <GBP>
    ip_assignment: <GBP>
    terms_and_conditions_b2b: <GBP>
    shareholders_agreement_cofounders: <GBP>
    articles_of_association: <GBP>
    employment_contract: <GBP>
```

## How advisor skills cite this file

Every advisor `draft` artifact carries in frontmatter:

```yaml
cost_baseline_ref: references/biz/cost-baseline-jpp-law-2026.md@<retrieved-date>
cost_baseline_source: seedlegals-public | solicitor-quoted | placeholder-pending
```

And in body footer (template; skill picks the appropriate source):

```markdown
## Cost baseline (provenance)

Per [SeedLegals public subscription pricing](https://seedlegals.com/pricing/), retrieved <retrieved-date>, the **Access** tier (£75/month or £590/year + VAT) provides templating access for the v1 doc set at the cost a founder would pay for self-serve. A UK solicitor engagement for an equivalent <doc-type> is by quote — see the "Your firm" section of `references/biz/cost-baseline-jpp-law-2026.md` for the founder's recorded quote (or run `/slo-legal prepare 'lawyer-quote-request for <doc-type>'` to draft the quote-request brief).

This advisor-skill draft is **NOT** a substitute for solicitor review — see the `lawyer_review_recommended: true` flag in the frontmatter. Cost reference snapshot: [references/biz/cost-baseline-jpp-law-2026.md](references/biz/cost-baseline-jpp-law-2026.md).
```

## Structural-contract test (added by follow-up `biz-pack-cost-baseline-refresh`)

The new test `crates/sldo-install/tests/e2e_biz_followup_m1.rs::cost_baseline_has_real_figures_or_explicit_placeholder` asserts ONE of:

1. The SeedLegals public-tier section contains at least 5 GBP figures (matched by regex `£\d+`) — OK because the public source is retrievable, **THIS IS THE STATE M1 SHIPS WITH**.
2. The "Your firm" section is populated (no `<...>` placeholder tokens remaining) — OK because the founder has quoted their solicitor.
3. The frontmatter `pricing_provenance: placeholder-pending` is set explicitly AND the file body contains a "REQUIRES POPULATION BEFORE PRODUCTION USE" header — explicit deferral acknowledgment.

The test passes today via path (1). When the founder populates "Your firm", path (2) takes over.

## Refresh cadence

- **Annual (recommended)**: refresh the SeedLegals figures + re-quote your firm. Update `retrieved:` in frontmatter.
- **Triggered**: refresh immediately when SeedLegals publishes a price change OR when your firm publishes new fixed fees OR when the founder switches firms.
- **`/loop @yearly` schedule** (offered to founder at end of M1): re-fetch SeedLegals page + ask founder for refreshed firm quote.
