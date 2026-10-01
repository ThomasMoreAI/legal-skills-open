# Source notes

- Owner/source: New Zealand Gazette, `https://gazette.govt.nz/`
- Authentication: none
- Access: public, read-only, server-rendered HTML; no account or API key
- Host allowlist: `gazette.govt.nz`
- Last verified: 2026-07-19
- Update cadence: notices are continuously published

## Implemented surface

The official search form supplies keyword, date, notice-type and Act filters. Search results expose the publication date, notice ID, concise visible title, type and legislation; commented preview text is excluded. Exact notice pages expose the official text, authority tags, amendment/revocation/correction relationships when explicitly stated, edition metadata and PDF link. The parser fails with a schema error when expected records disappear instead of reporting an invented empty result.

The connector is retrieval only. It does not determine legal effect, infer relationships between similarly named notices, or claim that a search is legal advice. Check the linked official notice for amendments, revocations and corrections. Bounded user-configured proxy routing remains supported by the repository fetch layer.
