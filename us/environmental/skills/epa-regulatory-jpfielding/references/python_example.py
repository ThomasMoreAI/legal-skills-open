#!/usr/bin/env python3
"""epa_ghg_client.py — Minimal EPA GHGRP Envirofacts client (stdlib only).

Usage:
    python python_example.py

No API key required. All data is public.

Queries the EPA Greenhouse Gas Reporting Program via the Envirofacts REST API.
Primary table: V_GHG_EMITTER_SUBPART (facility emissions by subpart, gas, year).
"""

from __future__ import annotations

import json
import sys
import urllib.request
import urllib.error
from dataclasses import dataclass, field
from typing import Any


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

BASE_URL = "https://data.epa.gov/efservice"

# Key GHGRP subparts for petroleum engineering
PNGE_SUBPARTS = {
    "W":  "Petroleum and Natural Gas Systems",
    "C":  "Stationary Combustion",
    "Y":  "Petroleum Refining",
    "UU": "Injection of CO2",
    "PP": "Suppliers of CO2",
    "MM": "Suppliers of Petroleum Products",
    "RR": "Geologic Sequestration of CO2",
}


# ---------------------------------------------------------------------------
# Query builder
# ---------------------------------------------------------------------------

@dataclass
class GHGQuery:
    """Parameters for an EPA GHGRP Envirofacts query.

    Attributes:
        table:          Envirofacts view name.
        filters:        Ordered list of (column, value) or (column, operator, value).
        row_start:      First row index (0-based, inclusive).
        row_end:        Last row index (inclusive). None = no limit.
        output_format:  JSON, CSV, or XML.
    """
    table: str = "V_GHG_EMITTER_SUBPART"
    filters: list[tuple[str, ...]] = field(default_factory=list)
    row_start: int = 0
    row_end: int | None = 99
    output_format: str = "JSON"

    def add_filter(self, column: str, value: str, operator: str = "") -> "GHGQuery":
        """Add a filter. Operator is optional (CONTAINING, BEGINNING, >, <, !=)."""
        if operator:
            self.filters.append((column, operator, value))
        else:
            self.filters.append((column, value))
        return self

    def build_url(self) -> str:
        """Construct the full Envirofacts REST URL."""
        parts = [BASE_URL, self.table]
        for f in self.filters:
            parts.extend(f)
        if self.row_end is not None:
            parts.append(f"rows/{self.row_start}:{self.row_end}")
        parts.append(self.output_format)
        return "/".join(parts)


# ---------------------------------------------------------------------------
# Client
# ---------------------------------------------------------------------------

class GHGClient:
    """Thin wrapper for EPA GHGRP Envirofacts queries."""

    def __init__(self, timeout: int = 30) -> None:
        self.timeout = timeout

    def fetch(self, query: GHGQuery) -> list[dict[str, Any]]:
        """Execute a query and return parsed JSON rows."""
        url = query.build_url()
        req = urllib.request.Request(url)
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                body = resp.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            raise RuntimeError(f"HTTP {e.code}: {e.reason} for {url}") from e
        except urllib.error.URLError as e:
            raise RuntimeError(f"URL error: {e.reason} for {url}") from e

        data = json.loads(body)
        if isinstance(data, dict) and "error" in data:
            raise RuntimeError(f"API error: {data['error']}")
        return data

    def count(self, query: GHGQuery) -> int:
        """Return total record count for a query (without fetching all rows)."""
        count_q = GHGQuery(
            table=query.table,
            filters=list(query.filters),
            row_start=0,
            row_end=None,
            output_format="JSON",
        )
        # Replace output with count
        url = "/".join([
            BASE_URL,
            count_q.table,
            *[seg for f in count_q.filters for seg in f],
            "count",
            "JSON",
        ])
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=self.timeout) as resp:
            body = resp.read().decode("utf-8")
        data = json.loads(body)
        if isinstance(data, list) and len(data) > 0:
            return data[0].get("TOTALQUERYRESULTS", 0)
        return 0

    def fetch_all(self, query: GHGQuery, page_size: int = 1000) -> list[dict[str, Any]]:
        """Paginate through all results."""
        total = self.count(query)
        if total == 0:
            return []

        all_rows: list[dict[str, Any]] = []
        offset = 0
        while offset < total:
            page_q = GHGQuery(
                table=query.table,
                filters=list(query.filters),
                row_start=offset,
                row_end=offset + page_size - 1,
                output_format=query.output_format,
            )
            rows = self.fetch(page_q)
            all_rows.extend(rows)
            offset += page_size
        return all_rows


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------

def print_table(rows: list[dict], cols: list[str], max_rows: int = 20) -> None:
    """Print a fixed-width table from a list of row dicts."""
    if not rows:
        print("(no data)")
        return
    display = rows[:max_rows]
    widths = {
        c: max(len(c), *(len(str(r.get(c, ""))) for r in display))
        for c in cols
    }
    header = "  ".join(c.ljust(widths[c]) for c in cols)
    print(header)
    print("-" * len(header))
    for row in display:
        print("  ".join(str(row.get(c, "")).ljust(widths[c]) for c in cols))
    if len(rows) > max_rows:
        print(f"... ({len(rows) - max_rows} more rows)")


def aggregate_co2e(rows: list[dict], group_col: str) -> dict[str, float]:
    """Sum co2e_emission by a grouping column."""
    totals: dict[str, float] = {}
    for row in rows:
        key = str(row.get(group_col, "unknown"))
        totals[key] = totals.get(key, 0.0) + float(row.get("co2e_emission", 0))
    return dict(sorted(totals.items(), key=lambda x: x[1], reverse=True))


# ---------------------------------------------------------------------------
# Example usage
# ---------------------------------------------------------------------------

def main() -> None:
    client = GHGClient()

    # --- Example 1: Subpart W (Petroleum & NG) emissions in WV, 2022 ---
    print("=== Subpart W Emissions in West Virginia (2022) ===\n")

    q = GHGQuery()
    q.add_filter("SUBPART_NAME", "W")
    q.add_filter("STATE", "WV")
    q.add_filter("YEAR", "2022")
    q.row_end = None  # Get all rows

    rows = client.fetch(q)
    total_count = len(rows)
    print(f"Records returned: {total_count}\n")

    # Aggregate by facility
    facility_totals = aggregate_co2e(rows, "facility_name")
    print(f"Unique facilities: {len(facility_totals)}\n")
    print(f"{'Facility':<70s}  {'CO2e (MT)':>12s}")
    print("-" * 84)
    for name, total in list(facility_totals.items())[:10]:
        print(f"{name[:70]:<70s}  {total:>12,.1f}")

    # Aggregate by gas
    print("\nBreakdown by gas:")
    gas_totals = aggregate_co2e(rows, "gas_name")
    for gas, total in gas_totals.items():
        print(f"  {gas:<25s}  {total:>12,.1f} MT CO2e")

    print()

    # --- Example 2: Search for a specific operator ---
    print("=== EQT Production Facilities (2022, Subpart W) ===\n")

    q2 = GHGQuery()
    q2.add_filter("FACILITY_NAME", "EQT", "CONTAINING")
    q2.add_filter("SUBPART_NAME", "W")
    q2.add_filter("YEAR", "2022")
    q2.row_end = None

    rows2 = client.fetch(q2)
    print(f"Records: {len(rows2)}\n")
    print_table(rows2, ["facility_name", "state", "gas_name", "co2e_emission"])

    print()

    # --- Example 3: Count Subpart W records nationally ---
    print("=== National Subpart W Record Count (2022) ===\n")

    q3 = GHGQuery()
    q3.add_filter("SUBPART_NAME", "W")
    q3.add_filter("YEAR", "2022")

    total = client.count(q3)
    print(f"Total Subpart W records for 2022: {total:,}")
    print("(Each record = one facility x gas x year combination)")


if __name__ == "__main__":
    main()
