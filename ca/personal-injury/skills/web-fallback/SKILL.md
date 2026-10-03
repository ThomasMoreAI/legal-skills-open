---
name: web-fallback
title: 'Web fallback'
description: When the Harvester misses a citation, fetch the statute live from an authoritative government source, verify the section number actually appears on the page, then summarize ONLY the fetched text. Refuse cleanly if no verified source.
author: barndonmai
author_url: https://github.com/barndonmai/specter/tree/main/openclaw/skills/web_fallback
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ca
practice: personal-injury
language: en
---

# web-fallback

Specter's last line of defense before fabrication.

The Harvester is the source of truth. When it misses, we don't guess — we go to the authoritative legislature website, fetch the page, **anchor-check** that the cited section actually appears on it, and only then cite it.

## When to use this skill

- `harvester-query.lookup_citation()` returned `None` for a specific citation.
- User asks for a state we haven't ingested yet.
- User asks for a citation in a state we *have* ingested but the specific section is missing (renumbered, new amendment, etc.).

## When NOT to use it

- Don't use it for general semantic search ("DUI laws everywhere"). That's the Harvester's job.
- Don't use it for case law (this skill is statute-only).
- Don't use it as a *first* resort. Always Harvester first.

## The hard rule

**No fabrication, ever.** Per hackathon ground rules, "records without a real source URL don't count."

This skill enforces that with five rules:

1. **URL is built deterministically from the citation** — never asked from a language model.
2. **The fetched page must actually contain the section number** before we cite it.
3. **The model only summarizes** the fetched text — never invents content.
4. **Failed fetches return a structured miss** — Specter says "no verified source" rather than guessing.
5. **Only `.gov` / official legislature domains** are in the URL builder map.

## How to call

```bash
cd ~/Specter && python3 -m openclaw.skills.web_fallback.verify "Cal. Veh. Code § 22350"
```

```python
from openclaw.skills.web_fallback.verify import verify
result = verify("Cal. Veh. Code § 22350")
# {
#   "verified": True,
#   "citation": "Cal. Veh. Code § 22350",
#   "section": "22350",
#   "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=VEH&sectionNum=22350.",
#   "text": "<actual fetched statute text>",
#   "fetched_at": "2026-05-09T15:34:12Z"
# }
```

On failure:
```python
# {
#   "verified": False,
#   "citation": "Cal. Veh. Code § 99999",
#   "reason": "section number 99999 not found on fetched page"
# }
```

### Optional: summarize the verified text

If `verify()` succeeds and you want a Specter-voiced one-liner instead of the raw statute text:

```python
from openclaw.skills.web_fallback.summarize import summarize_verified
short = summarize_verified(result)  # one constrained sentence, no fabrication
```

`summarize_verified` calls Claude with a tightly-scoped prompt that forbids new facts beyond the supplied text. If `result["verified"]` is False, it returns `None` — never invents.

## Supported jurisdictions

URL builders are deterministic per state. Currently:

| State | Code | Source |
|---|---|---|
| California | `Cal. Veh. Code` | leginfo.legislature.ca.gov |
| Texas | `Tex. Transp. Code` | statutes.capitol.texas.gov |
| New York | `N.Y. Veh. & Traf. Law` | nysenate.gov |
| Florida | `Fla. Stat.` | leg.state.fl.us |
| Illinois | `625 ILCS` | ilga.gov |

For unsupported jurisdictions, `verify()` returns:
```json
{"verified": false, "reason": "no authoritative URL pattern for <code>"}
```

Specter should then say: *"No authoritative source on hand for {jurisdiction}. Worth ingesting."*

## Format for WhatsApp

If verified, Specter answers like this (per SOUL voice rules — short, cited, source URL flagged):

> Cal. Veh. Code § 22350. Basic speed law — drive no faster than reasonable for conditions.
> Pulled live from leginfo.legislature.ca.gov. Not in the Harvester yet — worth ingesting.

If not verified:

> No verified source for {citation}. I won't make one up.

That's the whole skill. Verify or refuse.
