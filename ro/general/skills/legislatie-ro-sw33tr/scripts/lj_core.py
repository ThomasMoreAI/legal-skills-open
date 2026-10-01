#!/usr/bin/env python3
"""lj_core — textul ÎN VIGOARE al unui act de pe legislatie.just.ro + extragere articol.

Standalone: doar biblioteca standard Python 3.6+. Poate fi copiat și rulat oriunde
(inclusiv pe calculatorul utilizatorului), din orice director.

  python3 lj_core.py 215925 --articol 485^1
  python3 lj_core.py https://legislatie.just.ro/Public/DetaliiDocument/215925 --grep "concediu"
  python3 lj_core.py 215925 --info            # doar forma/data, fără text

Coduri de ieșire: 0 ok | 3 rețea: HTTPS către portal blocat din acest mediu |
                  4 articol negăsit | 5 pagina nu conține text de act | 6 act inexistent
"""
import argparse, json, os, re, ssl, sys, tempfile, time
import urllib.error, urllib.request
from html.parser import HTMLParser

VERSION = "6.1.0"
HOST = "legislatie.just.ro"
UA = "Mozilla/5.0 (legislatie-skill)"
CACHE_DIR = os.environ.get("LEGISLATIE_CACHE") or os.path.join(tempfile.gettempdir(), "legislatie_cache")
CACHE_TTL = 6 * 3600  # consolidările apar de câteva ori pe lună; 6h e sigur


class RouteBlocked(Exception):
    """HTTPS către portal nu merge din mediul curent (proxy, IP de datacenter, fără rețea)."""


def utf8_console():
    """Diacriticele nu trebuie să blocheze consolele Windows (cp1252/cp852)."""
    for st in (sys.stdout, sys.stderr):
        try:
            st.reconfigure(encoding="utf-8", errors="replace")
        except Exception:  # noqa: BLE001  (Python < 3.7 sau stream înlocuit)
            pass


def _cert_error(e):
    r = getattr(e, "reason", e)
    return isinstance(r, ssl.SSLError) and "CERTIFICATE_VERIFY_FAILED" in str(r)


def urlopen(req, timeout=90):
    """urllib.urlopen (respectă HTTP(S)_PROXY). Dacă magazinul de certificate lipsește
    (frecvent pe Python instalat de pe python.org pe macOS), reîncearcă cu certifi."""
    try:
        return urllib.request.urlopen(req, timeout=timeout)
    except urllib.error.URLError as e:
        if not _cert_error(e):
            raise
        try:
            import certifi  # noqa: WPS433
        except ImportError:
            raise RouteBlocked("certificatele SSL de sistem lipsesc: rulează «Install Certificates.command» "
                               "(macOS, python.org) sau `pip install certifi`")
        ctx = ssl.create_default_context(cafile=certifi.where())
        return urllib.request.urlopen(req, timeout=timeout, context=ctx)


def fetch_html(path, timeout=90):
    url = path if path.startswith("http") else "https://%s%s" % (HOST, path)
    url = url.replace("http://", "https://", 1)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html"})
    try:
        with urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        if e.code in (403, 407, 429, 502, 503, 504):  # proxy / filtrare / portal supraîncărcat
            raise RouteBlocked("HTTP %s pentru %s" % (e.code, url))
        raise LookupError("Portalul a răspuns HTTP %s pentru %s (id greșit?)" % (e.code, url))
    except (urllib.error.URLError, OSError) as e:  # reset, timeout, DNS, proxy
        raise RouteBlocked("%s: %s" % (type(e).__name__, getattr(e, "reason", e)))


class _H2T(HTMLParser):
    SKIP = {"script", "style", "head", "noscript"}
    BLOCK = {"p", "div", "br", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6",
             "section", "article", "ul", "ol", "table"}

    def __init__(self):
        HTMLParser.__init__(self, convert_charrefs=True)
        self.parts, self.skip = [], []

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip.append(tag)
        elif not self.skip:
            self.parts.append("\n" if tag in self.BLOCK else " ")

    def handle_endtag(self, tag):
        if self.skip and self.skip[-1] == tag:
            self.skip.pop()
        elif not self.skip:
            self.parts.append("\n" if tag in self.BLOCK else " ")

    def handle_data(self, d):
        if not self.skip:
            self.parts.append(d)


def html_to_text(raw):
    p = _H2T()
    p.feed(raw)
    return clean_text("".join(p.parts))


def clean_text(text):
    """Normalizează spațiile pe linii și elimină marcajele de listă (și pentru textul din API)."""
    out = []
    for ln in text.split("\n"):
        ln = re.sub(r"[ \t\xa0]+", " ", ln).strip()
        if ln and ln not in {"+", "-", "•", "·"}:
            out.append(ln)
    return "\n".join(out)


def _d(s):  # "12.09.2026" -> (2026, 9, 12)
    p = s.split(".")
    return (int(p[2]), int(p[1]), int(p[0])) if len(p) == 3 else (0, 0, 0)


def parse_istoric(raw):
    """Lista consolidărilor din blocul istoric_fa: [{'data','id'}]; id=None = forma afișată."""
    m = re.search(r"id=['\"]istoric_fa['\"].*?</div>", raw, re.S)
    if not m:
        return []
    out = []
    for attrs, data in re.findall(r"<a\b([^>]*)>\s*([\d]{2}\.[\d]{2}\.[\d]{4})\s*</a>", m.group(0)):
        h = re.search(r"DetaliiDocument(?:Afis)?/(\d+)", attrs)
        out.append({"data": data, "id": h.group(1) if h else None})
    return out


def _has_body(text):
    return len(text) > 1500 and re.search(r"(?m)^(?:Articolul|Art\.)\s+\S", text) is not None


def doc_id_of(act):
    m = re.search(r"(\d+)\s*$", str(act).strip().rstrip("/"))
    if not m:
        raise ValueError("Nu recunosc id-ul actului în: %r" % act)
    return m.group(1)


def _load(page_id):
    """(raw, text, id_urmat): DetaliiDocument/<id>; dacă pagina e doar „ambalaj” (ex. Legea
    53/2003 -> Codul muncii, id 309240), urmează link-ul din forma consolidată afișată."""
    raw = fetch_html("/Public/DetaliiDocument/%s" % page_id)
    text, followed, seen = html_to_text(raw), None, {str(page_id)}
    for _ in range(2):
        if _has_body(text):
            break
        i = raw.find("div_Formaconsolidata")
        ln = re.search(r"DetaliiDocument(?:Afis)?/(\d+)", raw[i:i + 20000]) if i >= 0 else None
        if not ln or ln.group(1) in seen:
            break
        followed = ln.group(1)
        seen.add(followed)
        raw = fetch_html("/Public/DetaliiDocument/%s" % followed)
        text = html_to_text(raw)
    if not _has_body(text):
        alt = html_to_text(fetch_html("/Public/DetaliiDocumentAfis/%s" % (followed or page_id)))
        if _has_body(alt):
            text = alt
    return raw, text, followed


def get_in_force(act, no_cache=False, forma_baza=False, exact=False):
    """Returnează dict: id, url, forma, data_consolidare, id_consolidare, text, cache."""
    doc_id = doc_id_of(act)
    key = "%s%s" % (doc_id, "_baza" if forma_baza else ("_exact" if exact else ""))
    meta_p, txt_p = (os.path.join(CACHE_DIR, key + ext) for ext in (".json", ".txt"))
    if not no_cache and os.path.exists(meta_p) and os.path.exists(txt_p) \
            and time.time() - os.path.getmtime(meta_p) < CACHE_TTL:
        with open(meta_p, encoding="utf-8") as f:
            meta = json.load(f)
        with open(txt_p, encoding="utf-8") as f:
            meta["text"] = f.read()
        meta["cache"] = txt_p
        return meta

    meta = {"id": doc_id, "url": "https://%s/Public/DetaliiDocument/%s" % (HOST, doc_id),
            "forma": None, "data_consolidare": None, "id_consolidare": None}
    if forma_baza:
        text = html_to_text(fetch_html("/Public/DetaliiDocumentAfis/%s" % doc_id))
        meta["forma"] = "publicată inițial (cerută explicit)"
    else:
        # DetaliiDocument/<id> servește ULTIMA consolidare (DetaliiDocumentAfis/<id> = forma
        # publicată inițial). Apoi verificăm cu istoricul că forma afișată e chiar cea mai nouă.
        raw, text, fid = _load(doc_id)
        hist = parse_istoric(raw)
        shown = [h["data"] for h in hist if h["id"] is None]
        linked = [h for h in hist if h["id"]]
        newest = max(linked, key=lambda h: _d(h["data"])) if linked else None
        shown_d = shown[0] if shown else None
        if not exact and newest and (not _has_body(text) or not shown_d or _d(newest["data"]) > _d(shown_d)):
            raw, text, fid2 = _load(newest["id"])
            meta.update(data_consolidare=newest["data"], id_consolidare=fid2 or newest["id"])
        else:
            meta.update(data_consolidare=shown_d, id_consolidare=fid)
        if meta["data_consolidare"]:
            meta["forma"] = "consolidată — Consolidarea din %s" % meta["data_consolidare"]
        else:
            meta["forma"] = ("publicată — portalul nu listează consolidări (nemodificat, "
                             "sau consolidarea încă nepublicată: verifică actele modificatoare recente)")
            if not _has_body(text):
                text = html_to_text(fetch_html("/Public/DetaliiDocumentAfis/%s" % doc_id))
    head = text[:6000]
    ab = re.search(r"[^\n]{0,120}\ba fost abrogat[ăa]?\b[^\n]{0,160}", head)
    meta["avertisment"] = ("Posibil abrogat — verifică: " + ab.group(0).strip()) if ab else None

    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(txt_p, "w", encoding="utf-8") as f:
        f.write(text)
    with open(meta_p, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False)
    meta["text"], meta["cache"] = text, txt_p
    return meta


def _norm_ref(ref):
    ref = re.sub(r"^\s*(?:art\.?|articolul)\s*", "", ref.strip(), flags=re.I)
    sup = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")
    ref = re.sub(r"\s*\^\s*\{?\s*(\d+)\s*\}?", r"^\1", ref)
    m = re.match(r"^(\d+)([⁰¹²³⁴⁵⁶⁷⁸⁹]+)$", ref)
    return m.group(1) + "^" + m.group(2).translate(sup) if m else ref


def extract_articol(text, ref):
    """Textul articolului (cu Notele și deciziile de sub el). None dacă nu există."""
    ref = _norm_ref(ref)
    text = text if "\t" not in text[:5000] else clean_text(text)
    lead = "Articolul" if len(re.findall(r"(?m)^Articolul\s", text)) >= \
        len(re.findall(r"(?m)^Art\.\s", text)) else r"Art\."
    if re.fullmatch(r"[IVXLCDM]+", ref, re.I):
        num, stop = re.escape(ref.upper()), r"(?![IVXLCDM\^])"
    elif ref.lower() == "unic":
        num, stop = "unic", r"\b"
    else:
        num, stop = re.escape(ref), r"(?![\d^])"
    start = re.compile(r"(?m)^%s\s+%s%s" % (lead, num, stop))
    nxt = re.compile(r"(?m)^%s\s+(?:\d+(?:\^\d+)?|[IVXLCDM]+|unic)(?![\w^])" % lead)
    best = None
    for m in start.finditer(text):  # prima apariție e de obicei cuprinsul: luăm corpul cel mai lung
        n = nxt.search(text, m.end())
        end = n.start() if n else len(text)
        if best is None or end - m.start() > best[1] - best[0]:
            best = (m.start(), end)
    return text[best[0]:best[1]].strip() if best else None


def grep(text, pattern, context=1, limit=40):
    lines, rx, out = text.split("\n"), re.compile(pattern, re.I), []
    for i, ln in enumerate(lines):
        if rx.search(ln):
            out.append("\n".join("%6d  %s" % (j + 1, lines[j][:600])
                                 for j in range(max(0, i - context), min(len(lines), i + context + 1))))
            if len(out) >= limit:
                out.append("… (limită %d potriviri)" % limit)
                break
    return "\n--\n".join(out)


def header(meta):
    s = ["ACT:    id %s — %s" % (meta["id"], meta["url"]), "FORMA:  " + meta["forma"]]
    if meta.get("id_consolidare"):
        s.append("        (id consolidare %s)" % meta["id_consolidare"])
    if meta.get("avertisment"):
        s.append("ATENȚIE: " + meta["avertisment"])
    if meta.get("cache"):
        s.append("TEXT:   %s caractere -> %s" % (format(len(meta["text"]), ","), meta["cache"]))
    return "\n".join(s)


def main(argv=None):
    utf8_console()
    ap = argparse.ArgumentParser(description="Text în vigoare + articol, legislatie.just.ro")
    ap.add_argument("act", nargs="?", help="id (215925) sau link DetaliiDocument/<id>")
    ap.add_argument("--articol", help="ex: 485^1, 12, XLIX, 'Art. 5', unic")
    ap.add_argument("--grep", help="regex căutat în text (linii cu context)")
    ap.add_argument("--context", type=int, default=1)
    ap.add_argument("--info", action="store_true", help="doar forma/data, fără text")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-cache", action="store_true")
    ap.add_argument("--forma-baza", action="store_true", help="forma publicată inițial")
    ap.add_argument("--exact", action="store_true",
                    help="exact consolidarea cu acest id (istoric), fără salt la cea mai nouă")
    ap.add_argument("--version", action="store_true")
    a = ap.parse_args(argv)
    if a.version:
        print("lj_core", VERSION)
        return 0
    if not a.act:
        ap.print_help()
        return 1
    try:
        meta = get_in_force(a.act, no_cache=a.no_cache, forma_baza=a.forma_baza, exact=a.exact)
    except RouteBlocked as e:
        print("ROUTE_BLOCKED: HTTPS către %s nu merge din acest mediu (%s).\n"
              "Treci la ruta următoare din SKILL.md (calculatorul utilizatorului / browser)." % (HOST, e),
              file=sys.stderr)
        return 3
    except LookupError as e:
        print(str(e), file=sys.stderr)
        return 6
    if not _has_body(meta["text"]):
        print(header(meta) + "\n[!] Pagina nu conține textul actului.", file=sys.stderr)
        return 5
    if a.json:
        print(json.dumps({k: v for k, v in meta.items() if k != "text"}, ensure_ascii=False, indent=1))
    else:
        print(header(meta))
    if a.articol:
        art = extract_articol(meta["text"], a.articol)
        if art is None:
            print("[!] Articolul %s nu apare în text." % a.articol, file=sys.stderr)
            return 4
        print("\n--- Articolul %s (%s caractere) ---\n%s" % (_norm_ref(a.articol), format(len(art), ","), art))
    elif a.grep:
        print("\n" + (grep(meta["text"], a.grep, a.context) or "(nicio potrivire)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
