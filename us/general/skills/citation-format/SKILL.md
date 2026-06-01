---
name: citation-format
title: citation-format
description: Normalize messy citation strings ("CVC 23152a", "California Vehicle Code Section 23152(a)") into canonical form ("Cal. Veh. Code § 23152(a)") before passing to harvester-query.
author: barndonmai
author_url: https://github.com/barndonmai/specter/tree/main/openclaw/skills/citation_format
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: general
language: en
---

# citation-format

Users (and judges, on live demo queries) will type citations any number of ways. The Harvester's `/lookup` is exact-string match — it'll miss otherwise valid citations because of formatting drift. This skill normalizes them.

## When to use this skill

- Right before calling `harvester-query.lookup_citation(...)` if the user-provided citation isn't already in canonical form.
- When you're not sure if a citation is canonical, just run it through `normalize()` — it's idempotent.

## Canonical form (CA Vehicle Code example)

```
Cal. Veh. Code § 23152(a)
```

- `Cal. Veh. Code` — the universal citation prefix (state-specific)
- ` § ` — section sign with thin spaces
- `23152(a)` — section number with subsection

## Use

```python
from openclaw.skills.citation_format.normalize import normalize

normalize("CVC 23152a")                          # → "Cal. Veh. Code § 23152(a)"
normalize("California Vehicle Code Section 23152(a)")
normalize("cal veh § 23152(a)")
```

From shell:

```bash
cd ~/Specter && python3 openclaw/skills/citation_format/normalize.py "CVC 23152a"
```

## Rules of thumb

1. If you have already-canonical form (`Cal. Veh. Code § 23152(a)`), pass through unchanged.
2. If user gives just a section number (`23152(a)`) and context is clearly California, prepend `Cal. Veh. Code § `.
3. **Don't guess across jurisdictions.** If the user just says "23152(a)" with no state, ask which state. Don't default to CA silently.

## Out of scope

- Case citations (e.g. *Smith v. Jones*) — this is statute-only.
- Federal citations (CFR, USC) — vehicle codes are state-level.
- Resolving statutes that have been renumbered. Out of scope for hackathon.
