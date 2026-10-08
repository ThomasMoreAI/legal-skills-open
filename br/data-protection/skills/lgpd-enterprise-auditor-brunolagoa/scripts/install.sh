#!/usr/bin/env bash
# LGPD Enterprise Auditor — instalador local, por projeto (macOS, Linux, Git Bash/WSL).
# Compatível com bash 3.2 (padrão do macOS): sem arrays associativos, sem mapfile.

set -euo pipefail

REPO_DEFAULT="BrunoLagoa/lgpd-enterprise-auditor"
SCHEMA_VERSION="1"
FRAMEWORK_REL=".agents/lgpd-enterprise-auditor"
STATE_REL="${FRAMEWORK_REL}/.install"
SKILL_NAME="lgpd-enterprise-auditor"
EXIT_NOT_FOUND=2
SUPPORTED_TARGETS="claude cursor vscode opencode agents"

ACTION="install"
NON_INTERACTIVE=0
TARGET=""
WITH_SKILL=""
VERSION=""
PROJECT_DIR=""
REPO="$REPO_DEFAULT"

SOURCE_ROOT=""
SOURCE_REF=""
SOURCE_VERSION=""
TMP_ROOT=""

SCRIPT_FILE="${BASH_SOURCE[0]:-}"
SCRIPT_DIR=""
if [[ -n "$SCRIPT_FILE" && -f "$SCRIPT_FILE" ]]; then
  SCRIPT_DIR="$(cd "$(dirname "$SCRIPT_FILE")" && pwd -P)"
fi

# ---------------------------------------------------------------------------
# Saída e interação
# ---------------------------------------------------------------------------

color() {
  if [[ -t 1 ]]; then printf "\033[%sm" "$1"; fi
}

color_reset() {
  if [[ -t 1 ]]; then printf "\033[0m"; fi
}

log_info() { printf "%s[INFO]%s %s\n" "$(color 36)" "$(color_reset)" "$*"; }
log_ok() { printf "%s[OK]%s %s\n" "$(color 32)" "$(color_reset)" "$*"; }
log_warn() { printf "%s[WARN]%s %s\n" "$(color 33)" "$(color_reset)" "$*" >&2; }
log_error() { printf "%s[ERROR]%s %s\n" "$(color 31)" "$(color_reset)" "$*" >&2; }

die() {
  log_error "$*"
  exit 1
}

die_with_code() {
  local code="$1"
  shift
  log_error "$*"
  exit "$code"
}

# LGPD_AUDITOR_NO_TTY=1 força a leitura pelo stdin (usado nos testes).
tty_available() {
  [[ "${LGPD_AUDITOR_NO_TTY:-0}" != "1" ]] && { : < /dev/tty; } 2>/dev/null
}

# Perguntas vão para o terminal (ou stderr) para não poluir capturas $(...).
prompt_out() {
  if tty_available; then
    printf "%s" "$*" > /dev/tty
  else
    printf "%s" "$*" >&2
  fi
}

read_answer() {
  local __var="$1"
  local __reply=""
  if tty_available; then
    IFS= read -r __reply < /dev/tty || die "Entrada interativa indisponível. Use --non-interactive."
  else
    IFS= read -r __reply || die "Entrada interativa indisponível. Use --non-interactive."
  fi
  printf -v "$__var" "%s" "$__reply"
}

confirm() {
  local question="$1"
  local default_choice="${2:-y}"
  local suffix="[y/N]"
  local answer=""
  if [[ "$default_choice" == "y" ]]; then suffix="[Y/n]"; fi
  prompt_out "${question} ${suffix}: "
  read_answer answer
  answer="$(printf "%s" "${answer:-$default_choice}" | tr '[:upper:]' '[:lower:]')"
  [[ "$answer" == "y" || "$answer" == "yes" || "$answer" == "s" || "$answer" == "sim" ]]
}

# Imprime as opções e devolve (stdout) o número escolhido.
choose_index() {
  local question="$1"
  shift
  local idx=1
  local answer=""
  local option
  prompt_out "${question}"$'\n'
  for option in "$@"; do
    prompt_out "  ${idx}) ${option}"$'\n'
    idx=$((idx + 1))
  done
  while true; do
    prompt_out "Selecione uma opção [1-$#]: "
    read_answer answer
    if [[ "$answer" =~ ^[0-9]+$ ]] && (( answer >= 1 && answer <= $# )); then
      printf "%s" "$answer"
      return 0
    fi
    log_warn "Opção inválida. Tente novamente."
  done
}

print_banner() {
  cat <<'EOF'
 _     ____ ____  ____
| |   / ___|  _ \|  _ \
| |  | |  _| |_) | | | |
| |__| |_| |  __/| |_| |
|_____\____|_|   |____/
EOF
  printf "\nLGPD Enterprise Auditor %s\n\n" "$1"
  printf "Framework de auditoria de conformidade LGPD orientado a evidências, para usar com o seu\n"
  printf "assistente de IA (Claude Code, Cursor, VS Code + Copilot, OpenCode, Codex, Gemini CLI).\n"
  printf "A instalação é local: tudo fica dentro do projeto auditado.\n\n"
}

usage() {
  cat <<'EOF'
LGPD Enterprise Auditor — instalador

Uso:
  install.sh [install|update|uninstall|check] [opções]

Ações:
  install     Instala o framework e os comandos da ferramenta escolhida (padrão)
  update      Reinstala as ferramentas já instaladas na versão escolhida
  uninstall   Remove a instalação de uma ferramenta (ou de todas)
  check       Verifica a instalação do projeto

Opções:
  --target <claude|cursor|vscode|opencode|agents>  Ferramenta (obrigatória com --non-interactive no install)
  --with-skill            Instala também a skill
  --no-skill              Não instala a skill (padrão)
  --project-dir <dir>     Projeto de destino (padrão: raiz git do diretório atual)
  --version <ref|local>   Tag, branch ou "local" (padrão: última tag publicada)
  --repo <owner/repo>     Repositório GitHub (padrão: BrunoLagoa/lgpd-enterprise-auditor)
  --non-interactive       Executa sem perguntas
  -h, --help              Exibe esta ajuda

Exemplos:
  curl -fsSL https://github.com/BrunoLagoa/lgpd-enterprise-auditor/releases/latest/download/install.sh | bash -s -- install
  ./scripts/install.sh install --target cursor --with-skill --project-dir ../meu-app
  ./scripts/install.sh update --non-interactive
  ./scripts/install.sh uninstall --target claude --non-interactive
EOF
}

# ---------------------------------------------------------------------------
# Argumentos e ambiente
# ---------------------------------------------------------------------------

require_value() {
  [[ $# -ge 2 && -n "$2" && "${2#--}" == "$2" ]] || die "A opção $1 exige um valor."
}

parse_args() {
  if [[ $# -gt 0 && "${1#-}" == "$1" ]]; then
    ACTION="$1"
    shift
  fi

  while [[ $# -gt 0 ]]; do
    case "$1" in
      --target) require_value "$@"; TARGET="$2"; shift 2 ;;
      --with-skill) WITH_SKILL=1; shift ;;
      --no-skill) WITH_SKILL=0; shift ;;
      --project-dir) require_value "$@"; PROJECT_DIR="$2"; shift 2 ;;
      --version) require_value "$@"; VERSION="$2"; shift 2 ;;
      --repo) require_value "$@"; REPO="$2"; shift 2 ;;
      --non-interactive) NON_INTERACTIVE=1; shift ;;
      -h|--help) usage; exit 0 ;;
      *) die "Argumento desconhecido: $1 (use --help)" ;;
    esac
  done

  case "$ACTION" in
    install|update|uninstall|check) ;;
    *) die "Ação inválida: $ACTION (use install, update, uninstall ou check)" ;;
  esac

  if [[ -n "$TARGET" ]] && ! is_supported_target "$TARGET"; then
    die "Ferramenta não suportada: $TARGET (use: ${SUPPORTED_TARGETS// /, })"
  fi

  [[ "$REPO" =~ ^[A-Za-z0-9._-]+/[A-Za-z0-9._-]+$ ]] || die "Repositório inválido: $REPO (use owner/repo)"
}

is_supported_target() {
  case "$1" in
    claude|cursor|vscode|opencode|agents) return 0 ;;
    *) return 1 ;;
  esac
}

detect_os() {
  case "$(uname -s | tr '[:upper:]' '[:lower:]')" in
    darwin*) printf "macos" ;;
    msys*|mingw*|cygwin*) printf "windows" ;;
    *) printf "linux" ;;
  esac
}

iso_timestamp() {
  date -u +"%Y-%m-%dT%H:%M:%SZ"
}

ensure_command() {
  command -v "$1" >/dev/null 2>&1 || die "Pré-requisito ausente: $1"
}

resolve_project_dir() {
  if [[ -n "$PROJECT_DIR" ]]; then
    [[ -d "$PROJECT_DIR" ]] || die "Diretório do projeto não encontrado: $PROJECT_DIR"
    PROJECT_DIR="$(cd "$PROJECT_DIR" && pwd -P)"
  else
    local current
    current="$(pwd -P)"
    PROJECT_DIR="$current"
    while [[ "$current" != "/" ]]; do
      if [[ -e "${current}/.git" ]]; then
        PROJECT_DIR="$current"
        break
      fi
      current="$(dirname "$current")"
    done
  fi

  if [[ "$PROJECT_DIR" == "/" || "$PROJECT_DIR" == "$(cd "$HOME" && pwd -P)" ]]; then
    die "Recusado instalar em ${PROJECT_DIR}. Rode na raiz do projeto ou use --project-dir."
  fi
}

# ---------------------------------------------------------------------------
# Ferramentas (targets)
# ---------------------------------------------------------------------------

target_label() {
  case "$1" in
    claude) printf "claude (Claude Code)" ;;
    cursor) printf "cursor (Cursor)" ;;
    vscode) printf "vscode (VS Code + GitHub Copilot)" ;;
    opencode) printf "opencode (OpenCode)" ;;
    agents) printf "agents (outra ferramenta: Codex, Gemini CLI e similares)" ;;
  esac
}

target_commands_dir() {
  case "$1" in
    claude) printf ".claude/commands" ;;
    cursor) printf ".cursor/commands" ;;
    vscode) printf ".github/prompts" ;;
    opencode) printf ".opencode/commands" ;;
    agents) printf "" ;;
  esac
}

target_command_file() {
  local target="$1"
  local stem="$2"
  if [[ "$target" == "vscode" ]]; then
    printf "%s.prompt.md" "$stem"
  else
    printf "%s.md" "$stem"
  fi
}

target_skill_dir() {
  if [[ "$1" == "claude" ]]; then
    printf ".claude/skills/%s" "$SKILL_NAME"
  else
    printf ".agents/skills/%s" "$SKILL_NAME"
  fi
}

print_next_steps() {
  local target="$1"
  local skill="$2"
  printf "\nPróximos passos\n"
  case "$target" in
    claude) printf "  Abra o Claude Code na raiz do projeto (claude) e rode /lgpd-saas, /lgpd-full-audit etc.\n" ;;
    cursor) printf "  No chat do Cursor, digite /lgpd-saas, /lgpd-full-audit etc.\n" ;;
    vscode) printf "  No Copilot Chat do VS Code, digite /lgpd-saas, /lgpd-full-audit etc.\n" ;;
    opencode) printf "  Rode opencode na raiz do projeto e use /lgpd-saas, /lgpd-full-audit etc.\n" ;;
    agents) printf "  Peça ao seu agente: \"faça uma auditoria LGPD deste projeto\" — ele carrega a skill %s.\n" "$SKILL_NAME" ;;
  esac
  if [[ "$skill" == "1" && "$target" != "agents" ]]; then
    printf "  Com a skill instalada, você também pode pedir a auditoria em linguagem natural.\n"
  fi
  printf "  Coloque política de privacidade, RIPD, contratos (DPA) e nomeação do DPO dentro do projeto\n"
  printf "  (ex.: docs/lgpd/) para que contem como evidência documental.\n"
}

# Claude e OpenCode leem o frontmatter como está.
# Cursor: remove o frontmatter e promove a description para a primeira linha.
# VS Code: mantém só os campos aceitos em .prompt.md (name, description) e roda em modo agent.
render_command() {
  local target="$1"
  local src="$2"
  local dest="$3"

  case "$target" in
    cursor)
      awk '
        NR == 1 && $0 == "---" { in_fm = 1; next }
        in_fm && $0 == "---" { in_fm = 0; if (desc != "") { print "> " desc; print "" }; skip_blank = 1; next }
        in_fm { if ($0 ~ /^description:/) { desc = $0; sub(/^description:[[:space:]]*/, "", desc); gsub(/^["\047]|["\047]$/, "", desc) }; next }
        skip_blank && $0 ~ /^[[:space:]]*$/ { next }
        { skip_blank = 0; print }
      ' "$src" > "$dest"
      ;;
    vscode)
      awk '
        NR == 1 && $0 == "---" { in_fm = 1; next }
        in_fm && $0 == "---" { in_fm = 0; print "---"; if (name != "") print name; if (desc != "") print desc; print "agent: agent"; print "---"; next }
        in_fm { if ($0 ~ /^name:/) name = $0; if ($0 ~ /^description:/) desc = $0; next }
        { print }
      ' "$src" > "$dest"
      ;;
    *)
      cp "$src" "$dest"
      ;;
  esac
}

# ---------------------------------------------------------------------------
# Origem dos arquivos (local ou GitHub)
# ---------------------------------------------------------------------------

cleanup() {
  if [[ -n "$TMP_ROOT" && -d "$TMP_ROOT" ]]; then
    rm -rf "$TMP_ROOT"
  fi
}

local_source_root() {
  if [[ -z "$SCRIPT_DIR" ]]; then
    return 1
  fi
  local root
  root="$(cd "$SCRIPT_DIR/.." && pwd -P)"
  if [[ -d "${root}/${FRAMEWORK_REL}" && -f "${root}/SKILL.md" && -d "${root}/commands" ]]; then
    printf "%s" "$root"
    return 0
  fi
  return 1
}

skill_version() {
  sed -n 's/^[[:space:]]*version:[[:space:]]*"\{0,1\}\([^"]*\)"\{0,1\}[[:space:]]*$/\1/p' "$1" | head -n 1
}

# Imprime a última tag publicada. Retorno: 0 com a tag; 1 se o repositório não tem tag v*;
# 2 se a consulta falhou (sem rede, limite da API do GitHub ou modo offline).
fetch_latest_tag() {
  local response
  [[ "${LGPD_AUDITOR_OFFLINE:-0}" != "1" ]] || return 2
  command -v curl >/dev/null 2>&1 || return 2
  response="$(curl -fsSL --max-time 10 "https://api.github.com/repos/${REPO}/tags?per_page=100" 2>/dev/null)" || return 2
  printf "%s" "$response" \
    | grep -o '"name": *"v[0-9][^"]*"' \
    | sed 's/.*"\(v[^"]*\)"/\1/' \
    | sort -V \
    | tail -n 1
}

# Define SOURCE_REF antes de baixar (para exibir no banner e no resumo).
resolve_ref() {
  if [[ -z "$VERSION" ]]; then
    if local_source_root >/dev/null; then
      VERSION="local"
    else
      local tag_status=0
      VERSION="$(fetch_latest_tag)" || tag_status=$?
      if [[ -z "$VERSION" ]]; then
        if [[ "$tag_status" -eq 2 ]]; then
          # Falha de consulta não é "sem versão publicada": a branch main pode ter mudanças não lançadas.
          log_warn "Não foi possível consultar a última versão publicada (sem rede ou limite da API do GitHub)."
          if [[ "$NON_INTERACTIVE" -eq 1 ]]; then
            die "Informe a versão com --version (ex.: --version vX.Y.Z) ou tente de novo mais tarde."
          fi
          confirm "Instalar a partir da branch main, que pode conter mudanças ainda não publicadas?" "n" \
            || die "Instalação cancelada. Informe a versão com --version (ex.: --version vX.Y.Z)."
        else
          log_warn "Nenhuma tag publicada encontrada; usando a branch main."
        fi
        VERSION="main"
      fi
    fi
  fi
  SOURCE_REF="$VERSION"

  if [[ "$SOURCE_REF" == "local" ]]; then
    SOURCE_ROOT="$(local_source_root)" || die "--version local exige rodar o script a partir de um clone do repositório."
    SOURCE_VERSION="$(skill_version "${SOURCE_ROOT}/SKILL.md")"
  fi
}

ref_label() {
  if [[ "$SOURCE_REF" == "local" ]]; then
    printf "v%s (cópia local em %s)" "$SOURCE_VERSION" "$SOURCE_ROOT"
  else
    printf "%s" "$SOURCE_REF"
  fi
}

fetch_source() {
  if [[ -n "$SOURCE_ROOT" ]]; then
    return 0
  fi
  ensure_command curl
  ensure_command tar
  local archive="${TMP_ROOT}/source.tar.gz"
  local url="https://codeload.github.com/${REPO}/tar.gz/${SOURCE_REF}"
  log_info "Baixando ${REPO}@${SOURCE_REF}..."
  curl -fsSL "$url" -o "$archive" || die "Falha ao baixar ${url}. Verifique a versão (--version) e a conexão."
  mkdir -p "${TMP_ROOT}/source"
  tar -xzf "$archive" -C "${TMP_ROOT}/source"
  local extracted
  extracted="$(find "${TMP_ROOT}/source" -mindepth 1 -maxdepth 1 -type d | head -n 1)"
  [[ -n "$extracted" && -d "${extracted}/${FRAMEWORK_REL}" && -f "${extracted}/SKILL.md" && -d "${extracted}/commands" ]] \
    || die "Conteúdo baixado inválido para ${SOURCE_REF}."
  SOURCE_ROOT="$extracted"
  SOURCE_VERSION="$(skill_version "${SOURCE_ROOT}/SKILL.md")"
}

guard_not_source_repo() {
  if [[ -n "$SOURCE_ROOT" && "$SOURCE_ROOT" == "$PROJECT_DIR" ]]; then
    die "O destino é o próprio repositório do framework. Use --project-dir para apontar o projeto a ser auditado."
  fi
}

# ---------------------------------------------------------------------------
# Manifestos (um por ferramenta, em .agents/lgpd-enterprise-auditor/.install/)
# ---------------------------------------------------------------------------

manifest_path() {
  printf "%s/%s/%s.json" "$PROJECT_DIR" "$STATE_REL" "$1"
}

json_value() {
  sed -n "s/^[[:space:]]*\"$2\":[[:space:]]*\"\{0,1\}\([^\",]*\)\"\{0,1\},\{0,1\}[[:space:]]*$/\1/p" "$1" | head -n 1
}

manifest_files() {
  awk '
    /"files":[[:space:]]*\[/ { if ($0 !~ /\]/) in_files = 1; next }
    in_files && /\]/ { in_files = 0; next }
    in_files { gsub(/^[[:space:]]*"|",?[[:space:]]*$/, ""); if ($0 != "") print }
  ' "$1"
}

installed_targets() {
  local target
  for target in $SUPPORTED_TARGETS; do
    if [[ -f "$(manifest_path "$target")" ]]; then
      printf "%s\n" "$target"
    fi
  done
}

write_manifest() {
  local target="$1"
  local skill="$2"
  local files="$3"
  local skill_dir="$4"
  local manifest
  manifest="$(manifest_path "$target")"
  mkdir -p "$(dirname "$manifest")"

  local skill_json="false"
  if [[ "$skill" == "1" ]]; then skill_json="true"; fi

  {
    printf "{\n"
    printf "  \"schemaVersion\": \"%s\",\n" "$SCHEMA_VERSION"
    printf "  \"project\": \"lgpd-enterprise-auditor\",\n"
    printf "  \"version\": \"%s\",\n" "$SOURCE_VERSION"
    printf "  \"ref\": \"%s\",\n" "$SOURCE_REF"
    printf "  \"repo\": \"%s\",\n" "$REPO"
    printf "  \"target\": \"%s\",\n" "$target"
    printf "  \"withSkill\": %s,\n" "$skill_json"
    printf "  \"os\": \"%s\",\n" "$(detect_os)"
    printf "  \"frameworkDir\": \"%s\",\n" "$FRAMEWORK_REL"
    printf "  \"commandsDir\": \"%s\",\n" "$(target_commands_dir "$target")"
    printf "  \"skillDir\": \"%s\",\n" "$skill_dir"
    printf "  \"installedAt\": \"%s\",\n" "$(iso_timestamp)"
    printf "  \"files\": ["
    local first=1
    local file
    while IFS= read -r file; do
      [[ -n "$file" ]] || continue
      if [[ "$first" -eq 1 ]]; then printf "\n"; first=0; else printf ",\n"; fi
      printf "    \"%s\"" "$file"
    done <<< "$files"
    if [[ "$first" -eq 0 ]]; then printf "\n  "; fi
    printf "]\n"
    printf "}\n"
  } > "$manifest"
}

# ---------------------------------------------------------------------------
# Instalação e remoção
# ---------------------------------------------------------------------------

safe_rel_path() {
  [[ -n "$1" && "${1:0:1}" != "/" && "$1" != *".."* ]]
}

# Outra ferramenta (diferente de $1) usa a mesma pasta de skill?
skill_dir_shared() {
  local target="$1"
  local skill_dir="$2"
  local other manifest
  for other in $(installed_targets); do
    [[ "$other" != "$target" ]] || continue
    manifest="$(manifest_path "$other")"
    if [[ "$(json_value "$manifest" withSkill)" == "true" && "$(json_value "$manifest" skillDir)" == "$skill_dir" ]]; then
      return 0
    fi
  done
  return 1
}

prune_empty_dirs() {
  local dir
  for dir in .claude/commands .claude/skills .claude .cursor/commands .cursor .github/prompts .github \
    .opencode/commands .opencode .agents/skills .agents; do
    rmdir "${PROJECT_DIR}/${dir}" 2>/dev/null || true
  done
}

remove_target_files() {
  local target="$1"
  local manifest
  manifest="$(manifest_path "$target")"
  [[ -f "$manifest" ]] || return 0

  local file
  while IFS= read -r file; do
    safe_rel_path "$file" || continue
    rm -f "${PROJECT_DIR}/${file}"
  done < <(manifest_files "$manifest")

  local skill_dir
  skill_dir="$(json_value "$manifest" skillDir)"
  if [[ "$(json_value "$manifest" withSkill)" == "true" ]] && safe_rel_path "$skill_dir" \
    && [[ "$skill_dir" == *"/${SKILL_NAME}" ]] && ! skill_dir_shared "$target" "$skill_dir"; then
    rm -rf "${PROJECT_DIR:?}/${skill_dir}"
  fi
}

backup_existing() {
  local target="$1"
  local backup_dir
  backup_dir="${PROJECT_DIR}/.lgpd-auditor-backup/$(date +%Y%m%d%H%M%S)"
  mkdir -p "$backup_dir"

  if [[ -d "${PROJECT_DIR}/${FRAMEWORK_REL}" ]]; then
    mkdir -p "${backup_dir}/$(dirname "$FRAMEWORK_REL")"
    cp -R "${PROJECT_DIR}/${FRAMEWORK_REL}" "${backup_dir}/${FRAMEWORK_REL}"
  fi

  local manifest file skill_dir
  manifest="$(manifest_path "$target")"
  if [[ -f "$manifest" ]]; then
    while IFS= read -r file; do
      safe_rel_path "$file" || continue
      if [[ -f "${PROJECT_DIR}/${file}" ]]; then
        mkdir -p "${backup_dir}/$(dirname "$file")"
        cp "${PROJECT_DIR}/${file}" "${backup_dir}/${file}"
      fi
    done < <(manifest_files "$manifest")
    skill_dir="$(json_value "$manifest" skillDir)"
    if safe_rel_path "$skill_dir" && [[ -d "${PROJECT_DIR}/${skill_dir}" ]]; then
      mkdir -p "${backup_dir}/$(dirname "$skill_dir")"
      cp -R "${PROJECT_DIR}/${skill_dir}" "${backup_dir}/${skill_dir}"
    fi
  fi
  log_info "Backup criado em ${backup_dir}"
  log_info "Dica: adicione .lgpd-auditor-backup/ ao .gitignore do projeto."
}

install_framework() {
  local framework_dir="${PROJECT_DIR}/${FRAMEWORK_REL}"
  local saved_state="${TMP_ROOT}/install-state"

  if [[ -d "${framework_dir}/.install" ]]; then
    rm -rf "$saved_state"
    mv "${framework_dir}/.install" "$saved_state"
  fi
  rm -rf "$framework_dir"
  mkdir -p "$(dirname "$framework_dir")"
  cp -R "${SOURCE_ROOT}/${FRAMEWORK_REL}" "$framework_dir"
  rm -rf "${framework_dir}/.install"
  find "$framework_dir" -name .DS_Store -type f -delete 2>/dev/null || true
  if [[ -d "$saved_state" ]]; then
    mv "$saved_state" "${framework_dir}/.install"
  fi
}

install_target() {
  local target="$1"
  local skill="$2"

  remove_target_files "$target"
  install_framework

  local files=""
  local commands_dir
  commands_dir="$(target_commands_dir "$target")"
  if [[ -n "$commands_dir" ]]; then
    mkdir -p "${PROJECT_DIR}/${commands_dir}"
    local src stem rel
    for src in "${SOURCE_ROOT}"/commands/*.md; do
      [[ -f "$src" ]] || continue
      stem="$(basename "$src" .md)"
      rel="${commands_dir}/$(target_command_file "$target" "$stem")"
      render_command "$target" "$src" "${PROJECT_DIR}/${rel}"
      files="${files}${rel}"$'\n'
    done
    [[ -n "$files" ]] || die "Nenhum comando encontrado em ${SOURCE_ROOT}/commands."
  fi

  local skill_dir=""
  if [[ "$skill" == "1" ]]; then
    skill_dir="$(target_skill_dir "$target")"
    mkdir -p "${PROJECT_DIR}/${skill_dir}"
    cp "${SOURCE_ROOT}/SKILL.md" "${PROJECT_DIR}/${skill_dir}/SKILL.md"
  fi

  write_manifest "$target" "$skill" "$files" "$skill_dir"
  prune_empty_dirs
  log_ok "$(target_label "$target") instalado (v${SOURCE_VERSION})."
}

warn_version_drift() {
  local target other installed_version
  target="$1"
  for other in $(installed_targets); do
    [[ "$other" != "$target" ]] || continue
    installed_version="$(json_value "$(manifest_path "$other")" version)"
    if [[ "$installed_version" != "$SOURCE_VERSION" ]]; then
      log_warn "Os comandos de ${other} estão na v${installed_version}, mas o framework agora está na v${SOURCE_VERSION}. Rode a ação update para alinhar."
    fi
  done
}

# ---------------------------------------------------------------------------
# Ações
# ---------------------------------------------------------------------------

run_install() {
  resolve_ref
  guard_not_source_repo

  if [[ "$NON_INTERACTIVE" -eq 0 ]]; then
    print_banner "$(ref_label)"
    log_info "Sistema operacional: $(detect_os)"
    log_info "Projeto: ${PROJECT_DIR}"
    printf "\n"
  fi

  if [[ -z "$TARGET" ]]; then
    [[ "$NON_INTERACTIVE" -eq 0 ]] || die "Informe --target no modo --non-interactive."
    local choice
    choice="$(choose_index "1 - Selecione a ferramenta" \
      "$(target_label claude)" "$(target_label cursor)" "$(target_label vscode)" \
      "$(target_label opencode)" "$(target_label agents)")"
    TARGET="$(printf "%s" "$SUPPORTED_TARGETS" | cut -d' ' -f"$choice")"
  else
    [[ "$NON_INTERACTIVE" -eq 1 ]] || printf "1 - Ferramenta\n  > %s\n" "$(target_label "$TARGET")"
  fi

  if [[ "$TARGET" == "agents" ]]; then
    [[ "$WITH_SKILL" != "0" ]] || die "A opção agents não tem slash commands: a skill é obrigatória (remova --no-skill)."
    WITH_SKILL=1
    [[ "$NON_INTERACTIVE" -eq 1 ]] || printf "2 - Skill\n  > sim (obrigatória para agents: é a forma de acionar a auditoria)\n"
  elif [[ -z "$WITH_SKILL" ]]; then
    WITH_SKILL=0
    if [[ "$NON_INTERACTIVE" -eq 0 ]]; then
      prompt_out "2 - Instalar também a skill?"$'\n'
      prompt_out "    Permite acionar a auditoria em linguagem natural, sem slash command."$'\n'
      if confirm "    Instalar a skill?" "n"; then WITH_SKILL=1; fi
    fi
  fi

  local commands_dir skill_label
  commands_dir="$(target_commands_dir "$TARGET")"
  skill_label="não"
  if [[ "$WITH_SKILL" == "1" ]]; then skill_label="sim → ${PROJECT_DIR}/$(target_skill_dir "$TARGET")"; fi

  printf "\nResumo da instalação\n"
  printf "  Ferramenta: %s\n" "$(target_label "$TARGET")"
  printf "  Versão:     %s\n" "$(ref_label)"
  printf "  Framework:  %s/%s\n" "$PROJECT_DIR" "$FRAMEWORK_REL"
  if [[ -n "$commands_dir" ]]; then
    printf "  Comandos:   %s/%s\n" "$PROJECT_DIR" "$commands_dir"
  fi
  printf "  Skill:      %s\n" "$skill_label"
  if [[ -f "$(manifest_path "$TARGET")" ]]; then
    printf "  Atenção:    já existe uma instalação para %s (v%s); ela será substituída.\n" \
      "$TARGET" "$(json_value "$(manifest_path "$TARGET")" version)"
  fi
  printf "\n"

  if [[ "$NON_INTERACTIVE" -eq 0 ]]; then
    confirm "Confirmar instalação?" "y" || { log_warn "Instalação cancelada."; exit 0; }
    if [[ -d "${PROJECT_DIR}/${FRAMEWORK_REL}" ]] && confirm "Instalação existente detectada. Criar backup antes de substituir?" "y"; then
      backup_existing "$TARGET"
    fi
  fi

  fetch_source
  guard_not_source_repo
  install_target "$TARGET" "$WITH_SKILL"
  warn_version_drift "$TARGET"
  print_next_steps "$TARGET" "$WITH_SKILL"
}

run_update() {
  local targets
  if [[ -n "$TARGET" ]]; then
    [[ -f "$(manifest_path "$TARGET")" ]] || die_with_code "$EXIT_NOT_FOUND" "Nenhuma instalação de ${TARGET} encontrada em ${PROJECT_DIR}."
    targets="$TARGET"
  else
    targets="$(installed_targets)"
    [[ -n "$targets" ]] || die_with_code "$EXIT_NOT_FOUND" "Nenhuma instalação encontrada em ${PROJECT_DIR}. Use a ação install."
  fi

  resolve_ref
  guard_not_source_repo
  printf "\nResumo da atualização\n"
  printf "  Projeto: %s\n" "$PROJECT_DIR"
  printf "  Versão:  %s\n" "$(ref_label)"
  local target
  for target in $targets; do
    printf "  - %s (atual: v%s)\n" "$(target_label "$target")" "$(json_value "$(manifest_path "$target")" version)"
  done
  printf "\n"

  if [[ "$NON_INTERACTIVE" -eq 0 ]]; then
    confirm "Confirmar atualização?" "y" || { log_warn "Atualização cancelada."; exit 0; }
  fi

  fetch_source
  guard_not_source_repo
  local skill
  for target in $targets; do
    skill=0
    if [[ "$(json_value "$(manifest_path "$target")" withSkill)" == "true" ]]; then skill=1; fi
    if [[ -n "$WITH_SKILL" && -n "$TARGET" && "$target" != "agents" ]]; then skill="$WITH_SKILL"; fi
    install_target "$target" "$skill"
  done
}

run_uninstall() {
  local installed
  installed="$(installed_targets)"
  [[ -n "$installed" ]] || die_with_code "$EXIT_NOT_FOUND" "Nenhuma instalação encontrada em ${PROJECT_DIR}."

  local targets=""
  if [[ -n "$TARGET" ]]; then
    [[ -f "$(manifest_path "$TARGET")" ]] || die_with_code "$EXIT_NOT_FOUND" "Nenhuma instalação de ${TARGET} encontrada em ${PROJECT_DIR}."
    targets="$TARGET"
  elif [[ "$NON_INTERACTIVE" -eq 1 || "$(printf "%s\n" "$installed" | wc -l | tr -d ' ')" -eq 1 ]]; then
    targets="$installed"
  else
    local options="" target choice count
    for target in $installed; do options="${options}${target} "; done
    # shellcheck disable=SC2086
    choice="$(choose_index "Qual instalação remover?" $options "todas")"
    count="$(printf "%s\n" "$installed" | wc -l | tr -d ' ')"
    if [[ "$choice" -gt "$count" ]]; then
      targets="$installed"
    else
      targets="$(printf "%s\n" "$installed" | sed -n "${choice}p")"
    fi
  fi

  printf "\nResumo da remoção\n"
  printf "  Projeto: %s\n" "$PROJECT_DIR"
  local target
  for target in $targets; do
    printf "  - %s\n" "$(target_label "$target")"
  done
  printf "\n"

  if [[ "$NON_INTERACTIVE" -eq 0 ]]; then
    confirm "Confirmar remoção?" "n" || { log_warn "Remoção cancelada."; exit 0; }
  fi

  for target in $targets; do
    remove_target_files "$target"
    rm -f "$(manifest_path "$target")"
    log_ok "$(target_label "$target") removido."
  done

  if [[ -z "$(installed_targets)" ]]; then
    rm -rf "${PROJECT_DIR:?}/${FRAMEWORK_REL}"
    log_ok "Framework removido de ${PROJECT_DIR}/${FRAMEWORK_REL}."
  fi
  prune_empty_dirs
}

run_check() {
  local installed
  installed="$(installed_targets)"
  [[ -n "$installed" ]] || die_with_code "$EXIT_NOT_FOUND" "Nenhuma instalação encontrada em ${PROJECT_DIR}."

  local broken=0
  if [[ ! -f "${PROJECT_DIR}/${FRAMEWORK_REL}/core/auditor-core.md" ]]; then
    log_error "Framework incompleto em ${PROJECT_DIR}/${FRAMEWORK_REL}."
    broken=1
  fi

  local target manifest file missing skill_dir version newest=""
  for target in $installed; do
    manifest="$(manifest_path "$target")"
    version="$(json_value "$manifest" version)"
    missing=0
    while IFS= read -r file; do
      [[ -f "${PROJECT_DIR}/${file}" ]] || { log_error "${target}: arquivo ausente ${file}"; missing=1; }
    done < <(manifest_files "$manifest")
    skill_dir="$(json_value "$manifest" skillDir)"
    if [[ "$(json_value "$manifest" withSkill)" == "true" && ! -f "${PROJECT_DIR}/${skill_dir}/SKILL.md" ]]; then
      log_error "${target}: skill ausente em ${skill_dir}"
      missing=1
    fi
    if [[ "$missing" -eq 0 ]]; then
      log_ok "$(target_label "$target") — v${version}, skill: $(json_value "$manifest" withSkill), instalado em $(json_value "$manifest" installedAt)"
    else
      broken=1
    fi
  done

  newest="$(fetch_latest_tag || true)"
  if [[ -n "$newest" && "v${version}" != "$newest" ]]; then
    log_info "Versão publicada mais recente: ${newest}. Rode a ação update para atualizar."
  fi

  if [[ "$broken" -eq 1 ]]; then
    log_error "Instalação com problemas. Rode a ação install novamente para corrigir."
    exit 1
  fi
}

main() {
  parse_args "$@"
  resolve_project_dir
  TMP_ROOT="$(mktemp -d)"
  trap cleanup EXIT

  case "$ACTION" in
    install) run_install ;;
    update) run_update ;;
    uninstall) run_uninstall ;;
    check) run_check ;;
  esac
}

main "$@"
