"""
CourtListener API client.

Wraps Free Law Project's CourtListener REST API v4 to find appellate cases
that cite a given statute. Used by Specter (the OpenClaw agent) to enrich
statute briefs with real precedent.

Hard rules (mirrored in SKILL.md):
- This module ONLY retrieves what CourtListener returns. No paraphrasing
  of opinion content. The agent surfaces case_name, court, date, URL, and
  snippet — that's it. The user clicks through for the full opinion.
- Never fabricates a case, citation, court, or date. If the API returns
  nothing, the function returns an empty list and the caller reports that
  honestly.

Required env:
    COURTLISTENER_API_KEY  — free token from
        https://www.courtlistener.com/help/api/rest/#authentication

Free tier: 5,000 queries/hour.
"""
from __future__ import annotations

import os
from typing import Any, Optional

import httpx

API_BASE = "https://www.courtlistener.com/api/rest/v4"
DEFAULT_TIMEOUT = 30.0
USER_AGENT = "Specter/0.1 (hackathon)"


# ---------- helpers ----------

def _api_key() -> str:
    key = os.environ.get("COURTLISTENER_API_KEY")
    if not key:
        raise RuntimeError(
            "COURTLISTENER_API_KEY not set. Get a free token at "
            "https://www.courtlistener.com/help/api/rest/#authentication "
            "and add it to ~/Specter/.env."
        )
    return key


def _headers() -> dict[str, str]:
    return {
        "Authorization": f"Token {_api_key()}",
        "User-Agent": USER_AGENT,
    }


def _client(timeout: float = DEFAULT_TIMEOUT) -> httpx.Client:
    return httpx.Client(
        base_url=API_BASE,
        headers=_headers(),
        timeout=timeout,
        follow_redirects=True,
    )


def _absolute_url(rel_or_abs: str | None) -> str:
    if not rel_or_abs:
        return ""
    if rel_or_abs.startswith("http://") or rel_or_abs.startswith("https://"):
        return rel_or_abs
    if rel_or_abs.startswith("/"):
        return f"https://www.courtlistener.com{rel_or_abs}"
    return rel_or_abs


# ---------- public API ----------

def healthz() -> dict[str, Any]:
    """
    Liveness check. Hits /search/?q=test&type=o just to confirm the API
    is reachable and the token is valid. Returns {'ok': True, ...} on success
    or {'ok': False, 'reason': ...} on any failure.
    """
    try:
        with _client(timeout=10) as c:
            r = c.get("/search/", params={"q": "test", "type": "o"})
        return {"ok": r.status_code == 200, "status": r.status_code}
    except httpx.HTTPError as e:
        return {"ok": False, "reason": f"{type(e).__name__}: {e}"}
    except RuntimeError as e:  # missing key
        return {"ok": False, "reason": str(e)}


def search_for_statute(
    citation: str,
    *,
    jurisdiction: Optional[str] = None,
    k: int = 5,
    timeout: float = DEFAULT_TIMEOUT,
) -> tuple[list[dict[str, Any]], int]:
    """
    Single API call that returns both the top-k cases AND the total count.
    Use this instead of cases_for_statute()+total_for_statute() to halve
    rate-limit pressure.

    Returns: (results_list, total_count). On any error: ([], 0).
    """
    if not citation or not citation.strip():
        return [], 0
    query = f'"{citation.strip()}"'
    params: dict[str, Any] = {
        "q": query,
        "type": "o",
        "order_by": "score desc",
    }
    try:
        with _client(timeout=timeout) as c:
            r = c.get("/search/", params=params)
    except httpx.HTTPError:
        return [], 0
    if r.status_code != 200:
        return [], 0
    try:
        data = r.json()
    except ValueError:
        return [], 0
    total = int(data.get("count") or 0)
    results = data.get("results") or []
    out: list[dict[str, Any]] = []
    for hit in results[:k]:
        out.append({
            "case_name":   hit.get("caseName") or hit.get("case_name") or "",
            "court":       hit.get("court") or "",
            "date_filed":  (hit.get("dateFiled") or hit.get("date_filed") or "")[:10],
            "url":         _absolute_url(hit.get("absolute_url")),
            "snippet":     hit.get("snippet") or "",
            "citation_id": hit.get("id") or hit.get("cluster_id"),
        })
    return out, total


def cases_for_statute(
    citation: str,
    *,
    jurisdiction: Optional[str] = None,
    k: int = 5,
    timeout: float = DEFAULT_TIMEOUT,
) -> list[dict[str, Any]]:
    """
    Find appellate cases that cite the given statute.

    citation:
        Statute citation as the user / Harvester gives it
        (e.g. 'Cal. Veh. Code § 23152(a)'). Quoted in the API call so we
        match the literal string in the opinion text.

    jurisdiction:
        Optional 2-letter state code ('CA', 'TX'). Currently used only as
        a hint to the score query, not a hard filter — CourtListener's court
        filter would require mapping our 2-letter codes to their court IDs,
        which is more work than this MVP needs. Cross-jurisdiction analogues
        are often useful, so soft filtering is fine for now.

    k:
        Top-k results to return.

    Returns:
        list of dicts shaped:
            {
              "case_name":   str,
              "court":       str,
              "date_filed":  "YYYY-MM-DD" (str),
              "url":         "https://www.courtlistener.com/opinion/.../" (str),
              "snippet":     str,           # CourtListener-provided context
              "citation_id": int | None,    # opinion id for follow-up queries
            }

    On any error: returns an empty list. The caller decides how to phrase
    the miss. We never raise — we never fabricate either.
    """
    """
    Convenience wrapper around search_for_statute() that returns just the
    cases list. Prefer search_for_statute() if you also want the total.
    """
    cases, _ = search_for_statute(
        citation, jurisdiction=jurisdiction, k=k, timeout=timeout,
    )
    return cases


def total_for_statute(citation: str, *, timeout: float = DEFAULT_TIMEOUT) -> int:
    """
    How many opinions cite this statute (count only, no result list).
    Useful for the brief: 'I have N cases interpreting this section.'
    """
    if not citation or not citation.strip():
        return 0
    try:
        with _client(timeout=timeout) as c:
            r = c.get("/search/", params={"q": f'"{citation.strip()}"', "type": "o"})
    except httpx.HTTPError:
        return 0
    if r.status_code != 200:
        return 0
    try:
        return int(r.json().get("count") or 0)
    except (ValueError, TypeError):
        return 0


# ---------- terminal renderer ----------

def render_text(citation: str, cases: list[dict[str, Any]], *, total: Optional[int] = None) -> str:
    """Plain-text formatter for WhatsApp / pretty.py."""
    if not cases:
        return f"No cases found citing {citation} in CourtListener."
    lines: list[str] = []
    lines.append(f"Cases interpreting {citation}:\n")
    for i, c in enumerate(cases, 1):
        court_short = (c["court"] or "").replace("Court of Appeals", "Ct. App.").replace("Supreme Court", "Sup. Ct.")
        year = (c["date_filed"] or "")[:4]
        head = f"  {i}. {c['case_name']}"
        meta = f"     {court_short[:55]}, {year}" if year else f"     {court_short[:55]}"
        lines.append(head)
        lines.append(meta)
        if c["url"]:
            lines.append(f"     {c['url']}")
        if c["snippet"]:
            # Clean up CourtListener's <mark> tags in snippets
            import re as _re
            snip = _re.sub(r"</?[a-z]+>", "", c["snippet"]).strip()
            if len(snip) > 220:
                snip = snip[:217] + "…"
            lines.append(f"     ↳ {snip}")
        lines.append("")
    if total is not None and total > len(cases):
        lines.append(f"({total} total — top {len(cases)} shown. Click for full opinion text.)")
    elif total is not None:
        lines.append(f"({total} total. Click for full opinion text.)")
    else:
        lines.append("Click any URL for the full opinion.")
    return "\n".join(lines).rstrip() + "\n"


# ---------- CLI ----------

if __name__ == "__main__":
    import argparse
    import json
    import sys

    # Load .env so the key is available when run as a module.
    from pathlib import Path
    env = Path(__file__).resolve().parents[3] / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            os.environ.setdefault(k.strip(), v.strip())

    ap = argparse.ArgumentParser(prog="caselaw-query")
    sub = ap.add_subparsers(dest="cmd")

    p_health = sub.add_parser("health")

    p_cases = sub.add_parser("cases", help="Find cases citing a statute")
    p_cases.add_argument("citation", help="e.g. 'Cal. Veh. Code § 23152(a)'")
    p_cases.add_argument("--jurisdiction", default=None)
    p_cases.add_argument("-k", type=int, default=5)
    p_cases.add_argument("--json", action="store_true")

    p_count = sub.add_parser("count", help="Just the count of cases citing the statute")
    p_count.add_argument("citation")

    # Default subcommand: cases (so `python -m … "<citation>"` Just Works)
    if len(sys.argv) >= 2 and sys.argv[1] not in {"-h", "--help", "health", "cases", "count"}:
        sys.argv.insert(1, "cases")

    args = ap.parse_args()

    if args.cmd == "health":
        out = healthz()
        print(json.dumps(out, indent=2))
        sys.exit(0 if out.get("ok") else 1)

    if args.cmd == "count":
        print(total_for_statute(args.citation))
        sys.exit(0)

    if args.cmd == "cases" or args.cmd is None:
        if args.cmd is None:
            ap.print_help()
            sys.exit(2)
        # Single API call: results + total at once. Halves rate-limit pressure.
        results, total = search_for_statute(
            args.citation, jurisdiction=args.jurisdiction, k=args.k,
        )
        if args.json:
            print(json.dumps(
                {"citation": args.citation, "total": total, "results": results},
                indent=2,
            ))
        else:
            print(render_text(args.citation, results, total=total))
        sys.exit(0)
