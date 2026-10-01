# NZ AI policy source map

This skill is an official-source map and briefing helper for New Zealand AI policy and guidance. It deliberately avoids asserting that guidance is binding law unless the source itself says so.

## Source categories

- `public-service-framework` - Digital.govt.nz framework and GCDO role material for central public-service AI system leadership.
- `responsible-ai-guidance` - Digital.govt.nz Responsible AI Guidance overview for public-service GenAI.
- `genai-foundations` - governance, security, procurement, accountability/responsibility.
- `customer-experience` - transparency, privacy, bias/discrimination, Māori/Pacific/ethnic communities.
- `work-programme` and `toolkit` - Public Service AI Work Programme, AI Toolkit, policy template, and records-management material.
- `algorithm-governance` - data.govt.nz Algorithm Charter and Algorithm Impact Assessment guide.
- `privacy` - Office of the Privacy Commissioner AI guidance.
- `national-strategy` - MBIE AI strategy and AI uptake/regulatory posture material.
- `official-information` - Public Service Commission OIA release PDF.

## Caveats for use

- This is not legal advice.
- Guidance and strategy material can change; cite the official URL and generated/fetched timestamp from the CLI output.
- Digital.govt.nz and data.govt.nz may return bot-protection HTML to plain `urllib` in some environments. The CLI reports `source_blocked_plain_http` and keeps the official source metadata instead of bypassing controls.
- The PSC OIA source is a PDF. The CLI confirms reachability and metadata with Python stdlib but does not extract full PDF text.
- Public Service guidance should not be assumed to apply unchanged to local government, Crown entities, schools, health organisations, council-controlled organisations, vendors, or private businesses.
- Use regulator/law sources for privacy-law questions and procurement/legal specialists for binding procurement or contractual advice.

## Recommended citation pattern

When answering users, include:

1. The official source title and agency.
2. The source URL.
3. The CLI `generated_at`, `searched_at`, or `fetched_at` timestamp.
4. The caveat: not legal advice; check current official wording.

Example:

> Source: Office of the Privacy Commissioner, "Artificial intelligence and privacy", https://www.privacy.org.nz/resources-and-learning/a-z-topics/ai/ (fetched 2026-07-02T...). Not legal advice; check current source wording.
