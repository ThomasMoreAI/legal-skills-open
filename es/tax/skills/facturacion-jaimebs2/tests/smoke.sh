#!/bin/bash
set -e

# Smoke test para fiscalidad-facturacion.
# Verifica que las páginas oficiales referenciadas responden correctamente
# (HTTP 200).

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

check_url "Reglamento de Facturación (RD 1619/2012)" \
  "https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696"

check_url "Sistemas Informáticos de Facturación y VeriFactu (AEAT)" \
  "https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu.html"

check_url "Ley Crea y Crece (Ley 18/2022)" \
  "https://www.boe.es/buscar/act.php?id=BOE-A-2022-15818"

check_url "FACe (factura electrónica AAPP)" \
  "https://face.gob.es"

check_url "Portal IVA AEAT" \
  "https://sede.agenciatributaria.gob.es/Sede/iva.html"

echo ""
echo "fiscalidad-facturacion smoke: $PASS ok, $FAIL fallos"
[ "$FAIL" -eq 0 ] || exit 1
