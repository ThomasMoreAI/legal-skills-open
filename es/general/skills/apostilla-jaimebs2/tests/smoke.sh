#!/usr/bin/env bash
# Smoke test para apostilla
# Verifica que las páginas del Ministerio de Justicia y MAEC
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

echo "=== apostilla smoke test ==="
echo ""

check_url "Sede Ministerio de Justicia" \
  "https://sede.mjusticia.gob.es"

check_url "Sede MAEC" \
  "https://sede.exteriores.gob.es"

check_url "Lista de traductores-intérpretes jurados (MAEC)" \
  "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Traductores-Interpretes-Jurados.aspx"

echo ""
echo "Resultado: $PASS OK, $FAIL fallos"

if [[ $FAIL -gt 0 ]]; then
  exit 1
fi
