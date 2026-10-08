#!/usr/bin/env bash
# Garante uma única versão do projeto: metadata.version do SKILL.md = de todos os commands/*.md,
# presente no CHANGELOG.md e, quando informada, igual à tag (ex.: v1.1.0).
# Uso: scripts/tests/test-versions.sh [tag]

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd -P)"
TAG="${1:-}"
FAILURES=0

frontmatter_version() {
  awk '
    NR == 1 && $0 == "---" { in_fm = 1; next }
    in_fm && $0 == "---" { exit }
    in_fm && $0 ~ /^[[:space:]]+version:/ { sub(/^[[:space:]]+version:[[:space:]]*/, ""); gsub(/"/, ""); print; exit }
  ' "$1"
}

fail() {
  printf "  FAIL %s\n" "$1"
  FAILURES=$((FAILURES + 1))
}

VERSION="$(frontmatter_version "${REPO_ROOT}/SKILL.md")"
if [[ ! "$VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "SKILL.md sem metadata.version válida (encontrado: '${VERSION}')."
  exit 1
fi
echo "Versão do projeto (SKILL.md): ${VERSION}"

for file in "${REPO_ROOT}"/commands/*.md; do
  command_version="$(frontmatter_version "$file")"
  if [[ "$command_version" == "$VERSION" ]]; then
    printf "  ok   %s\n" "commands/$(basename "$file")"
  else
    fail "commands/$(basename "$file") está em '${command_version}'"
  fi
done

if grep -q "^## \[${VERSION}\]" "${REPO_ROOT}/CHANGELOG.md"; then
  printf "  ok   CHANGELOG.md tem a seção [%s]\n" "$VERSION"
else
  fail "CHANGELOG.md não tem a seção ## [${VERSION}]"
fi

if [[ -n "$TAG" ]]; then
  if [[ "$TAG" == "v${VERSION}" ]]; then
    printf "  ok   tag %s\n" "$TAG"
  else
    fail "a tag ${TAG} não corresponde à versão v${VERSION}"
  fi
fi

if [[ "$FAILURES" -gt 0 ]]; then
  echo "${FAILURES} inconsistência(s) de versão."
  exit 1
fi
echo "Versões consistentes."
