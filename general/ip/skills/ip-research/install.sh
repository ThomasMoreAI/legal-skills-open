#!/bin/bash
# ip_research skill: quick-install helper for standalone dev symlink setup.
#
# Most users should NOT run this directly. Instead:
#
#   - Claude Code users (recommended):
#       claude plugin add github:parkerhancock/ip_tools
#
#   - Dev symlink into ~/.claude/skills/:
#       pip install 'patent-client-agents[mcp]'
#       patent-client-agents-skill-install
#
#   - Python library only:
#       pip install patent-client-agents
#       # or
#       uv add patent-client-agents
#
# This script stays in the wheel as a convenience for editable-install
# workflows where somebody has the patent-client-agents repo cloned locally and
# wants to make `import patent_client_agents` work without setting up a venv first.

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$SCRIPT_DIR"
while [[ "$REPO_ROOT" != "/" && ! -f "$REPO_ROOT/pyproject.toml" ]]; do
    REPO_ROOT="$(dirname "$REPO_ROOT")"
done

# Fast path: already importable.
if python3 -c "import patent_client_agents" 2>/dev/null; then
    exit 0
fi

# Prefer uv — it's faster, resolves deps cleanly, doesn't need a venv.
if command -v uv >/dev/null 2>&1; then
    if [[ -f "$REPO_ROOT/pyproject.toml" ]]; then
        # Dev repo: editable install into uv's project venv.
        (cd "$REPO_ROOT" && uv sync --quiet) || {
            echo "uv sync failed in $REPO_ROOT" >&2
            exit 1
        }
    else
        uv pip install --quiet 'patent-client-agents @ git+https://github.com/parkerhancock/ip_tools.git' || {
            echo "uv pip install from GitHub failed" >&2
            exit 1
        }
    fi
else
    # Fallback to pip if uv is absent.
    if [[ -f "$REPO_ROOT/pyproject.toml" ]]; then
        pip install --quiet --user -e "$REPO_ROOT"
    else
        pip install --quiet --user git+https://github.com/parkerhancock/ip_tools.git
    fi
fi

# Verify.
python3 -c "import patent_client_agents" || {
    echo "Error: patent_client_agents is still not importable after install." >&2
    echo "See https://github.com/parkerhancock/ip_tools/blob/main/docs/installation.md" >&2
    exit 1
}
