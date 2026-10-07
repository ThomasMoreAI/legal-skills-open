"""
EU AI Act Risk Classifier — Batch Mode
Classify multiple AI systems from a CSV or JSON file.
Author: Marco De Roni | github.com/marcoderoni
"""

import os
import csv
import json
import argparse
import time
from datetime import datetime
from dotenv import load_dotenv
from classifier import classify, print_banner

load_dotenv()

RISK_ORDER = {
    "PROHIBITED": 0,
    "HIGH-RISK": 1,
    "GPAI": 2,
    "LIMITED RISK": 3,
    "MINIMAL RISK": 4,
    "UNKNOWN": 5,
}

RISK_EMOJI = {
    "PROHIBITED":    "🚫",
    "HIGH-RISK":     "⚠️ ",
    "GPAI":          "🤖",
    "LIMITED RISK":  "ℹ️ ",
    "MINIMAL RISK":  "✅",
    "UNKNOWN":       "❓",
}


def load_systems(path: str) -> list[dict]:
    """Load AI systems from CSV or JSON."""
    if path.endswith(".csv"):
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)
    elif path.endswith(".json"):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    else:
        raise ValueError("Unsupported format. Use .csv or .json")


def run_batch(systems: list[dict], delay: float = 1.5) -> list[dict]:
    """Classify all systems with rate-limit-friendly delay."""
    results = []
    total = len(systems)

    for i, system in enumerate(systems, 1):
        desc = system.get("description") or system.get("system") or system.get("ai_system", "")
        name = system.get("name") or system.get("id") or f"System_{i}"

        print(f"  [{i}/{total}] Classifying: {name[:50]}...")

        try:
            result = classify(desc)
            results.append({
                "id": i,
                "name": name,
                "description": desc,
                "risk_level": result.get("risk_level", "UNKNOWN"),
                "confidence": result.get("confidence", ""),
                "legal_basis": result.get("legal_basis", ""),
                "annex_iii_category": result.get("annex_iii_category"),
                "recommendation": result.get("recommendation", ""),
                "full_result": result,
            })
            level = result.get("risk_level", "UNKNOWN")
            emoji = RISK_EMOJI.get(level, "❓")
            print(f"         → {emoji} {level}\n")
        except Exception as e:
            print(f"         → ❌ ERROR: {e}\n")
            results.append({"id": i, "name": name, "description": desc,
                             "risk_level": "ERROR", "error": str(e)})

        if i < total:
            time.sleep(delay)

    return results


def save_batch_report(results: list[dict], output_path: str):
    """Save full batch report as JSON."""
    report = {
        "timestamp": datetime.now().isoformat(),
        "tool": "EU AI Act Risk Classifier v1.0 — Batch",
        "author": "Marco De Roni | github.com/marcoderoni",
        "total_systems": len(results),
        "summary": {
            "PROHIBITED": sum(1 for r in results if r.get("risk_level") == "PROHIBITED"),
            "HIGH-RISK": sum(1 for r in results if r.get("risk_level") == "HIGH-RISK"),
            "GPAI": sum(1 for r in results if r.get("risk_level") == "GPAI"),
            "LIMITED RISK": sum(1 for r in results if r.get("risk_level") == "LIMITED RISK"),
            "MINIMAL RISK": sum(1 for r in results if r.get("risk_level") == "MINIMAL RISK"),
        },
        "results": results,
    }
    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)


def save_csv_summary(results: list[dict], output_path: str):
    """Save CSV summary for quick review."""
    fieldnames = ["id", "name", "risk_level", "confidence", "legal_basis",
                  "annex_iii_category", "recommendation"]
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(results)


def print_summary(results: list[dict]):
    """Print a summary table."""
    print("\n" + "─" * 60)
    print("  BATCH CLASSIFICATION SUMMARY")
    print("─" * 60)
    sorted_results = sorted(results, key=lambda r: RISK_ORDER.get(r.get("risk_level", "UNKNOWN"), 9))
    for r in sorted_results:
        level = r.get("risk_level", "UNKNOWN")
        emoji = RISK_EMOJI.get(level, "❓")
        name = r.get("name", "")[:38].ljust(38)
        print(f"  {emoji}  {name}  {level}")
    print("─" * 60)
    from collections import Counter
    counts = Counter(r.get("risk_level") for r in results)
    for level in ["PROHIBITED", "HIGH-RISK", "GPAI", "LIMITED RISK", "MINIMAL RISK"]:
        if counts.get(level):
            print(f"  {RISK_EMOJI.get(level, '')}  {level}: {counts[level]}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="EU AI Act Batch Classifier — classify multiple AI systems at once"
    )
    parser.add_argument("-i", "--input", required=True,
                        help="Input file: CSV (columns: name, description) or JSON list")
    parser.add_argument("-o", "--output", default="batch_report.json",
                        help="Output JSON report path (default: batch_report.json)")
    parser.add_argument("--csv", default=None,
                        help="Also save a CSV summary")
    parser.add_argument("--delay", type=float, default=1.5,
                        help="Delay between API calls in seconds (default: 1.5)")
    args = parser.parse_args()

    print_banner()
    print(f"  Loading systems from: {args.input}\n")

    systems = load_systems(args.input)
    print(f"  Found {len(systems)} AI system(s) to classify.\n")
    print("─" * 60)

    results = run_batch(systems, delay=args.delay)
    print_summary(results)

    save_batch_report(results, args.output)
    print(f"  [✓] Full report saved: {args.output}")

    if args.csv:
        save_csv_summary(results, args.csv)
        print(f"  [✓] CSV summary saved: {args.csv}")


if __name__ == "__main__":
    main()
