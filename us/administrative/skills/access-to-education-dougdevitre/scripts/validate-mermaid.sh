#!/usr/bin/env bash
# =============================================================================
# validate-mermaid.sh -- Find and validate ```mermaid blocks in markdown files.
#
# Checks for:
#   1. Count of mermaid blocks per file
#   2. Unmatched brackets: ( ) [ ] { }
#   3. Missing arrows in flowchart/graph lines (lines with nodes but no -->)
#   4. Empty mermaid blocks
#
# Usage:  ./scripts/validate-mermaid.sh
#
# Dependencies: bash, standard POSIX utilities (grep, sed, awk, find)
# =============================================================================

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# ---------------------------------------------------------------------------
# Color helpers
# ---------------------------------------------------------------------------
if [[ -t 1 ]]; then
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    YELLOW='\033[0;33m'
    BOLD='\033[1m'
    RESET='\033[0m'
else
    RED='' GREEN='' YELLOW='' BOLD='' RESET=''
fi

# ---------------------------------------------------------------------------
# Counters
# ---------------------------------------------------------------------------
TOTAL_BLOCKS=0
TOTAL_FILES_WITH_MERMAID=0
TOTAL_ISSUES=0

# Temp directory for extracted blocks
TMPDIR="$(mktemp -d)"
trap 'rm -rf "$TMPDIR"' EXIT

echo -e "${BOLD}Mermaid Block Validator -- scanning ${REPO_ROOT}${RESET}"
echo "======================================================"

# ---------------------------------------------------------------------------
# Find all markdown files that contain mermaid blocks
# ---------------------------------------------------------------------------
mapfile -t MD_FILES < <(find "$REPO_ROOT" -name '*.md' -not -path '*/.git/*' | sort)

for md_file in "${MD_FILES[@]}"; do
    rel_file="${md_file#"$REPO_ROOT"/}"

    # Count mermaid fences in this file
    block_count="$(grep -c '^ *```mermaid' "$md_file" 2>/dev/null || true)"
    block_count="${block_count//[^0-9]/}"    # strip any non-digit chars
    block_count="${block_count:-0}"
    if [[ "$block_count" -eq 0 ]]; then
        continue
    fi

    TOTAL_FILES_WITH_MERMAID=$((TOTAL_FILES_WITH_MERMAID + 1))
    echo -e "${BOLD}${rel_file}${RESET}  --  ${block_count} mermaid block(s)"

    # ------------------------------------------------------------------
    # Extract each mermaid block to a temporary file
    # We use awk to pull content between ```mermaid and the next ```
    # ------------------------------------------------------------------
    block_idx=0
    in_block=false
    block_file=""

    while IFS= read -r line; do
        if [[ "$in_block" == false ]]; then
            if [[ "$line" =~ ^[[:space:]]*\`\`\`mermaid ]]; then
                in_block=true
                block_idx=$((block_idx + 1))
                TOTAL_BLOCKS=$((TOTAL_BLOCKS + 1))
                block_file="${TMPDIR}/block_${TOTAL_BLOCKS}.mmd"
                : > "$block_file"   # create/truncate
            fi
        else
            if [[ "$line" =~ ^[[:space:]]*\`\`\` ]]; then
                in_block=false

                # --- Validate the extracted block ---

                # Check 1: empty block
                if [[ ! -s "$block_file" ]]; then
                    echo -e "  ${RED}[ISSUE]${RESET} Block #${block_idx}: empty mermaid block"
                    TOTAL_ISSUES=$((TOTAL_ISSUES + 1))
                    continue
                fi

                # Check 2: unmatched brackets
                for pair in '( )' '[ ]' '{ }'; do
                    open_char="${pair%% *}"
                    close_char="${pair##* }"

                    open_count="$(tr -cd "$open_char" < "$block_file" | wc -c)"
                    close_count="$(tr -cd "$close_char" < "$block_file" | wc -c)"

                    if [[ "$open_count" -ne "$close_count" ]]; then
                        echo -e "  ${YELLOW}[WARN]${RESET}  Block #${block_idx}: unmatched '${open_char}${close_char}' -- open=${open_count} close=${close_count}"
                        TOTAL_ISSUES=$((TOTAL_ISSUES + 1))
                    fi
                done

                # Check 3: flowchart/graph lines that look like node
                # definitions but lack any arrow (-->, ---, -.->)
                # Only applies when the diagram type is graph or flowchart
                first_line="$(head -1 "$block_file" | sed 's/^[[:space:]]*//')"
                if [[ "$first_line" =~ ^(graph|flowchart) ]]; then
                    line_num=0
                    while IFS= read -r diagram_line; do
                        line_num=$((line_num + 1))
                        # Skip the directive line, comments, empty lines, and
                        # style/class/subgraph/end keywords
                        stripped="$(echo "$diagram_line" | sed 's/^[[:space:]]*//')"
                        if [[ "$line_num" -eq 1 ]] \
                            || [[ -z "$stripped" ]] \
                            || [[ "$stripped" =~ ^%% ]] \
                            || [[ "$stripped" =~ ^(style|class|classDef|subgraph|end|click|linkStyle) ]]; then
                            continue
                        fi
                        # If a line has node-like content (e.g., A[text]) but
                        # no arrow operator, flag it
                        if [[ "$stripped" =~ [\[\(\{] ]] \
                            && ! [[ "$stripped" =~ (-->|---|\-\.\->|==>|--\||\|) ]]; then
                            echo -e "  ${YELLOW}[WARN]${RESET}  Block #${block_idx}, line ${line_num}: possible missing arrow: ${stripped:0:60}"
                            TOTAL_ISSUES=$((TOTAL_ISSUES + 1))
                        fi
                    done < "$block_file"
                fi
            else
                # Inside a block -- write line to temp file
                echo "$line" >> "$block_file"
            fi
        fi
    done < "$md_file"

    # If we ended while still inside a block, the closing ``` is missing
    if [[ "$in_block" == true ]]; then
        echo -e "  ${RED}[ISSUE]${RESET} Block #${block_idx}: missing closing \`\`\` fence"
        TOTAL_ISSUES=$((TOTAL_ISSUES + 1))
    fi
done

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
echo ""
echo "======================================================"
echo -e "${BOLD}Summary${RESET}"
echo "======================================================"
echo "  Files with mermaid blocks:  $TOTAL_FILES_WITH_MERMAID"
echo "  Total mermaid blocks:       $TOTAL_BLOCKS"
echo "  Issues found:               $TOTAL_ISSUES"

if [[ "$TOTAL_ISSUES" -gt 0 ]]; then
    echo ""
    echo -e "${YELLOW}Found $TOTAL_ISSUES potential issue(s). Review warnings above.${RESET}"
    exit 1
else
    echo ""
    echo -e "${GREEN}No issues detected.${RESET}"
    exit 0
fi
