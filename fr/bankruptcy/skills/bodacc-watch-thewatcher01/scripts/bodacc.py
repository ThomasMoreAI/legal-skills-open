#!/usr/bin/env python3
"""BODACC watch — monitor business signals from official announcements.

Usage:
    python3 bodacc.py --query "OVH" --format json
    python3 bodacc.py --department 31 --signal creation --days 7 --format text
"""

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta

BODACC_BASE = "https://bodacc-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/annonces-commerciales/records"

SIGNAL_MAP = {
    "creation": "Immatriculation",
    "modification": "Modification",
    "procedure_collective": "Proc\u00e9dure collective",
    "vente_cession": "Vente",
}


def parse_args():
    p = argparse.ArgumentParser(description="Monitor BODACC business signals")
    p.add_argument("--query", default=None, help="Company name or keywords")
    p.add_argument("--department", default=None, help="Department code (e.g. 31, 75)")
    p.add_argument("--signal", default=None, choices=list(SIGNAL_MAP.keys()), help="Signal type filter")
    p.add_argument("--days", type=int, default=7, help="Look back N days (default: 7)")
    p.add_argument("--per-page", type=int, default=20, help="Results per page (1-100)")
    p.add_argument("--format", choices=["json", "text"], default="json", help="Output format")
    return p.parse_args()


def build_where_clause(query=None, department=None, signal=None, days=7):
    """Build ODS where clause for BODACC API."""
    clauses = []

    # Date range
    since = (datetime.utcnow() - timedelta(days=days)).strftime("%Y-%m-%d")
    clauses.append(f'dateparution >= "{since}"')

    # Text search
    if query:
        escaped = query.replace('"', '\\"')
        clauses.append(f'search(registre, "{escaped}") OR search(commercant, "{escaped}")')

    # Department filter
    if department:
        clauses.append(f'departement_code_postal = "{department}"')

    # Signal type filter
    if signal and signal in SIGNAL_MAP:
        bodacc_type = SIGNAL_MAP[signal]
        escaped_type = bodacc_type.replace('"', '\\"')
        clauses.append(f'fampiilleav_lib = "{escaped_type}"')

    return " AND ".join(f"({c})" for c in clauses)


def classify_signal(record):
    """Classify a BODACC record into a signal type."""
    famille = (record.get("fampiilleav_lib") or "").lower()
    type_annonce = (record.get("typeavis_lib") or "").lower()

    if "immatriculation" in famille or "cr\u00e9ation" in famille:
        return "creation"
    if "proc\u00e9dure collective" in famille or "liquidation" in type_annonce or "redressement" in type_annonce:
        return "procedure_collective"
    if "vente" in famille or "cession" in famille:
        return "vente_cession"
    if "modification" in famille:
        return "modification"
    return "other"


def search_bodacc(query=None, department=None, signal=None, days=7, per_page=20):
    """Query BODACC OpenDataSoft API."""
    where = build_where_clause(query, department, signal, days)
    params = {
        "where": where,
        "limit": min(per_page, 100),
        "order_by": "dateparution DESC",
    }

    url = f"{BODACC_BASE}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "openclaw-bodacc/1.0"})

    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return {"error": f"BODACC API HTTP {e.code}: {e.reason}", "signals": []}
    except urllib.error.URLError as e:
        return {"error": f"BODACC API connection error: {e.reason}", "signals": []}
    except Exception as e:
        return {"error": f"BODACC API error: {str(e)}", "signals": []}

    signals = []
    for rec in data.get("results", []):
        signal_type = classify_signal(rec)
        entity_name = rec.get("commercant") or rec.get("registre") or "N/A"
        dept = rec.get("departement_code_postal") or ""

        # Extract SIREN from registre field if present
        registre = rec.get("registre") or ""
        siren = ""
        for part in registre.replace(",", " ").split():
            clean = part.strip().replace(" ", "")
            if clean.isdigit() and len(clean) == 9:
                siren = clean
                break

        # Build source URL
        annonce_id = rec.get("id_annonce") or rec.get("annonce_id") or ""
        source_url = ""
        if annonce_id:
            source_url = f"https://www.bodacc.fr/pages/annonces-commerciales/?q.id={annonce_id}"

        signals.append({
            "date": rec.get("dateparution", ""),
            "type": signal_type,
            "entity_name": entity_name.strip(),
            "siren": siren,
            "department": dept,
            "description": (rec.get("typeavis_lib") or "") + " - " + (rec.get("fampiilleav_lib") or ""),
            "source_url": source_url,
        })

    return {
        "source": "BODACC (OpenDataSoft/DILA)",
        "total": data.get("total_count", len(signals)),
        "signals": signals,
    }


def format_text(data):
    """Format signals as human-readable text."""
    lines = []
    lines.append(f"Source: {data.get('source', 'unknown')}")
    lines.append(f"Total: {data.get('total', 0)} signal(s)")
    if data.get("error"):
        lines.append(f"Error: {data['error']}")
    lines.append("")

    for i, s in enumerate(data.get("signals", []), 1):
        lines.append(f"--- Signal {i} ---")
        lines.append(f"  Date:        {s.get('date', 'N/A')}")
        lines.append(f"  Type:        {s.get('type', 'N/A')}")
        lines.append(f"  Entity:      {s.get('entity_name', 'N/A')}")
        lines.append(f"  SIREN:       {s.get('siren') or 'N/A'}")
        lines.append(f"  Department:  {s.get('department', 'N/A')}")
        lines.append(f"  Description: {s.get('description', 'N/A')}")
        if s.get("source_url"):
            lines.append(f"  URL:         {s['source_url']}")
        lines.append("")

    return "\n".join(lines)


def main():
    args = parse_args()

    if not args.query and not args.department and not args.signal:
        print(json.dumps({"error": "At least one of --query, --department, or --signal is required"}, indent=2))
        sys.exit(1)

    data = search_bodacc(
        query=args.query,
        department=args.department,
        signal=args.signal,
        days=args.days,
        per_page=args.per_page,
    )

    data["query"] = args.query or ""
    data["department"] = args.department or ""
    data["days"] = args.days
    data["timestamp"] = datetime.utcnow().isoformat() + "Z"

    if args.format == "text":
        print(format_text(data))
    else:
        print(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
