#!/usr/bin/env bash
# Roda localmente tudo o que o CI roda, para liberar commit, push e release sem esperar o GitHub.
# O CI continua valendo como segunda conferência (Ubuntu e Windows), não como porteiro.
# Uso: scripts/tests/run-all.sh [tag]
#   tag  opcional (ex.: v1.6.1): confere também se a versão do projeto bate com a tag.

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd -P)"
TAG="${1:-}"
FAILURES=0
SKIPPED=""

run() {
  local name="$1"
  shift
  local log
  log="$(mktemp)"
  if "$@" > "$log" 2>&1; then
    printf "  ok   %s\n" "$name"
  else
    printf "  FAIL %s\n" "$name"
    sed 's/^/         /' "$log" | tail -n 25
    FAILURES=$((FAILURES + 1))
  fi
  rm -f "$log"
}

skip() {
  printf "  --   %s\n" "$1"
  SKIPPED="${SKIPPED}${2}; "
}

# Mesma checagem do workflow attribution.yml, sobre os commits ainda não enviados.
attribution_clean() {
  local range="origin/main..HEAD"
  git -C "$REPO_ROOT" rev-parse --verify --quiet origin/main > /dev/null || range="-1 HEAD"
  # shellcheck disable=SC2086
  ! git -C "$REPO_ROOT" log $range --format='%h %an <%ae> | %cn <%ce>%n%B' \
    | grep -inE '^co-authored-by:|noreply@anthropic\.com|generated with claude|🤖'
}

cd "$REPO_ROOT" || exit 1
echo "Verificações locais (as mesmas do CI)"

run "framework: catálogo, paridade, cenários, manifestos" bash scripts/tests/test-framework.sh
run "relatório em HTML e exemplo" bash scripts/tests/test-html-report.sh
if [[ -n "$TAG" ]]; then
  run "versões (tag ${TAG})" bash scripts/tests/test-versions.sh "$TAG"
else
  run "versões" bash scripts/tests/test-versions.sh
fi
run "instalador (bash)" bash scripts/tests/test-install.sh
# O "curl | bash" de quem usa Mac roda no bash 3.2 do sistema.
if [[ -x /bin/bash && "$(/bin/bash -c 'echo "${BASH_VERSINFO[0]}"')" == "3" ]]; then
  run "instalador e framework no bash 3.2 (/bin/bash)" env BASH_BIN=/bin/bash /bin/bash -c \
    'scripts/tests/test-install.sh && scripts/tests/test-framework.sh'
fi

if command -v shellcheck > /dev/null 2>&1; then
  run "ShellCheck" shellcheck scripts/install.sh scripts/update-example-report.sh scripts/update-skill-catalog.sh scripts/tests/*.sh
else
  skip "ShellCheck não instalado (brew install shellcheck)" "ShellCheck"
fi

if command -v pwsh > /dev/null 2>&1; then
  run "instalador (PowerShell 7)" pwsh -NoProfile -File scripts/tests/test-install.ps1
else
  skip "PowerShell não instalado: install.ps1 só é testado no CI" "testes do install.ps1"
fi

run "commits sem assinatura de agente de IA" attribution_clean

echo
if [[ "$FAILURES" -gt 0 ]]; then
  echo "${FAILURES} verificação(ões) falharam. Não envie."
  exit 1
fi
if [[ -n "$SKIPPED" ]]; then
  echo "Tudo certo no que rodou. Não conferido aqui: ${SKIPPED%; }."
  if ! git diff --quiet origin/main -- scripts/install.ps1 scripts/tests/test-install.ps1 2> /dev/null; then
    echo "Atenção: há mudança no instalador PowerShell ainda não enviada; para ela, o CI do Windows é o único teste."
  fi
else
  echo "Tudo certo."
fi
