#!/usr/bin/env bash
# Garante que o modelo do relatório em HTML continua preenchível e offline, e que o exemplo
# público usa o modelo atual com dados válidos e coerentes com o catálogo e com o cálculo do score.
# Uso: scripts/tests/test-html-report.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd -P)"
FRAMEWORK="${REPO_ROOT}/.agents/lgpd-enterprise-auditor"
TEMPLATE="${FRAMEWORK}/reports/html-report-template.html"
EXAMPLE="${REPO_ROOT}/examples/saas-demo/relatorio-auditoria-lgpd.html"
PLACEHOLDER='{"_modelo": true}'
DATA_OPEN='<script type="application/json" id="lgpd-dados">'
LEGAL_NOTICE='Este relatório foi gerado com apoio de IA pelo LGPD Enterprise Auditor, a partir das evidências disponíveis no momento da análise. Ele apoia, mas não substitui, a avaliação do encarregado (DPO) e a assessoria jurídica especializada. As conclusões dependem da completude e da atualidade das evidências fornecidas.'
FAILURES=0

ok() { printf "  ok   %s\n" "$1"; }
fail() {
  printf "  FAIL %s\n" "$1"
  FAILURES=$((FAILURES + 1))
}
check() {
  local name="$1"
  shift
  if "$@"; then ok "$name"; else fail "$name"; fi
}

count_lines() { grep -cxF "$1" "$2" || true; }
count_matches() { grep -cF "$1" "$2" || true; }

# O bloco de dados volta a ser o do modelo, para comparar o resto do arquivo.
without_data() {
  awk -v open_tag="$DATA_OPEN" -v placeholder="$PLACEHOLDER" '
    $0 == open_tag { print; print placeholder; in_data = 1; next }
    in_data && /^<\/script>/ { in_data = 0 }
    !in_data { print }
  ' "$1"
}
data_block() {
  awk -v open_tag="$DATA_OPEN" '
    $0 == open_tag { in_data = 1; next }
    in_data && /^<\/script>/ { exit }
    in_data { print }
  ' "$1"
}

echo "Modelo: reports/html-report-template.html"
[[ -f "$TEMPLATE" ]] || { echo "  FAIL modelo não encontrado"; exit 1; }

check "linha do bloco de dados aparece uma única vez" test "$(count_lines "$PLACEHOLDER" "$TEMPLATE")" = "1"
check "abertura do bloco lgpd-dados aparece uma única vez" test "$(count_lines "$DATA_OPEN" "$TEMPLATE")" = "1"
check "marcação de confidencialidade presente" grep -qF "CONFIDENCIAL — uso interno" "$TEMPLATE"
check "aviso legal igual ao de core/reporting-engine.md no modelo" grep -qF "$LEGAL_NOTICE" "$TEMPLATE"
check "aviso legal presente em core/reporting-engine.md" grep -qF "$LEGAL_NOTICE" "${FRAMEWORK}/core/reporting-engine.md"
check "especificação reports/html-report.md cita a linha do bloco de dados" grep -qF "$PLACEHOLDER" "${FRAMEWORK}/reports/html-report.md"
check "skill cita a linha do bloco de dados" grep -qF "$PLACEHOLDER" "${REPO_ROOT}/SKILL.md"

# Offline: nenhum endereço externo e nenhum recurso carregado de fora do arquivo.
if grep -nE 'https?://|<link[[:space:]]|@import|[[:space:]]src=|url\(' "$TEMPLATE"; then
  fail "modelo sem recursos externos"
else
  ok "modelo sem recursos externos"
fi

echo "Exemplo: examples/saas-demo/relatorio-auditoria-lgpd.html"
if [[ ! -f "$EXAMPLE" ]]; then
  fail "exemplo não encontrado"
else
  if diff <(without_data "$EXAMPLE") "$TEMPLATE" > /dev/null; then
    ok "exemplo usa o modelo atual"
  else
    fail "exemplo desatualizado em relação ao modelo (rode scripts/update-example-report.sh)"
  fi

  if data_block "$EXAMPLE" | grep -q '<'; then
    fail "dados do exemplo sem o caractere '<' (usar \\u003c)"
  else
    ok "dados do exemplo sem o caractere '<' (usar \\u003c)"
  fi

  if command -v python3 > /dev/null 2>&1; then
    VERSION="$(awk '/^[[:space:]]+version:/ { gsub(/[" ]/, ""); sub(/^version:/, ""); print; exit }' "${REPO_ROOT}/SKILL.md")"
    if data_block "$EXAMPLE" | python3 -c '
import json, sys
data = json.load(sys.stdin)
sections = ["resumo_executivo", "score_lgpd", "checklist_conformidade", "nao_conformidades",
            "itens_obrigatorios_ausentes", "riscos_identificados", "plano_adequacao", "recomendacoes_tecnicas"]
missing = [s for s in sections if not data.get(s)]
if missing:
    sys.exit("seções ausentes: " + ", ".join(missing))
if data["meta"].get("framework_version") != sys.argv[1]:
    sys.exit("framework_version do exemplo (%s) difere da versão do projeto (%s)" % (data["meta"].get("framework_version"), sys.argv[1]))
' "$VERSION"; then
      ok "dados do exemplo são JSON válido, com as 8 seções e a versão ${VERSION}"
    else
      fail "dados do exemplo são JSON válido, com as 8 seções e a versão ${VERSION}"
    fi

    # Catálogo, enums, relação entre itens e achados, cálculo e o .md com os mesmos dados.
    if REPORT_CHECK="$(python3 "${REPO_ROOT}/scripts/validate-report.py" "$EXAMPLE" --md "${EXAMPLE%.html}.md" 2>&1)"; then
      ok "exemplo consistente com o framework (scripts/validate-report.py), no .html e no .md"
    else
      fail "exemplo consistente com o framework (scripts/validate-report.py), no .html e no .md"
      printf "%s\n" "$REPORT_CHECK" | sed 's/^/         /'
    fi
  else
    echo "  --   python3 ausente: validação dos dados do exemplo não executada"
  fi
fi

echo
if [[ "$FAILURES" -gt 0 ]]; then
  echo "${FAILURES} falha(s)."
  exit 1
fi
echo "Relatório em HTML consistente."
