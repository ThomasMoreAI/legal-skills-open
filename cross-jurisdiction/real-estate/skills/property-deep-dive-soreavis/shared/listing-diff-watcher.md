# Listing Diff Watcher

Track price drops, status changes, and listing edits on watched property URLs over time. Useful for users who are tracking specific listings before committing.

## Universal contract

For a watched listing URL, return:
1. **Initial snapshot** at watch time (price, status, photos, description hash)
2. **Periodic re-fetch** (default daily) and diff against snapshot
3. **Notification triggers** on price drop / status change / removed listing
4. **Audit trail** stored in `_local/watchlist/<commune>-<id>.json`

## Trigger conditions

| Event | Trigger | Verdict |
|---|---|---|
| Price reduced ≥3% | YES | 🟡 watch — soft signal |
| Price reduced ≥7% | YES | 🟠 active — seller likely motivated |
| Price reduced ≥15% | YES | 🔴 anomaly — investigate (defect? motivated seller? listing error?) |
| Status changed: active → "sale agreed" | YES | 🟢 you may have lost it |
| Status changed: removed | YES | 🟡 may have sold OR pulled by seller |
| New photos added | YES | 🟡 may indicate condition update |
| Description edit (semantic) | YES | 🟡 worth re-reading |
| Days-on-market crossing thresholds (30/60/90/180) | YES | 🟡 - 🟠 (longer = stronger signal) |

## Storage schema

```json
{
  "watch_id": "fr-adriers-86430-saffti-12345",
  "url": "https://www.safti.fr/...",
  "country": "fr",
  "commune": "adriers",
  "initial_snapshot": {
    "fetched_at": "2026-04-26T14:00:00Z",
    "price": 145000,
    "currency": "EUR",
    "status": "active",
    "days_on_market": 45,
    "description_hash": "abc123...",
    "photos_count": 12
  },
  "history": [
    {
      "fetched_at": "2026-04-27T14:00:00Z",
      "price": 145000,
      "status": "active",
      "days_on_market": 46,
      "delta": "no_change"
    },
    {
      "fetched_at": "2026-05-15T14:00:00Z",
      "price": 138000,
      "status": "active",
      "days_on_market": 64,
      "delta": "price_drop_4.83pct"
    }
  ]
}
```

## CLI invocation

```bash
# add a listing to the watchlist
/property-deep-dive --watch <listing-url> [--id=<custom-id>]

# list all watched listings
/property-deep-dive --watchlist

# fetch latest and diff
/property-deep-dive --watchlist-update [--id=<custom-id>]

# remove from watchlist
/property-deep-dive --unwatch <id>
```

## Schedule integration

Pair with `/schedule` for automation:

```bash
# Run the watchlist every morning
/schedule daily 09:00: /property-deep-dive --watchlist-update
/schedule weekly Mon 09:00: /property-deep-dive --watchlist-update --notify-priority=orange
```

## Per-portal extraction patterns

Reuse `shared/listing-aggregators.md` for portal-specific scrape rules:
- **Cloudflare-fronted** (Sreality, Bazaraki, etc.): use Playwright stealth headed mode
- **Partner-API** (Idealista, Funda, Rightmove): use authenticated API where available
- **Open** (athome.lu, ss.lv, etc.): direct curl/fetch
- **Restricted** (most CDN-protected): rate-limit to 1 req / 3-5s

## Anti-hallucination + ethics

- **Respect robots.txt** and platform ToS
- **Rate-limit aggressively** — daily fetch is plenty
- **Don't republish** photos / descriptions — only diff metadata
- **Cache by listing URL hash** to avoid re-fetching same URL twice in a window
- **Detect listing-platform changes** (DOM restructuring) and degrade gracefully — surface "extraction failed, retry manually" rather than fabricate

## Implementation skeleton (bash)

```bash
#!/usr/bin/env bash
# listing-watch.sh
# Usage: ./listing-watch.sh <command> [args]
WATCH_DIR="${HOME}/_local/property-watchlist"
mkdir -p "$WATCH_DIR"

case "$1" in
    add)
        url="$2"
        id=$(echo -n "$url" | sha256sum | head -c 12)

        # fetch initial snapshot via Playwright wrapper or curl
        snapshot=$(./fetch-listing.sh "$url")
        echo "$snapshot" > "$WATCH_DIR/$id.json"
        echo "Watching: $id ($url)"
        ;;
    list)
        ls -1 "$WATCH_DIR/" | sed 's/.json//'
        ;;
    update)
        for f in "$WATCH_DIR"/*.json; do
            id=$(basename "$f" .json)
            url=$(jq -r .url "$f")
            new_snap=$(./fetch-listing.sh "$url")
            ./compute-diff.sh "$f" "$new_snap" >> "${f%.json}.history.jsonl"
        done
        ;;
    diff)
        id="$2"
        cat "$WATCH_DIR/${id}.history.jsonl" | jq .
        ;;
esac
```

A full Python implementation belongs in a separate tooling repo; this MD documents the contract.

## Trigger types in detail

### Price drop
- **3-7% drop**: typical seasonal adjustment, especially after 30-60 days on market
- **7-15% drop**: motivated seller, often after a failed sale or financial pressure
- **15-25% drop**: investigate (defect found in inspection? listing error? distressed sale?)
- **>25% drop**: anomaly — likely listing error or defective property

### Status changes
- **active → sale agreed / sous compromis / under offer**: deal at offer, may fall through
- **active → withdrawn**: seller pulled — may relist later, may have sold privately
- **active → sold**: deal completed (often delayed update)
- **active → reserved**: similar to under offer

### Description edits
- **Cosmetic** (typos, formatting): low signal
- **Substantive** (price reason, defect disclosure, condition update): high signal — surface to user

## Privacy

The watchlist is **local-only** (`_local/watchlist/`). No data sent to a remote service. User can `git ignore` the directory or even encrypt it.

## Status

Last refreshed: 2026-04-26.
