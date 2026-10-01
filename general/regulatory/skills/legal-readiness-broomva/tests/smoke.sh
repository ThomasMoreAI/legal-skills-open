#!/usr/bin/env bash
set -euo pipefail

skill_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
scratch="$(mktemp -d)"
trap 'rm -rf "$scratch"' EXIT

python3 "$skill_dir/scripts/legal_readiness.py" init "$scratch/legal-readiness.json"

set +e
python3 "$skill_dir/scripts/legal_readiness.py" check "$scratch/legal-readiness.json" >/dev/null
template_rc=$?
set -e
if [[ "$template_rc" -ne 1 ]]; then
  echo "expected untouched template to exit 1, got $template_rc" >&2
  exit 1
fi

python3 - "$scratch/legal-readiness.json" "$scratch/completed.json" "$scratch/invalid.json" <<'PY'
import json
import sys
from pathlib import Path

data = json.loads(Path(sys.argv[1]).read_text())
data["project"] = {
    "name": "Mothlight Notes",
    "repository": "https://github.com/mothlight/notes",
    "base_url": "https://mothlight.test",
    "template": False,
}
Path(sys.argv[2]).write_text(json.dumps(data))
data["completion_statement"] = "All identified gaps are fixed."
Path(sys.argv[3]).write_text(json.dumps(data))
PY

python3 "$skill_dir/scripts/legal_readiness.py" check "$scratch/completed.json"

set +e
python3 "$skill_dir/scripts/legal_readiness.py" check "$scratch/invalid.json" >/dev/null
rc=$?
set -e
if [[ "$rc" -ne 1 ]]; then
  echo "expected invalid closure statement to exit 1, got $rc" >&2
  exit 1
fi

echo "legal-readiness smoke passed"
