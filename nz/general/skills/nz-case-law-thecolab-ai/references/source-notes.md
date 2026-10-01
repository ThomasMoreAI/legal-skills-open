# Source notes

- Owner/source: Courts of New Zealand, `https://www.courtsofnz.govt.nz/judgments`
- Authentication: none
- Last verified: 2026-07-19
- Parsed surfaces: Supreme Court judgment catalogue and Supreme Court, Court of Appeal, High Court and other-court public-interest pages
- Access: public and read-only; hosts `courtsofnz.govt.nz`, `www.courtsofnz.govt.nz`

Each result preserves the case name, neutral citation, court, judgment date, source summary and official PDF link. High Court and Court of Appeal public-interest pages generally retain only 90 days and are not exhaustive. Judicial Decisions Online remains the broader Ministry source but no stable documented bulk API was found.

The connector does not parse suppressed material from PDFs or infer parties, judges or outcomes absent from a source. Text, citation, judgment-ID and judge queries use the Courts site's official full-text search route and retain both search-result and canonical case-page provenance. Because that search can return weak or unrelated hits, the connector independently requires the requested text in the published result/case metadata. The case pages do not expose a structured judge-panel field, so `judge` additionally requires published judge context such as `Cooke J` or `Justice Cooke`, returns the matching evidence, and directs users to verify the complete panel in the linked judgment. It never treats a bare party-name match as judge attribution. Users must comply with suppression and republication restrictions. This is retrieval, not legal advice.
