#!/usr/bin/env python3
"""
bailii_fetch.py — Search BAILII and download a UK/Irish case as a clean PDF.

BAILII now sits behind Anubis, a JavaScript proof-of-work bot wall, and re-issues
challenges on most requests. This script solves the proof-of-work in pure Python
(no browser needed), handles the quirks of BAILII's CGI endpoints, strips the page
chrome, and renders the judgment to PDF.

Usage:
    python3 bailii_fetch.py cite "[2024] EAT 114" [--out DIR] [--keep-html] [--no-pdf]
    python3 bailii_fetch.py url  "https://www.bailii.org/uk/cases/UKEAT/2024/114.html" [--out DIR]
    python3 bailii_fetch.py search "Uber Aslam" [--limit 10]

Notes:
  * `cite`  — most reliable. Give a neutral citation; BAILII maps it to the case URL.
  * `url`   — when you already have the BAILII case URL.
  * `search`— name-based; prints candidates (it does NOT auto-download, because
              BAILII's title search is fuzzy and you should choose the right hit).
  * Only the Python standard library is required for fetching. PDF rendering uses
    whichever of these is found: wkhtmltopdf, Chrome/Chromium headless, or weasyprint.
    If none is present the cleaned HTML is saved and the path reported.
"""

import sys, os, re, json, time, argparse, hashlib, subprocess, shutil
import urllib.parse, urllib.request, urllib.error, http.cookiejar
import html as H

BASE = "https://www.bailii.org"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")


# --------------------------------------------------------------------------- #
# HTTP layer (Anubis-aware)                                                     #
# --------------------------------------------------------------------------- #
class _NoRedirect(urllib.request.HTTPRedirectHandler):
    # BAILII's citation finder 302-redirects to the case URL, and the redirect
    # target re-challenges. We follow redirects manually so each hop can solve
    # its own challenge, and so we can percent-encode targets containing spaces.
    def redirect_request(self, *a):
        return None


def make_opener():
    cj = http.cookiejar.CookieJar()
    op = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(cj), _NoRedirect())
    op.addheaders = [("User-Agent", UA),
                     ("Accept", "text/html,application/xhtml+xml,*/*;q=0.8"),
                     ("Accept-Language", "en-GB,en;q=0.9")]
    return op


def _raw(op, url, data=None, timeout=45):
    req = urllib.request.Request(url, data=data)
    try:
        with op.open(req, timeout=timeout) as r:
            return r.read().decode("utf-8", "replace"), r.geturl(), r.getcode(), dict(r.headers)
    except urllib.error.HTTPError as e:
        return e.read().decode("utf-8", "replace"), url, e.code, dict(e.headers)


def is_anubis(text):
    return ("anubis_challenge" in text) or ("Making sure you" in text)


def _solve_anubis(op, page_html):
    """Solve the Anubis proof-of-work and redeem it for the auth cookie.

    Anubis "fast": find nonce so SHA256(randomData + nonce) has `difficulty`
    leading zero hex chars, then GET the pass-challenge endpoint. We redeem with
    redir='/' (a harmless GET) — never the original POST endpoint, which 500s.
    """
    m = re.search(r'<script id="anubis_challenge"[^>]*>(.*?)</script>', page_html, re.S)
    if not m:
        return
    ch = json.loads(m.group(1).strip())["challenge"]
    rand, diff, cid = ch["randomData"], int(ch.get("difficulty", 2)), ch["id"]
    prefix, nonce, t0 = "0" * diff, 0, time.time()
    while True:
        digest = hashlib.sha256((rand + str(nonce)).encode()).hexdigest()
        if digest.startswith(prefix):
            break
        nonce += 1
    qs = urllib.parse.urlencode({
        "id": cid, "response": digest, "nonce": nonce,
        "redir": "/", "elapsedTime": int((time.time() - t0) * 1000)})
    _raw(op, f"{BASE}/.within.website/x/cmd/anubis/api/pass-challenge?{qs}")


def request(op, url, data=None, tries=12, follow=True):
    """Fetch a URL, transparently solving Anubis and following redirects.

    Anubis re-challenges frequently even with a valid cookie, so we solve on
    every challenged response and retry the same request. Returns (body, final_url, code).
    """
    body = final = ""
    code = 0
    for _ in range(tries):
        body, final, code, hdrs = _raw(op, url, data=data)
        if is_anubis(body):
            _solve_anubis(op, body)
            continue
        if code >= 500:
            time.sleep(0.4)
            continue
        loc = next((v for k, v in hdrs.items() if k.lower() == "location"), None)
        if follow and code in (301, 302, 303, 307, 308) and loc:
            # percent-encode spaces (BAILII's search redirect contains them)
            url = urllib.parse.urljoin(url, loc).replace(" ", "%20")
            data = None
            continue
        return body, final, code
    return body, final, code


def warm(op):
    """Obtain the first Anubis cookie via a harmless homepage GET."""
    request(op, BASE + "/")


def fetch_case(op, url, attempts=5):
    """Fetch a case page, validating it is a genuine judgment (not a stray
    challenge or error page). Retries the whole fetch if validation fails."""
    body, final = "", url
    for _ in range(attempts):
        body, final, code = request(op, url)
        if (code == 200 and not is_anubis(body) and len(body) > 8000
                and "/cases/" in final and final.endswith(".html")):
            return body, final
        time.sleep(0.3)
    return body, final


# --------------------------------------------------------------------------- #
# Search / resolve                                                              #
# --------------------------------------------------------------------------- #
def resolve_citation(op, citation):
    """Map a neutral citation to its BAILII case URL + HTML. Returns (url, html)
    or (None, html) when BAILII has no direct match."""
    body, final, code = request(
        op, BASE + "/cgi-bin/find_by_citation.cgi",
        data=urllib.parse.urlencode({"citation": citation}).encode())
    if ("/cases/" in final and final.endswith(".html")
            and not is_anubis(body) and len(body) > 8000):
        # ensure we actually have the full case (re-fetch with validation)
        body, final = fetch_case(op, final)
        return final, body
    return None, body


def search_by_name(op, name, limit=10):
    """Title-scoped search. BAILII's default all-fields search ranks alphabetically
    and rarely surfaces the target case; restricting to the title field works far
    better. Returns a list of (url, title) candidates."""
    query = "title:(%s)" % " ".join(re.findall(r"[\w']+", name))
    url = BASE + "/cgi-bin/lucy_search_1.cgi?" + urllib.parse.urlencode(
        {"query": query, "mask_path": "/", "method": "boolean"})
    body, final, code = request(op, url)
    out, seen = [], set()
    for href, txt in re.findall(
            r'<a href="(/\w+/cases/[^"]+\.html)"[^>]*>(.*?)</a>', body, re.I | re.S):
        if href in seen:
            continue
        seen.add(href)
        title = re.sub(r"<[^>]+>|\s+", " ", H.unescape(txt)).strip().lstrip(">").strip()
        out.append((BASE + href, title))
        if len(out) >= limit:
            break
    return out


# --------------------------------------------------------------------------- #
# Clean + render                                                                #
# --------------------------------------------------------------------------- #
def clean_html(raw, src_url):
    """Strip BAILII chrome (nav, search form, donation banner, footer, scripts,
    images) and return (case_title, standalone_html)."""
    mt = re.search(r"<title>(.*?)</title>", raw, re.S | re.I)
    title = re.sub(r"\s+", " ", H.unescape(mt.group(1))).strip() if mt else "BAILII case"

    h = raw
    for pat in (r"<script\b.*?</script>", r"<style\b.*?</style>",
                r"<noscript\b.*?</noscript>", r"<(iframe|object|embed)\b.*?</\1>",
                r"<form\b.*?</form>"):
        h = re.sub(pat, "", h, flags=re.I | re.S)
    h = re.sub(r"<link\b[^>]*>", "", h, flags=re.I)
    h = re.sub(r"<img\b[^>]*>", "", h, flags=re.I)

    # cut the footer (everything from the BAILII copyright line onward).
    # Tag-tolerant: in the HTML there is usually an <a> between "BAILII:" and
    # "Copyright Policy", so a plain-text match would miss it.
    h = re.split(r"BAILII:\s*(?:<[^>]+>\s*)*Copyright Policy", h,
                 maxsplit=1, flags=re.I)[0]
    # remove top nav bar ("[ Home ] [ Databases ] ...") up to the case heading/rule
    h = re.sub(r"\[\s*<a [^>]*>\s*Home\s*</a>\s*\].*?(?=<hr|<h1|<H1)", "",
               h, flags=re.I | re.S, count=1)
    h = re.sub(r"\[\s*Home\s*\].*?(?=<hr|<h1|<H1)", "", h, flags=re.I | re.S, count=1)
    # remove the "You are here:" breadcrumb line
    h = re.sub(r"You are here:.*?(?=<hr|<h1|<H1|<h2|<H2)", "",
               h, flags=re.I | re.S, count=1)
    # remove the "[New search] [Contents list] ... [Help]" toolbar that sits
    # above the judgment. Anchored on the stable first/last items so it works
    # regardless of which optional middle links (ICLR etc.) are present.
    h = re.sub(r"\[\s*<a\b[^>]*>\s*New search\s*</a>\s*\].*?"
               r"\[\s*<a\b[^>]*>\s*Help\s*</a>\s*\]", "",
               h, flags=re.I | re.S, count=1)
    # remove the donation appeal block
    h = re.sub(r"THE FUTURE OF BAILII.*?(?=<hr|<h2|<H2|JUDGMENT|<center)", "",
               h, flags=re.I | re.S, count=1)

    parts = re.split(r"<body[^>]*>", h, maxsplit=1, flags=re.I)
    inner = parts[1] if len(parts) > 1 else h
    inner = re.sub(r"</body>.*", "", inner, flags=re.I | re.S)

    css = ("<meta charset='utf-8'><style>"
           "body{font:13px/1.55 Georgia,'Times New Roman',serif;max-width:820px;"
           "margin:0 auto;padding:0 16px;color:#111}"
           "a{color:#111;text-decoration:none}"
           "h1{font-size:18px}h2{font-size:16px}h3{font-size:14px}"
           "blockquote{margin:0 0 0 24px}</style>")
    banner = ("<div style='font:11px Helvetica,Arial,sans-serif;color:#666;"
              "border-bottom:1px solid #ccc;padding:0 0 8px;margin-bottom:18px'>"
              "Retrieved from BAILII &middot; %s</div>" % H.escape(src_url))
    doc = ("<!doctype html><html><head>%s</head><body>%s%s</body></html>"
           % (css, banner, inner))
    return title, doc


def safe_filename(title):
    fn = re.sub(r'[\\/:*?"<>|]', "", title).strip()
    if len(fn) > 118:
        fn = fn[:118].rsplit(" ", 1)[0]
    return fn or "bailii_case"


def html_to_pdf(html_path, pdf_path):
    """Render local HTML to PDF using whatever converter is available.
    Returns the converter name on success, or None if none worked."""
    # 1) wkhtmltopdf (note: many builds use unpatched Qt — avoid --footer-* flags)
    if shutil.which("wkhtmltopdf"):
        r = subprocess.run(
            ["wkhtmltopdf", "--quiet", "--enable-local-file-access",
             "--load-error-handling", "ignore", "--load-media-error-handling", "ignore",
             "--margin-top", "16mm", "--margin-bottom", "16mm",
             "--margin-left", "15mm", "--margin-right", "15mm",
             html_path, pdf_path],
            capture_output=True, text=True, timeout=240)
        if r.returncode == 0 and os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 1000:
            return "wkhtmltopdf"

    # 2) Headless Chrome / Chromium
    for cand in ("google-chrome", "chromium", "chromium-browser",
                 "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                 "/Applications/Chromium.app/Contents/MacOS/Chromium"):
        exe = cand if os.path.exists(cand) else shutil.which(cand)
        if exe:
            r = subprocess.run(
                [exe, "--headless", "--disable-gpu", "--no-sandbox",
                 "--print-to-pdf=" + pdf_path, "--no-pdf-header-footer",
                 "file://" + os.path.abspath(html_path)],
                capture_output=True, text=True, timeout=240)
            if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 1000:
                return os.path.basename(exe)

    # 3) weasyprint (Python)
    try:
        import weasyprint  # noqa
        weasyprint.HTML(filename=html_path).write_pdf(pdf_path)
        if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 1000:
            return "weasyprint"
    except Exception:
        pass
    return None


def save_case(raw_html, src_url, outdir, keep_html=False, make_pdf=True):
    os.makedirs(outdir, exist_ok=True)
    title, doc = clean_html(raw_html, src_url)
    base = safe_filename(title)
    html_path = os.path.join(outdir, base + ".html")
    with open(html_path, "w") as f:
        f.write(doc)

    result = {"title": title, "source_url": src_url, "html": html_path, "pdf": None}
    if make_pdf:
        pdf_path = os.path.join(outdir, base + ".pdf")
        engine = html_to_pdf(html_path, pdf_path)
        if engine:
            result["pdf"] = pdf_path
            result["pdf_engine"] = engine
            if not keep_html:
                try:
                    os.remove(html_path)
                    result["html"] = None
                except OSError:
                    pass
    return result


# --------------------------------------------------------------------------- #
# CLI                                                                           #
# --------------------------------------------------------------------------- #
def _emit(result):
    print(json.dumps(result, indent=2))


def main():
    ap = argparse.ArgumentParser(description="Search BAILII and download a case as PDF.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    pc = sub.add_parser("cite", help="resolve a neutral citation and download")
    pc.add_argument("citation")
    pc.add_argument("--out", default=".")
    pc.add_argument("--keep-html", action="store_true")
    pc.add_argument("--no-pdf", action="store_true")

    pu = sub.add_parser("url", help="download a known BAILII case URL")
    pu.add_argument("url")
    pu.add_argument("--out", default=".")
    pu.add_argument("--keep-html", action="store_true")
    pu.add_argument("--no-pdf", action="store_true")

    ps = sub.add_parser("search", help="title search; prints candidates (no download)")
    ps.add_argument("name")
    ps.add_argument("--limit", type=int, default=10)

    args = ap.parse_args()
    op = make_opener()
    warm(op)

    if args.cmd == "search":
        cands = search_by_name(op, args.name, args.limit)
        if not cands:
            print("No candidates found. Try a neutral citation with the `cite` command.",
                  file=sys.stderr)
            sys.exit(2)
        print(json.dumps([{"url": u, "title": t} for u, t in cands], indent=2))
        return

    if args.cmd == "cite":
        url, body = resolve_citation(op, args.citation)
        if not url:
            print("No direct match on BAILII for citation: %s\n"
                  "Try the `search` command by case name, or check the citation."
                  % args.citation, file=sys.stderr)
            sys.exit(2)
    else:  # url
        if "bailii.org" not in args.url:
            print("Not a BAILII URL.", file=sys.stderr)
            sys.exit(2)
        body, url = fetch_case(op, args.url)
        if is_anubis(body) or len(body) < 8000:
            print("Could not retrieve a valid case page (bot wall / not found).",
                  file=sys.stderr)
            sys.exit(2)

    result = save_case(body, url, args.out,
                       keep_html=args.keep_html, make_pdf=not args.no_pdf)
    _emit(result)
    if not result["pdf"] and not args.no_pdf:
        print("\nNo PDF converter found (wkhtmltopdf / Chrome / weasyprint). "
              "Saved cleaned HTML instead — open it in a browser and Print to PDF.",
              file=sys.stderr)


if __name__ == "__main__":
    main()
