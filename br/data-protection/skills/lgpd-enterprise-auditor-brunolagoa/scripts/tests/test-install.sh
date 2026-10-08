#!/usr/bin/env bash
# Testes de regressão do scripts/install.sh. Rodam offline, a partir do clone (--version local),
# em projetos temporários. Uso: scripts/tests/test-install.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd -P)"
INSTALLER="${REPO_ROOT}/scripts/install.sh"
BASH_BIN="${BASH_BIN:-bash}"
WORK_DIR="$(mktemp -d)"
trap 'rm -rf "$WORK_DIR"' EXIT

export LGPD_AUDITOR_OFFLINE=1
export LGPD_AUDITOR_NO_TTY=1

COMMAND_COUNT="$(find "${REPO_ROOT}/commands" -maxdepth 1 -name '*.md' | wc -l | tr -d ' ')"
FAILURES=0
CURRENT=""

pass() { printf "  ok   %s\n" "$1"; }
fail() { printf "  FAIL %s\n" "$1"; FAILURES=$((FAILURES + 1)); }

check() {
  local description="$1"
  shift
  if "$@"; then pass "$description"; else fail "$description"; fi
}

new_project() {
  CURRENT="${WORK_DIR}/$1"
  mkdir -p "${CURRENT}/.git"
  echo "keep" > "${CURRENT}/app.txt"
}

run_installer() {
  "$BASH_BIN" "$INSTALLER" "$@" --project-dir "$CURRENT" > "${WORK_DIR}/last.log" 2>&1
}

install_quiet() {
  run_installer install --non-interactive --version local "$@"
}

exit_code_of() {
  local code=0
  "$@" > /dev/null 2>&1 || code=$?
  printf "%s" "$code"
}

count_files() {
  find "${CURRENT}/$1" -maxdepth 1 -name "$2" 2>/dev/null | wc -l | tr -d ' '
}

manifest() { printf "%s/.agents/lgpd-enterprise-auditor/.install/%s.json" "$CURRENT" "$1"; }
exists() { [[ -e "${CURRENT}/$1" ]]; }
missing() { [[ ! -e "${CURRENT}/$1" ]]; }
equals() { [[ "$1" == "$2" ]]; }
contains() { grep -q -- "$2" "${CURRENT}/$1"; }
not_contains() { ! grep -q -- "$2" "${CURRENT}/$1"; }
first_line_matches() { head -n 1 "${CURRENT}/$1" | grep -q -- "$2"; }
project_untouched() { [[ "$(cat "${CURRENT}/app.txt")" == "keep" ]]; }

echo "== install por ferramenta (sem skill)"
for target in claude cursor vscode opencode; do
  new_project "plain-${target}"
  install_quiet --target "$target"
  case "$target" in
    claude) dir=".claude/commands"; pattern="lgpd-*.md" ;;
    cursor) dir=".cursor/commands"; pattern="lgpd-*.md" ;;
    vscode) dir=".github/prompts"; pattern="lgpd-*.prompt.md" ;;
    opencode) dir=".opencode/commands"; pattern="lgpd-*.md" ;;
  esac
  check "${target}: framework instalado" exists ".agents/lgpd-enterprise-auditor/core/auditor-core.md"
  check "${target}: modelo do relatório em HTML instalado" exists ".agents/lgpd-enterprise-auditor/reports/html-report-template.html"
  check "${target}: ${COMMAND_COUNT} comandos em ${dir}" equals "$(count_files "$dir" "$pattern")" "$COMMAND_COUNT"
  check "${target}: manifesto criado" exists ".agents/lgpd-enterprise-auditor/.install/${target}.json"
  check "${target}: sem skill" missing ".agents/skills"
  check "${target}: sem skill do Claude" missing ".claude/skills"
  check "${target}: arquivo do projeto intacto" project_untouched
done

echo "== agents (skill obrigatória)"
new_project "agents"
install_quiet --target agents
check "agents: skill em .agents/skills" exists ".agents/skills/lgpd-enterprise-auditor/SKILL.md"
check "agents: manifesto sem comandos" contains ".agents/lgpd-enterprise-auditor/.install/agents.json" '"files": \[\]'
check "agents: --no-skill é recusado" equals "$(exit_code_of install_quiet --target agents --no-skill)" "1"

echo "== skill por ferramenta"
new_project "skill-claude"
install_quiet --target claude --with-skill
check "claude: skill em .claude/skills" exists ".claude/skills/lgpd-enterprise-auditor/SKILL.md"
check "claude: skill tem frontmatter" first_line_matches ".claude/skills/lgpd-enterprise-auditor/SKILL.md" "^---$"
new_project "skill-cursor"
install_quiet --target cursor --with-skill
check "cursor: skill em .agents/skills" exists ".agents/skills/lgpd-enterprise-auditor/SKILL.md"

echo "== transformações de formato"
new_project "formats"
install_quiet --target cursor
install_quiet --target vscode
check "cursor: description na primeira linha" first_line_matches ".cursor/commands/lgpd-saas.md" "^> Executa auditoria"
check "cursor: frontmatter removido" not_contains ".cursor/commands/lgpd-saas.md" "^license:"
check "vscode: frontmatter na primeira linha" first_line_matches ".github/prompts/lgpd-saas.prompt.md" "^---$"
check "vscode: modo agent" contains ".github/prompts/lgpd-saas.prompt.md" "^agent: agent$"
check "vscode: mantém name" contains ".github/prompts/lgpd-saas.prompt.md" "^name: lgpd-saas$"
check "vscode: remove campos não suportados" not_contains ".github/prompts/lgpd-saas.prompt.md" "^license:"

echo "== reinstalação e update"
new_project "reinstall"
install_quiet --target claude --with-skill
install_quiet --target claude --with-skill
check "reinstalação não duplica comandos" equals "$(count_files .claude/commands 'lgpd-*.md')" "$COMMAND_COUNT"
install_quiet --target claude --no-skill
check "reinstalar sem skill remove a skill" missing ".claude/skills"
sed 's/"version": "[^"]*"/"version": "0.0.1"/' "$(manifest claude)" > "${WORK_DIR}/m.json" && mv "${WORK_DIR}/m.json" "$(manifest claude)"
run_installer update --non-interactive --version local
check "update restaura a versão atual" not_contains ".agents/lgpd-enterprise-auditor/.install/claude.json" '"version": "0.0.1"'
new_project "empty-update"
check "update sem instalação retorna 2" equals "$(exit_code_of run_installer update --non-interactive --version local)" "2"

echo "== várias ferramentas e uninstall"
new_project "multi"
mkdir -p "${CURRENT}/.claude/commands" "${CURRENT}/.github/prompts"
echo "meu" > "${CURRENT}/.claude/commands/meu-comando.md"
echo "meu" > "${CURRENT}/.github/prompts/meu.prompt.md"
install_quiet --target claude
install_quiet --target vscode --with-skill
install_quiet --target agents
run_installer uninstall --non-interactive --target vscode
check "uninstall vscode remove os prompts" equals "$(count_files .github/prompts 'lgpd-*.prompt.md')" "0"
check "uninstall vscode mantém prompt do usuário" exists ".github/prompts/meu.prompt.md"
check "skill compartilhada com agents é mantida" exists ".agents/skills/lgpd-enterprise-auditor/SKILL.md"
check "framework mantido enquanto houver ferramentas" exists ".agents/lgpd-enterprise-auditor/core/auditor-core.md"
run_installer uninstall --non-interactive
check "uninstall total remove o framework" missing ".agents"
check "uninstall total remove comandos do Claude" equals "$(count_files .claude/commands 'lgpd-*.md')" "0"
check "uninstall total mantém comando do usuário" exists ".claude/commands/meu-comando.md"
check "arquivo do projeto intacto" project_untouched

echo "== check"
new_project "check"
check "check sem instalação retorna 2" equals "$(exit_code_of run_installer check)" "2"
install_quiet --target opencode
check "check com instalação íntegra retorna 0" equals "$(exit_code_of run_installer check)" "0"
rm -f "${CURRENT}/.opencode/commands/lgpd-saas.md"
check "check com arquivo ausente retorna 1" equals "$(exit_code_of run_installer check)" "1"

echo "== proteções"
new_project "guards"
check "--non-interactive sem --target retorna 1" equals "$(exit_code_of install_quiet)" "1"
check "argumento desconhecido retorna 1" equals "$(exit_code_of run_installer install --foo)" "1"
check "ferramenta inválida retorna 1" equals "$(exit_code_of install_quiet --target emacs)" "1"
check "instalar no próprio repositório é recusado" \
  equals "$(exit_code_of "$BASH_BIN" "$INSTALLER" install --non-interactive --version local --target claude --project-dir "$REPO_ROOT")" "1"
check "nada foi instalado no repositório" test ! -e "${REPO_ROOT}/.claude/commands/lgpd-saas.md"

echo "== última versão não consultável"
# Fora de um clone e sem conseguir consultar a última versão, o instalador não cai na branch main sozinho.
mkdir -p "${WORK_DIR}/solo"
cp "$INSTALLER" "${WORK_DIR}/solo/install.sh"
new_project "no-tag"
check "modo não interativo sem --version retorna 1" \
  equals "$(exit_code_of "$BASH_BIN" "${WORK_DIR}/solo/install.sh" install --non-interactive --target claude --project-dir "$CURRENT")" "1"
check "modo não interativo sem --version: nada é instalado" missing ".agents"
printf "n\n" | "$BASH_BIN" "${WORK_DIR}/solo/install.sh" install --target claude --no-skill --project-dir "$CURRENT" > "${WORK_DIR}/last.log" 2>&1 || true
check "modo interativo: recusar a branch main cancela a instalação" missing ".agents"
check "modo interativo: a pergunta sobre a branch main aparece" grep -q "branch main" "${WORK_DIR}/last.log"

echo "== assistente interativo"
new_project "wizard"
printf "9\n2\ny\ny\nn\n" | "$BASH_BIN" "$INSTALLER" install --version local --project-dir "$CURRENT" > "${WORK_DIR}/last.log" 2>&1
check "wizard: opção 2 instala cursor" equals "$(count_files .cursor/commands 'lgpd-*.md')" "$COMMAND_COUNT"
check "wizard: resposta y instala a skill" exists ".agents/skills/lgpd-enterprise-auditor/SKILL.md"
printf "y\n" | "$BASH_BIN" "$INSTALLER" uninstall --project-dir "$CURRENT" > "${WORK_DIR}/last.log" 2>&1
check "wizard: uninstall confirmado remove tudo" missing ".agents"

if command -v pwsh >/dev/null 2>&1; then
  echo "== compatibilidade com install.ps1"
  new_project "cross"
  install_quiet --target cursor --with-skill
  check "install.ps1 lê manifesto do install.sh" \
    equals "$(exit_code_of pwsh -NoProfile -File "${REPO_ROOT}/scripts/install.ps1" check -ProjectDir "$CURRENT")" "0"
fi

echo
if [[ "$FAILURES" -gt 0 ]]; then
  echo "${FAILURES} teste(s) falharam. Último log:"
  cat "${WORK_DIR}/last.log"
  exit 1
fi
echo "Todos os testes passaram."
