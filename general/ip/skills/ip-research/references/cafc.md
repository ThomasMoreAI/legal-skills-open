# Federal Circuit (CAFC) opinions

Search and download opinions from the US Court of Appeals for the Federal Circuit. The CAFC hears virtually every appeal in a US patent case — plus ITC §337, gov-contract, veterans, and TTAB appeals — so this is the primary appellate-law source for patent agents.

No API key required. The client extracts a WordPress nonce from the opinions page on first request and reuses it for the session.

## Module

```python
from patent_client_agents.cafc import (
    CAFCClient,
    CAFCOpinion,
    PatentClassifier,
)
```

## search(query, date_from, date_to, origins, max_results)

Search the upstream DataTables index. Returns `list[CAFCOpinion]`. Pass `query` to use the upstream search field (much faster than fetching everything and filtering client-side).

```python
from datetime import date
from patent_client_agents.cafc import CAFCClient

async with CAFCClient() as client:
    opinions = await client.search(
        query="IPR2024",
        date_from=date(2025, 1, 1),
        origins=["PTO"],
        max_results=50,
    )
    for op in opinions:
        print(op.release_date, op.appeal_number, op.case_name, op.is_patent_case)
```

## search_patent_opinions(date_from, date_to, max_results)

Convenience method — pre-filters origins to `PTO`, `DCT`, `ITC`, `CFC` (the four origins that carry patent appeals).

```python
patent_appeals = await client.search_patent_opinions(date_from=date(2025, 1, 1))
```

## recent(days)

Last *N* days across all origins.

```python
last_week = await client.recent(days=7)
```

## download_pdf(opinion, output_path=None)

Fetch the PDF bytes for an opinion. Pass `output_path` to also write to disk.

```python
pdf_bytes = await client.download_pdf(opinions[0])
await client.download_pdf(opinions[0], output_path="cafc_24-1234.pdf")
```

## Opinion shape

`CAFCOpinion` fields:

| Field | Notes |
|---|---|
| `appeal_number` | e.g. `24-1234`, `2023-1287` |
| `release_date` | `datetime.date` |
| `origin` | `PTO`, `DCT`, `ITC`, `CFC`, `CAVC`, `MSPB`, etc. |
| `document_type` | `OPINION`, `ORDER`, `RULE 36 JUDGMENT` |
| `case_name` / `case_name_short` | Full and short forms |
| `precedential_status` | `Precedential`, `Nonprecedential` |
| `file_path` / `pdf_url` | WordPress file path and absolute URL |
| `is_patent_case` | True if the classifier scored ≥0.5 confidence |
| `patent_confidence` | 0.0–0.95 |
| `patent_keywords` | Matched keywords (uspto, ipr, ptab, infringement, ...) |

## Origin codes (when to filter)

- `PTO` — appeals from the USPTO (PTAB IPR/PGR/CBM, ex parte appeals, reexams). Pure patent territory.
- `DCT` — district-court appeals. Most patent infringement cases live here.
- `ITC` — Section 337 investigations.
- `CFC` — Court of Federal Claims. Gov-contract patent disputes.
- `CAVC`, `MSPB` — veterans and federal employee appeals (not patent).

## Patent classifier

`PatentClassifier.classify(case_name, text_content=None)` returns `(is_patent, confidence, matched_keywords)`. Useful when you need to detect patent-relevance independently of origin (e.g. when scanning all recent opinions including non‑patent‑origin appeals).

```python
classifier = PatentClassifier()
is_patent, confidence, keywords = classifier.classify(
    "Apple Inc. v. Vidal, Director of the USPTO",
)
# (True, 0.9+, ["uspto", "vidal", ...])
```

False positives filtered: "patient care", "patent leather".

## Stability and ToS

- DataTables API is undocumented but stable for years. The WordPress nonce mechanism is the only fragile bit; if the theme is restyled and the `wdtNonceFrontendServerSide_1` hidden input goes away, the nonce regex needs updating.
- CAFC's CloudFront/WordPress stack blocks plain Python User-Agents with 403 on the AJAX endpoint; the client uses a desktop Chrome UA. No rate limits published.
- Opinions are public; the court's redistribution terms are standard for US federal court records.
