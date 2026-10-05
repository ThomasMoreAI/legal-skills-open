#!/usr/bin/env python3
"""
Polish KRS name-search helper, the only part of the PL path that needs a browser.

The official KRS API has no name search, and the public search portal
(wyszukiwarka-krs.ms.gov.pl) is an Angular SPA behind Incapsula bot-protection. The stealth
cloakbrowser passes the Incapsula challenge and renders the app; we drive the "Nazwa" field via
Playwright's accessibility labels (the DOM ids are randomised each load, so label targeting is
the only stable handle). Returns candidate {krs, name} rows which de-analyze then enriches via
the official API.

Usage:
  pl-browser.py search "Company Name" [--max N]   -> {found, count, results:[{krs,name,...}]}
"""
import sys, os, re, json, argparse

sys.path.insert(0, os.environ.get(
    "COMPANY_REGISTERS_BROWSER",
    os.path.expanduser("~/.claude/skills/browser/scripts")))
try:
    from cloakbrowser import launch
except Exception as e:  # pragma: no cover
    print(json.dumps({"error": f"cloakbrowser not available: {e}. Point COMPANY_REGISTERS_BROWSER "
                               "at a dir exposing a stealth-browser `launch()` (see README)."}))
    sys.exit(2)

PORTAL = "https://wyszukiwarka-krs.ms.gov.pl/"
KRS_RE = re.compile(r"\b(\d{10})\b")


def cmd_search(args):
    b = launch(headless=True)
    try:
        p = b.new_page(); p.set_default_timeout(45000)
        p.goto(PORTAL, wait_until="domcontentloaded")
        p.wait_for_timeout(4500)
        # The portal searches all registers; each result is tagged with its register kind
        # (Przedsiębiorców / Stowarzyszeń), which we map to P/S below.
        # Fill the company-name field (label "Nazwa") and search.
        p.get_by_label("Nazwa", exact=False).first.fill(args.name)
        p.wait_for_timeout(500)
        try:
            p.get_by_role("button", name="Wyszukaj").first.click(timeout=5000)
        except Exception:
            p.keyboard.press("Enter")
        p.wait_for_timeout(5000)

        # Results render as a table: [Numer KRS, Nazwa/Firma, Miejscowość, Rodzaj rejestru, ...].
        # Read rows by cell; a data row's first cell is a 10-digit KRS.
        js = r"""() => {
          const rows = [];
          document.querySelectorAll("table tr").forEach(tr => {
            const tds = [...tr.querySelectorAll('td')].map(td => (td.innerText||'').replace(/\s+/g,' ').trim());
            if (tds.length && /^\d{10}$/.test((tds[0]||'').replace(/\s/g,''))) {
              rows.push(tds);
            }
          });
          return rows;
        }"""
        raw = p.evaluate(js)
        results = []
        seen = set()
        for tds in raw:
            krs = re.sub(r"\s", "", tds[0])
            if krs in seen:
                continue
            seen.add(krs)
            reg = (tds[3] if len(tds) > 3 else "") or ""
            register = "S" if "stowarzysze" in reg.lower() else ("P" if "przedsi" in reg.lower() or "rejestr przed" in reg.lower() else None)
            results.append({
                "krs": krs,
                "name": tds[1] if len(tds) > 1 else None,
                "city": tds[2] if len(tds) > 2 else None,
                "register_kind": reg or None,
                "register": register,
            })
            if len(results) >= args.max:
                break
        print(json.dumps({"found": len(results) > 0, "count": len(results),
                          "searched_name": args.name, "total_on_portal": None,
                          "results": results, "source": "wyszukiwarka-krs.ms.gov.pl"},
                         ensure_ascii=False))
    finally:
        b.close()


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search"); s.add_argument("name"); s.add_argument("--max", type=int, default=15)
    args = ap.parse_args()
    if args.cmd == "search":
        cmd_search(args)


if __name__ == "__main__":
    main()
