#!/usr/bin/env python3
"""
Fetch the free-but-checkbox-gated Unternehmensregister publication document(s) for a company
and return the raw report text, the piece the Bundesanzeiger HTTP path can't reach (GJ 2022+,
post-DiRUG). The figures themselves are extracted downstream by the Node `claude` extractor.

Why a browser: the published Jahresabschluss sits behind a free "Ich bin ein Mensch" checkbox
(Friendly-Captcha style, no payment/login). The encrypted payload is session-bound, so a direct
URL doesn't work, we drive one stealth-browser session: search -> click the year -> solve the
checkbox -> read the rendered text. Multiple years are done in the SAME session for efficiency.

Usage:
  ur_fetch_document.py --company "Pergolux" --years 2024,2023,2022 [--index 0] [--timeout 45000]
Output (stdout): JSON { "results": [ {year, ok, chars, text}, ... ] }   (progress on stderr)
"""

import sys, os, json, argparse

# Directory that exposes a stealth-browser module (`from cloakbrowser import launch`).
# Override with COMPANY_REGISTERS_BROWSER; defaults to the cloakbrowser skill location.
BROWSER_SCRIPTS = os.environ.get(
    "COMPANY_REGISTERS_BROWSER",
    os.path.expanduser("~/.claude/skills/browser/scripts"))
sys.path.insert(0, BROWSER_SCRIPTS)


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def solve_checkbox(page, attempts=4):
    """Click the 'Ich bin ein Mensch' checkbox until the security gate clears."""
    for i in range(attempts):
        body = page.inner_text("body")
        if "Ich bin ein Mensch" not in body and "Sicherheitsabfrage" not in body:
            return True
        for sel in ["label:has-text('Ich bin ein Mensch')", "text=Ich bin ein Mensch",
                    "input[type=checkbox]", ".fc-button", "[class*=captcha] label"]:
            try:
                page.locator(sel).first.click(timeout=4000)
                break
            except Exception:
                continue
        page.wait_for_timeout(5000)  # Friendly-Captcha proof-of-work + reveal
    body = page.inner_text("body")
    return "Ich bin ein Mensch" not in body


def extract_text(page):
    """Return the report text (sliced from the first Jahresabschluss marker to cut nav chrome)."""
    body = page.inner_text("body")
    markers = ["Jahresabschluss", "Lagebericht", "Bilanz", "Aktiva"]
    idx = min([body.find(m) for m in markers if body.find(m) != -1] or [0])
    text = body[idx:] if idx > 0 else body
    ok = any(k in body for k in ["Bilanz", "Aktiva", "Passiva", "Umsatz", "Eigenkapital",
                                 "Anlagevermögen", "Umlaufvermögen", "Jahresüberschuss"])
    return ok, text


def run(company, years, index=0, timeout=45000):
    from cloakbrowser import launch
    browser = launch(headless=True)
    page = browser.new_page()
    page.set_default_timeout(timeout)
    results = []
    try:
        search_url = "https://www.unternehmensregister.de/de/suche?areas=all"
        page.goto(search_url, wait_until="domcontentloaded")
        page.wait_for_timeout(2500)
        for label in ["Nur technisch notwendige Cookies akzeptieren", "Allen zustimmen"]:
            try:
                page.get_by_text(label, exact=False).first.click(timeout=2000)
                page.wait_for_timeout(600)
                break
            except Exception:
                pass
        el = page.query_selector("input[name*='company' i]") or page.query_selector("input[type='text']")
        el.click(); el.fill(company)
        page.keyboard.press("Enter")
        page.wait_for_timeout(6000)
        results_url = page.url  # search-results URL with the live token, reused per year

        for year in years:
            log(f"[{company}] GJ {year}: opening publication…")
            try:
                page.goto(results_url, wait_until="domcontentloaded")
                page.wait_for_timeout(3500)
                page.get_by_text(f"Geschäftsjahr vom 01.01.{year}", exact=False).first.click(timeout=10000)
                page.wait_for_timeout(4000)
                solved = solve_checkbox(page)
                page.wait_for_timeout(1500)
                ok, text = extract_text(page)
                log(f"[{company}] GJ {year}: solved={solved} ok={ok} chars={len(text)}")
                results.append({"year": year, "ok": ok, "chars": len(text),
                                "text": text if ok else text[:1500]})
            except Exception as e:
                log(f"[{company}] GJ {year}: ERROR {str(e)[:120]}")
                results.append({"year": year, "ok": False, "error": str(e)[:200], "text": ""})
    finally:
        browser.close()
    return {"company": company, "results": results}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--company", required=True)
    ap.add_argument("--years", required=True, help="comma-separated, e.g. 2024,2023,2022")
    ap.add_argument("--index", type=int, default=0)
    ap.add_argument("--timeout", type=int, default=45000)
    args = ap.parse_args()
    years = [y.strip() for y in args.years.split(",") if y.strip()]
    out = run(args.company, years, args.index, args.timeout)
    print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
