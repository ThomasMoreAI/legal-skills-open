# Verifying Idaho Cases via CourtListener

> **NOT LEGAL ADVICE.** A verification procedure. A search hit confirms a
> case exists and lets you read the holding; it does not assess legal
> sufficiency. Confirm the proposition and current validity yourself.

Use the bundled **CourtListener** MCP server (and the **Legal Data
Hunter** MCP) to confirm that every Idaho case cited in a filing is real,
that the reporter cite is right, and that the case stands for what the
brief claims.

## Idaho court ids

| Court | CourtListener court id |
|-------|------------------------|
| Idaho Supreme Court | `idaho` |
| Idaho Court of Appeals | `idahoctapp` |

Restrict opinion searches to these ids when verifying an Idaho cite.

## Verification procedure

1. **Search by citation or party name.** Use the CourtListener `search`
   tool over the Opinions collection, filtered to court `idaho` and/or
   `idahoctapp`. Query by the reporter cite (e.g., `113 Idaho 730` or
   `747 P.2d 752`) or by the party names.
2. **Confirm the match.** Verify the party names, the reporter cite, the
   deciding court, and the year line up with what the brief asserts. A
   Court of Appeals decision must carry the "(Ct. App. YEAR)"
   parenthetical (see `references/idaho-citation-format.md`).
3. **Read the holding.** Use `read_document` / `search_document` on the
   matched opinion to confirm it actually stands for the cited
   proposition — do not rely on the headnote or a memory of the holding.
4. **Check it is still good law.** Note any later history; a cite that
   has been overruled or superseded is a FAIL even if the opinion exists.

## What to flag

- **FAIL** — no opinion found on `idaho` / `idahoctapp` matching the
  party names and cite; or the opinion does not support the proposition;
  or it has been overruled.
- **WARN** — the opinion exists but the reporter cite, year, or court
  parenthetical in the brief is off; the parallel P.2d/P.3d cite is
  missing.
- **PASS** — opinion found, cite correct, holding supports the claim,
  still good law.

## Notes

- CourtListener / Legal Data Hunter cover **case law**; for **statute**
  (Idaho Code) and **rule** (I.R.C.P. / I.R.E. / I.R.F.L.P. / I.A.R.)
  text, verify against `id-law-references`, not CourtListener.
- Idaho has **no neutral citation**, so verify against the Idaho Reports
  + Pacific Reporter cite, not a vendor-neutral identifier.

## Composition

- Citation form: `references/idaho-citation-format.md`
- Canonical statute / rule text: `id-law-references`
- On-demand case-law research generally: `case-law-research` (federal
  plugin)
