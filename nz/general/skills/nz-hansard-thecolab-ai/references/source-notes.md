# Source notes

- Owner/source: New Zealand Parliament Hansard, `https://hansard.parliament.nz/`
- Authentication: none
- Last verified: 2026-07-19
- Exact transcript pattern: `/hansard-transcript/YYYY-MM-DD`
- Access: public, read-only HTML; host `hansard.parliament.nz`

Exact sitting pages publish the official transcript with sitting date, volume, headings, questions and attributed speaker turns. The parser returns stable date-plus-heading debate IDs, full item text and bounded speaker turns with per-record source URL, retrieval time and transcript status. Heading/narrative boundaries prevent later sections from being attributed to the preceding speaker. `oral-questions` returns only items in the named section.

The Blazor host returns only its client shell for its browser-shaped request path but server-renders the official transcript for a lean curl-compatible request. This connector uses that bounded source-specific mode through `nzfetch`; no browser automation or access-control bypass is involved.

The official browse route is parsed only for canonical `/hansard-transcript/YYYY-MM-DD` links. `latest` returns that listing; undated search/speaker/bill commands search the latest five sittings by default and accept `--sittings` from 1 to 20, while `--date` selects one deterministic sitting. The CLI reports the bounded corpus in its warnings. Full-text search covers debate text rather than headings alone. Some networks receive Parliament's Radware challenge; that is an explicit blocked result, and the shared fetch layer retains user-configured proxy routing.
