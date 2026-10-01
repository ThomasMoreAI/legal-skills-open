#!/usr/bin/env python3
"""cc — colombia-conflict knowledge engine.

A kg / LLM-wiki retrieval CLI over the Colombian Truth Commission (CEV) final
report 'Hay Futuro Si Hay Verdad' (2022). Substrate-canonical knowledge pages
live in references/ (12 per-volume digests + master synthesis); a dense catalog
projection (references/knowledge-index.md) routes tier-1; body-grep is the
tier-2 fallback; the agent is the query engine.

Subcommands
  load <topic>      two-tier retrieval over the knowledge pages -> ranked sections
  rec               query the 67 recommendations (--theme/--block/--search)
  stat [key|--all]  query the conflict statistical universe
  actor [key|--all] query armed actors + collective-responsibility shares
  concept [--search] query the coined-concepts lexicon
  align "<text>"    score a proposed policy/action against the recommendations
                    -> "does this advance no repetición?" alignment report
  index             (re)generate references/knowledge-index.md from data + digests

Pure-stdlib, zero network, deterministic.
"""
from __future__ import annotations

import argparse
import gzip
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
REFS = ROOT / "references"
FULLTEXT = REFS / "fulltext"

_STOP = {
    "the", "a", "an", "of", "to", "and", "or", "in", "on", "for", "with", "is",
    "are", "be", "by", "as", "at", "this", "that", "it", "its", "from", "de",
    "la", "el", "los", "las", "y", "en", "que", "un", "una", "del", "se", "no",
    "se", "su", "al", "lo", "con", "por", "para", "una", "como",
}


# --- pure helpers (unit-tested) ---------------------------------------------

def _fold(text: str) -> str:
    """Lowercase + ASCII-fold Spanish accents (1:1, length-preserving)."""
    text = (text or "").lower()
    for a, b in (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"),
                 ("ñ", "n"), ("ü", "u")):
        text = text.replace(a, b)
    return text


def tokenize(text: str) -> set[str]:
    """Lowercase word-tokens, ASCII-folded, stopwords + <3-char tokens dropped."""
    toks = re.findall(r"[a-z0-9]+", _fold(text))
    return {t for t in toks if len(t) >= 3 and t not in _STOP}


def score_overlap(query: set[str], doc: set[str]) -> float:
    """Overlap score: |q ∩ d| normalized by query size (recall-leaning)."""
    if not query:
        return 0.0
    return len(query & doc) / len(query)


def search_recommendations(blocks: list[dict], *, theme: str | None = None,
                           block: int | None = None, query: str | None = None) -> list[dict]:
    """Filter recommendation blocks by theme / block number / free-text query."""
    out = []
    qtok = tokenize(query) if query else set()
    for b in blocks:
        if theme and theme.lower() not in b.get("theme", "").lower():
            continue
        if block is not None and b.get("block") != block:
            continue
        if qtok:
            hay = tokenize(" ".join([b.get("title", ""), b.get("theme", ""),
                                     " ".join(b.get("keywords", [])),
                                     " ".join(b.get("recommendations", []))]))
            if not (qtok & hay):
                continue
        out.append(b)
    return out


def lookup(records: list[dict], key: str | None, *, fields: tuple[str, ...]) -> list[dict]:
    """Substring match on `key` across `fields` (case-insensitive); all if None."""
    if not key:
        return list(records)
    k = key.lower()
    return [r for r in records
            if any(k in str(r.get(f, "")).lower() for f in fields)]


# Anti-pattern tokens: things the report recommends ENDING. A proposal carrying
# these is CONTRARY to the named block, even if it lexically overlaps it. Tokens
# are accent-folded to match tokenize() output (e.g. "fumigación" -> "fumigacion").
_CONTRARY = {
    4: {"glifosato", "glyphosate", "fumigacion", "fumigation", "aspersion",
        "prohibicionismo", "prohibition", "prohibitionism"},  # drug-war tools the report wants ended
    6: {"militarizacion", "militarization"},                  # security: human-security, not militarization
    3: {"estigmatizacion", "estigmatizar", "criminalizar", "criminalize",
        "criminalization"},                                   # democracy: don't criminalize protest/leaders
}


def contrary_flags(text: str) -> list[dict]:
    """Blocks the proposal appears to CONTRADICT (carries an anti-pattern token).

    This gives `align` stance/polarity awareness: lexical overlap alone cannot
    tell 'end fumigation' from 'increase fumigation' — both share the token
    'fumigation'. The anti-pattern set flags the contrary direction explicitly.
    """
    qtok = tokenize(text)
    out = []
    for block, anti in _CONTRARY.items():
        hit = sorted(qtok & anti)
        if hit:
            out.append({"block": block, "contrary_tokens": hit})
    return out


def align_text(text: str, blocks: list[dict]) -> list[dict]:
    """Score a proposed policy/action against each recommendation block.

    Returns blocks ranked by token overlap with their keywords+title+recs,
    each with a 0..1 `score` and the matched tokens. This is LEXICAL overlap
    only — it is stance-blind; pair it with contrary_flags() and agent reasoning
    about polarity. The deterministic half of the 'does this advance no
    repetición?' check.
    """
    qtok = tokenize(text)
    ranked = []
    for b in blocks:
        btok = tokenize(" ".join([b.get("title", ""), b.get("theme", ""),
                                  " ".join(b.get("keywords", [])),
                                  " ".join(b.get("recommendations", []))]))
        matched = sorted(qtok & btok)
        if matched:
            ranked.append({"block": b.get("block"), "theme": b.get("theme"),
                           "title": b.get("title"), "rec_range": b.get("rec_range"),
                           "score": round(score_overlap(qtok, btok), 3),
                           "matched": matched})
    ranked.sort(key=lambda r: (-r["score"], r["block"]))
    return ranked


def build_catalog(stats: list[dict], actors: list[dict], blocks: list[dict],
                  concepts: list[dict], digest_headers: list[tuple[str, str]]) -> str:
    """Render the dense tier-1 catalog (one routable line per knowledge item)."""
    lines = ["# colombia-conflict — knowledge index (catalog projection)",
             "",
             "> Tier-1 routing catalog for `cc.py load`. Substrate is `references/`+`data/`.",
             "> Auto-generated by `cc.py index` — do not hand-edit.", ""]
    lines.append("## Statistics")
    for s in stats:
        lines.append(f"- stat:`{s['key']}` — {s['label']} · {s.get('documented')} "
                     f"({s.get('period','')}) [data/statistics.json]")
    lines.append("\n## Armed actors & responsibility")
    for a in actors:
        lines.append(f"- actor:`{a['key']}` — {a['name']} [data/actors.json]")
    lines.append("\n## Recommendation blocks (67 recs / 8 blocks)")
    for b in blocks:
        lines.append(f"- rec-block:{b['block']} `{b['theme']}` — {b['title']} "
                     f"(recs {b['rec_range']}) [data/recommendations.json]")
    lines.append("\n## Concepts (lexicon)")
    for c in concepts:
        lines.append(f"- concept:`{c['term']}` — {c['gloss'][:80]}… [data/concepts.json]")
    lines.append("\n## Knowledge pages (per-volume digests + synthesis)")
    for relpath, header in digest_headers:
        lines.append(f"- page:{relpath} — {header} [references/]")
    return "\n".join(lines) + "\n"


# --- io ----------------------------------------------------------------------

def _load_json(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def _digest_headers() -> list[tuple[str, str]]:
    out = []
    for p in sorted(REFS.rglob("*.md")):
        if p.name == "knowledge-index.md":
            continue
        header = ""
        for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.startswith("# "):
                header = line[2:].strip()
                break
        out.append((str(p.relative_to(REFS)), header or p.stem))
    return out


def _grep_sections(topic: str, limit: int) -> list[dict]:
    """Tier-2: body-grep over knowledge pages; return matching heading-sections."""
    qtok = tokenize(topic)
    hits = []
    for p in sorted(REFS.rglob("*.md")):
        if p.name == "knowledge-index.md":
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        cur_head, buf = p.stem, []
        sections = []
        for line in text.splitlines():
            if re.match(r"^#{1,4}\s", line):
                if buf:
                    sections.append((cur_head, "\n".join(buf)))
                cur_head, buf = line.lstrip("# ").strip(), []
            else:
                buf.append(line)
        if buf:
            sections.append((cur_head, "\n".join(buf)))
        for head, body in sections:
            sc = score_overlap(qtok, tokenize(head + " " + body))
            if sc > 0:
                hits.append({"page": str(p.relative_to(REFS)), "section": head,
                             "score": round(sc, 3),
                             "snippet": re.sub(r"\s+", " ", body).strip()[:240]})
    hits.sort(key=lambda h: -h["score"])
    return hits[:limit]


def search_fulltext(topic: str, limit: int = 5) -> list[dict]:
    """Verbatim grounding: grep the gzipped full text (references/fulltext/*.txt.gz)
    for paragraphs matching the topic, ranked by token overlap.

    The digests are summaries; this searches the *actual source prose* so the
    agent can quote the report verbatim. Returns up to `limit` passages, each
    {page, score, snippet}. Empty if the full-text substrate isn't present
    (e.g. a slim install) — callers fall back to `load`/digests.
    """
    limit = max(1, limit)
    qtok = tokenize(topic)
    if not qtok or not FULLTEXT.is_dir():
        return []
    hits: list[dict] = []
    for p in sorted(FULLTEXT.glob("*.txt.gz")):
        try:
            with gzip.open(p, "rt", encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except OSError:
            continue
        page = p.name[:-7] if p.name.endswith(".txt.gz") else p.stem
        for para in re.split(r"\n\s*\n", text):
            para = para.strip()
            if len(para) < 40:
                continue
            sc = score_overlap(qtok, tokenize(para))
            if sc > 0:
                hits.append({"page": page, "score": round(sc, 3),
                             "snippet": _snippet(para, qtok)})
    hits.sort(key=lambda h: -h["score"])
    return hits[:limit]


def _snippet(para: str, qtok: set[str], width: int = 300) -> str:
    """A ~width-char window centered on the first query-token match (so the hit
    is visible, not cut off by a prefix), whitespace-collapsed."""
    folded = _fold(para)  # length-preserving fold -> indices map to `para`
    positions = [i for i in (folded.find(t) for t in qtok) if i >= 0]
    if positions:
        pos = min(positions)
        start = max(0, pos - 80)
        window = para[start:pos + (width - 80)]
        out = re.sub(r"\s+", " ", window).strip()
        return ("…" + out) if start > 0 else out
    return re.sub(r"\s+", " ", para).strip()[:width]


def two_tier_load(topic: str, limit: int = 6) -> dict:
    """Tier-1 catalog routing; tier-2 body-grep fallback when tier-1 is thin.

    `limit` is a TOTAL result budget across both tiers: tier-1 takes up to
    `limit` catalog hits, then tier-2 fills only the remaining slots — so
    len(tier1) + len(tier2) <= limit. `limit` is clamped to >= 1.
    """
    limit = max(1, limit)
    qtok = tokenize(topic)
    catalog = (REFS / "knowledge-index.md")
    tier1 = []
    if catalog.is_file():
        for line in catalog.read_text(encoding="utf-8").splitlines():
            if not line.startswith("- "):
                continue
            sc = score_overlap(qtok, tokenize(line))
            if sc > 0:
                tier1.append({"line": line[2:].strip(), "score": round(sc, 3)})
        tier1.sort(key=lambda h: -h["score"])
        tier1 = tier1[:limit]
    remaining = limit - len(tier1)
    tier2 = _grep_sections(topic, remaining) if remaining > 0 else []
    return {"topic": topic, "tier1": tier1, "tier2": tier2}


# --- cli ---------------------------------------------------------------------

def _print(obj):
    print(json.dumps(obj, ensure_ascii=False, indent=2))


def cmd_load(a):
    _print(two_tier_load(a.topic, a.n))


def cmd_rec(a):
    blocks = _load_json("recommendations.json")["blocks"]
    _print(search_recommendations(blocks, theme=a.theme, block=a.block, query=a.search))


def cmd_stat(a):
    stats = _load_json("statistics.json")["statistics"]
    _print(lookup(stats, None if a.all else a.key, fields=("key", "label")))


def cmd_actor(a):
    actors = _load_json("actors.json")["actors"]
    _print(lookup(actors, None if a.all else a.key, fields=("key", "name", "type")))


def cmd_concept(a):
    concepts = _load_json("concepts.json")["concepts"]
    _print(lookup(concepts, a.search, fields=("term", "gloss", "volume")))


def cmd_align(a):
    blocks = _load_json("recommendations.json")["blocks"]
    ranked = align_text(a.text, blocks)
    contrary = contrary_flags(a.text)
    by_theme = {b["block"]: b.get("theme") for b in blocks}
    parts = []
    if contrary:
        parts.append("⚠ appears CONTRARY to the roadmap on: " + ", ".join(
            f"block {c['block']} ({by_theme.get(c['block'])}, via {'/'.join(c['contrary_tokens'])})"
            for c in contrary) + " — the report recommends the OPPOSITE")
    if ranked:
        parts.append("lexically aligns with: " + ", ".join(
            f"block {r['block']} ({r['theme']})" for r in ranked[:3]))
    if not parts:
        parts.append("no clear lexical alignment with the CEV roadmap — refine the proposal")
    _print({
        "input": a.text,
        "verdict": " | ".join(parts),
        "note": "align is LEXICAL + a curated anti-pattern check — it is not a full stance model; reason about polarity and the gaps the report would flag (impunity, structural causes, differential harms, terceros civiles).",
        "contrary": contrary,
        "matches": ranked,
    })


def cmd_source(a):
    _print({"topic": a.topic, "passages": search_fulltext(a.topic, a.n)})


def cmd_index(a):
    stats = _load_json("statistics.json")["statistics"]
    actors = _load_json("actors.json")["actors"]
    blocks = _load_json("recommendations.json")["blocks"]
    concepts = _load_json("concepts.json")["concepts"]
    cat = build_catalog(stats, actors, blocks, concepts, _digest_headers())
    out = REFS / "knowledge-index.md"
    if a.check:
        cur = out.read_text(encoding="utf-8") if out.is_file() else ""
        if cur != cat:
            print("knowledge-index.md is STALE — run `cc.py index`", file=sys.stderr)
            return 1
        print("knowledge-index.md up to date")
        return 0
    out.write_text(cat, encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)} ({cat.count(chr(10))} lines)")
    return 0


def _positive_int(s: str) -> int:
    """argparse type: a >= 1 integer (rejects 0 / negatives that would slice oddly)."""
    v = int(s)
    if v < 1:
        raise argparse.ArgumentTypeError("must be a positive integer (>= 1)")
    return v


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="cc", description="colombia-conflict knowledge engine")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("load", help="two-tier kg retrieval over knowledge pages")
    p.add_argument("topic")
    p.add_argument("-n", type=_positive_int, default=6)
    p.set_defaults(func=cmd_load)

    p = sub.add_parser("rec", help="query the 67 recommendations")
    p.add_argument("--theme")
    p.add_argument("--block", type=int)
    p.add_argument("--search")
    p.set_defaults(func=cmd_rec)

    p = sub.add_parser("stat", help="query conflict statistics")
    p.add_argument("key", nargs="?")
    p.add_argument("--all", action="store_true")
    p.set_defaults(func=cmd_stat)

    p = sub.add_parser("actor", help="query armed actors & responsibility")
    p.add_argument("key", nargs="?")
    p.add_argument("--all", action="store_true")
    p.set_defaults(func=cmd_actor)

    p = sub.add_parser("concept", help="query the lexicon")
    p.add_argument("--search")
    p.set_defaults(func=cmd_concept)

    p = sub.add_parser("source", help="verbatim full-text search over references/fulltext/*.txt.gz")
    p.add_argument("topic")
    p.add_argument("-n", type=_positive_int, default=5)
    p.set_defaults(func=cmd_source)

    p = sub.add_parser("align", help="score a proposal vs the recommendation roadmap")
    p.add_argument("text")
    p.set_defaults(func=cmd_align)

    p = sub.add_parser("index", help="(re)generate references/knowledge-index.md")
    p.add_argument("--check", action="store_true", help="exit 1 if stale (CI)")
    p.set_defaults(func=cmd_index)
    return ap


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    rc = args.func(args)
    return rc if isinstance(rc, int) else 0


if __name__ == "__main__":
    sys.exit(main())
