"""
EU AI Act Risk Classifier
Classifies AI systems under the EU AI Act (Reg. 2024/1689)
Author: Marco De Roni | github.com/marcoderoni
"""

import os
import sys
import json
import argparse
import textwrap
from datetime import datetime
from dotenv import load_dotenv
import anthropic

load_dotenv()

# ─── EU AI Act Reference Framework ──────────────────────────────────────────

PROHIBITED_PRACTICES = """
Article 5 — PROHIBITED AI PRACTICES:
- Subliminal or manipulative techniques exploiting vulnerabilities (age, disability)
- Social scoring by public authorities affecting rights
- Real-time remote biometric identification in public spaces (law enforcement, with exceptions)
- Emotion recognition in workplace or educational institutions
- Biometric categorisation inferring sensitive attributes (race, political views, sexual orientation)
- Predictive policing based solely on profiling or personality traits
- Untargeted scraping of facial images from internet/CCTV to build databases
"""

HIGH_RISK_ANNEX_III = """
Annex III — HIGH-RISK AI SYSTEMS (8 categories):

1. BIOMETRICS: Remote biometric ID systems; biometric categorisation; emotion recognition
2. CRITICAL INFRASTRUCTURE: Safety management in transport, water, gas, electricity, digital infra
3. EDUCATION & TRAINING: Admissions decisions, exam proctoring, learning assessment, monitoring
4. EMPLOYMENT & WORKERS: Recruitment/CV screening, promotion/demotion decisions, task allocation, performance monitoring
5. ESSENTIAL SERVICES: Credit scoring, insurance risk assessment, public benefit eligibility, emergency dispatch prioritisation
6. LAW ENFORCEMENT: Individual risk assessment for crime, lie detection, evidence reliability, crime analytics/profiling, deepfake detection
7. MIGRATION & ASYLUM: Risk assessment of migrants, asylum application decisions, identity verification, document authenticity
8. ADMINISTRATION OF JUSTICE: AI in judicial decisions, legal interpretation assistance, dispute resolution
"""

GPAI_FRAMEWORK = """
GPAI MODELS (Article 51-56):
- General Purpose AI Models (e.g., foundation models/LLMs)
- Systemic risk if FLOP threshold exceeded (10^25 FLOPs training compute)
- Obligations: transparency, copyright compliance, technical documentation
- High-impact GPAI: additional adversarial testing, incident reporting, cybersecurity
"""

LIMITED_RISK = """
LIMITED RISK (Transparency Obligations — Article 50):
- Chatbots: must disclose AI nature to users
- Deepfakes: must label synthetic audio/visual content
- AI-generated text for public interest topics: must be labelled
- Emotion recognition systems: must inform users
"""

CLASSIFICATION_PROMPT = """You are a senior EU AI Act compliance specialist with deep expertise in Regulation (EU) 2024/1689.

Your task: classify the described AI system under the EU AI Act risk framework.

## EU AI Act Framework Reference

{prohibited}

{high_risk}

{gpai}

{limited_risk}

## Classification Rules

Apply this decision tree strictly:
1. Check Article 5 first → if matches → PROHIBITED (unacceptable risk)
2. Check Annex III → if matches → HIGH-RISK
3. Check GPAI (Articles 51-56) → if foundation/general-purpose model → GPAI
4. Check transparency obligations (Article 50) → if chatbot/deepfake/emotion → LIMITED RISK
5. Otherwise → MINIMAL/NO RISK

## Output Format (JSON only, no markdown, no preamble)

{{
  "risk_level": "PROHIBITED | HIGH-RISK | GPAI | LIMITED RISK | MINIMAL RISK",
  "confidence": "HIGH | MEDIUM | LOW",
  "legal_basis": "Specific article/annex reference",
  "annex_iii_category": "Category number and name if HIGH-RISK, else null",
  "prohibited_practice": "Specific prohibited practice if PROHIBITED, else null",
  "key_obligations": ["list", "of", "3-5", "main", "obligations"],
  "deployer_obligations": ["list", "of", "deployer-specific", "obligations"],
  "provider_obligations": ["list", "of", "provider-specific", "obligations"],
  "compliance_deadlines": "Applicable dates from the AI Act gradual rollout",
  "caveats": "Any important caveats, edge cases, or jurisdiction-specific notes",
  "recommendation": "Practical next step for a legal/compliance team"
}}

## System to Classify

{system_description}
"""

# ─── Risk Level Display ──────────────────────────────────────────────────────

RISK_COLORS = {
    "PROHIBITED":    "\033[91m",  # Red
    "HIGH-RISK":     "\033[93m",  # Yellow
    "GPAI":          "\033[95m",  # Magenta
    "LIMITED RISK":  "\033[94m",  # Blue
    "MINIMAL RISK":  "\033[92m",  # Green
}
RESET = "\033[0m"
BOLD  = "\033[1m"
DIM   = "\033[2m"

RISK_EMOJI = {
    "PROHIBITED":    "🚫",
    "HIGH-RISK":     "⚠️ ",
    "GPAI":          "🤖",
    "LIMITED RISK":  "ℹ️ ",
    "MINIMAL RISK":  "✅",
}


def print_banner():
    banner = f"""
{BOLD}╔══════════════════════════════════════════════════════════════╗
║         EU AI ACT RISK CLASSIFIER  v1.0                      ║
║         Regulation (EU) 2024/1689 · github.com/marcoderoni   ║
╚══════════════════════════════════════════════════════════════╝{RESET}
    """
    print(banner)


def classify(system_description: str, verbose: bool = False) -> dict:
    """Call Claude API to classify the AI system."""
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    prompt = CLASSIFICATION_PROMPT.format(
        prohibited=PROHIBITED_PRACTICES,
        high_risk=HIGH_RISK_ANNEX_III,
        gpai=GPAI_FRAMEWORK,
        limited_risk=LIMITED_RISK,
        system_description=system_description,
    )

    if verbose:
        print(f"{DIM}[→] Sending to Claude API...{RESET}\n")

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = message.content[0].text.strip()

    # Strip markdown fences if present
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]

    return json.loads(raw)


def render_result(result: dict, system_description: str):
    """Pretty-print the classification result."""
    level = result.get("risk_level", "UNKNOWN")
    color = RISK_COLORS.get(level, "")
    emoji = RISK_EMOJI.get(level, "❓")

    print(f"\n{BOLD}AI SYSTEM:{RESET}")
    wrapped = textwrap.fill(system_description, width=70, initial_indent="  ", subsequent_indent="  ")
    print(f"{DIM}{wrapped}{RESET}\n")

    print("─" * 62)
    print(f"\n{BOLD}CLASSIFICATION RESULT{RESET}\n")
    print(f"  {emoji}  Risk Level   : {color}{BOLD}{level}{RESET}")
    print(f"  📊  Confidence   : {result.get('confidence', 'N/A')}")
    print(f"  📜  Legal Basis  : {result.get('legal_basis', 'N/A')}")

    if result.get("annex_iii_category"):
        print(f"  📁  Annex III    : {result['annex_iii_category']}")
    if result.get("prohibited_practice"):
        print(f"  ❌  Prohibited   : {result['prohibited_practice']}")

    print(f"\n{BOLD}KEY OBLIGATIONS:{RESET}")
    for ob in result.get("key_obligations", []):
        print(f"  • {ob}")

    if result.get("provider_obligations"):
        print(f"\n{BOLD}PROVIDER OBLIGATIONS:{RESET}")
        for ob in result.get("provider_obligations", []):
            print(f"  • {ob}")

    if result.get("deployer_obligations"):
        print(f"\n{BOLD}DEPLOYER OBLIGATIONS:{RESET}")
        for ob in result.get("deployer_obligations", []):
            print(f"  • {ob}")

    print(f"\n{BOLD}COMPLIANCE DEADLINES:{RESET}")
    print(f"  {result.get('compliance_deadlines', 'N/A')}")

    if result.get("caveats"):
        print(f"\n{BOLD}CAVEATS:{RESET}")
        print(f"  {DIM}{result['caveats']}{RESET}")

    print(f"\n{BOLD}RECOMMENDATION:{RESET}")
    rec = textwrap.fill(result.get("recommendation", "N/A"), width=66,
                        initial_indent="  ", subsequent_indent="  ")
    print(rec)

    print("\n" + "─" * 62)
    print(f"{DIM}  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')} | EU AI Act Classifier v1.0{RESET}\n")


def save_report(result: dict, system_description: str, output_path: str):
    """Save JSON report to file."""
    report = {
        "timestamp": datetime.now().isoformat(),
        "tool": "EU AI Act Risk Classifier v1.0",
        "author": "Marco De Roni | github.com/marcoderoni",
        "system_description": system_description,
        "classification": result,
    }
    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\n{DIM}[✓] Report saved to: {output_path}{RESET}")


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="EU AI Act Risk Classifier — classify any AI system under Reg. 2024/1689",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""
        Examples:
          python classifier.py -d "HR tool that scores job applicants using CV data"
          python classifier.py -d "Chatbot for customer support" --output report.json
          python classifier.py --interactive
        """),
    )
    parser.add_argument("-d", "--description", type=str,
                        help="Description of the AI system to classify")
    parser.add_argument("-o", "--output", type=str, default=None,
                        help="Save JSON report to file")
    parser.add_argument("--interactive", action="store_true",
                        help="Enter interactive mode")
    parser.add_argument("--verbose", action="store_true",
                        help="Show API call details")

    args = parser.parse_args()
    print_banner()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print(f"\033[91m[ERROR] ANTHROPIC_API_KEY not set. Copy .env.example → .env and add your key.\033[0m")
        sys.exit(1)

    if args.interactive:
        print("Interactive mode — describe your AI system. Type 'quit' to exit.\n")
        while True:
            desc = input(f"{BOLD}AI System Description:{RESET}\n> ").strip()
            if desc.lower() in ("quit", "exit", "q"):
                break
            if not desc:
                continue
            print()
            result = classify(desc, verbose=args.verbose)
            render_result(result, desc)
            if args.output:
                save_report(result, desc, args.output)
    elif args.description:
        result = classify(args.description, verbose=args.verbose)
        render_result(result, args.description)
        if args.output:
            save_report(result, args.description, args.output)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
