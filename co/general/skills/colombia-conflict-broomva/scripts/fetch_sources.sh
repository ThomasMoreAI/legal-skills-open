#!/usr/bin/env bash
# Fetch the CEV source PDFs (385 MB) on demand from sources/MANIFEST.json and
# verify each against its sha256. The raw PDFs are deliberately NOT committed to
# the repo (the gzipped full text under references/fulltext/ is the grounding
# substrate); this script makes the provenance binaries reproducibly available
# when actually needed (deep verification, re-extraction, archival).
#
# Usage:
#   scripts/fetch_sources.sh [DEST_DIR]
#   (default DEST: ~/Downloads/comision-de-la-verdad-informe-final)
set -euo pipefail

HERE="$(cd "$(dirname "$0")/.." && pwd)"
MANIFEST="$HERE/sources/MANIFEST.json"
DEST="${1:-$HOME/Downloads/comision-de-la-verdad-informe-final}"
mkdir -p "$DEST"

[ -f "$MANIFEST" ] || { echo "manifest not found: $MANIFEST" >&2; exit 1; }
command -v curl >/dev/null || { echo "curl required" >&2; exit 1; }

sha_of() {
  if command -v shasum >/dev/null 2>&1; then shasum -a 256 "$1" | awk '{print $1}'
  else sha256sum "$1" | awk '{print $1}'; fi
}

TSV="$(mktemp)"; trap 'rm -f "$TSV"' EXIT
python3 -c '
import json, sys
m = json.load(open(sys.argv[1]))
for d in m["downloads"]:
    print("\t".join([d["url"], d["filename"], d["sha256"] or "",
                     "zip" if d.get("extract") else ""]))
' "$MANIFEST" > "$TSV"

while IFS=$'\t' read -r url fn sha kind; do
  out="$DEST/$fn"
  if [ -f "$out" ]; then
    echo "[skip] $fn (already present)"
  else
    echo "[get ] $fn"
    curl -fL --retry 3 --retry-delay 2 -A "Mozilla/5.0" -o "$out" "$url"
  fi
  if [ -n "$sha" ]; then
    got="$(sha_of "$out")"
    if [ "$got" != "$sha" ]; then
      echo "[FAIL] sha256 mismatch for $fn" >&2
      echo "       expected $sha" >&2
      echo "       got      $got" >&2
      exit 1
    fi
    echo "[ ok ] sha256 verified: $fn"
  fi
  if [ "$kind" = "zip" ] && command -v unzip >/dev/null 2>&1; then
    unzip -o -q "$out" -d "$DEST/05-Colombia-adentro"
    echo "[unzip] $fn -> 05-Colombia-adentro/ (14 territorial books)"
  fi
done < "$TSV"

echo "Done. Source corpus at: $DEST"
