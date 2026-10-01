# Source notes

- Owner: Office of the Clerk / New Zealand Parliament
- Authentication: none
- Last verified: 2026-07-19
- Base: `https://www3.parliament.nz/en/pb/sc/`
- Public listings: committee list, open submissions, business, evidence/submissions and reports
- Access: public and read-only; hosts `www3.parliament.nz`, `www.parliament.nz`

The parser reads Parliament listing rows and preserves title, committee, closing date/time and canonical item URL. Exact times are normalised with the explicit `Pacific/Auckland` timezone; a date-only source remains date-only. Bounded detail enrichment adds published committee membership and official evidence/submission/briefing links to committee, item and evidence commands. Missing detail fields remain missing rather than inferred.

No account or submission flow is implemented. Parliament may present Radware challenges; these are blocked states, not empty results. User-configured proxy routing remains available through the repository fetch layer.
