#!/usr/bin/env python3
"""Property-balancing (izun mashabim) worksheet for Israeli divorce.

Computes the equal-value balance under the Spousal Property Relations Law,
5733-1973 (chok yachasei mamon), section 5. Each spouse is entitled to half
the value of ALL the couple's assets, EXCEPT a closed list of exclusions
(assets owned before the marriage, gifts and inheritances received during
the marriage, National Insurance benefits, personal-injury compensation, and
anything agreed in writing not to balance). The script balances VALUE, so one
spouse keeps an asset and pays the other half its value.

The 50/50 default can be varied by the court under section 8 of the law (for
example an unequal division where an equal split would be unjust). This script
does not model that; it computes only the equal balance. Treat the equal split
as a starting point a court can adjust, and confirm the result with a lawyer.

This is a preparation tool, not a court filing or legal advice. Classification
of each item (balanceable vs. excluded, commingling questions) and the final
settlement must be confirmed with a family lawyer.

No third-party dependencies. Python 3.8+.

Usage:
  python3 izun_mashabim.py --example
  python3 izun_mashabim.py --file assets.json
  python3 izun_mashabim.py --asset "Family home:J:1800000:balanceable" \
                           --asset "Premarital flat:A:1200000:excluded" \
                           --debt "Mortgage:J:900000" \
                           --debt "Mortgage on premarital flat:A:500000:excluded"

JSON input shape (see --example output for a full sample):
  {
    "spouse_a": "Spouse A",
    "spouse_b": "Spouse B",
    "assets": [
      {"label": "Family home", "owner": "A", "value": 1800000, "balanceable": true}
    ],
    "debts": [
      {"label": "Mortgage", "owner": "A", "value": 900000}
    ]
  }
Owner is "A", "B", or "J" (jointly registered: split half to each spouse).
"balanceable" is REQUIRED on every asset (true/false, or the words
"balanceable"/"excluded"); a missing flag is an error, so an inheritance cannot
slip into the pool by omission. Excluded assets stay with the owner and do not
enter the pool. Debts enter the pool EXCEPT a debt connected with an excluded
asset (for example a mortgage on a pre-marriage apartment): section 6(a)
deducts debts "except debts connected with assets whose value is not to be
balanced". Mark such a debt with "excluded": true (CLI: label:owner:value:excluded).
A negative net position (debts above balanceable assets) is computed by the
section 6(b) half-the-difference formula but flagged for a lawyer, because a
court does not mechanically make the other spouse share such a deficit.
"""

import argparse
import json
import sys


def normalize_owner(owner):
    """Return 'A', 'B' or 'J' (joint), or raise ValueError."""
    key = str(owner).strip().upper()
    if key in ("A", "B", "J"):
        return key
    raise ValueError("owner must be 'A', 'B' or 'J' (joint), got: %r" % owner)


def parse_value(raw, label):
    """Parse a non-negative amount; accepts '1,000,000'. Rejects NaN and negatives."""
    try:
        value = float(str(raw).replace(",", "").strip())
    except ValueError:
        raise ValueError("value for %r is not a number: %r" % (label, raw))
    if value != value or value in (float("inf"), float("-inf")):
        raise ValueError("value for %r is not a finite number" % label)
    if value < 0:
        raise ValueError("value for %r is negative; enter a liability as a debt" % label)
    return value


def parse_flag(raw, label, field):
    """Strict boolean: true/false or balanceable/excluded. Anything else is an error."""
    if isinstance(raw, bool):
        return raw
    key = str(raw).strip().lower()
    if key in ("true", "balanceable", "yes"):
        return True
    if key in ("false", "excluded", "no"):
        return False
    raise ValueError("%s for %r must be balanceable/excluded (true/false), got %r"
                     % (field, label, raw))


def parse_excluded(raw, label):
    """Strict flag for a debt: True only for true/yes/excluded; False for false/no."""
    if isinstance(raw, bool):
        return raw
    key = str(raw).strip().lower()
    if key in ("true", "yes", "excluded"):
        return True
    if key in ("false", "no", ""):
        return False
    raise ValueError("excluded for debt %r must be true/false, got %r" % (label, raw))


def add_to(bucket, owner, value):
    """Add value to a per-spouse bucket; a joint item is split half to each."""
    if owner == "J":
        bucket["A"] += value / 2.0
        bucket["B"] += value / 2.0
    else:
        bucket[owner] += value


def build_worksheet(data):
    """Compute the balance. Returns a result dict with per-spouse figures."""
    name_a = data.get("spouse_a", "Spouse A")
    name_b = data.get("spouse_b", "Spouse B")

    # Value of balanceable assets currently held by each spouse.
    held = {"A": 0.0, "B": 0.0}
    # Value of excluded assets (kept out of the pool, shown for transparency).
    excluded = {"A": 0.0, "B": 0.0}
    # Marital debts netted against the pool, tracked per spouse.
    debts = {"A": 0.0, "B": 0.0}

    # Debts connected with excluded assets leave the balance with the asset (s.6(a)).
    excluded_debts = {"A": 0.0, "B": 0.0}
    # Excluded debts owned solely by one spouse (not joint), for the mislabel warning.
    sole_excluded_debts = {"A": 0.0, "B": 0.0}

    for asset in data.get("assets", []):
        label = asset.get("label", "?")
        owner = normalize_owner(asset["owner"])
        value = parse_value(asset["value"], label)
        if "balanceable" not in asset:
            raise ValueError("asset %r is missing 'balanceable' (true/false); an "
                             "unclassified asset is never assumed balanceable" % label)
        if parse_flag(asset["balanceable"], label, "balanceable"):
            add_to(held, owner, value)
        else:
            add_to(excluded, owner, value)

    for debt in data.get("debts", []):
        label = debt.get("label", "?")
        owner = normalize_owner(debt["owner"])
        value = parse_value(debt["value"], label)
        unknown = set(debt) - {"label", "owner", "value", "excluded"}
        if unknown:
            raise ValueError("debt %r has unknown field(s) %s" % (label, sorted(unknown)))
        if parse_excluded(debt.get("excluded", False), label):
            add_to(excluded_debts, owner, value)
            if owner != "J":
                sole_excluded_debts[owner] += value
        else:
            add_to(debts, owner, value)

    # s.6(a) excludes only debts CONNECTED with an excluded asset: an "excluded"
    # debt with no excluded asset held by that spouse is almost always a
    # mislabelled marital debt, so refuse it rather than drop it from the pool.
    # Checked on the pooled totals, so a debt co-signed by both spouses (owner J)
    # on ONE spouse's excluded asset is accepted.
    if sum(excluded_debts.values()) > 0 and sum(excluded.values()) == 0:
        raise ValueError("a debt is marked excluded but no asset is excluded; s.6(a) "
                         "excludes only debts connected with an excluded asset. List "
                         "that asset as excluded (a co-signed mortgage on one spouse's "
                         "pre-marriage flat may be entered as J or under that spouse), "
                         "or treat the debt as marital.")

    # Pool = balanceable assets of both spouses minus marital debts.
    gross_pool = held["A"] + held["B"]
    total_debt = debts["A"] + debts["B"]
    net_pool = gross_pool - total_debt
    half_share = net_pool / 2.0

    # Net position of each spouse: what they hold minus what they owe.
    net_a = held["A"] - debts["A"]
    net_b = held["B"] - debts["B"]

    # The spouse above the half share pays the difference down to equal halves.
    # A positive number means A pays B; a negative number means B pays A.
    payment_a_to_b = net_a - half_share

    return {
        "name_a": name_a,
        "name_b": name_b,
        "held": held,
        "excluded": excluded,
        "debts": debts,
        "excluded_debts": excluded_debts,
        "sole_excluded_debts": sole_excluded_debts,
        "gross_pool": gross_pool,
        "total_debt": total_debt,
        "net_pool": net_pool,
        "half_share": half_share,
        "net_a": net_a,
        "net_b": net_b,
        "payment_a_to_b": payment_a_to_b,
    }


def shekels(value):
    """Format a number as rounded shekels with thousands separators."""
    return "{:,} ILS".format(int(round(value)))


def print_worksheet(result):
    name_a = result["name_a"]
    name_b = result["name_b"]
    line = "-" * 56

    print(line)
    print("PROPERTY-BALANCING WORKSHEET (izun mashabim, section 5)")
    print("Arithmetic under the 50/50 default on YOUR classification of each item.")
    print("Not legal advice and not a determination of what anyone owes: a court")
    print("can vary it (section 8) and the classification itself is a lawyer question.")
    print(line)
    print("Balanceable assets held by %s: %s" % (name_a, shekels(result["held"]["A"])))
    print("Balanceable assets held by %s: %s" % (name_b, shekels(result["held"]["B"])))
    print("Excluded (kept by %s):        %s" % (name_a, shekels(result["excluded"]["A"])))
    print("Excluded (kept by %s):        %s" % (name_b, shekels(result["excluded"]["B"])))
    ex_debt = result["excluded_debts"]["A"] + result["excluded_debts"]["B"]
    if ex_debt:
        print("Debts on excluded assets, left out of the pool (s.6(a)): %s" % shekels(ex_debt))
    for side, name in (("A", name_a), ("B", name_b)):
        if result["sole_excluded_debts"][side] > 0 and result["excluded"][side] == 0:
            print("WARNING: %s alone owes %s marked as connected with an excluded asset, but"
                  % (name, shekels(result["sole_excluded_debts"][side])))
            print("holds no excluded asset. s.6(a) leaves out only a debt connected with an")
            print("asset whose value is not balanced. If it is not, the debt is marital and the")
            print("figure below moves by half of it.")
    if ex_debt > result["excluded"]["A"] + result["excluded"]["B"]:
        print("NOTE: the excluded debts exceed the excluded assets; the excess is also left")
        print("out of the balance. Whether marital money paid it down is a lawyer question.")
    print(line)
    print("Gross balanceable pool:       %s" % shekels(result["gross_pool"]))
    print("Marital debts netted:         %s" % shekels(result["total_debt"]))
    print("Net pool:                     %s" % shekels(result["net_pool"]))
    print("Each spouse's half share:     %s" % shekels(result["half_share"]))
    print(line)
    print("Net position of %s:           %s" % (name_a, shekels(result["net_a"])))
    print("Net position of %s:           %s" % (name_b, shekels(result["net_b"])))
    print(line)

    payment = result["payment_a_to_b"]
    if abs(payment) < 1:
        print("Default-rule arithmetic: both net positions already equal the half share.")
    elif payment > 0:
        print("Default-rule arithmetic: %s's net position exceeds the half share by %s"
              % (name_a, shekels(payment)))
    else:
        print("Default-rule arithmetic: %s's net position exceeds the half share by %s"
              % (name_b, shekels(-payment)))
    if result["net_a"] < 0 or result["net_b"] < 0 or result["net_pool"] < 0:
        print("WARNING: a spouse's debts exceed their balanceable assets. The payment")
        print("above applies the s.6(b) half-the-difference formula literally, which")
        print("makes the other spouse share that deficit. Courts do not do this")
        print("mechanically, especially for debts not taken for the family. Lawyer question.")
    print(line)
    print("Preparation tool only. Confirm classification and the settlement")
    print("with a family lawyer. Pension division goes to israeli-pension-advisor.")


def example_data():
    """A worked case: family home plus savings, one inheritance excluded."""
    return {
        "spouse_a": "Dana",
        "spouse_b": "Yossi",
        "assets": [
            {"label": "Family home", "owner": "A", "value": 1800000, "balanceable": True},
            {"label": "Joint savings", "owner": "B", "value": 300000, "balanceable": True},
            {"label": "Yossi car", "owner": "B", "value": 90000, "balanceable": True},
            {"label": "Dana inheritance", "owner": "A", "value": 400000, "balanceable": False},
        ],
        "debts": [
            {"label": "Mortgage", "owner": "A", "value": 900000},
        ],
    }


def parse_cli_items(asset_args, debt_args):
    """Parse repeated --asset and --debt flags into a data dict."""
    data = {"spouse_a": "Spouse A", "spouse_b": "Spouse B", "assets": [], "debts": []}
    for raw in asset_args or []:
        parts = raw.split(":")
        if len(parts) != 4:
            raise ValueError("--asset must be label:owner:value:balanceable|excluded")
        label, owner, value, flag = parts
        data["assets"].append({
            "label": label,
            "owner": owner,
            "value": value,
            "balanceable": parse_flag(flag, label, "balanceable"),
        })
    for raw in debt_args or []:
        parts = raw.split(":")
        if len(parts) not in (3, 4):
            raise ValueError("--debt must be label:owner:value[:excluded]")
        label, owner, value = parts[:3]
        excluded = False
        if len(parts) == 4:
            if parts[3].strip().lower() != "excluded":
                raise ValueError("--debt 4th field may only be 'excluded', got %r" % parts[3])
            excluded = True
        data["debts"].append({"label": label, "owner": owner, "value": value,
                              "excluded": excluded})
    return data


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Israeli property-balancing (izun mashabim) worksheet.")
    parser.add_argument("--example", action="store_true",
                        help="run a built-in worked example")
    parser.add_argument("--file", help="path to a JSON input file")
    parser.add_argument("--asset", action="append",
                        help="label:owner:value:balanceable|excluded (repeatable)")
    parser.add_argument("--debt", action="append",
                        help="label:owner:value (repeatable)")
    args = parser.parse_args(argv)

    if args.example:
        data = example_data()
    elif args.file:
        with open(args.file, "r", encoding="utf-8") as handle:
            data = json.load(handle)
    elif args.asset or args.debt:
        try:
            data = parse_cli_items(args.asset, args.debt)
        except ValueError as err:
            print("Input error: %s" % err, file=sys.stderr)
            return 2
    else:
        parser.print_help()
        return 1

    try:
        result = build_worksheet(data)
    except (ValueError, KeyError) as err:
        print("Input error: %s" % err, file=sys.stderr)
        return 2
    print_worksheet(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
