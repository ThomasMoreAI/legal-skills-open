# Practice profile: Life Sciences — Cross-jurisdiction

Orchestrator cold-start for plugin `cross-jurisdiction-life-sciences`. Loaded after `cross-jurisdiction/CLAUDE.md`, before invoking a specific skill.

## Scope

Pharmacovigilance and post-marketing safety of medicinal products across regulatory regimes: spontaneous adverse-event reporting, individual case safety reports (ICSRs), periodic safety reporting (PSUR/PBRER), signal detection, and the duties of marketing-authorisation holders. The regimes (EU, US, ICH-harmonised) overlap but impose distinct formats and timelines — keep them separate.

## Forums & authorities

European Medicines Agency (EMA) and national competent authorities in the EU; the US Food and Drug Administration (FDA); the International Council for Harmonisation (ICH) for harmonised guidelines (guidance, not directly binding law).

## Key sources of law

- **ICH harmonised guidelines:** ICH E2C(R2) (PBRER — periodic benefit-risk evaluation), ICH E2D (post-approval safety data management), ICH E2F (development safety update report).
- **EU:** Good Pharmacovigilance Practices (GVP) modules issued by EMA; the EU pharmacovigilance framework (Regulation (EC) 726/2004 and Directive 2001/83/EC as amended) — verify article references against the current consolidated text.
- **US:** post-marketing safety reporting under 21 CFR Part 314 (drugs) and Part 600/606 (biologics); verify the exact section.

Attribute each obligation to its regime (ICH / EU / US); ICH guidelines are harmonised standards, not statute. See `cross-jurisdiction/CLAUDE.md` for the jurisdiction guardrail.

## Citation discipline

Follow the rules in `cross-jurisdiction/CLAUDE.md`. Cite ICH guidelines by code and revision (e.g. "ICH E2C(R2)"), EU instruments in EU form, US rules as "21 CFR § [n]". **Never invent** guideline section numbers, regulation articles, or reporting timelines — verify against the current published version before relying on it.

## When this plugin does NOT apply

- A single jurisdiction's medicines/devices regulation → that jurisdiction's `life-sciences` (e.g. `eu/life-sciences`, `us/life-sciences`)
- Clinical-trial contracts or product-liability litigation → `commercial` / `litigation`
- Data-protection of patient/health data → `data-protection`

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute, regulation, and court/agency rules before relying on it.
