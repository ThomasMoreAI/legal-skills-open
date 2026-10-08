#!/usr/bin/env bash
# Smoke test para extranjeria-nacionalidad
# Verifica que las páginas informativas referenciadas en la skill responden correctamente.

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

echo "=== extranjeria-nacionalidad smoke test ==="
echo ""

check_url "Ministerio de Justicia — Nacionalidad" \
  "https://www.mjusticia.gob.es/es/ciudadania/nacionalidad"

check_url "Prueba CCSE — Instituto Cervantes" \
  "https://ccse.cervantes.es"

check_url "DELE — Instituto Cervantes" \
  "https://examenes.cervantes.es/es/dele/que-es"

check_url "Instituto Cervantes — Portal" \
  "https://www.cervantes.es"

echo ""
echo "Resultado: $PASS OK, $FAIL fallos"

if [[ $FAIL -gt 0 ]]; then
  exit 1
fi
