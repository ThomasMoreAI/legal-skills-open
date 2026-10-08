#!/usr/bin/env bash
# =============================================================================
# check-links.sh -- Validate internal cross-references and external URLs
#                   in all markdown files within the repository.
#
# Usage:  ./scripts/check-links.sh [--skip-external]
#
# Dependencies: bash, curl, standard POSIX utilities (grep, sed, awk, find)
# =============================================================================

set -euo pipefail

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CURL_TIMEOUT=10          # seconds per external URL check
SKIP_EXTERNAL=false

if [[ "${1:-}" == "--skip-external" ]]; then
    SKIP_EXTERNAL=true
fi

# ---------------------------------------------------------------------------
# Counters
# ---------------------------------------------------------------------------
TOTAL_INTERNAL=0
TOTAL_EXTERNAL=0
BROKEN_INTERNAL=0
BROKEN_EXTERNAL=0

# Associative arrays to avoid re-checking the same URL twice
declare -A CHECKED_EXTERNAL   # url -> "ok" | "broken"

# ---------------------------------------------------------------------------
# Color helpers (disabled when stdout is not a terminal)
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
# Utility: normalise a relative path against a base directory
# ---------------------------------------------------------------------------
resolve_path() {
    local base_dir="$1"   # directory of the file that contains the link
    local target="$2"     # the relative (or absolute-from-repo) path

    # Strip any anchor or query string for file-existence check
    local file_part="${target%%#*}"
    file_part="${file_part%%\?*}"

    # Handle paths starting with / as repo-relative
    if [[ "$file_part" == /* ]]; then
        echo "${REPO_ROOT}${file_part}"
    else
        # Resolve ../ and ./ via cd + pwd
        local resolved
        resolved="$(cd "$base_dir" && cd "$(dirname "$file_part")" 2>/dev/null && pwd)/$(basename "$file_part")"
        echo "$resolved"
    fi
}

# ---------------------------------------------------------------------------
# Utility: check whether a heading anchor exists in a markdown file
# ---------------------------------------------------------------------------
anchor_exists() {
    local file="$1"
    local anchor="$2"   # e.g. #some-heading

    # Remove leading #
    anchor="${anchor#\#}"
    [[ -z "$anchor" ]] && return 0   # bare "#" means top of file -- always valid

    # Convert markdown headings to their GitHub-style anchor slugs:
    #   - lowercase, strip non-alphanumeric except hyphens and spaces,
    #     replace spaces with hyphens, collapse consecutive hyphens
    while IFS= read -r heading; do
        # Strip leading # marks and whitespace
        heading="$(echo "$heading" | sed 's/^#\+[[:space:]]*//')"
        # Build slug: lowercase, keep alnum / spaces / hyphens, spaces->hyphens
        local slug
        slug="$(echo "$heading" | tr '[:upper:]' '[:lower:]' \
            | sed 's/[^a-z0-9 _-]//g' \
            | sed 's/ /-/g' \
            | sed 's/--\+/-/g' \
            | sed 's/^-//;s/-$//')"
        if [[ "$slug" == "$anchor" ]]; then
            return 0
        fi
    done < <(grep -E '^#{1,6} ' "$file" 2>/dev/null || true)

    return 1
}

# ---------------------------------------------------------------------------
# Utility: check a single external URL
# ---------------------------------------------------------------------------
check_external_url() {
    local url="$1"

    # Return cached result if we already checked this URL
    if [[ -n "${CHECKED_EXTERNAL[$url]+x}" ]]; then
        [[ "${CHECKED_EXTERNAL[$url]}" == "ok" ]] && return 0 || return 1
    fi

    # Use curl with a HEAD request first; fall back to GET on 405
    local http_code
    http_code="$(curl -o /dev/null -s -w '%{http_code}' \
        --max-time "$CURL_TIMEOUT" \
        -L -I "$url" 2>/dev/null || echo "000")"

    if [[ "$http_code" == "405" ]]; then
        http_code="$(curl -o /dev/null -s -w '%{http_code}' \
            --max-time "$CURL_TIMEOUT" \
            -L "$url" 2>/dev/null || echo "000")"
    fi

    if [[ "$http_code" =~ ^[23] ]]; then
        CHECKED_EXTERNAL["$url"]="ok"
        return 0
    else
        CHECKED_EXTERNAL["$url"]="broken"
        return 1
    fi
}

# ---------------------------------------------------------------------------
# Main: iterate over every markdown file
# ---------------------------------------------------------------------------
echo -e "${BOLD}Link Checker -- scanning ${REPO_ROOT}${RESET}"
echo "======================================================"

# Collect all markdown files
mapfile -t MD_FILES < <(find "$REPO_ROOT" -name '*.md' -not -path '*/.git/*' | sort)

echo "Found ${#MD_FILES[@]} markdown files."
echo ""

for md_file in "${MD_FILES[@]}"; do
    rel_file="${md_file#"$REPO_ROOT"/}"
    file_dir="$(dirname "$md_file")"

    # ------------------------------------------------------------------
    # Extract inline links:  [text](url)
    # Also handles [text](url "title") by stripping the title part.
    # ------------------------------------------------------------------
    while IFS= read -r link_match; do
        # link_match is the raw URL between ( and )
        # Strip optional title in quotes
        local_url="$(echo "$link_match" | sed 's/[[:space:]]*"[^"]*"[[:space:]]*$//' | sed 's/[[:space:]]*$//')"

        # Skip empty, mailto:, tel:, javascript:, data: links
        if [[ -z "$local_url" ]] || [[ "$local_url" =~ ^(mailto:|tel:|javascript:|data:|#$) ]]; then
            continue
        fi

        # Classify: external vs internal
        if [[ "$local_url" =~ ^https?:// ]]; then
            # --- External link ---
            TOTAL_EXTERNAL=$((TOTAL_EXTERNAL + 1))
            if [[ "$SKIP_EXTERNAL" == true ]]; then
                continue
            fi
            if ! check_external_url "$local_url"; then
                BROKEN_EXTERNAL=$((BROKEN_EXTERNAL + 1))
                echo -e "${RED}BROKEN (external)${RESET}  ${rel_file}  ->  ${local_url}"
            fi
        else
            # --- Internal link ---
            TOTAL_INTERNAL=$((TOTAL_INTERNAL + 1))

            # Separate file path and anchor
            anchor=""
            if [[ "$local_url" == *"#"* ]]; then
                anchor="#${local_url#*#}"
                file_path_part="${local_url%%#*}"
            else
                file_path_part="$local_url"
            fi

            # A pure anchor link (#foo) references the current file
            if [[ -z "$file_path_part" ]]; then
                if [[ -n "$anchor" ]] && ! anchor_exists "$md_file" "$anchor"; then
                    BROKEN_INTERNAL=$((BROKEN_INTERNAL + 1))
                    echo -e "${RED}BROKEN (anchor)${RESET}    ${rel_file}  ->  ${local_url}"
                fi
                continue
            fi

            resolved="$(resolve_path "$file_dir" "$file_path_part")"

            if [[ ! -e "$resolved" ]]; then
                BROKEN_INTERNAL=$((BROKEN_INTERNAL + 1))
                echo -e "${RED}BROKEN (not found)${RESET} ${rel_file}  ->  ${local_url}"
            elif [[ -n "$anchor" ]] && [[ -f "$resolved" ]]; then
                if ! anchor_exists "$resolved" "$anchor"; then
                    BROKEN_INTERNAL=$((BROKEN_INTERNAL + 1))
                    echo -e "${RED}BROKEN (anchor)${RESET}    ${rel_file}  ->  ${local_url}"
                fi
            fi
        fi
    done < <(grep -oP '\[[^\]]*\]\(\K[^)]+' "$md_file" 2>/dev/null || true)

    # ------------------------------------------------------------------
    # Extract reference-style links:  [label]: url
    # ------------------------------------------------------------------
    while IFS= read -r ref_url; do
        # Strip optional title
        ref_url="$(echo "$ref_url" | sed 's/[[:space:]]*"[^"]*"[[:space:]]*$//' | sed 's/[[:space:]]*$//')"

        if [[ -z "$ref_url" ]] || [[ "$ref_url" =~ ^(mailto:|tel:|javascript:|data:) ]]; then
            continue
        fi

        if [[ "$ref_url" =~ ^https?:// ]]; then
            TOTAL_EXTERNAL=$((TOTAL_EXTERNAL + 1))
            if [[ "$SKIP_EXTERNAL" == true ]]; then
                continue
            fi
            if ! check_external_url "$ref_url"; then
                BROKEN_EXTERNAL=$((BROKEN_EXTERNAL + 1))
                echo -e "${RED}BROKEN (external)${RESET}  ${rel_file}  ->  ${ref_url}"
            fi
        else
            TOTAL_INTERNAL=$((TOTAL_INTERNAL + 1))
            anchor=""
            if [[ "$ref_url" == *"#"* ]]; then
                anchor="#${ref_url#*#}"
                file_path_part="${ref_url%%#*}"
            else
                file_path_part="$ref_url"
            fi

            if [[ -z "$file_path_part" ]]; then
                if [[ -n "$anchor" ]] && ! anchor_exists "$md_file" "$anchor"; then
                    BROKEN_INTERNAL=$((BROKEN_INTERNAL + 1))
                    echo -e "${RED}BROKEN (anchor)${RESET}    ${rel_file}  ->  ${ref_url}"
                fi
                continue
            fi

            resolved="$(resolve_path "$file_dir" "$file_path_part")"

            if [[ ! -e "$resolved" ]]; then
                BROKEN_INTERNAL=$((BROKEN_INTERNAL + 1))
                echo -e "${RED}BROKEN (not found)${RESET} ${rel_file}  ->  ${ref_url}"
            elif [[ -n "$anchor" ]] && [[ -f "$resolved" ]]; then
                if ! anchor_exists "$resolved" "$anchor"; then
                    BROKEN_INTERNAL=$((BROKEN_INTERNAL + 1))
                    echo -e "${RED}BROKEN (anchor)${RESET}    ${rel_file}  ->  ${ref_url}"
                fi
            fi
        fi
    done < <(grep -oP '^\[[^\]]+\]:\s+\K\S+' "$md_file" 2>/dev/null || true)

done

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
echo ""
echo "======================================================"
echo -e "${BOLD}Summary${RESET}"
echo "======================================================"
TOTAL=$((TOTAL_INTERNAL + TOTAL_EXTERNAL))
echo "  Total links checked:     $TOTAL"
echo "  Internal links:          $TOTAL_INTERNAL  (broken: $BROKEN_INTERNAL)"
echo "  External links:          $TOTAL_EXTERNAL  (broken: $BROKEN_EXTERNAL)"
if [[ "$SKIP_EXTERNAL" == true ]]; then
    echo -e "  ${YELLOW}(external link checks were skipped)${RESET}"
fi

TOTAL_BROKEN=$((BROKEN_INTERNAL + BROKEN_EXTERNAL))
if [[ "$TOTAL_BROKEN" -gt 0 ]]; then
    echo ""
    echo -e "${RED}Found $TOTAL_BROKEN broken link(s).${RESET}"
    exit 1
else
    echo ""
    echo -e "${GREEN}All links are valid.${RESET}"
    exit 0
fi
