#!/usr/bin/env python3
"""
Agrega/actualiza el bloque legal en research/catalog.json.
Idempotente: borra entradas con id legal_* antes de re-insertar.
"""
import json
import os
from pathlib import Path

CATALOG = Path("/Volumes/Storage/sistemia-skills-mx/research/catalog.json")
BASE = Path("/Volumes/Storage/sistemia-skills-mx/research")

LEGAL_SOURCES = [
    # ── SAT — CFDI 4.0 ────────────────────────────────────────────────
    {"id": "sat_cfdi40_xsd",       "institution": "SAT", "name": "CFDI 4.0 — Esquema XSD principal",            "year": 2022, "topics": ["cfdi", "factura_electronica"], "geography": "nacional", "granularity": "documento_xml", "format": "xsd", "path": "sat/cfdi-4/cfdv40.xsd"},
    {"id": "sat_cfdi40_catalogos", "institution": "SAT", "name": "CFDI 4.0 — Catálogos (régimen/uso/forma pago)", "year": 2022, "topics": ["cfdi", "factura_electronica"], "geography": "nacional", "granularity": "catalogo", "format": "xsd", "path": "sat/cfdi-4/catCFDI.xsd"},
    {"id": "sat_cfdi40_tipos",     "institution": "SAT", "name": "CFDI 4.0 — Tipos de datos",                     "year": 2022, "topics": ["cfdi", "factura_electronica"], "geography": "nacional", "granularity": "documento_xml", "format": "xsd", "path": "sat/cfdi-4/tdCFDI.xsd"},

    # ── SAT — RMF 2026 ────────────────────────────────────────────────
    {"id": "sat_rmf_2026",       "institution": "SAT", "name": "Resolución Miscelánea Fiscal 2026",                 "year": 2026, "topics": ["sat_tramites", "rfc", "obligaciones_fiscales"], "geography": "nacional", "granularity": "norma", "format": "pdf", "path": "sat/rmf-2026/RMF_2026.pdf"},
    {"id": "sat_rmf_2026_anexo1", "institution": "SAT", "name": "RMF 2026 Anexo 1 — Formas oficiales",              "year": 2026, "topics": ["sat_tramites", "rfc"], "geography": "nacional", "granularity": "anexo", "format": "pdf", "path": "sat/rmf-2026/Anexo-1-RMF-2026.pdf"},
    {"id": "sat_rmf_2026_anexo2", "institution": "SAT", "name": "RMF 2026 Anexo 2 — Trámites fiscales (fichas)",    "year": 2026, "topics": ["sat_tramites"], "geography": "nacional", "granularity": "anexo", "format": "pdf", "path": "sat/rmf-2026/Anexo-2-RMF-2026.pdf"},
    {"id": "sat_rmf_2026_anexo29","institution": "SAT", "name": "RMF 2026 Anexo 29 — Validaciones CFDI/LRFC/LCO",   "year": 2026, "topics": ["cfdi", "sat_tramites"], "geography": "nacional", "granularity": "anexo", "format": "pdf", "path": "sat/rmf-2026/Anexo-29-RMF-2026.pdf"},

    # ── SAT — Listas 69-B y 69 CFF ────────────────────────────────────
    {"id": "sat_69b_listado_completo", "institution": "SAT", "name": "Lista 69-B — Listado completo (presuntos + definitivos + desvirtuados + sentencias)", "year": 2026, "topics": ["riesgo_proveedor", "antifraude"], "geography": "nacional", "granularity": "contribuyente_rfc", "format": "csv", "path": "sat/listas-negras/69-B_Listado_Completo.csv"},
    {"id": "sat_69b_definitivos",      "institution": "SAT", "name": "Lista 69-B — Definitivos (factureras confirmadas)", "year": 2026, "topics": ["riesgo_proveedor", "antifraude"], "geography": "nacional", "granularity": "contribuyente_rfc", "format": "csv", "path": "sat/listas-negras/69-B_Definitivos.csv"},
    {"id": "sat_69b_presuntos",        "institution": "SAT", "name": "Lista 69-B — Presuntos",                            "year": 2026, "topics": ["riesgo_proveedor", "antifraude"], "geography": "nacional", "granularity": "contribuyente_rfc", "format": "csv", "path": "sat/listas-negras/69-B_Presuntos.csv"},
    {"id": "sat_69b_desvirtuados",     "institution": "SAT", "name": "Lista 69-B — Desvirtuados (limpios)",               "year": 2026, "topics": ["riesgo_proveedor", "antifraude"], "geography": "nacional", "granularity": "contribuyente_rfc", "format": "csv", "path": "sat/listas-negras/69-B_Desvirtuados.csv"},
    {"id": "sat_69b_sentencias_fav",   "institution": "SAT", "name": "Lista 69-B — Sentencias favorables",               "year": 2026, "topics": ["riesgo_proveedor", "antifraude"], "geography": "nacional", "granularity": "contribuyente_rfc", "format": "csv", "path": "sat/listas-negras/69-B_Sentencias_Favorables.csv"},
    {"id": "sat_69cff_cancelados",     "institution": "SAT", "name": "69 CFF — Contribuyentes cancelados",               "year": 2026, "topics": ["riesgo_proveedor", "incumplidos"], "geography": "nacional", "granularity": "contribuyente_rfc", "format": "csv", "path": "sat/listas-negras/69CFF_Cancelados.csv"},
    {"id": "sat_69cff_firmes",         "institution": "SAT", "name": "69 CFF — Créditos firmes",                          "year": 2026, "topics": ["riesgo_proveedor", "incumplidos"], "geography": "nacional", "granularity": "contribuyente_rfc", "format": "csv", "path": "sat/listas-negras/69CFF_Firmes.csv"},
    {"id": "sat_69cff_exigibles",      "institution": "SAT", "name": "69 CFF — Créditos exigibles",                       "year": 2026, "topics": ["riesgo_proveedor", "incumplidos"], "geography": "nacional", "granularity": "contribuyente_rfc", "format": "csv", "path": "sat/listas-negras/69CFF_Exigibles.csv"},
    {"id": "sat_69cff_no_localizados", "institution": "SAT", "name": "69 CFF — No localizados",                           "year": 2026, "topics": ["riesgo_proveedor", "incumplidos"], "geography": "nacional", "granularity": "contribuyente_rfc", "format": "csv", "path": "sat/listas-negras/69CFF_No_localizados.csv"},
    {"id": "sat_69cff_sentencias",     "institution": "SAT", "name": "69 CFF — Con sentencias",                           "year": 2026, "topics": ["riesgo_proveedor", "incumplidos"], "geography": "nacional", "granularity": "contribuyente_rfc", "format": "csv", "path": "sat/listas-negras/69CFF_Sentencias.csv"},
    {"id": "sat_69cff_csd_sin_efectos","institution": "SAT", "name": "69 CFF — CSD sin efectos (no pueden facturar)",     "year": 2026, "topics": ["riesgo_proveedor", "incumplidos"], "geography": "nacional", "granularity": "contribuyente_rfc", "format": "csv", "path": "sat/listas-negras/69CFF_CSD_sin_efectos.csv"},

    # ── Diputados — Leyes federales canónicas ────────────────────────
    {"id": "diputados_cff",       "institution": "Cámara de Diputados", "name": "Código Fiscal de la Federación",         "year": 2026, "topics": ["fiscal", "obligaciones_fiscales"], "geography": "nacional", "granularity": "ley", "format": "pdf", "path": "diputados/leyes/CFF.pdf"},
    {"id": "diputados_lfpdppp",   "institution": "Cámara de Diputados", "name": "Ley Federal de Protección de Datos Personales en Posesión de los Particulares (nueva 2025)", "year": 2025, "topics": ["proteccion_datos", "aviso_privacidad"], "geography": "nacional", "granularity": "ley", "format": "pdf", "path": "diputados/leyes/LFPDPPP.pdf"},
    {"id": "diputados_lfpc",      "institution": "Cámara de Diputados", "name": "Ley Federal de Protección al Consumidor (reforma 12-12-2025)", "year": 2025, "topics": ["consumidor", "ecommerce"], "geography": "nacional", "granularity": "ley", "format": "pdf", "path": "diputados/leyes/LFPC.pdf"},
    {"id": "diputados_reg_lfpc",  "institution": "Cámara de Diputados", "name": "Reglamento LFPC",                          "year": 2019, "topics": ["consumidor", "ecommerce"], "geography": "nacional", "granularity": "reglamento", "format": "pdf", "path": "diputados/reglamentos/Reg_LFPC_191219.pdf"},
    {"id": "diputados_lss",       "institution": "Cámara de Diputados", "name": "Ley del Seguro Social (reforma 15-01-2026)", "year": 2026, "topics": ["imss", "laboral"], "geography": "nacional", "granularity": "ley", "format": "pdf", "path": "diputados/leyes/LSS.pdf"},
    {"id": "diputados_lifnvt",    "institution": "Cámara de Diputados", "name": "Ley del INFONAVIT (reforma 21-02-2025)",  "year": 2025, "topics": ["infonavit", "laboral"], "geography": "nacional", "granularity": "ley", "format": "pdf", "path": "diputados/leyes/LIFNVT.pdf"},
    {"id": "diputados_lft",       "institution": "Cámara de Diputados", "name": "Ley Federal del Trabajo",                  "year": 2026, "topics": ["laboral"], "geography": "nacional", "granularity": "ley", "format": "pdf", "path": "diputados/leyes/LFT.pdf"},
    {"id": "diputados_lfppi",     "institution": "Cámara de Diputados", "name": "Ley Federal de Protección a la Propiedad Industrial", "year": 2026, "topics": ["propiedad_industrial", "marcas"], "geography": "nacional", "granularity": "ley", "format": "pdf", "path": "diputados/leyes/LFPPI.pdf"},
    {"id": "diputados_lfpiorpi",  "institution": "Cámara de Diputados", "name": "Ley Federal Prevención e Identificación de Operaciones Recursos Procedencia Ilícita (Antilavado, reforma 16-07-2025)", "year": 2025, "topics": ["antilavado", "actividades_vulnerables"], "geography": "nacional", "granularity": "ley", "format": "pdf", "path": "diputados/leyes/LFPIORPI.pdf"},

    # ── STPS / NOM-035 ────────────────────────────────────────────────
    {"id": "stps_nom_035", "institution": "STPS", "name": "NOM-035-STPS-2018 — Factores de riesgo psicosocial (con Guías II-V)", "year": 2018, "topics": ["nom_stps", "riesgo_psicosocial"], "geography": "nacional", "granularity": "norma", "format": "pdf", "path": "stps/nom-035/NOM-035-STPS-2018.pdf"},

    # ── INAI / Datos Personales ───────────────────────────────────────
    {"id": "inai_manual_aviso_privacidad", "institution": "INAI", "name": "Manual Aviso de Privacidad — modelos integral/simplificado/corto", "year": 2023, "topics": ["proteccion_datos", "aviso_privacidad"], "geography": "nacional", "granularity": "guia", "format": "pdf", "path": "inai/ManualAvisoPrivacidad.pdf"},

    # ── RENAPO / CURP ─────────────────────────────────────────────────
    {"id": "renapo_reglas_curp", "institution": "SEGOB/RENAPO", "name": "Reglas para la asignación de la CURP (algoritmo oficial)", "year": 2021, "topics": ["curp", "validacion"], "geography": "nacional", "granularity": "reglas", "format": "pdf", "path": "renapo/reglas_asignacion_CURP.pdf"},
]

LEGAL_TOPICS_INDEX = {
    "cfdi": ["sat_cfdi40_xsd", "sat_cfdi40_catalogos", "sat_cfdi40_tipos", "sat_rmf_2026_anexo29"],
    "factura_electronica": ["sat_cfdi40_xsd", "sat_cfdi40_catalogos", "sat_cfdi40_tipos"],
    "rfc": ["sat_rmf_2026", "sat_rmf_2026_anexo1", "sat_rmf_2026_anexo29", "diputados_cff"],
    "riesgo_proveedor": ["sat_69b_listado_completo", "sat_69b_definitivos", "sat_69b_presuntos", "sat_69b_desvirtuados", "sat_69cff_cancelados", "sat_69cff_firmes", "sat_69cff_csd_sin_efectos"],
    "antifraude": ["sat_69b_listado_completo", "sat_69b_definitivos"],
    "incumplidos": ["sat_69cff_cancelados", "sat_69cff_firmes", "sat_69cff_exigibles", "sat_69cff_no_localizados", "sat_69cff_sentencias", "sat_69cff_csd_sin_efectos"],
    "sat_tramites": ["sat_rmf_2026", "sat_rmf_2026_anexo1", "sat_rmf_2026_anexo2"],
    "obligaciones_fiscales": ["sat_rmf_2026", "diputados_cff"],
    "fiscal": ["diputados_cff"],
    "proteccion_datos": ["diputados_lfpdppp", "inai_manual_aviso_privacidad"],
    "aviso_privacidad": ["diputados_lfpdppp", "inai_manual_aviso_privacidad"],
    "consumidor": ["diputados_lfpc", "diputados_reg_lfpc"],
    "ecommerce": ["diputados_lfpc", "diputados_reg_lfpc"],
    "imss": ["diputados_lss"],
    "infonavit": ["diputados_lifnvt"],
    "laboral": ["diputados_lft", "diputados_lss", "diputados_lifnvt"],
    "nom_stps": ["stps_nom_035"],
    "riesgo_psicosocial": ["stps_nom_035"],
    "propiedad_industrial": ["diputados_lfppi"],
    "marcas": ["diputados_lfppi"],
    "antilavado": ["diputados_lfpiorpi"],
    "actividades_vulnerables": ["diputados_lfpiorpi"],
    "curp": ["renapo_reglas_curp"],
    "validacion": ["renapo_reglas_curp"],
}


def add_filesize(src):
    """Add size_bytes to each source if file exists."""
    path = BASE / src["path"]
    if path.exists():
        src["size_bytes"] = path.stat().st_size
    return src


def main():
    with open(CATALOG) as f:
        cat = json.load(f)

    # remover entradas legales previas
    cat["sources"] = [s for s in cat["sources"] if not s["id"].startswith(("sat_", "diputados_", "stps_nom", "inai_manual", "renapo_"))]

    # añadir nuevas
    new_sources = [add_filesize(dict(s)) for s in LEGAL_SOURCES]
    cat["sources"].extend(new_sources)

    # actualizar topics_index
    if "topics_index" not in cat:
        cat["topics_index"] = {}
    for topic, ids in LEGAL_TOPICS_INDEX.items():
        cat["topics_index"][topic] = ids

    # stats
    cat.setdefault("stats", {})["total_sources"] = len(cat["sources"])
    cat["stats"]["legal_sources"] = len(new_sources)
    cat["last_updated"] = "2026-05-29"

    with open(CATALOG, "w") as f:
        json.dump(cat, f, ensure_ascii=False, indent=2)

    print(f"✓ catalog.json actualizado")
    print(f"  total sources: {len(cat['sources'])}")
    print(f"  legal sources agregados: {len(new_sources)}")
    print(f"  topics legales agregados: {len(LEGAL_TOPICS_INDEX)}")


if __name__ == "__main__":
    main()
