#!/usr/bin/env python3
"""Valida el corpus contra los esquemas de `schemas/` y contra sus índices YAML.

Comprueba tres cosas que hasta ahora no comprobaba nadie:

1. Cada ficha cumple el esquema JSON Schema de su tipo de entidad.
2. El ID del frontmatter coincide con el nombre del fichero.
3. Cada entidad está registrada en su índice de `06_indices/` y cada entrada
   del índice apunta a una entidad que existe (regla R11 de AGENTS.md).

Uso:

    python3 11_calidad/validar_corpus.py              # informe legible
    python3 11_calidad/validar_corpus.py --json       # salida para CI
    python3 11_calidad/validar_corpus.py --tipo NOR   # solo un tipo

Devuelve 1 si hay errores. Los avisos no hacen fallar la ejecución: señalan
campos recomendados ausentes que exigen decisión editorial o evidencia nueva,
y no pueden rellenarse inventando datos (R1).

Dependencias: pyyaml, jsonschema.
"""

from __future__ import annotations

import argparse
import datetime
import json
import pathlib
import re
import sys

try:
    import yaml
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError as exc:  # pragma: no cover - guía de instalación
    sys.exit(f"Falta una dependencia ({exc.name}). Instala con: pip install pyyaml jsonschema")

RAIZ = pathlib.Path(__file__).resolve().parent.parent

# tipo -> configuración de validación
#   patron:        glob de las fichas, relativo a la raíz del repositorio
#   esquema:       fichero de `schemas/`
#   origen:        "frontmatter" (YAML entre --- de un .md) o "documento" (.yaml entero)
#   indice:        índice canónico de `06_indices/`
#   recomendados:  campos no obligatorios cuya ausencia se avisa
ENTIDADES = {
    "FTE": {
        "patron": "01_fuentes/**/FTE-*.md",
        "esquema": "fuente.schema.yaml",
        "origen": "frontmatter",
        "indice": "fuentes.yaml",
        # `fecha_analisis` no entra aquí: R5 solo la exige cuando hay análisis, y
        # una fuente catalogada sin analizar legítimamente no la tiene.
        # `relacionadas: []` es válido y no se avisa: hay fuentes que todavía no
        # referencia ninguna ficha.
        "recomendados": ["nivel_evidencia"],
    },
    "NOR": {
        "patron": "02_normativa/**/NOR-*.md",
        "esquema": "norma.schema.yaml",
        "origen": "frontmatter",
        "indice": "normativa.yaml",
        "recomendados": ["temas"],
    },
    "CUR": {
        "patron": "03_curriculos/**/CUR-*.yaml",
        "esquema": "curriculum.schema.yaml",
        "origen": "documento",
        "indice": "curriculos.yaml",
        "recomendados": [],
        # El índice duplica estos campos de la ficha; si divergen, manda la ficha.
        "espejo": ["estado_extraccion", "etapa", "materia", "norma_base", "fuente"],
    },
    "REL": {
        "patron": "05_relaciones/**/REL-*.yaml",
        "esquema": "relacion.schema.yaml",
        "origen": "documento",
        "indice": "relaciones.yaml",
        "recomendados": [],
    },
    "PREG": {
        "patron": "08_tareas/preguntas/PREG-*.md",
        "esquema": "pregunta.schema.yaml",
        "origen": "frontmatter",
        "indice": "preguntas.yaml",
        "recomendados": [],
    },
    "TAREA": {
        "patron": "08_tareas/backlog/TAREA-*.md",
        "esquema": "tarea.schema.yaml",
        "origen": "frontmatter",
        "indice": "tareas.yaml",
        "recomendados": [],
    },
    # TAREA-091: los chunks 00006-00022 convivieron meses con un esquema propio
    # (`contenido`, `fecha_registro`, `<aviso>`) sin que nada lo detectara, porque
    # no se validaban contra `schemas/chunk.schema.yaml`. Como entidad más, reutilizan
    # el esquema, la cobertura de índice y la comprobación referencial.
    "CHUNK": {
        "patron": "07_corpus_ia/chunks/CHUNK-*.yaml",
        "esquema": "chunk.schema.yaml",
        "origen": "documento",
        "indice": "chunks.yaml",
        "recomendados": [],
    },
}

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---", re.S)
ID_EN_NOMBRE = re.compile(r"\A([A-Z]+-[0-9]+)")

# Firma del doble encodeo UTF-8 -> latin-1: `Ã` o `Â` seguidos del segundo byte
# de la secuencia original. Se exige el par para no marcar una `Ã` legítima.
FIRMA_MOJIBAKE = re.compile("Ã[-¿¡-ÿ]|Â[ -¿-]")


def normalizar(valor):
    """Convierte fechas de PyYAML a cadenas ISO.

    `fecha_consulta: 2026-04-26` sin comillas es un `datetime.date` para YAML,
    pero los esquemas declaran `type: string`. Normalizar aquí evita tener que
    entrecomillar cientos de fechas o relajar el tipo del esquema.
    """
    if isinstance(valor, (datetime.datetime, datetime.date)):
        return valor.isoformat()
    if isinstance(valor, dict):
        return {k: normalizar(v) for k, v in valor.items()}
    if isinstance(valor, list):
        return [normalizar(v) for v in valor]
    return valor


def cargar(ruta: pathlib.Path, origen: str):
    """Devuelve (datos, error). `datos` es None si no se pudo leer."""
    texto = ruta.read_text(encoding="utf-8")
    if origen == "frontmatter":
        encontrado = FRONTMATTER.match(texto)
        if not encontrado:
            return None, "sin frontmatter YAML delimitado por ---"
        texto = encontrado.group(1)
    try:
        return normalizar(yaml.safe_load(texto)), None
    except yaml.YAMLError as exc:
        return None, f"YAML no parseable: {str(exc).splitlines()[0]}"


def entradas_del_indice(nombre: str) -> dict:
    ruta = RAIZ / "06_indices" / nombre
    if not ruta.exists():
        return {}
    datos = yaml.safe_load(ruta.read_text(encoding="utf-8")) or {}
    return datos if isinstance(datos, dict) else {}


def errores_de_ruta(indice: str, entradas: dict, con_ficha: set[str]) -> list[dict]:
    """Comprueba que cada `ruta` del índice resuelve y apunta a su propia ficha.

    Sin esto una entrada puede apuntar al fichero de otra entidad sin que nada lo
    detecte: así acabó TAREA-055 apuntando a la ficha de TAREA-054. Solo se
    comprueban las entidades que sí tienen ficha; las que no la tienen ya generan
    el aviso de «entrada de índice sin ficha» y no procede duplicarlo.
    """
    fallos = []
    for identificador, datos in entradas.items():
        if not isinstance(datos, dict) or identificador not in con_ficha:
            continue
        ruta = datos.get("ruta")
        if not ruta:
            continue
        nombre = pathlib.Path(ruta).name
        if not (RAIZ / ruta).exists():
            fallos.append({
                "fichero": f"06_indices/{indice}",
                "campo": identificador,
                "mensaje": f"la ruta del índice no resuelve: {ruta}",
            })
        elif not nombre.startswith(identificador + "-"):
            fallos.append({
                "fichero": f"06_indices/{indice}",
                "campo": identificador,
                "mensaje": f"la ruta apunta a {nombre}, que no es la ficha de {identificador}",
            })
    return fallos


def validar_tipo(tipo: str, cfg: dict) -> dict:
    esquema_ruta = RAIZ / "schemas" / cfg["esquema"]
    validador = Draft202012Validator(
        yaml.safe_load(esquema_ruta.read_text(encoding="utf-8")),
        format_checker=FormatChecker(),
    )

    errores: list[dict] = []
    avisos: list[dict] = []
    vistos: set[str] = set()
    ficheros = sorted(RAIZ.glob(cfg["patron"]))

    for fichero in ficheros:
        rel = fichero.relative_to(RAIZ).as_posix()
        datos, fallo = cargar(fichero, cfg["origen"])
        if fallo:
            errores.append({"fichero": rel, "campo": "(fichero)", "mensaje": fallo})
            continue
        if not isinstance(datos, dict):
            errores.append({"fichero": rel, "campo": "(fichero)", "mensaje": "el contenido no es un mapa YAML"})
            continue

        # El ID del frontmatter debe coincidir con el del nombre del fichero (R10).
        en_nombre = ID_EN_NOMBRE.match(fichero.name)
        if en_nombre and datos.get("id") != en_nombre.group(1):
            errores.append({
                "fichero": rel,
                "campo": "id",
                "mensaje": f"el id {datos.get('id')!r} no coincide con el nombre del fichero ({en_nombre.group(1)})",
            })
        if isinstance(datos.get("id"), str):
            vistos.add(datos["id"])

        for error in sorted(validador.iter_errors(datos), key=lambda e: list(e.path)):
            errores.append({
                "fichero": rel,
                "campo": ".".join(str(p) for p in error.path) or "(raíz)",
                "mensaje": error.message,
            })

        for campo in cfg["recomendados"]:
            if campo not in datos or datos[campo] in (None, [], ""):
                avisos.append({"fichero": rel, "campo": campo, "mensaje": "campo recomendado ausente o vacío"})

        # DEC-0008: `descriptores` debe ser un mapa por curso. La lista plana es
        # transitoria y señala una competencia cuya vinculación no se ha verificado.
        for comp in (datos.get("elementos") or {}).get("competencias_especificas") or []:
            if isinstance(comp, dict) and isinstance(comp.get("descriptores"), list):
                avisos.append({
                    "fichero": rel, "campo": f"{comp.get('codigo')}.descriptores",
                    "mensaje": "lista plana sin migrar a mapa por curso (DEC-0008); pendiente de TAREA-073",
                })

        # Campos que el índice duplica: la ficha es la fuente de verdad.
        entrada = entradas_del_indice(cfg["indice"]).get(datos.get("id"))
        if isinstance(entrada, dict):
            for campo in cfg.get("espejo", []):
                if campo in entrada and normalizar(entrada[campo]) != datos.get(campo):
                    errores.append({
                        "fichero": f"06_indices/{cfg['indice']}",
                        "campo": f"{datos['id']}.{campo}",
                        "mensaje": f"el índice dice {entrada[campo]!r} y la ficha dice {datos.get(campo)!r}",
                    })

    # Cobertura de índice (R11). Una ficha fuera del índice es un error: rompe la
    # puerta de entrada del repositorio y siempre se puede corregir. Una entrada de
    # índice sin ficha es deuda documental histórica, que sólo se resuelve
    # reconstruyendo lo que se hizo: se avisa, no se bloquea.
    entradas = entradas_del_indice(cfg["indice"])
    errores.extend(errores_de_ruta(cfg["indice"], entradas, vistos))
    indexados = set(entradas)
    for identificador in sorted(vistos - indexados):
        errores.append({
            "fichero": f"06_indices/{cfg['indice']}",
            "campo": identificador,
            "mensaje": f"{identificador} existe como ficha pero no está en el índice",
        })
    for identificador in sorted(indexados - vistos):
        entrada = entradas.get(identificador)
        # `ficha: null` marca un hueco reconocido y documentado (DEC-0007): la
        # entrada existe, la ficha nunca se escribió y no se puede reconstruir.
        if isinstance(entrada, dict) and "ficha" in entrada and entrada["ficha"] is None:
            continue
        avisos.append({
            "fichero": f"06_indices/{cfg['indice']}",
            "campo": identificador,
            "mensaje": f"{identificador} está en el índice pero no tiene ficha",
        })

    return {
        "tipo": tipo,
        "ficheros": len(ficheros),
        "errores": errores,
        "avisos": avisos,
    }


CAMPOS_REFERENCIA = [
    "relacionadas", "fuente_principal", "fuente", "norma_base", "origen", "destino",
    "origen_id",
    "desarrolla_a", "modificada_por", "modifica_a", "deroga_a", "derogada_por",
    "relacionada_con",
]
REFERENCIA = re.compile(r"\A(?:FTE|NOR|CUR|REL|CHUNK|PREG|TAREA|DEC)-\d{3,5}\Z")


def _referencias(objeto) -> set[str]:
    """IDs citados en los campos estructurados de relación de una ficha."""
    encontradas: set[str] = set()
    if isinstance(objeto, dict):
        for clave, valor in objeto.items():
            if clave in CAMPOS_REFERENCIA:
                for elemento in (valor if isinstance(valor, list) else [valor]):
                    if isinstance(elemento, str) and REFERENCIA.match(elemento):
                        encontradas.add(elemento)
            encontradas |= _referencias(valor)
    elif isinstance(objeto, list):
        for valor in objeto:
            encontradas |= _referencias(valor)
    return encontradas


def validar_referencias() -> dict:
    """Comprueba que las entidades citadas por otras fichas existen.

    Una ficha puede quedar huérfana sin que nada lo note: así se descubrió que
    `REL-058` estaba guardada como `.md` en vez de `.yaml` y por eso escapaba tanto
    al validador como a la sincronización de índices, pese a que `FTE-075` la citaba.
    Solo se miran campos estructurados de relación, no el texto en prosa, que
    legítimamente menciona entidades retiradas para dejar constancia histórica.
    """
    existen: set[str] = set()
    for cfg in ENTIDADES.values():
        for fichero in RAIZ.glob(cfg["patron"]):
            encontrado = ID_EN_NOMBRE.match(fichero.name)
            if encontrado:
                existen.add(encontrado.group(1))
    for fichero in RAIZ.glob("09_decisiones-editoriales/**/DEC-*.md"):
        encontrado = ID_EN_NOMBRE.match(fichero.name)
        if encontrado:
            existen.add(encontrado.group(1))
    for fichero in RAIZ.glob("07_corpus_ia/**/CHUNK-*.yaml"):
        encontrado = ID_EN_NOMBRE.match(fichero.name)
        if encontrado:
            existen.add(encontrado.group(1))
    for fichero in RAIZ.glob("04_analisis/**/AN-*.md"):
        encontrado = ID_EN_NOMBRE.match(fichero.name)
        if encontrado:
            existen.add(encontrado.group(1))

    errores = []
    revisados = 0
    for tipo, cfg in ENTIDADES.items():
        for fichero in sorted(RAIZ.glob(cfg["patron"])):
            datos, fallo = cargar(fichero, cfg["origen"])
            if fallo or not isinstance(datos, dict):
                continue
            revisados += 1
            for referencia in sorted(_referencias(datos) - existen):
                errores.append({
                    "fichero": fichero.relative_to(RAIZ).as_posix(),
                    "campo": referencia,
                    "mensaje": f"referencia a {referencia}, que no existe como ficha",
                })
    return {"tipo": "REFERENCIAS", "ficheros": revisados, "errores": errores, "avisos": []}


def validar_desdoblamientos() -> dict:
    """Detecta normas descritas por más de una ficha (DEC-0010).

    El desdoblamiento por etapa produjo metadatos divergentes, copias locales
    duplicadas y hasta una fuente inventada para justificar la segunda ficha. Dos
    señales lo delatan: fichas que comparten `fecha_disposicion` y
    `fuente_principal`, y copias locales con el mismo contenido.
    """
    avisos = []

    por_norma: dict[tuple, list[str]] = {}
    for fichero in sorted(RAIZ.glob(ENTIDADES["NOR"]["patron"])):
        datos, fallo = cargar(fichero, "frontmatter")
        if fallo or not isinstance(datos, dict):
            continue
        clave = (str(datos.get("fecha_disposicion")), str(datos.get("fuente_principal")))
        if clave[0] not in ("None", "") and clave[1] != "None":
            por_norma.setdefault(clave, []).append(datos["id"])
    for (fecha, fuente), ids in sorted(por_norma.items()):
        if len(ids) > 1:
            avisos.append({
                "fichero": "02_normativa/",
                "campo": ", ".join(sorted(ids)),
                "mensaje": f"comparten fecha_disposicion {fecha} y fuente {fuente}: "
                           f"¿describen la misma norma? (DEC-0010)",
            })

    # Copias locales con contenido idéntico: la cabecera de exportación son 9 líneas.
    import hashlib
    por_contenido: dict[str, list[str]] = {}
    for fichero in sorted(RAIZ.glob("07_corpus_ia/textos-completos/*.txt")):
        cuerpo = "\n".join(fichero.read_text(encoding="utf-8", errors="replace").splitlines()[9:])
        huella = hashlib.sha256(cuerpo.encode()).hexdigest()
        por_contenido.setdefault(huella, []).append(fichero.name)
    for nombres in por_contenido.values():
        if len(nombres) > 1:
            avisos.append({
                "fichero": "07_corpus_ia/textos-completos/",
                "campo": ", ".join(sorted(nombres)),
                "mensaje": "copias locales con contenido idéntico (DEC-0010)",
            })

    return {"tipo": "DESDOBLAMIENTOS", "ficheros": len(por_norma), "errores": [], "avisos": avisos}


GENERICAS = {
    "de", "la", "el", "los", "las", "por", "que", "se", "y", "en", "del", "al", "a", "con",
    "para", "un", "una", "sobre", "orden", "decreto", "resolucion", "real", "ley", "articulo",
    "canarias", "comunidad", "autonoma", "consejeria", "educacion", "gobierno", "boletin",
    "oficial", "no", "es", "su", "sus", "lo", "como", "mayo", "junio", "julio", "enero",
    "febrero", "marzo", "abril", "agosto", "septiembre", "octubre", "noviembre", "diciembre",
}


def _significativas(texto: str) -> list[str]:
    palabras = re.sub(r"[^a-z0-9 ]+", " ", _sin_tildes(texto).lower()).split()
    return [p for p in palabras if len(p) > 3 and p not in GENERICAS]


def _sin_tildes(texto: str) -> str:
    import unicodedata
    texto = unicodedata.normalize("NFD", texto)
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def validar_correspondencia_textos() -> dict:
    """Comprueba que cada copia local contiene la norma que declara su cabecera.

    El proceso de exportación original tomó en varios casos el ítem equivocado del
    sumario del boletín, de modo que la cabecera R16 es correcta —título y URL— pero
    el cuerpo es otra disposición por completo. Nada lo detectaba: el fichero está
    bien codificado, tiene su cabecera y su tamaño es plausible.

    Se comparan las palabras significativas del título declarado con el cuerpo. Un
    título cuyo vocabulario propio no aparece señala que el cuerpo no le corresponde.
    """
    errores, avisos = [], []
    ficheros = sorted(RAIZ.glob("07_corpus_ia/textos-completos/*.txt"))
    for fichero in ficheros:
        lineas = fichero.read_text(encoding="utf-8", errors="replace").splitlines()
        titulo = next((l.split(":", 1)[1] for l in lineas[:12] if l.startswith("Título oficial:")), "")
        if not titulo:
            continue
        cuerpo = _sin_tildes("\n".join(lineas[9:])).lower()
        claves = _significativas(titulo)
        if len(claves) < 4:
            continue
        presentes = sum(1 for p in set(claves) if p in cuerpo)
        proporcion = presentes / len(set(claves))
        entrada = {
            "fichero": fichero.relative_to(RAIZ).as_posix(),
            "campo": "(contenido)",
            "mensaje": f"solo {presentes} de {len(set(claves))} términos propios del título "
                       f"aparecen en el cuerpo ({proporcion:.0%}): la copia puede no corresponder "
                       f"a la norma declarada",
        }
        # Una copia marcada explícitamente como contaminada es deuda documentada y
        # con tarea abierta, no un fallo oculto: se avisa. Sin marca, es error, para
        # que una contaminación nueva no pase inadvertida.
        marcada = "ADVERTENCIA DE CONTENIDO" in "\n".join(lineas[:14])
        if proporcion < 0.65:
            (avisos if marcada else errores).append(entrada)
    return {"tipo": "CORRESPONDENCIA", "ficheros": len(ficheros),
            "errores": errores, "avisos": avisos}


def validar_textos_locales() -> dict:
    """Comprueba que las copias locales de texto oficial no estén dobles-codificadas.

    Un texto guardado como UTF-8 leído como latin-1 y vuelto a guardar deja `Ã` o
    `Â` donde debía haber una vocal acentuada, y eso lo vuelve inservible para
    búsqueda: `Competencia específica` pasa a `Competencia especÃ­fica` y ninguna
    consulta lo encuentra. Ocurrió en 33 de 97 ficheros sin que nada lo detectara
    (TAREA-074), así que se comprueba en cada validación.
    """
    errores = []
    ficheros = sorted(RAIZ.glob("07_corpus_ia/textos-completos/*.txt"))
    for fichero in ficheros:
        texto = fichero.read_text(encoding="utf-8", errors="replace")
        dañados = FIRMA_MOJIBAKE.findall(texto)
        if dañados:
            muestra = ", ".join(sorted(set(dañados))[:4])
            errores.append({
                "fichero": fichero.relative_to(RAIZ).as_posix(),
                "campo": "(codificación)",
                "mensaje": f"{len(dañados)} secuencias de doble encodeo ({muestra}); "
                           f"repara con 11_calidad/reparar_mojibake.py",
            })
    return {"tipo": "TEXTOS", "ficheros": len(ficheros), "errores": errores, "avisos": []}


def validar_frontmatter_curricular() -> dict:
    """Comprueba que cada ficha curricular `.md` tiene frontmatter válido.

    Las 23 fichas de ESO lo llevan desde el principio, pero las 27 de Infantil,
    Primaria y Bachillerato se crearon sin él: la práctica divergió por etapa y
    nada lo detectaba porque el validador sólo miraba los `.yaml` emparejados
    (TAREA-091). Sin frontmatter, la ficha no cumple AGENTS.md §5.1 ni es
    consumible por las herramientas que leen metadatos del propio Markdown.
    """
    errores = []
    revisados = 0
    for fichero in sorted(RAIZ.glob("03_curriculos/**/CUR-*.md")):
        rel = fichero.relative_to(RAIZ).as_posix()
        revisados += 1
        datos, fallo = cargar(fichero, "frontmatter")
        if fallo:
            errores.append({"fichero": rel, "campo": "(frontmatter)", "mensaje": fallo})
            continue
        if not isinstance(datos, dict):
            errores.append({"fichero": rel, "campo": "(frontmatter)", "mensaje": "el frontmatter no es un mapa YAML"})
            continue
        en_nombre = ID_EN_NOMBRE.match(fichero.name)
        if en_nombre and datos.get("id") != en_nombre.group(1):
            errores.append({
                "fichero": rel,
                "campo": "id",
                "mensaje": f"el id {datos.get('id')!r} no coincide con el nombre del fichero ({en_nombre.group(1)})",
            })
    return {"tipo": "CURRICULARES-MD", "ficheros": revisados, "errores": errores, "avisos": []}


def validar_resumenes() -> dict:
    """Comprueba el formato de los resúmenes IA de `07_corpus_ia/resumenes/`.

    Cuatro resúmenes estuvieron íntegramente sangrados a 4 espacios —frontmatter,
    delimitadores y cuerpo— y `yaml.safe_load` no fallaba porque el bloque
    sangrado se interpreta como un escalar. Se exige: delimitadores `---` en
    columna 0, claves de primer nivel sin sangría inicial (AGENTS.md §5.1) y
    cuerpo sin sangría sistemática.
    """
    errores = []
    revisados = 0
    for fichero in sorted(RAIZ.glob("07_corpus_ia/resumenes/*.md")):
        rel = fichero.relative_to(RAIZ).as_posix()
        revisados += 1
        texto = fichero.read_text(encoding="utf-8")
        if not texto.startswith("---\n"):
            errores.append({"fichero": rel, "campo": "(frontmatter)", "mensaje": "no empieza con --- en columna 0"})
            continue
        fin = re.search(r"\n---\s*\n", texto)
        if not fin:
            errores.append({"fichero": rel, "campo": "(frontmatter)", "mensaje": "sin delimitador de cierre --- en columna 0"})
            continue
        for linea in texto[4:fin.start()].splitlines():
            if linea[:1] in (" ", "\t"):
                errores.append({
                    "fichero": rel,
                    "campo": "(frontmatter)",
                    "mensaje": f"clave de primer nivel con sangría inicial: {linea.strip()[:40]!r}",
                })
                break
        cuerpo = texto[fin.end():]
        sangradas = [l for l in cuerpo.splitlines() if l.startswith("    ") and l.strip()]
        # Un bloque de código indentado es legítimo; una ficha entera sangrada no.
        if len(sangradas) > len(cuerpo.splitlines()) * 0.5:
            errores.append({
                "fichero": rel,
                "campo": "(cuerpo)",
                "mensaje": f"{len(sangradas)} líneas del cuerpo empiezan por 4 espacios: sangrado sistemático",
            })
    return {"tipo": "RESUMENES", "ficheros": revisados, "errores": errores, "avisos": []}


def validar_textos_oficiales() -> dict:
    """Comprueba la integridad de `06_indices/textos-oficiales.yaml`.

    Dos defectos convivieron meses sin que nada los detectara (TAREA-092): las
    entradas de NOR-017/018/050 seguían declarando `estado_vigencia: Vigente`
    después de que DEC-0011 retirara las fichas como catalogación errónea, y una
    `ruta_local` eliminada habría dejado una entrada de índice apuntando a un
    fichero inexistente. Se comprueba que cada copia local resuelva y que la
    vigencia declarada coincida con la de su ficha normativa.
    """
    errores = []
    indice = entradas_del_indice("textos-oficiales.yaml")
    normativa = entradas_del_indice("normativa.yaml")

    def recorrer(node):
        if isinstance(node, dict):
            if "ruta_corpus" in node:
                yield node
            else:
                for valor in node.values():
                    yield from recorrer(valor)

    revisados = 0
    for entrada in recorrer(indice):
        revisados += 1
        ruta_corpus = str(entrada.get("ruta_corpus", ""))
        identificador = ID_EN_NOMBRE.match(pathlib.Path(ruta_corpus).name)
        identificador = identificador.group(1) if identificador else None
        bloque_copia = entrada.get("texto_plano_local")
        ruta_local = bloque_copia.get("ruta_local") if isinstance(bloque_copia, dict) else None
        if ruta_local and not (RAIZ / ruta_local).exists():
            errores.append({
                "fichero": "06_indices/textos-oficiales.yaml",
                "campo": identificador or ruta_corpus,
                "mensaje": f"la copia local declarada no existe: {ruta_local}",
            })
        ficha = normativa.get(identificador) if identificador else None
        if ficha and normalizar(entrada.get("estado_vigencia")) != normalizar(ficha.get("estado_vigencia")):
            errores.append({
                "fichero": "06_indices/textos-oficiales.yaml",
                "campo": f"{identificador}.estado_vigencia",
                "mensaje": f"el índice dice {entrada.get('estado_vigencia')!r} y la ficha "
                           f"normativa dice {ficha.get('estado_vigencia')!r}",
            })
    return {"tipo": "TEXTOS-OFICIALES", "ficheros": revisados, "errores": errores, "avisos": []}


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida el corpus contra schemas/ y 06_indices/.")
    parser.add_argument("--json", action="store_true", help="salida JSON para integración continua")
    parser.add_argument("--tipo", choices=sorted(ENTIDADES), help="validar solo un tipo de entidad")
    parser.add_argument("--sin-avisos", action="store_true", help="omitir los avisos del informe")
    args = parser.parse_args()

    tipos = [args.tipo] if args.tipo else sorted(ENTIDADES)
    informes = [validar_tipo(t, ENTIDADES[t]) for t in tipos]
    if not args.tipo:
        informes.append(validar_referencias())
        informes.append(validar_desdoblamientos())
        informes.append(validar_correspondencia_textos())
        informes.append(validar_textos_locales())
        informes.append(validar_frontmatter_curricular())
        informes.append(validar_resumenes())
        informes.append(validar_textos_oficiales())
    total_errores = sum(len(i["errores"]) for i in informes)
    total_avisos = sum(len(i["avisos"]) for i in informes)

    if args.json:
        print(json.dumps({"informes": informes, "errores": total_errores, "avisos": total_avisos},
                         ensure_ascii=False, indent=2))
        return 1 if total_errores else 0

    for informe in informes:
        estado = "OK" if not informe["errores"] else f"{len(informe['errores'])} errores"
        print(f"\n## {informe['tipo']} — {informe['ficheros']} fichas · {estado}")
        for error in informe["errores"]:
            print(f"   ✗ {error['fichero']} [{error['campo']}] {error['mensaje']}")
        if not args.sin_avisos:
            for aviso in informe["avisos"]:
                print(f"   · {aviso['fichero']} [{aviso['campo']}] {aviso['mensaje']}")

    print(f"\n{'—' * 60}")
    print(f"Total: {total_errores} errores · {total_avisos} avisos")
    if total_errores:
        print("Los errores bloquean el cierre de tarea (AGENTS.md §15).")
    return 1 if total_errores else 0


if __name__ == "__main__":
    raise SystemExit(main())
