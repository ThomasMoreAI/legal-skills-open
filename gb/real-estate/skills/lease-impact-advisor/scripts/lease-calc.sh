#!/usr/bin/env bash
# Lease Impact Advisor — deterministic lease assessment for estate agents
# Usage: lease-calc.sh <years_remaining> [property_value] [mortgage_term]
# All calculations use integer arithmetic (no bc dependency)

set -euo pipefail

YEARS="${1:-}"
VALUE="${2:-0}"
MORTGAGE_TERM="${3:-25}"

if [ -z "$YEARS" ]; then
  echo "Usage: lease-calc.sh <years_remaining> [property_value] [mortgage_term]"
  echo ""
  echo "  years_remaining  Current unexpired lease term (required)"
  echo "  property_value   Property value in £ (optional, for extension estimate)"
  echo "  mortgage_term    Mortgage term in years (default: 25)"
  exit 1
fi

# Strip currency symbols and commas
VALUE=$(echo "$VALUE" | sed 's/[£,]//g')

format_number() {
  local n="$1"
  local sign=""
  if [ "$n" -lt 0 ]; then
    sign="-"
    n=$(( -n ))
  fi
  local result=""
  local str="$n"
  local len=${#str}
  local i=0
  while [ $i -lt $len ]; do
    if [ $i -gt 0 ] && [ $(( (len - i) % 3 )) -eq 0 ]; then
      result="${result},"
    fi
    result="${result}${str:$i:1}"
    i=$(( i + 1 ))
  done
  echo "${sign}${result}"
}

YEARS_AT_END=$(( YEARS - MORTGAGE_TERM ))

echo "═══════════════════════════════════════════════════════"
echo " LEASE IMPACT ASSESSMENT"
echo "═══════════════════════════════════════════════════════"
echo ""
echo " Unexpired term:     ${YEARS} years"
if [ "$VALUE" -gt 0 ]; then
  echo " Property value:     £$(format_number "$VALUE")"
fi
echo " Mortgage term:      ${MORTGAGE_TERM} years"
echo " Years at redemption: ${YEARS_AT_END} years"
echo ""

# Risk band
echo "───────────────────────────────────────────────────────"
echo " RISK BAND"
echo "───────────────────────────────────────────────────────"
if [ "$YEARS" -ge 90 ]; then
  echo " [GREEN] No impact on saleability"
  echo ""
  echo " Full buyer pool. All mainstream lenders accept."
  echo " No action needed — lease length is not a factor."
elif [ "$YEARS" -ge 80 ]; then
  echo " [AMBER] Approaching threshold — act soon"
  echo ""
  echo " Most lenders still accept. No marriage value payable."
  echo " However, this lease will drop below 80 years within"
  echo " $(( YEARS - 80 )) years — at which point extension costs"
  echo " increase significantly due to marriage value."
  echo ""
  echo " Recommendation: extend before it drops below 80."
  echo " This is the cheapest time to extend."
elif [ "$YEARS" -ge 70 ]; then
  echo " [RED] Restricted buyer pool"
  echo ""
  echo " Marriage value now applies — extension will cost more."
  echo " Some lenders will decline. Buyer pool narrowed."
  echo " Estimated price discount: 5-15% vs equivalent freehold."
  echo ""
  echo " Recommendation: strongly advise vendor to extend before"
  echo " marketing, or price to reflect lease impact."
elif [ "$YEARS" -ge 55 ]; then
  echo " [CRITICAL] Severely restricted"
  echo ""
  echo " Most mainstream lenders decline. Cash buyers or"
  echo " specialist lenders only. Significant price impact."
  echo " Estimated price discount: 15-30% vs equivalent freehold."
  echo ""
  echo " Recommendation: extension essential before marketing."
  echo " Without extension, expect much longer time to sell"
  echo " and substantially reduced offers."
else
  echo " [UNMORTGAGEABLE] Virtually unsaleable without extension"
  echo ""
  echo " No mainstream lender will accept this lease."
  echo " Cash buyers only — very small buyer pool."
  echo " Price discount: 30%+ vs equivalent freehold."
  echo " Some properties at this level are functionally unsaleable."
  echo ""
  echo " Recommendation: do not market without commencing"
  echo " lease extension. Consider informal negotiation with"
  echo " freeholder (no 2-year ownership requirement)."
fi

echo ""
echo "───────────────────────────────────────────────────────"
echo " MARRIAGE VALUE"
echo "───────────────────────────────────────────────────────"
if [ "$YEARS" -ge 80 ]; then
  echo " No marriage value payable (lease is 80+ years)."
  echo " This is the most cost-effective time to extend."
  echo " Once it drops below 80, costs increase significantly."
else
  echo " Marriage value APPLIES (lease is under 80 years)."
  echo ""
  echo " The leaseholder must pay the freeholder 50% of the"
  echo " increase in property value from the extension."
  echo ""
  echo " Note: the Leasehold and Freehold Reform Act 2024"
  echo " abolishes marriage value, but this has NOT yet come"
  echo " into force. Advise based on current law."
fi

echo ""
echo "───────────────────────────────────────────────────────"
echo " LENDER ELIGIBILITY (${YEARS} years, ${MORTGAGE_TERM}-year term)"
echo "───────────────────────────────────────────────────────"
echo ""

check_lender() {
  local name="$1"
  local min_at_completion="$2"
  local min_at_end="$3"
  local notes="$4"

  local status="ELIGIBLE"
  local reason=""

  if [ "$YEARS" -lt "$min_at_completion" ]; then
    status="INELIGIBLE"
    reason="Minimum ${min_at_completion} years at completion"
  elif [ "$min_at_end" -gt 0 ] && [ "$YEARS_AT_END" -lt "$min_at_end" ]; then
    status="INELIGIBLE"
    reason="Need ${min_at_end} years at end of ${MORTGAGE_TERM}-year term (would have ${YEARS_AT_END})"
  fi

  # Marginal cases
  if [ "$status" = "ELIGIBLE" ]; then
    if [ "$min_at_completion" -gt 0 ] && [ $(( YEARS - min_at_completion )) -lt 5 ]; then
      status="MARGINAL"
      reason="Close to minimum — may need referral"
    fi
  fi

  printf " %-20s [%-10s]" "$name" "$status"
  if [ -n "$reason" ]; then
    echo " $reason"
  elif [ -n "$notes" ]; then
    echo " $notes"
  else
    echo ""
  fi
}

# Lender: name, min_at_completion, min_at_end_of_term, notes
check_lender "Nationwide" 55 30 "90yr min for >85% LTV second-hand flat"
check_lender "NatWest" $(( MORTGAGE_TERM + 30 )) 0 "Requires term + 30 years"
check_lender "HSBC" $(( MORTGAGE_TERM + 50 )) 0 "50yr after mortgage; refer if <85yr"
check_lender "Barclays" 70 0 "Prestige London estates may get discretion"
check_lender "Halifax" 70 0 ""
check_lender "Lloyds" 70 0 ""
check_lender "TSB" 70 30 ""
check_lender "Santander" 55 30 "Complex rules — refer if <82yr"
check_lender "Coventry BS" 70 0 "80yr for lifetime mortgages"
check_lender "Virgin Money" 85 0 "Must extend before completion if shorter"
check_lender "Yorkshire BS" 60 0 ""
check_lender "Skipton BS" 55 0 ""
check_lender "Leeds BS" 60 0 ""

# Count eligible/marginal/ineligible
eligible=0
marginal=0
ineligible=0

count_lender() {
  local min_c="$1"
  local min_e="$2"
  if [ "$YEARS" -lt "$min_c" ]; then
    ineligible=$(( ineligible + 1 ))
  elif [ "$min_e" -gt 0 ] && [ "$YEARS_AT_END" -lt "$min_e" ]; then
    ineligible=$(( ineligible + 1 ))
  elif [ "$min_c" -gt 0 ] && [ $(( YEARS - min_c )) -lt 5 ]; then
    marginal=$(( marginal + 1 ))
  else
    eligible=$(( eligible + 1 ))
  fi
}

count_lender 55 30   # Nationwide
count_lender $(( MORTGAGE_TERM + 30 )) 0  # NatWest
count_lender $(( MORTGAGE_TERM + 50 )) 0  # HSBC
count_lender 70 0    # Barclays
count_lender 70 0    # Halifax
count_lender 70 0    # Lloyds
count_lender 70 30   # TSB
count_lender 55 30   # Santander
count_lender 70 0    # Coventry
count_lender 85 0    # Virgin Money
count_lender 60 0    # Yorkshire
count_lender 55 0    # Skipton
count_lender 60 0    # Leeds

echo ""
echo " Summary: ${eligible} eligible, ${marginal} marginal, ${ineligible} ineligible out of 13 major lenders"

# Extension cost estimate
if [ "$VALUE" -gt 0 ]; then
  echo ""
  echo "───────────────────────────────────────────────────────"
  echo " EXTENSION COST ESTIMATE"
  echo "───────────────────────────────────────────────────────"
  echo ""
  echo " These are rough estimates only. Actual premiums depend"
  echo " on ground rent, local values, and negotiation."
  echo " A specialist surveyor valuation is always recommended."
  echo ""

  # Simplified premium estimation based on years remaining
  # Uses percentage of property value as rough guide
  # Based on published guidance and industry norms
  if [ "$YEARS" -ge 90 ]; then
    low=$(( VALUE * 1 / 100 ))
    high=$(( VALUE * 3 / 100 ))
    echo " Estimated premium: £$(format_number $low) - £$(format_number $high)"
    echo " (Very low — mainly landlord's reversion interest)"
  elif [ "$YEARS" -ge 80 ]; then
    low=$(( VALUE * 2 / 100 ))
    high=$(( VALUE * 5 / 100 ))
    echo " Estimated premium: £$(format_number $low) - £$(format_number $high)"
    echo " (No marriage value — this is the sweet spot to extend)"
  elif [ "$YEARS" -ge 70 ]; then
    low=$(( VALUE * 5 / 100 ))
    high=$(( VALUE * 12 / 100 ))
    echo " Estimated premium: £$(format_number $low) - £$(format_number $high)"
    echo " (Marriage value applies — 50% of value uplift)"
  elif [ "$YEARS" -ge 60 ]; then
    low=$(( VALUE * 10 / 100 ))
    high=$(( VALUE * 20 / 100 ))
    echo " Estimated premium: £$(format_number $low) - £$(format_number $high)"
    echo " (Significant marriage value component)"
  elif [ "$YEARS" -ge 50 ]; then
    low=$(( VALUE * 15 / 100 ))
    high=$(( VALUE * 30 / 100 ))
    echo " Estimated premium: £$(format_number $low) - £$(format_number $high)"
    echo " (Very high marriage value — extension urgent)"
  else
    low=$(( VALUE * 25 / 100 ))
    high=$(( VALUE * 50 / 100 ))
    echo " Estimated premium: £$(format_number $low) - £$(format_number $high)"
    echo " (Extremely high — specialist valuation essential)"
  fi

  echo ""
  echo " Plus professional fees (solicitor + surveyor):"
  echo " Typically £2,000 - £4,000"
  echo ""
  echo " Net cost if extending before marketing:"
  low_total=$(( low + 3000 ))
  high_total=$(( high + 3000 ))
  echo " £$(format_number $low_total) - £$(format_number $high_total) approx"
fi

echo ""
echo "───────────────────────────────────────────────────────"
echo " EXTENSION OPTIONS"
echo "───────────────────────────────────────────────────────"
echo ""
echo " 1. STATUTORY (Section 42 notice)"
echo "    - Requires 2 years ownership"
echo "    - Adds 90 years to current lease"
echo "    - Ground rent reduced to peppercorn (£0)"
echo "    - Freeholder cannot refuse"
echo "    - Timeline: 6-12 months typically"
echo ""
echo " 2. INFORMAL NEGOTIATION"
echo "    - No ownership requirement"
echo "    - Terms negotiable (length, ground rent)"
echo "    - Faster but freeholder can set terms"
echo "    - Consider if vendor hasn't owned 2 years"
echo ""
echo " 3. ASSIGN BENEFIT (for sales)"
echo "    - Seller starts Section 42 process"
echo "    - Assigns the right to buyer on completion"
echo "    - Buyer completes the extension"
echo "    - Good option when seller hasn't owned 2 years"
echo "    - Or when buyer wants to control the process"
echo ""
echo "═══════════════════════════════════════════════════════"
echo " This assessment is for guidance only. It is not legal"
echo " advice. Always consult a specialist lease extension"
echo " solicitor for formal advice."
echo "═══════════════════════════════════════════════════════"
