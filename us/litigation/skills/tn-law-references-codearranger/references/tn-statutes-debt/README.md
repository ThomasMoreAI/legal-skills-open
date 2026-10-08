# tn-statutes-debt Corpus — Tennessee

Tennessee Code Annotated chapters covering the civil-practice +
consumer-debt + family-law + landlord-tenant + tort surface,
pulled by `scripts/pull_tn_statutes.py`.

Directory name retains the legacy `debt` slug for path stability
across the marketplace, but scope covers the full civil + family
practice surface.

## Sources and access posture

The Tennessee Code's **statutory text is public domain** — a
government edict that no one can copyright (Banks v. Manchester,
128 U.S. 244 (1888); Georgia v. Public.Resource.Org, 590 U.S.
255 (2020)). What **LexisNexis** copyrights is the *Annotated*
compilation (case notes, history, cross-references) it publishes
as the state's official code under contract; Tennessee itself
posts no clean structured copy of the bare text (its free
`lexisnexis.com/hottopics/tncode/` mirror is a JS container, not
flat HTML). This corpus copies **only the section text — never
the annotations** — from the structured free mirrors **Justia**
(`law.justia.com/codes/tennessee/`) and **FindLaw**
(`codes.findlaw.com/tn/`). Both sit behind **Cloudflare bot-fight
mode** that fingerprints the TLS handshake — stdlib `urllib`
gets a 403 even from a residential IP.

**As of v0.2.0** the puller uses **`curl_cffi` with Chrome TLS
impersonation** to defeat the fingerprint check and walks
**Chapter → Part → Section** when a chapter is subdivided into
Parts. Run from a residential or VPN-routed IP, it produces
**verbatim Markdown** for all 25 chapters (~2.6 MB; 1,496
sections).

When fetch fails (no `curl_cffi` installed, blocked egress,
upstream structure change) the puller falls back to **well-formed
pointer stubs** carrying the canonical Justia URL plus the
official LexisNexis URL plus a one-line scope description —
mirroring the `pull_indiana_statutes.py` / `pull_ny_statutes.py`
"publish what we can verify + honest stubs for the rest"
discipline. The `_file_is_stub` regression guard preserves any
existing verbatim file rather than overwriting it with a stub on
re-run.

## Target catalog (25 chapters)

| Chapter | Topic |
|---|---|
| Title 15, Ch. 1 | Legal Holidays (§ 15-1-101) |
| Title 16, Ch. 15 | General Sessions Courts — $25,000 civil cap (§ 16-15-501) |
| Title 20, Ch. 6 | Process — incl. § 20-6-104 debt-buyer documentation (2024) |
| Title 20, Ch. 12 | Costs and fees — § 20-12-119(c) fee-shifting on 12.02(6) |
| Title 20, Ch. 16 | Summary judgment standard (§ 20-16-101) |
| Title 24, Ch. 5 | Witnesses; sworn-account procedure (§ 24-5-107) |
| Title 26, Ch. 2 | Executions |
| Title 26, Ch. 3 | Sales under execution |
| Title 27, Ch. 5 | Appeals — de novo from General Sessions (§ 27-5-108) |
| Title 28, Ch. 3 | Limitations of actions (§§ 28-3-104, -105, -109) |
| Title 29, Ch. 18 | Forcible entry and detainer (eviction) |
| Title 29, Ch. 20 | Governmental Tort Liability Act (GTLA) |
| Title 29, Ch. 26 | Health Care Liability Act (HCLA) |
| Title 36, Ch. 3 | Domestic abuse — Orders of Protection |
| Title 36, Ch. 4 | Divorce and annulment |
| Title 36, Ch. 5 | Alimony, child support, UIFSA |
| Title 36, Ch. 6 | Custody, parenting plans, UCCJEA |
| Title 37, Ch. 1 | Juvenile Court — dependency, neglect, parentage, TPR |
| Title 47, Ch. 2 | UCC — Sales (Article 2; § 47-2-725 4-year SOL) |
| Title 47, Ch. 11 | Retail installment sales (RISA) |
| Title 47, Ch. 14 | Interest and usury |
| Title 47, Ch. 18 | Tennessee Consumer Protection Act |
| Title 62, Ch. 20 | Tennessee Collection Service Act |
| Title 66, Ch. 7 | General landlord and tenant (non-URLTA counties) |
| Title 66, Ch. 28 | Uniform Residential Landlord and Tenant Act (URLTA) |

## How to refresh

```
python3 scripts/pull_tn_statutes.py --workers 4
```

Or to force pointer stubs only (useful for validating the stub
shape on a machine that CAN reach Justia):

```
python3 scripts/pull_tn_statutes.py --stubs-only
```

Wired into the quarterly `refresh-references` workflow under
`target=tn`. The `_file_is_stub` regression guard ensures that
any verbatim content already committed survives a stub-only CI
refresh (the worst case is a `Fetched:` date bump in the
manifest).
