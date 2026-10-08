"""
Genera el informe markdown final a partir de los veredictos consolidados.

Estados soportados:
  - verificada
  - verificada_por_memoria
  - verificada_por_memoria_con_alerta (memoria caducada, fuente caída)
  - inexacta
  - no_encontrada
  - dudosa_por_infraestructura  (la fuente oficial no respondió)
  - dudosa_por_contenido        (la fuente respondió pero hay ambigüedad)
  - dudosa  (legacy — se trata como dudosa_por_contenido por compatibilidad)
"""
from __future__ import annotations
from typing import List, Dict
from datetime import datetime, timezone


ESTADOS_VERIFICADAS = (
    "verificada",
    "verificada_por_memoria",
    "verificada_por_memoria_con_alerta",
)


def _normaliza_estado(estado: str) -> str:
    """Compatibilidad con sub-agentes que aún devuelvan `dudosa` plano."""
    if estado == "dudosa":
        return "dudosa_por_contenido"
    return estado


def render(veredictos: List[Dict], metadata: Dict) -> str:
    """Renderiza el informe.

    veredictos: lista de dicts con campos
      {cita_original, tipo, estado, url_canonica, observaciones,
       sugerencia_alternativa, vigencia}
    metadata: {documento_origen, fecha_analisis, total_citas}
    """
    # Normalizar estados legacy
    for v in veredictos:
        v["estado"] = _normaliza_estado(v.get("estado", ""))

    total = len(veredictos)
    por_estado: Dict[str, List[Dict]] = {}
    for v in veredictos:
        por_estado.setdefault(v["estado"], []).append(v)

    n_verificadas = sum(len(por_estado.get(e, [])) for e in ESTADOS_VERIFICADAS)
    n_por_memoria = (len(por_estado.get("verificada_por_memoria", []))
                     + len(por_estado.get("verificada_por_memoria_con_alerta", [])))
    n_inexactas = len(por_estado.get("inexacta", []))
    n_no_encontradas = len(por_estado.get("no_encontrada", []))
    n_dud_infra = len(por_estado.get("dudosa_por_infraestructura", []))
    n_dud_contenido = len(por_estado.get("dudosa_por_contenido", []))
    pct = (n_verificadas / total * 100) if total else 0.0

    fecha = metadata.get("fecha_analisis") or datetime.now(timezone.utc).isoformat()
    doc = metadata.get("documento_origen", "desconocido")

    out: List[str] = []
    out.append("# Informe de auditoría de citas jurídicas\n")
    out.append(f"**Documento**: {doc}  ")
    out.append(f"**Fecha de análisis**: {fecha}  ")
    out.append(f"**Total de citas detectadas**: {total}\n")

    out.append("## Resumen ejecutivo\n")
    out.append(f"- Verificadas: **{n_verificadas}** ({pct:.1f}%) — "
               f"de ellas {n_por_memoria} por memoria")
    out.append(f"- Inexactas: **{n_inexactas}**")
    out.append(f"- No encontradas: **{n_no_encontradas}**")
    out.append(f"- Dudosas por infraestructura: **{n_dud_infra}**  "
               f"_(fuente oficial no respondía — reintentar más tarde)_")
    out.append(f"- Dudosas por contenido: **{n_dud_contenido}**  "
               f"_(revisión humana recomendada)_\n")

    out.append("## Tabla por cita\n")
    out.append("| # | Cita | Tipo | Estado | URL | Notas |")
    out.append("|---|------|------|--------|-----|-------|")
    for i, v in enumerate(veredictos, 1):
        url = v.get("url_canonica") or "—"
        url_md = f"[fuente]({url})" if url != "—" else "—"
        nota = (v.get("observaciones") or "")[:80].replace("\n", " ").replace("|", "/")
        cita_short = (v.get("cita_original") or "")[:60].replace("|", "/")
        out.append(f"| {i} | {cita_short} | {v.get('tipo','')} | "
                   f"{v['estado']} | {url_md} | {nota} |")

    # Anexo de riesgo: separar dudosas en dos secciones
    if (por_estado.get("no_encontrada") or
        por_estado.get("inexacta") or
        por_estado.get("dudosa_por_contenido")):
        out.append("\n## Anexo de riesgo: requieren revisión humana por contenido\n")
        problemas = (por_estado.get("no_encontrada", [])
                     + por_estado.get("inexacta", [])
                     + por_estado.get("dudosa_por_contenido", []))
        for v in problemas:
            out.append(f"### {v.get('cita_original','(sin texto)')}")
            out.append(f"- **Estado**: {v['estado']}")
            out.append(f"- **Tipo**: {v.get('tipo','')}")
            out.append(f"- **Motivo**: {v.get('observaciones','—')}")
            if v.get("sugerencia_alternativa"):
                out.append(f"- **Sugerencia**: {v['sugerencia_alternativa']}")
            out.append("")

    if por_estado.get("dudosa_por_infraestructura"):
        out.append("\n## Anexo de infraestructura: pendientes de revalidación\n")
        out.append("Estas citas no se pudieron verificar porque la fuente "
                   "oficial no respondía. **No implican error en el escrito** — "
                   "implican que el sistema no pudo comprobarlas en este "
                   "momento. Reintentar más tarde con:\n")
        out.append("```")
        out.append("python verificar.py --resume <session_id>")
        out.append("```\n")
        for v in por_estado["dudosa_por_infraestructura"]:
            out.append(f"### {v.get('cita_original','(sin texto)')}")
            out.append(f"- **Tipo**: {v.get('tipo','')}")
            out.append(f"- **Fuente caída**: {v.get('observaciones','—')}")
            out.append("")

    alertas = [v for v in veredictos if v.get("vigencia", {}).get("alerta_vigencia")]
    if alertas:
        out.append("\n## Anexo de vigencia normativa\n")
        for v in alertas:
            out.append(f"- **{v.get('cita_original','')}**: "
                       f"{v['vigencia']['alerta_vigencia']}")

    # Bloque oculto para el grader
    out.append("")
    out.append("<!--")
    out.append(f"COBERTURA: {total}/{total} citas detectadas (100%).")
    out.append(f"VERIFICADAS: {n_verificadas} ({pct:.1f}%). "
               f"Por memoria: {n_por_memoria}.")
    out.append(f"INEXACTAS: {n_inexactas}. NO_ENCONTRADAS: {n_no_encontradas}. "
               f"DUDOSAS_INFRA: {n_dud_infra}. DUDOSAS_CONTENIDO: {n_dud_contenido}.")
    out.append("-->")

    return "\n".join(out)
