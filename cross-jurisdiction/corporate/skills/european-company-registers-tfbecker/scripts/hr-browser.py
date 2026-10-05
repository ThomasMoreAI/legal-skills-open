#!/usr/bin/env python3
"""
handelsregister.de browser helper (the ONLY part of the German Handelsregister path that
needs a real browser). Driven by de-handelsregister.js, it owns the JSON contract and the
AD-document parsing; this file only does the stateful PrimeFaces/JSF flow that is brittle to
hand-roll in pure HTTP.

Why a browser: handelsregister.de is a JSF/PrimeFaces app (ViewState + partial-AJAX). No
bot-protection, but the search + document retrieval need real session/AJAX state. Since the
DiRUG reform (1 Aug 2022) the AD (Aktueller Abdruck / current extract) is free.

Uses the shared stealth cloakbrowser (same engine as the `browser` skill). A reuse daemon
keeps per-call startup near ~0.3 s.

Subcommands (all print JSON to stdout):
  search "<name>" [--max N]
      -> { found, count, results:[ {name, register_type, register_number, court, state,
           seat, status, former_names:[...] } ] }
  ad "<name>" --out <file.pdf> [--hrb <number>] [--court <name>]
      -> { downloaded, out, matched:{...} }   (picks the row by HRB if given, else best name)
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

SEARCH_URL = "https://www.handelsregister.de/rp_web/normalesuche/welcome.xhtml"

# cell[1] of a result row, e.g. "North Rhine-Westphalia District court Köln HRB 37497"
REGLINE_RE = re.compile(
    r"^(?P<state>.+?)\s+District court\s+(?P<court>.+?)\s+"
    r"(?P<rtype>HRA|HRB|GnR|PR|VR|GsR)\s+(?P<rnum>\d+\s*[A-Z]{0,3})\s*$",
    re.IGNORECASE,
)


def _rows_js():
    # Read the PrimeFaces datatable's data rows (tr[data-ri]) by CELL, so the column
    # boundaries survive (flattened innerText merges register-number and company name).
    #   td[1]=register line, td[2]=name, td[3]=seat, td[4]=status, td[5]=doc actions,
    #   td[8],td[10],... = former names (history), td[9],td[11],... = former seats.
    return r"""() => {
      const out = [];
      document.querySelectorAll("tr[data-ri]").forEach(tr => {
        const tds = [...tr.querySelectorAll('td')].map(td => (td.innerText||'').replace(/\s+/g,' ').trim());
        const ad = tr.querySelector("a[id$=':0:fade_']");
        const si = tr.querySelector("a[id$=':6:fade_']");
        const former = [];
        for (let i = 8; i < tds.length; i += 2) {
          const m = (tds[i]||'').match(/^\d+\.\)\s*(.+)/);
          if (m) former.push(m[1]);
        }
        out.push({ regline: tds[1]||'', name: tds[2]||'', seat: tds[3]||'',
                   status: tds[4]||'', former, ad: ad?ad.id:null, si: si?si.id:null });
      });
      return out;
    }"""


def _parse_row(r):
    m = REGLINE_RE.match(r.get("regline", ""))
    if not m or not r.get("name"):
        return None
    rnum = re.sub(r"\s+", "", m.group("rnum"))
    st = (r.get("status") or "").lower()
    return {
        "name": r["name"],
        "seat": r.get("seat") or None,
        "state": m.group("state").strip() or None,
        "court": m.group("court").strip() or None,
        "register_type": m.group("rtype").upper(),
        "register_number": rnum,
        "register": f"{m.group('rtype').upper()} {rnum}",
        "status": "active" if st.startswith("currently") else (r.get("status") or None),
        "former_names": r.get("former") or [],
        "_ad": r.get("ad"), "_si": r.get("si"),
    }


def _do_search(page, name):
    page.goto(SEARCH_URL, wait_until="domcontentloaded")
    page.wait_for_timeout(1500)
    ta = page.query_selector("#form\\:schlagwoerter") or page.query_selector("textarea[id$='schlagwoerter']")
    if not ta:
        return []
    ta.fill(name)
    page.click("#form\\:btnSuche")
    page.wait_for_timeout(5000)
    return [p for p in (_parse_row(r) for r in page.evaluate(_rows_js())) if p]


def cmd_search(args):
    b = launch(headless=True)
    try:
        p = b.new_page(); p.set_default_timeout(45000)
        rows = _do_search(p, args.name)
        # De-dup by register+court.
        seen, uniq = set(), []
        for r in rows:
            k = (r["register"], r["court"])
            if k in seen:
                continue
            seen.add(k); uniq.append(r)
        uniq = uniq[: args.max]
        for r in uniq:
            r.pop("_ad", None); r.pop("_si", None)
        print(json.dumps({"found": len(uniq) > 0, "count": len(uniq),
                          "searched_name": args.name, "results": uniq}, ensure_ascii=False))
    finally:
        b.close()


def cmd_ad(args):
    b = launch(headless=True)
    try:
        p = b.new_page(); p.set_default_timeout(45000)
        rows = _do_search(p, args.name)
        want = re.sub(r"\s+", "", str(args.hrb)).lower() if args.hrb else None
        target = None
        for r in rows:
            if not r["_ad"]:
                continue
            if want:
                if want == r["register_number"].lower() and \
                   (not args.court or args.court.lower() in (r["court"] or "").lower()):
                    target = r; break
            else:
                target = r; break
        if not target:
            print(json.dumps({"downloaded": False,
                              "error": f"no matching register row (hrb={args.hrb}) among {len(rows)} results"}))
            return

        # Try to download the AD. handelsregister.de throttles document retrieval: after a few
        # docs in a short window it routes the click to /documents/error.xhtml instead of the
        # PDF. Detect that, back off, and retry a couple of times.
        matched = {k: target[k] for k in ("name", "seat", "register", "court", "state", "status")}
        outcome = "timeout"
        for attempt in range(3):
            try:
                with p.expect_download(timeout=25000) as di:
                    p.click("[id='%s']" % target["_ad"])
                di.value.save_as(args.out)
                if os.path.exists(args.out) and os.path.getsize(args.out) > 1000:
                    print(json.dumps({"downloaded": True, "out": args.out, "matched": matched},
                                     ensure_ascii=False))
                    return
            except Exception:
                pass
            # No download; inspect where we landed.
            throttled = "documents/error" in (p.url or "")
            outcome = "throttled" if throttled else "timeout"
            if attempt < 2:
                p.wait_for_timeout(4000)
                # re-run the search so the (row-indexed) AD link ids are fresh
                rows = _do_search(p, args.name)
                target = next((r for r in rows if r["_ad"] and (not want or
                              (want == r["register_number"].lower() and
                               (not args.court or args.court.lower() in (r["court"] or "").lower())))), target)

        note = ("handelsregister.de rate-limited document retrieval (routes to an error page "
                "after several downloads in a short window). The search worked; retry the AD "
                "after a short cooldown (minutes).") if outcome == "throttled" else \
               "AD download did not start (no document event). The search worked."
        print(json.dumps({"downloaded": False, "reason": outcome, "error": note, "matched": matched},
                         ensure_ascii=False))
    finally:
        b.close()


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search"); s.add_argument("name"); s.add_argument("--max", type=int, default=25)
    a = sub.add_parser("ad"); a.add_argument("name"); a.add_argument("--out", required=True)
    a.add_argument("--hrb"); a.add_argument("--court")
    args = ap.parse_args()
    if args.cmd == "search":
        cmd_search(args)
    elif args.cmd == "ad":
        cmd_ad(args)


if __name__ == "__main__":
    main()
