#!/usr/bin/env bash
# Smoke test para laboral-desempleo
# Verifica que las páginas informativas del SEPE y Seguridad Social
# referenciadas en la skill responden correctamente.

set -euo pipefail

PASS=0
FAIL=0

check_url() {
  local label="$1"
  local url="$2"
  local http_code
  http_code=$(curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36" -o /dev/null -w '%{http_code}' -L --max-time 15 "$url" || true)
  if [[ "$http_code" =~ ^(200|301|302|303)$ ]]; then
    echo "  ✓ $label ($http_code)"
    PASS=$((PASS + 1))
  else
    echo "  ✗ $label → HTTP $http_code ($url)"
    FAIL=$((FAIL + 1))
  fi
}

echo "=== laboral-desempleo smoke test ==="
echo ""

check_url "Prestaciones SEPE" \
  "https://www.sepe.es/HomeSepe/Personas/distributiva-prestaciones.html"

check_url "Quiero cobrar el paro (SEPE)" \
  "https://www.sepe.es/HomeSepe/Personas/distributiva-prestaciones/quiero-cobrar-el-paro.html"

check_url "Capitalización del desempleo (SEPE)" \
  "https://www.sepe.es/HomeSepe/autonomos/capitaliza-tu-prestacion.html"

check_url "Ingreso Mínimo Vital (Seguridad Social)" \
  "https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/PrestacionesPensionesTrabajadores/72702"

echo ""
echo "Resultado: $PASS OK, $FAIL fallos"

if [[ $FAIL -gt 0 ]]; then
  exit 1
fi
