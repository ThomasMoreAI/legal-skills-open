#!/usr/bin/env bash
# Smoke test para fiscalidad-sociedades
# Verifica que las paginas informativas de la AEAT referenciadas en la
# skill responden correctamente.

set -euo pipefail

PASS=0
FAIL=0

check_url() {
  local label="$1"
  local url="$2"
  local http_code
  http_code=$(curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36" -o /dev/null -w '%{http_code}' -L --max-time 15 "$url" || true)
  if [[ "$http_code" =~ ^(200|301|302|303)$ ]]; then
    echo "  OK $label ($http_code)"
    PASS=$((PASS + 1))
  else
    echo "  FAIL $label -> HTTP $http_code ($url)"
    FAIL=$((FAIL + 1))
  fi
}

echo "=== fiscalidad-sociedades smoke test ==="
echo ""

check_url "Sede AEAT — Impuesto de Sociedades" \
  "https://sede.agenciatributaria.gob.es/Sede/impuesto-sobre-sociedades.html"

check_url "Modelo 200" \
  "https://sede.agenciatributaria.gob.es/Sede/procedimientoini/GE04.shtml"

check_url "Calendario del contribuyente" \
  "https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026.html"

echo ""
echo "Resultado: $PASS OK, $FAIL fallos"

if [[ $FAIL -gt 0 ]]; then
  exit 1
fi
