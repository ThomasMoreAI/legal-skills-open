#!/usr/bin/env bash
# Builds ai-policy-generator.skill from this directory.
# Outputs the .skill bundle to the parent directory.

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
NAME="ai-policy-generator"
OUT="${HERE}/../${NAME}.skill"

cd "$HERE/.."

rm -f "${NAME}.skill"

zip -r "${NAME}.skill" "${NAME}" \
  -x "${NAME}/REPO_README.md" \
  -x "${NAME}/.git/*" \
  -x "${NAME}/.github/*" \
  -x "${NAME}/build.sh" \
  -x "*.DS_Store"

echo ""
echo "Built ${OUT}"
echo "Drag the .skill file into Cowork or Claude Code to install."
