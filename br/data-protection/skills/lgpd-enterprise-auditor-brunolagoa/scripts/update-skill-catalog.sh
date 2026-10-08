#!/usr/bin/env bash
# Regera, na skill (SKILL.md), o catálogo de itens do checklist e a lista de dependências a partir dos módulos
# do framework. Os módulos são a fonte; o bloco entre os marcadores da skill nunca é editado à mão.
# Uso: scripts/update-skill-catalog.sh [--check]
#   --check  não grava: sai com 1 se a skill estiver desatualizada em relação aos módulos.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
FRAMEWORK="${REPO_ROOT}/.agents/lgpd-enterprise-auditor"
SKILL="${REPO_ROOT}/SKILL.md"
START='<!-- CATALOGO:INICIO (gerado por scripts/update-skill-catalog.sh a partir dos módulos do framework; não editar à mão) -->'
END='<!-- CATALOGO:FIM -->'
CHECK=0
[[ "${1:-}" == "--check" ]] && CHECK=1

# A ordem dos arquivos define a ordem dos itens dentro de cada domínio.
MODULE_FILES=(
  legal/legal-bases-engine.md
  legal/rights-of-data-subject.md
  legal/children-adolescents.md
  legal/international-transfer.md
  governance/dpo-framework.md
  cloud/cloud-audit.md
  appsec/owasp-api.md
  mobile/mobile-storage.md
  devsecops/ci-cd-security.md
  ai-llm/llm-audit.md
  legal/eca-digital.md
  legal/plataformas-digitais.md
)

[[ -f "$SKILL" ]] || { echo "Skill não encontrada: ${SKILL}"; exit 1; }
for marker in "$START" "$END"; do
  [[ "$(grep -cxF -- "$marker" "$SKILL" || true)" == "1" ]] \
    || { echo "Marcador ausente ou repetido em SKILL.md: ${marker}"; exit 1; }
done

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

sources=("${FRAMEWORK}/core/scoring-engine.md")
for file in "${MODULE_FILES[@]}"; do
  [[ -f "${FRAMEWORK}/${file}" ]] || { echo "Módulo não encontrado: ${file}"; exit 1; }
  sources+=("${FRAMEWORK}/${file}")
done

# Primeiro arquivo: mapa de domínios (código, nome, área). Demais: linhas de item do catálogo,
# agrupadas pelo domínio (coluna 3) e impressas sem essa coluna, que vira o título do grupo.
LC_ALL=C awk '
  FNR == 1 { file++ }
  file == 1 {
    if ($0 ~ /^\| `(BL|[0-9]+)` \|/) {
      split($0, c, /[ ]*\|[ ]*/)
      code = c[2]; gsub(/`/, "", code)
      order[++total] = code; name[code] = c[3]; area[code] = c[4]
    }
    next
  }
  /^\| `[A-Z][A-Z]+-[0-9]+` \|/ {
    split($0, c, /[ ]*\|[ ]*/)
    if (!(c[4] in name)) { printf "Domínio desconhecido em %s: %s\n", c[2], c[4] > "/dev/stderr"; bad = 1 }
    rows[c[4]] = rows[c[4]] "| " c[2] " | " c[3] " | " c[5] " | " c[6] " | " c[7] " | " c[8] " |\n"
  }
  # Dependências entre itens, para a contagem única: "- `GV-05` depende de `GV-02`: motivo".
  /^- `[A-Z][A-Z]+-[0-9]+` depende de `[A-Z][A-Z]+-[0-9]+`/ { deps = deps $0 "\n" }
  END {
    if (bad) exit 1
    for (i = 1; i <= total; i++) {
      code = order[i]
      if (rows[code] == "") continue
      printf "## %s. %s — área %s\n\n", code, name[code], area[code]
      print "| ID | Item | Criticidade | Agravante ou atenuante | Controle | Fundamento |"
      print "|---|---|---|---|---|---|"
      printf "%s\n", rows[code]
    }
    if (deps != "") {
      print "## Dependências entre itens\n"
      print "Com o segundo item `NAO_CONFORME`, o primeiro fica `NAO_APLICAVEL`. A lista é fechada: fora dela, cada item é avaliado pelo próprio requisito.\n"
      printf "%s\n", deps
    }
  }
' "${sources[@]}" > "${TMP_DIR}/catalog.md"

[[ -s "${TMP_DIR}/catalog.md" ]] || { echo "Nenhum item de catálogo encontrado nos módulos."; exit 1; }

LC_ALL=C awk -v start="$START" -v end="$END" -v catalog="${TMP_DIR}/catalog.md" '
  $0 == start { print; print ""; while ((getline line < catalog) > 0) print line; skip = 1; next }
  $0 == end { skip = 0 }
  !skip { print }
' "$SKILL" > "${TMP_DIR}/SKILL.md"

if cmp -s "${TMP_DIR}/SKILL.md" "$SKILL"; then
  echo "Catálogo da skill em dia com os módulos."
  exit 0
fi

if [[ "$CHECK" -eq 1 ]]; then
  echo "Catálogo da skill desatualizado em relação aos módulos (rode scripts/update-skill-catalog.sh)."
  exit 1
fi

cat "${TMP_DIR}/SKILL.md" > "$SKILL"
echo "Catálogo da skill atualizado a partir dos módulos."
