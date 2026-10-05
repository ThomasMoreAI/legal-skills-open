#!/usr/bin/env python3
"""Run IS 5568 accessibility audit on Israeli websites.

Checks for Israeli-specific accessibility requirements based on the
IS 5568 standard, which is anchored to WCAG 2.0 AA (IS 5568 adds some
2.1-aligned criteria; sources differ). Covers Hebrew language
declaration, RTL direction, ARIA labels, and the mandatory
accessibility statement page.

Usage:
    python audit_a11y.py --url https://example.co.il
    python audit_a11y.py --url https://example.co.il --output report.json
    python audit_a11y.py --help

Requirements:
    pip install requests beautifulsoup4
"""

import argparse
import json
import sys
from urllib.parse import urljoin

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Missing required dependencies. Install with:", file=sys.stderr)
    print("  pip install requests beautifulsoup4", file=sys.stderr)
    sys.exit(1)


def check_lang_attribute(soup):
    """Check for Hebrew language declaration on html element."""
    html_tag = soup.find("html")
    if not html_tag:
        return {"pass": False, "message": "No <html> element found"}

    lang = html_tag.get("lang", "")
    if lang.startswith("he"):
        return {"pass": True, "message": f"lang=\"{lang}\" found"}
    elif lang:
        return {
            "pass": False,
            "message": f"lang=\"{lang}\" found but expected \"he\"",
        }
    return {"pass": False, "message": "No lang attribute on <html>"}


def check_dir_attribute(soup):
    """Check for RTL direction declaration."""
    html_tag = soup.find("html")
    if not html_tag:
        return {"pass": False, "message": "No <html> element found"}

    dir_attr = html_tag.get("dir", "")
    if dir_attr == "rtl":
        return {"pass": True, "message": "dir=\"rtl\" found"}
    elif dir_attr:
        return {
            "pass": False,
            "message": f"dir=\"{dir_attr}\" found but expected \"rtl\"",
        }
    return {"pass": False, "message": "No dir attribute on <html>"}


def check_page_title(soup):
    """Check for Hebrew page title."""
    title = soup.find("title")
    if not title or not title.string:
        return {"pass": False, "message": "No <title> element found"}
    title_text = title.string.strip()
    if len(title_text) > 0:
        return {"pass": True, "message": f"Title: \"{title_text[:50]}\""}
    return {"pass": False, "message": "Empty <title> element"}


def check_skip_navigation(soup):
    """Check for skip navigation link."""
    skip_links = soup.find_all("a", href=True)
    for link in skip_links:
        href = link.get("href", "")
        text = link.get_text(strip=True)
        if href.startswith("#") and ("דלג" in text or "skip" in text.lower()):
            return {"pass": True, "message": f"Skip link found: \"{text}\""}
    return {
        "pass": False,
        "message": "No skip navigation link found (expected Hebrew text with 'דלג')",
    }


def check_images_alt(soup):
    """Check that all images have alt attributes."""
    images = soup.find_all("img")
    if not images:
        return {"pass": True, "message": "No images found"}

    missing = []
    for i, img in enumerate(images):
        if not img.has_attr("alt"):
            src = img.get("src", f"image_{i}")
            missing.append(src[:50])

    if missing:
        return {
            "pass": False,
            "message": f"{len(missing)} images missing alt: {', '.join(missing[:3])}",
        }
    return {"pass": True, "message": f"All {len(images)} images have alt text"}


def check_form_labels(soup):
    """Check that form inputs have associated labels."""
    inputs = soup.find_all(["input", "select", "textarea"])
    unlabeled = []
    for inp in inputs:
        if inp.get("type") in ("hidden", "submit", "button", "reset"):
            continue
        inp_id = inp.get("id", "")
        has_label = bool(inp_id and soup.find("label", attrs={"for": inp_id}))
        has_aria = bool(inp.get("aria-label") or inp.get("aria-labelledby"))
        if not has_label and not has_aria:
            unlabeled.append(inp.get("name", inp.get("id", "unknown")))

    if unlabeled:
        return {
            "pass": False,
            "message": f"{len(unlabeled)} inputs without labels: {', '.join(unlabeled[:3])}",
        }
    return {"pass": True, "message": "All form inputs have labels"}


def check_accessibility_statement(soup, base_url):
    """Check for link to accessibility statement page."""
    links = soup.find_all("a", href=True)
    a11y_keywords = ["נגישות", "accessibility", "negishot"]

    for link in links:
        text = link.get_text(strip=True).lower()
        href = link.get("href", "").lower()
        if any(kw in text or kw in href for kw in a11y_keywords):
            full_url = urljoin(base_url, link.get("href", ""))
            return {
                "pass": True,
                "message": f"Accessibility link found: \"{link.get_text(strip=True)}\" -> {full_url}",
            }

    return {
        "pass": False,
        "message": "No link to accessibility statement (הצהרת נגישות) found",
    }


def check_heading_hierarchy(soup):
    """Check that heading hierarchy is logical."""
    headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
    if not headings:
        return {"pass": False, "message": "No headings found"}

    h1_count = len(soup.find_all("h1"))
    if h1_count == 0:
        return {"pass": False, "message": "No H1 heading found"}
    if h1_count > 1:
        return {
            "pass": False,
            "message": f"Multiple H1 headings found ({h1_count})",
        }

    return {
        "pass": True,
        "message": f"Heading hierarchy OK ({len(headings)} headings, 1 H1)",
    }


def run_audit(url):
    """Run full IS 5568 accessibility audit on a URL."""
    print(f"Auditing: {url}\n")

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}", file=sys.stderr)
        sys.exit(1)

    soup = BeautifulSoup(response.text, "html.parser")

    checks = {
        "lang_attribute": check_lang_attribute(soup),
        "dir_attribute": check_dir_attribute(soup),
        "page_title": check_page_title(soup),
        "skip_navigation": check_skip_navigation(soup),
        "images_alt": check_images_alt(soup),
        "form_labels": check_form_labels(soup),
        "accessibility_statement": check_accessibility_statement(soup, url),
        "heading_hierarchy": check_heading_hierarchy(soup),
    }

    passed = sum(1 for c in checks.values() if c["pass"])
    total = len(checks)

    print("IS 5568 Accessibility Audit Results")
    print("=" * 50)
    for name, result in checks.items():
        status = "PASS" if result["pass"] else "FAIL"
        print(f"  [{status}] {name}: {result['message']}")

    print(f"\nScore: {passed}/{total} checks passed")
    if passed < total:
        print("Status: NON-COMPLIANT - remediation required")
    else:
        print("Status: AUTOMATED CHECKS PASSED (manual testing still required)")

    return {"url": url, "checks": checks, "passed": passed, "total": total}


def main():
    parser = argparse.ArgumentParser(
        description="Run IS 5568 accessibility audit on Israeli websites"
    )
    parser.add_argument(
        "--url", required=True,
        help="URL to audit"
    )
    parser.add_argument(
        "--output", default=None,
        help="Output JSON report file path (optional)"
    )
    args = parser.parse_args()

    results = run_audit(args.url)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"\nReport saved: {args.output}")


if __name__ == "__main__":
    main()
