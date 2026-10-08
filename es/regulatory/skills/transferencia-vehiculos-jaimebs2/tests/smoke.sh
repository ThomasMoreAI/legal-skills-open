#!/usr/bin/env bash
# Smoke test para transferencia-vehiculos
# Verifica que las páginas informativas de la DGT referenciadas en la
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
    echo "  ✓ $label ($http_code)"
    PASS=$((PASS + 1))
  else
    echo "  ✗ $label → HTTP $http_code ($url)"
    FAIL=$((FAIL + 1))
  fi
}

echo "=== transferencia-vehiculos smoke test ==="
echo ""

check_url "Sede DGT — Cambio de titularidad" \
  "https://sede.dgt.gob.es/es/vehiculos/cambio-de-titularidad/"

check_url "Sede DGT — Informe de vehículo" \
  "https://sede.dgt.gob.es/es/vehiculos/informe-vehiculo/"

check_url "Sede DGT — Notificación de venta" \
  "https://sede.dgt.gob.es/es/vehiculos/notificacion-de-venta/"

echo ""
echo "Resultado: $PASS OK, $FAIL fallos"

if [[ $FAIL -gt 0 ]]; then
  exit 1
fi
