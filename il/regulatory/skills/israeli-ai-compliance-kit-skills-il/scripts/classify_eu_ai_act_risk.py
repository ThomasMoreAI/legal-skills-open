#!/usr/bin/env python3
"""Classify an AI system under the EU AI Act (Regulation 2024/1689).

Walks through a question tree covering Article 5 (prohibited), Annex III
(high-risk categories), limited-risk transparency obligations, and GPAI
obligations. Outputs a classification, reasoning, and a next-step checklist
for Israeli providers.

Not legal advice. Use with counsel for production deployments.

Usage:
    python classify_eu_ai_act_risk.py              # interactive
    python classify_eu_ai_act_risk.py --example    # run against a sample input
    python classify_eu_ai_act_risk.py --input case.json
"""

import argparse
import json
import sys

ANNEX_III_CATEGORIES = [
    ("biometrics", "Biometric identification, categorization, or emotion recognition"),
    ("critical_infra", "Safety components of critical infrastructure"),
    ("education", "Education, vocational training, student assessment"),
    ("employment", "Recruitment, worker management, access to self-employment"),
    ("essential_services", "Credit scoring, insurance underwriting, public benefits"),
    ("law_enforcement", "Policing, evidence assessment, profiling for crime"),
    ("migration", "Migration, asylum, border control"),
    ("justice", "Administration of justice, democratic processes"),
]

# A SCREEN, not a rendering of Article 5. Each label is shortened; read the Article
# before relying on a negative answer. Note that Article 5(1)(c) social scoring is NOT
# limited to public authorities, and 5(1)(a) and 5(1)(g) are easy to miss.
PROHIBITED_PRACTICES = [
    ("subliminal_manipulative", "Subliminal, purposefully manipulative or deceptive techniques that materially distort behaviour and cause significant harm (Art 5(1)(a))"),
    ("vulnerability_exploitation", "Exploiting vulnerabilities of age, disability or a specific social or economic situation (Art 5(1)(b))"),
    ("social_scoring", "Social scoring of persons or groups over time, by ANY actor public or private, leading to detrimental or unjustified treatment (Art 5(1)(c))"),
    ("predictive_policing_profile", "Predicting criminal offending based solely on profiling or personality traits (Art 5(1)(d))"),
    ("untargeted_scraping_face", "Untargeted scraping of facial images from the internet or CCTV to build or expand facial recognition databases (Art 5(1)(e))"),
    ("emotion_work_school", "Inferring emotions in the workplace or education, outside medical or safety uses (Art 5(1)(f))"),
    ("biometric_categorisation_sensitive", "Biometric categorisation to deduce race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation (Art 5(1)(g))"),
    ("biometric_public", "Real-time remote biometric ID in publicly accessible spaces for law enforcement (Art 5(1)(h))"),
]


def ask_yn(q: str) -> bool:
    while True:
        ans = input(f"{q} [y/n]: ").strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Please answer y or n.")


# Article 5 was amended by Regulation (EU) 2026/1744 (Digital Omnibus on AI), which
# inserted further prohibited practices applying from 2 December 2026. The list below
# predates that amendment, so a "not prohibited" result from this script is not a
# clearance. Every non-prohibited result carries the warning below.
AMENDED_ARTICLE_5_WARNING = (
    "This is a SCREEN, not a clearance. The questions above are shortened paraphrases "
    "of Article 5(1)(a) to (h), and Regulation (EU) 2026/1744 further adds points (ba) "
    "and (bb) to Article 5(1) first subparagraph plus Articles 5(1a) and 5(1b), all "
    "applying from 2 December 2026, which this script does not ask about at all. A "
    "not-prohibited result here means only that none of the shortened questions matched. "
    "Read the amended Article 5 in full before telling anyone the system is lawful."
)

ROLE_CAVEAT = (
    "- This result assumes you have already determined your ROLE. Provider, deployer, "
    "importer and distributor carry different obligations, and a deployer that puts its "
    "own name or trademark on a high-risk system, or substantially modifies one, can be "
    "treated as its provider. Read Articles 3, 25 and 26 of Regulation (EU) 2024/1689 "
    "rather than assuming. Article 4 AI literacy binds deployers as well as providers."
)

APPLICABILITY_DATES = (
    "Applicability, per Article 113 as amended by Regulation (EU) 2026/1744: the "
    "general date of application remains 2 August 2026 and has passed. Chapter III "
    "Sections 1 to 3 apply from 2 December 2027 for Annex III high-risk systems "
    "(Article 6(2)) and from 2 August 2028 for Annex I high-risk systems (Article 6(1))."
)


def classify(answers: dict) -> dict:
    reasons = []
    next_steps = []

    # Step 1: scope FIRST. Article 5 prohibitions are obligations under Regulation
    # (EU) 2024/1689, so they bite only on a system within the Regulation's Article 2
    # scope. Testing prohibitions before scope told Israel-only deployments they were
    # "Prohibited" under a regulation that does not apply to them.
    in_scope = (
        answers.get("eu_placed_on_market")
        or answers.get("eu_put_into_service")
        or answers.get("eu_output_used")
    )
    if not in_scope:
        matched = [
            label for key, label in PROHIBITED_PRACTICES
            if answers.get(f"prohibited_{key}")
        ]
        reasons = [
            "System is not placed on the EU market, not put into service in the EU, "
            "and its output is not used in the EU, so Regulation (EU) 2024/1689 does "
            "not apply to it."
        ]
        steps = [
            "Re-run this classification if EU deployment plans change.",
            "Document the scoping decision with date and owner.",
            "Confirm your ROLE before trusting this result. Provider, deployer, "
            "importer and distributor carry different obligations, and a deployer that "
            "puts its own name or trademark on a high-risk system, or substantially "
            "modifies one, can be treated as its provider. If in doubt, read Articles "
            "3, 25 and 26 of Regulation (EU) 2024/1689 rather than assuming.",
            "Israeli law still applies. Check the PPL and Amendment 13, and your "
            "sector regulator.",
        ]
        if matched:
            reasons.append(
                "NOTE: this system matches practices that WOULD be prohibited if it "
                "were in scope: " + "; ".join(matched) + ". That is a design and "
                "ethics signal and it blocks any future EU launch, but it is not an "
                "EU AI Act finding today."
            )
        return {"classification": "Out of scope", "reasons": reasons, "next_steps": steps}

    # Step 2: prohibited? (only meaningful once the system is in scope)
    for key, label in PROHIBITED_PRACTICES:
        if answers.get(f"prohibited_{key}"):
            return {
                "classification": "Prohibited",
                "reasons": [f"Matches prohibited practice: {label}"],
                "next_steps": [
                    "Cannot be placed on the EU market. Redesign or exclude EU.",
                    AMENDED_ARTICLE_5_WARNING,
                ],
            }

    # Step 3: GPAI?
    if answers.get("is_gpai"):
        gpai_obligations = [
            "Technical documentation for downstream developers",
            "Information summary of copyrighted training data",
            "Copyright policy for TDM opt-outs",
            "Compliance with Union copyright law",
        ]
        if answers.get("gpai_systemic_risk"):
            gpai_obligations += [
                "Model evaluations and adversarial testing",
                "Cybersecurity protections",
                "Serious incident reporting",
                "Track Article 51 thresholds and designation procedures",
            ]
        reasons.append("System is a general-purpose AI model.")
        next_steps += gpai_obligations

    # Step 4: high-risk?
    matched_annex = [
        label for key, label in ANNEX_III_CATEGORIES if answers.get(f"annex_iii_{key}")
    ]
    if matched_annex:
        reasons.append(f"Matches Annex III category: {'; '.join(matched_annex)}")
        next_steps += [
            "Implement risk management system across the lifecycle",
            "Ensure data governance for training, validation, and test sets",
            "Produce technical documentation per Annex IV",
            "Enable logging for traceability",
            "Provide transparency and information to deployers",
            "Enable human oversight",
            "Meet accuracy, robustness, and cybersecurity requirements",
            "Implement quality management system",
            "Perform conformity assessment (Annex VI or VII)",
            "Register in the EU database",
            "Apply CE marking",
            "Appoint authorized representative in the EU (Article 22)",
            "Establish post-market monitoring and incident reporting",
        ]
        if answers.get("is_gpai"):
            return {
                "classification": "High-risk + GPAI",
                "reasons": reasons,
                "next_steps": next_steps,
            }
        return {
            "classification": "High-risk",
            "reasons": reasons,
            "next_steps": next_steps,
        }

    # Step 5: limited-risk transparency?
    if (
        answers.get("is_chatbot_or_voice")
        or answers.get("is_deepfake_or_synthetic")
        or answers.get("is_emotion_recognition_general")
    ):
        reasons.append("System interacts with users or produces synthetic content.")
        next_steps += [
            "Disclose to users that they interact with AI",
            "Mark synthetic content as machine-readable AI-generated",
            "Inform users when emotion recognition or biometric categorization is used",
        ]
        if answers.get("is_gpai"):
            return {
                "classification": "Limited-risk + GPAI",
                "reasons": reasons,
                "next_steps": next_steps,
            }
        return {
            "classification": "Limited-risk",
            "reasons": reasons,
            "next_steps": next_steps,
        }

    if answers.get("is_gpai"):
        label = (
            "GPAI with systemic risk"
            if answers.get("gpai_systemic_risk")
            else "GPAI (no additional risk tier)"
        )
        return {
            "classification": label,
            "reasons": reasons,
            "next_steps": next_steps,
        }

    return {
        "classification": "Minimal-risk",
        "reasons": ["System does not trigger prohibited, high-risk, or limited-risk categories."],
        "next_steps": [
            "Consider voluntary codes of conduct",
            "Document the decision and review periodically",
        ],
    }


ALL_ANSWER_KEYS = (
    [f"prohibited_{k}" for k, _ in PROHIBITED_PRACTICES]
    + ["eu_placed_on_market", "eu_put_into_service", "eu_output_used"]
    + ["is_gpai", "gpai_systemic_risk"]
    + [f"annex_iii_{k}" for k, _ in ANNEX_III_CATEGORIES]
    + ["is_chatbot", "generates_synthetic_content", "is_emotion_recognition_general"]
)


def validate_answers(answers: dict):
    """Return (unknown_keys, missing_keys).

    An absent key used to default to False, so a partially filled or misspelled
    input produced a confident clearance against questions nobody had answered.
    Silence is not a 'no'.
    """
    known = set(ALL_ANSWER_KEYS)
    unknown = set(answers) - known
    missing = known - set(answers)
    # gpai_systemic_risk is only meaningful when is_gpai is true.
    if not answers.get("is_gpai"):
        missing.discard("gpai_systemic_risk")
    return unknown, missing


def interactive() -> dict:
    print("EU AI Act classifier. Answer each question y or n.\n")
    a = {}
    print("--- Prohibited practices ---")
    for key, label in PROHIBITED_PRACTICES:
        a[f"prohibited_{key}"] = ask_yn(label)
    print("\n--- EU scope ---")
    a["eu_placed_on_market"] = ask_yn("Is the system placed on the EU market?")
    a["eu_put_into_service"] = ask_yn("Is it put into service in the EU under your name?")
    a["eu_output_used"] = ask_yn("Is the system output used in the EU?")
    print("\n--- System type ---")
    a["is_gpai"] = ask_yn("Is the system a general-purpose AI model (foundation model)?")
    if a["is_gpai"]:
        a["gpai_systemic_risk"] = ask_yn(
            "Does the GPAI model meet the systemic-risk threshold (e.g. 10^25 FLOPs training)?"
        )
    print("\n--- Annex III categories ---")
    for key, label in ANNEX_III_CATEGORIES:
        a[f"annex_iii_{key}"] = ask_yn(label)
    print("\n--- Limited-risk transparency ---")
    a["is_chatbot_or_voice"] = ask_yn("Does the system interact with users via chat or voice?")
    a["is_deepfake_or_synthetic"] = ask_yn("Does it produce synthetic audio, image, or video?")
    a["is_emotion_recognition_general"] = ask_yn("Does it perform emotion recognition outside work/school?")
    return a


def render(result: dict) -> str:
    lines = [f"## Classification: {result['classification']}", "", "### Reasoning"]
    for r in result["reasons"]:
        lines.append(f"- {r}")
    lines.append("")
    lines.append("### Next Steps")
    for s in result["next_steps"]:
        lines.append(f"- {s}")
    if result["classification"] not in ("Prohibited", "Out of scope"):
        lines += ["", "### Caveats", f"- {AMENDED_ARTICLE_5_WARNING}"]
    if result["classification"] != "Out of scope":
        lines += [f"- {APPLICABILITY_DATES}", ROLE_CAVEAT]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Classify an AI system under the EU AI Act.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--input", help="JSON file of answers (skip interactive)")
    parser.add_argument("--example", action="store_true", help="Run with a sample Hebrew summarizer")
    args = parser.parse_args()

    if args.example:
        answers = {
            "eu_placed_on_market": False,
            "eu_put_into_service": False,
            "eu_output_used": False,
            "is_gpai": False,
            "is_chatbot_or_voice": False,
            "is_deepfake_or_synthetic": False,
            "is_emotion_recognition_general": False,
        }
        for key, _ in PROHIBITED_PRACTICES:
            answers[f"prohibited_{key}"] = False
        for key, _ in ANNEX_III_CATEGORIES:
            answers[f"annex_iii_{key}"] = False
    elif args.input:
        try:
            with open(args.input, "r", encoding="utf-8") as f:
                answers = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            print(f"Error loading input: {e}", file=sys.stderr)
            return 1
        if not isinstance(answers, dict):
            print("Error: input JSON must be an object mapping answer keys to true/false.",
                  file=sys.stderr)
            return 1
        unknown, missing = validate_answers(answers)
        if unknown:
            print("Error: unrecognised answer keys (typo?): " + ", ".join(sorted(unknown)),
                  file=sys.stderr)
            return 1
        if missing:
            print(
                "Error: the following answers are missing, and an unanswered question is "
                "NOT the same as a 'no'. Supply every key explicitly:\n  "
                + "\n  ".join(sorted(missing)),
                file=sys.stderr,
            )
            return 1
    else:
        answers = interactive()

    result = classify(answers)
    print(render(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
