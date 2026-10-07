"""
Specter Harvester API client.

Thin wrapper Specter (the OpenClaw agent) uses to query the FastAPI service.
Reads SPECTER_API from env, defaults to http://127.0.0.1:8000.

Design notes:
- Returns plain dicts/lists — easy for the agent to inspect, format, or pipe to JSON.
- Fail-fast on transport errors (raise httpx.HTTPError) so the agent can decide
  whether to retry, fall back to web search, or report API-down to the user.
- 404 on /lookup is NOT an exception — it's a clean "not found" the agent should
  handle gracefully ("not in the Harvester yet").
"""
from __future__ import annotations

import os
from typing import Any, Optional

import httpx

API_BASE = os.getenv("SPECTER_API", "http://127.0.0.1:8000").rstrip("/")
DEFAULT_TIMEOUT = 15.0


def _client() -> httpx.Client:
    return httpx.Client(base_url=API_BASE, timeout=DEFAULT_TIMEOUT)


def healthz() -> dict[str, Any]:
    """Liveness check. Returns {'ok': True, 'collection': ..., 'count': N}."""
    with _client() as c:
        r = c.get("/healthz")
        r.raise_for_status()
        return r.json()


def list_factors() -> list[str]:
    """The 17 canonical contributing-factor categories."""
    with _client() as c:
        r = c.get("/factors")
        r.raise_for_status()
        return list(r.json().get("factors", []))


def lookup_citation(citation: str) -> Optional[dict[str, Any]]:
    """
    Exact citation lookup. Returns the record dict, or None if not present.

    `citation` should match the canonical form in the Harvester:
        "Cal. Veh. Code § 23152(a)"

    If you're not sure of canonical form, run normalization first
    (see openclaw/skills/citation-format).
    """
    with _client() as c:
        r = c.get("/lookup", params={"citation": citation})
        if r.status_code == 404:
            return None
        r.raise_for_status()
        return r.json()


def search(
    q: str,
    *,
    state: Optional[str] = None,
    factor: Optional[str] = None,
    pi_only: bool = False,
    k: int = 10,
) -> list[dict[str, Any]]:
    """
    Semantic + filtered search.

    state: 2-letter code ("CA", "TX"). Case-insensitive on the API side, but pass uppercase.
    factor: one of the 17 canonical categories. Server will 400 on invalid factor.
    pi_only: if True, restrict to records the tagger marked PI-relevant.
    k: top-k results.

    Returns the `results` array (list of dicts with id/score/text/citation/source_url/...).
    """
    params: dict[str, Any] = {"q": q, "k": k, "pi_only": str(pi_only).lower()}
    if state:
        params["state"] = state.upper()
    if factor:
        params["factor"] = factor
    with _client() as c:
        r = c.get("/search", params=params)
        r.raise_for_status()
        return list(r.json().get("results", []))


def ask(
    question: str,
    *,
    state: Optional[str] = None,
    factor: Optional[str] = None,
    k: int = 8,
) -> list[dict[str, Any]]:
    """
    Natural-language question wrapper. Same retrieval as `search` under the hood.
    Returns the `hits` array.
    """
    body: dict[str, Any] = {"question": question, "k": k}
    if state:
        body["state"] = state.upper()
    if factor:
        body["factor"] = factor
    with _client() as c:
        r = c.post("/ask", json=body)
        r.raise_for_status()
        return list(r.json().get("hits", []))


# Convenience for ad-hoc CLI use:
#   python -m openclaw.skills.harvester_query.client lookup "Cal. Veh. Code § 23152(a)"
#   python -m openclaw.skills.harvester_query.client search "drunk driving" --state CA --factor "DUI/DWI"
if __name__ == "__main__":
    import argparse
    import json
    import sys

    ap = argparse.ArgumentParser(prog="harvester-query")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("health")
    sub.add_parser("factors")

    p_lookup = sub.add_parser("lookup")
    p_lookup.add_argument("citation")

    p_search = sub.add_parser("search")
    p_search.add_argument("q")
    p_search.add_argument("--state")
    p_search.add_argument("--factor")
    p_search.add_argument("--pi-only", action="store_true")
    p_search.add_argument("-k", type=int, default=10)

    p_ask = sub.add_parser("ask")
    p_ask.add_argument("question")
    p_ask.add_argument("--state")
    p_ask.add_argument("--factor")
    p_ask.add_argument("-k", type=int, default=8)

    args = ap.parse_args()

    try:
        if args.cmd == "health":
            print(json.dumps(healthz(), indent=2))
        elif args.cmd == "factors":
            print(json.dumps(list_factors(), indent=2))
        elif args.cmd == "lookup":
            res = lookup_citation(args.citation)
            print(json.dumps(res, indent=2) if res else "null")
        elif args.cmd == "search":
            res = search(args.q, state=args.state, factor=args.factor,
                         pi_only=args.pi_only, k=args.k)
            print(json.dumps(res, indent=2))
        elif args.cmd == "ask":
            res = ask(args.question, state=args.state, factor=args.factor, k=args.k)
            print(json.dumps(res, indent=2))
    except httpx.HTTPError as e:
        print(f"[harvester-query] transport error: {e}", file=sys.stderr)
        sys.exit(2)
