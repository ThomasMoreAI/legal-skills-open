#!/usr/bin/env bash
# legal-pyme-mx · download_corpus.sh
#
# Baja el corpus oficial de cumplimiento legal federal MX para PyMEs.
# Destino: $RESEARCH_BASE/{institucion}/...
#
# Idempotente: si el archivo ya existe y tiene tamaño >0, lo skipea.
# Para forzar redescarga: rm -f research/<archivo> antes de correr.
#
# Uso:
#   ./download_corpus.sh           # bajar todo
#   ./download_corpus.sh --only=69b   # bajar solo lista 69-B (refresco diario)
#   ./download_corpus.sh --report     # solo reporta qué se va a bajar

set -uo pipefail

RESEARCH_BASE="${RESEARCH_BASE:-/Volumes/Storage/sistemia-skills-mx/research}"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# fuentes: array de "categoria|path_relativo|url"
SOURCES=(
  # ── SAT — CFDI 4.0 y catálogos ────────────────────────────────────────
  "sat-cfdi|sat/cfdi-4/cfdv40.xsd|https://www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd"
  "sat-cfdi|sat/cfdi-4/catCFDI.xsd|https://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd"
  "sat-cfdi|sat/cfdi-4/tdCFDI.xsd|https://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/tdCFDI.xsd"
  "sat-cfdi|sat/cfdi-4/Anexo20_2022.pdf|https://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/Anexo20_2022.pdf"
  "sat-cfdi|sat/cfdi-4/Anexo_20_Guia_de_llenado_CFDI.pdf|https://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/Anexo_20_Guia_de_llenado_CFDI.pdf"

  # ── SAT — RMF 2026 + Anexos ───────────────────────────────────────────
  "sat-rmf|sat/rmf-2026/RMF_2026.pdf|https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf"
  "sat-rmf|sat/rmf-2026/Anexo-1-RMF-2026.pdf|https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/Anexo-1-RMF-2026_DOF-28122025.pdf"
  "sat-rmf|sat/rmf-2026/Anexo-2-RMF-2026.pdf|https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/Anexo-2-RMF-2026_DOF-28122025.pdf"
  "sat-rmf|sat/rmf-2026/Anexo-29-RMF-2026.pdf|https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/Anexo_29_RMF2026-09012026.pdf"

  # ── SAT — Listas 69-B y 69 CFF (URLs Azure Blob reales, refresco frecuente) ─
  "sat-69b|sat/listas-negras/69-B_Listado_Completo.csv|https://wu1agsprosta001.blob.core.windows.net/agsc-publicaciones/Datos_abiertos/Documents_AGAFF/Listado_completo_69-B.csv"
  "sat-69b|sat/listas-negras/69-B_Definitivos.csv|https://wu1agsprosta001.blob.core.windows.net/agsc-publicaciones/Datos_abiertos/Documents_AGAFF/Definitivos.csv"
  "sat-69b|sat/listas-negras/69-B_Desvirtuados.csv|https://wu1agsprosta001.blob.core.windows.net/agsc-publicaciones/Datos_abiertos/Documents_AGAFF/Desvirtuados.csv"
  "sat-69b|sat/listas-negras/69-B_Presuntos.csv|https://wu1agsprosta001.blob.core.windows.net/agsc-publicaciones/Datos_abiertos/Documents_AGAFF/Presuntos.csv"
  "sat-69b|sat/listas-negras/69-B_Sentencias_Favorables.csv|https://wu1agsprosta001.blob.core.windows.net/agsc-publicaciones/Datos_abiertos/Documents_AGAFF/SentenciasFavorables.csv"
  "sat-69cff|sat/listas-negras/69CFF_Cancelados.csv|https://wu1agsprosta001.blob.core.windows.net/agsc-publicaciones/Datos_abiertos/Documents_AGR/Cancelados.csv"
  "sat-69cff|sat/listas-negras/69CFF_Firmes.csv|https://wu1agsprosta001.blob.core.windows.net/agsc-publicaciones/Datos_abiertos/Documents_AGR/Firmes.csv"
  "sat-69cff|sat/listas-negras/69CFF_Exigibles.csv|https://wu1agsprosta001.blob.core.windows.net/agsc-publicaciones/Datos_abiertos/Documents_AGR/Exigibles.csv"
  "sat-69cff|sat/listas-negras/69CFF_No_localizados.csv|https://wu1agsprosta001.blob.core.windows.net/agsc-publicaciones/Datos_abiertos/Documents_AGR/No_localizados.csv"
  "sat-69cff|sat/listas-negras/69CFF_Sentencias.csv|https://wu1agsprosta001.blob.core.windows.net/agsc-publicaciones/Datos_abiertos/Documents_AGR/Sentencias.csv"
  "sat-69cff|sat/listas-negras/69CFF_CSD_sin_efectos.csv|https://wu1agsprosta001.blob.core.windows.net/agsc-publicaciones/Datos_abiertos/Documents_AGR/CSDsinefectos.csv"

  # ── Diputados — Leyes federales canónicas ────────────────────────────
  "diputados|diputados/leyes/CFF.pdf|https://www.diputados.gob.mx/LeyesBiblio/pdf/CFF.pdf"
  "diputados|diputados/leyes/LFPDPPP.pdf|https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf"
  "diputados|diputados/leyes/LFPC.pdf|https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPC.pdf"
  "diputados|diputados/leyes/LSS.pdf|https://www.diputados.gob.mx/LeyesBiblio/pdf/LSS.pdf"
  "diputados|diputados/leyes/LIFNVT.pdf|https://www.diputados.gob.mx/LeyesBiblio/pdf/LIFNVT.pdf"
  "diputados|diputados/leyes/LFT.pdf|https://www.diputados.gob.mx/LeyesBiblio/pdf/LFT.pdf"
  "diputados|diputados/leyes/LFPPI.pdf|https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPPI.pdf"
  "diputados|diputados/leyes/LFPIORPI.pdf|https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPIORPI.pdf"
  "diputados|diputados/reglamentos/Reg_LFPC_191219.pdf|https://www.diputados.gob.mx/LeyesBiblio/regley/Reg_LFPC_191219.pdf"

  # ── STPS — NOM-035 y REPSE ───────────────────────────────────────────
  "stps|stps/nom-035/NOM-035-STPS-2018.pdf|https://asinom.stps.gob.mx/upload/nom/48.pdf"
  "stps|stps/repse/GUIA_REPSE.pdf|https://repse.stps.gob.mx/assets/GUIA_REPSE.pdf"

  # ── INAI — Guía Aviso de Privacidad ──────────────────────────────────
  "inai|inai/ManualAvisoPrivacidad.pdf|https://inicio.inai.org.mx/CalendarioCapacitacion/ManualAvisoPrivacidad.pdf"

  # ── RENAPO — Reglas CURP ────────────────────────────────────────────
  "renapo|renapo/reglas_asignacion_CURP.pdf|https://www.gob.mx/cms/uploads/attachment/file/681698/reglas_para_la_ejecucion_de_los_procedimientos_asignacion_de_la_curp.pdf"

  # ── Datasets datos.gob.mx ────────────────────────────────────────────
  "datos-gob|datos-gob-mx-legal/datos_gob_index.md|MANUAL"
)

REPORT_ONLY=0
ONLY_FILTER=""

for arg in "$@"; do
  case "$arg" in
    --report) REPORT_ONLY=1 ;;
    --only=*) ONLY_FILTER="${arg#--only=}" ;;
    -h|--help)
      grep "^#" "$0" | head -25
      exit 0
      ;;
  esac
done

echo "→ legal-pyme-mx · download_corpus"
echo "  destino: $RESEARCH_BASE"
echo "  fecha:   $(date -Iseconds)"
echo ""

OK=0
SKIP=0
FAIL=0
FAILED_URLS=()

for entry in "${SOURCES[@]}"; do
  IFS='|' read -r categoria rel_path url <<< "$entry"

  if [ -n "$ONLY_FILTER" ] && [[ "$categoria" != *"$ONLY_FILTER"* ]]; then
    continue
  fi

  dest="$RESEARCH_BASE/$rel_path"
  mkdir -p "$(dirname "$dest")"

  if [ "$url" = "MANUAL" ]; then
    # placeholder, se llena después
    continue
  fi

  if [ -s "$dest" ] && [ "$REPORT_ONLY" -eq 0 ]; then
    printf "  ⊘ %-50s (ya existe)\n" "$rel_path"
    SKIP=$((SKIP+1))
    continue
  fi

  if [ "$REPORT_ONLY" -eq 1 ]; then
    printf "  ◇ %-50s ← %s\n" "$rel_path" "$url"
    continue
  fi

  printf "  ↓ %-50s " "$rel_path"
  if curl -fsSL --max-time 60 -A "$UA" -o "$dest" "$url" 2>/dev/null; then
    size=$(stat -f%z "$dest" 2>/dev/null || stat -c%s "$dest" 2>/dev/null)
    printf "✓ (%s bytes)\n" "$size"
    OK=$((OK+1))
  else
    printf "✗ FAIL\n"
    rm -f "$dest"
    FAIL=$((FAIL+1))
    FAILED_URLS+=("$categoria|$rel_path|$url")
  fi
done

echo ""
echo "Resumen:"
echo "  ok:   $OK"
echo "  skip: $SKIP"
echo "  fail: $FAIL"

if [ "$FAIL" -gt 0 ]; then
  echo ""
  echo "Fallaron:"
  for f in "${FAILED_URLS[@]}"; do
    echo "  · $f"
  done
fi
