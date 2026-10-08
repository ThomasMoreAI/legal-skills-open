#!/usr/bin/env bash
# Smoke test para alta-autonomo
# Verifica que las páginas informativas referenciadas en la skill
# responden correctamente.

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

echo "=== alta-autonomo smoke test ==="
echo ""

check_url "Import@ss (alta en Seguridad Social)" \
  "https://importass.seg-social.es"

check_url "Alta censal AEAT (Modelo 036/037)" \
  "https://sede.agenciatributaria.gob.es/Sede/procedimientoini/G322.shtml"

check_url "Portal Cl@ve" \
  "https://clave.gob.es"

check_url "Certificado digital FNMT" \
  "https://www.sede.fnmt.gob.es/certificados/persona-fisica"

echo ""
echo "Resultado: $PASS OK, $FAIL fallos"

if [[ $FAIL -gt 0 ]]; then
  exit 1
fi
