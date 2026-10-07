"""
Canada PI Case Assessment Memo client.

Thin wrapper around POST /canada/memo on the Specter API. Triggered when
the user's message starts with the word "Canada" (case-insensitive).

Returns a single markdown string — the memo as it should appear on
WhatsApp, verbatim.

Usage:
    from openclaw.skills.canada_memo.client import generate_memo
    memo = generate_memo("my child was playing soccer outside Target and got hurt")
    print(memo)
"""
from __future__ import annotations

import os
import re
import sys
from typing import Optional

import httpx

API_BASE = os.getenv("SPECTER_API", "http://127.0.0.1:8000").rstrip("/")
DEFAULT_TIMEOUT = 120.0  # memo + Claude can take 20s

# Match a leading "Canada" / "canada" / "CANADA" with optional separators after.
_CANADA_PREFIX_RE = re.compile(r"^\s*canada\b[\s,:.\-—–]*", re.IGNORECASE)


def starts_with_canada(message: str) -> bool:
    """Return True iff the user's message starts with 'Canada' (any case)."""
    return bool(_CANADA_PREFIX_RE.match(message or ""))


def strip_canada_prefix(message: str) -> str:
    """Drop the leading 'Canada' token + separators so we keep only the facts."""
    return _CANADA_PREFIX_RE.sub("", message or "").strip()


def generate_memo(facts: str, **filters) -> str:
    """
    POST the facts to /canada/memo and return the markdown memo.

    `filters` is forwarded as JSON keys; supported: treatment_gap, pre_existing,
    surveillance, contributory_negligence, municipal, plaintiff_won,
    defendant_type, court, year_min. Pass None / omit to skip a filter.
    """
    payload = {"facts": facts}
    # Only include filters with explicit values.
    for k, v in filters.items():
        if v is not None:
            payload[k] = v

    with httpx.Client(base_url=API_BASE, timeout=DEFAULT_TIMEOUT) as c:
        r = c.post("/canada/memo", json=payload)
        r.raise_for_status()
        data = r.json()
    return data.get("memo", "")


def whatif(original_facts: str, modified_facts: str,
           original_filters: Optional[dict] = None,
           modified_filters: Optional[dict] = None) -> str:
    """POST a what-if comparison to /canada/whatif and return the memo."""
    payload = {
        "original_facts": original_facts,
        "modified_facts": modified_facts,
    }
    if original_filters is not None:
        payload["original_filters"] = original_filters
    if modified_filters is not None:
        payload["modified_filters"] = modified_filters

    with httpx.Client(base_url=API_BASE, timeout=DEFAULT_TIMEOUT) as c:
        r = c.post("/canada/whatif", json=payload)
        r.raise_for_status()
        return r.json().get("memo", "")


def main() -> None:
    """CLI entry point used by `python3 -m openclaw.skills.canada_memo.client`."""
    if len(sys.argv) < 2:
        print("usage: python -m openclaw.skills.canada_memo.client \"<facts>\"", file=sys.stderr)
        print("       (the leading word 'Canada' is stripped automatically)", file=sys.stderr)
        sys.exit(2)

    raw = " ".join(sys.argv[1:])
    facts = strip_canada_prefix(raw) if starts_with_canada(raw) else raw
    print(generate_memo(facts))


if __name__ == "__main__":
    main()
