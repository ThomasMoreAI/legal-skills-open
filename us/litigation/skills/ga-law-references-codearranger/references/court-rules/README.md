# Georgia court-rules corpus

Verbatim snapshot of the Georgia court rules that govern civil
practice. This directory is the in-plugin (Georgia-specific) half of
the `ga-law-references` corpus; the federal corpora are symlinked from
the shared `claude-legal-federal-laws` plugin and live elsewhere.

## Scope

- **Uniform Superior Court Rules (USCR)** — the practice rules for the
  Superior Courts (the workhorse rule set; includes USCR 5 discovery
  period, USCR 6 motions, USCR 24 domestic-relations rules, USCR 36
  e-filing).
- **Uniform State Court Rules** — the parallel rule set for the State
  Courts (largely tracks the USCR).
- **Uniform Magistrate Court Rules** — the practice rules for the
  Magistrate Courts (small-claims, dispossessory, garnishment).
- **Supreme Court of Georgia rules** — appellate practice in the
  Supreme Court.
- **Court of Appeals of Georgia rules** — appellate practice in the
  Court of Appeals.

Note: the operative pleading-form and civil-procedure rules are
statutory (the Civil Practice Act, O.C.G.A. Title 9 Ch. 11, in
`../ga-statutes-debt/`); the rule sets here supply the court-side
practice overlay (motions, hearings, discovery period, e-filing,
domestic standing orders).

## Sources

- `georgiacourts.gov` / `assets.georgiacourts.gov` — Uniform Court
  Rules and Uniform Magistrate Court Rules (dated-filename PDFs;
  discover the current filename from the rules landing page).
- Council of Superior Court Judges — `cscj.georgiacourts.gov`.
- `gasupreme.us/rules/` — Supreme Court of Georgia rules.
- `gaappeals.gov/court-rules/` — Court of Appeals rules.

All sources are open. There is no paywall on the Georgia court rules
(unlike the official O.C.G.A. statute text).

## Refresh

Pulled by `scripts/pull_georgia_rules.py` (to be added) from
`georgiacourts.gov` and the appellate-court rule pages. After a
refresh, bump the `ga-law-references` `SKILL.md` `version:` (PATCH for
a routine refresh, MINOR if a new rule set is added).

> **NOT LEGAL ADVICE.** Snapshot for drafting reference only. Verify
> against the current rule text at the source before filing.
