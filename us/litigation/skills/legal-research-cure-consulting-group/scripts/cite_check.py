#!/usr/bin/env python3
"""cite_check.py — Extract and verify every legal citation in a draft.

Finds case citations (U.S., S. Ct., F., F. Supp., N.Y., A.D., Misc., N.E.,
N.Y.S., NY Slip Op, WL/LEXIS) and NY/federal statute citations, then:
  cases     verified against CourtListener: the citation-lookup API when
            COURTLISTENER_API_TOKEN is set, otherwise an exact citation search
            on the public search API (slower, 1 request/second). The case
            name in the draft is compared with the name on record to catch
            real-cite/wrong-case fabrications.
  statutes  given an official lookup URL (nysenate.gov, law.cornell.edu);
            --live fetches each URL and confirms the section exists.
Existence is not support: a VERIFIED case still has to be read for the
proposition it is cited for.

Usage:
  python3 cite_check.py memo.md
  python3 cite_check.py memo.md --live --json
  cat memo.md | python3 cite_check.py -

Exit 0 when every citation is VERIFIED/OK, 1 when any is not, 2 on bad input.
"""

import argparse
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://www.courtlistener.com/api/rest/v4/citation-lookup/"
SEARCH = "https://www.courtlistener.com/api/rest/v4/search/"
# Periods optional on the NY reporters: the NY Official Reports style (Tanbook) writes "80 NY2d 336".
REPORTERS = (r"U\.\s?S\.|S\.\s?Ct\.|L\.\s?Ed\.(?:\s?2d)?|F\.\s?Supp\.(?:\s?[23]d)?|F\.(?:\s?(?:2d|3d|4th))?"
             r"|F\.\s?App'x|N\.?Y\.?S\.?(?:\s?[23]d)?|N\.?Y\.?(?:\s?[23]d)?|A\.?D\.?(?:\s?[23]d)?|Misc\.?(?:\s?[23]d)?"
             r"|N\.E\.(?:\s?[23]d)?|B\.R\.|A\.(?:\s?[23]d)?|P\.(?:\s?[23]d)?"
             r"|S\.W\.(?:\s?[23]d)?|So\.(?:\s?[23]d)?|N\.W\.(?:\s?2d)?|S\.E\.(?:\s?2d)?|Cal\.\s?Rptr\.(?:\s?[23]d)?")
CASE_RE = re.compile(rf"\b(\d{{1,4}})\s+({REPORTERS})\s+(\d{{1,5}})\b")
SLIP_RE = re.compile(r"\b(\d{4})\s+N\.?Y\.?\s+Slip\s+Op\.?\s+(\d{3,6})(?:\(U\))?", re.I)
PROP_RE = re.compile(r"\b\d{4}\s+(?:WL|U\.S\.\s?Dist\.\s?LEXIS|N\.Y\.\s?LEXIS)\s+\d+", re.I)
_W = r"(?:[A-Z][\w'&-]*\.?|of|the|and|&|ex rel\.)"
NAME_RE = re.compile(rf"((?:{_W}\s+){{0,6}}{_W}\s+v\.?\s+(?:{_W},?\s+){{0,6}}{_W}),?\s*$")
SIGNALS = re.compile(r"^(?:(?:Under|See|Also|Cf\.|But|Accord|Compare|In|And|The)\s+)+")

# NY consolidated-law ids on nysenate.gov: https://www.nysenate.gov/legislation/laws/<ID>/<section>
NY_LAWS = {"CPLR": "CVP", "EPTL": "EPT", "SCPA": "SCP", "DRL": "DOM", "Domestic Relations Law": "DOM",
           "FCA": "FCT", "Family Court Act": "FCT", "GOL": "GOB", "General Obligations Law": "GOB",
           "BCL": "BSC", "Business Corporation Law": "BSC", "LLCL": "LLC", "Limited Liability Company Law": "LLC",
           "Partnership Law": "PTR", "Penal Law": "PEN", "PL": "PEN", "CPL": "CPL",
           "Criminal Procedure Law": "CPL", "RPL": "RPP", "Real Property Law": "RPP",
           "RPAPL": "RPA", "Judiciary Law": "JUD", "SAPA": "SAP", "Public Officers Law": "PBO",
           "General Municipal Law": "GMU", "GML": "GMU", "Labor Law": "LAB", "Insurance Law": "ISC",
           "Vehicle and Traffic Law": "VAT", "VTL": "VAT", "Civil Rights Law": "CVR", "Education Law": "EDN",
           # Bluebook forms
           "N.Y. C.P.L.R.": "CVP", "N.Y. Gen. Oblig. Law": "GOB", "N.Y. Est. Powers & Trusts Law": "EPT",
           "N.Y. Surr. Ct. Proc. Act": "SCP", "N.Y. Dom. Rel. Law": "DOM", "N.Y. Fam. Ct. Act": "FCT",
           "N.Y. Bus. Corp. Law": "BSC", "N.Y. Ltd. Liab. Co. Law": "LLC", "N.Y. Limited Liability Company Law": "LLC",
           "N.Y. P'ship Law": "PTR", "N.Y. Penal Law": "PEN", "N.Y. Crim. Proc. Law": "CPL",
           "N.Y. Real Prop. Law": "RPP", "N.Y. Real Prop. Acts. Law": "RPA", "N.Y. Jud. Law": "JUD",
           "N.Y. Pub. Off. Law": "PBO", "N.Y. Gen. Mun. Law": "GMU", "N.Y. Lab. Law": "LAB",
           "N.Y. Ins. Law": "ISC", "N.Y. Veh. & Traf. Law": "VAT", "N.Y. Civ. Rights Law": "CVR",
           "N.Y. Educ. Law": "EDN", "N.Y. State Admin. Proc. Act": "SAP"}
_names = "|".join(sorted((re.escape(k) for k in NY_LAWS), key=len, reverse=True))
NY_STAT_RE = re.compile(rf"(?<![\w.])({_names})\s*(?:§+|[Ss]ection|[Rr]ule|R\.)?\s*(\d+(?:[-.]\d+)*(?:-[a-z])?(?:\.\d+)?)")
USC_RE = re.compile(r"\b(\d{1,2})\s+U\.S\.C\.?\s*§+\s*(\d+[a-z]?(?:-\d+)?)")
CFR_RE = re.compile(r"\b(\d{1,2})\s+C\.F\.R\.?\s*§+\s*(\d+\.\d+)")


def tls():
    """Default TLS context; falls back to the system bundle when Python ships none (macOS)."""
    ctx = ssl.create_default_context()
    if not ctx.cert_store_stats().get("x509_ca") and os.path.exists("/etc/ssl/cert.pem"):
        ctx.load_verify_locations("/etc/ssl/cert.pem")
    return ctx


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    """Never follow redirects: urllib would carry the Authorization header to the new host."""

    def redirect_request(self, *args, **kwargs):
        return None


def _open(req, timeout):
    opener = urllib.request.build_opener(_NoRedirect, urllib.request.HTTPSHandler(context=tls()))
    return opener.open(req, timeout=timeout)


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def extract(text):
    cites, seen = [], set()
    for m in CASE_RE.finditer(text):
        key = norm(m.group(0))
        if key in seen:
            continue
        seen.add(key)
        before = re.sub(r"[*_]", "", text[max(0, m.start() - 160):m.start()])
        nm = NAME_RE.search(before)
        name = SIGNALS.sub("", norm(nm.group(1))) if nm else None
        cites.append({"kind": "case", "cite": key, "name": name if name and " v" in name else None,
                      "volume": m.group(1), "reporter": canon(norm(m.group(2))), "page": m.group(3)})
    for m in SLIP_RE.finditer(text):
        key = norm(m.group(0))
        if key not in seen:
            seen.add(key)
            cites.append({"kind": "slip-op", "cite": key,
                          "url": f"https://nycourts.gov/reporter/slipidx/  (search {key})"})
    for m in PROP_RE.finditer(text):
        cites.append({"kind": "proprietary", "cite": norm(m.group(0))})
    for m in NY_STAT_RE.finditer(text):
        law, sec = m.group(1), m.group(2).rstrip(".")
        key = f"{law} {sec}"
        if key not in seen:
            seen.add(key)
            cites.append({"kind": "ny-statute", "cite": key,
                          "url": f"https://www.nysenate.gov/legislation/laws/{NY_LAWS[law]}/{sec.upper()}"})
    for m in USC_RE.finditer(text):
        key = norm(m.group(0))
        if key not in seen:
            seen.add(key)
            cites.append({"kind": "usc", "cite": key,
                          "url": f"https://www.law.cornell.edu/uscode/text/{m.group(1)}/{m.group(2)}"})
    for m in CFR_RE.finditer(text):
        key = norm(m.group(0))
        if key not in seen:
            seen.add(key)
            cites.append({"kind": "cfr", "cite": key,
                          "url": f"https://www.ecfr.gov/current/title-{m.group(1)}/section-{m.group(2)}"})
    return cites


_OFFICIAL = [(r"^N\.?Y\.?S\.?", "N.Y.S."), (r"^N\.?Y\.?", "N.Y."), (r"^A\.?D\.?", "A.D."), (r"^Misc\.?", "Misc.")]


def canon(reporter):
    """Tanbook 'NY2d' / 'AD3d' / 'Misc 3d' → the dotted form CourtListener indexes."""
    rep = reporter.replace(" ", "")
    for pat, dotted in _OFFICIAL:
        m = re.match(pat, rep)
        if m:
            series = rep[m.end():]
            return dotted + series if dotted != "Misc." else f"Misc. {series}".strip()
    return reporter


def tokens(name):
    stop = {"v", "the", "of", "inc", "co", "corp", "llc", "people", "state", "city", "new", "york", "in", "re", "matter"}
    return {w for w in re.findall(r"[a-z]+", (name or "").lower()) if w not in stop and len(w) > 2}


def verify_cases(cites, token, timeout):
    cases = [c for c in cites if c["kind"] == "case"]
    if not cases:
        return
    if not token:
        for c in cases:
            search_case(c, timeout)
        return
    text = "\n".join(c["cite"] for c in cases)
    req = urllib.request.Request(API, data=urllib.parse.urlencode({"text": text}).encode(),
                                 headers={"Authorization": f"Token {token}"}, method="POST")
    try:
        with _open(req, timeout) as r:
            results = json.loads(r.read())
    except (urllib.error.URLError, ValueError, OSError) as e:
        for c in cases:
            c["status"], c["note"] = "UNVERIFIED", f"lookup failed: {e}"
        return
    by_cite = {}
    for r in results:
        for nc in r.get("normalized_citations") or [r.get("citation", "")]:
            by_cite[norm(nc)] = r
        by_cite.setdefault(norm(r.get("citation", "")), r)
    for c in cases:
        r = by_cite.get(c["cite"]) or by_cite.get(f"{c['volume']} {c['reporter']} {c['page']}")
        code = (r or {}).get("status")
        clusters = (r or {}).get("clusters") or []
        record = clusters[0].get("case_name") if clusters else None
        c["record_name"] = record
        c["status"] = {200: "VERIFIED", 300: "AMBIGUOUS", 400: "BAD-REPORTER", 404: "NOT-FOUND",
                       429: "UNVERIFIED"}.get(code, "UNVERIFIED")
        if c["status"] == "VERIFIED" and c.get("name") and record and not (tokens(c["name"]) & tokens(record)):
            c["status"] = "NAME-MISMATCH"
            c["note"] = f"draft says '{c['name']}', record is '{record}'"


# nysenate.gov's bot filter admits curl-style agents only; the suffix says who we are.
UA = "curl/8.4.0 (cure-cite-check/1.0)"


def _fetch(url, timeout, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout, context=tls()) as r:
                return r.read(400_000).decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code != 429 or i == tries - 1:
                raise
            time.sleep(min(30, int(e.headers.get("Retry-After") or 0) or 5 * (i + 1)))


def search_case(c, timeout):
    """Tokenless fallback: exact citation-field search on CourtListener's public search API."""
    q = urllib.parse.quote(f'citation:("{c["volume"]} {c["reporter"]} {c["page"]}")')
    try:
        data = json.loads(_fetch(f"{SEARCH}?type=o&q={q}", timeout))
    except (urllib.error.URLError, ValueError, OSError) as e:
        c["status"], c["note"] = "UNVERIFIED", f"search failed: {e}"
        return
    time.sleep(1)  # be polite to the anonymous endpoint
    want = norm(f"{c['volume']} {c['reporter']} {c['page']}").replace(" ", "").lower()
    hits = [r for r in data.get("results", [])
            if any(norm(x).replace(" ", "").lower() == want for x in r.get("citation", []))]
    if not hits:
        c["status"] = "NOT-FOUND"
        c["note"] = "not in CourtListener; check the Official Reports before calling it fabricated"
        return
    record = hits[0].get("caseName")
    c["record_name"] = record
    c["status"] = "VERIFIED"
    if c.get("name") and record and not (tokens(c["name"]) & tokens(record)):
        c["status"] = "NAME-MISMATCH"
        c["note"] = f"draft says '{c['name']}', record is '{record}'"


def check_url(c, timeout):
    try:
        body = _fetch(c["url"], timeout).lower()
        missing = "could not be found" in body or "page not found" in body
        c["status"] = "NOT-FOUND" if missing else "OK"
    except urllib.error.HTTPError as e:
        c["status"], c["note"] = ("NOT-FOUND", "HTTP 404") if e.code == 404 else ("UNVERIFIED", f"HTTP {e.code}")
    except (urllib.error.URLError, OSError, ValueError) as e:
        c["status"], c["note"] = "UNVERIFIED", f"fetch failed: {e}"


def main():
    ap = argparse.ArgumentParser(description="Extract and verify legal citations in a draft.")
    ap.add_argument("file", help="draft to check (markdown or text); '-' for stdin")
    ap.add_argument("--live", action="store_true", help="fetch statute URLs to confirm each section exists")
    ap.add_argument("--timeout", type=float, default=20, help="network timeout, seconds")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    a = ap.parse_args()
    try:
        text = sys.stdin.read() if a.file == "-" else open(a.file, encoding="utf-8").read()
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    cites = extract(text)
    verify_cases(cites, os.environ.get("COURTLISTENER_API_TOKEN"), a.timeout)
    for c in cites:
        if c["kind"] in ("ny-statute", "usc", "cfr"):
            if a.live:
                check_url(c, a.timeout)
            else:
                c.setdefault("status", "UNVERIFIED")
                c.setdefault("note", "run with --live, or open the URL")
        elif c["kind"] == "slip-op":
            c["status"], c["note"] = "UNVERIFIED", "check the NY Official Reports slip-opinion index"
        elif c["kind"] == "proprietary":
            c["status"], c["note"] = "UNVERIFIED", "Westlaw/Lexis cite — verify in that service"
    bad = [c for c in cites if c["status"] not in ("VERIFIED", "OK")]
    counts = {}
    for c in cites:
        counts[c["status"]] = counts.get(c["status"], 0) + 1
    if a.json:
        print(json.dumps({"citations": cites, "counts": counts, "clean": not bad}, indent=2))
    else:
        print(f"{len(cites)} citations: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
        for c in cites:
            extra = c.get("note") or c.get("url") or ""
            label = f"{c['name']}, {c['cite']}" if c.get("name") else c["cite"]
            print(f"  {c['status']:<13} {c['kind']:<11} {label}   {extra}")
        if not cites:
            print("  (no citations found — a legal memo with none is itself a finding)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
