#!/usr/bin/env python3
"""Re-exporta una copia local de texto oficial desde el PDF firmado del boletín.

Motivo (TAREA-084): las copias locales existentes se generaron desde la versión HTML
del BOC apuntando a un ordinal dentro del boletín (`/boc/AAAA/NNN/001.html`) en lugar
de a la disposición concreta. Cuando el ordinal no correspondía, el fichero acabó
conteniendo otra norma; y la versión HTML omite además los anexos publicados como
imagen, que en algunas normas *son* la norma.

Este script resuelve las dos cosas a la vez: localiza la disposición en el sumario del
boletín contrastando su título, y extrae el texto del **PDF oficial firmado**, que sí
incluye los anexos.

Uso:

    python3 11_calidad/reexportar_texto_oficial.py NOR-044            # sólo diagnostica
    python3 11_calidad/reexportar_texto_oficial.py NOR-044 --aplicar  # reescribe
    python3 11_calidad/reexportar_texto_oficial.py --marcadas         # todas las marcadas
    python3 11_calidad/reexportar_texto_oficial.py --auditar          # revisa las URL de todas las NOR

Requiere `pdftotext` (paquete poppler) en el PATH.
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import subprocess
import sys
import tempfile
import unicodedata
import urllib.request

RAIZ = pathlib.Path(__file__).resolve().parent.parent
TEXTOS = RAIZ / "07_corpus_ia" / "textos-completos"

BOC_BOLETIN = re.compile(r"gobiernodecanarias\.org/boc/(\d{4})/(\d{3})/")
# Los boletines han usado tres marcados distintos para la misma lista de disposiciones.
ENTRADA_BOC = re.compile(r'<li class="justificado(?:_boc)?">(.*?)</li>', re.S)
# Los boletines recientes enlazan el PDF firmado en la sede; los anteriores a 2011
# lo sirven como ruta relativa dentro del propio boletín.
PDF_BOC = re.compile(
    r'href="(https://sede\.gobiernodecanarias\.org/boc/boc-a-[\d-]+\.pdf'
    r'|/boc/\d{4}/\d{3}/boc-\d{4}-\d{3}-\d{3}\.pdf)"'
)
CVE_BOC = re.compile(r"(BOC-A-\d{4}-\d{3}-\d+)")
ORDINAL_BOC = re.compile(r"Ir a la disposición (\d{4}/\d{3}/\d{3})")
VACIAS = {
    "de", "la", "el", "los", "las", "por", "que", "se", "y", "en", "del", "a", "al",
    "con", "para", "un", "una", "su", "sus", "e", "o", "u", "lo",
}


def sin_acentos(texto: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn"
    )


def fichas(texto: str) -> set[str]:
    """Palabras significativas de un título, para contrastar sumario contra cabecera."""
    limpio = sin_acentos(texto.lower())
    return {p for p in re.findall(r"[a-z0-9]+", limpio) if p not in VACIAS and len(p) > 1}


def descargar(url: str) -> bytes:
    peticion = urllib.request.Request(url, headers={"User-Agent": "normativa-educativa-canaria/1.0"})
    with urllib.request.urlopen(peticion, timeout=90) as respuesta:
        return respuesta.read()


def sin_marcas(texto: str) -> str:
    return re.sub(r"<[^>]+>", " ", texto).replace("&nbsp;", " ")


def disposiciones_del_boletin(anio: str, numero: str) -> list[dict]:
    """Devuelve las disposiciones del sumario con su PDF, su CVE y su título."""
    html = descargar(
        f"https://www.gobiernodecanarias.org/boc/{anio}/{numero}/index.html"
    ).decode("utf-8", errors="replace")
    salida = []
    for bruto in ENTRADA_BOC.findall(html):
        pdf = PDF_BOC.search(bruto)
        if not pdf:
            continue
        enlace = pdf.group(1)
        if enlace.startswith("/"):
            enlace = "https://www.gobiernodecanarias.org" + enlace
        cve = CVE_BOC.search(bruto)
        ordinal = ORDINAL_BOC.search(bruto)
        # El título es el texto de los enlaces, sin el número de disposición ni el
        # rótulo [PDF] que los boletines antiguos añaden al final.
        cuerpo = bruto.split('<div class="document_info">')[0]
        cuerpo = re.sub(r"\[\s*<a[^>]*>PDF</a>\s*\]", " ", cuerpo)
        titulo = re.sub(r"\s+", " ", sin_marcas(cuerpo)).strip()
        titulo = re.sub(r"^\d+\s+", "", titulo)
        salida.append(
            {
                "posicion": len(salida) + 1,
                "pdf": enlace,
                "cve": cve.group(1) if cve else pathlib.Path(enlace).stem.upper(),
                "ordinal": ordinal.group(1) if ordinal else None,
                "titulo": titulo,
            }
        )
    return salida


BOLETIN_DEL_ANIO = re.compile(r'href="/boc/(\d{4})/(\d{3})/')
TITULO_BOLETIN = re.compile(
    r"<TITLE>\s*BOC\s*-\s*\d{4}/\d{1,4}\.\s*\w+\s+(\d{1,2})\s+de\s+([A-Za-záéíóúÁÉÍÓÚ]+)\s+de\s+(\d{4})",
    re.I | re.S,
)
MESES = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
    "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11,
    "diciembre": 12,
}
FECHA_EN_TITULO = re.compile(r"\b(\d{1,2}) de ([a-záéíóú]+) de (\d{4})\b", re.I)


def numeros_del_anio(anio: int) -> list[str]:
    """Números de boletín publicados en un año, en orden.

    El índice anual ha cambiado de marcado tres veces y sólo en algunos años lleva la
    fecha, así que aquí sólo se recogen los números y la fecha se lee después del
    propio boletín, que sí la publica de forma estable en su `<title>`.
    """
    try:
        html = descargar(
            f"https://www.gobiernodecanarias.org/boc/{anio}/index.html"
        ).decode("utf-8", errors="replace")
    except Exception:  # noqa: BLE001 — un año sin archivo no debe abortar la búsqueda
        return []
    return sorted({n for a, n in BOLETIN_DEL_ANIO.findall(html) if a == str(anio)})


_FECHAS: dict[tuple[int, str], str] = {}


def fecha_del_boletin(anio: int, numero: str) -> str | None:
    """Fecha ISO de publicación de un boletín, leída de su propio `<title>`."""
    clave = (anio, numero)
    if clave in _FECHAS:
        return _FECHAS[clave]
    try:
        html = descargar(
            f"https://www.gobiernodecanarias.org/boc/{anio}/{numero}/index.html"
        ).decode("utf-8", errors="replace")[:2000]
    except Exception:  # noqa: BLE001
        _FECHAS[clave] = None
        return None
    encontrada = TITULO_BOLETIN.search(html)
    iso = None
    if encontrada and encontrada.group(2).lower() in MESES:
        iso = (
            f"{int(encontrada.group(3)):04d}-{MESES[encontrada.group(2).lower()]:02d}"
            f"-{int(encontrada.group(1)):02d}"
        )
    _FECHAS[clave] = iso
    return iso


def buscar_en_archivo(titulo: str, boletines: int = 90) -> dict | None:
    """Recorre el archivo del BOC desde la fecha de la disposición hasta encontrarla.

    Se usa cuando el boletín declarado en la cabecera es el equivocado: el número se
    perdió, pero la fecha de la disposición está en su propio título y la publicación
    siempre es posterior y cercana. Se localiza el primer boletín de esa fecha por
    búsqueda binaria y a partir de ahí se recorre el sumario de cada uno.
    """
    fecha = FECHA_EN_TITULO.search(titulo)
    if not fecha or fecha.group(2).lower() not in MESES:
        return None
    anio = int(fecha.group(3))
    desde = f"{anio:04d}-{MESES[fecha.group(2).lower()]:02d}-{int(fecha.group(1)):02d}"

    numeros = [(anio, n) for n in numeros_del_anio(anio)]
    numeros += [(anio + 1, n) for n in numeros_del_anio(anio + 1)]
    if not numeros:
        return None

    izquierda, derecha = 0, len(numeros)
    while izquierda < derecha:
        medio = (izquierda + derecha) // 2
        iso = fecha_del_boletin(*numeros[medio])
        if iso is None or iso < desde:
            izquierda = medio + 1
        else:
            derecha = medio

    buscadas = fichas(titulo)
    # La fecha de la disposición aparece literalmente en el sumario y discrimina mucho
    # más que las palabras del título, que en el corpus suelen estar reformuladas. Se
    # exige coincidencia de fecha y, sobre ese conjunto ya reducido, basta media
    # coincidencia léxica.
    dia_mes_anio = fecha.group(0).lower()
    for anio_b, numero in numeros[izquierda : izquierda + boletines]:
        for disposicion in disposiciones_del_boletin(str(anio_b), numero):
            rotulo = sin_acentos(disposicion["titulo"].lower())
            proporcion = len(buscadas & fichas(disposicion["titulo"])) / max(len(buscadas), 1)
            coincide = proporcion >= 0.7 or (
                sin_acentos(dia_mes_anio) in rotulo and proporcion >= 0.6
            )
            if coincide:
                return {
                    "anio": str(anio_b),
                    "numero": numero,
                    "fecha_boletin": fecha_del_boletin(anio_b, numero) or "?",
                    "proporcion": round(proporcion, 3),
                    **disposicion,
                }
    return None


def url_html_de_disposicion(anio: str, numero_boletin: str, posicion: int, cve: str) -> str | None:
    """URL de la versión HTML de una disposición, probando los dos esquemas del BOC.

    El BOC cambió de esquema alrededor de 2025: antes el último tramo de la URL era la
    **posición** de la disposición dentro del boletín (`/boc/2023/110/001.html`) y ahora
    es su **número de disposición** (`/boc/2026/046/751.html`). El sumario ya no publica
    ese enlace, así que se prueban ambas formas y se usa la que responde.
    """
    numero = cve.rsplit("-", 1)[-1]
    for tramo in (numero, f"{posicion:03d}"):
        candidata = f"https://www.gobiernodecanarias.org/boc/{anio}/{numero_boletin}/{tramo}.html"
        try:
            peticion = urllib.request.Request(
                candidata, headers={"User-Agent": "normativa-educativa-canaria/1.0"}
            )
            with urllib.request.urlopen(peticion, timeout=30) as respuesta:
                if respuesta.status == 200:
                    return candidata
        except Exception:  # noqa: BLE001 — un 404 sólo descarta este esquema
            continue
    return None


def texto_del_pdf(datos: bytes) -> str:
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp.write(datos)
        ruta = tmp.name
    try:
        completado = subprocess.run(
            ["pdftotext", "-layout", "-enc", "UTF-8", ruta, "-"],
            capture_output=True,
            check=True,
        )
        return completado.stdout.decode("utf-8", errors="replace")
    finally:
        pathlib.Path(ruta).unlink(missing_ok=True)


def cabecera_y_cuerpo(ruta: pathlib.Path) -> tuple[list[str], str]:
    contenido = ruta.read_text(encoding="utf-8")
    partes = contenido.split("\n---\n", 1)
    if len(partes) != 2:
        raise SystemExit(f"{ruta.name}: no encuentro el separador de cabecera")
    return partes[0].split("\n"), partes[1]


def campo(cabecera: list[str], nombre: str) -> str | None:
    for linea in cabecera:
        if linea.startswith(nombre + ":"):
            return linea.split(":", 1)[1].strip()
    return None


def reexportar(ruta: pathlib.Path, fecha: str, aplicar: bool, buscar: bool = True) -> dict:
    cabecera, _ = cabecera_y_cuerpo(ruta)
    titulo = campo(cabecera, "Título oficial") or ""
    url = campo(cabecera, "URL origen") or ""
    resultado = {"fichero": ruta.name, "titulo": titulo}

    boletin = BOC_BOLETIN.search(url)
    if not boletin:
        resultado["estado"] = "no-boc"
        resultado["detalle"] = f"la URL no es un boletín del BOC: {url}"
        return resultado

    anio, numero = boletin.groups()
    candidatas = disposiciones_del_boletin(anio, numero)
    if not candidatas:
        resultado["estado"] = "sin-sumario"
        return resultado

    buscadas = fichas(titulo)
    puntuadas = sorted(
        (
            (len(buscadas & fichas(c["titulo"])) / max(len(buscadas), 1), c)
            for c in candidatas
        ),
        key=lambda par: par[0],
        reverse=True,
    )
    proporcion, mejor = puntuadas[0]
    segunda = puntuadas[1][0] if len(puntuadas) > 1 else 0.0
    resultado.update(
        {
            "cve": mejor["cve"],
            "coincidencia": round(proporcion, 3),
            "margen": round(proporcion - segunda, 3),
            "titulo_sumario": mejor["titulo"][:160],
            "pdf": mejor["pdf"],
        }
    )
    if proporcion < 0.55:
        # El boletín declarado en la cabecera no contiene la disposición: se busca en
        # el archivo del BOC a partir de la fecha que el propio título indica.
        hallazgo = buscar_en_archivo(titulo) if buscar else None
        if not hallazgo:
            resultado["estado"] = "dudosa"
            return resultado
        anio, numero = hallazgo["anio"], hallazgo["numero"]
        mejor, proporcion = hallazgo, hallazgo["proporcion"]
        resultado.update(
            {
                "boletin_corregido": f"{anio}/{numero} ({hallazgo['fecha_boletin']})",
                "cve": mejor["cve"],
                "coincidencia": proporcion,
                "titulo_sumario": mejor["titulo"][:160],
                "pdf": mejor["pdf"],
            }
        )

    cuerpo = texto_del_pdf(descargar(mejor["pdf"]))
    resultado["lineas"] = cuerpo.count("\n")
    # Comprobación de seguridad: el texto extraído debe hablar de lo que dice el título.
    presentes = sum(1 for p in buscadas if p in sin_acentos(cuerpo.lower()))
    resultado["correspondencia"] = round(presentes / max(len(buscadas), 1), 3)
    if resultado["correspondencia"] < 0.65:
        resultado["estado"] = "pdf-no-corresponde"
        return resultado

    nueva_url = url_html_de_disposicion(anio, numero, mejor["posicion"], mejor["cve"]) or url
    nueva_cabecera = []
    for linea in cabecera:
        if linea.startswith("ADVERTENCIA DE CONTENIDO"):
            continue  # la contaminación queda resuelta con esta re-exportación
        if linea.startswith("URL origen:"):
            linea = f"URL origen: {nueva_url}"
        elif linea.startswith("Fecha de consulta:"):
            linea = f"Fecha de consulta: {fecha}"
        elif linea.startswith("Fecha de exportación local:"):
            linea = f"Fecha de exportación local: {fecha}"
        elif linea.startswith("Nota de extracción:"):
            linea = (
                "Nota de extracción: Texto extraído con pdftotext -layout desde el PDF oficial "
                f"firmado del BOC ({mejor['cve']}), {mejor['pdf']}."
            )
        nueva_cabecera.append(linea)
    if not any(l.startswith("PDF oficial:") for l in nueva_cabecera):
        nueva_cabecera.insert(4, f"PDF oficial: {mejor['pdf']}")

    resultado["url_nueva"] = nueva_url
    resultado["estado"] = "listo"
    if aplicar:
        contenido = "\n".join(nueva_cabecera) + "\n---\n" + cuerpo
        ruta.write_text(contenido, encoding="utf-8")
        resultado["sha256"] = hashlib.sha256(contenido.encode("utf-8")).hexdigest()
        resultado["pdf_oficial"] = mejor["pdf"]
        resultado["estado"] = "reexportado"
    return resultado


INDICE_TEXTOS = RAIZ / "06_indices" / "textos-oficiales.yaml"


def sincronizar_indice(cambios: dict[str, dict]) -> list[str]:
    """Actualiza en el índice la procedencia y el hash de las copias re-exportadas.

    Se edita línea a línea en lugar de volcar el YAML entero para no reformatear un
    índice de 1.500 líneas que nadie ha pedido tocar.
    """
    if not cambios:
        return []
    lineas = INDICE_TEXTOS.read_text(encoding="utf-8").split("\n")
    actual = None
    tocados: list[str] = []
    for indice, linea in enumerate(lineas):
        encabezado = re.match(r"^  (NOR-\d{3}):\s*$", linea)
        if encabezado:
            actual = cambios.get(encabezado.group(1))
            if actual:
                tocados.append(encabezado.group(1))
            continue
        if not actual:
            continue
        for clave, valor in (
            ("    fecha_consulta:", actual["fecha"]),
            ("      url_html:", actual["url"]),
            ("      url_pdf:", actual["pdf"]),
            ("      url_origen:", actual["url"]),
            ("      fecha_exportacion:", f"'{actual['fecha']}'"),
            ("      sha256:", actual["sha256"]),
        ):
            if linea.startswith(clave):
                lineas[indice] = f"{clave} {valor}"
                break
    INDICE_TEXTOS.write_text("\n".join(lineas), encoding="utf-8")
    return tocados


def auditar_urls() -> int:
    """Contrasta la `url_oficial` de cada ficha NOR contra el sumario de su boletín.

    Es la comprobación que descubrió, en `TAREA-085`, que tres fichas describían normas
    inexistentes. Vive aquí y no en `validar_corpus.py` porque necesita red y el
    validador debe poder correr sin ella.
    """
    import concurrent.futures
    import yaml  # noqa: PLC0415 — dependencia opcional, sólo para este modo

    patron = re.compile(r"gobiernodecanarias\.org/boc/(\d{4})/(\d{3})/(\d{1,4})\.html")
    casos = []
    for ficha in sorted((RAIZ / "02_normativa").rglob("NOR-*.md")):
        frontmatter = yaml.safe_load(ficha.read_text(encoding="utf-8").split("---")[1])
        encontrada = patron.search(frontmatter.get("url_oficial") or "")
        if not encontrada:
            continue
        # Las fichas retiradas por DEC-0011 no describen una norma real: por definición
        # no van a contrastar contra ningún sumario, y repetirlo cada vez sería ruido.
        if str(frontmatter.get("estado_vigencia", "")).startswith("No normativa"):
            continue
        casos.append((frontmatter["id"], frontmatter["titulo"], encontrada.groups()))

    def revisar(caso):
        ident, titulo, (anio, boletin, tramo) = caso
        try:
            disposiciones = disposiciones_del_boletin(anio, boletin)
        except Exception as error:  # noqa: BLE001
            return ident, "error", str(error), ""
        if not disposiciones:
            return ident, "sumario-vacio", f"{anio}/{boletin}", ""
        # El último tramo de la URL es la posición dentro del boletín en el esquema
        # antiguo y el número de disposición desde 2025; se aceptan ambos.
        declarada = next(
            (d for d in disposiciones if d["cve"].rsplit("-", 1)[-1] == str(int(tramo))), None
        )
        if declarada is None and int(tramo) <= len(disposiciones):
            declarada = disposiciones[int(tramo) - 1]
        buscadas = fichas(titulo)
        proporcion = lambda d: len(buscadas & fichas(d["titulo"])) / max(len(buscadas), 1)  # noqa: E731
        mejor = max(disposiciones, key=proporcion)
        correcta = declarada is not None and proporcion(declarada) >= 0.6
        detalle = (
            f"{anio}/{boletin}/{tramo} coincidencia={proporcion(declarada):.2f}"
            if declarada
            else f"{anio}/{boletin}/{tramo} fuera de rango"
        )
        return (
            ident,
            "ok" if correcta else "revisar",
            detalle,
            f"mejor={proporcion(mejor):.2f} [{mejor['cve']}] {mejor['titulo'][:110]}",
        )

    sospechosas = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ejecutor:
        for ident, estado, detalle, mejor in ejecutor.map(revisar, casos):
            if estado != "ok":
                sospechosas += 1
                print(f"{ident} [{estado}] {detalle}\n    {mejor}")
    print(f"\n{len(casos)} fichas NOR contrastadas · {sospechosas} a revisar")
    return 1 if sospechosas else 0


def marcadas() -> list[pathlib.Path]:
    salida = []
    for fichero in sorted(TEXTOS.glob("texto-oficial-*.txt")):
        cabeza = fichero.read_text(encoding="utf-8", errors="replace")[:4000]
        if "ADVERTENCIA DE CONTENIDO" in cabeza:
            salida.append(fichero)
    return salida


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ids", nargs="*", help="IDs a re-exportar, p. ej. NOR-044")
    parser.add_argument("--marcadas", action="store_true", help="todas las marcadas como contaminadas")
    parser.add_argument("--auditar", action="store_true",
                        help="contrasta la url_oficial de cada ficha NOR contra el sumario de su boletín")
    parser.add_argument("--aplicar", action="store_true", help="reescribe los ficheros")
    parser.add_argument("--fecha", default="2026-08-05", help="fecha de consulta y exportación")
    args = parser.parse_args()

    if args.auditar:
        return auditar_urls()

    objetivos: list[pathlib.Path] = []
    if args.marcadas:
        objetivos = marcadas()
    for ident in args.ids:
        encontrados = list(TEXTOS.glob(f"texto-oficial-{ident}-*.txt"))
        if not encontrados:
            print(f"! sin copia local para {ident}", file=sys.stderr)
        objetivos.extend(encontrados)
    if not objetivos:
        parser.error("indica al menos un ID o usa --marcadas")

    fallos = 0
    cambios: dict[str, dict] = {}
    for ruta in objetivos:
        try:
            info = reexportar(ruta, args.fecha, args.aplicar)
        except Exception as error:  # noqa: BLE001 — el informe debe continuar
            print(f"{ruta.name}\n  ERROR {error}")
            fallos += 1
            continue
        estado = info.get("estado")
        print(f"{ruta.name}\n  estado={estado} " + " ".join(
            f"{k}={v}" for k, v in info.items()
            if k in ("cve", "coincidencia", "margen", "correspondencia", "lineas", "boletin_corregido")
        ))
        if estado in ("dudosa", "pdf-no-corresponde"):
            print(f"  sumario: {info.get('titulo_sumario')}")
        if estado == "reexportado":
            identificador = re.search(r"(NOR|CUR|FTE)-\d{3}", ruta.name).group(0)
            cambios[identificador] = {
                "url": info["url_nueva"],
                "pdf": info["pdf_oficial"],
                "sha256": info["sha256"],
                "fecha": args.fecha,
            }
        if estado not in ("listo", "reexportado"):
            fallos += 1

    if cambios:
        tocados = sincronizar_indice(cambios)
        print(f"\nÍndice textos-oficiales.yaml actualizado: {', '.join(tocados)}")
        faltan = sorted(set(cambios) - set(tocados))
        if faltan:
            print(f"! sin entrada en el índice: {', '.join(faltan)}")
            fallos += 1
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
