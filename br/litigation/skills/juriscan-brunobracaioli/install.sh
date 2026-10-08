#!/usr/bin/env bash
set -e

SKILL_NAME="juriscan"
SKILL_TARGET="$HOME/.claude/skills/$SKILL_NAME"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=== JuriScan — Installer ==="
echo ""

# 1. Check Python version
python3 -c "import sys; assert sys.version_info >= (3, 10), f'Python 3.10+ required, got {sys.version}'" 2>/dev/null || {
    echo "[ERROR] Python 3.10+ is required."
    exit 1
}
echo "[OK] Python $(python3 --version 2>&1 | cut -d' ' -f2)"

# 2. Install Python dependencies
echo ""
echo "Installing Python dependencies..."
pip install pypdf pytesseract Pillow jsonschema 2>/dev/null \
    || pip install --user pypdf pytesseract Pillow jsonschema 2>/dev/null \
    || { echo "[WARN] Could not install Python packages. Run: pip install -r $SCRIPT_DIR/requirements.txt"; }
echo "[OK] Python dependencies"

# 3. Check system dependencies
echo ""
HAS_ISSUES=0

if command -v pdftotext &>/dev/null; then
    echo "[OK] poppler-utils (pdftotext)"
else
    echo "[WARN] poppler-utils not found. Install with:"
    echo "       Ubuntu/Debian: sudo apt-get install poppler-utils"
    echo "       macOS: brew install poppler"
    HAS_ISSUES=1
fi

if command -v tesseract &>/dev/null; then
    echo "[OK] tesseract-ocr"
else
    echo "[WARN] tesseract-ocr not found (optional — needed for scanned PDFs). Install with:"
    echo "       Ubuntu/Debian: sudo apt-get install tesseract-ocr tesseract-ocr-por"
    echo "       macOS: brew install tesseract tesseract-lang"
    HAS_ISSUES=1
fi

# 4. Install as Claude Code skill
echo ""
if [ "$SCRIPT_DIR" = "$SKILL_TARGET" ]; then
    echo "[OK] Already installed at $SKILL_TARGET"
else
    mkdir -p "$HOME/.claude/skills"
    if [ -e "$SKILL_TARGET" ]; then
        echo "[INFO] Removing previous installation at $SKILL_TARGET"
        rm -rf "$SKILL_TARGET"
    fi
    ln -sf "$SCRIPT_DIR" "$SKILL_TARGET"
    echo "[OK] Installed as symlink: $SKILL_TARGET -> $SCRIPT_DIR"
fi

# 4b. Expose juriscan subagents to Claude Code
#     Subagents live inside the repo at .claude/agents/ so they're versioned
#     alongside the code, but Claude Code discovers agents at ~/.claude/agents/.
#     We symlink each juriscan-*.md file there.
AGENTS_SRC="$SCRIPT_DIR/.claude/agents"
AGENTS_DST="$HOME/.claude/agents"
if [ -d "$AGENTS_SRC" ]; then
    mkdir -p "$AGENTS_DST"
    agent_count=0
    for agent_file in "$AGENTS_SRC"/juriscan-*.md; do
        [ -e "$agent_file" ] || continue
        agent_name="$(basename "$agent_file")"
        ln -sf "$agent_file" "$AGENTS_DST/$agent_name"
        agent_count=$((agent_count + 1))
    done
    if [ $agent_count -gt 0 ]; then
        echo "[OK] Linked $agent_count juriscan subagent(s) into $AGENTS_DST"
    fi
fi

# 5. Summary
echo ""
echo "=== Installation Complete ==="
echo ""
echo "The skill is now available in Claude Code — globally, in any project."
echo ""
echo "NEXT STEP — do NOT run 'claude' from this directory."
echo "  1. cd into the folder that contains your PDF (e.g. cd /mnt/c/meus-processos)"
echo "  2. claude"
echo "  3. /juriscan processo.pdf"
echo ""
echo "Trigger phrases: análise de processo, contradições, prazos, timeline jurídica."
echo ""
if [ $HAS_ISSUES -eq 1 ]; then
    echo "[!] Some optional system dependencies are missing — see warnings above."
fi
