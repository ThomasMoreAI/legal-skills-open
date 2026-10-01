#!/usr/bin/env python3
"""Split a shared-building (bayit meshutaf) cost by floor area.

Default rule, Land Law s.58(a): each apartment pays by the ratio of its floor
area to the floor area of all apartments, unless the registered takanon sets
another rate. Balconies and external walls are not counted unless the takanon
says otherwise (s.57(b)). An attached part of the common property counts at the
rate set in the takanon or by the Mafkach (s.57(c)); pass that rate as
attached_rate, never guess it.

For elevator INSTALLATION under s.59F(b) the owners who bear the cost share it by
floor area among themselves; ground-floor owners do not bear installation.
For installation, mark every apartment with "ground_floor": true or false; the
script always drops ground-floor apartments from an installation split. Then
list who DECIDED on it and exclude the other owners with --exclude (or pass
--all-decided if every non-ground-floor owner decided).

Informational helper only, not legal advice. Stdlib only, no network.

Input JSON: {"total": <number>, "apartments": [{"id": "1", "area": 90,
  "attached_area": 0, "attached_rate": 0, "ground_floor": false}, ...]}
"""
import argparse
import json
import sys

EXAMPLE = {
    "total": 36000,
    "apartments": [
        {"id": "1 (ground)", "area": 90, "ground_floor": True},
        {"id": "2 (ground)", "area": 90, "ground_floor": True},
        {"id": "3", "area": 100, "ground_floor": False},
        {"id": "4", "area": 100, "ground_floor": False},
        {"id": "5", "area": 110, "ground_floor": False},
        {"id": "6", "area": 110, "ground_floor": False},
    ],
}


def effective_area(apt):
    base = float(apt["area"])
    extra = float(apt.get("attached_area", 0)) * float(apt.get("attached_rate", 0))
    return base + extra


def validate(data, exclude, kind="maintenance"):
    if not isinstance(data, dict) or not isinstance(data.get("apartments"), list) or "total" not in data:
        raise ValueError('input must be {"total": <number>, "apartments": [...]}')
    if kind == "installation":
        unmarked = [str(a.get("id")) for a in data["apartments"] if not isinstance(a.get("ground_floor"), bool)]
        if unmarked:
            raise ValueError("installation split: mark every apartment with ground_floor true/false "
                             "(s.59F(b)(2)); unmarked: " + ", ".join(unmarked))
    ids = [str(a["id"]) for a in data["apartments"]]
    dups = sorted({i for i in ids if ids.count(i) > 1})
    if dups:
        raise ValueError("duplicate apartment ids: " + ", ".join(dups))
    for a in data["apartments"]:
        if float(a["area"]) <= 0:
            raise ValueError(f"apartment {a['id']}: area must be positive")
        if float(a.get("attached_area", 0)) < 0 or float(a.get("attached_rate", 0)) < 0:
            raise ValueError(f"apartment {a['id']}: attached area and rate cannot be negative")
    unknown = [x for x in exclude if x not in ids]
    if unknown:
        raise ValueError("unknown ids in --exclude: " + ", ".join(unknown))
    if float(data["total"]) < 0:
        raise ValueError("total cannot be negative")


def split(data, exclude=(), kind="maintenance"):
    """Return (payers' area, rows). Payments are in agorot-precise shekels and
    always sum exactly to the total: each payer is floored to the agora, and the
    leftover agorot go one each to the payers with the largest area, ties broken
    by input order."""
    exclude = list(exclude)
    validate(data, exclude, kind)
    payers = [a for a in data["apartments"] if str(a["id"]) not in set(exclude)
              and not (kind == "installation" and a.get("ground_floor") is True)]
    if not payers:
        raise ValueError("no apartments left to pay")
    total_area = sum(effective_area(a) for a in payers)
    if total_area <= 0:
        raise ValueError("total counted area is zero")
    total_ag = round(float(data["total"]) * 100)
    exact = {id(a): effective_area(a) / total_area * total_ag for a in payers}
    alloc = {k: int(v // 1) for k, v in exact.items()}
    rest = total_ag - sum(alloc.values())
    order = sorted(range(len(payers)), key=lambda i: (-effective_area(payers[i]), i))
    for n in range(rest):
        alloc[id(payers[order[n % len(payers)]])] += 1
    rows = []
    for a in data["apartments"]:
        if id(a) in alloc:
            rows.append((str(a["id"]), effective_area(a), effective_area(a) / total_area, alloc[id(a)] / 100))
        else:
            rows.append((str(a["id"]), effective_area(a), 0.0, 0.0))
    return total_area, rows


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("json_file", nargs="?", help="input JSON file (see docstring)")
    p.add_argument("--exclude", default="", help="comma-separated apartment ids that do not bear this payment")
    p.add_argument("--total", type=float, help="override the total cost")
    p.add_argument("--kind", choices=["maintenance", "installation"], default="maintenance",
                   help="maintenance/running cost (default) or elevator installation")
    p.add_argument("--all-decided", action="store_true",
                   help="installation only: confirm that every non-ground-floor apartment decided on the "
                        "installation (s.59F(b)(1)); ground-floor apartments are dropped automatically")
    p.add_argument("--example", action="store_true", help="run the built-in example")
    args = p.parse_args()
    if args.example:
        data = EXAMPLE
    elif args.json_file:
        try:
            with open(args.json_file, encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, ValueError) as e:
            print("ERROR: cannot read input JSON: " + str(e), file=sys.stderr)
            return 2
    else:
        p.print_help()
        return 1
    if args.total is not None:
        data = dict(data, total=args.total)
    exclude = [x.strip() for x in args.exclude.split(",") if x.strip()]
    if exclude and args.kind == "maintenance":
        print("WARNING: --exclude on a maintenance/running cost. s.58(a) has no non-use "
              "exemption; exclude only if the registered takanon or the owner's own agreement says so.",
              file=sys.stderr)
    if args.kind == "installation" and not exclude and not args.all_decided:
        print("ERROR: elevator installation is borne only by the owners who decided on it, and never by the "
              "ground floor (s.59F(b)(1)-(2)). Mark ground_floor on every apartment (they are dropped "
              "automatically), then pass --exclude with every owner who did not decide, or --all-decided if "
              "every non-ground-floor owner decided.", file=sys.stderr)
        return 2
    try:
        total_area, rows = split(data, exclude, args.kind)
    except (ValueError, TypeError, OverflowError, KeyError, AttributeError) as e:
        print("ERROR: " + str(e), file=sys.stderr)
        return 2
    print("apartment | counted area | share | payment")
    for rid, area, share, pay in rows:
        print(f"{rid} | {area:g} | {share:.4f} | {pay:,.2f}")
    print(f"payers' counted area: {total_area:g}; total: {float(data['total']):,.2f}; "
          f"sum of payments: {sum(r[3] for r in rows):,.2f}")
    print("Rounding: payments are floored to the agora; leftover agorot go to the largest-area payers first.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
