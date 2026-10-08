#!/usr/bin/env python3
"""Vigilancia semanal del portal de normativa educativa del Gobierno de Canarias.

Escanea las páginas oficiales vigiladas (FTE-001 y normativa clasificada
FTE-013/014/015, leídas de ``06_indices/fuentes.yaml``), extrae los enlaces a
normas/documentos, los compara contra lo ya catalogado en los índices del corpus
y contra un snapshot de URLs ya vistas, y reporta solo las **novedades**.

No crea fichas normativas ni afirma vigencia: únicamente señala URLs nuevas y,
opcionalmente, descarga los PDFs detectados a ``input/`` para que DocDigester2MD
los convierta a Markdown. La catalogación final es siempre supervisada
(AGENTS.md §7–§8).

Uso típico:
    python3 scan_normativa.py --dry-run          # no escribe nada, solo lista
    python3 scan_normativa.py                    # actualiza snapshot + descargas
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import logging
import pathlib
import re
import sys
from urllib.parse import urljoin, urlparse, urlunparse

import requests
import yaml
from bs4 import BeautifulSoup

# --- Rutas relativas a la raíz del repositorio ---------------------------------
REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
INDICES_DIR = REPO_ROOT / "06_indices"
DEFAULT_SNAPSHOT = (
    REPO_ROOT / "11_calidad" / "monitor" / "portal-normativa-canaria.seen.json"
)
DEFAULT_INPUT_DIR = REPO_ROOT / "input"

# FTE cuyo url_oficial se vigila (solo portal de normativa de Canarias).
DEFAULT_WATCH_IDS = ["FTE-001", "FTE-013", "FTE-014", "FTE-015"]

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36 "
    "normativa-canaria-monitor/1.0"
)
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3

logging.basicConfig(
    level=logging.INFO, format="%(levelname)s %(message)s", stream=sys.stderr
)
log = logging.getLogger("monitor")


# --- Utilidades ----------------------------------------------------------------
def normalize_url(url: str) -> str:
    """Normaliza una URL para comparar: host en minúsculas, sin fragmento ni
    barra final redundante."""
    try:
        p = urlparse(url.strip())
    except ValueError:
        return url.strip()
    if not p.scheme:
        return url.strip()
    netloc = p.netloc.lower()
    path = p.path.rstrip("/") or "/"
    return urlunparse((p.scheme.lower(), netloc, path, "", p.query, ""))


def is_relevant(url: str, base_host: str) -> bool:
    """¿El enlace apunta a normativa/documento de interés y no a ruido de menú?"""
    low = url.lower()
    if low.endswith(".pdf"):
        return True
    host = urlparse(low).netloc
    if any(d in host for d in ("boe.es", "gobiernodecanarias.org", "gobcan")):
        # Solo secciones de normativa o boletines, no la home ni assets.
        if "/servicios/normativa/" in low or "normativa_clasificada" in low:
            return True
        if "boe.es/" in low and ("boe-a-" in low or "/buscar/" in low):
            return True
        if "sede" in host or "/boc/" in low:
            return True
    return False


def sanitize_filename(url: str) -> str:
    name = pathlib.Path(urlparse(url).path).name or "documento"
    name = re.sub(r"[^A-Za-z0-9._-]+", "-", name).strip("-")
    if not name.lower().endswith(".pdf"):
        name += ".pdf"
    return name[:120]


def fetch(url: str) -> str | None:
    """Descarga el HTML de una página; devuelve None si falla tras reintentos."""
    headers = {"User-Agent": USER_AGENT, "Accept-Language": "es-ES,es;q=0.9"}
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
            r.raise_for_status()
            r.encoding = r.apparent_encoding or r.encoding
            return r.text
        except requests.RequestException as exc:
            log.warning("Intento %d/%d falló para %s: %s", attempt, MAX_RETRIES, url, exc)
    return None


# --- Carga de índices y snapshot ----------------------------------------------
def load_yaml(path: pathlib.Path) -> dict:
    if not path.exists():
        return {}
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        log.error("No se pudo parsear %s: %s", path, exc)
        return {}


def collect_catalogued_urls(indices_dir: pathlib.Path) -> set[str]:
    """Reúne todas las url_oficial ya conocidas en los índices del corpus."""
    urls: set[str] = set()
    for fname in ("fuentes.yaml", "normativa.yaml", "textos-oficiales.yaml"):
        data = load_yaml(indices_dir / fname)
        for value in _iter_url_strings(data):
            urls.add(normalize_url(value))
    return urls


def _iter_url_strings(node) -> list[str]:
    found: list[str] = []
    if isinstance(node, dict):
        for k, v in node.items():
            if isinstance(v, str) and ("url" in str(k).lower()) and v.startswith("http"):
                found.append(v)
            else:
                found.extend(_iter_url_strings(v))
    elif isinstance(node, list):
        for item in node:
            found.extend(_iter_url_strings(item))
    elif isinstance(node, str) and node.startswith("http"):
        found.append(node)
    return found


def watch_urls(indices_dir: pathlib.Path, watch_ids: list[str]) -> list[str]:
    fuentes = load_yaml(indices_dir / "fuentes.yaml")
    urls = []
    for fid in watch_ids:
        entry = fuentes.get(fid)
        if entry and entry.get("url_oficial"):
            urls.append(entry["url_oficial"])
        else:
            log.warning("No se encontró url_oficial para %s en fuentes.yaml", fid)
    return urls


def extract_links(html: str, page_url: str) -> list[tuple[str, str]]:
    """Devuelve [(url_absoluta, texto)] de enlaces relevantes."""
    soup = BeautifulSoup(html, "html.parser")
    base_host = urlparse(page_url).netloc
    out: list[tuple[str, str]] = []
    for a in soup.find_all("a", href=True):
        href = urljoin(page_url, a["href"].strip())
        if not href.startswith("http"):
            continue
        if is_relevant(href, base_host):
            text = " ".join(a.get_text(" ", strip=True).split())[:200]
            out.append((href, text or "(sin título)"))
    return out


def download_pdf(url: str, dest_dir: pathlib.Path) -> str | None:
    dest_dir.mkdir(parents=True, exist_ok=True)
    fname = sanitize_filename(url)
    dest = dest_dir / fname
    headers = {"User-Agent": USER_AGENT}
    try:
        with requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT, stream=True) as r:
            r.raise_for_status()
            ctype = r.headers.get("Content-Type", "")
            if "pdf" not in ctype.lower() and not url.lower().endswith(".pdf"):
                log.info("Se omite descarga (no es PDF): %s [%s]", url, ctype)
                return None
            with open(dest, "wb") as fh:
                for chunk in r.iter_content(chunk_size=65536):
                    fh.write(chunk)
        log.info("Descargado %s -> %s", url, dest.name)
        return str(dest.relative_to(REPO_ROOT))
    except requests.RequestException as exc:
        log.warning("No se pudo descargar %s: %s", url, exc)
        return None


# --- Reporte -------------------------------------------------------------------
def render_markdown(nuevas: list[dict], fecha: str) -> str:
    lines = [
        f"# Novedades de normativa educativa canaria — {fecha}",
        "",
        "> Detección automática del portal oficial (FTE-001 + normativa clasificada).",
        "> **No sustituye la fuente oficial** ni confirma vigencia: requiere catalogación",
        "> supervisada siguiendo `AGENTS.md` §7–§8 y el skill `catalogacion-fuentes`.",
        "",
        f"Se han detectado **{len(nuevas)}** entrada(s) nueva(s):",
        "",
        "| Título | URL oficial | PDF descargado |",
        "| --- | --- | --- |",
    ]
    for item in nuevas:
        pdf = item.get("descarga") or "—"
        titulo = (item.get("titulo") or "(sin título)").replace("|", "\\|")
        lines.append(f"| {titulo} | {item['url']} | {pdf} |")
    lines += [
        "",
        "## Checklist de catalogación (por entrada)",
        "",
        "- [ ] Confirmar fuente oficial y registrar fecha de consulta (R4).",
        "- [ ] Decidir si es nueva fuente (`FTE-NNN`) y/o nueva norma (`NOR-NNN`).",
        "- [ ] Verificar estado de vigencia en fuente oficial (R3).",
        "- [ ] Crear ficha desde `10_plantillas/` y actualizar índices YAML (R11).",
        "- [ ] Registrar relaciones (`REL-NNN`) si aplica y dudas como `PREG-NNN`.",
        "- [ ] Anotar el cierre en el diario (`08_tareas/diario/`).",
        "",
        "Los borradores de texto convertidos (si los hay) están en "
        "`07_corpus_ia/_borradores-monitor/` y son **material no validado**.",
    ]
    return "\n".join(lines) + "\n"


# --- Main ----------------------------------------------------------------------
# --- Deuda de catalogación -----------------------------------------------------
IDENTIFICADOR = re.compile(r"(boc-a-\d{4}-\d{3}-\d+|boe-a-\d{4}-\d+)", re.I)
DISPOSICION_BOC = re.compile(r"boc-a-\d{4}-\d{3}-\d+\.pdf|/boc/\d{4}/\d{3}/\d+\.html", re.I)


def identificador(url: str) -> str | None:
    """Identificador oficial de la disposición (CVE del BOC o BOE-A), si lo tiene.

    Comparar URL contra URL no basta: la misma disposición aparece como PDF de la
    sede, como HTML del boletín y como texto consolidado, y el corpus guarda sólo
    una de esas formas. El identificador es el mismo en las tres.
    """
    encontrado = IDENTIFICADOR.search(url)
    return encontrado.group(1).lower() if encontrado else None


POSICIONAL_BOC = re.compile(r"gobiernodecanarias\.org/boc/(\d{4})/(\d{3})/(\d{1,4})\.html", re.I)
_CVE_POR_POSICION: dict[tuple[str, str, str], str | None] = {}


def cve_de_url_posicional(url: str) -> str | None:
    """Resuelve el CVE de una URL del BOC que sólo lleva la posición en el boletín.

    Hasta 2024 el último tramo de la URL era la posición de la disposición dentro
    del boletín, no su número, así que la URL no contiene el identificador. Se lee
    del sumario, que sí lo publica.
    """
    encontrada = POSICIONAL_BOC.search(url)
    if not encontrada:
        return None
    anio, boletin, tramo = encontrada.groups()
    clave = (anio, boletin, tramo)
    if clave in _CVE_POR_POSICION:
        return _CVE_POR_POSICION[clave]
    html = fetch(f"https://www.gobiernodecanarias.org/boc/{anio}/{boletin}/index.html")
    cve = None
    if html:
        cves = re.findall(rf"BOC-A-{anio}-{boletin}-(\d+)", html)
        # el sumario repite cada CVE varias veces; interesa el orden de aparición
        vistos: list[str] = []
        for c in cves:
            if c not in vistos:
                vistos.append(c)
        posicion = int(tramo)
        if str(posicion) in vistos:            # esquema nuevo: el tramo ES el número
            cve = f"boc-a-{anio}-{boletin}-{posicion}"
        elif 1 <= posicion <= len(vistos):     # esquema antiguo: el tramo es la posición
            cve = f"boc-a-{anio}-{boletin}-{vistos[posicion - 1]}"
    _CVE_POR_POSICION[clave] = cve
    return cve


def rastro_en_corpus(url: str, corpus: str, catalogadas: set[str]) -> bool:
    ident = identificador(url) or cve_de_url_posicional(url)
    if ident:
        return ident in corpus
    return normalize_url(url) in catalogadas


def texto_del_corpus(repo: pathlib.Path) -> str:
    """Las fichas que constituyen catalogación, más los índices, en minúsculas.

    Se limita a fuentes, normativa, currículos e índices a propósito. Si se
    incluyeran tareas o diario, bastaría con **mencionar** el identificador de una
    disposición pendiente para que se contara como catalogada, que es justo lo
    contrario de lo que este informe debe detectar.
    """
    partes = []
    for patron in ("01_fuentes/**/*.md", "02_normativa/**/*.md",
                   "03_curriculos/**/*.md", "03_curriculos/**/*.yaml",
                   "05_relaciones/**/*.yaml", "06_indices/*.yaml"):
        for fichero in repo.glob(patron):
            try:
                partes.append(fichero.read_text(encoding="utf-8", errors="replace"))
            except OSError:
                continue
    return "\n".join(partes).lower()


def clasificar(url: str) -> str:
    if DISPOSICION_BOC.search(url):
        return "disposicion-boc"
    if "boe.es" in url.lower():
        return "disposicion-boe"
    if url.lower().endswith(".pdf"):
        return "pdf-consejeria"
    return "pagina-portal"


DESCARTADOS = pathlib.Path(__file__).resolve().parent / "descartados.yaml"


def exclusiones() -> dict[str, str]:
    """URL detectadas que NO procede catalogar, con su motivo (DEC-0012)."""
    datos = load_yaml(DESCARTADOS)
    return {normalize_url(u): (v or {}).get("motivo", "") for u, v in (datos.get("descartados") or {}).items()}


def informe_pendientes(snapshot: dict, indices_dir: pathlib.Path, repo: pathlib.Path) -> int:
    """Lista las URL del snapshot que siguen sin rastro en el corpus.

    El snapshot silencia una URL en cuanto se ve una vez, así que una disposición
    detectada y nunca catalogada desaparece del radar para siempre. Este modo
    convierte esa deuda silenciosa en un informe.
    """
    corpus = texto_del_corpus(repo)
    catalogadas = collect_catalogued_urls(indices_dir)
    descartadas = exclusiones()
    grupos: dict[str, list[tuple[str, str]]] = {
        "disposicion-boc": [], "disposicion-boe": [], "pdf-consejeria": [], "pagina-portal": [],
    }
    excluidas: list[tuple[str, str]] = []
    for url, fecha in sorted(snapshot.items(), key=lambda par: (par[1], par[0])):
        if rastro_en_corpus(url, corpus, catalogadas):
            continue
        motivo = descartadas.get(normalize_url(url))
        if motivo is not None:
            excluidas.append((url, motivo))
            continue
        grupos[clasificar(url)].append((fecha, url))

    total = sum(len(v) for v in grupos.values())
    print(f"{len(snapshot)} URL en el snapshot · {total} sin rastro en el corpus\n")
    ROTULOS = {
        "disposicion-boc": "Disposiciones del BOC sin catalogar",
        "disposicion-boe": "Disposiciones del BOE sin catalogar",
        "pdf-consejeria": "PDF de la Consejería sin catalogar",
        "pagina-portal": "Páginas de portal (no son normas; no requieren ficha)",
    }
    for clave, entradas in grupos.items():
        print(f"## {ROTULOS[clave]}: {len(entradas)}")
        for fecha, url in entradas:
            print(f"  {fecha}  {url}")
        print()
    if excluidas:
        print(f"## Descartadas con motivo escrito (DEC-0012): {len(excluidas)}")
        for url, motivo in excluidas:
            print(f"  {url}\n      {motivo}")
        print()
    # Sólo las disposiciones son deuda real; las páginas de portal son navegación y
    # las descartadas tienen ya una decisión editorial escrita.
    return 1 if (grupos["disposicion-boc"] or grupos["disposicion-boe"]) else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true",
                    help="No escribe snapshot ni descarga; solo lista candidatas.")
    ap.add_argument("--seed", action="store_true",
                    help="Inicializa el snapshot con TODAS las candidatas actuales "
                         "(sin descargas ni PR), para no reportar el baseline.")
    ap.add_argument("--pendientes", action="store_true",
                    help="Lista las URL ya vistas que siguen sin rastro en el corpus "
                         "y termina, sin escanear el portal.")
    ap.add_argument("--snapshot", type=pathlib.Path, default=DEFAULT_SNAPSHOT)
    ap.add_argument("--indices", type=pathlib.Path, default=INDICES_DIR)
    ap.add_argument("--input-dir", type=pathlib.Path, default=DEFAULT_INPUT_DIR,
                    help="Carpeta donde dejar los PDFs para DocDigester2MD.")
    ap.add_argument("--watch-ids", nargs="*", default=DEFAULT_WATCH_IDS)
    ap.add_argument("--max-downloads", type=int, default=20)
    ap.add_argument("--nuevas-json", type=pathlib.Path,
                    default=REPO_ROOT / "11_calidad" / "monitor" / "nuevas.json")
    ap.add_argument("--output", type=pathlib.Path,
                    default=REPO_ROOT / "11_calidad" / "monitor" / "nuevas.md")
    args = ap.parse_args()

    if args.pendientes:
        return informe_pendientes(
            load_yaml_json(args.snapshot), args.indices, REPO_ROOT
        )

    fecha = dt.date.today().isoformat()
    pages = watch_urls(args.indices, args.watch_ids)
    if not pages:
        log.error("No hay páginas que vigilar; abortando.")
        return 1

    catalogued = collect_catalogued_urls(args.indices)
    snapshot: dict = load_yaml_json(args.snapshot)
    seen = {normalize_url(u) for u in snapshot.keys()}

    candidates: dict[str, str] = {}  # url_norm -> titulo
    failures = 0
    for page in pages:
        html = fetch(page)
        if html is None:
            failures += 1
            continue
        for url, text in extract_links(html, page):
            norm = normalize_url(url)
            candidates.setdefault(norm, text)

    if failures == len(pages):
        log.error("Fallaron todas las páginas vigiladas; abortando sin cambios.")
        return 1

    # Se compara por identificador oficial además de por URL: la misma disposición
    # se publica como PDF de la sede, como HTML del boletín y como consolidado, y el
    # corpus guarda sólo una de esas formas.
    corpus = texto_del_corpus(REPO_ROOT)
    nuevas_urls = [
        u for u in candidates
        if u not in seen and not rastro_en_corpus(u, corpus, catalogued)
    ]
    log.info("Candidatas: %d | catalogadas: %d | ya vistas: %d | nuevas: %d",
             len(candidates), len(catalogued), len(seen), len(nuevas_urls))

    if args.seed:
        for u in nuevas_urls:
            snapshot[u] = fecha
        args.snapshot.parent.mkdir(parents=True, exist_ok=True)
        args.snapshot.write_text(
            json.dumps(snapshot, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        log.info("Snapshot inicializado con %d URLs (baseline). No se abre PR.",
                 len(nuevas_urls))
        return 0

    nuevas: list[dict] = []
    downloads = 0
    for url in sorted(nuevas_urls):
        item = {"url": url, "titulo": candidates[url], "detectada": fecha}
        if (not args.dry_run) and url.lower().endswith(".pdf") and downloads < args.max_downloads:
            rel = download_pdf(url, args.input_dir)
            if rel:
                item["descarga"] = rel
                downloads += 1
        nuevas.append(item)

    if args.dry_run:
        for item in nuevas:
            print(f"NUEVA  {item['url']}  — {item['titulo']}")
        print(f"\nTotal nuevas: {len(nuevas)} (dry-run, sin cambios)")
        return 0

    if not nuevas:
        log.info("Sin novedades. No se abre PR.")
        # Limpia artefactos previos para que el workflow no abra PR vacío.
        for p in (args.nuevas_json, args.output):
            if p.exists():
                p.unlink()
        return 0

    # Actualiza snapshot con las nuevas (URL -> fecha de primera detección).
    for item in nuevas:
        snapshot[item["url"]] = item["detectada"]
    args.snapshot.parent.mkdir(parents=True, exist_ok=True)
    args.snapshot.write_text(
        json.dumps(snapshot, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    args.nuevas_json.write_text(
        json.dumps(nuevas, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    args.output.write_text(render_markdown(nuevas, fecha), encoding="utf-8")
    log.info("Escritos %s y %s; snapshot actualizado.", args.nuevas_json.name, args.output.name)
    return 0


def load_yaml_json(path: pathlib.Path) -> dict:
    """El snapshot es JSON, pero YAML lo parsea igualmente; tolera ausencia."""
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8") or "{}")
    except json.JSONDecodeError as exc:
        log.error("Snapshot corrupto %s: %s", path, exc)
        return {}


if __name__ == "__main__":
    raise SystemExit(main())
