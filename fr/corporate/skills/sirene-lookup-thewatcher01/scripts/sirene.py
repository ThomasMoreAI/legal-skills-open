#!/usr/bin/env python3
"""SIRENE lookup — search French companies via DINUM + INSEE APIs.

Usage:
    python3 sirene.py --query "OVH Roubaix" --format json
    python3 sirene.py --query "424761419" --department 59 --format text
"""

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime

DINUM_BASE = "https://recherche-entreprises.api.gouv.fr/search"
INSEE_BASE = "https://api.insee.fr/entreprises/sirene/V3.11"


def parse_args():
    p = argparse.ArgumentParser(description="Search SIRENE registry")
    p.add_argument("--query", required=True, help="Company name, SIREN, SIRET, or keywords")
    p.add_argument("--department", default=None, help="Department code (e.g. 31, 75)")
    p.add_argument("--per-page", type=int, default=10, help="Results per page (1-25)")
    p.add_argument("--format", choices=["json", "text"], default="json", help="Output format")
    return p.parse_args()


def search_dinum(query, department=None, per_page=10):
    """Search via Recherche Entreprises DINUM API (no auth)."""
    params = {
        "q": query,
        "page": 1,
        "per_page": min(per_page, 25),
    }
    if department:
        params["departement"] = department

    url = f"{DINUM_BASE}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "openclaw-sirene/1.0"})

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return {"error": f"DINUM API HTTP {e.code}: {e.reason}", "results": []}
    except urllib.error.URLError as e:
        return {"error": f"DINUM API connection error: {e.reason}", "results": []}
    except Exception as e:
        return {"error": f"DINUM API error: {str(e)}", "results": []}

    results = []
    for ent in data.get("results", []):
        # RGPD: skip non-diffusible entities
        if ent.get("statut_diffusion") == "P":
            continue

        siege = ent.get("siege", {})
        result = {
            "siren": ent.get("siren", ""),
            "siret": siege.get("siret", ""),
            "denomination": ent.get("nom_complet", ""),
            "address": _build_address(siege),
            "naf_code": siege.get("activite_principale", ""),
            "naf_label": siege.get("libelle_activite_principale", ent.get("activite_principale", "")),
            "effectif": ent.get("tranche_effectif_salarie", ""),
            "categorie_juridique": ent.get("nature_juridique", ""),
            "date_creation": ent.get("date_creation", ""),
            "etat_administratif": ent.get("etat_administratif", ""),
        }
        results.append(result)

    return {
        "source": "DINUM Recherche Entreprises",
        "total": data.get("total_results", len(results)),
        "results": results,
    }


def _build_address(siege):
    """Build a human-readable address from siege data."""
    parts = []
    for field in ["numero_voie", "type_voie", "libelle_voie"]:
        val = siege.get(field)
        if val:
            parts.append(str(val))
    street = " ".join(parts)

    cp = siege.get("code_postal", "")
    city = siege.get("libelle_commune", "")

    addr_parts = [p for p in [street, f"{cp} {city}".strip()] if p]
    return ", ".join(addr_parts)


def search_insee(query, department=None, per_page=10):
    """Search via INSEE SIRENE V3.11 API (requires INSEE_API_KEY)."""
    api_key = os.environ.get("INSEE_API_KEY", "").strip()
    if not api_key:
        return None

    # Determine if query is a SIREN number
    clean_query = query.strip().replace(" ", "")
    if clean_query.isdigit() and len(clean_query) == 9:
        url = f"{INSEE_BASE}/siren/{clean_query}"
    elif clean_query.isdigit() and len(clean_query) == 14:
        url = f"{INSEE_BASE}/siret/{clean_query}"
    else:
        # Full-text search on legal units
        encoded_q = urllib.parse.quote(query)
        url = f"{INSEE_BASE}/siren?q=denominationUniteLegale:{encoded_q}&nombre={min(per_page, 20)}"

    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}",
            "User-Agent": "openclaw-sirene/1.0",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        if e.code == 401:
            return {"error": "INSEE API: invalid or expired API key", "results": []}
        if e.code == 404:
            return {"source": "INSEE SIRENE V3.11", "total": 0, "results": []}
        return {"error": f"INSEE API HTTP {e.code}: {e.reason}", "results": []}
    except Exception as e:
        return {"error": f"INSEE API error: {str(e)}", "results": []}

    results = []

    # Handle single SIREN/SIRET lookup
    if "uniteLegale" in data:
        ul = data["uniteLegale"]
        # RGPD filter
        if ul.get("statutDiffusionUniteLegale") != "O":
            return {"source": "INSEE SIRENE V3.11", "total": 0, "results": [], "note": "Entity is non-diffusible (RGPD)"}

        periods = ul.get("periodesUniteLegale", [{}])
        current = periods[0] if periods else {}
        results.append({
            "siren": ul.get("siren", ""),
            "siret": "",
            "denomination": current.get("denominationUniteLegale", ""),
            "address": "",
            "naf_code": current.get("activitePrincipaleUniteLegale", ""),
            "naf_label": "",
            "effectif": ul.get("trancheEffectifsUniteLegale", ""),
            "categorie_juridique": current.get("categorieJuridiqueUniteLegale", ""),
            "date_creation": ul.get("dateCreationUniteLegale", ""),
            "etat_administratif": current.get("etatAdministratifUniteLegale", ""),
        })
    elif "unitesLegales" in data:
        for ul in data.get("unitesLegales", []):
            # RGPD filter
            if ul.get("statutDiffusionUniteLegale") != "O":
                continue
            periods = ul.get("periodesUniteLegale", [{}])
            current = periods[0] if periods else {}
            results.append({
                "siren": ul.get("siren", ""),
                "siret": "",
                "denomination": current.get("denominationUniteLegale", ""),
                "address": "",
                "naf_code": current.get("activitePrincipaleUniteLegale", ""),
                "naf_label": "",
                "effectif": ul.get("trancheEffectifsUniteLegale", ""),
                "categorie_juridique": current.get("categorieJuridiqueUniteLegale", ""),
                "date_creation": ul.get("dateCreationUniteLegale", ""),
                "etat_administratif": current.get("etatAdministratifUniteLegale", ""),
            })

    return {
        "source": "INSEE SIRENE V3.11",
        "total": data.get("header", {}).get("total", len(results)),
        "results": results,
    }


def format_text(data):
    """Format results as human-readable text."""
    lines = []
    lines.append(f"Source: {data.get('source', 'unknown')}")
    lines.append(f"Total: {data.get('total', 0)} result(s)")
    if data.get("error"):
        lines.append(f"Error: {data['error']}")
    lines.append("")

    for i, r in enumerate(data.get("results", []), 1):
        lines.append(f"--- Result {i} ---")
        lines.append(f"  SIREN:        {r.get('siren', 'N/A')}")
        lines.append(f"  SIRET:        {r.get('siret', 'N/A')}")
        lines.append(f"  Denomination: {r.get('denomination', 'N/A')}")
        lines.append(f"  Address:      {r.get('address', 'N/A')}")
        lines.append(f"  NAF:          {r.get('naf_code', 'N/A')} — {r.get('naf_label', '')}")
        lines.append(f"  Effectif:     {r.get('effectif', 'N/A')}")
        lines.append(f"  Statut:       {r.get('etat_administratif', 'N/A')}")
        lines.append(f"  Creation:     {r.get('date_creation', 'N/A')}")
        lines.append("")

    return "\n".join(lines)


def main():
    args = parse_args()

    # Primary: DINUM API (always available)
    dinum_data = search_dinum(args.query, args.department, args.per_page)

    # Secondary: INSEE API (if key is available)
    insee_data = search_insee(args.query, args.department, args.per_page)

    # Merge results: prefer DINUM as primary, add INSEE if it returned unique SIRENs
    output = dinum_data.copy()
    if insee_data and not insee_data.get("error"):
        existing_sirens = {r["siren"] for r in output.get("results", [])}
        for r in insee_data.get("results", []):
            if r["siren"] not in existing_sirens:
                output["results"].append(r)
                existing_sirens.add(r["siren"])
        if insee_data.get("results"):
            output["source"] = f"{dinum_data.get('source', 'DINUM')} + INSEE SIRENE V3.11"

    output["query"] = args.query
    output["timestamp"] = datetime.utcnow().isoformat() + "Z"

    if args.format == "text":
        print(format_text(output))
    else:
        print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
