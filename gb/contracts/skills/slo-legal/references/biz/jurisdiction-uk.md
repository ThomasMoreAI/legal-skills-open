---
name: jurisdiction-uk
created: 2026-04-25
status: stable-interface (the canonical "v1 UK only" error string is interface; the regulator list is evolving)
audience: every advisor skill in the biz pack
purpose: UK-only jurisdiction prose anchors + the canonical "v1 supports UK only" error string used by every advisor skill on non-UK requests, plus the indexed list of UK regulators that fire `gate-1-regulated`.
---

# UK jurisdiction — anchors and rejection patterns

## v1 jurisdiction stance: UK only

Every advisor skill in the biz pack operates on **UK English law** (England & Wales, Scotland, Northern Ireland — collectively "UK") only in v1. Non-UK requests are rejected before any artifact write.

**Why UK only**: The `/slo-architect biz-skill-pack` synthesis (paragraph 3) and dossier prior-art evidence are clear that no surveyed legal-templating tool uses shared-prose-with-jurisdiction-flag — Stripe Atlas and Clerky stayed Delaware-only by design; SeedLegals took six months to localise France. A `--jurisdiction us` or `--jurisdiction eu` flag in v1 would imply false portability. v2 expansion is a fresh `/slo-architect` pass against per-jurisdiction prose work, not a config flag.

## Canonical "v1 UK only" error string

When an advisor skill detects a non-UK jurisdiction (counterparty in non-UK, work performed in non-UK, governing law specified as non-UK, founder explicitly requests non-UK), the skill MUST emit:

> **v1 supports UK only; US/EU is a v2 architectural pivot — see [docs/slo/design/biz-skill-pack-overview.md](../../docs/slo/design/biz-skill-pack-overview.md) for the v2 design rationale and [docs/slo/research/biz-skill-pack/synthesis.md](../../docs/slo/research/biz-skill-pack/synthesis.md) paragraph 3 for the prior-art evidence (no surveyed legal-templating tool uses shared-prose-with-jurisdiction-flag — Stripe Atlas and Clerky are Delaware-only by design; SeedLegals took six months to localise France). Engage a solicitor / accountant qualified in the relevant jurisdiction.**

The string `v1 supports UK only` and `v2 architectural pivot` are interface — present in the test `non_uk_jurisdiction_arg_rejected`. Skill prose MAY paraphrase the surrounding context but MUST preserve those two phrases.

## UK regulator index (fires `gate-1-regulated`)

When the founder's situation involves any of the regulators below, `gate-1-regulated` fires and the matter routes to triage. The default route is `lawyer`, but advisor skills MAY override based on which regulator's domain is relevant:

| Regulator | Domain | Default route_to | Skill override pattern |
|---|---|---|---|
| **HMRC** | Tax (corporation tax, VAT, PAYE, NI, R&D credits, SEIS / EIS, IR35) | `accountant` | `/slo-accounting` and `/slo-fundraise` route to accountant by default; `/slo-legal` may route to lawyer if the matter is contractual (e.g., contesting an HMRC inquiry letter) |
| **ICO** | UK GDPR + PECR (privacy notice, ROPA, DPA, direct marketing) | `dpo` (or `lawyer + dpo` if no DPO) | gate-4-gdpr-document supersedes gate-1 here — see triage-gate.md gate-4 routing |
| **FCA** | Financial services (FSMA 2000, regulated activities, AR / authorisation, consumer credit) | `lawyer` (specialist) | All four advisor skills route to specialist FS lawyer; this is not "any solicitor" |
| **MHRA** | Medicines & medical devices | `lawyer` (specialist) + `accountant` (R&D context) | `/slo-equity` and `/slo-fundraise` cite this pair |
| **CQC** (Care Quality Commission) | Health and social care providers | `lawyer` (specialist) | All four advisor skills |
| **Ofcom** | Communications, broadcasting | `lawyer` (specialist) | All four advisor skills |
| **CMA** (Competition and Markets Authority) | Mergers, anti-competitive practice, consumer law | `lawyer` (specialist) | `/slo-fundraise` (round-related), `/slo-legal` (B2B contracts) |
| **HSE** (Health and Safety Executive) | Workplace health & safety | `lawyer` (employment specialist) + `accountant` (cost-allocation context) | `/slo-hire` (Runbook C) |
| **Companies House** | Company filings, registration, beneficial ownership | `accountant` (default) — most filings are accountant-territory | `/slo-equity` (cap-table changes), `/slo-accounting` (annual filings) |
| **Pensions Regulator** | Workplace pensions auto-enrolment | `accountant` (payroll context) | `/slo-hire`, `/slo-accounting` |

**Adding a new regulator**: Append a row above with the regulator name, domain summary, default route_to, and which advisor skill(s) cite it. This is per-milestone discipline — extending the table doesn't require a `/slo-architect` re-pass, but does require a `/slo-critique` security-persona review of the new row before merge.

## UK regulatory anchor URLs

The advisor skills emit these URLs as **citations** (the founder follows them manually) — never fetched at runtime by any biz skill:

| Anchor | URL | Used by |
|---|---|---|
| GOV.UK (root) | https://www.gov.uk/ | All four advisor skills |
| HMRC Venture Capital Schemes Manual | https://www.gov.uk/hmrc-internal-manuals/venture-capital-schemes-manual | `/slo-equity`, `/slo-fundraise` (cited via `references/biz/hmrc-vcm-index.md` from M3 onward) |
| HMRC CEST tool | https://www.gov.uk/guidance/check-employment-status-for-tax | `/slo-legal triage` (contractor vs employee), `/slo-fundraise` (qualifying-employee context), `/slo-hire` (Runbook C) |
| ICO (root) | https://ico.org.uk/ | `/slo-legal` (gate-4 routing), `/slo-accounting` (records of processing for tax data) |
| ICO DUAA 2025 summary | https://ico.org.uk/about-the-ico/what-we-do/legislation-we-cover/data-use-and-access-act-2025/the-data-use-and-access-act-2025-duaa-summary-of-the-changes/ | `/slo-legal triage` (cited via `references/biz/ico-duaa-index.md`) |
| legislation.gov.uk DUAA 2025 | https://www.legislation.gov.uk/ukpga/2025/18 | Statutory authority for DUAA citations |
| legislation.gov.uk ERA 1996 s86 | https://www.legislation.gov.uk/ukpga/1996/18/section/86 | `/slo-legal triage` (notice periods), `/slo-hire` (Runbook C) |
| FCA Handbook | https://www.handbook.fca.org.uk/ | When gate-1 fires for FS-regulated matters |

## UK / E&W law specifics that drive the advisor skills

- **Contractor IP defaults to the contractor unless explicitly assigned in writing.** This is a UK-law specific that drives `/slo-legal draft contractor-sow` to make the IP-assignment clause load-bearing. US "work made for hire" doctrine (17 USC §101) handles this differently — another reason v1 is UK only.
- **Employment notice (ERA 1996 s86)**: 1 week if <2 yrs service, 1 week per completed year up to 12 weeks at 12+ yrs (employer); 1 week after 1 month service (employee). Cited by `/slo-legal` and `/slo-hire`.
- **Statutory holiday (WTR 1998)**: 5.6 weeks paid leave / year (28 days FT including bank holidays).
- **VAT registration threshold**: £90,000 turnover (2024–2025; verify current threshold at retrieval time on gov.uk). Cited by `/slo-accounting`.
- **SEIS / EIS qualifying-trade and qualifying-company tests**: cited by `/slo-equity` and `/slo-fundraise` via M3's `references/biz/hmrc-vcm-index.md`.
- **CC BY-ND 4.0 verbatim render obligation for oneNDA**: cited by `/slo-legal draft nda`. See `references/biz/open-template-anchors.md` (M2) and the placeholder at `references/biz/templates/onenda-uk.md`.
