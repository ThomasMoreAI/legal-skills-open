# Jurisdiction registry — index

Read this every run. Read the entry for the jurisdiction in play before fetching
anything. Read `_unmapped.md` if there isn't one.

Each entry carries the official publisher, the URL forms that work, the version
markers `read_version.py` matches against the fetched bytes, and the traps that
jurisdiction sets. Entries are written only after their markers have been
verified against two versions of a real instrument.

| Code | Publisher | Current text | The trap in one line |
|---|---|---|---|
| `EU` | eur-lex.europa.eu | Consolidated, but formally "no legal effect" | Neither text is both current and authoritative — read consolidated, cite the OJ. |
| `UK` | legislation.gov.uk | Revised, and running behind | "Up to date" and "changes yet to be applied" are both on the page and both true. |
| `US-FEDERAL` | www.ecfr.gov | The eCFR, daily, "authoritative but unofficial" | Three texts, not two: current-unofficial, official-annual, and the Federal Register notice the codification came from. |
| `US-CA` | leginfo.legislature.ca.gov | The section as it stands, with no banner anywhere | The version is one bracketed line at the foot of each section, and "effective" is not "operative". |
| `SG` | sso.agc.gov.sg | The text in force on any date you name | The Revised Edition line looks like a staleness warning and is not — only `Status:` answers that. |

Anything else → `_unmapped.md`. Do not guess a publisher, and do not let a
search engine pick one for you.

Two entries name a second publisher for part of the material: US federal
regulations are official on `www.govinfo.gov` in their annual edition, and the
California Code of Regulations is published for the state at `govt.westlaw.com`.
A commercial host is not automatically wrong — read the entry before deciding a
fetch went astray.

## How this is used

    python3 scripts/fetch_source.py <url> <outdir> --publisher <publisher> --label "<version>"
    python3 scripts/read_version.py <outdir>/source.html --jurisdiction <code>

`--publisher` comes from this registry, and `fetch_source.py` refuses to save
anything that redirects off that host. `read_version.py` exits non-zero when a
marker says the text is superseded or incomplete. When it does, refetch the
version the marker names — do not carry on and caveat it.

Exit 0 with no markers matched is **not** a clean bill of health. It means the
page did not carry the markers the entry expects, which usually means the
publisher changed its furniture. Establish the version by hand and fix the entry.

## Adding a jurisdiction

See `_unmapped.md`. The bar is two versions of one instrument, fetched, with the
markers watched both firing and staying silent.
