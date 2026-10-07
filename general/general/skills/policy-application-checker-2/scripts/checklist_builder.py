#!/usr/bin/env python3
import argparse, json

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("requirements_json", help="JSON list with requirement,owner,deadline")
    ap.add_argument("--out", default="checklist.md")
    args = ap.parse_args()
    rows = json.load(open(args.requirements_json, "r", encoding="utf-8"))
    parts = ["# Submission Checklist\n"]
    for row in rows:
        parts.append(f"- [ ] {row.get('requirement','Requirement')}\n  - Owner: {row.get('owner','')}\n  - Deadline: {row.get('deadline','')}\n  - Evidence: \n")
    open(args.out, "w", encoding="utf-8").write("\n".join(parts))
    print(f"Wrote {args.out}")

if __name__ == "__main__":
    main()
