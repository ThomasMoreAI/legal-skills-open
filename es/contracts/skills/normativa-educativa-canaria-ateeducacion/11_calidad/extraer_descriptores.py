#!/usr/bin/env python3
"""Extrae los descriptores operativos del perfil de salida desde el texto oficial.

Los decretos de currículo repiten un bloque competencial por cada competencia y
cada curso en que se imparte la materia:

    Competencia específica
    N. <enunciado oficial>
    Descriptores operativos de las competencias clave[. Perfil de salida]
    <códigos, repartidos en varias líneas>
    Criterios de evaluación

La marca aparece con y sin «Perfil de salida» según la etapa, así que ese sufijo
es opcional; exigirlo dejaba fuera 327 de 637 bloques.

Uso:

    python3 11_calidad/extraer_descriptores.py --auditar     # contrasta las fichas
    python3 11_calidad/extraer_descriptores.py --cobertura   # bloques por decreto

El emparejamiento con la ficha se hace por el texto del enunciado, que es largo y
distintivo, con una similitud mínima alta. Por debajo de ese umbral no se compara:
se reporta aparte, para no arriesgar una comparación falsa.

Dependencias: pyyaml.
"""

from __future__ import annotations

import argparse
import difflib
import json
import pathlib
import re
import sys
import unicodedata

sys.path = [p for p in sys.path if p]  # el cwd rompe la búsqueda de módulos en algunos entornos

try:
    import yaml
except ImportError:
    sys.exit("Falta pyyaml. Instala con: pip install pyyaml")

RAIZ = pathlib.Path(__file__).resolve().parent.parent
TEXTOS = RAIZ / "07_corpus_ia/textos-completos"

# norma base -> copia local del texto oficial
FUENTES = {
    "NOR-005": "texto-oficial-NOR-005-decreto-30-2023.txt",
    "NOR-043": "texto-oficial-NOR-043-decreto-211-2022-primaria.txt",
    "NOR-047": "texto-oficial-NOR-047-decreto-196-2022-infantil.txt",
}

MARCA = re.compile(
    r"Descriptores operativos de las\s*competencias clave(?:\.\s*Perfil de salida)?", re.I)
FIN = re.compile(r"Criterios de evaluaci", re.I)
# Bachillerato usa subcódigos decimales (CPSAA1.1, CCEC3.2) que la enseñanza
# básica no tiene; sin el sufijo opcional se truncaban a CPSAA1 y CCEC3.
CODIGO = re.compile(r"\b(?:CCL|CP|STEM|CD|CPSAA|CC|CE|CCEC)\d(?:\.\d)?\b")
ENUNCIADO = re.compile(r"(?:^|\n)\s*(\d+)\.\s*([^\n].*?)\s*$", re.S)
CURSO = re.compile(r"(\d\.º\s*(?:ESO|Bachillerato))", re.I)
RUIDO = re.compile(
    r"=== Página \d+ ===|boc-a-[\w-]+|https://sede\S+|Boletín Oficial de Canarias núm\.[^\n]*")
UMBRAL = 0.90


def limpiar(texto: str) -> str:
    """Normaliza para comparar: minúsculas, sin tildes ni puntuación."""
    texto = unicodedata.normalize("NFD", str(texto).lower())
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9 ]+", " ", re.sub(r"\s+", " ", texto)).strip()


def bloques(norma: str) -> list[dict]:
    """Devuelve [{numero, enunciado, curso, descriptores}] del decreto indicado."""
    ruta = TEXTOS / FUENTES[norma]
    plano = re.sub(r"[ \t]+", " ", RUIDO.sub("\n", ruta.read_text(encoding="utf-8", errors="replace")))

    encontrados = []
    for marca in MARCA.finditer(plano):
        fin = FIN.search(plano, marca.end())
        if not fin:
            continue
        codigos = list(dict.fromkeys(CODIGO.findall(plano[marca.end():fin.start()])))
        if not codigos:
            continue
        previo = plano[max(0, marca.start() - 1500):marca.start()]
        corte = previo.lower().rfind("competencia específica")
        if corte == -1:
            continue
        enun = ENUNCIADO.search(previo[corte + len("competencia específica"):])
        if not enun:
            continue
        cursos = CURSO.findall(plano[max(0, marca.start() - 12000):marca.start()])
        encontrados.append({
            "numero": int(enun.group(1)),
            "enunciado": re.sub(r"\s+", " ", enun.group(2)).strip(),
            "curso": cursos[-1] if cursos else "?",
            "descriptores": codigos,
        })
    return encontrados


def fichas_con_descriptores():
    """Fichas curriculares cuyas competencias ya llevan descriptores volcados."""
    for fichero in sorted(RAIZ.glob("03_curriculos/**/CUR-*.yaml")):
        datos = yaml.safe_load(fichero.read_text(encoding="utf-8"))
        if not isinstance(datos, dict):
            continue
        comps = (datos.get("elementos") or {}).get("competencias_especificas") or []
        if comps and isinstance(comps[0], dict) and "descriptores" in comps[0]:
            yield fichero, datos, comps


def indexar(texto: str) -> tuple[str, list[int]]:
    """Devuelve el texto reducido a letras y dígitos, y el mapa a las posiciones originales.

    Quitar tildes, puntuación y **todos los espacios** absorbe las diferencias que
    introduce la conversión del PDF —guiones de final de línea, saltos dentro de
    una frase— y también variantes ortográficas como «medio ambiente» frente a
    «medioambiente», que de otro modo rompen el anclaje.
    """
    reducido, mapa = [], []
    for posicion, caracter in enumerate(texto):
        base = unicodedata.normalize("NFD", caracter.lower())
        base = "".join(c for c in base if unicodedata.category(c) != "Mn")
        if base.isalnum():
            reducido.append(base)
            mapa.extend([posicion] * len(base))
    return "".join(reducido), mapa


def descriptores_tras(plano: str, indice: tuple[str, list[int]], enunciado: str,
                      palabras: int = 12) -> dict:
    """Descriptores que el decreto asigna a un enunciado, por curso.

    Se ancla en el texto de la competencia y no en la estructura del documento: la
    conversión del PDF entremezcla las celdas de la tabla, y unas veces el
    enunciado precede a la marca de descriptores y otras la sigue. Buscar los
    códigos que van tras el enunciado y antes de «Criterios de evaluación»
    funciona con ambas disposiciones.

    El decreto repite el bloque por cada curso en que se imparte la materia, así
    que se devuelven todas las apariciones indexadas por curso.
    """
    reducido, mapa = indice
    ancla, _ = indexar(" ".join(str(enunciado).split()[:palabras]))
    if len(ancla) < 30:
        return {}

    por_curso: dict[str, list[str]] = {}
    desde = 0
    while True:
        encontrado = reducido.find(ancla, desde)
        if encontrado == -1:
            break
        desde = encontrado + 1
        fin_ancla = mapa[min(encontrado + len(ancla), len(mapa) - 1)]
        fin = FIN.search(plano, fin_ancla)
        if not fin:
            continue
        codigos = list(dict.fromkeys(CODIGO.findall(plano[fin_ancla:fin.start()])))
        if not codigos:
            continue
        inicio = mapa[encontrado]
        cursos = CURSO.findall(plano[max(0, inicio - 12000):inicio])
        clave = cursos[-1] if cursos else "?"
        # Sin cabecera de curso a la vista, todas las apariciones caerían bajo la
        # misma clave y `setdefault` se quedaría solo con la primera, ocultando
        # justo las variantes por curso que interesan. Se numeran para conservarlas.
        if clave in por_curso and por_curso[clave] != codigos:
            n = 2
            while f"{clave} ({n})" in por_curso:
                n += 1
            clave = f"{clave} ({n})"
        por_curso.setdefault(clave, codigos)
    return por_curso


def auditar(norma: str = "NOR-005") -> list[dict]:
    """Contrasta cada competencia de las fichas con el texto oficial."""
    plano = re.sub(r"[ \t]+", " ",
                   RUIDO.sub("\n", (TEXTOS / FUENTES[norma]).read_text(encoding="utf-8",
                                                                       errors="replace")))
    indice = indexar(plano)
    informe = []
    for _, datos, comps in fichas_con_descriptores():
        resultado = {"id": datos["id"], "materia": datos.get("materia"),
                     "cursos": datos.get("cursos") or [], "competencias": []}
        for comp in comps:
            por_curso = descriptores_tras(plano, indice, comp.get("enunciado_oficial") or "")
            if not por_curso:
                resultado["competencias"].append({
                    "codigo": comp["codigo"], "estado": "sin-emparejar",
                    "ficha": comp["descriptores"]})
                continue
            union = {d for lista in por_curso.values() for d in lista}
            comun = set.intersection(*[set(v) for v in por_curso.values()])
            declarado = comp["descriptores"]

            if isinstance(declarado, dict):
                # Formato DEC-0008: se compara curso a curso, que es lo que
                # permite detectar si se copió la lista del curso equivocado.
                desajustes = []
                for curso, codigos in declarado.items():
                    oficial = por_curso.get(curso)
                    if oficial is None:
                        desajustes.append(f"{curso}: no localizado en la fuente")
                    elif sorted(codigos) != sorted(oficial):
                        sobran = sorted(set(codigos) - set(oficial))
                        faltan = sorted(set(oficial) - set(codigos))
                        desajustes.append(
                            f"{curso}: sobran {sobran or '—'}, faltan {faltan or '—'}")
                sin_declarar = sorted(set(por_curso) - set(declarado))
                estado = "coincide-por-curso" if not desajustes and not sin_declarar else "diverge"
                entrada = {"codigo": comp["codigo"], "estado": estado,
                           "desajustes": desajustes, "cursos_sin_declarar": sin_declarar}
            else:
                # Forma transitoria: lista plana pendiente de migrar.
                if any(sorted(v) == sorted(declarado) for v in por_curso.values()):
                    estado = "lista-plana-coincide"
                elif sorted(union) == sorted(declarado):
                    estado = "lista-plana-union"
                else:
                    estado = "diverge"
                entrada = {"codigo": comp["codigo"], "estado": estado, "ficha": declarado,
                           "sobran": sorted(set(declarado) - union),
                           "faltan_en_todos": sorted(comun - set(declarado))}

            entrada["oficial_por_curso"] = por_curso
            entrada["cursos_distintos"] = len({tuple(sorted(v)) for v in por_curso.values()}) > 1
            resultado["competencias"].append(entrada)
        informe.append(resultado)
    return informe


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--auditar", action="store_true", help="contrastar las fichas con la fuente")
    parser.add_argument("--cobertura", action="store_true", help="bloques localizados por decreto")
    parser.add_argument("--json", action="store_true", help="salida JSON")
    args = parser.parse_args()

    if args.cobertura or not (args.auditar or args.json):
        for norma in FUENTES:
            if (TEXTOS / FUENTES[norma]).exists():
                b = bloques(norma)
                cursos = sorted({x["curso"] for x in b})
                print(f"{norma}: {len(b)} bloques · cursos detectados: {', '.join(cursos)}")
        if not args.auditar:
            return 0

    informe = auditar()
    if args.json:
        print(json.dumps(informe, ensure_ascii=False, indent=1))
        return 0

    import collections
    est = collections.Counter()
    for ficha in informe:
        for comp in ficha["competencias"]:
            est[comp["estado"]] += 1
    total = sum(est.values())
    print(f"\n{len(informe)} fichas · {total} competencias")
    for clave, valor in est.most_common():
        print(f"  {valor:3} ({100 * valor / total:4.1f}%)  {clave}")
    print("\nDivergencias:")
    for ficha in informe:
        for comp in ficha["competencias"]:
            if comp["estado"] != "diverge":
                continue
            print(f"  {ficha['id']} {comp['codigo']} — {ficha['materia']}")
            for linea in comp.get("desajustes", []):
                print(f"      {linea}")
            if comp.get("cursos_sin_declarar"):
                print(f"      cursos en la fuente sin declarar: {comp['cursos_sin_declarar']}")
            if comp.get("sobran"):
                print(f"      sobran: {comp['sobran']}")
            if comp.get("faltan_en_todos"):
                print(f"      faltan: {comp['faltan_en_todos']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
