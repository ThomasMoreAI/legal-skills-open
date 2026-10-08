#!/usr/bin/env bash
# Reaplica o modelo do relatório em HTML ao exemplo público, mantendo os dados do exemplo.
# Rodar sempre que reports/html-report-template.html mudar.
# Uso: scripts/update-example-report.sh [relatorio.html]

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
TEMPLATE="${REPO_ROOT}/.agents/lgpd-enterprise-auditor/reports/html-report-template.html"
REPORT="${1:-${REPO_ROOT}/examples/saas-demo/relatorio-auditoria-lgpd.html}"
PLACEHOLDER='{"_modelo": true}'

[[ -f "$TEMPLATE" ]] || { echo "Modelo não encontrado: ${TEMPLATE}"; exit 1; }
[[ -f "$REPORT" ]] || { echo "Relatório não encontrado: ${REPORT}"; exit 1; }

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

# Dados: as linhas entre a abertura do bloco "lgpd-dados" e o </script> que o fecha.
awk '
  /<script type="application\/json" id="lgpd-dados">/ { in_data = 1; next }
  in_data && /^<\/script>/ { exit }
  in_data { print }
' "$REPORT" > "${TMP_DIR}/data.json"

[[ -s "${TMP_DIR}/data.json" ]] || { echo "Bloco de dados vazio em ${REPORT}"; exit 1; }
if grep -qxF "$PLACEHOLDER" "${TMP_DIR}/data.json"; then
  echo "O relatório ainda está com o bloco de dados do modelo; nada a reaplicar."
  exit 1
fi

awk -v data="${TMP_DIR}/data.json" -v placeholder="$PLACEHOLDER" '
  $0 == placeholder { while ((getline line < data) > 0) print line; next }
  { print }
' "$TEMPLATE" > "${TMP_DIR}/report.html"

mv "${TMP_DIR}/report.html" "$REPORT"
echo "Modelo reaplicado em ${REPORT}"
