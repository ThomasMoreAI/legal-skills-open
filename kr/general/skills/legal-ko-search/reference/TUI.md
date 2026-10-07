# TUI Context Integration

## Context JSON

The TUI writes to `~/.cache/legal-ko/context.json` on every navigation event.
Read with `legal-ko-cli context --json`.

```json
{
  "view": "detail",
  "timestamp": "2026-04-03T12:00:00Z",
  "selected_law": {
    "id": "kr/주택임대차보호법/법률",
    "title": "주택임대차보호법",
    "category": "법률",
    "departments": ["법무부"]
  },
  "filters": {
    "search_query": "임대차",
    "category": null,
    "department": null,
    "bookmarks_only": false,
    "total_laws": 6200,
    "filtered_count": 15
  },
  "detail": {
    "law_id": "kr/주택임대차보호법/법률",
    "law_title": "주택임대차보호법",
    "current_article": { "index": 2, "label": "제3조 (대항력 등)" },
    "total_articles": 18,
    "scroll_position": 45,
    "total_lines": 320
  }
}
```

| Field | Present When | Description |
|-------|-------------|-------------|
| `view` | Always | `"loading"`, `"list"`, or `"detail"` |
| `selected_law` | List/detail | Law highlighted/open |
| `filters` | List/detail | Active search, category, department |
| `detail` | Detail only | Scroll position, current article |

## Using Context

- **Detail view** → skip to `show`/`articles` for `detail.law_id`
- **Search query** → use `filters.search_query` as starting point
- **Current article** → quote `detail.current_article.label` directly

## Navigate Command

`legal-ko-cli navigate "<id>" --article "제N조"` — works from any view.
Article matching uses prefix: `"제3조"` matches `"제3조 (대항력 등)"`.

## Debugging

```bash
tail -f ~/Library/Caches/legal-ko/legal-ko.log
```

Key log messages: `take_command`, `Received external command`, `handle_navigate start`, `select_law_by_id`.

| Symptom | Fix |
|---------|-----|
| TUI doesn't react | Law ID not in filtered list — clear filters |
| Article not found | Check exact labels via `articles --json` |
| Command file lingers | TUI not running — start it first |
