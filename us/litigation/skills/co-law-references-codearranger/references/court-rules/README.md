# court-rules Corpus — Colorado

- Last refreshed: 2026-05-14
- Chief Justice Directives (verbatim): 72
- Rule-set stubs (full text paywalled): 6
- Total corpus size: 1,311,767 bytes

This corpus holds the Colorado court-rules content most relevant to civil practice. The Colorado-specific situation: **Chief Justice Directives (CJDs)** are published as free PDFs on `coloradojudicial.gov`; the rule sets themselves — **C.R.C.P., CRE, C.A.R., Colorado RPC** — are **public-domain edicts of the Colorado Supreme Court** (the government edicts doctrine — Banks v. Manchester, 128 U.S. 244 (1888); Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)), but the only conveniently published copies are the *annotated compilations* West (Colorado Court Rules) and LexisNexis copyright, and the free third-party mirrors (Justia, FindLaw, Casetext) sit behind Cloudflare. The obstacle is **access, not ownership** — copyright sits on the annotations, not the rule text. The `STUB-*.md` entries explain the access gap and point to the canonical publication. Substantive citations in the Colorado plugin's SKILL.md files reference the rule numbers and verbatim short excerpts, not the full rule text.

## Inventory

### Chief Justice Directives (auto-pulled, verbatim)

- `CJD-00-01.md`
- `CJD-01-01.md`
- `CJD-04-01.md`
- `CJD-04-02.md`
- `CJD-04-03.md`
- `CJD-04-04.md`
- `CJD-04-05.md`
- `CJD-04-06.md`
- `CJD-04-07.md`
- `CJD-04-08.md`
- `CJD-05-01.md`
- `CJD-05-02.md`
- `CJD-05-03.md`
- `CJD-05-05.md`
- `CJD-06-01.md`
- `CJD-06-02.md`
- `CJD-06-03.md`
- `CJD-07-01.md`
- `CJD-07-02.md`
- `CJD-08-01.md`
- `CJD-08-02.md`
- `CJD-08-04.md`
- `CJD-08-05.md`
- `CJD-08-06.md`
- `CJD-11-01.md`
- `CJD-11-02.md`
- `CJD-11-03.md`
- `CJD-12-01.md`
- `CJD-12-02.md`
- `CJD-12-03.md`
- `CJD-13-01.md`
- `CJD-14-01.md`
- `CJD-15-01.md`
- `CJD-16-02.md`
- `CJD-16-03.md`
- `CJD-21-01.md`
- `CJD-21-02.md`
- `CJD-22-01.md`
- `CJD-23-01.md`
- `CJD-23-02.md`
- `CJD-23-03.md`
- `CJD-23-04.md`
- `CJD-23-05.md`
- `CJD-85-02.md`
- `CJD-85-06.md`
- `CJD-85-09.md`
- `CJD-85-18.md`
- `CJD-85-19.md`
- `CJD-85-22.md`
- `CJD-85-23.md`
- `CJD-85-25.md`
- `CJD-85-27.md`
- `CJD-85-31.md`
- `CJD-86-01.md`
- `CJD-87-03.md`
- `CJD-94-01.md`
- `CJD-94-02.md`
- `CJD-95-01.md`
- `CJD-95-02.md`
- `CJD-95-03.md`
- `CJD-95-05.md`
- `CJD-96-07.md`
- `CJD-96-08.md`
- `CJD-97-03.md`
- `CJD-97-04.md`
- `CJD-98-01.md`
- `CJD-98-02.md`
- `CJD-98-03.md`
- `CJD-98-06.md`
- `CJD-98-08.md`
- `CJD-99-02.md`
- `CJD-99-03.md`

### Rule-set stubs (refresh manually from West / Lexis)

- `CRCP.md` — Colorado Rules of Civil Procedure (C.R.C.P.) (Colo. R. Civ. P. (citation form: `C.R.C.P. <num>`))
- `CRE.md` — Colorado Rules of Evidence (CRE) (Colo. R. Evid. (citation form: `CRE <num>`))
- `CAR.md` — Colorado Appellate Rules (C.A.R.) (Colo. App. R. (citation form: `C.A.R. <num>`))
- `Colorado-RPC.md` — Colorado Rules of Professional Conduct (Colo. RPC (citation form: `Colo. RPC <num>`))
- `CRCP-Chapter-25-Small-Claims.md` — C.R.C.P. Chapter 25 — Simplified Procedure / Small Claims (Colo. R. Civ. P. 501-521 (citation form: `C.R.C.P. 50X`))
- `CRCP-County-Court-Rules.md` — C.R.C.P. Chapter 18 — County Court Civil Procedure (Rules 301-411) (Colo. R. Civ. P. 301-411 (citation form: `C.R.C.P. 3XX`))

## Re-pull

```
python3 scripts/pull_co_court_rules.py \
  --out plugins/co-court-docs/skills/co-law-references/references/court-rules \
  --workers 4
```

Re-running is idempotent: existing CJD MD files are rewritten with fresh metadata; existing stubs (and any hand-authored MD files in this directory) are preserved untouched unless `--overwrite-stubs` is passed.
