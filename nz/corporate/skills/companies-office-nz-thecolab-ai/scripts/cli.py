#!/usr/bin/env python3
"""Companies Office NZ public register CLI.

Provides read-only access to the New Zealand Companies Register via the
public website endpoints used by the register UI. No login, API key, or
account credentials required.

Supported commands:
  search     - search by name, company number, or NZBN
  entity     - summary + addresses for one company
  directors  - current directors (HTML parse, public)
  shareholders - shareholder allocations (HTML parse, public)
  documents  - filing history / documents list (JSON API)
  full       - all of the above in one call
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import sys
import time
import urllib.parse
from typing import Any

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "lib"))
import nzfetch  # noqa: E402

BASE = "https://app.companiesoffice.govt.nz/companies/app"
SVC = BASE + "/service/services"
UI = BASE + "/ui/pages/companies"

# entityStatus integer → readable label (observed values only)
STATUS_MAP = {
    10: "PRE-REGISTRATION",
    50: "REGISTERED",
    80: "REMOVED",
    90: "IN LIQUIDATION",
    91: "IN RECEIVERSHIP",
    92: "IN VOLUNTARY ADMINISTRATION",
    93: "AMALGAMATED",
    94: "DISSOLVED",
    95: "CONVERTED",
}


def die(msg: str, code: int = 1) -> None:
    print(f"companies-office-nz: {msg}", file=sys.stderr)
    raise SystemExit(code)


def get_json(url: str, timeout: int = 25) -> Any:
    try:
        return nzfetch.fetch_json(
            url,
            timeout=timeout,
            accept="application/json, text/html, */*",
            headers={
                "Referer": BASE + "/ui/pages/companies/search",
                "X-Requested-With": "XMLHttpRequest",
            },
        )
    except nzfetch.Blocked as e:
        die(f"network error: {e}")
    except nzfetch.FetchError as e:
        die(str(e))


def get_html(url: str, timeout: int = 25) -> str:
    try:
        return nzfetch.fetch_text(
            url,
            timeout=timeout,
            accept="text/html,*/*",
        )
    except nzfetch.Blocked as e:
        die(f"network error: {e}")
    except nzfetch.FetchError as e:
        die(str(e))


# ---------------------------------------------------------------------------
# Data helpers
# ---------------------------------------------------------------------------

def _compact_addr(parts: list[str | None]) -> str:
    return ", ".join(p.strip() for p in parts if p and p.strip())


def _status_label(code: int | str | None) -> str:
    if code is None:
        return "UNKNOWN"
    try:
        return STATUS_MAP.get(int(code), str(code))
    except (ValueError, TypeError):
        return str(code)


def _addr_line(a: dict) -> str:
    return _compact_addr([a.get("line1"), a.get("line2"), a.get("line3"), a.get("line4"), a.get("postCode"), a.get("countryCode")])


def _fmt_phone(phone: Any) -> str | None:
    if not phone:
        return None
    if isinstance(phone, str):
        return phone or None
    if isinstance(phone, dict):
        parts = [phone.get("countryCode"), phone.get("area"), phone.get("number")]
        combined = " ".join(str(p) for p in parts if p)
        return combined or None
    return None


def search_company(query: str, limit: int = 10, start: int = 0) -> dict:
    params = urllib.parse.urlencode({"mode": "company", "q": query, "start": start, "limit": limit})
    url = f"{SVC}/entity/search?{params}"
    t0 = time.perf_counter()
    data = get_json(url)
    elapsed = round((time.perf_counter() - t0) * 1000)
    items = data.get("list") or []
    return {
        "query": query,
        "total_matches": data.get("totalMatches"),
        "returned": len(items),
        "elapsed_ms": elapsed,
        "results": [
            {
                "company_number": r.get("identifier"),
                "nzbn": r.get("nzbn"),
                "name": r.get("name"),
                "status": r.get("statusGroup"),
                "entity_type": r.get("entityType"),
                "incorporation_date": (r.get("incorporationDate") or "")[:10] or None,
                "registered_office": r.get("entityRegisteredOffice"),
                "url": f"https://app.companiesoffice.govt.nz/companies/app/ui/pages/companies/{r.get('identifier')}",
            }
            for r in items
            if isinstance(r, dict) and r.get("category") == "entity"
        ],
    }


def resolve_company_id(identifier: str) -> str:
    """
    Given a company number, NZBN, or name query, return the numeric company identifier.
    If `identifier` is already a pure number, return it directly after confirming entity exists.
    Otherwise search and return first match.
    """
    clean = re.sub(r"\D", "", identifier)
    if len(clean) >= 7 and identifier.strip().lstrip("0").isdigit() or clean == identifier.strip():
        # Looks like a company number or NZBN - search for it
        results = search_company(identifier.strip(), limit=1)
        hits = results.get("results") or []
        if hits:
            return hits[0]["company_number"]
        # If no search hit, try using it directly as entity id
        return identifier.strip()
    # Text query - return first match
    results = search_company(identifier.strip(), limit=1)
    hits = results.get("results") or []
    if not hits:
        die(f"no company found matching: {identifier}")
    return hits[0]["company_number"]


def fetch_entity(company_id: str) -> dict:
    data = get_json(f"{SVC}/entity/{company_id}")
    addrs_data = get_json(f"{SVC}/entity/{company_id}/addresses")

    current_addrs = (addrs_data.get("currentAddresses") or {}).get("addresses") or []
    reg_idx = (addrs_data.get("currentAddresses") or {}).get("registeredIndexes") or []
    svc_idx = (addrs_data.get("currentAddresses") or {}).get("serviceIndexes") or []

    def pick_addr(idx_list: list) -> str | None:
        for i in idx_list:
            if 0 <= i < len(current_addrs):
                return _addr_line(current_addrs[i])
        return None

    prev_names = [
        {
            "name": p.get("name"),
            "from": (p.get("start") or "")[:10] or None,
            "to": (p.get("end") or "")[:10] or None,
        }
        for p in (data.get("previousNames") or [])
        if isinstance(p, dict)
    ]

    return {
        "company_number": data.get("entityIdentifier"),
        "name": data.get("name"),
        "entity_type": data.get("entityType"),
        "status": _status_label(data.get("entityStatus")),
        "incorporation_date": (data.get("registrationDateTime") or "")[:10] or None,
        "last_updated": (data.get("lastUpdated") or "")[:10] or None,
        "director_count": data.get("directorCount"),
        "shareholder_count": data.get("shareholderCount"),
        "document_count": data.get("docCount"),
        "previous_names": prev_names,
        "overseas_company": data.get("overseasCompany"),
        "registered_office": pick_addr(reg_idx),
        "address_for_service": pick_addr(svc_idx),
        "website": addrs_data.get("webUrl") or addrs_data.get("websiteWithProtocol"),
        "email": addrs_data.get("email") if isinstance(addrs_data.get("email"), str) else None,
        "phone": _fmt_phone(addrs_data.get("phone")),
        "url": f"https://app.companiesoffice.govt.nz/companies/app/ui/pages/companies/{data.get('entityIdentifier')}",
    }


def _strip_html(html: str) -> str:
    """Remove HTML tags and collapse whitespace."""
    text = re.sub(r"<[^>]+>", " ", html)
    return re.sub(r"\s+", " ", text).strip()


def fetch_directors(company_id: str) -> list[dict]:
    html = get_html(f"{UI}/{company_id}/directors")

    # Each director is in a <div class="allocationDetail"> or <td class="director"> block
    directors: list[dict] = []

    # Parse the directorsPanel section
    panel_match = re.search(r'id="directorsPanel"[^>]*>([\s\S]*?)(?:<div class="secondaryPanel|Generated on)', html)
    if not panel_match:
        # Fallback: look for director table cells
        panel_match = re.search(r'directorsPanel([\s\S]{0,50000})', html)
    panel = panel_match.group(1) if panel_match else html

    # Split into individual director blocks by <td class="director">
    td_blocks = re.split(r'<td[^>]*class="director"[^>]*>', panel)
    if len(td_blocks) < 2:
        # Alternative: split by director div structure
        td_blocks = re.split(r'(?=<div class="row"><label[^>]*>\s*Full legal name)', panel)

    for block in td_blocks[1:]:
        # Extract name
        name_match = re.search(
            r'Full legal name:\s*</label>\s*([\s\S]*?)(?:</div>|<div)',
            block,
        )
        name = _strip_html(name_match.group(1)) if name_match else None

        # Extract residential address
        addr_match = re.search(
            r'Residential Address:\s*</label>\s*([\s\S]*?)(?:</div>|<div)',
            block,
        )
        addr_raw = ""
        if addr_match:
            # Address may span multiple elements
            addr_section = re.search(
                r'Residential Address.*?</label>([\s\S]*?)(?:<div class="row"><label|$)',
                block,
            )
            if addr_section:
                addr_raw = _strip_html(addr_section.group(1))

        # Extract appointment date
        appt_match = re.search(r'Appointment Date:\s*</label>\s*([0-9][^<\n]{3,30}?)(?:\s*</div>|\s*<)', block)
        appt = appt_match.group(1).strip() if appt_match else None

        # Extract ceased/resignation date if present
        ceased_match = re.search(r'(?:Ceased|Resignation)\s+Date:\s*</label>\s*([0-9][^<\n]{3,30}?)(?:\s*</div>|\s*<)', block)
        ceased = ceased_match.group(1).strip() if ceased_match else None

        if name:
            directors.append({
                "name": name,
                "address": addr_raw if addr_raw else None,
                "appointment_date": appt,
                "ceased_date": ceased,
            })

    return directors


def fetch_shareholders(company_id: str) -> dict:
    html = get_html(f"{UI}/{company_id}/shareholdings")

    # Extract from shareholdersPanel to Generated on (don't stop at inner <div id=>)
    idx_start = html.find('id="shareholdersPanel"')
    idx_end = html.find("Generated on", idx_start if idx_start >= 0 else 0)
    if idx_start >= 0:
        panel = html[idx_start: idx_end if idx_end > idx_start else idx_start + 30000]
    else:
        panel = html
    panel_match = re.search(r'id="shareholdersPanel"[^>]*>([\s\S]*)', panel)
    panel = panel_match.group(1) if panel_match else html

    # Total shares
    total_match = re.search(r'Total Number of Shares:\s*</label><span>([0-9,]+)</span>', panel)
    total_shares = int(total_match.group(1).replace(",", "")) if total_match else None

    extensive = bool(re.search(r'Extensive Shareholding[^<]*<[^>]*class="yesLabel"', panel))

    note_match = re.search(r'<div class="captionText">([\s\S]*?)</div>', panel)
    note = _strip_html(note_match.group(1)) if note_match else None

    # Parse individual allocations
    allocations: list[dict] = []
    alloc_blocks = re.split(r'<div class="allocationDetail">', panel)
    for block in alloc_blocks[1:]:
        # Shares and percentage
        shares_match = re.search(r"name='shares'\s+value='([0-9]+)'", block)
        shares = int(shares_match.group(1)) if shares_match else None

        pct_match = re.search(r"\(([0-9.]+)%\)", block)
        pct = float(pct_match.group(1)) if pct_match else None

        # Holder names - may be multiple. Each holder group is separated by
        # <div class="clear">. The first labelValue col2 in each group is the
        # holder name; the second is the address (which we skip here).
        holder_names: list[str] = []
        # Split by clear divs to isolate each holder group
        holder_blocks = re.split(r'<div class="clear"[^>]*>', block)
        for hb in holder_blocks:
            # Company link
            company_link = re.search(
                r'<a href="/companies/app/ui/pages/companies/([0-9]+)"[^>]*>([^<]+)</a>', hb
            )
            if company_link:
                holder_names.append(f"{company_link.group(2).strip()} ({company_link.group(1)})")
                continue
            # Plain name in a multi-line labelValue div (name rows have whitespace/newlines
            # before the closing tag, unlike compact address rows)
            name_m = re.search(
                r'<div class="labelValue col2">\s*\n([\s\S]*?)\n\s*</div>', hb
            )
            if name_m:
                txt = _strip_html(name_m.group(1))
                if txt and len(txt) < 150:
                    holder_names.append(txt)

        if shares is not None:
            allocations.append({
                "allocation": len(allocations) + 1,
                "shares": shares,
                "percentage": pct,
                "holders": holder_names,
            })

    return {
        "total_shares": total_shares,
        "extensive_shareholding": extensive,
        "note": note,
        "allocations": allocations,
    }


def fetch_documents(company_id: str, limit: int = 20, start: int = 0) -> dict:
    params = urllib.parse.urlencode({"start": start, "count": limit})
    data = get_json(f"{SVC}/entity/{company_id}/documents?{params}")
    items = data.get("list") or []
    total = data.get("count")
    return {
        "total": total,
        "start": start,
        "returned": len(items),
        "documents": [
            {
                "id": d.get("id"),
                "date": d.get("registrationDate"),
                "type": d.get("description"),
                "filing_code": d.get("bseFunctionCode"),
                "attachments": [
                    {
                        "id": a.get("id"),
                        "description": a.get("description"),
                        "code": a.get("documentCode"),
                        "url": f"https://app.companiesoffice.govt.nz/companies/app/service/services/documents/{a['drmKey']}"
                        if a.get("drmKey")
                        else None,
                    }
                    for a in (d.get("attachments") or [])
                    if isinstance(a, dict)
                ],
            }
            for d in items
            if isinstance(d, dict)
        ],
    }


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def _section(title: str) -> None:
    print(f"\n{title}")
    print("-" * len(title))


def emit(data: Any, as_json: bool, output_mode: str = "human") -> None:
    if as_json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return
    if output_mode == "md":
        emit_md(data)
        return
    emit_human(data)


def emit_human(data: Any) -> None:
    kind = data.get("_kind") if isinstance(data, dict) else None

    if kind == "search":
        total = data.get("total_matches")
        results = data.get("results") or []
        print(f"Companies Office search: {total} total, showing {len(results)} ({data.get('elapsed_ms')} ms)")
        print()
        for r in results:
            status = r.get("status") or ""
            etype = r.get("entity_type") or ""
            inc = r.get("incorporation_date") or ""
            print(f"{r.get('company_number'):>10}  {r.get('name')}")
            print(f"           {status} {etype} inc:{inc}".rstrip())
            if r.get("registered_office"):
                print(f"           {r['registered_office']}")
            if r.get("nzbn"):
                print(f"           NZBN: {r['nzbn']}")
            print()

    elif kind == "entity":
        e = data.get("entity") or {}
        print(f"{e.get('company_number')}  {e.get('name')}")
        print(f"  Status: {e.get('status')}  Type: {e.get('entity_type')}")
        if e.get("incorporation_date"):
            print(f"  Incorporated: {e['incorporation_date']}")
        if e.get("previous_names"):
            for pn in e["previous_names"]:
                print(f"  prev name: {pn['name']} ({pn.get('from','')} - {pn.get('to','')})")
        if e.get("registered_office"):
            print(f"  Registered office: {e['registered_office']}")
        if e.get("address_for_service"):
            print(f"  Address for service: {e['address_for_service']}")
        if e.get("website"):
            print(f"  Website: {e['website']}")
        if e.get("email"):
            print(f"  Email: {e['email']}")
        if e.get("phone"):
            print(f"  Phone: {e['phone']}")
        print(f"  Directors: {e.get('director_count')}  Shareholders: {e.get('shareholder_count')}  Documents: {e.get('document_count')}")
        print(f"  {e.get('url')}")
        print(f"  (fetched in {data.get('elapsed_ms')} ms)")

    elif kind == "directors":
        dirs = data.get("directors") or []
        print(f"Directors ({len(dirs)}) for company {data.get('company_number')} {data.get('company_name', '')}:")
        for d in dirs:
            status = " [CEASED]" if d.get("ceased_date") else ""
            print(f"  {d['name']}{status}")
            if d.get("appointment_date"):
                print(f"    Appointed: {d['appointment_date']}", end="")
                if d.get("ceased_date"):
                    print(f"  Ceased: {d['ceased_date']}", end="")
                print()
            if d.get("address"):
                print(f"    Address: {d['address']}")

    elif kind == "shareholders":
        sh = data.get("shareholders") or {}
        print(f"Shareholders for company {data.get('company_number')} {data.get('company_name', '')}:")
        if sh.get("total_shares"):
            print(f"  Total shares: {sh['total_shares']:,}")
        if sh.get("extensive_shareholding"):
            print("  Extensive shareholding (listed company - top parcels only)")
        if sh.get("note"):
            print(f"  Note: {sh['note']}")
        for alloc in sh.get("allocations") or []:
            holders = ", ".join(alloc.get("holders") or []) or "(unknown)"
            pct = f"{alloc['percentage']:.2f}%" if alloc.get("percentage") else ""
            print(f"  [{alloc['allocation']}] {alloc.get('shares', 0):,} shares {pct}")
            print(f"      {holders}")

    elif kind == "documents":
        docs = data.get("documents") or {}
        items = docs.get("documents") or []
        total = docs.get("total", 0)
        print(f"Documents for company {data.get('company_number')} {data.get('company_name', '')}: {total} total, showing {len(items)}")
        for doc in items:
            atts = doc.get("attachments") or []
            att_info = f" [{len(atts)} attachment(s)]" if atts else ""
            print(f"  [{doc.get('date')}] {doc.get('type')}{att_info}")
            for a in atts:
                if a.get("url"):
                    print(f"    -> {a['url']}")

    elif kind == "full":
        # Delegate to sub-sections
        emit_human({**data, "_kind": "entity"})
        _section("Directors")
        emit_human({**data, "_kind": "directors"})
        _section("Shareholders")
        emit_human({**data, "_kind": "shareholders"})
        _section("Recent Documents")
        emit_human({**data, "_kind": "documents"})

    else:
        print(json.dumps(data, indent=2, ensure_ascii=False))


def emit_md(data: Any) -> None:
    kind = data.get("_kind") if isinstance(data, dict) else None

    if kind == "search":
        results = data.get("results") or []
        total = data.get("total_matches")
        print(f"# Companies Office Search\n")
        print(f"Query: **{data.get('query')}** — {total} total, {len(results)} shown\n")
        print("| # | Name | Status | Type | Incorporated | Office |")
        print("|---|------|--------|------|-------------|--------|")
        for r in results:
            name_link = f"[{r.get('name')}]({r.get('url')})"
            print(f"| {r.get('company_number')} | {name_link} | {r.get('status')} | {r.get('entity_type')} | {r.get('incorporation_date','')} | {r.get('registered_office','')} |")

    elif kind == "entity":
        e = data.get("entity") or {}
        print(f"# {e.get('name')} ({e.get('company_number')})\n")
        print(f"**Status:** {e.get('status')}  ")
        print(f"**Type:** {e.get('entity_type')}  ")
        print(f"**Incorporated:** {e.get('incorporation_date','')}  ")
        if e.get("previous_names"):
            print("\n## Previous Names\n")
            for pn in e["previous_names"]:
                print(f"- {pn['name']} ({pn.get('from','')} — {pn.get('to','')})")
        print("\n## Addresses\n")
        if e.get("registered_office"):
            print(f"**Registered office:** {e['registered_office']}  ")
        if e.get("address_for_service"):
            print(f"**Address for service:** {e['address_for_service']}  ")
        if e.get("website"):
            print(f"\n**Website:** {e['website']}  ")

    elif kind == "directors":
        dirs = data.get("directors") or []
        print(f"## Directors ({len(dirs)})\n")
        print("| Name | Appointed | Ceased | Address |")
        print("|------|-----------|--------|---------|")
        for d in dirs:
            ceased = d.get("ceased_date") or ""
            addr = d.get("address") or ""
            print(f"| {d['name']} | {d.get('appointment_date','')} | {ceased} | {addr} |")

    elif kind == "shareholders":
        sh = data.get("shareholders") or {}
        allocs = sh.get("allocations") or []
        total_shares = sh.get("total_shares")
        print(f"\n## Shareholders\n")
        if total_shares:
            print(f"**Total shares:** {total_shares:,}  ")
        if sh.get("extensive_shareholding"):
            print("*Listed company — top parcels only*  ")
        print()
        print("| # | Shares | % | Holders |")
        print("|---|--------|---|---------|")
        for a in allocs:
            pct = f"{a['percentage']:.2f}" if a.get("percentage") else ""
            holders = ", ".join(a.get("holders") or []) or "—"
            print(f"| {a['allocation']} | {a.get('shares',0):,} | {pct} | {holders} |")

    elif kind == "documents":
        docs = data.get("documents") or {}
        items = docs.get("documents") or []
        print(f"\n## Documents ({docs.get('total',0)} total)\n")
        print("| Date | Type | Attachments |")
        print("|------|------|-------------|")
        for doc in items:
            atts = doc.get("attachments") or []
            att_links = " ".join(f"[{a.get('description',a.get('code','doc'))}]({a['url']})" for a in atts if a.get("url")) or "—"
            print(f"| {doc.get('date','')} | {doc.get('type','')} | {att_links} |")

    elif kind == "full":
        emit_md({**data, "_kind": "entity"})
        emit_md({**data, "_kind": "directors"})
        emit_md({**data, "_kind": "shareholders"})
        emit_md({**data, "_kind": "documents"})

    else:
        print(json.dumps(data, indent=2, ensure_ascii=False))


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_search(args: argparse.Namespace) -> None:
    t0 = time.perf_counter()
    data = search_company(args.query, limit=args.limit, start=args.start)
    data["_kind"] = "search"
    data["elapsed_ms"] = data.get("elapsed_ms")
    emit(data, args.json, args.output)


def cmd_entity(args: argparse.Namespace) -> None:
    if args.nzbn:
        company_id = resolve_company_id(args.nzbn)
    else:
        company_id = args.company_number
    t0 = time.perf_counter()
    entity = fetch_entity(company_id)
    elapsed = round((time.perf_counter() - t0) * 1000)
    data = {"_kind": "entity", "entity": entity, "elapsed_ms": elapsed}
    emit(data, args.json, args.output)


def cmd_directors(args: argparse.Namespace) -> None:
    company_id = args.company_number
    t0 = time.perf_counter()
    dirs = fetch_directors(company_id)
    elapsed = round((time.perf_counter() - t0) * 1000)
    # Also get company name
    try:
        entity = get_json(f"{SVC}/entity/{company_id}")
        name = entity.get("name", "")
    except SystemExit:
        name = ""
    data = {
        "_kind": "directors",
        "company_number": company_id,
        "company_name": name,
        "directors": dirs,
        "elapsed_ms": elapsed,
    }
    emit(data, args.json, args.output)


def cmd_shareholders(args: argparse.Namespace) -> None:
    company_id = args.company_number
    t0 = time.perf_counter()
    sh = fetch_shareholders(company_id)
    elapsed = round((time.perf_counter() - t0) * 1000)
    try:
        entity = get_json(f"{SVC}/entity/{company_id}")
        name = entity.get("name", "")
    except SystemExit:
        name = ""
    data = {
        "_kind": "shareholders",
        "company_number": company_id,
        "company_name": name,
        "shareholders": sh,
        "elapsed_ms": elapsed,
    }
    emit(data, args.json, args.output)


def cmd_documents(args: argparse.Namespace) -> None:
    company_id = args.company_number
    t0 = time.perf_counter()
    docs = fetch_documents(company_id, limit=args.limit, start=args.start)
    elapsed = round((time.perf_counter() - t0) * 1000)
    try:
        entity = get_json(f"{SVC}/entity/{company_id}")
        name = entity.get("name", "")
    except SystemExit:
        name = ""
    data = {
        "_kind": "documents",
        "company_number": company_id,
        "company_name": name,
        "documents": docs,
        "elapsed_ms": elapsed,
    }
    emit(data, args.json, args.output)


def cmd_full(args: argparse.Namespace) -> None:
    company_id = args.company_number
    t0 = time.perf_counter()

    entity = fetch_entity(company_id)
    name = entity.get("name", "")
    dirs = fetch_directors(company_id)
    sh = fetch_shareholders(company_id)
    docs = fetch_documents(company_id, limit=args.doc_limit, start=0)

    elapsed = round((time.perf_counter() - t0) * 1000)

    data = {
        "_kind": "full",
        "company_number": company_id,
        "company_name": name,
        "entity": entity,
        "directors": dirs,
        "shareholders": sh,
        "documents": docs,
        "elapsed_ms": elapsed,
    }
    emit(data, args.json, args.output)


# ---------------------------------------------------------------------------
# Argument parser
# ---------------------------------------------------------------------------

def _add_output_flags(p: argparse.ArgumentParser) -> None:
    p.add_argument("--json", action="store_true", help="emit JSON")
    p.add_argument("--output", choices=["human", "md"], default="human", help="output format (human or md)")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="companies-office-nz",
        description="Query the New Zealand Companies Register (read-only, no login required)",
    )
    sub = p.add_subparsers(dest="command", required=True)

    # search
    s = sub.add_parser("search", help="search by company name, number, or NZBN")
    s.add_argument("query", help="company name, number, or NZBN")
    s.add_argument("--limit", type=int, default=10, help="max results (default: 10)")
    s.add_argument("--start", type=int, default=0, help="result offset (default: 0)")
    _add_output_flags(s)
    s.set_defaults(func=cmd_search)

    # entity
    e = sub.add_parser("entity", help="company summary and addresses")
    e.add_argument("company_number", nargs="?", help="numeric company number")
    e.add_argument("--nzbn", help="look up by 13-digit NZBN instead")
    _add_output_flags(e)
    e.set_defaults(func=cmd_entity)

    def entity_wrapper(args: argparse.Namespace) -> None:
        if not args.company_number and not args.nzbn:
            e.error("company_number or --nzbn is required")
        cmd_entity(args)
    e.set_defaults(func=entity_wrapper)

    # directors
    d = sub.add_parser("directors", help="list directors (current and historical)")
    d.add_argument("company_number", help="numeric company number")
    _add_output_flags(d)
    d.set_defaults(func=cmd_directors)

    # shareholders
    sh = sub.add_parser("shareholders", help="list shareholder allocations")
    sh.add_argument("company_number", help="numeric company number")
    _add_output_flags(sh)
    sh.set_defaults(func=cmd_shareholders)

    # documents
    dc = sub.add_parser("documents", help="list documents / filing history")
    dc.add_argument("company_number", help="numeric company number")
    dc.add_argument("--limit", type=int, default=20, help="documents to return (default: 20)")
    dc.add_argument("--start", type=int, default=0, help="document offset (default: 0)")
    _add_output_flags(dc)
    dc.set_defaults(func=cmd_documents)

    # full
    f = sub.add_parser("full", help="all data bundled (entity + directors + shareholders + documents)")
    f.add_argument("company_number", help="numeric company number")
    f.add_argument("--doc-limit", type=int, default=10, help="documents to include in full output (default: 10)")
    _add_output_flags(f)
    f.set_defaults(func=cmd_full)

    return p


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
