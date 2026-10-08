---
name: oh-county-courts-codearranger
title: Ohio County Common Pleas (Long-tail Roll-up)
description: Use when filing in an Ohio Court of Common Pleas other than the 8 flagship counties (Cuyahoga, Franklin, Hamilton, Summit, Montgomery, Lucas, Stark, Butler). Triggers include any other Ohio county's Common Pleas name (Mahoning / Youngstown, Warren, Lake, Lorain, Trumbull, Clark, Greene, etc.). Layers on top of `oh-statewide-format` with the common-denominator Loc. R. patterns across Ohio's 88 county Courts of Common Pleas.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/oh-court-docs/skills/oh-county-courts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Ohio County Common Pleas (Long-tail Roll-up)

> **NOT LEGAL ADVICE.** Each Ohio county Court of Common
> Pleas publishes its own Loc. R. The 80 non-flagship
> counties vary significantly. Always verify per-court
> rules before filing.

## What this covers

This skill covers Common Pleas courts in the **80 Ohio
counties not separately covered by dedicated flagship
skills** (the 8 flagships are `oh-cuya`, `oh-frank`,
`oh-hamil`, `oh-summit`, `oh-montgomery`, `oh-lucas`,
`oh-stark`, `oh-butler`).

## Court of Common Pleas overview

Ohio has **88 county Courts of Common Pleas** — one per
county under the Ohio Constitution. Each is a court of
general jurisdiction:

- **General Division** — civil + criminal
- **Domestic Relations Division** — divorce, custody,
  support (see `oh-family-court`)
- **Juvenile Division** — juvenile cases + unmarried-
  parent custody (see `oh-family-court`)
- **Probate Division** — wills, estates, adoption

Smaller counties may combine divisions; larger counties
operate them as separate courts within Common Pleas.

## Higher-volume non-flagship counties

| County | Seat | Approx. pop. | Notable |
|---|---|---|---|
| Mahoning | Youngstown | 0.23M | Steelbelt; significant L&T volume |
| Warren | Lebanon | 0.24M | Cincinnati's northern exurbs |
| Lake | Painesville | 0.23M | Cleveland's eastern suburbs |
| Lorain | Elyria | 0.31M | Cleveland's western suburbs |
| Trumbull | Warren | 0.20M | Northeast / steel-belt |
| Clark | Springfield | 0.13M | Central / industrial |
| Greene | Xenia | 0.17M | Dayton's eastern suburbs |
| Wood | Bowling Green | 0.13M | Toledo's southern suburbs |
| Portage | Ravenna | 0.16M | Kent State; Cleveland exurbs |
| Delaware | Delaware | 0.22M | Columbus's northern suburbs; Gen. Div. Loc. R. mirrored verbatim at `oh-law-references/references/local-rules/Delaware-CommonPleas-LocalRules.md` (eff. 4/14/2025) — still confirm the court's current version + e-filing before filing |
| Allen | Lima | 0.10M | Northwest / industrial |
| Mercer / Auglaize / Putnam | rural | low | low-volume rural civil dockets |

## Common Loc. R. patterns across non-flagship Common Pleas

Smaller Common Pleas courts share most procedural
conventions:

- **Civ. R. baseline** governs unless a Loc. R. modifies
- **Page limits on briefs** — typically 15-25 pages
- **Working copies** — many smaller courts require paper
  bench copies; verify
- **Notice of hearing** — typically scheduled with
  chambers / bailiff
- **Magistrates** under Civ. R. 53 handle pretrial civil
  matters in most courts

## E-filing landscape

- Larger non-flagship Common Pleas courts use Tyler
  Technologies (Odyssey) or county-built portals
- Smaller rural Common Pleas may still require paper
  filings or partial e-filing

Verify per-court before assuming e-filing is available.

## Repossession / auto-deficiency defense (non-flagship counties)

A repossession or deficiency suit filed in a non-flagship
Common Pleas court (e.g., Delaware County) runs on the
statewide Civ. R. baseline plus that county's Loc. R.; the
**substantive** defense layers three statutes, all carried
verbatim in `oh-law-references/references/oh-statutes-debt/`:

- **UCC Article 9 — `RC-Chapter-1309.md`** (the disposition
  regime):
  - **Notice of disposition** before sale — R.C. 1309.611
    (defective/absent notice limits the deficiency under
    R.C. 1309.626).
  - **Commercially reasonable** disposition — R.C. 1309.610(B).
  - **Chain of title** / standing of the assignee-plaintiff —
    R.C. 1309.406.
- **Retail Installment Sales Act — `RC-Chapter-1317.md`**: if
  the loan is a retail installment contract (most auto
  financing), RISA's contract-form and notice/cure provisions
  apply on top of Article 9.
- **Certificate of Motor Vehicle Title Law —
  `RC-Chapter-4505.md`**: lien perfection on the vehicle runs
  through the certificate of title (R.C. 4505.13) — check that
  the plaintiff's security interest was properly noted.

See `oh-consumer-debt` for the full repossession-deficiency
fact-pattern and RFP/RFA banks.

## Composition with other oh- skills

- `oh-statewide-format` — Civ. R. 10 format baseline
- `oh-pro-se` — pro-se framework
- `oh-discovery`, `oh-first-30-days`, `oh-hearings`,
  `oh-post-judgment` — procedural skills used across all
  Common Pleas courts
- `oh-consumer-debt`, `oh-family-law` — subject bundles
- `oh-municipal-courts` — Municipal Court layer (separate
  from Common Pleas; $15k cap)
