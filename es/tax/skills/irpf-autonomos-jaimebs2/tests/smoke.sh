#!/bin/bash
set -e

# Smoke test para fiscalidad-irpf-autonomos.
# Verifica que las páginas oficiales de la AEAT referenciadas en la skill
# responden correctamente (HTTP 200).

PASS=0
FAIL=0

check_url() {
  local label="$1"
  local url="$2"
  echo ">>> Comprobando: $label"
  HTTP_CODE=$(curl -sf -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36" -o /dev/null -w "%{http_code}" -L "$url" 2>/dev/null || true)
  if [ "$HTTP_CODE" -eq 200 ]; then
    echo "    ok  HTTP $HTTP_CODE"
    PASS=$((PASS + 1))
  else
    echo "    x   HTTP $HTTP_CODE — $url"
    FAIL=$((FAIL + 1))
  fi
}

check_url "Modelo 130 — ficha" \
  "https://sede.agenciatributaria.gob.es/Sede/procedimientoini/G601.shtml"

check_url "Pagos fraccionados — plazos" \
  "https://sede.agenciatributaria.gob.es/Sede/irpf/retenciones-ingresos-cuenta-pagos-fraccionados/pagos-fraccionados/plazos-declaracion-ingreso.html"

check_url "Folleto actividades económicas" \
  "https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas.html"

check_url "Instrucciones Modelo 130" \
  "https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html"

echo ""
echo "fiscalidad-irpf-autonomos smoke: $PASS ok, $FAIL fallos"
[ "$FAIL" -eq 0 ] || exit 1
