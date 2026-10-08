#!/usr/bin/env bash
# Compilar el anonimizador en macOS (genera .app en dist/)
set -euo pipefail
cd "$(dirname "$0")"

echo "[1/4] Instalando dependencias..."
python3 -m pip install -r requirements.txt

echo
echo "[2/4] Descargando modelo de lenguaje español (spaCy)..."
python3 -m spacy download es_core_news_sm

echo
echo "[3/4] Compilando aplicación (puede tardar varios minutos)..."
python3 -m PyInstaller anonimizador.spec --noconfirm

echo
echo "[4/4] Copiando archivos de configuración..."
cp -f reemplazos.json dist/reemplazos.json
cp -f lista_blanca.json dist/lista_blanca.json
cp -f dist/LEEME.txt dist/LEEME.txt 2>/dev/null || cp -f LEEME_MAC.txt dist/LEEME.txt 2>/dev/null || true

echo
echo "Listo. Reparte la carpeta dist/ completa:"
if [[ -d dist/Anonimizador-Trifuerza.app ]]; then
  echo "  - Anonimizador-Trifuerza.app"
else
  echo "  - Anonimizador-Trifuerza"
fi
echo "  - reemplazos.json"
echo "  - lista_blanca.json"
echo "  - LEEME.txt"
echo
echo "Nota: en Mac, si macOS bloquea la app, clic derecho → Abrir (primera vez)."
