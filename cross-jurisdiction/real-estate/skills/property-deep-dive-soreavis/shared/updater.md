# Country Playbook Updater

The skill includes a maintenance mode for keeping country playbooks fresh and source URLs alive.

## When to use

- **Quarterly maintenance** — re-validate URLs, refresh price benchmarks
- **After a known regulatory change** (e.g., new EU regulation, national tax reform)
- **Before a high-stakes use** — if the user is about to make a real purchase decision, run the updater first
- **Annually** for full re-research of a country's tax + price + rental sections (these change most)
- **As-needed** when a user reports a broken URL or stale data

## Invocation

```
/property-deep-dive --update                          # update ALL populated countries
/property-deep-dive --update=<iso2>                   # update one country
/property-deep-dive --update=<iso2>,<iso2>,...        # update specific list
/property-deep-dive --update --validate-only          # URL liveness only (fast, no re-research)
/property-deep-dive --update --refresh-only           # re-research data only (skip URL check)
/property-deep-dive --update --add=<iso2>             # populate a scaffold country fully (one-shot)
/property-deep-dive --update --diff                   # show planned changes; do not write
/property-deep-dive --update --interactive            # confirm each playbook before writing
```

**Defaults**:
- `--update` alone = validate URLs **AND** refresh data, for **all populated countries**
- `--validate-only` skips re-research (faster; use weekly/monthly)
- `--refresh-only` skips URL check (use when you trust URLs are current)
- `--diff` shows the planned diff without writing — always run this first if uncertain

## Updater workflow

For each target country, the skill executes these steps in order:

### Step 1 — Inventory current playbook

Read `countries/<iso2>/playbook.md` and extract:
- All markdown link URLs `[text](url)`
- All plain URLs in code blocks and tables
- All "as of <date>" tags
- All numeric benchmarks (€/m², tax rates, thresholds, occupancy figures)
- All "Status: <X>" + "researched <date>" timestamp at the bottom

Build an inventory:
```
inventory:
  iso2: <iso2>
  last_researched: <date>
  url_count: <N>
  numeric_facts:
    - {item: "TFPB rate Adriers", value: "32.90 %", asof: "2024"}
    - {item: "OMI seconda casa BTP-IMU", value: "1.06 % max", asof: "2025"}
    - ...
  urls:
    - https://example.gov/path/to/source
    - ...
```

### Step 2 — Validate URLs (unless `--refresh-only`)

For each URL, perform an HTTP HEAD (fall back to GET) and classify:

| Status | Action |
|---|---|
| **2xx** (200, 204) | ✅ alive — keep |
| **301/302/308** | 🟡 redirect — note the new URL; replace if redirect is permanent and stable |
| **403** behind login wall (Cloudflare, paywall) | 🟡 verify manually — keep but note auth required |
| **404** | 🔴 broken — search for replacement; if no replacement, mark deprecated |
| **5xx** (transient) | 🟡 retry once; if persistent, flag for manual review |
| **timeout / network error** | 🟡 retry; if persistent, flag |
| **DNS failure** | 🔴 domain dead — find replacement |

Implementation:

```bash
# Use curl with --head, fallback to GET on HEAD failure
for url in $URLS; do
  status=$(curl -s -o /dev/null -w "%{http_code}" \
    --max-time 10 --head -L \
    -H "User-Agent: Claude-property-deep-dive/1.0" \
    "$url")
  if [ "$status" -ge 400 ] || [ -z "$status" ]; then

    # retry with GET (some servers reject HEAD)
    status=$(curl -s -o /dev/null -w "%{http_code}" \
      --max-time 15 -L \
      -H "User-Agent: Claude-property-deep-dive/1.0" \
      "$url")
  fi
  echo "$status $url"
done
```

Throttle rate to **5 requests/sec per domain** to avoid bot blocks.

For each broken URL → run a focused WebSearch for the replacement:
- Search: `<domain> "<exact path keyword>" site:<gov-domain>`
- If government sources have moved (e.g., reorganization), try the parent department
- Replace the URL in the playbook with the new one + add `(updated YYYY-MM-DD)` annotation

### Step 3 — Refresh data (unless `--validate-only`)

For each country, re-research the **fast-changing sections**:

| Section | Re-research cadence | What to refresh |
|---|---|---|
| `--price` | Quarterly | Average €/m² benchmarks, listing trend (YoY %), top platforms still active |
| `--tax` | Annually (or after reform) | Local rates, transaction taxes, VAT rates, thresholds |
| `--rental` | Quarterly | Short-let regulation status, classification fees, EU regulation transposition |
| `--risks` | Annually | New PPRN/PPR, climate projections updates |
| `--mains` | Annually | Operator changes (mergers, privatizations) |
| `--traffic` | Every 5 yrs | Major recensus / CSD updates |
| `--work` | Annually | Job platforms still relevant, salary benchmarks |

Use **WebSearch + Tavily** to verify each numeric fact:
- Old fact: `IMU seconda casa max 1.06 %`
- Search: `"IMU seconda casa" 2025 aliquota massima`
- New fact: confirm or update

For sections that are **stable** (e.g., diagnostic obligations, build-era hazards), skip the re-research unless URL validation flagged a primary source as broken.

### Step 4 — Diff and confirm

Build a structured diff:

```markdown
## Planned changes for <country>

### URL changes
- 🔴 BROKEN: <old_url>
  → REPLACE: <new_url>
- 🟡 REDIRECT: <old_url>
  → UPDATE: <new_url>

### Data refreshes
- TFPB Adriers: 32.90 % → **34.20 %** (source: impots-locaux.org Nov 2026)
- IMU seconda casa: max 1.06 % → unchanged (re-verified 2026-04)
- ...

### Section additions
- New regulatory item: "..."

### Section deletions
- Removed obsolete reference to ...
```

If `--diff` flag: print this and stop.
If `--interactive` flag: print and ask "Apply changes? [y/N/edit]".
Else: apply automatically and log to update history.

### Step 5 — Apply changes

For each affected country:
1. Backup current playbook to `countries/<iso2>/playbook.md.bak-<YYYY-MM-DD>`
2. Edit the playbook with the new URLs and data
3. Update the **status footer**:
   ```markdown
   ## Status

   ✅ **Fully populated**, last updated 2026-MM-DD.
   **Coverage check**: ... (re-validated)
   **Confidence**: <recompute based on new sources>
   ```
4. Append a **Update log** at the bottom:
   ```markdown
   ## Update history

   - **2026-04-25** — Initial population
   - **2026-07-15** — Quarterly refresh: updated 12 URLs (8 redirects + 4 broken-replaced); refreshed price benchmarks Q2 2026; noted DPH change effective Sep 2026
   - **2026-10-10** — Annual tax refresh: TFPB rate Adriers 32.90 % → 34.20 %; new RVLLH delay confirmed
   ```

### Step 6 — Report

Output a maintenance report:

```markdown
# Property-deep-dive Updater Run — 2026-MM-DD

## Summary
- Countries processed: <N>
- URLs validated: <total>
- URLs broken: <count> (replaced: <count>, deprecated: <count>)
- URLs redirected: <count>
- Data facts refreshed: <count>
- Data facts unchanged: <count>
- Time elapsed: <X>m

## Per-country status

### FR 🇫🇷
- 47 URLs checked, 45 ✅, 2 redirects updated
- 8 numeric facts re-verified, 1 changed (TFPB Adriers 32.90 → 34.20 %)
- Status: HEALTHY

### IT 🇮🇹
- 38 URLs checked, 35 ✅, 1 broken (replaced), 2 redirects
- 12 numeric facts re-verified, 3 changed (cedolare secca limit dropped from 4 to 2 properties effective 2026)
- Status: HEALTHY

### CZ 🇨🇿
- ...

## Action items
- [ ] Manual review: <url1> behind paywall (kept)
- [ ] Verify: <claim> needs fresh primary source
```

Save report as `_local/reports/property-deep-dive-update-<YYYY-MM-DD>.md`.

## Auto-downgrade — confidence decay rule

The skill cannot be re-run on every country every week. To stop stale data masquerading as HIGH confidence, **every section's confidence label decays automatically over time** and is recomputed **at render time** (every `--<section>` invocation), not only during `--update` runs.

### The decay ladder

Without re-verification, confidence drops one tier per interval:

| Original label | After 6 months | After 12 months | After 18 months |
|---|---|---|---|
| **HIGH** | MEDIUM | LOW | STALE |
| **MEDIUM** | LOW | STALE | STALE |
| **LOW** | STALE | STALE | STALE |

`STALE` is a distinct fourth tier (not in `anti-hallucination.md`'s original three) introduced here for the auto-downgrade flow. It means: *the data is older than any sensible reuse window — surface a warning before the user reads any number from it.*

### The `last-verified` field

Every section's confidence depends on a `**Last verified**: YYYY-MM-DD` stamp.

**Resolution order** (first match wins):
1. Section-level explicit stamp: `**Last verified**: 2026-04-26 — re-checked tax rates against ANAF`
2. Playbook-level Status footer: `✅ **Fully populated** as of 2026-04-25`
3. Playbook file mtime (filesystem fallback) — only if neither of the above exists

**Backfill is not required.** Existing playbooks need not be edited; they default to the Status footer date until a section is individually re-verified.

### Render-time decay calculation

```python
# pseudocode — runs every time a section is rendered
def effective_confidence(section, today):
    last_verified = resolve_last_verified(section)  # see resolution order above
    age_days = (today - last_verified).days
    original = section.confidence  # HIGH / MEDIUM / LOW
    
    # Step down per 6-month interval, floor at STALE
    steps = age_days // 180
    ladder = ["HIGH", "MEDIUM", "LOW", "STALE"]
    start_idx = ladder.index(original)
    new_idx = min(start_idx + steps, len(ladder) - 1)
    
    # Override 1: regulatory-watch entry since last_verified makes age irrelevant
    if has_unprocessed_regwatch_entry(section, since=last_verified):
        return "STALE"  # force re-verify regardless of age
    
    # Override 2: user passed --override-confidence
    if user_override:
        return user_override
    
    return ladder[new_idx]
```

### Render-time banners

When a section's effective confidence has been auto-downgraded, the banner appears **immediately above the section content**:

| Effective | Banner |
|---|---|
| HIGH (no decay) | *(no banner — render normally)* |
| MEDIUM (decayed from HIGH) | `> ⏱️ **Auto-downgraded HIGH → MEDIUM** (last verified <date>, <N> months ago). Numbers in this section may have moved; verify before high-stakes use.` |
| LOW (decayed from HIGH or MEDIUM) | `> ⚠️ **Auto-downgraded to LOW** (last verified <date>, <N> months ago). Treat all numbers as indicative only; re-research before relying on them.` |
| STALE | `> 🛑 **STALE — last verified <date>, <N> months ago.** This section is past the reuse window. Either run `/property-deep-dive --update=<iso2>` or pass `--override-confidence=LOW` to acknowledge the staleness.` |

The banner uses Markdown blockquote (`> `) so it stands out without breaking the surrounding flow.

### `regulatory-watch.md` override

The decay calculation is **bypassed to STALE** if `shared/regulatory-watch.md` has a Tier 1 or Tier 2 entry whose `enacted_date` is **after** the section's `last_verified` AND whose `playbook_sections_touched` includes the rendered section.

Why: a fresh tax reform (e.g., RO VAT 19→21% Aug 2025) makes a 4-month-old `--tax` stamp meaningless if the playbook still asserts 19%. The regulatory-watch entry is the authoritative signal that "something changed since you last looked," regardless of the calendar.

When this override fires, the banner is:

```markdown
> 🛑 **REGULATORY-WATCH FLAG** — `shared/regulatory-watch.md` logs a <Tier> reform for <country> on <enacted_date> touching this section. Last verified <date> predates the reform. Output suppressed until the playbook is re-stamped — run `/property-deep-dive --update=<iso2>`.
```

For Tier 1 (CRITICAL — e.g., visa programs ENDED, ownership rules reversed) the section content is **not rendered** at all; only the banner appears with a verification path. For Tier 2 the section renders but with the banner above and every affected number tagged `(may be superseded by <reform> — see regulatory-watch.md)`.

### Override flag

`--override-confidence=<HIGH|MEDIUM|LOW>` lets the user (or a trusted operator) acknowledge the staleness and continue. Use cases:
- The user just hand-verified a section against the source URL and is ready to continue without running a full update.
- The decay calc is wrong (e.g., the section is genuinely stable like commune-level INSEE pop figures from 2024 census — those don't decay in 6 months).
- A run is exploratory and rough numbers are acceptable.

The override is **per-invocation, not persisted**. To make it persistent, the user must update the playbook's `**Last verified**` stamp (which is what `--update` does).

### Status footer extension

The playbook-level Status footer is extended with a **per-section verification table** when sections have been individually re-stamped:

```markdown
## Status

✅ **Fully populated** as of 2026-04-25.
**Confidence**: HIGH for tax + risk + rental sources (multi-source corroborated). MEDIUM for work catchment heuristics (region-dependent).

### Per-section verification (overrides playbook-level date)

| Section | Last verified | Verifier | Notes |
|---|---|---|---|
| `--tax` | 2026-09-15 | auto-validate cron | All ANAF + impots-locaux URLs 200; rates re-checked |
| `--rental` | 2026-08-01 | manual (Loi Le Meur reform) | Regulation re-read; STR thresholds confirmed |
| `--risks` | 2026-04-25 | initial population | (defaults to playbook date) |
```

This table is **optional**. Sections without an entry default to the Status footer date.

### Confidence override syntax in the playbook itself

Inside a section, an explicit re-stamp overrides the playbook-level date:

```markdown
## Tax — France

**Last verified**: 2026-09-15 — re-checked TFPB Adriers 32.90% against impots-locaux.org Sep 2026 publication.
**Confidence**: HIGH

[section content...]
```

The `**Last verified**: <date>` line, when present, is the authoritative timestamp for that section.

### Cron interaction

`shared/auto-validate.md`'s weekly URL-liveness pass does **not** re-stamp `Last verified`. URL-200 ≠ data-still-current. Only `--update` (data-refresh mode) re-stamps. This separation is intentional: the validator catches dead links, the updater catches stale facts.

### Reporting

`/property-deep-dive --health-report` (new flag) generates a per-country / per-section decay matrix:

```markdown
# Decay Health Report — 2026-10-15

| Country | Section | Stamped | Effective | Days old | Banner |
|---|---|---|---|---:|---|
| FR | --tax | 2026-09-15 | HIGH | 30 | (none) |
| FR | --rental | 2026-08-01 | HIGH | 75 | (none) |
| FR | --risks | 2026-04-25 | MEDIUM (was HIGH) | 173 | ⏱️ |
| IT | --tax | 2026-04-26 | MEDIUM (was HIGH) | 172 | ⏱️ |
| IT | --rental | 2026-04-26 | STALE — regwatch flag | 172 | 🛑 (cedolare 4→2 reform) |
| ... | | | | | |

## Action queue
1. 🛑 IT --rental — regulatory-watch flag (cedolare secca limit dropped, effective 2026-01-01); update before next render
2. ⏱️ FR --risks — decayed to MEDIUM; quarterly refresh window opening
3. ...
```

This is a maintenance dashboard, not an output-blocking gate. Run it monthly to plan the next `--update` batch.

### Why decay, not freshness-on-demand?

Two design choices considered:

| Approach | Pro | Con |
|---|---|---|
| **Freshness-on-demand** (re-research every section every render) | Always current | 30-min cost per render; impossible at scale |
| **Decay + re-stamp** (this design) | Cheap render; honest about age | Needs a re-stamp loop |
| **Status quo** (manual confidence labels, no decay) | Simplest | Confidence labels rot silently — the failure mode this rule fixes |

The decay rule's job is to make staleness **visible** — not to fix it. The fix is `--update`. The rule guarantees that a 14-month-old playbook never silently displays "Confidence: HIGH".

---

## Strict rules

1. **Never fabricate URL replacements.** If a broken URL cannot be replaced via search, mark it `❌ DEPRECATED — primary source removed; verify with <fallback authority>`.
2. **Always backup before writing.** `playbook.md.bak-<date>` files are kept for 30 days.
3. **Anti-hallucination layer applies in full.** All eight pre-output checks (`shared/anti-hallucination.md`) must pass before write.
4. **Don't silently change "as of" dates.** Each numeric fact's "as of" date must be verifiable from the new source — don't re-stamp dates without re-verifying.
5. **Per-domain rate limit**: 5 req/sec to government domains; 2 req/sec to private platforms.
6. **Respect robots.txt** for any non-government source.
7. **Provenance preserved.** Every changed line in the playbook must have a corresponding entry in the update log explaining what changed and why.

## Failure modes

- **Mass URL failures** (>30 % broken): possible domain reorganization or DNS issue → don't auto-replace; create a flag report and stop.
- **Tavily / WebSearch quota exhausted**: pause, save partial progress, output `partial-update` report.
- **Conflicting sources** (two primary sources giving different numbers): always surface both; don't silently pick one. The diff shows both options; the user picks via `--interactive`.
- **Country playbook completely out of date** (e.g., country never re-researched in 2+ years): trigger a **full re-research** instead of incremental update.

## Scaffold population (`--add=<iso2>`)

When the user passes `--update --add=<iso2>` for a country with only a scaffold:

1. Read the scaffold (115-ish lines, structure-only)
2. Identify each section's TODO items
3. Run focused research:
   - Cadastre + price platforms (1–2 primary, 2–3 listing)
   - Traffic data sources
   - Tax structure (annual + transaction)
   - Rental regulations + 2025-2026 reforms
   - Risk registries (flood, earthquake, radon, landslide)
   - Mains drains operators
   - Mandatory diagnostics
   - Common quirks
4. Write the full populated playbook (target 300–500 lines, FR/IT/CZ/SK density)
5. Update the master SKILL.md country support matrix
6. Move scaffold to `countries/<iso2>/playbook.md.scaffold-<date>` (preserved for review)

This is a one-shot ~30-minute research investment per country.

## Health check (read-only mode)

`/property-deep-dive --update --validate-only` is the lightweight quarterly check.

Output format:
```markdown
# Health Check Report — 2026-MM-DD

| Country | URLs ✅ | URLs 🟡 | URLs 🔴 | Status |
|---|---:|---:|---:|---|
| fr | 45 | 2 | 0 | 🟢 HEALTHY |
| it | 35 | 2 | 1 | 🟡 NEEDS UPDATE |
| cz | 27 | 0 | 0 | 🟢 HEALTHY |
| sk | 31 | 1 | 0 | 🟢 HEALTHY |

## Broken URLs (require replacement)
1. https://example-old-portal.gov.it/path (404)
   → Suggested replacement: https://example-new-portal.gov.it/path
   → Confidence: HIGH (same domain root, redirect chain)

2. ...
```

## Implementation pseudocode

```python
# High-level flow
def update_skill(targets, mode):
    if mode == "validate-only":
        report = []
        for country in targets:
            urls = extract_urls(read(f"countries/{country}/playbook.md"))
            results = validate(urls)  # parallel HTTP HEAD/GET
            report.append((country, results))
        write_health_report(report)
        return

    if mode == "refresh-only":
        for country in targets:
            facts = extract_numeric_facts(read(f"countries/{country}/playbook.md"))
            new_facts = research_facts(facts, country)
            diff = build_diff(facts, new_facts)
            if user_confirms(diff):
                apply_changes(country, diff)
        return

    if mode == "update":  # default
        for country in targets:

            # 1. Validate URLs
            url_results = validate_urls(country)

            # 2. Refresh facts
            fact_results = refresh_facts(country)

            # 3. Build combined diff
            diff = build_diff(url_results, fact_results)

            # 4. Confirm if interactive
            if user_confirms(diff):

                # 5. Backup + apply
                backup(country)
                apply_changes(country, diff)

                # 6. Update log
                append_update_log(country, diff)
        write_summary_report()

    if mode == "add":
        country = targets[0]

        # 1. Read scaffold
        scaffold = read(f"countries/{country}/playbook.md")

        # 2. Run full research
        playbook = research_country_full(country)

        # 3. Anti-hallucination check
        validate_anti_hallucination(playbook)

        # 4. Write + preserve scaffold
        backup_scaffold(country)
        write(f"countries/{country}/playbook.md", playbook)
        update_master_matrix(country)
```

## Refresh tiers — cadence-by-country

At 126 countries × 41 sections, refreshing everything quarterly is ~46 hours of research. The tier system splits the work by market activity so high-velocity jurisdictions get attention every 90 days while stable frontier markets ride a 365-day cycle.

**Tier definitions** live in `config/_tiers.json` at the repo root (single source of truth):

| Tier | Cadence | Count | Rationale |
|---|---|---:|---|
| **A** | Quarterly (90 d) | 16 | High-volume foreign-buyer markets with frequent regulatory change. Tax/visa/rental rules shift mid-year; numeric benchmarks move quarterly. |
| **B** | Semi-annual (180 d) | 38 | Stable mid-volume markets. Numbers drift slowly; major reforms hit a 6-month cycle reliably. |
| **C** | Annual (365 d) | 72 | Smaller markets, microstates, frontier jurisdictions. Foundational data is stable; targeted patches happen via regulatory-watch override, not the cadence. |

**Tier membership** (canonical list — see `config/_tiers.json` for machine-readable form):

- **Tier-A** (16): `fr, it, es, de, uk, us, pt, ie, nl, at, gr, tr, ae, au, ch, kz`
- **Tier-B** (38): `be, dk, fi, no, se, is, lu, mt, cy, pl, cz, sk, hu, ro, bg, hr, si, ee, lv, lt, ca, nz, jp, kr, sg, hk, tw, il, mx, br, mu, cv, bs, cn, bb, lk, kh, uz`
- **Tier-C** (72): `ad, al, am, ar, aw, az, ba, bh, bq, bz, cl, co, cr, cw, do, ec, eg, fo, ge, gg, gh, gi, gl, id, im, in, je, jm, jo, ke, kw, lb, li, ma, mc, md, me, mk, mo, mv, my, ng, om, pa, pe, ph, py, qa, rs, rw, sa, sc, sm, sx, th, tn, uy, vn, za, ky, bm, tc, vg, kn, ag, lc, gd, na, bw, vu, tt, pk`

### Tier invocation

```
/property-deep-dive --update --tier=A                     # refresh all Tier-A countries
/property-deep-dive --update --tier=A --refresh-only      # data refresh, no URL check
/property-deep-dive --update --tier=B --validate-only     # URL liveness for Tier-B
/property-deep-dive --update --tier=C --diff              # preview Tier-C planned changes
```

`--tier=<A|B|C>` and `--update=<iso2,...>` are mutually exclusive — use one or the other.

### Auto-promotion via regulatory-watch

When a Tier-1 or Tier-2 entry lands in `shared/regulatory-watch.md` for a Tier-B or Tier-C country, that country is auto-promoted to Tier-A for the NEXT refresh cycle only, then reverts. Tracked via the `regulatory-watch-revisit` workflow.

The mechanism: the `regwatch_promotion` rule in `config/_tiers.json` triggers when an entry's `enacted_date` is within the last 90 days. The next Tier-A cron run picks up the promoted country alongside the canonical 16.

### Manual override

```
/property-deep-dive --update --tier=A --include=<iso2>    # force-include regardless of canonical tier
/property-deep-dive --update --tier=A --exclude=<iso2>    # skip a canonical Tier-A country this cycle
```

Use `--include` when a Tier-C country has a known reform mid-cycle; use `--exclude` when a Tier-A country was hand-verified yesterday and doesn't need re-research.

## Frequency recommendations (legacy — superseded by tiers above)

| Mode | Cadence | Cost (time) |
|---|---|---|
| `--validate-only` (all countries) | **Weekly** | ~5 min via `url-liveness.yml` cron |
| `--health-report` | **Monthly** | ~1 min via `health-report.yml` cron |
| `--update --tier=A` | **Quarterly** | ~8 hr (16 countries × ~30 min) |
| `--update --tier=B` | **Semi-annual** | ~19 hr (38 countries × ~30 min) |
| `--update --tier=C` | **Annual** | ~36 hr (72 countries × ~30 min) |
| `--update --add=<iso2>` | **As needed** | ~30 min/country |

## Trigger events

Run `--update` after any of these news triggers:

- New EU regulation affecting property (e.g., 2024/1028 short-let, EPBD recast)
- National tax reform announcement (often Q4 of preceding year)
- Major data source migration (e.g., government portal redesign)
- User reports broken URL or stale data
- Major real-estate market shift (>15 % YoY change)
- New mandatory diagnostic requirement
- New seismic/flood event prompting hazard map update

## Integration with `/schedule`

For automated maintenance, encourage the user to schedule by tier:

```
/schedule weekly: /property-deep-dive --update --validate-only          # URL liveness, all 126
/schedule monthly: /property-deep-dive --health-report                  # decay matrix
/schedule quarterly: /property-deep-dive --update --tier=A              # 16 high-velocity markets
/schedule semi-annually: /property-deep-dive --update --tier=B          # 38 mid-volume markets
/schedule annually: /property-deep-dive --update --tier=C               # 72 stable/frontier markets
```

The repo-side equivalents are GitHub Actions workflows:
- `url-liveness.yml` — Monday 09:00 UTC weekly
- `health-report.yml` — 1st of month 09:00 UTC monthly
- `tier-a-refresh.yml` — 1st of Jan/Apr/Jul/Oct 09:00 UTC quarterly
- `tier-b-refresh.yml` — 1st of Jan/Jul 09:00 UTC semi-annually
- `tier-c-refresh.yml` — 15 Jan 09:00 UTC annually

These cron jobs do NOT modify playbooks autonomously. They open issues with the list of countries due for refresh; a human (or `/property-deep-dive --update --tier=X`) executes the actual refresh.

Schedule output goes to `_local/reports/property-deep-dive-update-YYYY-MM-DD.md`.

## Quality bar

- The updater **must not introduce hallucinations**. Anti-hallucination guard applies in full.
- The updater **must preserve all manually-curated quirks** (the "Caveats unique to FR" type sections — these are wisdom, not data).
- The updater **must surface conflicts**, not silently pick a winner.
- The updater **must keep update logs** so changes can be audited and reverted.
