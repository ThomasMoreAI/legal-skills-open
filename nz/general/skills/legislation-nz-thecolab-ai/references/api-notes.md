# legislation-nz API Notes

## Official sources

- New Zealand Legislation website: `https://www.legislation.govt.nz/`
  - Official home for New Zealand Acts, Bills, and secondary legislation.
  - Canonical URLs use `/{type}/{subtype}/{year}/{number}/en/{version}/`.
  - PCO-drafted legislation has direct XML format URLs such as `.../en/latest.xml/`.
- PCO developer API: `https://api.legislation.govt.nz/docs/`
  - Endpoints documented as `/v0/works/`, `/v0/works/{work_id}/versions/`, and `/v0/versions/{version_id}/`.
  - The API requires a free key. Request it from `contact@pco.govt.nz` and agree to the API terms.
  - Set the key as `LEGISLATION_NZ_API_KEY` or `PCO_API_KEY` to use `search --source api`.
- Official web feeds:
  - The website publishes generated Atom/RSS feeds for all legislation, filtered searches, and document versions.
  - `updates` requests a feed URL through the public website feed generator, then parses the returned Atom XML.
- Bulk XML catalogue:
  - `https://catalogue.data.govt.nz/dataset/new-zealand-legislation`
  - Catalogue entry for the whole-corpus XML directory and related resources.

## Identifier notes

- Work IDs use `{type}_{subtype}_{year}_{number}`, for example `act_public_2003_52`.
- Version IDs add `_en_{version_date}`, for example `act_public_1990_109_en_2022-08-30`.
- The website accepts `latest` as the current-version alias. XML payloads expose the resolved `date.as.at`.
- Some agency-published secondary legislation uses ephemeral `~` identifier segments. Treat those IDs as less stable.

## Access caveats

- The clean developer API route is not keyless. Without a key, the API returns `401` and the CLI reports `api_key_required`.
- Keyless XML and web pages are official but can be affected by bot protection or upstream HTML changes. The CLI reports explicit `upstream_bot_protection`, `upstream_unexpected_html`, or `upstream_parse_error` states rather than fabricating data.
- Search/list parsing uses the current public website HTML. Prefer `--json` and keep `source_url` with quoted facts so future agents can verify if the page shape changes.
- The generated web-feed URL contains a feed-specific `api_key` parameter returned by the public website. This is not the PCO developer API key supplied by the user.

## Practical citation workflow

1. Use `search` to resolve the work when only a title is known.
2. Use `get-section ACT_ID SECTION --json` for exact text and source URL.
3. Use `versions ACT_ID --json` to check point-in-time history.
4. Use `updates --since YYYY-MM-DD --json` to flag recently published matching legislation.
