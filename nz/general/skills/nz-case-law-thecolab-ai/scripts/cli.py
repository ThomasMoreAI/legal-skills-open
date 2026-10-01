#!/usr/bin/env python3
"""Search official public New Zealand judgment listings."""

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "lib"))

import nzfetch  # noqa: E402
from court_judgments import (  # noqa: E402
    judge_match_evidence,
    parse_case_page,
    parse_judgments,
    parse_search_results,
    text_matches_query,
)
from result_contract import result_envelope, utc_now  # noqa: E402

ALLOWED = {"courtsofnz.govt.nz", "www.courtsofnz.govt.nz"}
SEARCH_URL = "https://www.courtsofnz.govt.nz/search/SearchForm"
PAGES = {
    "NZSC": "https://www.courtsofnz.govt.nz/the-courts/supreme-court/judgments-supreme",
    "NZCA": "https://www.courtsofnz.govt.nz/judgments/court-of-appeal",
    "NZHC": "https://www.courtsofnz.govt.nz/judgments/high-court",
    "OTHER": "https://www.courtsofnz.govt.nz/judgments/other-courts",
}
WARNINGS = [
    "Retrieval only; this is not legal advice and results are not exhaustive.",
    "Comply with suppression, publication and re-publication restrictions shown by the source.",
    "Coverage varies by court and page; High Court and Court of Appeal public-interest pages generally cover only recent judgments.",
]


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    commands = root.add_subparsers(dest="command", required=True)
    for name, positional in (("search", "query"), ("citation", "citation"), ("judge", "name"), ("judgment", "id")):
        child = commands.add_parser(name)
        child.add_argument(positional)
        child.add_argument("--limit", type=int, default=50)
        child.add_argument("--json", action="store_true")
    court = commands.add_parser("court")
    court.add_argument("code")
    court.add_argument("--limit", type=int, default=50)
    court.add_argument("--json", action="store_true")
    recent = commands.add_parser("recent")
    recent.add_argument("--court", dest="code", required=True)
    recent.add_argument("--limit", type=int, default=50)
    recent.add_argument("--json", action="store_true")
    return root


def main() -> int:
    args = parser().parse_args()
    stamp = utc_now()
    if not 1 <= args.limit <= 100:
        print(json.dumps({"error": "invalid_input", "message": "--limit must be between 1 and 100"}), file=sys.stderr)
        return 2
    codes = [args.code.upper()] if args.command in {"court", "recent"} else list(PAGES)
    if any(code not in PAGES for code in codes):
        print(json.dumps({"error": "invalid_input", "message": "unsupported court code; use NZSC, NZCA, NZHC or OTHER"}), file=sys.stderr)
        return 2

    rows = []
    urls = []
    failures = []
    schema_failures = []
    upstream_failures = []
    blocked_failure = None
    search_commands = {"search", "citation", "judge", "judgment"}
    if args.command in search_commands:
        query = getattr(args, "query", None) or getattr(args, "citation", None) or getattr(args, "name", None) or getattr(args, "id", None)
        url = SEARCH_URL + "?" + urlencode({"Search": query, "start": 0})
        try:
            document = nzfetch.fetch_text(url, timeout=30, allowed_hosts=ALLOWED)
            rows = parse_search_results(document, url, stamp, query)
            urls.append(url)
            if args.command == "citation":
                rows = [row for row in rows if args.citation.casefold() == row["citation"].casefold()]
            elif args.command == "judgment":
                rows = [
                    row for row in rows
                    if text_matches_query(
                        f"{row['citation']} {row['case_name']} {row['case_page_url']}",
                        args.id,
                    )
                ]
            enriched = []
            candidate_cap = min(max(args.limit * 3, 20), 50)
            for row in rows[:candidate_cap]:
                try:
                    detail_document = nzfetch.fetch_text(row["case_page_url"], timeout=20, allowed_hosts=ALLOWED)
                    detail = parse_case_page(detail_document, row["case_page_url"], stamp)
                    detail.update({key: row[key] for key in ("search_source_url", "search_query", "search_match_basis", "search_excerpt")})
                    enriched.append(detail)
                except (nzfetch.FetchError, ValueError) as exc:
                    failures.append(f"{row['citation']}: detail unavailable: {exc}")
                    enriched.append(row)
            rows = enriched
            if args.command == "search":
                rows = [
                    row for row in rows
                    if text_matches_query(
                        f"{row.get('case_name') or ''} {row.get('citation') or ''} {row.get('summary') or ''} {row.get('search_excerpt') or ''}",
                        args.query,
                    )
                ]
            elif args.command == "judge":
                matched = []
                for row in rows:
                    evidence = judge_match_evidence(
                        f"{row.get('summary') or ''} {row.get('search_excerpt') or ''}",
                        args.name,
                    )
                    if not evidence:
                        continue
                    row["judge_query"] = args.name
                    row["judge_match_evidence"] = evidence
                    row["judge_attribution_status"] = "published judge-context match; verify the linked judgment for the complete panel"
                    matched.append(row)
                rows = matched
        except nzfetch.RateLimited as exc:
            blocked_failure = ("rate_limited", str(exc), exc.retry_after)
            failures.append("official site search: rate limited")
        except nzfetch.Blocked as exc:
            blocked_failure = ("blocked", str(exc), None)
            failures.append("official site search: blocked")
        except nzfetch.FetchError as exc:
            failures.append(f"official site search: {exc}")
            upstream_failures.append(f"official site search: {exc}")
        except ValueError as exc:
            failures.append(f"official site search: {exc}")
            schema_failures.append(f"official site search: {exc}")

    for code in ([] if args.command in search_commands else codes):
        url = PAGES[code]
        try:
            document = nzfetch.fetch_text(url, timeout=30, allowed_hosts=ALLOWED)
            rows.extend(parse_judgments(document, url, stamp, code, allow_empty=args.command in {"search", "citation", "judge", "judgment"}))
            urls.append(url)
        except nzfetch.RateLimited as exc:
            blocked_failure = ("rate_limited", str(exc), exc.retry_after)
            failures.append(f"{code}: rate limited")
        except nzfetch.Blocked as exc:
            blocked_failure = ("blocked", str(exc), None)
            failures.append(f"{code}: blocked")
        except nzfetch.FetchError as exc:
            failures.append(f"{code}: {exc}")
            upstream_failures.append(f"{code}: {exc}")
        except ValueError as exc:
            failures.append(f"{code}: {exc}")
            schema_failures.append(f"{code}: {exc}")

    if not urls:
        if blocked_failure:
            kind, message, retry_after = blocked_failure
            print(json.dumps({"error": kind, "message": message, "retry_after": retry_after}), file=sys.stderr)
            return 4
        kind = "source_schema_failure" if schema_failures and not upstream_failures else "source_unavailable"
        print(json.dumps({"error": kind, "message": "; ".join(failures)}), file=sys.stderr)
        return 6 if kind == "source_schema_failure" else 5

    source_url = urls[0] if len(urls) == 1 else "https://www.courtsofnz.govt.nz/judgments"
    warnings = list(WARNINGS)
    if failures:
        warnings.append("Some court sources failed independently: " + "; ".join(failures))
    if args.command == "judge":
        warnings.append("The source does not publish a structured judge field; results require judge-context evidence such as 'Cooke J' or 'Justice Cooke' in published case text and still require verification in the linked judgment.")
    envelope = result_envelope(
        ok=True,
        source_name="Courts of New Zealand",
        source_url=source_url,
        retrieved_at=stamp,
        freshness="court-specific published-judgment listings",
        query=vars(args),
        data=rows[: args.limit],
        warnings=warnings,
        blocked=False,
    )
    print(json.dumps(envelope if args.json else rows[: args.limit], indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
