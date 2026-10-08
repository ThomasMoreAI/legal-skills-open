# Auto-Validate Cron Tracking

Extends `--update --validate-only` with per-country pass/fail tracking, scheduled cadence, and trend monitoring.

## Universal contract

For each country playbook, on each validation run, return:
1. **URL liveness** (200 / 3xx / 4xx / 5xx / timeout / bot-blocked)
2. **Per-country health score** (0-100 = % of URLs returning 2xx or browser-OK)
3. **Per-section health** (price / tax / risks / mains / etc.)
4. **Trend** (improving / stable / degrading vs prior runs)
5. **Critical-source freshness** (price-index, tax-rate, regulatory URLs)
6. **Generated maintenance report** at `_local/reports/property-deep-dive-validate-<date>.md`

## Scheduled cadence

```bash
# weekly URL liveness only (~5 min)
/schedule weekly Mon 09:00: /property-deep-dive --update --validate-only

# monthly per-country pass/fail tracking
/schedule monthly 1st 09:00: /property-deep-dive --update --validate-only --track

# quarterly full data refresh per country
/schedule quarterly 1st 09:00: /property-deep-dive --update --refresh-only

# annual full re-validation + research
/schedule yearly Jan 15 09:00: /property-deep-dive --update
```

## Per-country tracking schema

`_local/validate-history/<iso2>.jsonl`:

```jsonl
{"date": "2026-04-26", "urls_total": 42, "urls_200": 39, "urls_403_bot": 2, "urls_404": 1, "urls_timeout": 0, "score": 92, "critical_failures": ["amccrs-pmb.ro"]}
{"date": "2026-05-26", "urls_total": 42, "urls_200": 40, "urls_403_bot": 2, "urls_404": 0, "urls_timeout": 0, "score": 95, "critical_failures": []}
{"date": "2026-06-26", "urls_total": 42, "urls_200": 38, "urls_403_bot": 2, "urls_404": 2, "urls_timeout": 0, "score": 90, "critical_failures": ["bnr.ro/financial-stability"]}
```

## Per-country pass/fail thresholds

| Score | Verdict |
|---|---|
| 95-100% | 🟢 Healthy |
| 85-94% | 🟡 Acceptable — monitor |
| 70-84% | 🟠 Degraded — schedule review |
| <70% | 🔴 Failing — immediate human review |

## URL classification

| Status | Class |
|---|---|
| 200 | LIVE |
| 301 / 302 (resolves to 2xx) | LIVE (redirect) |
| 403 (Cloudflare/DataDome bot challenge) | LIVE (bot-blocked, browser-OK) |
| 401 / 403 (auth required) | RESTRICTED (login needed) |
| 404 | DEAD |
| 410 | DEAD (gone) |
| 5xx persistent | INTERMITTENT |
| timeout / DNS fail | DEAD or HOST-DOWN |

## Critical-source list

For each country, mark these URLs as **critical** (failure triggers immediate human review):

| Source | Why critical |
|---|---|
| Cadastre / land registry | foundational for `--mains` |
| Statistics office HPI | foundational for `--price` |
| Central bank | foundational for `--macro` + `--finance` |
| Tax authority (national) | foundational for `--tax` |
| Notary chamber | foundational for `--notary` |
| Flood / seismic risk authority | foundational for `--risks` |
| EPC / energy register | foundational for `--esg` |

If 2+ critical sources fail simultaneously for one country, escalate to immediate human review.

## Maintenance report format

```markdown
# Property-Deep-Dive Validate Report — 2026-04-26

## Summary

- 109 countries validated
- 41 healthy 🟢
- 2 acceptable 🟡 (LV, AL)
- 1 degraded 🟠 (RO — INSSE intermittent 503)
- 0 failing 🔴

## Per-country detail

### 🇫🇷 FR — score 100% 🟢
- 38 URLs · 38× 200 · 0× 4xx · 0× timeout
- All critical sources live

### 🇷🇴 RO — score 78% 🟠
- 42 URLs · 33× 200 · 4× 403-bot · 3× 503 · 2× 404
- **Critical failures**: insse.ro (503 intermittent — last 7 days), afm.ro (503 intermittent)
- **Action**: monitor 7 more days; if persists, contact sources or find replacement
- **Replaced 2 dead URLs** since last run: anaf.ro/path-x → anaf.ro/path-x-new

### 🇱🇻 LV — score 88% 🟡
- 35 URLs · 31× 200 · 4× 403-bot
- All critical sources live (403-bot are listings portals)

### 🇦🇱 AL — score 88% 🟡
- 28 URLs · 25× 200 · 1× 403 · 1× 404 · 1× timeout
- iKadaster Beta: timeout (still in development per gov)

## Trend

Scores compared to last 4 weeks:

| Country | 4 wks ago | 3 wks | 2 wks | last wk | Today | Trend |
|---|---|---|---|---|---|---|
| FR | 100 | 100 | 100 | 100 | 100 | → |
| DE | 95 | 95 | 92 | 95 | 100 | ↑ |
| RO | 90 | 88 | 82 | 80 | 78 | ↓ |

## Action items

1. RO degradation — monitor for 7 days; if persists, schedule research agent for source replacement
2. AL iKadaster timeout — known issue (gov dev); recheck monthly
3. UK SDLT URL changes — verify all SDLT-mentioning playbooks (UK, NI) reflect 1 Apr 2025 reverted thresholds
```

## Auto-replacement workflow

When a URL fails 4 consecutive runs:

1. **Search for replacement** via web search on the cited document title or source authority
2. **Verify replacement URL** returns 2xx
3. **Update country playbook** with the new URL
4. **Log replacement** in playbook update history
5. **Notify user** via maintenance report

## Gating rules

- **Auto-replace only structurally-stable replacements** (same authority, same data type)
- **Never auto-add a new claim** — only swap dead-URL→live-URL for same fact
- **Human-review required for**:
  - Tax-rate changes
  - Regulatory cutoff dates
  - Schema-of-data changes (e.g., HPI methodology change)
  - Currency / peg / regulatory-regime changes

## Cron scheduling pattern

```bash
# /schedule integration
/schedule weekly Mon 09:00: /property-deep-dive --update --validate-only

# pings every URL, classifies status, computes per-country score
# logs to _local/validate-history/<iso2>.jsonl
# generates _local/reports/property-deep-dive-validate-<date>.md
/schedule monthly 1st 09:00: /property-deep-dive --update --validate-only --notify-changes

# same but emits notification on score-degradation events
/schedule quarterly 1st 09:00: /property-deep-dive --update --refresh-only --diff

# pulls fresh data from price-index-feeds.md sources
# preserves URLs unless dead
/schedule yearly Jan 15: /property-deep-dive --update --interactive

# annual deep refresh; human-in-the-loop confirmation
```

## Anti-hallucination

- **403 bot-block ≠ dead** — many CDN-protected portals respond 403 to curl HEAD but render in browser
- **Verify with multiple methods** before flagging dead: HEAD, GET, GET with browser UA, Playwright headed
- **Don't auto-replace tax-related URLs** — these need human review on each refresh
- **Mark replacements in update history** so the user can audit auto-changes
- **Trend matters more than single-day** — a one-off 503 doesn't mean dead

## Privacy

All tracking is local (`_local/validate-history/`). No remote service. User can encrypt or git-ignore.

## Status

Last refreshed: 2026-04-26.
