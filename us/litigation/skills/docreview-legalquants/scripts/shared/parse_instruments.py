#!/usr/bin/env python3
"""Parse enumerated legal instruments and optionally scaffold a framework."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

KINDS = ("rfp", "rfa", "srog", "issues-list")
REQUEST_HEADING = re.compile(
    r"^[ \t]*(?P<label>"
    r"REQUEST[ \t]+FOR[ \t]+PRODUCTION|"
    r"REQUEST[ \t]+FOR[ \t]+ADMISSION|"
    r"SPECIAL[ \t]+INTERROGATORY"
    r")[ \t]+NO\.?[ \t]*(?P<number>[^ \t\r\n.:]+)"
    r"[ \t]*[.:]?(?:[ \t]+(?P<text>[^ \t\r\n][^\r\n]*))?[ \t]*\r?$",
    re.IGNORECASE | re.MULTILINE,
)
ISSUE_HEADING = re.compile(
    r"^[ \t]*(?P<number>[0-9]+)[.)][ \t]+(?P<text>[^\r\n]+?)[ \t]*\r?$",
    re.MULTILINE,
)
LABEL_KIND = {
    "request for production": "rfp",
    "request for admission": "rfa",
    "special interrogatory": "srog",
}
PLAIN_DESIGNATOR = re.compile(r"[1-9][0-9]*")
COMPOUND_DESIGNATOR = re.compile(r"(?P<series>[A-Z]+)-(?P<number>[1-9][0-9]*)")
HIT_RULE = (
    "a document or category the request describes by its plain terms, "
    "including drafts and attachments"
)
UNRESOLVED_WHEN = "The request cannot be resolved from the available document text."
ANSWER_TEMPLATE = "STATUS: responsive to the request by its plain terms (QUOTE)."


class InstrumentError(ValueError):
    pass


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(value, indent=2, sort_keys=True) + "\n")


def slug(stem: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", stem.casefold()).strip("-")


def read_exact_text(path: Path) -> str:
    try:
        with path.open(encoding="utf-8", newline="") as handle:
            return handle.read()
    except (OSError, UnicodeDecodeError) as error:
        raise InstrumentError(
            f"{path.name}: cannot read UTF-8 input ({error})"
        ) from error


def strip_outer_blank_lines(value: str) -> str:
    lines = value.splitlines(keepends=True)
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "".join(lines).rstrip("\r\n")


def request_kind(label: str) -> str:
    normalized = " ".join(label.casefold().split())
    return LABEL_KIND[normalized]


def parse_designator(token: str):
    plain = PLAIN_DESIGNATOR.fullmatch(token)
    if plain:
        series = None
        number = int(token)
    else:
        compound = COMPOUND_DESIGNATOR.fullmatch(token)
        if compound is None:
            raise InstrumentError(f"unsupported request designator {token}")
        series = compound.group("series")
        number = int(compound.group("number"))
    reconstructed = f"{series}-{number}" if series is not None else str(number)
    if reconstructed != token:
        raise InstrumentError(f"request designator does not round-trip: {token}")
    return series, number


def element_designator(series, number):
    return f"{series}-{number}" if series is not None else str(number)


def elements_from_matches(text: str, matches: list[re.Match[str]], issues: bool):
    elements = []
    seen = set()
    for index, match in enumerate(matches):
        if issues:
            series = None
            number = int(match.group("number"))
        else:
            series, number = parse_designator(match.group("number"))
        identity = (series, number)
        if identity in seen:
            if series is None:
                raise InstrumentError(f"duplicate element number {number}")
            raise InstrumentError(
                f"duplicate element designator {element_designator(series, number)}"
            )
        seen.add(identity)
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        tail = strip_outer_blank_lines(text[match.end() : end])
        inline = match.groupdict().get("text")
        inline = inline.strip() if inline else ""
        body = inline if not tail else inline + "\n" + tail
        if not inline:
            body = tail
        if not body.strip():
            raise InstrumentError(f"element {number} has no text")
        element = {"no": number, "text": body}
        if series is not None:
            element["series"] = series
        elements.append(element)
    return elements


def parse_one(path: Path, override: str | None):
    text = read_exact_text(path)
    heading_matches = list(REQUEST_HEADING.finditer(text))
    invalid_designators = []
    for match in heading_matches:
        token = match.group("number")
        if not (
            PLAIN_DESIGNATOR.fullmatch(token) or COMPOUND_DESIGNATOR.fullmatch(token)
        ):
            invalid_designators.append(token)
    if invalid_designators:
        raise InstrumentError(
            "{}: unsupported request designator(s): {}".format(
                path.name, ", ".join(invalid_designators)
            )
        )
    request_matches = heading_matches
    kinds = {request_kind(match.group("label")) for match in request_matches}
    if len(kinds) > 1:
        raise InstrumentError(
            f"{path.name}: mixed instrument kinds ({', '.join(sorted(kinds))})"
        )
    if request_matches:
        kind = next(iter(kinds))
        if override is not None and override != kind:
            raise InstrumentError(
                f"{path.name}: --kind {override} conflicts with recognized "
                f"{kind} headings"
            )
        matches = request_matches
        issues = False
    elif override == "issues-list":
        kind = override
        matches = list(ISSUE_HEADING.finditer(text))
        issues = True
        if not matches:
            raise InstrumentError(
                f"{path.name}: --kind issues-list supplied but no numbered items found"
            )
    elif override is not None:
        raise InstrumentError(
            f"{path.name}: --kind {override} supplied but no matching headings found"
        )
    else:
        raise InstrumentError(
            f"{path.name}: unclassified input; supply a recognized served heading "
            "or an explicit --kind FILE=issues-list override"
        )
    try:
        elements = elements_from_matches(text, matches, issues)
    except InstrumentError as error:
        raise InstrumentError(f"{path.name}: {error}") from error
    instrument_id = slug(path.stem)
    if not instrument_id or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", instrument_id):
        raise InstrumentError(f"{path.name}: cannot derive a valid instrument_id")
    return {
        "elements": elements,
        "instrument_id": instrument_id,
        "kind": kind,
        "label": path.name,
        "party": None,
        "set": None,
        "staged": False,
    }


def parse_overrides(values: list[str]):
    overrides = {}
    errors = []
    for value in values:
        if "=" not in value:
            errors.append(f"--kind value must be FILE=KIND: {value}")
            continue
        raw_path, kind = value.rsplit("=", 1)
        if kind not in KINDS:
            errors.append(f"--kind for {raw_path} has unsupported kind {kind!r}")
            continue
        key = str(Path(raw_path).expanduser().resolve())
        if key in overrides:
            errors.append(f"duplicate --kind override for {raw_path}")
        overrides[key] = kind
    if errors:
        raise InstrumentError("; ".join(errors))
    return overrides


def build_census(paths: list[str], raw_overrides: list[str]):
    overrides = parse_overrides(raw_overrides)
    instruments = []
    errors = []
    seen_paths = set()
    for raw in paths:
        path = Path(raw).expanduser().resolve()
        key = str(path)
        if key in seen_paths:
            errors.append(f"{path.name}: input listed more than once")
            continue
        seen_paths.add(key)
        if not path.is_file():
            errors.append(f"{path.name}: input is not a file")
            continue
        try:
            instruments.append(parse_one(path, overrides.get(key)))
        except InstrumentError as error:
            errors.append(str(error))
    unused = sorted(set(overrides) - seen_paths)
    errors.extend(
        f"{Path(path).name}: --kind override names no input" for path in unused
    )
    ids = {}
    for instrument in instruments:
        instrument_id = instrument["instrument_id"]
        if instrument_id in ids:
            errors.append(
                f"instrument-ID slug collision: {ids[instrument_id]} and "
                f"{instrument['label']} both map to {instrument_id}"
            )
        ids[instrument_id] = instrument["label"]
    if errors:
        raise InstrumentError("\n".join(errors))
    instruments.sort(key=lambda item: item["instrument_id"])
    by_kind = {}
    for instrument in instruments:
        by_kind[instrument["kind"]] = by_kind.get(instrument["kind"], 0) + len(
            instrument["elements"]
        )
    return {
        "counts": {
            "by_kind": by_kind,
            "elements": sum(by_kind.values()),
            "instruments": len(instruments),
        },
        "instruments": instruments,
    }


def load_census(path: str):
    try:
        with open(path, encoding="utf-8") as handle:
            value = json.load(handle)
    except (OSError, json.JSONDecodeError) as error:
        raise InstrumentError(f"cannot read instruments at {path}: {error}") from error
    if not isinstance(value, dict) or not isinstance(value.get("instruments"), list):
        raise InstrumentError(f"{path}: invalid instruments.json")
    return value


def scaffold(census, frame_id: str, corpus_id: str, purpose: str, compile_kinds):
    compiled = set(compile_kinds)
    frame_instruments = []
    lenses = []
    source_inputs = []
    for instrument in census["instruments"]:
        is_compiled = instrument["kind"] in compiled
        frame_instruments.append(
            {
                "element_count": len(instrument["elements"]),
                "instrument_id": instrument["instrument_id"],
                "kind": instrument["kind"],
                "label": instrument["label"],
                "party": instrument.get("party"),
                "set": instrument.get("set"),
                "staged": not is_compiled,
            }
        )
        source_inputs.append({"kind": instrument["kind"], "label": instrument["label"]})
        if not is_compiled:
            continue
        items = []
        for element in instrument["elements"]:
            series = element.get("series")
            suffix = (
                f"{series.lower()}{element['no']:03d}"
                if series is not None
                else f"{element['no']:03d}"
            )
            target_ref = {
                "element": element["no"],
                "instrument_id": instrument["instrument_id"],
            }
            if series is not None:
                target_ref["series"] = series
            items.append(
                {
                    "answer_shape": {
                        "characterization_max_words": 40,
                        "statuses": ["present", "absent", "unresolved"],
                        "template": ANSWER_TEMPLATE,
                    },
                    "disposition": "report",
                    "evidence": {
                        "required": "verbatim quote plus section reference",
                        "unresolved_when": UNRESOLVED_WHEN,
                    },
                    "exclusions": [],
                    "hit_rule": HIT_RULE,
                    "issue_id": f"{instrument['instrument_id']}-{suffix}",
                    "materiality": {"bands": [], "default": "medium"},
                    "overlap_owner": None,
                    "question": element["text"],
                    "target_ref": target_ref,
                }
            )
        lenses.append(
            {
                "items": items,
                "lens_id": instrument["instrument_id"],
                "name": instrument["label"],
            }
        )
    if not lenses:
        raise InstrumentError("--compile-kinds selected no instruments")
    return {
        "approved": False,
        "frame": {
            "corpus_id": corpus_id,
            "frame_id": frame_id,
            "instruments": frame_instruments,
            "kind": "requests",
            "purpose": purpose,
        },
        "framework_version": 1,
        "lenses": lenses,
        "source_inputs": source_inputs,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", nargs="+", default=None)
    parser.add_argument("--instruments", default=None)
    parser.add_argument(
        "--kind",
        action="append",
        default=[],
        metavar="FILE=KIND",
        help="Explicit per-file classification; issues-list requires this override.",
    )
    parser.add_argument("--scaffold", action="store_true")
    parser.add_argument("--frame-id")
    parser.add_argument("--corpus-id")
    parser.add_argument("--purpose", choices=("receiving-audit", "producing-review"))
    parser.add_argument("--compile-kinds", nargs="+", choices=KINDS)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    try:
        if bool(args.inputs) == bool(args.instruments):
            raise InstrumentError("supply exactly one of --inputs or --instruments")
        if args.instruments:
            if args.kind:
                raise InstrumentError("--kind applies only with --inputs")
            census = load_census(args.instruments)
        else:
            census = build_census(args.inputs, args.kind)
        if args.scaffold:
            missing = [
                name
                for name, value in (
                    ("--frame-id", args.frame_id),
                    ("--corpus-id", args.corpus_id),
                    ("--purpose", args.purpose),
                    ("--compile-kinds", args.compile_kinds),
                )
                if not value
            ]
            if missing:
                raise InstrumentError("--scaffold requires " + ", ".join(missing))
            if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", args.frame_id):
                raise InstrumentError("--frame-id must be a lowercase slug")
            if not re.fullmatch(r"[0-9a-f]{16}", args.corpus_id):
                raise InstrumentError("--corpus-id must be 16 lowercase hex characters")
            value = scaffold(
                census,
                args.frame_id,
                args.corpus_id,
                args.purpose,
                args.compile_kinds,
            )
        else:
            if any(
                value
                for value in (
                    args.frame_id,
                    args.corpus_id,
                    args.purpose,
                    args.compile_kinds,
                )
            ):
                raise InstrumentError("scaffold options require --scaffold")
            value = census
        dump(Path(args.out), value)
    except InstrumentError as error:
        print(f"parse_instruments: {error}", file=sys.stderr)
        sys.exit(1)

    if args.scaffold:
        items = sum(len(lens["items"]) for lens in value["lenses"])
        print(
            f"wrote {args.out}: {len(value['lenses'])} compiled instrument(s), "
            f"{items} item(s)"
        )
    else:
        print(
            f"wrote {args.out}: {value['counts']['instruments']} instrument(s), "
            f"{value['counts']['elements']} element(s)"
        )


if __name__ == "__main__":
    main()
