#!/usr/bin/env bash
# SDLT Calculator — England & Northern Ireland residential property
# Usage: sdlt-calc.sh <price> [--ftb] [--additional] [--non-resident] [--compare] [--json]
# Rates effective from 1 April 2025 (post-temporary threshold revert)

set -euo pipefail

# --- Rate loading ---
# Try live rates first (GitHub raw), fall back to local file
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RATES_URL="https://raw.githubusercontent.com/MoverlyLtd/conveyancing-toolkit/master/sdlt-calculator/scripts/sdlt-rates.json"
RATES_FILE="$SCRIPT_DIR/sdlt-rates.json"
RATES_JSON=""

# Attempt live fetch (1s timeout)
if command -v curl &>/dev/null; then
  RATES_JSON=$(curl -sf --max-time 1 "$RATES_URL" 2>/dev/null || true)
fi

# Fallback to local file
if [[ -z "$RATES_JSON" ]] && [[ -f "$RATES_FILE" ]]; then
  RATES_JSON=$(cat "$RATES_FILE")
fi

# Parse rates from JSON if available, otherwise use baked-in defaults
if [[ -n "$RATES_JSON" ]] && command -v python3 &>/dev/null; then
  # Extract rates via python3 (available on all modern systems)
  eval "$(python3 -c "
import json, sys
r = json.loads('''$RATES_JSON''')
s = r['standard']
print(f'STD_B1={s[0][\"threshold\"]}')
print(f'STD_B2={s[1][\"threshold\"]}')
print(f'STD_B3={s[2][\"threshold\"]}')
print(f'STD_B4={s[3][\"threshold\"]}')
print(f'STD_R2={s[1][\"rate\"]}')
print(f'STD_R3={s[2][\"rate\"]}')
print(f'STD_R4={s[3][\"rate\"]}')
print(f'STD_R5={s[4][\"rate\"]}')
ftb = r['firstTimeBuyer']
print(f'FTB_MAX={ftb[\"maxPrice\"]}')
print(f'FTB_B1={ftb[\"bands\"][0][\"threshold\"]}')
print(f'FTB_R2={ftb[\"bands\"][1][\"rate\"]}')
print(f'FTB_B2={ftb[\"bands\"][1][\"threshold\"]}')
print(f'ADD_SURCHARGE={r[\"additionalSurcharge\"]}')
print(f'NR_SURCHARGE={r[\"nonResidentSurcharge\"]}')
print(f'RATES_DATE={r[\"effectiveFrom\"]}')
" 2>/dev/null)" || {
    # Parse failed — use defaults
    RATES_JSON=""
  }
fi

# Baked-in fallback (1 April 2025 rates)
: "${STD_B1:=125000}"
: "${STD_B2:=250000}"
: "${STD_B3:=925000}"
: "${STD_B4:=1500000}"
: "${STD_R2:=2}"
: "${STD_R3:=5}"
: "${STD_R4:=10}"
: "${STD_R5:=12}"
: "${FTB_MAX:=500000}"
: "${FTB_B1:=300000}"
: "${FTB_R2:=5}"
: "${FTB_B2:=500000}"
: "${ADD_SURCHARGE:=5}"
: "${NR_SURCHARGE:=2}"
: "${RATES_DATE:=2025-04-01}"

PRICE=""
FTB=false
ADDITIONAL=false
NON_RESIDENT=false
COMPARE=false
JSON=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --ftb) FTB=true; shift ;;
    --additional) ADDITIONAL=true; shift ;;
    --non-resident|--non-uk) NON_RESIDENT=true; shift ;;
    --compare) COMPARE=true; shift ;;
    --json) JSON=true; shift ;;
    --help|-h)
      echo "Usage: sdlt-calc.sh <price> [--ftb] [--additional] [--non-resident] [--compare] [--json]"
      echo ""
      echo "  --ftb           First-time buyer relief"
      echo "  --additional    Additional property (+5% surcharge)"
      echo "  --non-resident  Non-UK resident (+2% surcharge)"
      echo "  --compare       Show all scenarios"
      echo "  --json          Output as JSON"
      exit 0
      ;;
    *)
      if [[ -z "$PRICE" ]]; then
        PRICE="$1"
      else
        echo "Error: unexpected argument '$1'" >&2; exit 1
      fi
      shift
      ;;
  esac
done

if [[ -z "$PRICE" ]]; then
  echo "Error: purchase price required" >&2
  echo "Usage: sdlt-calc.sh <price> [--ftb] [--additional] [--non-resident] [--compare]" >&2
  exit 1
fi

# Strip commas, £, spaces — keep digits only
PRICE=$(echo "$PRICE" | tr -d ',£ ')
if ! [[ "$PRICE" =~ ^[0-9]+$ ]]; then
  echo "Error: invalid price '$PRICE' (whole pounds only)" >&2; exit 1
fi

# Format number with commas
fmt() {
  echo "$1" | sed ':a;s/\B[0-9]\{3\}\>/.&/;ta' | tr '.' ','
}

# Calculate tax on a band: tax_on_band <amount_in_band> <rate_percent>
# Uses integer arithmetic: amount * rate / 100
tax_on_band() {
  echo $(( $1 * $2 / 100 ))
}

# min of two values
min() { (( $1 < $2 )) && echo "$1" || echo "$2"; }
max() { (( $1 > $2 )) && echo "$1" || echo "$2"; }

# Calculate SDLT
# Args: price ftb(0/1) additional(0/1) non_resident(0/1)
calculate_sdlt() {
  local p=$1 ftb=$2 add=$3 nr=$4
  local surcharge=0
  (( add == 1 )) && (( surcharge += ADD_SURCHARGE )) || true
  (( nr == 1 )) && (( surcharge += NR_SURCHARGE )) || true

  local total=0
  local -a bands=()   # "label|rate|tax" entries
  local remaining=$p

  # Check FTB eligibility
  local ftb_eligible=0
  if (( ftb == 1 && p <= FTB_MAX )); then
    ftb_eligible=1
  fi

  if (( ftb_eligible == 1 )); then
    # FTB Band 1: 0–FTB_B1 at 0% + surcharge
    local b1; b1=$(min $remaining $FTB_B1)
    local r1=$surcharge
    local t1; t1=$(tax_on_band $b1 $r1)
    (( total += t1 )) || true
    bands+=("£0–£$(fmt $FTB_B1)|${r1}%|£$(fmt $t1)")
    remaining=$(max $(( remaining - FTB_B1 )) 0)

    # FTB Band 2: FTB_B1+1–FTB_B2 at FTB_R2% + surcharge
    if (( remaining > 0 )); then
      local ftb_b2_width=$(( FTB_B2 - FTB_B1 ))
      local b2; b2=$(min $remaining $ftb_b2_width)
      local r2=$(( FTB_R2 + surcharge ))
      local t2; t2=$(tax_on_band $b2 $r2)
      (( total += t2 )) || true
      bands+=("£$(fmt $(( FTB_B1 + 1 )))–£$(fmt $FTB_B2)|${r2}%|£$(fmt $t2)")
      remaining=$(max $(( remaining - ftb_b2_width )) 0)
    fi
  else
    # Standard bands (dynamic from rates config)
    # Band 1: 0–STD_B1 at 0% + surcharge
    local b1; b1=$(min $remaining $STD_B1)
    local r1=$surcharge
    local t1; t1=$(tax_on_band $b1 $r1)
    (( total += t1 )) || true
    bands+=("£0–£$(fmt $STD_B1)|${r1}%|£$(fmt $t1)")
    remaining=$(max $(( remaining - STD_B1 )) 0)

    # Band 2: STD_B1+1–STD_B2 at STD_R2% + surcharge
    if (( remaining > 0 )); then
      local b2_width=$(( STD_B2 - STD_B1 ))
      local b2; b2=$(min $remaining $b2_width)
      local r2=$(( STD_R2 + surcharge ))
      local t2; t2=$(tax_on_band $b2 $r2)
      (( total += t2 )) || true
      bands+=("£$(fmt $(( STD_B1 + 1 )))–£$(fmt $STD_B2)|${r2}%|£$(fmt $t2)")
      remaining=$(max $(( remaining - b2_width )) 0)
    fi

    # Band 3: STD_B2+1–STD_B3 at STD_R3% + surcharge
    if (( remaining > 0 )); then
      local b3_width=$(( STD_B3 - STD_B2 ))
      local b3; b3=$(min $remaining $b3_width)
      local r3=$(( STD_R3 + surcharge ))
      local t3; t3=$(tax_on_band $b3 $r3)
      (( total += t3 )) || true
      bands+=("£$(fmt $(( STD_B2 + 1 )))–£$(fmt $STD_B3)|${r3}%|£$(fmt $t3)")
      remaining=$(max $(( remaining - b3_width )) 0)
    fi

    # Band 4: STD_B3+1–STD_B4 at STD_R4% + surcharge
    if (( remaining > 0 )); then
      local b4_width=$(( STD_B4 - STD_B3 ))
      local b4; b4=$(min $remaining $b4_width)
      local r4=$(( STD_R4 + surcharge ))
      local t4; t4=$(tax_on_band $b4 $r4)
      (( total += t4 )) || true
      bands+=("£$(fmt $(( STD_B3 + 1 )))–£$(fmt $STD_B4)|${r4}%|£$(fmt $t4)")
      remaining=$(max $(( remaining - b4_width )) 0)
    fi

    # Band 5: above STD_B4 at STD_R5% + surcharge
    if (( remaining > 0 )); then
      local r5=$(( STD_R5 + surcharge ))
      local t5; t5=$(tax_on_band $remaining $r5)
      (( total += t5 )) || true
      bands+=("Above £$(fmt $STD_B4)|${r5}%|£$(fmt $t5)")
    fi
  fi

  # Effective rate: total * 10000 / price gives basis points, then format
  local eff_bp=0
  (( p > 0 )) && eff_bp=$(( total * 10000 / p ))
  local eff_whole=$(( eff_bp / 100 ))
  local eff_frac=$(( eff_bp % 100 ))
  local effective
  printf -v effective "%d.%02d%%" "$eff_whole" "$eff_frac"

  # Build label
  local label=""
  if (( ftb_eligible == 1 )); then
    label="First-time buyer"
  elif (( ftb == 1 )); then
    label="Standard (FTB not available — price exceeds £$(fmt $FTB_MAX))"
  else
    label="Standard purchase"
  fi
  (( add == 1 )) && label="${label} + additional property"
  (( nr == 1 )) && label="${label} + non-resident"

  if [[ "$JSON" == true ]]; then
    local ftb_json="false"; (( ftb_eligible == 1 )) && ftb_json="true"
    local add_json="false"; (( add == 1 )) && add_json="true"
    local nr_json="false"; (( nr == 1 )) && nr_json="true"
    echo "{\"scenario\":\"$label\",\"price\":$p,\"sdlt\":$total,\"effectiveRate\":\"$effective\",\"ftb\":$ftb_json,\"additional\":$add_json,\"nonResident\":$nr_json}"
    return
  fi

  echo "=== $label ==="
  echo "Purchase price: £$(fmt $p)"
  echo ""
  printf "  %-24s %8s %12s\n" "Band" "Rate" "Tax"
  printf "  %-24s %8s %12s\n" "------------------------" "--------" "------------"
  for entry in "${bands[@]}"; do
    IFS='|' read -r band rate tax <<< "$entry"
    printf "  %-24s %8s %12s\n" "$band" "$rate" "$tax"
  done
  echo ""
  echo "  Total SDLT:    £$(fmt $total)"
  echo "  Effective rate: $effective"
  echo "  Rates from:    $RATES_DATE"
}

# --- Main ---

if [[ "$COMPARE" == true ]]; then
  echo "SDLT Comparison — £$(fmt $PRICE)"
  echo "════════════════════════════════════════════════"
  echo ""
  calculate_sdlt "$PRICE" 0 0 0

  if (( PRICE <= FTB_MAX )); then
    echo ""
    calculate_sdlt "$PRICE" 1 0 0
  fi

  echo ""
  calculate_sdlt "$PRICE" 0 1 0
  echo ""
  calculate_sdlt "$PRICE" 0 0 1
  echo ""
  calculate_sdlt "$PRICE" 0 1 1
else
  local_ftb=0; [[ "$FTB" == true ]] && local_ftb=1
  local_add=0; [[ "$ADDITIONAL" == true ]] && local_add=1
  local_nr=0; [[ "$NON_RESIDENT" == true ]] && local_nr=1
  calculate_sdlt "$PRICE" "$local_ftb" "$local_add" "$local_nr"
fi
