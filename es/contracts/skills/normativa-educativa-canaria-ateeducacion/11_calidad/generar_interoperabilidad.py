#!/usr/bin/env python3
"""Generate public semantic exports from canonical Markdown/YAML records."""

from __future__ import annotations

import argparse
import datetime
import json
import pathlib
import re
import sys
import xml.sax.saxutils
from typing import Any

import yaml


ROOT = pathlib.Path(__file__).resolve().parent.parent
PUBLIC_BASE = "https://ateeducacion.github.io/normativa_educativa_canaria/"
SCHEMA_CONTEXT = "https://schema.org/"
START_MARKER = "<!-- datos-estructurados:inicio -->"
END_MARKER = "<!-- datos-estructurados:fin -->"
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---", re.S)
LEGISLATION_PATH = ROOT / "docs" / "datos" / "legislacion.jsonld"
CURRICULA_PATH = ROOT / "docs" / "datos" / "curriculos.jsonld"
SOURCES_PATH = ROOT / "docs" / "datos" / "fuentes.jsonld"
CATALOG_PATH = ROOT / "docs" / "datos" / "catalogo.jsonld"
AKN_DIR = ROOT / "docs" / "datos" / "akoma-ntoso"
PILOT_PATH = ROOT / "11_calidad" / "akoma_ntoso_pilotos.yaml"
INDEX_HTML = ROOT / "docs" / "index.html"
STAGE_LABELS = {
    "infantil": "Educación Infantil",
    "primaria": "Educación Primaria",
    "eso": "Educación Secundaria Obligatoria",
    "bachillerato": "Bachillerato",
    "formacion-profesional": "Formación Profesional",
    "regimen-especial": "Régimen especial",
}


def normalize(value: Any) -> Any:
    """Convert PyYAML dates to the JSON-compatible ISO representation."""
    if isinstance(value, (datetime.datetime, datetime.date)):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: normalize(item) for key, item in value.items()}
    if isinstance(value, list):
        return [normalize(item) for item in value]
    return value


def load_frontmatter(path: pathlib.Path) -> dict[str, Any]:
    """Load the YAML object that opens a Markdown ficha."""
    match = FRONTMATTER.match(path.read_text(encoding="utf-8"))
    if match is None:
        raise ValueError(f"{path.relative_to(ROOT)} no contiene frontmatter YAML")
    data = normalize(yaml.safe_load(match.group(1)))
    if not isinstance(data, dict):
        raise ValueError(f"{path.relative_to(ROOT)} no contiene un objeto YAML")
    return data


def load_yaml_document(path: pathlib.Path) -> dict[str, Any]:
    """Load a standalone YAML document and require a mapping."""
    data = normalize(yaml.safe_load(path.read_text(encoding="utf-8")))
    if not isinstance(data, dict):
        raise ValueError(f"{path.relative_to(ROOT)} no contiene un objeto YAML")
    return data


def load_norms() -> list[tuple[pathlib.Path, dict[str, Any]]]:
    """Load normative frontmatter and retain its canonical repository path."""
    return [
        (path, load_frontmatter(path))
        for path in sorted(ROOT.glob("02_normativa/**/NOR-*.md"))
    ]


def load_curricula() -> list[tuple[pathlib.Path, dict[str, Any]]]:
    """Load canonical curricular YAML records."""
    return [
        (path, load_yaml_document(path))
        for path in sorted(ROOT.glob("03_curriculos/**/CUR-*.yaml"))
    ]


def load_sources() -> list[tuple[pathlib.Path, dict[str, Any]]]:
    """Load official-source frontmatter."""
    return [
        (path, load_frontmatter(path))
        for path in sorted(ROOT.glob("01_fuentes/**/FTE-*.md"))
    ]


def public_url(path: pathlib.Path) -> str:
    """Return a stable GitHub Pages URL for a repository path."""
    return PUBLIC_BASE + path.relative_to(ROOT).as_posix()


def legislation_ref(identifier: str, paths_by_id: dict[str, pathlib.Path]) -> dict[str, str]:
    """Build an internal semantic reference without inventing an official URI."""
    path = paths_by_id.get(identifier)
    if path is None:
        raise ValueError(f"La relación apunta a una norma inexistente: {identifier}")
    return {"@id": public_url(path), "@type": "Legislation"}


def legal_force(status: str) -> str | None:
    """Map the controlled status prefix to Schema.org legal-force terms."""
    if status.startswith(("Derogada parcialmente", "Parcialmente vigente")):
        return "https://schema.org/PartiallyInForce"
    if status.startswith(("Derogada", "Superada", "Sustituida", "Histórica")):
        return "https://schema.org/NotInForce"
    if status.startswith("Vigente"):
        return "https://schema.org/InForce"
    return None


def xml_text(value: str) -> str:
    """Escape text for Akoma Ntoso content."""
    return xml.sax.saxutils.escape(value, {"\"": "&quot;"})


def build_legislation() -> dict[str, Any]:
    """Build a Schema.org Legislation graph for every canonical normative record."""
    norms = load_norms()
    paths_by_id = {data["id"]: path for path, data in norms}
    graph = []

    for path, data in norms:
        identifiers: list[Any] = [
            {
                "@type": "PropertyValue",
                "propertyID": "identificador interno",
                "value": data["id"],
            }
        ]
        if data.get("uri_eli"):
            identifiers.append(
                {
                    "@type": "PropertyValue",
                    "propertyID": "ELI",
                    "value": data["uri_eli"],
                }
            )

        item: dict[str, Any] = {
            "@id": public_url(path),
            "@type": "Legislation",
            "name": data["titulo"],
            "alternateName": data["nombre_corto"],
            "identifier": identifiers,
            "legislationIdentifier": [data["id"]]
            + ([data["uri_eli"]] if data.get("uri_eli") else []),
            "legislationType": data["tipo_norma"],
            "legislationJurisdiction": {
                "@type": "AdministrativeArea",
                "name": "Comunidad Autónoma de Canarias"
                if data["ambito"] == "canarias"
                else data["ambito"],
            },
            "legislationPassedBy": {
                "@type": "Organization",
                "name": data["autoridad"],
            },
            "inLanguage": "es",
            "url": public_url(path),
            "sameAs": list(
                dict.fromkeys(
                    [data["url_oficial"]]
                    + ([data["uri_eli"]] if data.get("uri_eli") else [])
                )
            ),
        }

        for source, target in (
            ("fecha_disposicion", "legislationDate"),
            ("fecha_publicacion", "datePublished"),
        ):
            if data.get(source):
                item[target] = data[source]
        if data.get("temas"):
            item["keywords"] = data["temas"]
        force = legal_force(data["estado_vigencia"])
        if force:
            item["legislationLegalForce"] = {"@id": force}

        relations = data.get("relaciones") or {}
        for source, target in (
            ("modifica_a", "legislationAmends"),
            ("deroga_a", "legislationRepeals"),
        ):
            references = [
                legislation_ref(identifier, paths_by_id)
                for identifier in relations.get(source, [])
                if identifier.startswith("NOR-")
            ]
            if references:
                item[target] = references
        developed = [
            legislation_ref(identifier, paths_by_id)
            for identifier in relations.get("desarrolla_a", [])
            if identifier.startswith("NOR-")
        ]
        if developed:
            item["isBasedOn"] = developed
        graph.append(item)

    return {"@context": SCHEMA_CONTEXT, "@graph": graph}


def build_curricula(paths_by_norm: dict[str, pathlib.Path]) -> dict[str, Any]:
    """Build a Schema.org LearningResource graph for every curricular record."""
    graph = []
    for path, data in load_curricula():
        item: dict[str, Any] = {
            "@id": public_url(path),
            "@type": ["LearningResource", "Course"],
            "name": data["titulo"],
            "identifier": data["id"],
            "learningResourceType": "curriculum",
            "educationalLevel": STAGE_LABELS.get(data["etapa"], data["etapa"]),
            "about": data["materia"],
            "inLanguage": "es",
            "url": public_url(path),
            "sameAs": data["url_oficial"],
            "creativeWorkStatus": data["estado_extraccion"],
        }
        if data.get("cursos"):
            item["educationalUse"] = data["cursos"]
        if data.get("fecha_consulta"):
            item["dateModified"] = data["fecha_consulta"]
        if data.get("norma_base") and data["norma_base"] in paths_by_norm:
            item["isBasedOn"] = legislation_ref(data["norma_base"], paths_by_norm)
        graph.append(item)
    return {"@context": SCHEMA_CONTEXT, "@graph": graph}


def build_sources() -> dict[str, Any]:
    """Build a Schema.org WebPage graph for every official source record."""
    graph = []
    for path, data in load_sources():
        item: dict[str, Any] = {
            "@id": public_url(path),
            "@type": "WebPage",
            "name": data["titulo"],
            "identifier": data["id"],
            "url": data["url_oficial"],
            "sameAs": public_url(path),
            "inLanguage": "es",
            "publisher": {
                "@type": "Organization",
                "name": data["autoridad"],
            },
        }
        if data.get("tipo_fuente"):
            item["additionalType"] = data["tipo_fuente"]
        if data.get("fecha_consulta"):
            item["dateModified"] = data["fecha_consulta"]
        graph.append(item)
    return {"@context": SCHEMA_CONTEXT, "@graph": graph}


def load_pilots() -> list[dict[str, Any]]:
    """Load the reviewed Akoma Ntoso portion catalogue."""
    data = load_yaml_document(PILOT_PATH)
    pilots = data.get("pilotos")
    if not isinstance(pilots, list) or not pilots:
        raise ValueError("akoma_ntoso_pilotos.yaml debe declarar una lista de pilotos")
    return pilots


def pilot_kind(pilot: dict[str, Any]) -> str:
    """Return 'articulo' or the declared disposition kind of a pilot."""
    return pilot.get("tipo", "articulo")


def block_eid(pilot: dict[str, Any]) -> str:
    """Return the AKN eId of the reviewed portion."""
    kind = pilot_kind(pilot)
    if kind == "articulo":
        return f"art_{pilot['articulo']}"
    suffix = "adi" if kind == "disposicion_adicional" else "fin"
    return f"dis_{suffix}_{pilot['ordinal']}"


def file_stem(pilot: dict[str, Any]) -> str:
    """Return the public filename stem of a reviewed portion."""
    kind = pilot_kind(pilot)
    if kind == "articulo":
        return f"{pilot['id']}-articulo-{pilot['articulo']}"
    suffix = "adicional" if kind == "disposicion_adicional" else "final"
    return f"{pilot['id']}-disposicion-{suffix}-{pilot['ordinal']}"


def akn_path(pilot: dict[str, Any]) -> pathlib.Path:
    """Return the public XML path of a reviewed Akoma Ntoso portion."""
    return AKN_DIR / f"{file_stem(pilot)}.xml"


def pilot_label(pilot: dict[str, Any]) -> str:
    """Return a human-readable description of a reviewed portion."""
    kind = pilot_kind(pilot)
    if kind == "articulo":
        return f"{pilot['id']} artículo {pilot['articulo']}"
    suffix = "adicional" if kind == "disposicion_adicional" else "final"
    return f"{pilot['id']} disposición {suffix} {pilot['ordinal']}"


def render_akoma_ntoso(pilot: dict[str, Any], eli: str | None) -> str:
    """Render a reviewed article or disposition as an Akoma Ntoso 3.0 portion."""
    work = pilot["work_uri"]
    author = pilot["author_eid"]
    eid = block_eid(pilot)
    kind = pilot_kind(pilot)
    eli_line = (
        f'          <FRBRalias name="ELI" value="{xml_text(eli)}"/>\n' if eli else ""
    )
    paragraphs = []
    for index, paragraph in enumerate(pilot["parrafos"], start=1):
        num = paragraph.get("num")
        num_xml = f"\n          <num>{xml_text(num)}</num>" if num else ""
        texts = paragraph["text"] if isinstance(paragraph["text"], list) else [paragraph["text"]]
        body = "".join(f"<p>{xml_text(text)}</p>" for text in texts)
        paragraphs.append(
            f"        <paragraph eId=\"{eid}__para_{index}\">"
            f"{num_xml}\n"
            "          <content>"
            f"{body}"
            "</content>\n"
            "        </paragraph>"
        )
    if kind == "articulo":
        block_open = f'<article eId="{eid}">'
        block_close = "</article>"
    else:
        name = "disposicion-adicional" if kind == "disposicion_adicional" else "disposicion-final"
        block_open = f'<hcontainer eId="{eid}" name="{name}">'
        block_close = "</hcontainer>"
    heading_xml = f"\n        <heading>{xml_text(pilot['heading'])}</heading>" if pilot.get("heading") else ""
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<akomaNtoso xmlns="http://docs.oasis-open.org/legaldocml/ns/akn/3.0">
  <portion includedIn="{xml_text(work)}">
    <meta>
      <identification source="#corpus">
        <FRBRWork>
          <FRBRthis value="{xml_text(work)}/!{eid}"/>
          <FRBRuri value="{xml_text(work)}"/>
{eli_line}          <FRBRdate date="{pilot["work_date"]}" name="Generation"/>
          <FRBRauthor href="#{author}"/>
          <FRBRcountry value="{pilot["country"]}"/>
          <FRBRnumber value="{xml_text(str(pilot["frbr_number"]))}"/>
          <FRBRname value="{xml_text(pilot["frbr_name"])}"/>
        </FRBRWork>
        <FRBRExpression>
          <FRBRthis value="{xml_text(work)}/spa@/!{eid}"/>
          <FRBRuri value="{xml_text(work)}/spa@"/>
          <FRBRdate date="{pilot["expression_date"]}" name="Publication"/>
          <FRBRauthor href="#{author}"/>
          <FRBRlanguage language="spa"/>
        </FRBRExpression>
        <FRBRManifestation>
          <FRBRthis value="{xml_text(work)}/spa@/xml/!{eid}"/>
          <FRBRuri value="{xml_text(work)}/spa@/xml"/>
          <FRBRdate date="2026-08-22" name="Generation"/>
          <FRBRauthor href="#corpus"/>
        </FRBRManifestation>
      </identification>
      <references source="#corpus">
        <TLCOrganization eId="{author}" href="{xml_text(pilot["author_href"])}" showAs="{xml_text(pilot["author_show"])}"/>
        <TLCOrganization eId="corpus" href="https://github.com/ateeducacion/normativa_educativa_canaria" showAs="Normativa Educativa Canaria"/>
      </references>
    </meta>
    <portionBody>
      {block_open}
        <num>{xml_text(pilot["num"])}</num>{heading_xml}
{chr(10).join(paragraphs)}
      {block_close}
    </portionBody>
  </portion>
</akomaNtoso>
'''


def build_catalog(
    legislation: dict[str, Any],
    pilots: list[dict[str, Any]],
) -> dict[str, Any]:
    """Describe the public corpus as a Schema.org Dataset for discovery clients."""
    dates = [
        item.get("datePublished")
        for item in legislation["@graph"]
        if item.get("datePublished")
    ]
    distributions = [
        ("Inventario del corpus", "datos/inventario.json", "application/json"),
        ("Metadatos de legislación", "datos/legislacion.jsonld", "application/ld+json"),
        ("Metadatos de currículos", "datos/curriculos.jsonld", "application/ld+json"),
        ("Metadatos de fuentes", "datos/fuentes.jsonld", "application/ld+json"),
        ("Índice normativo", "06_indices/normativa.yaml", "application/yaml"),
        ("Guía para modelos de lenguaje", "llms.txt", "text/plain"),
    ]
    for pilot in pilots:
        distributions.append(
            (
                f"Piloto Akoma Ntoso {pilot_label(pilot)}",
                f"datos/akoma-ntoso/{file_stem(pilot)}.xml",
                "application/akn+xml",
            )
        )
    dataset: dict[str, Any] = {
        "@context": SCHEMA_CONTEXT,
        "@id": PUBLIC_BASE + "#dataset",
        "@type": "Dataset",
        "name": "Normativa Educativa Canaria",
        "description": (
            "Corpus abierto y versionado de normativa y currículos educativos de "
            "Canarias, con fuentes oficiales, relaciones y metadatos para reutilización."
        ),
        "url": PUBLIC_BASE,
        "inLanguage": "es",
        "isAccessibleForFree": True,
        "license": "https://creativecommons.org/publicdomain/zero/1.0/",
        "creator": {
            "@type": "Organization",
            "name": "Área de Tecnología Educativa",
        },
        "publisher": {
            "@type": "Organization",
            "name": "Área de Tecnología Educativa",
        },
        "keywords": [
            "normativa educativa",
            "Canarias",
            "currículo",
            "datos jurídicos",
            "educación",
        ],
        "includedInDataCatalog": {
            "@type": "DataCatalog",
            "name": "Catálogo público del corpus",
            "url": PUBLIC_BASE + "datos/catalogo.jsonld",
        },
        "distribution": [
            {
                "@type": "DataDownload",
                "name": name,
                "contentUrl": PUBLIC_BASE + path,
                "encodingFormat": media_type,
            }
            for name, path, media_type in distributions
        ],
    }
    if dates:
        dataset["temporalCoverage"] = f"{min(dates)}/{max(dates)}"
    return dataset


def replace_html_block(text: str, dataset: dict[str, Any]) -> str:
    """Replace the single generated JSON-LD block in the public home page."""
    if text.count(START_MARKER) != 1 or text.count(END_MARKER) != 1:
        raise ValueError("docs/index.html debe contener un único bloque de datos estructurados")
    script = "\n".join(
        [
            START_MARKER,
            '    <script type="application/ld+json">',
            json.dumps(dataset, ensure_ascii=False, indent=2, sort_keys=True),
            "    </script>",
            f"    {END_MARKER}",
        ]
    )
    before, remainder = text.split(START_MARKER, 1)
    _, after = remainder.split(END_MARKER, 1)
    return f"{before}{script}{after}"


def expected_files() -> dict[pathlib.Path, str]:
    """Return all generated semantic exports and their expected content."""
    legislation = build_legislation()
    paths_by_norm = {data["id"]: path for path, data in load_norms()}
    eli_by_id = {
        data["id"]: data.get("uri_eli")
        for _, data in load_norms()
    }
    curricula = build_curricula(paths_by_norm)
    sources = build_sources()
    pilots = load_pilots()
    catalog = build_catalog(legislation, pilots)
    json_options = {"ensure_ascii": False, "indent": 2, "sort_keys": True}
    files = {
        LEGISLATION_PATH: json.dumps(legislation, **json_options) + "\n",
        CURRICULA_PATH: json.dumps(curricula, **json_options) + "\n",
        SOURCES_PATH: json.dumps(sources, **json_options) + "\n",
        CATALOG_PATH: json.dumps(catalog, **json_options) + "\n",
        INDEX_HTML: replace_html_block(INDEX_HTML.read_text(encoding="utf-8"), catalog),
    }
    for pilot in pilots:
        files[akn_path(pilot)] = render_akoma_ntoso(pilot, eli_by_id.get(pilot["id"]))
    return files


def write_files(files: dict[pathlib.Path, str]) -> None:
    """Write generated files, creating output directories when needed."""
    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(f"Actualizado: {path.relative_to(ROOT)}")


def check_files(files: dict[pathlib.Path, str]) -> int:
    """Fail if a generated semantic output is missing or stale."""
    stale = [
        path.relative_to(ROOT)
        for path, expected in files.items()
        if not path.exists() or path.read_text(encoding="utf-8") != expected
    ]
    if not stale:
        print("Exportaciones interoperables actualizadas.")
        return 0
    print("Exportaciones interoperables desactualizadas:", file=sys.stderr)
    for path in stale:
        print(f"- {path}", file=sys.stderr)
    print(
        "Ejecute: python3 11_calidad/generar_interoperabilidad.py --write",
        file=sys.stderr,
    )
    return 1


def main() -> int:
    """Generate or check the public semantic export layer."""
    parser = argparse.ArgumentParser(
        description="Genera metadatos JSON-LD y los pilotos Akoma Ntoso."
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="Actualiza los archivos.")
    mode.add_argument("--check", action="store_true", help="Comprueba sin escribir.")
    args = parser.parse_args()
    files = expected_files()
    if args.write:
        write_files(files)
        return 0
    return check_files(files)


if __name__ == "__main__":
    raise SystemExit(main())
