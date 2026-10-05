#!/usr/bin/env python3
"""validate_skill.py — Structural validator for the privacy-compliance skill.

Validates that the skill package is complete, well-formed, and follows
established conventions. Run from the skill root directory:

    python3 scripts/validate_skill.py [--root /path/to/skill]

Exit code 0 = all checks passed.
Exit code 1 = validation error(s) found.
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple


# ── Required files ──────────────────────────────────────────────────────────

REQUIRED_FILES = [
    "SKILL.md",
    "LICENSE",
    "CHANGELOG.md",
    "scripts/validate_skill.py",
    "evals/test_cases.json",
    "references/privacy-regulations.md",
]

OPTIONAL_DIRS = [
    "assets",
    "examples",
    "templates",
]

# ── Required frontmatter fields in SKILL.md ────────────────────────────────

REQUIRED_FRONTMATTER = [
    "name",
    "version",
    "author",
    "description",
    "platforms",
    "tags",
]

# ── Required sections (H2 headings) in SKILL.md body ───────────────────────

REQUIRED_SECTIONS = [
    "Quick Reference",
    "When to Use This Skill",
    "Common Pitfalls",  # Headings containing "Common Pitfalls" match
    "Workflows",
    "Safety Rules",
    "Platform Compatibility Notes",
    "References",
]

# ── Required tags (must be present in the tags list) ───────────────────────

REQUIRED_TAGS = [
    "privacy",
    "GDPR",
    "CCPA",
    "data-protection",
    "compliance",
    "PII",
]

# ── Helpers ─────────────────────────────────────────────────────────────────

def success(msg: str) -> str:
    return f"  ✅ {msg}"

def failure(msg: str) -> str:
    return f"  ❌ {msg}"


def parse_frontmatter(text: str) -> Dict[str, object]:
    """Extract YAML frontmatter between --- markers."""
    pattern = r"^---\s*\n(.*?)\n---\s*\n"
    match = re.search(pattern, text, re.DOTALL)
    if not match:
        return {}
    # Simple YAML parser — handles flat keys, lists, and nested objects.
    raw = match.group(1)
    result: Dict[str, object] = {}
    current_key: str | None = None
    current_list: List[str] = []
    in_list = False
    indent_level = 0

    for line in raw.split("\n"):
        stripped = line.rstrip()
        if not stripped or stripped.startswith("#"):
            continue

        # Check if this is a list item under the current key
        if in_list and stripped.strip().startswith("-"):
            item = re.sub(r"^\s*-\s+", "", stripped.strip())
            current_list.append(item)
            continue
        elif in_list and (not stripped.startswith(" ") and not stripped.startswith("\t")):
            # End of list — this line is a new top-level key
            if current_list:
                result[current_key or "tags"] = current_list
            current_list = []
            in_list = False
            # Fall through to process this line as a new key-value pair

        # Key-value pair
        kv_match = re.match(r"^(\s*)([\w\-]+):\s*(.*)", stripped)
        if kv_match:
            indent = len(kv_match.group(1))
            key = kv_match.group(2)
            value = kv_match.group(3).strip()

            if value == "[]":
                result[key] = []
                continue

            if value == "":
                # Empty value — this key might have indented list items below
                # If next non-empty line is indented and starts with -, it's a list
                in_list = True
                current_key = key
                current_list = []
                indent_level = indent
                continue

            if value.startswith("[") or value.startswith("-"):
                # Inline list
                if value.startswith("[") and value.endswith("]"):
                    items = [v.strip().strip("'\"") for v in value[1:-1].split(",") if v.strip()]
                    result[key] = items
                elif value.startswith("-"):
                    in_list = True
                    current_key = key
                    items = [value[1:].strip().strip("'\"")]
                    current_list = items
                    indent_level = indent
            else:
                result[key] = value.strip("'\"")

    # Finalize any open list
    if in_list and current_list:
        result[current_key or "tags"] = current_list

    return result


def extract_body(text: str) -> str:
    """Extract body content after YAML frontmatter."""
    pattern = r"^---\s*\n.*?\n---\s*\n"
    return re.sub(pattern, "", text, count=1, flags=re.DOTALL)


def get_h2_headings(text: str) -> List[str]:
    """Extract level-2 markdown headings (## heading)."""
    headings = re.findall(r"^##\s+(.+)$", text, re.MULTILINE)
    return [h.strip() for h in headings]


# ── Check functions ─────────────────────────────────────────────────────────

def check_files(root: Path) -> List[Tuple[bool, str]]:
    results = []
    for f in REQUIRED_FILES:
        path = root / f
        if path.is_file():
            results.append((True, success(f"Required file present: {f}")))
        else:
            results.append((False, failure(f"Missing required file: {f}")))
    return results


def check_frontmatter(root: Path) -> List[Tuple[bool, str]]:
    results = []
    skill_path = root / "SKILL.md"
    if not skill_path.is_file():
        results.append((False, failure("SKILL.md not found — cannot validate frontmatter")))
        return results

    text = skill_path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)

    if not fm:
        results.append((False, failure("No valid YAML frontmatter found in SKILL.md")))
        return results

    for field in REQUIRED_FRONTMATTER:
        if field in fm:
            results.append((True, success(f"Frontmatter field present: {field}")))
        else:
            results.append((False, failure(f"Missing frontmatter field: {field}")))

    # Validate version format (semver)
    if "version" in fm:
        version = str(fm["version"])
        if re.match(r"^\d+\.\d+\.\d+$", version):
            results.append((True, success(f"Version format valid: {version}")))
        else:
            results.append((False, failure(f"Version not semver: {version}")))

    # Validate tags
    if "tags" in fm:
        tags = fm["tags"]
        if isinstance(tags, list):
            for tag in REQUIRED_TAGS:
                if tag in tags:
                    results.append((True, success(f"Required tag present: {tag}")))
                else:
                    results.append((False, failure(f"Missing required tag: {tag}")))
        else:
            results.append((False, failure("Tags field is not a list")))

    # Validate platforms
    if "platforms" in fm:
        platforms = fm["platforms"]
        if isinstance(platforms, list) and len(platforms) >= 3:
            results.append((True, success(f"Platforms listed: {len(platforms)}")))
        else:
            results.append((False, failure("Platforms missing or too few (need 3+)")))

    return results


def check_sections(root: Path) -> List[Tuple[bool, str]]:
    results = []
    skill_path = root / "SKILL.md"
    if not skill_path.is_file():
        return results

    text = skill_path.read_text(encoding="utf-8")
    body = extract_body(text)
    headings = get_h2_headings(text)

    for section in REQUIRED_SECTIONS:
        # Support partial match for sections like "Common Pitfalls & Anti-Patterns"
        found = any(section in h for h in headings)
        if found:
            results.append((True, success(f"Required section present: {section}")))
        else:
            results.append((False, failure(f"Missing required section: {section}")))

    # Check disclaimer presence
    disclaimer_pattern = r"(?i)THIS\s+IS\s+NOT\s+LEGAL\s+ADVICE|not\s+legal\s+advice|NOT\s+LEGAL\s+ADVICE"
    if re.search(disclaimer_pattern, body):
        results.append((True, success("Legal disclaimer present")))
    else:
        results.append((False, failure("Missing legal disclaimer — 'THIS IS NOT LEGAL ADVICE'")))

    return results


def check_changelog(root: Path) -> List[Tuple[bool, str]]:
    results = []
    cl_path = root / "CHANGELOG.md"
    if not cl_path.is_file():
        results.append((False, failure("CHANGELOG.md not found")))
        return results

    text = cl_path.read_text(encoding="utf-8")
    if "1.0.0" in text and "Initial release" in text:
        results.append((True, success("CHANGELOG.md contains v1.0.0 entry")))
    else:
        results.append((False, failure("CHANGELOG.md missing v1.0.0 entry")))
    return results


def check_test_cases(root: Path) -> List[Tuple[bool, str]]:
    results = []
    tc_path = root / "evals" / "test_cases.json"
    if not tc_path.is_file():
        results.append((False, failure("evals/test_cases.json not found")))
        return results

    import json
    try:
        with open(tc_path) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        results.append((False, failure(f"test_cases.json is not valid JSON: {e}")))
        return results

    if isinstance(data, list):
        count = len(data)
        if count >= 5:
            results.append((True, success(f"test_cases.json has {count} test cases (≥5)")))
        else:
            results.append((False, failure(f"test_cases.json has only {count} test cases (need ≥5)")))

        # Check each test case has required fields
        for i, case in enumerate(data):
            if not isinstance(case, dict):
                results.append((False, failure(f"Test case {i} is not an object")))
                continue
            for field in ("name", "input", "expected_workflow"):
                if field not in case:
                    results.append((False, failure(f"Test case {i} missing field: {field}")))
        return results
    else:
        results.append((False, failure("test_cases.json is not an array")))
        return results


def check_reference_doc(root: Path) -> List[Tuple[bool, str]]:
    results = []
    ref_path = root / "references" / "privacy-regulations.md"
    if not ref_path.is_file():
        results.append((False, failure("references/privacy-regulations.md not found")))
        return results

    text = ref_path.read_text(encoding="utf-8")

    # Check for key regulations
    required_regs = ["GDPR", "CCPA", "HIPAA", "LGPD", "EU AI Act"]
    for reg in required_regs:
        if reg in text:
            results.append((True, success(f"Reference covers: {reg}")))
        else:
            results.append((False, failure(f"Reference missing: {reg}")))

    return results


def check_optional_dirs(root: Path) -> List[Tuple[bool, str]]:
    results = []
    for d in OPTIONAL_DIRS:
        path = root / d
        if path.is_dir():
            results.append((True, success(f"Optional directory present: {d}/")))
    return results


# ── Main ────────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(description="Validate privacy-compliance skill package")
    parser.add_argument(
        "--root",
        default=None,
        help="Path to skill root directory (default: parent of scripts/)",
    )
    args = parser.parse_args()

    if args.root:
        root = Path(args.root).resolve()
    else:
        # Assume script is in skill_root/scripts/
        root = Path(__file__).resolve().parent.parent

    print(f"\n🔍 Validating privacy-compliance skill at: {root}\n")
    print("="  *  60)

    all_checks: List[Tuple[bool, str]] = []

    sections = {
        "File Structure": check_files,
        "Frontmatter": check_frontmatter,
        "Sections & Disclaimer": check_sections,
        "Changelog": check_changelog,
        "Test Cases": check_test_cases,
        "Reference Document": check_reference_doc,
        "Optional Directories": check_optional_dirs,
    }

    total = 0
    passed = 0

    for label, check_fn in sections.items():
        print(f"\n📋 {label}:")
        results = check_fn(root)
        all_checks.extend(results)
        for ok, msg in results:
            print(msg)
            total += 1
            if ok:
                passed += 1

    failed = total - passed

    print(f"\n{'='  *  60}")
    print(f"📊 Results: {passed}/{total} checks passed")

    if failed > 0:
        print(f"❌ {failed} check(s) FAILED")
    else:
        print("✅ All checks passed!")

    print()

    return 1 if failed > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
