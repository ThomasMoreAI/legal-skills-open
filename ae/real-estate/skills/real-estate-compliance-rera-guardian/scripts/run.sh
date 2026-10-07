#!/usr/bin/env bash
# Run the Compliance & RERA Guardian agent with a task.
# Usage: ./run.sh "Your task here"
#   or:  echo "Your task" | ./run.sh --stdin
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
REPO_ROOT="$(cd "$SKILL_DIR/../.." && pwd)"

if [[ "${1:-}" == "--stdin" ]]; then
  exec python3 "$REPO_ROOT/scripts/run-skill.py" --skill-file "$SKILL_DIR/SKILL.md" --stdin
elif [[ -n "${1:-}" ]]; then
  exec python3 "$REPO_ROOT/scripts/run-skill.py" --skill-file "$SKILL_DIR/SKILL.md" --task "$*"
else
  echo "Usage: $0 \"Your task here\""
  echo "   or: echo \"task\" | $0 --stdin"
  exit 1
fi
