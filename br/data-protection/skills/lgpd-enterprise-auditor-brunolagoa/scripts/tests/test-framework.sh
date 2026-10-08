#!/usr/bin/env bash
# Confere as invariantes do framework que antes dependiam de leitura: catálogo de itens,
# paridade mecânica entre a skill e o framework, cenários e módulos, manifestos e documentação.
# Uso: scripts/tests/test-framework.sh

# As crases dentro de aspas simples são as do Markdown conferido, não expansões do shell.
# shellcheck disable=SC2016

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd -P)"
FRAMEWORK="${REPO_ROOT}/.agents/lgpd-enterprise-auditor"
SKILL="${REPO_ROOT}/SKILL.md"
SCORING="${FRAMEWORK}/core/scoring-engine.md"
TEMPLATE="${FRAMEWORK}/reports/html-report-template.html"
MODULE_DIRS="legal governance cloud appsec mobile devsecops ai-llm"
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
# Compara duas listas (uma por linha, já ordenadas); mostra a diferença quando houver.
same() {
  local name="$1" left="$2" right="$3"
  if [[ "$left" == "$right" && -n "$left" ]]; then
    ok "$name"
  else
    fail "$name"
    diff <(printf "%s\n" "$left") <(printf "%s\n" "$right") | sed 's/^/         /' || true
  fi
}

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

module_files() {
  local dir
  for dir in $MODULE_DIRS; do
    find "${FRAMEWORK}/${dir}" -name '*.md' -type f
  done | sort
}

# ---------------------------------------------------------------------------
echo "Catálogo de itens"
# ---------------------------------------------------------------------------
# Linhas de item: | `ID` | Item | Domínio | `Criticidade` | Agravante | `Controle` | Fundamento |
module_files | while IFS= read -r file; do
  LC_ALL=C awk -v file="${file#"${FRAMEWORK}"/}" '
    /^\| `[A-Z][A-Z]+-[0-9]+` \|/ {
      n = split($0, c, /[ ]*\|[ ]*/)
      id = c[2]; gsub(/`/, "", id)
      print id "\t" c[4] "\t" c[5] "\t" c[7] "\t" (n - 2) "\t" file "\t" (c[8] == "" ? "sem-fundamento" : "ok")
    }
  ' "$file"
done > "${TMP_DIR}/catalog.tsv"

DOMAIN_MAP="$(LC_ALL=C awk '/^\| `(BL|[0-9]+)` \|/ { split($0, c, /[ ]*\|[ ]*/); gsub(/`/, "", c[2]); gsub(/`/, "", c[4]); print c[2] "=" c[4] }' "$SCORING")"
DOMAIN_CODES="$(printf "%s\n" "$DOMAIN_MAP" | cut -d= -f1)"

check "há itens no catálogo" test -s "${TMP_DIR}/catalog.tsv"
DUPLICATES="$(cut -f1 "${TMP_DIR}/catalog.tsv" | sort | uniq -d | tr '\n' ' ')"
check "IDs únicos${DUPLICATES:+ (repetidos: ${DUPLICATES})}" test -z "$DUPLICATES"
BAD_COLUMNS="$(awk -F'\t' '$5 != 7 { print $1 }' "${TMP_DIR}/catalog.tsv" | tr '\n' ' ')"
check "toda linha de item tem 7 colunas${BAD_COLUMNS:+ (${BAD_COLUMNS})}" test -z "$BAD_COLUMNS"
BAD_CRITICALITY="$(awk -F'\t' '$3 !~ /^`(CRITICO|ALTO|MEDIO|BAIXO)`$/ { print $1 }' "${TMP_DIR}/catalog.tsv" | tr '\n' ' ')"
check "criticidade canônica em todos os itens${BAD_CRITICALITY:+ (${BAD_CRITICALITY})}" test -z "$BAD_CRITICALITY"
BAD_CONTROL="$(awk -F'\t' '$4 !~ /^`(TECNICO|DOCUMENTAL)`$/ { print $1 }' "${TMP_DIR}/catalog.tsv" | tr '\n' ' ')"
check "tipo de controle canônico em todos os itens${BAD_CONTROL:+ (${BAD_CONTROL})}" test -z "$BAD_CONTROL"
BAD_BASIS="$(awk -F'\t' '$7 != "ok" { print $1 }' "${TMP_DIR}/catalog.tsv" | tr '\n' ' ')"
check "todo item cita o fundamento${BAD_BASIS:+ (${BAD_BASIS})}" test -z "$BAD_BASIS"
BAD_DOMAIN=""
while IFS=$'\t' read -r id domain _; do
  printf "%s\n" "$DOMAIN_CODES" | grep -qxF -- "$domain" || BAD_DOMAIN="${BAD_DOMAIN}${id} "
done < "${TMP_DIR}/catalog.tsv"
check "domínio de cada item existe no mapa de core/scoring-engine.md${BAD_DOMAIN:+ (${BAD_DOMAIN})}" test -z "$BAD_DOMAIN"
# Cada prefixo pertence a um único arquivo: é o que mantém a numeração estável.
SPLIT_PREFIXES="$(awk -F'\t' '{ split($1, p, "-"); print p[1] "\t" $6 }' "${TMP_DIR}/catalog.tsv" | sort -u | cut -f1 | uniq -d | tr '\n' ' ')"
check "cada prefixo de ID fica em um só arquivo${SPLIT_PREFIXES:+ (${SPLIT_PREFIXES})}" test -z "$SPLIT_PREFIXES"

if bash "${REPO_ROOT}/scripts/update-skill-catalog.sh" --check > "${TMP_DIR}/skill-check.txt" 2>&1; then
  ok "catálogo da skill gerado a partir dos módulos e em dia"
else
  fail "catálogo da skill em dia ($(tr '\n' ' ' < "${TMP_DIR}/skill-check.txt"))"
fi

PREFIXES="$(cut -f1 "${TMP_DIR}/catalog.tsv" | cut -d- -f1 | sort -u)"
MISSING_PREFIX=""
for prefix in $PREFIXES; do
  grep -qE "\`${prefix}(-[0-9]+)?\`" "${FRAMEWORK}/validation/traceability-matrix.md" || MISSING_PREFIX="${MISSING_PREFIX}${prefix} "
done
check "matriz de rastreabilidade cita todos os prefixos${MISSING_PREFIX:+ (faltam: ${MISSING_PREFIX})}" test -z "$MISSING_PREFIX"

# ---------------------------------------------------------------------------
echo "Score: núcleo, skill e modelo HTML"
# ---------------------------------------------------------------------------
CORE_WEIGHTS="$(sed -n 's/^- `\([a-z_]*\)`: \([0-9]*\)%$/\1=\2/p' "$SCORING" | sort)"
SKILL_WEIGHTS="$(sed -n 's/^| [^|]* | `\([a-z_]*\)` | \([0-9]*\)% |$/\1=\2/p' "$SKILL" | sort)"
TEMPLATE_WEIGHTS="$(LC_ALL=C awk '/var PESO_AREA = \{/ { on = 1 } on { print } on && /\};/ { exit }' "$TEMPLATE" \
  | grep -oE '[a-z_]+: [0-9]+' | sed 's/: /=/' | sort)"
WEIGHT_SUM="$(printf "%s\n" "$CORE_WEIGHTS" | cut -d= -f2 | awk '{ s += $1 } END { print s + 0 }')"
check "pesos das áreas somam 100 (soma: ${WEIGHT_SUM})" test "$WEIGHT_SUM" = "100"
same "pesos das áreas iguais na skill" "$CORE_WEIGHTS" "$SKILL_WEIGHTS"
same "pesos das áreas iguais no modelo HTML" "$CORE_WEIGHTS" "$TEMPLATE_WEIGHTS"

SKILL_DOMAIN_MAP="$(LC_ALL=C awk '/^\| `(BL|[0-9]+)` \|/ { split($0, c, /[ ]*\|[ ]*/); gsub(/`/, "", c[2]); gsub(/`/, "", c[4]); print c[2] "=" c[4] }' "$SKILL")"
same "mapa de domínios igual na skill" "$DOMAIN_MAP" "$SKILL_DOMAIN_MAP"
check "mapa cobre BL e os 17 domínios" test "$(printf "%s\n" "$DOMAIN_MAP" | wc -l | tr -d ' ')" = "18"
MAP_AREAS="$(printf "%s\n" "$DOMAIN_MAP" | cut -d= -f2 | sort -u)"
same "toda área de score tem domínio, e todo domínio aponta para uma área" "$(printf "%s\n" "$CORE_WEIGHTS" | cut -d= -f1)" "$MAP_AREAS"

for label in CRITICO BAIXO_NIVEL PARCIALMENTE_CONFORME ALTA_CONFORMIDADE EXCELENTE; do
  for file in "$SCORING" "$SKILL" "$TEMPLATE"; do
    grep -qF "$label" "$file" || fail "rótulo de classificação ${label} ausente em ${file#"${REPO_ROOT}"/}"
  done
done
ok "rótulos de classificação presentes no núcleo, na skill e no modelo"
check "teto de classificação igual no núcleo e na skill" grep -qF 'não passa de `PARCIALMENTE_CONFORME`' "$SCORING"
check "teto de classificação descrito na skill" grep -qF 'não passa de `PARCIALMENTE_CONFORME`' "$SKILL"
check "teto de classificação aplicado no modelo HTML" grep -qF "TETO = 'PARCIALMENTE_CONFORME'" "$TEMPLATE"

# ---------------------------------------------------------------------------
echo "Cenários e módulos"
# ---------------------------------------------------------------------------
normalize() { tr -d '`.;' | tr ',' '\n' | sed 's/^ *//; s/ *$//' | grep -v '^$' | sort | tr '\n' ' ' | sed 's/ $//'; }

ROUTER="${FRAMEWORK}/orchestrator/router.md"
MATRIX="${FRAMEWORK}/orchestrator/activation-matrix.md"
router_modules() {
  if [[ "$1" == "full_audit" ]]; then
    LC_ALL=C awk '/^## Auditoria completa/ { on = 1; next } on && /^`core`/ { print; exit }' "$ROUTER" | normalize
  else
    sed -n "s/^- \`$1\`: \(.*\)$/\1/p" "$ROUTER" | head -n 1 | normalize
  fi
}
SCENARIOS="$(sed -n 's/^Identificadores de cenário: \(.*\)\.$/\1/p' "$MATRIX" | tr -d '`' | tr ',' '\n' | sed 's/^ *//')"
check "matriz lista os identificadores de cenário" test -n "$SCENARIOS"

# Matriz: a ordem das linhas é a ordem dos identificadores listados logo abaixo dela.
LC_ALL=C awk '
  /^\| Cenário \|/ { n = split($0, h, /[ ]*\|[ ]*/); next }
  n && /^\|---/ { next }
  n && /^\|/ {
    split($0, c, /[ ]*\|[ ]*/); line = ""
    for (i = 3; i < n; i++) if (c[i] == "X") line = line h[i] " "
    print line
  }
' "$MATRIX" > "${TMP_DIR}/matrix-rows.txt"
check "matriz tem uma linha por cenário" test "$(wc -l < "${TMP_DIR}/matrix-rows.txt" | tr -d ' ')" = "$(printf "%s\n" "$SCENARIOS" | wc -l | tr -d ' ')"

ROW=0
for scenario in $SCENARIOS; do
  ROW=$((ROW + 1))
  expected="$(router_modules "$scenario")"
  matrix_modules="$(sed -n "${ROW}p" "${TMP_DIR}/matrix-rows.txt" | tr ' ' ',' | normalize)"
  same "${scenario}: router e matriz ativam os mesmos módulos" "$expected" "$matrix_modules"
  command_file="$(grep -lE "(Ative o cenário|Execute no modo) \`${scenario}\`" "${REPO_ROOT}"/commands/*.md || true)"
  if [[ -z "$command_file" ]]; then
    fail "${scenario}: nenhum comando em commands/ ativa o cenário"
    continue
  fi
  command_modules="$(LC_ALL=C awk -v id="$scenario" '$0 ~ "(Ative o cenário|Execute no modo) `" id "`" { on = 1; next } on && /^- `/ { sub(/^- /, ""); print; exit }' "$command_file" | normalize)"
  same "${scenario}: comando $(basename "$command_file") ativa os mesmos módulos" "$expected" "$command_modules"
  grep -qF "\`${scenario}\`" "${FRAMEWORK}/README.md" || fail "${scenario}: ausente do README do framework"
done

ALL_MODULES="$(sed -n 's/^| Cenário | \(.*\) |$/\1/p' "$MATRIX" | tr '|' ',' | normalize)"
same "full_audit ativa todos os módulos da matriz" "$ALL_MODULES" "$(router_modules full_audit)"

# ---------------------------------------------------------------------------
echo "Manifestos"
# ---------------------------------------------------------------------------
: > "${TMP_DIR}/manifest-files.txt"
for module in $(printf "%s\n" "$ALL_MODULES" | tr ' ' '\n'); do
  manifest="${FRAMEWORK}/orchestrator/manifests/${module}.manifest.md"
  if [[ ! -f "$manifest" ]]; then
    fail "manifesto ausente: ${module}"
    continue
  fi
  files="$(sed -n 's/^- `files`: \(.*\)$/\1/p' "$manifest" | tr -d '`' | tr ',' '\n' | sed 's/^ *//')"
  if [[ -z "$files" ]]; then
    fail "manifesto de ${module} sem o campo files"
    continue
  fi
  missing=""
  for file in $files; do
    [[ -f "${FRAMEWORK}/${file}" ]] || missing="${missing}${file} "
    printf "%s\n" "$file" >> "${TMP_DIR}/manifest-files.txt"
  done
  check "manifesto de ${module}: arquivos existem${missing:+ (faltam: ${missing})}" test -z "$missing"
done
LISTED="$(grep -v '^core/' "${TMP_DIR}/manifest-files.txt" | sort)"
ON_DISK="$(module_files | sed "s|^${FRAMEWORK}/||")"
same "todo arquivo de módulo está em exatamente um manifesto" "$ON_DISK" "$LISTED"

# ---------------------------------------------------------------------------
echo "Documentação"
# ---------------------------------------------------------------------------
BROKEN_LINKS=""
for name in $(grep -rhoE '\[\[[a-z0-9-]+\]\]' "$FRAMEWORK" --include='*.md' | tr -d '[]' | sort -u); do
  [[ "$(find "$FRAMEWORK" -name "${name}.md" -type f | wc -l | tr -d ' ')" == "1" ]] || BROKEN_LINKS="${BROKEN_LINKS}${name} "
done
check "referências [[arquivo]] apontam para um arquivo do framework${BROKEN_LINKS:+ (quebradas: ${BROKEN_LINKS})}" test -z "$BROKEN_LINKS"

SYNC_PT="$(sed -n 's/^| Última sincronização | `\([0-9-]*\)` |$/\1/p' "${REPO_ROOT}/README.md")"
SYNC_EN="$(sed -n 's/^| Last synchronization | `\([0-9-]*\)` |$/\1/p' "${REPO_ROOT}/README.en.md")"
check "data de sincronização presente no README.md (${SYNC_PT:-ausente})" test -n "$SYNC_PT"
check "data de sincronização igual nos dois READMEs (${SYNC_PT:-?} e ${SYNC_EN:-?})" test "$SYNC_PT" = "$SYNC_EN"

echo
if [[ "$FAILURES" -gt 0 ]]; then
  echo "${FAILURES} falha(s)."
  exit 1
fi
echo "Framework consistente."
