#!/usr/bin/env python3
"""Audit frontmatter of all published skills (excludes skillsmp/, lawve/, tools/ quarantine)."""
import os, csv, json, re
import yaml
from jsonschema import Draft202012Validator

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA = json.load(open(os.path.join(ROOT, "schemas", "skill-frontmatter.schema.json")))
validator = Draft202012Validator(SCHEMA)

EXCLUDE_TOP = {"skillsmp", "lawve", "tools", "audit", "schemas"}

def find_skills():
    out = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        rel = os.path.relpath(dirpath, ROOT)
        top = rel.split(os.sep)[0]
        if top in EXCLUDE_TOP:
            dirnames[:] = []
            continue
        if "SKILL.md" in filenames:
            out.append(os.path.join(dirpath, "SKILL.md"))
    return sorted(out)

def parse_frontmatter(path):
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---"):
        return None, "no frontmatter (file does not start with ---)"
    # split on the first two --- delimiters
    m = re.match(r"^---\s*\n(.*?)\n---\s*(\n|$)", text, re.DOTALL)
    if not m:
        return None, "frontmatter delimiters not closed properly"
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        return None, f"YAML parse error: {str(e).splitlines()[0]}"
    if not isinstance(data, dict):
        return None, "frontmatter is not a mapping"
    return data, None

def check(path):
    issues = []
    rel = os.path.relpath(path, ROOT)
    parts = rel.split(os.sep)
    data, err = parse_frontmatter(path)
    if err:
        return rel, "ERROR", err
    # schema validation
    for e in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        loc = "/".join(str(p) for p in e.path) or "(root)"
        issues.append(f"{loc}: {e.message}")
    # path consistency: {jur}/{practice}/skills/{slug}/SKILL.md
    if len(parts) >= 5 and parts[2] == "skills":
        jur_seg, prac_seg, slug_seg = parts[0], parts[1], parts[3]
        if data.get("name") != slug_seg:
            issues.append(f"name '{data.get('name')}' != folder '{slug_seg}'")
        if data.get("jurisdiction") != jur_seg:
            issues.append(f"jurisdiction '{data.get('jurisdiction')}' != path '{jur_seg}'")
        if data.get("practice") != prac_seg:
            issues.append(f"practice '{data.get('practice')}' != path '{prac_seg}'")
    else:
        issues.append(f"unexpected path layout: {rel}")
    if issues:
        return rel, "ERROR", "; ".join(issues)
    return rel, "OK", ""

def main():
    skills = find_skills()
    rows = []
    ok = 0
    for s in skills:
        rel, status, detail = check(s)
        if status == "OK":
            ok += 1
        rows.append((rel, status, detail))
    out_csv = os.path.join(ROOT, "audit", "сhecking_frontmatter.csv")
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["skill", "frontmatter_status", "issues"])
        w.writerows(rows)
    print(f"total={len(rows)} ok={ok} errors={len(rows)-ok}")
    # field-presence consistency summary
    from collections import Counter
    keysets = Counter()
    for s in skills:
        d, e = parse_frontmatter(s)
        if d:
            keysets[tuple(sorted(d.keys()))] += 1
    print(f"distinct frontmatter key-sets: {len(keysets)}")

if __name__ == "__main__":
    main()
