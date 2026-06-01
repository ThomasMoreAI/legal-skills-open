---
name: courtlistener
title: CourtListener REST API v4
description: Search U.S. case law, PACER dockets, judges, oral arguments, and citations via CourtListener REST API v4. Use bash+curl+jq against https://www.courtlistener.com/api/rest/v4/.
author: PlebeiusGaragicus
author_url: https://github.com/PlebeiusGaragicus/dot-pi/tree/main/shared/skills/courtlistener
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# CourtListener REST API v4

Use `curl` + `jq` to query CourtListener. Do NOT scrape the HTML website — it is blocked by CloudFront WAF. Always use the API endpoints below.

Base URL: `https://www.courtlistener.com/api/rest/v4/`

Anonymous access works (no token needed) but has lower rate limits. Authenticated users get 5,000 requests/hour.

## Search API (primary entry point)

The search endpoint mirrors the website's search with `GET` parameters:

```bash
curl -s "https://www.courtlistener.com/api/rest/v4/search/?q=QUERY&type=o" | jq '.results[:5]'
```

### Type parameter

| Value | Data |
|-------|------|
| `o` | Case law opinions (default) |
| `r` | RECAP dockets + up to 3 nested docs |
| `rd` | RECAP filing documents only |
| `d` | Federal dockets only |
| `p` | Judges |
| `oa` | Oral argument audio |

### Examples

```bash
# Case law search
curl -s "https://www.courtlistener.com/api/rest/v4/search/?q=fourth+amendment+cell+phone&type=o" \
  | jq '.results[:3] | .[] | {caseName, dateFiled, court, citation, cluster_id}'

# PACER docket search
curl -s "https://www.courtlistener.com/api/rest/v4/search/?q=Apple+v+Epic&type=r" \
  | jq '.results[:3] | .[] | {caseName, docketNumber, court, dateFiled}'

# Judge search
curl -s "https://www.courtlistener.com/api/rest/v4/search/?q=Ketanji+Brown+Jackson&type=p" \
  | jq '.results[:3]'

# Oral arguments
curl -s "https://www.courtlistener.com/api/rest/v4/search/?q=qualified+immunity&type=oa" \
  | jq '.results[:3] | .[] | {caseName, dateArgued, court, download_url}'
```

### Advanced operators

Use the same field operators as the website in the `q` parameter:

- `caseName:Smith` — filter by case name
- `docketNumber:23-1234` — filter by docket number
- `court:scotus` — filter by court ID
- `dateFiled:[2024-01-01 TO *]` — date range
- `citeCount:[10 TO *]` — minimum citation count
- `status:Published` — publication status

Full operator list: https://www.courtlistener.com/help/search-operators/

### Ordering and highlighting

```bash
# Order by date filed descending
curl -s "...&order_by=dateFiled+desc" | jq ...

# Enable snippet highlighting
curl -s "...&highlight=on" | jq '.results[0].opinions[0].snippet'
```

## Case Law Detail

After finding a `cluster_id` from search, retrieve full case details:

```bash
# Get cluster metadata
curl -s "https://www.courtlistener.com/api/rest/v4/clusters/2812209/" \
  | jq '{case_name, date_filed, citations, sub_opinions}'

# Get opinion text (use field selection to limit payload)
curl -s "https://www.courtlistener.com/api/rest/v4/opinions/6489975/?fields=id,type,html_with_citations" \
  | jq '{id, type, text: .html_with_citations[:2000]}'
```

### Filtering case law endpoints

```bash
# Opinions in a specific court
curl -s "https://www.courtlistener.com/api/rest/v4/opinions/?cluster__docket__court=scotus" \
  | jq '.results[:3] | .[] | .id'

# Cluster by docket number + court
curl -s "https://www.courtlistener.com/api/rest/v4/clusters/?docket__docket_number=23A994&docket__court=scotus" \
  | jq '.results[:3]'
```

## PACER / Docket Data

```bash
# Look up a docket by number and court
curl -s "https://www.courtlistener.com/api/rest/v4/dockets/?docket_number=1:16-cv-00745&court=dcd" \
  | jq '.results[:1] | .[] | {id, case_name, date_filed, date_terminated}'

# Get docket by ID
curl -s "https://www.courtlistener.com/api/rest/v4/dockets/4214664/" \
  | jq '{case_name, docket_number, court_id, date_filed, date_last_filing}'
```

Follow `docket_entries`, `parties`, and `attorneys` links from the docket object for deeper data.

## Judges

```bash
# Search by name
curl -s "https://www.courtlistener.com/api/rest/v4/people/?name_last=Jackson&name_first=Ketanji" \
  | jq '.results[:3] | .[] | {id, name_first, name_last, date_dob}'
```

Positions, education, and financial disclosures are linked from the person object.

## Oral Arguments

```bash
curl -s "https://www.courtlistener.com/api/rest/v4/audio/?docket__court=scotus&order_by=-date_created" \
  | jq '.results[:3] | .[] | {id, case_name, date_argued, download_url}'
```

## Citation Lookup (verify citations / fight hallucinations)

```bash
# Look up a single citation
curl -s "https://www.courtlistener.com/api/rest/v4/citation-lookup/?text=410+U.S.+113" \
  | jq '.'

# Bulk: POST a block of text to parse all citations in it
curl -s -X POST "https://www.courtlistener.com/api/rest/v4/citation-lookup/" \
  -H "Content-Type: application/json" \
  -d '{"text": "See Roe v. Wade, 410 U.S. 113 (1973) and Brown v. Board of Education, 347 U.S. 483 (1954)."}' \
  | jq '.'
```

## Query Refinement

These apply to all non-search endpoints (clusters, opinions, dockets, people, audio):

- **Field selection**: `&fields=id,case_name,date_filed` (reduces payload)
- **Omit fields**: `&omit=html_with_citations`
- **Pagination**: follow the `next` URL in responses
- **Counting**: `&count=on` returns only `{"count": N}`
- **Date filters**: `&date_filed__gte=2024-01-01&date_filed__lte=2024-12-31`
- **Ordering**: `&order_by=-date_modified` (prefix `-` for descending)
- **Exclusion**: `&court__jurisdiction!=F` (prepend `!` to exclude)

## Authentication (optional)

If you have a token, add it for higher rate limits:

```bash
curl -s --header 'Authorization: Token YOUR_TOKEN' \
  "https://www.courtlistener.com/api/rest/v4/search/?q=QUERY" | jq ...
```

Get a token from your CourtListener profile page.

## Reference Links

- Full API docs: https://wiki.free.law/c/courtlistener/help/api/rest/v4/overview
- Advanced search operators: https://www.courtlistener.com/help/search-operators/
- Jurisdiction list: https://www.courtlistener.com/help/api/jurisdictions/
- Data coverage: https://www.courtlistener.com/help/coverage/
- Relative date queries: https://www.courtlistener.com/help/relative-dates/
