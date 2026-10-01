# nz-comcom — source & parsing notes

Source: **www.comcom.govt.nz** — the NZ Commerce Commission website, a
server-rendered **SilverStripe** CMS. Keyless, read-only; no login, API key, or
browser. (`comcom.govt.nz` 301-redirects to `www.comcom.govt.nz`.)

There is no public JSON API, but every listing on the site uses one repeated
**card component**, and pages are fully server-rendered, so the skill scrapes
deterministic HTML.

## Endpoints used

| Command | URL | Notes |
|---------|-----|-------|
| `search` | `/search/?q=<terms>` | Site-wide search; results are cards. Single page of results (the site does not expose reliable `?start=` paging here). |
| `cases`  | `/case-register/case-register-entries/` | Recent case register entries (≈10 cards: clearances, mergers, cartel, consumer credit, fair trading). `--keyword` instead searches site-wide and keeps only `/case-register/` results. |
| `news`   | `/news-and-media/news-and-events/` (optional `/<year>/`) | Media releases, decisions, and report announcements. |
| `page`   | any `comcom.govt.nz` URL/path | Fetches one page and extracts its summary + linked documents (reports/PDFs). |

## Card parsing

Listings share the `card--has-link` component; the leading class varies by page
(`card card--has-link`, `card card--media-release-page card--has-link`, …), so the
parser splits on the common `card--has-link` token. Per card it reads:

- `card__link" href="…">Title</a>` → title + URL
- `card__status…">…</div>` → Open / Closed (case register)
- `card__summary">…</div>` → summary (search / news)
- `card__info">…</div>` → sector / outcome (case register, e.g. "Consumer credit",
  "Outcome: Merger cleared")

## Document / report extraction (`page`)

Reports are linked as files or via the CMS asset store. The `page` command treats
a link as a document when its href contains `/assets/`, `/__data/`, `dmsdocument`,
or ends in `.pdf/.doc(x)/.xls(x)/.ppt(x)/.csv` — e.g.
`/assets/pdf_file/0029/228476/Market-studies-guidelines.pdf`. Favicons and theme
assets under `/_resources/` are not files of interest and are skipped by the
extension/asset-path test.

## Scope

Covers case register entries, news/media releases, site search, and per-page
document discovery — i.e. the Commission's public competition, consumer, and
regulated-industry (electricity, gas, telco, fibre, airports, dairy, grocery,
fuel) material. Bulk regulatory datasets that are published only as downloadable
spreadsheets are surfaced as document links via `page`, not parsed cell-by-cell.

## CI / smoke tests

`smoke_test.py` exercises `search`, `cases`, `news`, and `page`. All keyless;
network / upstream 5xx errors are treated as SKIP.
