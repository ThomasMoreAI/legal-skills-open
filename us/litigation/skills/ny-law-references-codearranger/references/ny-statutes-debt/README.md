# ny-statutes-debt Corpus — New York

Verbatim text of selected New York consolidated-laws articles covering
the full civil-practice surface — procedure, evidence, fees,
limitations, exemptions, garnishment, family law, landlord-tenant,
consumer-debt, UCC enactment, debt-collection licensing.

The directory name is retained for path stability; the scope is no
longer "debt-only" despite the slug.

## Sources

- **NY State Senate Open Legislation API** — canonical machine-readable
  source for the consolidated laws. Endpoint:
  `https://legislation.nysenate.gov/api/3/laws/{lawId}/{locationId}`.
  Free API key registration at:
  `https://legislation.nysenate.gov/static/docs/html/#api-key-registration`.
  Set `NYSENATE_API_KEY` in the environment to enable the API path.

## Target catalog

| lawId | Slice | Topic |
|---|---|---|
| `CVP` | A1-A53 (14 articles) | Civil Practice Law and Rules (CPLR) — procedure, evidence, judgments, enforcement |
| `GOB` | T5, T17 | General Obligations Law — interest, statute of frauds, revival of debts |
| `GBS` | A22A, A29H | General Business Law — §§ 349-350 deceptive-practices and the NY mini-FDCPA |
| `RPA` | A7, A13 | RPAPL — summary proceedings (Articles 7, 7-A, 7-B) and mortgage foreclosure |
| `RPP` | A7 | Real Property Law — landlord and tenant baseline |
| `UCC` | A2, A3, A9 | NY enactment of the Uniform Commercial Code |
| `DOM` | A9, A11, A5B | Domestic Relations — divorce, child support, UIFSA |
| `EPT` | A5 | Estates, Powers and Trusts — family rights |
| `GCN` | full | General Construction Law — holidays / time computation |
| `BNK` | A12-A, A12-G | Banking — mortgage bankers and student-loan servicers |

Each row is one output MD file (e.g. `CVP-Article-31-Disclosure.md`).
The full catalog (~31 files) is defined in `scripts/pull_ny_statutes.py`.

## How to refresh

```bash
# With an API key (the canonical path — produces verbatim statutory text):
export NYSENATE_API_KEY=<your-key>
python3 scripts/pull_ny_statutes.py --workers 4 \
    --out plugins/ny-court-docs/skills/ny-law-references/references/ny-statutes-debt

# Without an API key (stub mode — writes pointer stubs):
python3 scripts/pull_ny_statutes.py --workers 4 --stubs-only \
    --out plugins/ny-court-docs/skills/ny-law-references/references/ny-statutes-debt

# Refresh one target:
python3 scripts/pull_ny_statutes.py --only CVP-Article-31-Disclosure
```

The puller follows a **conditional-API** pattern: when
`NYSENATE_API_KEY` is set, it pulls verbatim JSON from the Open
Legislation API and renders Markdown. When the key is unset, it
writes well-formed pointer stubs so the corpus's shape is honest
about the gap. A successful API-mode refresh never regresses
existing verbatim content to a stub.

## File naming convention

`<lawId>-<short-label>.md`

Examples:
- `CVP-Article-31-Disclosure.md` — CPLR Article 31 (Discovery)
- `GBS-Article-29H-Debt-Collection.md` — GBL Article 29-H (NY mini-FDCPA)
- `RPA-Article-7-Summary-Proceedings.md` — RPAPL Article 7 (housing)
- `UCC-Article-9-Secured.md` — NY UCC Article 9 (Secured Transactions)

> **NOT LEGAL ADVICE.** This corpus is a drafting aid; verify against
> the current canonical text before filing.
