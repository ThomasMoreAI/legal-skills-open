# EUIPO (EU Trade Marks + Registered Community Designs)

Read-only access to the European Union Intellectual Property Office's
Trademark Search and Design Search APIs. ~2.3M EUTMs and ~1.5M RCDs.

## Modules

```python
from patent_client_agents.euipo_trademarks import (
    EuipoTrademarksClient,
    SearchTrademarksInput,
    GetTrademarkInput,
    search_trademarks,
    get_trademark,
)
from patent_client_agents.euipo_designs import (
    EuipoDesignsClient,
    SearchDesignsInput,
    GetDesignInput,
    search_designs,
    get_design,
)
```

## Auth

OAuth2 client_credentials with scope `uid`. Both APIs share the same
dev-portal app. Set `EUIPO_CLIENT_ID` and `EUIPO_CLIENT_SECRET` in the
environment. Set `EUIPO_ENV=sandbox` to point at the sandbox (auto-approved
on subscription, but data is a frozen snapshot + synthetic test rows);
production access requires mailing identity documents to
`docs.apiplatform@euipo.europa.eu`.

## search_trademarks / get_trademark

```python
from patent_client_agents.euipo_trademarks import (
    SearchTrademarksInput,
    search_trademarks,
    GetTrademarkInput,
    get_trademark,
)

# All registered marks containing "Apple"
page = await search_trademarks(SearchTrademarksInput(
    query="wordMarkSpecification.verbalElement==*Apple* and status==REGISTERED",
    size=25,
    sort="applicationDate:desc",
))
print(page.total_elements, "matches")

# Full record by application number
tm = await get_trademark(GetTrademarkInput(application_number="000428557"))
print(tm.status, tm.application_language)
for gns in tm.goods_and_services:
    print(gns.class_number, gns.terms_in("en"))
```

## search_designs / get_design

```python
from patent_client_agents.euipo_designs import (
    SearchDesignsInput,
    search_designs,
    GetDesignInput,
    get_design,
)

# RCDs in Locarno class 14 (recording equipment), 2024 onwards
page = await search_designs(SearchDesignsInput(
    query="applicationDate>=2024-01-01 and locarnoClasses=in=(14.01,14.02,14.03)",
    sort="applicationDate:desc",
))

# Full record by design number (NNNNNNNNN-NNNN)
d = await get_design(GetDesignInput(design_number="099037115-0001"))
print(d.product_terms_in("en"))
```

## Query DSL (RSQL)

Filter syntax for `query`:

- `==` exact / `!=` not-equal — `markFeature==FIGURATIVE`
- `=in=` / `=out=` set membership — `niceClasses=in=(25,35)`
- `=all=` all-of — `niceClasses=all=(25,28,40)`
- Wildcards with `*` — `wordMarkSpecification.verbalElement==*Apple*`
- Comparators — `applicationDate>=2024-01-01`
- Combine with `and` / `or` / `not` plus parens

Field paths are dotted (e.g. `applicants.name`, `wordMarkSpecification.verbalElement`).

## Pagination

`page` is 0-indexed. `size` must be 10..100; the spec's `size=3` examples
will return HTTP 400. `total_pages = ceil(total_elements / size)`.

## Limits

- 25,000 calls/day per app on the Default Plan
- 7,200-second token lifetime; library refreshes automatically on 401
- HTTPS only; every request carries `Authorization: Bearer ...` + `X-IBM-Client-Id: ...`
