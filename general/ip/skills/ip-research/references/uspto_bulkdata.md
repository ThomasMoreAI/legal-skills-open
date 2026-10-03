# USPTO Bulk Data

Programmatic access to USPTO's bulk data product catalog (weekly patent
grants, weekly applications, assignments, etc.). Requires `USPTO_ODP_API_KEY`.

## Module

```python
from patent_client_agents.uspto_bulkdata import search_products, get_product
```

Low-level access is also available via
`patent_client_agents.uspto_odp.BulkDataClient`.

## search_products(query=None, ...)

Enumerate available bulk data products.

```python
response = await search_products(query="grant")
for product in response.bulkDataBag:
    print(product.productIdentifier, product.productTitle, product.publicationDate)
```

## get_product(product_identifier)

Fetch a single product's metadata and download manifest.

```python
product = await get_product("PTGRXML")
for f in product.productFiles:
    print(f.fileName, f.fileDownloadURI)
```

## Notes

- Download URIs are auth-required — use `ApplicationsClient` or the
  `BulkDataClient` directly to retrieve content with the API key attached.
- Product IDs live in USPTO's product catalog documentation; common ones:
  `PTGRXML` (patent grants XML), `PATAPPXML` (published applications XML),
  `ASSIGN` (assignment dataset).

See `src/patent_client_agents/uspto_bulkdata/data/` for bundled schemas and the 2025 Bulk
Data Product Guide.
