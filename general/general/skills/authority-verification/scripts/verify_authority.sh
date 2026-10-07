#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "usage: $0 '531 U.S. 98' [highlight query]" >&2
  exit 1
fi

if [[ -z "${CASEDEV_API_KEY:-}" ]]; then
  echo "CASEDEV_API_KEY is required" >&2
  exit 1
fi

if ! command -v casedev >/dev/null 2>&1; then
  echo "casedev CLI is required; install with 'brew tap CaseMark/casedev && brew install casedev'" >&2
  exit 1
fi

CITATION="$1"
HIGHLIGHT_QUERY="${2:-holding}"
VERIFY_JSON="$(mktemp)"

cleanup() {
  rm -f "$VERIFY_JSON"
}

trap cleanup EXIT

echo "== verify =="
casedev legal:v1 verify --text "$CITATION" --json | tee "$VERIFY_JSON"

if ! command -v jq >/dev/null 2>&1; then
  echo "jq is required for the follow-on CLI steps; install with 'brew install jq'" >&2
  exit 1
fi

VERIFIED_URL="$(jq -r '.citations[] | select(.status == "verified") | .case.url' "$VERIFY_JSON" | head -n 1)"

if [[ -z "$VERIFIED_URL" ]]; then
  echo "No verified authority URL returned; stop and review the verification output." >&2
  exit 1
fi

echo
echo "== if verified, retrieve full text =="
casedev legal:v1 get-full-text \
  --url "$VERIFIED_URL" \
  --highlight-query "$HIGHLIGHT_QUERY" \
  --max-characters 12000 \
  --json

echo
echo "== find related authorities =="
casedev legal:v1 similar \
  --url "$VERIFIED_URL" \
  --num-results 5 \
  --json
