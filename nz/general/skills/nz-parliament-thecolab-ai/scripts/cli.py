#!/usr/bin/env python3
"""Track New Zealand Parliament bills and their legislative progress.

Data source: the public bills.parliament.nz JSON API (keyless, no login):
- search/list bills:  POST /api/data/search
- single bill detail: GET  /api/data/Bill/{id}

`bills`  searches/lists bills (current or all, optional keyword).
`bill`   shows one bill's full detail and its stage timeline.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import ssl
import sys
import urllib.parse
from typing import Any

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "lib"))
import nzfetch  # noqa: E402

BASE = "https://bills.parliament.nz"
SEARCH_URL = f"{BASE}/api/data/search"
BILL_URL = f"{BASE}/api/data/Bill"
GUID_RE = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", re.I)


class ApiError(RuntimeError):
    """Upstream/network failure with a clean human message."""


def _request(url: str, *, payload: dict[str, Any] | None = None, timeout: int = 15) -> Any:
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    headers = {
        "Accept": "application/json",
        "Origin": BASE,
        "Referer": BASE + "/",
    }
    if data is not None:
        headers["Content-Type"] = "application/json; charset=utf-8"
    ctx = ssl.create_default_context()
    try:
        body = nzfetch.fetch_text(
            url, timeout=timeout, headers=headers, data=data,
            method="POST" if data else "GET", context=ctx,
        )
    except nzfetch.Blocked as e:
        raise ApiError(f"network error contacting bills.parliament.nz: {e}") from e
    except nzfetch.FetchError as e:
        raise ApiError(str(e)) from e
    if not body.strip():
        return {}
    try:
        return json.loads(body)
    except json.JSONDecodeError as e:
        raise ApiError(f"invalid JSON from {url}: {e}") from e


# ---------------------------------------------------------------------------
# Data access
# ---------------------------------------------------------------------------

def _search_payload(keyword: str | None, scope: str, limit: int, page: int) -> dict[str, Any]:
    # Mirror the fields the bills.parliament.nz front-end sends; missing fields
    # cause the API to 500, so send the full shape with sensible defaults.
    return {
        "id": None,
        "documentPreset": 1,  # 1 = bills (the only dataset this endpoint serves)
        "keyword": keyword or None,
        "selectCommittee": None,
        "status": [],
        "documentTypes": [],
        "documentSubtypes": [],
        "beforeCommittee": None,
        "billStages": [],
        "billTab": "All" if scope == "all" else "Current",
        "billId": None,
        "includeBillStages": True,
        "subject": None,
        "person": None,
        "parliament": None,
        "dateFrom": None,
        "dateTo": None,
        "datePeriod": None,
        "restrictedFrom": None,
        "restrictedTo": None,
        "terminatedReason": None,
        "prettyTerminatedReason": None,
        "terminatedReasons": [],
        "column": 17,      # default sort column used by the site (latest activity)
        "direction": 1,
        "pageSize": max(1, min(limit, 50)),
        "page": max(1, page),
    }


def search_bills(keyword: str | None, scope: str, limit: int, page: int) -> dict[str, Any]:
    data = _request(SEARCH_URL, payload=_search_payload(keyword, scope, limit, page))
    results = [normalise_summary(b) for b in (data.get("results") or [])]
    return {
        "scope": scope,
        "keyword": keyword,
        "page": data.get("page", page),
        "page_size": data.get("pageSize", limit),
        "total": data.get("totalResults"),
        "count": len(results),
        "results": results,
    }


def get_bill_by_id(bill_id: str) -> dict[str, Any]:
    return _request(f"{BILL_URL}/{urllib.parse.quote(bill_id)}")


def resolve_bill(ref: str) -> dict[str, Any]:
    """Resolve a bill id (GUID) or bill number (e.g. '324-1') to full detail."""
    bill_id = ref
    if not GUID_RE.match(ref):
        # Treat as a bill number / title keyword: search all and match the number.
        found = search_bills(ref, "all", 20, 1)["results"]
        match = next((b for b in found if (b.get("bill_number") or "").lower() == ref.lower()), None)
        if match is None and found:
            match = found[0]
        if match is None:
            raise ApiError(f"no bill found for {ref!r}")
        bill_id = match["id"]
    return normalise_detail(get_bill_by_id(bill_id))


# ---------------------------------------------------------------------------
# Normalisation (the search endpoint is camelCase, detail is PascalCase)
# ---------------------------------------------------------------------------

def page_url(bill_id: str | None) -> str | None:
    return f"{BASE}/v/6/{bill_id}" if bill_id else None


def normalise_summary(b: dict[str, Any]) -> dict[str, Any]:
    bid = b.get("id")
    return {
        "id": bid,
        "title": b.get("title"),
        "bill_number": b.get("billNumber"),
        "type": b.get("itemType"),          # Government / Member's / Local / Private
        "status": b.get("status") or b.get("billCurrentStageName"),
        "current_stage": b.get("billCurrentStageName"),
        "member": b.get("memberName"),
        "party": b.get("partyName"),
        "parliament": b.get("parliamentNumber"),
        "last_activity": b.get("lastStageDate") or b.get("lastModified") or b.get("date"),
        "url": page_url(bid),
    }


def _date(value: Any) -> Any:
    # Trim ISO timestamps to the date for readability; pass through anything else.
    if isinstance(value, str) and len(value) >= 10 and value[4] == "-":
        return value[:10]
    return value


def normalise_detail(d: dict[str, Any]) -> dict[str, Any]:
    bid = d.get("Id")
    members = []
    for m in d.get("Members") or []:
        if not isinstance(m, dict):
            continue
        name = m.get("PreferredFormOfAddress") or m.get("DisplayName") or m.get("SortedName")
        if name:
            members.append({"name": name, "party": m.get("PartyName")})
    stages = []
    for s in d.get("Stages") or []:
        if isinstance(s, dict):
            stages.append({"name": s.get("Name") or s.get("StageName"), "date": _date(s.get("Date") or s.get("StageDate"))})
    attachments = []
    for a in d.get("Attachments") or []:
        if isinstance(a, dict):
            attachments.append({"name": a.get("Name") or a.get("Title"), "url": a.get("Url") or a.get("DownloadUrl")})
    committee = d.get("SelectCommitteeInfo")
    if isinstance(committee, dict):
        committee = committee.get("Name") or committee.get("CommitteeName")
    return {
        "id": bid,
        "title": d.get("Title"),
        "bill_number": d.get("BillNumber"),
        "type": d.get("BillTypeName"),
        "status": d.get("BillStatusName"),
        "current_stage": d.get("BillCurrentStageName"),
        "parliament": d.get("ParliamentNumber"),
        "members": members,
        "select_committee": committee,
        "introduced": _date(d.get("IntroducedDate") or d.get("InitiationDate")),
        "first_reading": _date(d.get("FirstReadingDate")),
        "public_submissions": d.get("PublicSubmissionCalled"),
        "description": d.get("Description"),
        "legislation_url": d.get("BillLegislationUrl"),
        "stages": stages,
        "attachments": attachments,
        "url": page_url(bid),
    }


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_bills(args: argparse.Namespace) -> int:
    scope = "all" if args.all else "current"
    data = search_bills(args.keyword, scope, args.limit, args.page)
    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return 0
    label = "all" if scope == "all" else "current"
    kw = f" matching {args.keyword!r}" if args.keyword else ""
    total = data["total"]
    print(f"{total if total is not None else '?'} {label} bills{kw} (showing {data['count']}, page {data['page']})")
    for b in data["results"]:
        sponsor = f" — {b['member']} ({b['party']})" if b.get("member") else ""
        num = b.get("bill_number") or "—"
        print(f"\n  [{b.get('type') or '?'}] {num}  {b.get('title')}")
        print(f"    {b.get('current_stage') or b.get('status') or ''}{sponsor}")
        if b.get("last_activity"):
            print(f"    last activity: {_date(b['last_activity'])}")
        if b.get("url"):
            print(f"    {b['url']}")
    return 0


def cmd_bill(args: argparse.Namespace) -> int:
    bill = resolve_bill(args.bill)
    if args.json:
        print(json.dumps(bill, indent=2, ensure_ascii=False))
        return 0
    print(f"{bill.get('bill_number') or ''}  {bill.get('title')}")
    print(f"  Type: {bill.get('type')}  |  Status: {bill.get('status')}  |  Parliament: {bill.get('parliament')}")
    if bill.get("members"):
        names = [f"{m['name']} ({m['party']})" if m.get("party") else m["name"] for m in bill["members"]]
        print("  Member(s): " + ", ".join(names))
    if bill.get("select_committee"):
        print(f"  Select committee: {bill['select_committee']}")
    if bill.get("introduced"):
        print(f"  Introduced: {bill['introduced']}")
    if bill.get("description"):
        print(f"\n  {bill['description'][:500]}")
    if bill.get("stages"):
        print("\n  Stages:")
        for s in bill["stages"]:
            print(f"    {s.get('date') or '          '}  {s.get('name')}")
    if bill.get("attachments"):
        print("\n  Documents:")
        for a in bill["attachments"]:
            print(f"    {a.get('name')}  {a.get('url') or ''}")
    if bill.get("url"):
        print(f"\n  {bill['url']}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        description="Track New Zealand Parliament bills and their legislative progress (bills.parliament.nz)."
    )
    sub = ap.add_subparsers(dest="command", required=True)

    p_bills = sub.add_parser("bills", help="search / list bills (current by default)")
    p_bills.add_argument("-k", "--keyword", help="full-text keyword to search bill titles/content")
    p_bills.add_argument("--all", action="store_true", help="include all bills (default: current only)")
    p_bills.add_argument("--limit", type=int, default=20, help="max bills to return (1-50, default 20)")
    p_bills.add_argument("--page", type=int, default=1, help="results page (default 1)")
    p_bills.add_argument("--json", action="store_true", help="emit JSON")
    p_bills.set_defaults(func=cmd_bills)

    p_bill = sub.add_parser("bill", help="show one bill's detail and stage timeline")
    p_bill.add_argument("bill", help="bill number (e.g. 324-1) or bill id (GUID)")
    p_bill.add_argument("--json", action="store_true", help="emit JSON")
    p_bill.set_defaults(func=cmd_bill)

    return ap


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except ApiError as e:
        if getattr(args, "json", False):
            print(json.dumps({"error": "upstream_error", "message": str(e)}, indent=2), file=sys.stderr)
        else:
            print(f"nz-parliament: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
