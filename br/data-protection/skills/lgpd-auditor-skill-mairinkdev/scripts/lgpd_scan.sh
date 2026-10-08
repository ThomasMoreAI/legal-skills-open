#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
OUT="${2:-lgpd-scan-report.txt}"

{
  echo "# LGPD Static Scan"
  echo "Root: $ROOT"
  echo "Generated: $(date -Iseconds)"
  echo
  echo "This scan is only a heuristic. Review findings manually."
  echo

  echo "## Repository files of interest"
  if git -C "$ROOT" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    git -C "$ROOT" ls-files \
      | grep -Ei '(^|/)(app|src|pages|routes|api|server|backend|frontend|prisma|drizzle|migrations|schema|models|entities|controllers|services|middlewares|lib|utils|auth|admin|legal|privacy|terms|cookies)' \
      | grep -Eiv '(node_modules|dist|build|coverage|\.next|\.turbo|package-lock|pnpm-lock|yarn.lock)' \
      | head -300
  else
    find "$ROOT" -type f \
      | grep -Ei '(^|/)(app|src|pages|routes|api|server|backend|frontend|prisma|drizzle|migrations|schema|models|entities|controllers|services|middlewares|lib|utils|auth|admin|legal|privacy|terms|cookies)' \
      | grep -Eiv '(node_modules|dist|build|coverage|\.next|\.turbo|package-lock|pnpm-lock|yarn.lock)' \
      | head -300
  fi

  echo
  echo "## Possible secrets/env files (names only)"
  find "$ROOT" -maxdepth 4 -type f \( -name ".env" -o -name ".env.*" -o -name "*secret*" -o -name "*credential*" \) \
    | grep -Eiv '(node_modules|dist|build|coverage|\.next|\.turbo)' || true

  echo
  echo "## Pattern hits"
} > "$OUT"

run_rg() {
  local title="$1"
  local pattern="$2"
  {
    echo
    echo "### $title"
    rg -n --hidden --glob '!node_modules' --glob '!dist' --glob '!build' --glob '!coverage' --glob '!.next' --glob '!.turbo' --glob '!.env' --glob '!.env.*' \
      -i "$pattern" "$ROOT" || true
  } >> "$OUT"
}

run_rg "PII common fields" "email|phone|telefone|cpf|cnpj|document|rg|passport|birth|nascimento|address|endereco|cep|pix|bank|account"
run_rg "Sensitive data indicators" "health|saude|medical|religion|religiao|politic|politica|race|racial|biometric|biometria|sexual|genetic|genetico"
run_rg "Auth/session/security" "password|hash|token|jwt|session|cookie|csrf|oauth|refresh|authorization|bearer"
run_rg "Logs and telemetry" "console\.log|logger|debug|print|Sentry|captureException|captureMessage"
run_rg "Cookies and browser storage" "localStorage|sessionStorage|document\.cookie|Set-Cookie|cookies|consent"
run_rg "Analytics/marketing" "gtag|GA4|posthog|mixpanel|hotjar|clarity|pixel|Meta Pixel|TikTok|analytics"
run_rg "AI/LLM/data sent to models" "openai|anthropic|claude|gemini|llm|prompt|embedding|vector|AI_PROVIDER"
run_rg "Data subject rights" "deleteAccount|exportData|privacy|consent|retention|anonymize|erase|portability|lgpd"
run_rg "Third-party processors" "resend|stripe|mercado ?pago|mercadopago|pluggy|sentry|discord|webhook|storage|s3|cloudinary|firebase"

echo "Report written to $OUT"
