"""Rutas de recursos y configuración (Windows, macOS .app, desarrollo)."""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

NOMBRE_APP = "Anonimizador-Trifuerza"


def dir_recursos() -> Path:
    """Archivos empaquetados (lista blanca, modelo spaCy). Solo lectura en onefile."""
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)
    return Path(__file__).parent


def dir_config() -> Path:
    """Donde leer/escribir reemplazos.json del usuario."""
    if getattr(sys, "frozen", False):
        exe = Path(sys.executable)
        if sys.platform == "darwin" and exe.parent.name == "MacOS":
            d = Path.home() / "Library" / "Application Support" / NOMBRE_APP
            d.mkdir(parents=True, exist_ok=True)
            return d
        return exe.parent
    return Path(__file__).parent


def ruta_lista_blanca() -> Path:
    for candidato in (dir_recursos() / "lista_blanca.json",
                      dir_config() / "lista_blanca.json"):
        if candidato.exists():
            return candidato
    return dir_recursos() / "lista_blanca.json"


def ruta_reemplazos() -> Path:
    destino = dir_config() / "reemplazos.json"
    if not destino.exists():
        origen = dir_recursos() / "reemplazos.json"
        if origen.exists() and origen != destino:
            shutil.copy2(origen, destino)
    return destino


def _directorios_modelo_spacy(base: Path) -> list[Path]:
    """Rutas con config.cfg (el paquete pip anida es_core_news_sm-X.Y.Z/)."""
    candidatos: list[Path] = []
    modelo_dir = base / "es_core_news_sm"
    if not modelo_dir.is_dir():
        return candidatos
    for sub in sorted(modelo_dir.iterdir()):
        if sub.is_dir() and (sub / "config.cfg").exists():
            candidatos.append(sub)
    if (modelo_dir / "config.cfg").exists():
        candidatos.append(modelo_dir)
    return candidatos


def rutas_modelo_spacy() -> list[Path]:
    return _directorios_modelo_spacy(dir_recursos())


def ruta_preferencias() -> Path:
    return dir_config() / "preferencias.json"


def cargar_preferencias() -> dict:
    ruta = ruta_preferencias()
    if ruta.exists():
        try:
            datos = json.loads(ruta.read_text(encoding="utf-8"))
            if isinstance(datos, dict):
                return datos
        except Exception:
            pass
    return {}


def guardar_preferencias(preferencias: dict):
    ruta_preferencias().write_text(
        json.dumps(preferencias, ensure_ascii=False, indent=2), encoding="utf-8")
