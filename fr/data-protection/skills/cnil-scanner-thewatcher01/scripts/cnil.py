#!/usr/bin/env python3
"""CNIL scanner — check DPO declarations via CNIL open data.

Usage:
    python3 cnil.py --query "424761419" --format json
    python3 cnil.py --query "OVH" --format text
"""

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime

# CNIL DPO declarations dataset on data.gouv.fr
CNIL_BASE = "https://tabular-api.data.gouv.fr/api/resources/0651b990-9d0f-404e-8aee-9f3a7755eedb/data/"


def parse_args():
    p = argparse.ArgumentParser(description="Check CNIL DPO declarations")
    p.add_argument("--query", required=True, help="SIREN number (9 digits) or company name")
    p.add_argument("--department", default=None, help="Filter by department (postal code prefix)")
    p.add_argument("--format", choices=["json", "text"], default="json", help="Output format")
    return p.parse_args()


def is_siren(query):
    """Check if query looks like a SIREN number."""
    clean = query.strip().replace(" ", "")
    return clean.isdigit() and len(clean) == 9


def search_by_siren(siren):
    """Search CNIL DPO dataset by exact SIREN."""
    clean_siren = siren.strip().replace(" ", "")
    params = {"siren__exact": clean_siren}
    url = f"{CNIL_BASE}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "openclaw-cnil/1.0"})

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return {"error": f"CNIL API HTTP {e.code}: {e.reason}"}
    except urllib.error.URLError as e:
        return {"error": f"CNIL API connection error: {e.reason}"}
    except Exception as e:
        return {"error": f"CNIL API error: {str(e)}"}

    return data


def search_by_name(name, department=None):
    """Search CNIL DPO dataset by organism name."""
    params = {"organisme__contains": name, "page_size": 20}
    if department:
        params["code_postal__startswith"] = department

    url = f"{CNIL_BASE}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "openclaw-cnil/1.0"})

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        # Try alternative field names if the API schema differs
        if e.code == 400:
            return search_by_name_fallback(name, department)
        return {"error": f"CNIL API HTTP {e.code}: {e.reason}"}
    except urllib.error.URLError as e:
        return {"error": f"CNIL API connection error: {e.reason}"}
    except Exception as e:
        return {"error": f"CNIL API error: {str(e)}"}

    return data


def search_by_name_fallback(name, department=None):
    """Fallback search trying different field names."""
    # The tabular API field names may vary, try common variants
    for field in ["organisme__contains", "Organisme__contains", "nom_organisme__contains", "denomination__contains"]:
        params = {field: name, "page_size": 20}
        if department:
            for cp_field in ["code_postal__startswith", "Code_postal__startswith", "cp__startswith"]:
                params[cp_field] = department
                url = f"{CNIL_BASE}?{urllib.parse.urlencode(params)}"
                req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "openclaw-cnil/1.0"})
                try:
                    with urllib.request.urlopen(req, timeout=10) as resp:
                        return json.loads(resp.read().decode("utf-8"))
                except Exception:
                    del params[cp_field]
                    continue
        else:
            url = f"{CNIL_BASE}?{urllib.parse.urlencode(params)}"
            req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "openclaw-cnil/1.0"})
            try:
                with urllib.request.urlopen(req, timeout=10) as resp:
                    return json.loads(resp.read().decode("utf-8"))
            except Exception:
                continue

    # Last resort: fetch schema to discover field names
    schema_url = f"{CNIL_BASE}?page_size=1"
    req = urllib.request.Request(schema_url, headers={"Accept": "application/json", "User-Agent": "openclaw-cnil/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            schema_data = json.loads(resp.read().decode("utf-8"))
            sample = schema_data.get("data", [{}])
            if sample:
                available_fields = list(sample[0].keys()) if sample else []
                return {"error": f"Could not find matching field. Available fields: {available_fields}", "data": []}
    except Exception:
        pass

    return {"error": "Could not query CNIL API with any known field name", "data": []}


def parse_results(raw_data, query):
    """Parse CNIL API results into standardized output."""
    if raw_data.get("error"):
        return {
            "query": query,
            "has_dpo": False,
            "prospect_signal": "UNKNOWN",
            "error": raw_data["error"],
            "declarations": [],
        }

    records = raw_data.get("data", [])
    if not records:
        return {
            "query": query,
            "has_dpo": False,
            "prospect_signal": "HOT",
            "note": "No DPO declaration found — potential RGPD compliance gap",
            "declarations": [],
        }

    declarations = []
    for rec in records:
        # Adapt to varying field names
        decl = {
            "organism_name": rec.get("organisme") or rec.get("Organisme") or rec.get("nom_organisme") or "N/A",
            "siren": rec.get("siren") or rec.get("Siren") or rec.get("SIREN") or "",
            "dpo_name": rec.get("dpo") or rec.get("DPO") or rec.get("nom_dpo") or "",
            "declaration_date": rec.get("date_designation") or rec.get("Date_designation") or rec.get("date") or "",
            "postal_code": rec.get("code_postal") or rec.get("Code_postal") or rec.get("cp") or "",
        }
        declarations.append(decl)

    return {
        "query": query,
        "has_dpo": True,
        "prospect_signal": "COLD",
        "declarations": declarations,
    }


def format_text(data):
    """Format results as human-readable text."""
    lines = []
    lines.append(f"Query: {data.get('query', '')}")
    lines.append(f"DPO declared: {'YES' if data.get('has_dpo') else 'NO'}")
    lines.append(f"Prospect signal: {data.get('prospect_signal', 'UNKNOWN')}")

    if data.get("note"):
        lines.append(f"Note: {data['note']}")
    if data.get("error"):
        lines.append(f"Error: {data['error']}")
    lines.append("")

    if data.get("has_dpo"):
        for i, d in enumerate(data.get("declarations", []), 1):
            lines.append(f"--- Declaration {i} ---")
            lines.append(f"  Organism:    {d.get('organism_name', 'N/A')}")
            lines.append(f"  SIREN:       {d.get('siren') or 'N/A'}")
            lines.append(f"  DPO:         {d.get('dpo_name') or 'Not public'}")
            lines.append(f"  Declared on: {d.get('declaration_date') or 'N/A'}")
            lines.append(f"  Postal code: {d.get('postal_code') or 'N/A'}")
            lines.append("")
    else:
        lines.append("=> This entity has NO declared DPO.")
        lines.append("=> If it processes personal data at scale, this is a RGPD compliance gap.")
        lines.append("=> Hot prospect for RGPD consulting / DPO externalization.")
        lines.append("")

    return "\n".join(lines)


def main():
    args = parse_args()

    if is_siren(args.query):
        raw = search_by_siren(args.query)
    else:
        raw = search_by_name(args.query, args.department)

    output = parse_results(raw, args.query)
    output["timestamp"] = datetime.utcnow().isoformat() + "Z"
    output["source"] = "CNIL DPO declarations (data.gouv.fr)"

    if args.format == "text":
        print(format_text(output))
    else:
        print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
