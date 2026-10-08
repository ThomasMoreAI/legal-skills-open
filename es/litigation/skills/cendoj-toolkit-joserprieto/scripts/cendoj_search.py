#!/usr/bin/env python3
"""
cendoj_search.py — Free-text search on CENDOJ via Playwright.

Searches https://www.poderjudicial.es/search/indexAN.jsp using the JS-driven
form (plain HTTP POST is unreliable) and extracts the full list of results with
ECLI codes, reference IDs, and metadata. Output is a JSON inventory consumable
by cendoj_download.py.

CENDOJ legal notice (uso particular only) is enforced — see SKILL.md.

Usage:
    python cendoj_search.py --query "Avincis" --output results.json
    python cendoj_search.py --query "Avincis" --output results.json --no-headless
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path

# Ensure the script can import its sibling `cendoj_lib` whether launched
# directly or via `python -m`.
_THIS_DIR = Path(__file__).resolve().parent
if str(_THIS_DIR) not in sys.path:
    sys.path.insert(0, str(_THIS_DIR))

from cendoj_lib import (  # type: ignore[import-not-found]  # noqa: E402
    LEGAL_NOTICE,
    MIN_DELAY_SECONDS,
    SEARCH_URL,
    build_pdf_url,
    parse_open_document_url,
    parse_result_text,
    parse_title,
)


def print_legal_notice() -> None:
    print(LEGAL_NOTICE, file=sys.stderr)


def extract_results_from_page(page) -> list[dict]:
    """Run JS on the current page to extract all visible search results.

    Filters out sidebar items (which lack 'ROJ:' or full date format).
    """
    raw = page.evaluate(
        """() => {
            const allLinks = Array.from(document.querySelectorAll('a[href*="openDocument"]'));
            return allLinks.map(a => {
                const p1 = a.parentElement;
                const p2 = p1?.parentElement;
                const p3 = p2?.parentElement;
                const text = p3?.innerText || p2?.innerText || p1?.innerText || '';
                return { href: a.href, title: a.textContent.trim(), text };
            }).filter(x => x.title && x.title.length > 5);
        }"""
    )

    results: list[dict] = []
    seen_refs: set[str] = set()

    for item in raw:
        href = item["href"]
        title = item["title"]
        text = item["text"]

        # Skip sidebar "most consulted" items — they lack ROJ + dates
        if "ROJ:" not in title and not re.search(r"de\s+\d{4}", title):
            continue

        parsed_url = parse_open_document_url(href)
        if parsed_url is None:
            continue
        reference, optimize = parsed_url

        if reference in seen_refs:
            continue
        seen_refs.add(reference)

        title_data = parse_title(title)
        meta = parse_result_text(text)

        entry = {
            "title": title,
            **title_data,
            **meta,
            "reference": reference,
            "optimize": optimize,
            "open_document_url": href,
            "pdf_url": build_pdf_url(reference, optimize),
        }
        results.append(entry)

    return results


def search_cendoj(query: str, headless: bool = True, page_delay: float = MIN_DELAY_SECONDS) -> list[dict]:
    """Run a free-text search on CENDOJ and return all results across pages."""
    from playwright.sync_api import sync_playwright  # type: ignore[import-not-found]

    print(
        f"[{datetime.now().isoformat(timespec='seconds')}] Starting CENDOJ search: {query!r}",
        file=sys.stderr,
    )

    all_results: list[dict] = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            ),
            locale="es-ES",
        )
        page = context.new_page()

        page.goto(SEARCH_URL, wait_until="domcontentloaded")

        # Close legal notice modal if present
        try:
            page.locator('button:has-text("×")').first.click(timeout=3000)
        except Exception:
            pass

        page.get_by_role("textbox", name="Texto libre").fill(query)
        page.get_by_role("button", name="Buscar").click()
        page.wait_for_timeout(3000)

        # Determine total pages from pagination label "Página X de Y"
        page_count = 1
        try:
            page_info = page.locator("text=/de\\s+\\d+/").first.inner_text(timeout=3000)
            m = re.search(r"de\s+(\d+)", page_info)
            if m:
                page_count = int(m.group(1))
        except Exception:
            pass

        print(f"  Detected {page_count} pages of results", file=sys.stderr)

        for page_num in range(1, page_count + 1):
            print(
                f"  [{datetime.now().isoformat(timespec='seconds')}] "
                f"Extracting page {page_num}/{page_count}",
                file=sys.stderr,
            )
            results = extract_results_from_page(page)
            print(f"    Found {len(results)} results on this page", file=sys.stderr)
            all_results.extend(results)

            if page_num < page_count:
                time.sleep(page_delay)
                clicked = page.evaluate(
                    """() => {
                        const pagLinks = document.querySelectorAll(
                            '#jurisprudenciaresults_bottompagination a, #jurisprudenciaresults_toppagination a'
                        );
                        for (const a of pagLinks) {
                            if (a.title && a.title.includes('siguiente')) { a.click(); return true; }
                        }
                        return false;
                    }"""
                )
                if not clicked:
                    print("    WARNING: could not navigate to next page", file=sys.stderr)
                    break
                page.wait_for_timeout(2500)

        browser.close()

    # Deduplicate by reference across pages (defensive — should already be unique)
    seen: set[str] = set()
    deduped: list[dict] = []
    for r in all_results:
        if r["reference"] not in seen:
            deduped.append(r)
            seen.add(r["reference"])

    print(
        f"[{datetime.now().isoformat(timespec='seconds')}] Total unique results: {len(deduped)}",
        file=sys.stderr,
    )
    return deduped


def main() -> int:
    print_legal_notice()

    parser = argparse.ArgumentParser(
        description="Search CENDOJ by free text and produce a JSON inventory.",
    )
    parser.add_argument("--query", required=True, help="Free text search query")
    parser.add_argument("--output", required=True, help="Output JSON file path")
    parser.add_argument(
        "--headless",
        action="store_true",
        default=True,
        help="Run browser headless (default: True)",
    )
    parser.add_argument(
        "--no-headless",
        dest="headless",
        action="store_false",
        help="Run browser with visible UI (for debugging)",
    )
    parser.add_argument(
        "--page-delay",
        type=float,
        default=MIN_DELAY_SECONDS,
        help=f"Seconds to wait between page navigations (min {MIN_DELAY_SECONDS}, default {MIN_DELAY_SECONDS})",
    )
    args = parser.parse_args()

    if args.page_delay < MIN_DELAY_SECONDS:
        print(
            f"ERROR: --page-delay cannot be less than {MIN_DELAY_SECONDS} seconds "
            f"(CENDOJ robots.txt Crawl-delay).",
            file=sys.stderr,
        )
        return 2

    try:
        results = search_cendoj(
            query=args.query,
            headless=args.headless,
            page_delay=args.page_delay,
        )
    except ImportError as e:
        print(
            "ERROR: missing dependency. Install with: "
            "pip install playwright && playwright install chromium",
            file=sys.stderr,
        )
        print(f"  Detail: {e}", file=sys.stderr)
        return 3
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        f"[{datetime.now().isoformat(timespec='seconds')}] "
        f"Wrote {len(results)} results to {out_path}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
