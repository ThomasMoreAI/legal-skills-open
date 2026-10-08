#!/usr/bin/env python3
"""Generate the public corpus inventory from canonical YAML indexes."""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from collections import Counter
from typing import Any

import yaml


ROOT = pathlib.Path(__file__).resolve().parent.parent
START_MARKER = "<!-- inventario-corpus:inicio -->"
END_MARKER = "<!-- inventario-corpus:fin -->"
PUBLIC_INVENTORY = ROOT / "docs" / "datos" / "inventario.json"
INDEX_PATHS = {
    "fuentes": ROOT / "06_indices" / "fuentes.yaml",
    "normativa": ROOT / "06_indices" / "normativa.yaml",
    "curriculos": ROOT / "06_indices" / "curriculos.yaml",
    "relaciones": ROOT / "06_indices" / "relaciones.yaml",
    "chunks": ROOT / "06_indices" / "chunks.yaml",
    "tareas": ROOT / "06_indices" / "tareas.yaml",
}
ID_PATTERN = re.compile(r"^(?P<prefix>[A-Z]+)-(?P<number>\d+)$")
TEXT_PATTERN = re.compile(r"^texto-oficial-(?P<kind>NOR|CUR)-\d+.*\.txt$")


def load_mapping(path: pathlib.Path) -> dict[str, Any]:
    """Load an index and require a top-level mapping."""
    with path.open(encoding="utf-8") as stream:
        data = yaml.safe_load(stream) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path.relative_to(ROOT)} debe contener un objeto YAML")
    return data


def id_sort_key(identifier: str) -> tuple[str, int, str]:
    """Sort corpus identifiers by prefix and numeric component."""
    match = ID_PATTERN.fullmatch(identifier)
    if match is None:
        return identifier, -1, identifier
    return match.group("prefix"), int(match.group("number")), identifier


def summarize_index(data: dict[str, Any]) -> dict[str, Any]:
    """Return deterministic count and identifier bounds for an index."""
    identifiers = sorted(data, key=id_sort_key)
    return {
        "total": len(identifiers),
        "primer_id": identifiers[0] if identifiers else None,
        "ultimo_id": identifiers[-1] if identifiers else None,
    }


def sorted_counter(values: list[str]) -> dict[str, int]:
    """Return stable counters suitable for JSON and Markdown output."""
    return dict(sorted(Counter(values).items()))


def build_inventory() -> dict[str, Any]:
    """Build the inventory solely from tracked canonical sources."""
    indexes = {name: load_mapping(path) for name, path in INDEX_PATHS.items()}
    curriculos = indexes["curriculos"]
    tareas = indexes["tareas"]

    local_texts = Counter()
    text_dir = ROOT / "07_corpus_ia" / "textos-completos"
    for path in text_dir.glob("*.txt"):
        match = TEXT_PATTERN.fullmatch(path.name)
        if match:
            local_texts[match.group("kind")] += 1

    return {
        "version_esquema": 1,
        "fuente": "06_indices/",
        "entidades": {
            name: summarize_index(indexes[name])
            for name in ("fuentes", "normativa", "curriculos", "relaciones", "chunks", "tareas")
        },
        "curriculos": {
            "por_etapa": sorted_counter(
                [str(item.get("etapa", "sin-etapa")) for item in curriculos.values()]
            ),
            "por_estado_extraccion": sorted_counter(
                [
                    str(item.get("estado_extraccion", "sin-estado"))
                    for item in curriculos.values()
                ]
            ),
        },
        "tareas": {
            "por_estado": sorted_counter(
                [str(item.get("estado", "Sin estado")) for item in tareas.values()]
            )
        },
        "textos_oficiales_locales": {
            "total": sum(local_texts.values()),
            "normativa": local_texts["NOR"],
            "curriculos": local_texts["CUR"],
        },
    }


def id_range(summary: dict[str, Any]) -> str:
    """Format an identifier range without implying contiguous identifiers."""
    first = summary["primer_id"]
    last = summary["ultimo_id"]
    if first is None:
        return "sin identificadores"
    if first == last:
        return str(first)
    return f"{first} a {last}, con posibles huecos reservados"


def format_counter(counter: dict[str, int]) -> str:
    """Format a counter as a concise Spanish list."""
    return ", ".join(f"{key}: {value}" for key, value in counter.items())


def render_readme(inventory: dict[str, Any]) -> str:
    """Render the generated README inventory block."""
    entities = inventory["entidades"]
    texts = inventory["textos_oficiales_locales"]
    return "\n".join(
        [
            START_MARKER,
            "_Sección generada desde los índices canónicos; no se edita manualmente._",
            "",
            f"- Fuentes: **{entities['fuentes']['total']}** ({id_range(entities['fuentes'])}).",
            f"- Normativa: **{entities['normativa']['total']}** ({id_range(entities['normativa'])}).",
            f"- Currículos: **{entities['curriculos']['total']}** ({id_range(entities['curriculos'])}); "
            f"{format_counter(inventory['curriculos']['por_etapa'])}.",
            f"- Relaciones: **{entities['relaciones']['total']}** ({id_range(entities['relaciones'])}).",
            f"- Chunks IA: **{entities['chunks']['total']}** ({id_range(entities['chunks'])}).",
            f"- Tareas: **{entities['tareas']['total']}**; "
            f"{format_counter(inventory['tareas']['por_estado'])}.",
            f"- Copias locales de textos oficiales: **{texts['total']}** "
            f"(normativa: {texts['normativa']}; currículos: {texts['curriculos']}).",
            "- Inventario legible por máquinas: "
            "[docs/datos/inventario.json](docs/datos/inventario.json).",
            END_MARKER,
        ]
    )


def render_llms(inventory: dict[str, Any]) -> str:
    """Render the generated llms.txt inventory block."""
    entities = inventory["entidades"]
    texts = inventory["textos_oficiales_locales"]
    tick = chr(96)
    return "\n".join(
        [
            START_MARKER,
            f"Esta sección se genera desde {tick}06_indices/{tick}; los huecos de "
            "identificadores se conservan y no implican entidades ausentes.",
            "",
            f"- {entities['fuentes']['total']} fuentes ({id_range(entities['fuentes'])}).",
            f"- {entities['normativa']['total']} normas ({id_range(entities['normativa'])}).",
            f"- {entities['curriculos']['total']} currículos ({id_range(entities['curriculos'])}); "
            f"{format_counter(inventory['curriculos']['por_etapa'])}.",
            f"- {entities['relaciones']['total']} relaciones ({id_range(entities['relaciones'])}).",
            f"- {entities['chunks']['total']} chunks IA ({id_range(entities['chunks'])}).",
            f"- {entities['tareas']['total']} tareas; "
            f"{format_counter(inventory['tareas']['por_estado'])}.",
            f"- {texts['total']} copias locales de textos oficiales "
            f"(normativa: {texts['normativa']}; currículos: {texts['curriculos']}).",
            "- [Inventario JSON público](docs/datos/inventario.json): resumen derivado "
            "para clientes automáticos.",
            END_MARKER,
        ]
    )


def replace_generated_block(text: str, replacement: str, path: pathlib.Path) -> str:
    """Replace exactly one generated block while preserving the rest of a file."""
    if text.count(START_MARKER) != 1 or text.count(END_MARKER) != 1:
        raise ValueError(
            f"{path.relative_to(ROOT)} debe contener un único bloque de inventario"
        )
    before, remainder = text.split(START_MARKER, 1)
    _, after = remainder.split(END_MARKER, 1)
    return f"{before}{replacement}{after}"


def expected_files(inventory: dict[str, Any]) -> dict[pathlib.Path, str]:
    """Return every generated file and its expected content."""
    readme = ROOT / "README.md"
    llms = ROOT / "llms.txt"
    return {
        readme: replace_generated_block(
            readme.read_text(encoding="utf-8"), render_readme(inventory), readme
        ),
        llms: replace_generated_block(
            llms.read_text(encoding="utf-8"), render_llms(inventory), llms
        ),
        PUBLIC_INVENTORY: json.dumps(
            inventory, ensure_ascii=False, indent=2, sort_keys=True
        )
        + "\n",
    }


def write_files(files: dict[pathlib.Path, str]) -> None:
    """Write generated files."""
    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(f"Actualizado: {path.relative_to(ROOT)}")


def check_files(files: dict[pathlib.Path, str]) -> int:
    """Report stale or missing generated files."""
    stale = []
    for path, expected in files.items():
        if not path.exists() or path.read_text(encoding="utf-8") != expected:
            stale.append(path.relative_to(ROOT))
    if not stale:
        print("Inventario público actualizado.")
        return 0
    print("Inventario público desactualizado:", file=sys.stderr)
    for path in stale:
        print(f"- {path}", file=sys.stderr)
    print(
        "Ejecute: python3 11_calidad/generar_inventario.py --write",
        file=sys.stderr,
    )
    return 1


def main() -> int:
    """Run the inventory generator or freshness check."""
    parser = argparse.ArgumentParser(
        description="Genera y valida el inventario público del corpus."
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="Actualiza los archivos.")
    mode.add_argument("--check", action="store_true", help="Comprueba sin escribir.")
    args = parser.parse_args()

    inventory = build_inventory()
    files = expected_files(inventory)
    if args.write:
        write_files(files)
        return 0
    return check_files(files)


if __name__ == "__main__":
    raise SystemExit(main())
