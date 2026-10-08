---
name: spanish-jurisprudence-search-edusu
title: CENDOJ jurisprudence search
description: Search Spanish jurisprudence at CENDOJ (Poder Judicial). Use when user asks for a sentencia, jurisprudencia, STSJ, STS, SAP, ATS, ECLI, or ROJ; wants case law on a legal topic; or filters by sala (Civil/Penal/Contencioso/Social/Militar/Especial), comunidad autónoma, fecha, ponente, recurso. Triggers on "busca una sentencia", "jurisprudencia sobre", "encuentra fallos del TSJ", "qué dice el Supremo sobre", "casos de art X ET", "buscar en CENDOJ".
author: edusu
author_url: https://github.com/edusu/spanish-jurisprudence-search
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: litigation
language: en
---

# CENDOJ jurisprudence search

Searches the official Spanish jurisprudence database at `poderjudicial.es/search` using the reverse-engineered Struts/IDOL endpoint. There is **no public REST API** — this skill wraps the internal `search.action` endpoint that the JS frontend uses, handling the wire-format quirks.

## Tooling

`<skill-path>` below is this skill's own base directory, reported when the skill loads. The script sits at its root, so the skill works from whatever location it is installed in — do not hardcode an absolute path.

- **Primary**: `<skill-path>/cendoj_search.py` — pure-stdlib Python script. Bootstraps session, posts query, parses XHTML, returns JSON.
- **Fallback**: when the WAF blocks the script (HTTP 500 / "vuelva a probar dentro de unos minutos"), use `playwright-cli` to drive the UI directly — see "WAF fallback" below.

## When to use it

Trigger on any of these:
- User asks for a sentencia ("busca una sentencia de…", "encuéntrame jurisprudencia sobre…")
- User mentions a tribunal: TS, TSJ, AN, AP, JSO, JCA
- User cites an ECLI or ROJ
- User asks about case law on an article (art. 41 ET, art. 50 ET, art. 1124 CC, etc.)

## Quick usage

```bash
# Basic search
<skill-path>/cendoj_search.py "responsabilidad patrimonial sanitaria"

# Filtered: sala social + Canarias + fechas
<skill-path>/cendoj_search.py "despido nulo víctima violencia género" \
  --jurisdiccion SOCIAL --comunidad CANARIAS \
  --desde 01/01/2023 --hasta 31/12/2024 --per-page 15

# Lookup by exact identifier
<skill-path>/cendoj_search.py "" --ecli "ECLI:ES:TSJICAN:2024:913"
<skill-path>/cendoj_search.py "" --roj "STSJ ICAN 287/2026"

# Pagination (start=1 → 11 → 21 …)
<skill-path>/cendoj_search.py "art 41 ET" --start 11 --per-page 10

# Truncate the `text` field for compact output
<skill-path>/cendoj_search.py "..." --truncate 300
```

Output is JSON to stdout: `{"total": N, "count": M, "items": [...]}`. Each item has `ref`, `db`, `fechares` (YYYYMMDD), `url` (link to the full document), and `text` (extracted résumé / first paragraph).

## Filter values

| Flag | Allowed values |
|---|---|
| `--jurisdiccion` (repeatable) | `CIVIL`, `PENAL`, `CONTENCIOSO`, `SOCIAL`, `MILITAR`, `ESPECIAL` |
| `--comunidad` | `CANARIAS`, `MADRID`, `CATALUÑA`, `ANDALUCÍA`, `ARAGÓN`, `ASTURIAS`, `BALEARES`, `CANTABRIA`, `CASTILLA_LA_MANCHA`, `CASTILLA_Y_LEÓN`, `CEUTA`, `COMUNIDAD_VALENCIANA`, `EXTREMADURA`, `GALICIA`, `LA_RIOJA`, `MELILLA`, `MURCIA`, `NAVARRA`, `PAÍS_VASCO` |
| `--desde` / `--hasta` | `dd/mm/yyyy` |

## Search strategy — IDOL behavior

The backend is **Autonomy IDOL**. Implications for query phrasing:

- **AND across tokens, not OR**: the free-text box requires EVERY token to appear somewhere in the document. `"derrame café caliente pasajero aeronave quemaduras"` returns **zero** hits, while each of those terms alone matches thousands of documents. Build queries **short and add terms**, never long-and-then-trim — three or four high-signal tokens is usually the ceiling.
- **AND is not relevance**: matching every token only means the words co-occur somewhere in the full text, frequently by accident. `"café aeronave"` returns 179 hits that are almost entirely drug-trafficking judgments, where a coffee and an aircraft turn up in unrelated paragraphs. Query the **legal cause**, not the facts (see step 3).
- **Penal vs Social mix**: queries about "violencia de género" return mostly **penal** results unless you filter `--jurisdiccion SOCIAL`. Always set jurisdicción for labor-law topics.
- **Article numbers tokenize weirdly**: `49.1.m` may not match. Better to combine: legal phrase + tribunal + comunidad. Or use `--ecli` / `--roj` for direct lookup.
- **Synonyms matter**: the law and case law don't always use the user's phrasing. Translate first:
  - "incumplimiento grave" → "despido nulo", "extinción a instancia", "rescisión contrato"
  - "víctima de violencia de género" → "trabajadora víctima de violencia", "ejercicio de derechos sociolaborales"
  - "modificación sustancial" → "art 41 ET", "MSCT", "alteración condiciones laborales"
  - "responsabilidad patrimonial" → "indemnización Administración", "art 32 LRJSP"

## Search loop — query, triage, refine, then respond

This skill operates as a **loop, not a single query**. Spanish judicial decisions contain extensive boilerplate: arts. 55.5 ET, 14 CE, 24 CE, 96 LRJS and similar protective rules are recited routinely in nearly every labour dismissal case, regardless of whether the protected ground is actually at issue. A first-pass search on a generic phrase will almost always include such template matches. **Treating those hits as relevant is the single biggest failure mode of this skill** — it leads to confidently telling the user "*here's a case about X*" when the case merely cites the article protecting X while ruling on something else entirely.

The correct workflow runs **before responding to the user**: search → triage → refine and re-search → (optionally fetch a PDF to confirm) → report. Do not stop at the first result set if the hits look like template. Refine and try again yourself; do not just tell the user to refine.

Budget: at most **2–3 refinement passes** per user request. The WAF starts blocking around 5 rapid requests, so a typical loop is initial + 1–2 refinements + maybe one PDF fetch. Stay inside that envelope.

### Step 1: First pass

Start with **three or four high-signal tokens** plus the obvious filters (jurisdicción, comunidad, fechas). Because the box ANDs its tokens, opening with a long descriptive sentence is the single most reliable way to get zero hits — don't. Goal: gauge total hits and what's actually in the database.

- Zero hits → you almost certainly used too many tokens. Cut to the two or three that carry the legal meaning, then add terms back one at a time.
- Too many penal hits for a labour-law topic → add `--jurisdiccion SOCIAL` (or the matching sala) and retry.
- Many hits but visibly off-topic → the tokens are co-occurring incidentally; switch from fact words to the statutory or doctrinal name of the cause.

### Step 2: Triage — template vs substance

The `text` field is IDOL's auto-extracted résumé. For each candidate hit, ask whether the snippet describes **the case** (hechos, fundamentos, fallo) or merely **names statutes**.

- ❌ Template: *"…el art. 55.5 ET considera nulo el despido de personas trabajadoras víctimas de violencia de género o sexual por el ejercicio de su derecho a la tutela judicial efectiva…"* — recitation of the legal regime. The article was cited; the case is not necessarily about it.
- ✅ Substantive: *"…la actora acreditó su condición de víctima de violencia de género mediante orden de protección de fecha…, y fue despedida tras solicitar la reducción de jornada prevista en el art. 37.8 ET…"* — the protected ground is a fact of the case and the dispute turns on it.

- ❌ Incidental: the query words are all present but scattered across unrelated passages — a drug-trafficking judgment that happens to mention a *café* in one paragraph and an *aeronave* in another. This is distinct from template matching: template noise is boilerplate *law*, incidental noise is boilerplate *narrative*. The tell is a RESUMEN naming a completely different subject matter from the one you asked about.

Substantive engagement appears in hechos probados ("*la trabajadora ostentaba la condición de…*"), in fundamentos jurídicos that analyse the cause *as applied* to this case, or in the case's own headnote (the "RESUMEN" field — distinct from the "Resumen Automático" IDOL extracts). Keywords buried inside a long list of statutory citations are the strongest signal of boilerplate.

If a snippet leaves you genuinely uncertain whether the case is substantive or template — and the case is otherwise a strong candidate — **fetch the PDF** (`url` field, see "Document fetch" below) and read the fundamentos jurídicos. Two minutes of reading is cheaper than misleading the user. Do not, however, fetch PDFs for every hit; use this for the 1–2 borderline candidates that would change your answer.

### Step 3: If hits are weak, refine and re-search yourself

Generic queries ("violencia de género", "despido nulo") match every case that *mentions* the rule. If the triage in step 2 reveals all or most hits are template, **issue a second search yourself** — do not stop and recommend the user run one. The right refinement is to query the **literal phrasing of the article that creates the specific cause of action** the user is asking about:

| Cause | Article | Better query |
|---|---|---|
| Extinción a instancia de la trabajadora víctima | art. 49.1.m ET | `"abandono definitivo puesto trabajo víctima violencia género"` |
| Nulidad del despido por ejercicio de derechos | art. 55.5.b ET | `"despido nulo ejercicio derechos reducción jornada víctima"` |
| Cómputo de ausencias derivadas de violencia | art. 52.d ET | `"ausencias justificadas víctima violencia género no computables"` |
| Reducción / reordenación de jornada | art. 37.8 ET | `"reducción jornada víctima violencia género horario flexible"` |

The table is illustrative, not exhaustive — for any cause of action, the principle is: pick the article that creates the cause, then query phrases that would appear in the *ratio* of a case applying it, not phrases that appear in routine recitations of the protective regime. Article numbers tokenise unreliably in IDOL (`49.1.m` is not one token), so combining a literal statutory phrase with a tribunal/comunidad filter outperforms `"art 49.1.m ET"` alone.

If the user's request doesn't map cleanly to one article, pick the closest cause and run the refined search. You can chain: if refinement on art. 55.5.b still yields template, try art. 49.1.m. Stop after **2–3 refinements** (WAF budget) and report.

### Step 4: Report — including the "nothing relevant found" outcome

After the loop, report honestly. Three outcomes:

1. **Found substantively relevant cases.** List them with ECLI/ROJ, fecha, ponente and one line on what makes them on-point. Note which search yielded them ("*found via refined query on art. 49.1.m ET phrasing*").

2. **Found tangential cases but nothing directly on the cause.** Name them as tangential, do not dress them up. E.g.: "*STSJ X menciona la protección como bloque legal pero el despido se resuelve en otro motivo. No es jurisprudencia sobre la causa solicitada.*"

3. **Nothing relevant after refinement.** **Say so explicitly.** Example:

   > *"Ejecuté 3 búsquedas: inicial `<q1>` (95 hits, todos cita template del art. 55.5 ET), refinada con art. 49.1.m `<q2>` (12 hits, 1 tangencial), refinada con art. 37.8 `<q3>` (0 hits). No he encontrado jurisprudencia del TSJ de Canarias que resuelva sobre la causa solicitada en el rango de fechas indicado. El caso más próximo es STSJ X, pero ruled on Y, no on the gender-violence ground. Posibles siguientes pasos: ampliar a otra comunidad, otro rango, o consultar la Sala Cuarta del TS."*

   A clean "no result found, here is what I tried" is far more useful than a list of impressive-looking citations that don't answer the question. Hiding the absence behind boilerplate matches is the failure mode this loop exists to prevent.

## WAF / rate-limit awareness

> [!warning]
> The portal has an aggressive WAF. After ~5 rapid requests from the same IP it returns HTTP 500 with the page "*Vuelva a probar dentro de unos minutos*". The script reports this as `{"error": "server_error_or_waf"}`.

Mitigations baked into the script:
- Realistic Chrome User-Agent
- Proper `X-Requested-With`, `Accept`, `Referer` headers
- Sleep `--delay 0.5` (default) between bootstrap and search
- Stdlib `urllib` with cookie jar to maintain JSESSIONID with sticky `.sidolappNN` suffix

If blocked:
1. Wait 3–5 minutes and retry.
2. If still blocked, switch to **playwright-cli fallback** (driving the UI in a real browser bypasses WAF fingerprinting since requests carry the browser's TLS/JA3 signature).

## WAF fallback — playwright-cli

When the script returns `server_error_or_waf` repeatedly, use `playwright-cli` to drive the UI:

```bash
playwright-cli open https://www.poderjudicial.es/search/indexAN.jsp
# Force-close the legal modal (more reliable than clicking ×):
playwright-cli eval "() => { document.getElementById('modalAvisoLegal')?.remove(); document.body.classList.remove('modal-open'); document.querySelector('.modal-backdrop')?.remove(); return 'ok'; }"

# Type query
playwright-cli fill "#frmBusquedajurisprudencia_TEXT" "your query here"

# Tag the Jurisdicción button (it has no stable id):
playwright-cli eval "() => { const sel=document.getElementById('frmBusquedajurisprudencia_JURISDICCION'); let p=sel.parentElement; while(p){ const b=p.querySelector('button.multiselect.dropdown-toggle'); if(b){b.id='__jurisbtn__'; break;} p=p.parentElement; } return 'tagged'; }"
playwright-cli click "#__jurisbtn__"
playwright-cli click "input[type=checkbox][value=SOCIAL]"
playwright-cli click "#__jurisbtn__"

# Comunidad (Las Palmas / Tenerife both via CANARIAS):
playwright-cli click "#COMUNIDADmultiselec"
playwright-cli click "#chkCOM_CANARIAS"
playwright-cli click "#COMUNIDADmultiselec"

# Capture the XHR before clicking Buscar:
playwright-cli eval "() => { window.__log=[]; const O=window.XMLHttpRequest; function P(){const x=new O(); let _u,_b; const op=x.open; x.open=function(m,u){_u=u;return op.apply(x,arguments);}; const sn=x.send; x.send=function(b){_b=b; x.addEventListener('loadend',()=>window.__log.push({url:_u,body:_b?String(_b):null,resp:x.responseText||''})); return sn.apply(x,arguments);}; return x;} P.prototype=O.prototype; window.XMLHttpRequest=P; return 'ok'; }"
playwright-cli click "#srcjur_search"

# Read the parsed results:
playwright-cli eval "() => { const e=(window.__log||[]).find(x=>x.url&&x.url.includes('search.action')); if(!e) return 'no-call'; const doc=new DOMParser().parseFromString(e.resp,'text/html'); const total=doc.querySelector('[data-totalhits]')?.getAttribute('data-totalhits'); const items=[...doc.querySelectorAll('div.row.searchresult.doc')].slice(0,15).map(el=>({ref:el.getAttribute('data-ref'),db:el.getAttribute('data-db'),fechares:el.getAttribute('data-fechares'),url:el.querySelector('a[data-link]')?.getAttribute('data-link'),text:el.innerText.replace(/\\s+/g,' ').trim().slice(0,800)})); return {total, items}; }"
```

## Document fetch

To get the full text of a document, follow the `url` field. It serves a PDF (`content-type: application/pdf`).

> [!warning]
> **`curl` does not work**, even with a browser User-Agent. The endpoint is session-bound, so a bare request returns an HTML error page that `curl -o sentencia.pdf` happily saves under a `.pdf` name — `file` reports "HTML document" and any PDF parser then fails on a file that looks superficially fine. Always check the magic bytes are `%PDF-`.

Fetch from the **page context of the playwright session** that ran the search, which carries the cookies. Base64 the bytes, dump to a file, and decode — never let the base64 hit your context window:

```bash
OUT=/tmp/cendoj   # scratch dir
U="<url-from-result>"
playwright-cli eval "async () => { const r=await fetch('$U',{credentials:'include'}); const b=new Uint8Array(await r.arrayBuffer()); let s=''; for(let i=0;i<b.length;i++) s+=String.fromCharCode(b[i]); return btoa(s); }" > "$OUT/raw.txt" 2>&1

python3 - "$OUT" <<'EOF'
import re, sys, base64, pathlib
out = pathlib.Path(sys.argv[1])
m = re.search(r'"([A-Za-z0-9+/=]{500,})"', (out / 'raw.txt').read_text())
if not m:
    print('NO BASE64 FOUND'); sys.exit(1)
d = base64.b64decode(m.group(1))
(out / 'sent.pdf').write_bytes(d)
print('bytes', len(d), 'magic', d[:5])
EOF

pdftotext "$OUT/sent.pdf" "$OUT/sent.txt"
```

Then grep `sent.txt` for the fact keywords and read the fundamentos jurídicos. The `>` redirect matters: a judgment is ~130 KB, so the base64 is ~180 KB of noise you must keep out of the transcript.

The URL pattern is `/search/AN/openDocument/<UUID32>/<YYYYMMDD>` where the trailing date is the **optimization date** (when IDOL indexed it), NOT the resolution date — that one is in `data-fechares`.

## Wire-format gotchas (already handled by the script — for reference)

If you ever need to call the API directly from another tool, watch out for:

| Quirk | What works | What breaks |
|---|---|---|
| Spaces in body | `+` (form-urlencoded) | `%20` → "búsqueda no es válida" |
| Parens in `VALUESCOMUNIDAD` | `CANARIAS(C)` literal | `CANARIAS%28C%29` → rejected |
| `JURISDICCION` multi-value | `\|SOCIAL\|` (pipe-wrapped) | `SOCIAL` (bare) → no filter applied silently |
| `VALUESCOMUNIDAD` value | `CANARIAS(C) \| ` (with `(C)` + trailing pipe + space) | `ALL@ALL@CANARIAS` (the HTML form `value`) → rejected |
| Sticky session | `JSESSIONID=...sidolapp01..04` (suffix is sticky) | strip suffix → server can't find session, 500 |
| Bootstrap | always `GET /search/indexAN.jsp` first | direct POST without prior GET → 403 |

## Legal context

> [!quote] Aviso legal del portal
> "No está permitida la utilización de la base de datos para usos comerciales, ni la descarga masiva de información. La reutilización de esta información para la elaboración de bases de datos o con fines comerciales debe seguir el procedimiento y las condiciones establecidas por el CGPJ a través de su Centro de Documentación Judicial."

- Personal/educational consultation: **OK**.
- Building a derived database / commercial reuse: **needs licence** from CENDOJ (procedure under art. 560.1.10º LOPJ).
- Mass downloading: **prohibited** — and the WAF enforces it technically.

This skill is for **personal queries**, not bulk extraction. Don't loop over thousands of results.

## See also

Full reverse-engineering writeup with code samples (Python and Rust) lives in the user's vault:

```
/Users/edusu/Obsidian/research/tech/cendoj-api-jurisprudencia.md
```
