# court-rules Corpus — New York

Verbatim text of New York court-rule canonical sources, scoped to
civil practice across every NY civil-court venue.

## Sources

Published by the New York Unified Court System at
`www.nycourts.gov/rules/...`. **15 Parts of 22 NYCRR pulled verbatim;
4 ancillary publications and 1 paywalled Part shipped as pointer
stubs.**

### Trial-court rules (200-221)

- **Part 202** — Uniform Civil Rules for the Supreme Court and the
  County Court (the core civil-procedure rule set; includes the
  Commercial Division Rules at § 202.70 as a sub-section, the IAS
  at § 202.3, motion practice at §§ 202.7-202.8-g, e-filing at
  § 202.5-b, settle-order at § 202.48, and the CCFA default-
  scrutiny rule at § 202.27-a)
- **Part 205** — Uniform Rules for the Family Court (FCA Articles
  3-10)
- **Part 206** — Uniform Rules for the Court of Claims
- **Part 207** — Uniform Rules for the Surrogate's Court
- **Part 208** — Uniform Civil Rules for the NYC Civil Court
  (includes the Housing Part overlay at § 208.42 and the CCFA
  default-scrutiny rule at § 208.6-a)
- **Part 210** — Uniform Civil Rules for the upstate City Courts
  (UCCA)
- **Part 212** — Uniform Civil Rules for the District Courts
  (Nassau + Suffolk, UDCA)
- **Part 214** — Uniform Civil Rules for the Justice Courts
  (~1,250 Town and Village courts, UJCA)
- **Part 216** — Sealing of Court Records in Civil Actions
- **Part 220** — Jury Selection and Deliberation
- **Part 221** — Conduct of Depositions

### Chief Administrator rules (100-161)

- **Part 100** — Rules Governing Judicial Conduct
- **Part 104** — Retention and Disposition of Court Records
- **Part 125** — Uniform Rules for the Engagement of Counsel
- **Part 130** — Costs and Sanctions for Frivolous Conduct

### Stubs (no free authoritative HTML source)

- **Part 1200** — Rules of Professional Conduct (paywalled at West
  / LexisNexis; Cornell LII has a regulatory-index wrapper but
  not the verbatim rule body)
- **NY Law Reports Style Manual (Tanbook)** — published by the
  Reporter of Decisions; PDF distribution only
- **NYC Civil Court Directives and Procedures Manual** — local-
  rule overlay including Consumer Credit Part directives + Housing
  Part directives
- **Nassau / Suffolk District Court local rules** — per-court
  Part Rules

## How to refresh

```bash
# Refresh from a developer workstation, routing through a local
# Cloudflare-Warp HTTP proxy so nycourts.gov sees a Cloudflare-
# trusted source IP:
NY_RULES_PROXY=http://192.168.8.21:9091 \
  python3 scripts/pull_ny_court_rules.py --workers 4

# Refresh without proxy (will most likely hit Cloudflare bot-fight
# mode and fall back to stubs — useful only for development
# sanity-checks):
python3 scripts/pull_ny_court_rules.py --workers 4
```

> **The quarterly CI workflow runs without `NY_RULES_PROXY`** —
> that env var points at a developer-local LAN endpoint that
> GitHub Actions runners can't reach. The CI run still attempts
> the pull (curl_cffi alone sometimes passes Cloudflare on a
> well-reputed runner IP), but when it can't, the puller falls
> back to writing stubs and the **"don't regress substantive
> content"** check keeps any verbatim content already committed
> in place. So the canonical way to refresh the verbatim corpus
> is for an operator to run the puller locally with their
> proxy set and commit the diff.

The puller:

1. **Fetches via curl_cffi** with Chrome TLS impersonation, which
   defeats Cloudflare's TLS-fingerprint bot detection. Install
   with `pip install --break-system-packages curl_cffi` if
   needed.
2. **Honors `NY_RULES_PROXY`** when set — routes the curl_cffi
   client through that HTTP proxy (typically a Cloudflare-Warp
   container giving the puller a Cloudflare-trusted source IP).
3. **Falls back to pointer stubs** when the upstream returns a
   Cloudflare interstitial despite both layers. Stubs document
   the canonical URL.
4. **Never regresses substantive content to a stub.** If a
   previous refresh wrote real Markdown and the current refresh
   would only produce a stub, the existing file is kept in place
   (CI-safe — a date-only re-run with no proxy doesn't overwrite
   verbatim content with stubs).

## File index

| File | Rule set | Scope |
|---|---|---|
| `Part-100-Judicial-Conduct.md` | 22 NYCRR Part 100 | Judicial conduct + recusal |
| `Part-104-Records-Retention.md` | 22 NYCRR Part 104 | Court-records retention schedule |
| `Part-125-Engagement-Counsel.md` | 22 NYCRR Part 125 | Engagement-of-counsel scheduling |
| `Part-130-Costs-Sanctions.md` | 22 NYCRR Part 130 | Sanctions for frivolous conduct |
| `Part-202-Supreme-County.md` | 22 NYCRR Part 202 | Supreme + County Court (incl. § 202.70 Commercial Division) |
| `Part-205-Family.md` | 22 NYCRR Part 205 | Family Court |
| `Part-206-Court-Claims.md` | 22 NYCRR Part 206 | Court of Claims |
| `Part-207-Surrogates.md` | 22 NYCRR Part 207 | Surrogate's Court |
| `Part-208-NYC-Civil.md` | 22 NYCRR Part 208 | NYC Civil Court + Housing Part |
| `Part-210-City-Courts.md` | 22 NYCRR Part 210 | Upstate City Courts |
| `Part-212-District-Courts.md` | 22 NYCRR Part 212 | Nassau + Suffolk District Courts |
| `Part-214-Justice-Courts.md` | 22 NYCRR Part 214 | Justice Courts (Town and Village) |
| `Part-216-Sealing.md` | 22 NYCRR Part 216 | Sealing court records |
| `Part-220-Jury-Selection.md` | 22 NYCRR Part 220 | Jury selection and deliberation |
| `Part-221-Depositions.md` | 22 NYCRR Part 221 | Conduct of depositions |
| `Part-1200-Professional-Conduct.md` | 22 NYCRR Part 1200 | Rules of Professional Conduct (stub) |
| `Tanbook.md` | NY Law Reports Style Manual | Citation format (stub) |
| `NYC-CivilCourt-LR.md` | NYC Civil Court Directives | Civil Court local overlay (stub) |
| `Nassau-DC-LR.md` | Nassau District Court rules | Long Island District Court (stub) |
| `Suffolk-DC-LR.md` | Suffolk District Court rules | Long Island District Court (stub) |

> **NOT LEGAL ADVICE.** This corpus is a drafting aid; verify
> against the current canonical text before filing.
