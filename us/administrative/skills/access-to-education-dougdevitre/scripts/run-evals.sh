#!/usr/bin/env bash
#
# run-evals.sh — Run Access to Education eval test cases against the Claude API
#
# Usage:
#   export ANTHROPIC_API_KEY="your-key-here"
#   ./scripts/run-evals.sh                    # Run all 30 test cases
#   ./scripts/run-evals.sh S01 P01 T01        # Run specific test cases by ID
#   ./scripts/run-evals.sh --dry-run          # Show prompts without calling API
#
# Requirements:
#   - curl
#   - jq
#   - ANTHROPIC_API_KEY environment variable (unless --dry-run)
#
# Output:
#   Results are printed to stdout and saved to evals/results-YYYY-MM-DD.json

set -euo pipefail

EVALS_FILE="evals/test-cases.json"
SKILL_FILE="SKILL.md"
MODEL="${CLAUDE_MODEL:-claude-sonnet-4-6}"
DRY_RUN=false
IDS=()

# Parse arguments
for arg in "$@"; do
  if [ "$arg" = "--dry-run" ]; then
    DRY_RUN=true
  elif [ "$arg" = "--help" ] || [ "$arg" = "-h" ]; then
    head -15 "$0" | tail -13
    exit 0
  else
    IDS+=("$arg")
  fi
done

# Validate prerequisites
if [ ! -f "$EVALS_FILE" ]; then
  echo "Error: $EVALS_FILE not found. Run from the repo root." >&2
  exit 1
fi

if [ "$DRY_RUN" = false ] && [ -z "${ANTHROPIC_API_KEY:-}" ]; then
  echo "Error: ANTHROPIC_API_KEY is not set." >&2
  echo "  export ANTHROPIC_API_KEY=\"your-key-here\"" >&2
  exit 1
fi

# Load system prompt
if [ ! -f "$SKILL_FILE" ]; then
  echo "Error: $SKILL_FILE not found. Run from the repo root." >&2
  exit 1
fi

SYSTEM_PROMPT=$(cat "$SKILL_FILE")
TOTAL=$(jq 'length' "$EVALS_FILE")
DATE=$(date +%Y-%m-%d)
RESULTS_FILE="evals/results-${DATE}.json"

echo "Access to Education — Eval Runner"
echo "================================="
echo "Model:      $MODEL"
echo "Test cases: $EVALS_FILE ($TOTAL total)"
echo "Date:       $DATE"
echo ""

# Build test case list
if [ ${#IDS[@]} -gt 0 ]; then
  FILTER=$(printf '"%s",' "${IDS[@]}")
  FILTER="[${FILTER%,}]"
  TEST_CASES=$(jq --argjson ids "$FILTER" '[.[] | select(.id as $id | $ids | index($id))]' "$EVALS_FILE")
  COUNT=$(echo "$TEST_CASES" | jq 'length')
  echo "Running $COUNT of $TOTAL test cases: ${IDS[*]}"
else
  TEST_CASES=$(cat "$EVALS_FILE")
  COUNT=$TOTAL
  echo "Running all $COUNT test cases"
fi
echo ""

# Initialize results array
RESULTS="[]"
PASS=0
FAIL=0
SKIP=0

for i in $(seq 0 $((COUNT - 1))); do
  CASE=$(echo "$TEST_CASES" | jq ".[$i]")
  ID=$(echo "$CASE" | jq -r '.id')
  PROMPT=$(echo "$CASE" | jq -r '.prompt')
  ROLE=$(echo "$CASE" | jq -r '.role')
  EXPECTED=$(echo "$CASE" | jq -r '.expected_behavior')
  QUICK=$(echo "$CASE" | jq -r '.quick_answer')

  echo "[$((i + 1))/$COUNT] $ID ($ROLE): $PROMPT"

  if [ "$DRY_RUN" = true ]; then
    echo "  [DRY RUN] Skipped"
    echo ""
    SKIP=$((SKIP + 1))
    continue
  fi

  # Call Claude API
  RESPONSE=$(curl -s https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d "$(jq -n \
      --arg model "$MODEL" \
      --arg system "$SYSTEM_PROMPT" \
      --arg prompt "$PROMPT" \
      '{
        model: $model,
        max_tokens: 2048,
        system: $system,
        messages: [{role: "user", content: $prompt}]
      }')")

  # Extract response text
  RESPONSE_TEXT=$(echo "$RESPONSE" | jq -r '.content[0].text // "ERROR: No response"')

  if echo "$RESPONSE_TEXT" | grep -q "^ERROR:"; then
    echo "  FAIL: $RESPONSE_TEXT"
    ERROR=$(echo "$RESPONSE" | jq -r '.error.message // "Unknown error"')
    echo "  API Error: $ERROR"
    FAIL=$((FAIL + 1))
    STATUS="error"
  else
    echo "  Response: ${RESPONSE_TEXT:0:150}..."
    STATUS="completed"
    PASS=$((PASS + 1))
  fi

  # Append to results
  RESULTS=$(echo "$RESULTS" | jq \
    --arg id "$ID" \
    --arg role "$ROLE" \
    --arg prompt "$PROMPT" \
    --arg expected "$EXPECTED" \
    --arg response "$RESPONSE_TEXT" \
    --arg status "$STATUS" \
    --argjson quick "$QUICK" \
    '. += [{
      id: $id,
      role: $role,
      prompt: $prompt,
      expected_behavior: $expected,
      quick_answer: $quick,
      response: $response,
      status: $status
    }]')

  echo ""

  # Rate limit: 1 request per second
  sleep 1
done

# Save results
if [ "$DRY_RUN" = false ]; then
  echo "$RESULTS" | jq '.' > "$RESULTS_FILE"
  echo "================================="
  echo "Results: $PASS completed, $FAIL errors out of $COUNT"
  echo "Saved to: $RESULTS_FILE"
  echo ""
  echo "Next step: Review results manually or feed them back to Claude"
  echo "to check each response against the expected_behavior field."
else
  echo "================================="
  echo "Dry run complete. $COUNT test cases would be run."
fi
