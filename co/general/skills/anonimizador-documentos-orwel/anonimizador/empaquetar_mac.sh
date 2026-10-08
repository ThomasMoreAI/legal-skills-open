#!/usr/bin/env bash
# Empaqueta .app firmada + ZIP + DMG listos para repartir en macOS
set -euo pipefail
cd "$(dirname "$0")"

APP="dist/Anonimizador-Trifuerza.app"
ZIP="dist/Anonimizador-Trifuerza-mac.zip"
DMG="dist/Anonimizador-Trifuerza-macOS.dmg"
STAGE="dist/mac-paquete"

echo "=== Compilando ==="
./construir.sh

if [[ ! -d "$APP" ]]; then
  echo "Error: no se generó $APP"
  exit 1
fi

echo
echo "=== Firmando (ad-hoc, sin cuenta Apple) ==="
xattr -cr "$APP" || true
codesign --force --deep --sign - "$APP"
codesign --verify --verbose "$APP"

echo
echo "=== Creando ZIP ==="
rm -f "$ZIP"
ditto -c -k --sequesterRsrc --keepParent "$APP" "$ZIP"

echo
echo "=== Creando DMG (arrastrar a Aplicaciones) ==="
rm -rf "$STAGE"
mkdir -p "$STAGE"
cp -R "$APP" "$STAGE/"
cp -f LEEME_MAC.txt "$STAGE/LEEME.txt"
ln -sf /Applications "$STAGE/Aplicaciones"
rm -f "$DMG"
hdiutil create -volname "Anonimizador Trifuerza" -srcfolder "$STAGE" -ov -format UDZO "$DMG"
rm -rf "$STAGE"

echo
echo "Listo para repartir:"
echo "  $ZIP   (descarga directa)"
echo "  $DMG   (abrir → arrastrar .app a Aplicaciones → doble clic)"
echo
echo "Primera apertura: doble clic en la app desde Aplicaciones."
echo "Si macOS bloquea: Ajustes → Privacidad y seguridad → Abrir igualmente."
