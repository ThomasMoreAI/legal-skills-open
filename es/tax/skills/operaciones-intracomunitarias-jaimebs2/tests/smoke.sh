#!/bin/bash
set -e

# Smoke test para fiscalidad-operaciones-intracomunitarias.
# Verifica que las páginas oficiales de AEAT y VIES referenciadas
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

check_url "Portal IVA AEAT" \
  "https://sede.agenciatributaria.gob.es/Sede/iva.html"

check_url "Modelo 349 — ficha procedimiento" \
  "https://sede.agenciatributaria.gob.es/Sede/procedimientoini/G417.shtml"

check_url "Modelo 303 — ficha procedimiento" \
  "https://sede.agenciatributaria.gob.es/Sede/procedimientoini/G414.shtml"

check_url "Modelo 036/037 — ficha procedimiento" \
  "https://sede.agenciatributaria.gob.es/Sede/procedimientoini/G322.shtml"

check_url "VIES (verificación NIF-IVA)" \
  "https://ec.europa.eu/taxation_customs/vies/"

echo ""
echo "fiscalidad-operaciones-intracomunitarias smoke: $PASS ok, $FAIL fallos"
[ "$FAIL" -eq 0 ] || exit 1
