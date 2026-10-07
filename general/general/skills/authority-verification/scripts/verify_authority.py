#!/usr/bin/env python3
"""Minimal case.dev authority-verification example.

Verifies a citation, retrieves source text for verified matches,
and optionally expands to related authorities.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any


def serialize_summary(summary: Any) -> dict[str, Any]:
    return {
        "total": getattr(summary, "total", None),
        "verified": getattr(summary, "verified", None),
        "not_found": getattr(summary, "not_found", None),
        "multiple_matches": getattr(summary, "multiple_matches", None),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Verify a legal citation with case.dev.")
    parser.add_argument("--citation", required=True, help="Citation text to verify, e.g. '531 U.S. 98'")
    parser.add_argument(
        "--highlight-query",
        default="holding",
        help="Highlight query for full-text retrieval when verification succeeds.",
    )
    parser.add_argument(
        "--related-count",
        type=int,
        default=5,
        help="Number of related authorities to request with legal.similar().",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    api_key = os.environ.get("CASEDEV_API_KEY")
    if not api_key:
        print("CASEDEV_API_KEY is required", file=sys.stderr)
        return 1

    try:
        import casedev
    except ImportError:
        print("Missing dependency: install with 'python3 -m pip install casedev'", file=sys.stderr)
        return 1

    client = casedev.Casedev(api_key=api_key)

    try:
        verification = client.legal.v1.verify(text=args.citation)
    except Exception as exc:
        print(f"case.dev verification failed: {exc}", file=sys.stderr)
        return 1

    report: dict[str, Any] = {
        "citation": args.citation,
        "summary": serialize_summary(getattr(verification, "summary", None)),
        "results": [],
    }

    for item in verification.citations:
        result: dict[str, Any] = {
            "original": item.original,
            "status": item.status,
        }

        if item.status == "verified":
            case = item.case
            result["case"] = {
                "name": case.name,
                "url": case.url,
            }

            try:
                full_text = client.legal.v1.get_full_text(
                    url=case.url,
                    highlight_query=args.highlight_query,
                    max_characters=12000,
                )
                similar = client.legal.v1.similar(
                    url=case.url,
                    num_results=args.related_count,
                )
            except Exception as exc:
                print(f"case.dev follow-on retrieval failed: {exc}", file=sys.stderr)
                return 1

            result["highlights"] = list(getattr(full_text, "highlights", []))
            result["related_authorities"] = [
                {"title": source.title, "url": source.url}
                for source in getattr(similar, "similar_sources", [])
            ]

        elif item.status == "multiple_matches":
            result["candidates"] = [
                {"name": candidate.name, "url": candidate.url}
                for candidate in getattr(item, "candidates", [])
            ]

        report["results"].append(result)

    print(json.dumps(report, indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
