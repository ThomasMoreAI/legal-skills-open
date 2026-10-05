"""Deterministic gate for a /pressuretest method-v2.8 deliverable.

Stdlib only. Invoke with a direct, quoted path (works from any directory):

    python "<skill root>/scripts/validate_deliverable.py" DELIVERABLE.json \
        --source-root ROOT [--brief BRIEF.md]

Exit codes:
    0  contract satisfied (counts and derived verdict on stdout as JSON)
    1  contract fault in the deliverable itself -- fix the output and rerun
    2  operational fault (missing/unreadable root or source) -- deliver with
       the honest downgrade line; do not simulate a pass. A run without
       --source-root always exits 2 by design: structural checks only.

The validator re-derives the verdict from the findings table, checks coverage
arithmetic and containment, checks normalised quote occurrence in its named
reviewed source (not pinpoint accuracy or entailment), and, when --brief is
given, binds the exported brief to the companion: the plain-English verdict
line mapped from the machine verdict, Pressure Point IDs, the document
shape ('What this document is' and 'How this review was done' sections,
the at-a-glance table header for the verdict, the verbatim closing
sentence), a ban on machine vocabulary outside fenced code blocks, a ban
on process telemetry, and -- on position_holds -- the impact-vocabulary
ban. Two v2.7 contract rules: a position flagged as depending on the other
party's breach must have at least one adjudicated attack in the causation
test family, and two breaks_position findings may not share a flip
statement (the standard does not move after the first Pressure Point).
v2.8 adds the rendered-brief contract: the companion carries a `brief`
object with the prose the renderer needs, every finding has a title, and
every Pressure Point carries hits / test_applied / next_step. The
checkpoint may precede the full read: the companion's `checkpoint` block
records which selected documents had been read when the map was shown
(and any change the full read forced), the docket must state what had
been read, and the receipt discloses both.

Native text: .md/.txt/UTF-8 files, plus .docx (stdlib extraction). Other
binary formats (e.g. PDF) leave their anchors unverified and are reported
per-anchor as an operational limitation, never as a pass.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
import zipfile
from pathlib import Path

from result_contract import METHOD_VERSION as CHAT_METHOD_VERSION
from result_contract import check_result, presentation_faults

METHOD_VERSION = "lq.pressuretest.method.v2.8"
PP_CLASSES = {"breaks_position", "internal_defect"}
CLASSIFICATIONS = PP_CLASSES | {"defeated", "weakens_route", "proof_gap", "context"}
VERDICTS = {"pressure_points", "position_holds", "incomplete"}
# The brief is written for a lawyer: it must contain the canonical
# plain-English verdict line for the companion's machine verdict (the
# pressure_points line depends on whether any finding breaks the position),
# and the method's machine vocabulary must not appear in it outside fenced
# code blocks. The fence stripper is deliberately simple: an unclosed
# ``` fence or an indented (non-fenced) code block is NOT exempt, so
# tokens there still fault — fail-strict by design.
PLAIN_VERDICT_LINES = {
    "pressure_points_breaks": "the position does not hold as stated — pressure points found",  # noqa: E501
    "pressure_points_internal": "the conclusion survives on the supplied documents, but the position as drafted contradicts itself — pressure points found",  # noqa: E501
    "position_holds": "the position holds on the supplied documents",
    "incomplete": "this review is incomplete",
}
MACHINE_TOKENS = re.compile(
    r"\b(pressure_points|position_holds|breaks_position|internal_defect"
    r"|weakens_route|proof_gap|machine_proposed)\b",
    re.IGNORECASE,
)
# Document shape of the exported brief (Step 7): a self-introducing
# section, an at-a-glance table before the detail, and a closing receipt.
# Matched on whitespace-collapsed, emphasis-stripped, lowercased text.
REQUIRED_SECTIONS = {
    "brief_missing_intro_section": "what this document is",
    "brief_missing_receipt_section": "how this review was done",
}
# The closing sentence, required verbatim (matched on whitespace-collapsed,
# emphasis-stripped, dash-normalised, lowercased text).
CLOSING_SENTENCE = (
    "this review can only test the routes it identified - anything it did "
    "not identify remains untested. it does not verify cited authorities "
    "or certify the position."
)
# Process telemetry belongs to the machinery, never to a document a client
# may read.
BANNED_TELEMETRY = re.compile(
    r"answered\s+['\"‘“]?go\b"
    r"|\bactive\s+mode\b"
    r"|\binteractive\s+checkpoint\b"
    r"|routes\s+the\s+map\s+failed\s+to\s+identify",
    re.IGNORECASE,
)
SUMMARY_TABLE_HEADERS = {
    "pressure_points": "| # | finding | whose case it hits | how serious | where |",  # noqa: E501
    "position_holds": "| # | attack tested | outcome | answered by |",
}
MODES = {"fast", "deep"}
BASES = {"instructed", "inferred"}
BRIEF_FIELDS = (
    "position_name",
    "run_date",
    "what_this_is",
    "meaning",
    "summary",
    "document_key",
    "scope_confirmation",
    "established",
    "follows",
)
PP_PROSE_FIELDS = ("hits", "test_applied", "next_step")
DOCKET_READ_LIST = re.compile(r"read\s+so\s+far\s*:", re.IGNORECASE)
TEST_FAMILIES = {
    "logic",
    "arithmetic-and-dates",
    "definitions-and-precedence",
    "mechanics",
    "consistency",
    "causation",
    "counterfactual",
    "other",
}
MIN_QUOTE_LEN = 6
# Impact vocabulary banned in the author's own prose outside Pressure Points.
# Quoted spans are stripped before scanning so defined terms from the sources
# ("material defect" carve-outs etc.) can be discussed in quotes.
BANNED_IMPACT = re.compile(
    r"load[- ]bearing"
    r"|material\s+(defect|finding|pressure\s+point|inconsisten)"
    r"|fatal(ly)?\b"
    r"|dispositive"
    r"|\bdefect(ive|s)?\b"
    r"|(materially|fundamentally|critically)\s+undermin",
    re.IGNORECASE,
)
QUOTED_SPAN = re.compile(r'"[^"\n]*"|“[^”\n]*”|‘[^’\n]*’|\'[^\'\n]*\'|`[^`\n]*`')

_QUOTE_MAP = str.maketrans(
    {
        "‘": "'",
        "’": "'",
        "“": '"',
        "”": '"',
        "–": "-",
        "—": "-",
        " ": " ",
    }
)
_DOCX_TAG = re.compile(r"<[^>]+>")


def normalise(text: str) -> str:
    text = unicodedata.normalize("NFC", text).translate(_QUOTE_MAP)
    return re.sub(r"\s+", " ", text).strip()


def strip_quoted(text: str) -> str:
    return QUOTED_SPAN.sub(" ", text)


def read_source_text(path: Path) -> str:
    """Return normalised text for a source file. Raises on unsupported bytes."""
    if path.suffix.lower() == ".docx":
        with zipfile.ZipFile(path) as zf:
            xml = zf.read("word/document.xml").decode("utf-8", errors="strict")
        # paragraph and break tags become spaces before tag stripping
        xml = re.sub(r"</w:p>|<w:br[^>]*/>|<w:tab[^>]*/>", " ", xml)
        return normalise(_DOCX_TAG.sub("", xml))
    return normalise(path.read_text(encoding="utf-8", errors="strict"))


class Report:
    def __init__(self) -> None:
        self.faults: list[dict] = []  # contract faults -> exit 1
        self.operational: list[dict] = []  # operational faults -> exit 2
        self.anchors_verified = 0
        self.anchors_unverified: list[str] = []

    def fault(self, code: str, detail: str) -> None:
        self.faults.append({"code": code, "detail": detail})

    def op(self, code: str, detail: str) -> None:
        self.operational.append({"code": code, "detail": detail})


def as_str_list(value, where: str, rep: Report) -> list[str]:
    if not isinstance(value, list) or not all(isinstance(x, str) and x for x in value):
        rep.fault("bad_list", f"{where} must be a list of non-empty strings")
        return []
    return value


def contained(root: Path, name: str) -> Path | None:
    """Resolve name under root; None if it escapes or is absolute."""
    if Path(name).is_absolute():
        return None
    candidate = (root / name).resolve()
    try:
        if candidate.is_relative_to(root.resolve()):
            return candidate
    except ValueError:
        pass
    return None


def check_anchor(
    anchor, where: str, reviewed: set[str], root: Path | None, cache: dict, rep: Report
) -> None:
    if (
        not isinstance(anchor, dict)
        or not isinstance(anchor.get("source"), str)
        or not isinstance(anchor.get("quote"), str)
    ):
        rep.fault("bad_anchor", f"{where}: anchor needs string 'source' and 'quote'")
        return
    source, quote = anchor["source"], anchor["quote"]
    if source not in reviewed:
        rep.fault(
            "anchor_source_not_reviewed",
            f"{where}: {source} is not in coverage.reviewed (anchors may cite reviewed sources only)",  # noqa: E501
        )
        return
    if len(normalise(quote)) < MIN_QUOTE_LEN:
        rep.fault(
            "anchor_quote_too_short", f"{where}: quote under {MIN_QUOTE_LEN} chars"
        )
        return
    if root is None:
        rep.anchors_unverified.append(f"{where}: no source root")
        return
    if source not in cache:
        path = contained(root, source)
        if path is None:
            rep.fault(
                "anchor_source_escapes_root",
                f"{where}: {source} is outside the source root",
            )
            cache[source] = None
            return
        try:
            cache[source] = read_source_text(path)
        except (OSError, UnicodeDecodeError, zipfile.BadZipFile, KeyError) as exc:
            rep.op(
                "source_unreadable_for_anchor_check", f"{source}: {type(exc).__name__}"
            )
            cache[source] = None
    text = cache[source]
    if text is None:
        rep.anchors_unverified.append(f"{where}: {source} unverifiable")
    elif normalise(quote) not in text:
        rep.fault("anchor_not_found", f"{where}: quote not found in {source}")
    else:
        rep.anchors_verified += 1


def scan_prose(obj, where: str, rep: Report) -> None:
    """Ban impact vocabulary in non-PP finding prose (anchor quotes exempt)."""  # noqa: E501
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "anchors" and isinstance(value, list):
                for i, anchor in enumerate(value):
                    if isinstance(anchor, dict):
                        loc = anchor.get("locator")
                        if isinstance(loc, str) and BANNED_IMPACT.search(
                            strip_quoted(loc)
                        ):
                            rep.fault(
                                "impact_vocabulary", f"{where}.anchors[{i}].locator"
                            )
            else:
                scan_prose(value, f"{where}.{key}", rep)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            scan_prose(item, f"{where}[{i}]", rep)
    elif isinstance(obj, str):
        if BANNED_IMPACT.search(strip_quoted(obj)):
            rep.fault(
                "impact_vocabulary",
                f"{where}: impact vocabulary in a non-Pressure-Point finding",
            )


def check_brief(
    brief_path: Path,
    declared: str,
    pp_ids: list[str],
    has_breaks: bool,
    rep: Report,
) -> None:
    try:
        brief = brief_path.read_text(encoding="utf-8")
    except OSError as exc:
        rep.fault("brief_missing", str(exc))
        return
    if declared == "pressure_points":
        key = "pressure_points_breaks" if has_breaks else "pressure_points_internal"
    else:
        key = declared
    plain = PLAIN_VERDICT_LINES[key]
    # Markdown emphasis around or inside the line is style, not a fault:
    # drop * and _ before matching (machine tokens would lose their
    # underscores here, but they cannot satisfy the plain phrase anyway).
    searchable = normalise(brief.replace("*", "").replace("_", ""))
    verdict_line = re.compile(
        r"verdict\s*[:—-]\s*`?\s*" + re.escape(normalise(plain)),
        re.IGNORECASE,
    )
    if not verdict_line.search(searchable):
        rep.fault(
            "brief_verdict_line",
            f"brief must contain the line 'Verdict: {plain}.' verbatim "
            f"(plain-English line for the {declared!r} verdict)",
        )
    no_code = re.sub(r"```.*?```", " ", brief, flags=re.DOTALL)
    token = MACHINE_TOKENS.search(no_code)
    if token:
        rep.fault(
            "brief_machine_tokens",
            "machine vocabulary belongs in deliverable.json, not the brief: "
            f"{token.group(0)!r}",
        )
    low = searchable.lower()
    for fault_code, needle in REQUIRED_SECTIONS.items():
        if needle not in low:
            rep.fault(
                fault_code,
                f"brief must contain a '{needle.title()}' section "
                "(exported-document shape, Step 7)",
            )
    table_header = SUMMARY_TABLE_HEADERS.get(declared)
    if table_header and table_header not in low:
        rep.fault(
            "brief_missing_summary_table",
            "brief must contain the at-a-glance table for the "
            f"{declared!r} verdict, headed exactly: {table_header}",
        )
    if CLOSING_SENTENCE not in low:
        rep.fault(
            "brief_missing_closing_sentence",
            "brief must end with the verbatim closing sentence "
            "(Step 7: 'This review can only test the routes it "
            "identified ...')",
        )
    leak = BANNED_TELEMETRY.search(no_code)
    if leak:
        rep.fault(
            "brief_process_telemetry",
            "process telemetry belongs to the machinery, not the exported "
            f"document: {leak.group(0)!r}",
        )
    for pid in pp_ids:
        if pid not in brief:
            rep.fault(
                "brief_missing_pressure_point",
                f"Pressure Point {pid} absent from brief",
            )
    if declared == "position_holds":
        # a resilience brief must not read as an attack: ban impact vocabulary
        # outside quoted spans and fenced code
        stripped = re.sub(r"```.*?```", " ", brief, flags=re.DOTALL)
        stripped = strip_quoted(stripped)
        match = BANNED_IMPACT.search(stripped)
        if match:
            rep.fault(
                "brief_impact_vocabulary",
                f"position_holds brief contains impact vocabulary: {match.group(0)!r}",
            )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("deliverable")
    parser.add_argument("--source-root", default=None)
    parser.add_argument("--brief", default=None)
    parser.add_argument("--html", default=None, help="exact HTML report to check")
    parser.add_argument(
        "--handoff", default=None, help="exact short chat summary to check"
    )
    parser.add_argument(
        "--chat", default=None, help="exact native-chat output to check"
    )
    parser.add_argument(
        "--docket",
        default=None,
        help="Interim docket file: checked for impact vocabulary, verdicts and asserted findings; never part of the export.",  # noqa: E501
    )
    args = parser.parse_args(argv)

    rep = Report()

    try:
        data = json.loads(Path(args.deliverable).read_text(encoding="utf-8"))
    except OSError as exc:
        rep.fault("deliverable_missing", str(exc))
        return finish(rep, None)
    except json.JSONDecodeError as exc:
        rep.fault("deliverable_not_json", str(exc))
        return finish(rep, None)

    root: Path | None = None
    if args.source_root is None:
        rep.op(
            "no_source_root",
            "structural validation only (exit 2 by design); anchors not verified",
        )
    else:
        root = Path(args.source_root)
        if not root.is_dir():
            rep.op("source_root_missing", str(root))
            root = None

    chat_method = data.get("method_version") == CHAT_METHOD_VERSION
    if data.get("method_version") not in (METHOD_VERSION, CHAT_METHOD_VERSION):
        rep.fault("method_version", f"expected {METHOD_VERSION!r}")
    if data.get("verdict") not in VERDICTS:
        rep.fault("bad_verdict", f"verdict must be one of {sorted(VERDICTS)}")
    if data.get("mode") not in MODES:
        rep.fault("bad_mode", f"mode must be one of {sorted(MODES)}")
    positions = data.get("positions")
    owners: set[str] = set()
    breach_dependent: set[str] = set()
    if not isinstance(positions, list) or not positions:
        rep.fault(
            "missing_positions",
            "positions must be a non-empty list of tested positions",
        )
    else:
        for i, p in enumerate(positions):
            where = f"positions[{i}]"
            if not isinstance(p, dict):
                rep.fault("bad_position", f"{where} must be an object")
                continue
            owner = p.get("owner")
            if not isinstance(owner, str) or not owner.strip():
                rep.fault("missing_position_owner_field", f"{where}.owner required")
            elif owner in owners:
                rep.fault("duplicate_position_owner", owner)
            else:
                owners.add(owner)
            if (
                not isinstance(p.get("conclusion"), str)
                or not p.get("conclusion", "").strip()
            ):
                rep.fault("missing_position_conclusion", f"{where}.conclusion required")
            if p.get("basis") not in BASES:
                rep.fault(
                    "bad_position_basis",
                    f"{where}.basis must be one of {sorted(BASES)}",
                )
            depends = p.get("depends_on_other_party_breach")
            if not isinstance(depends, bool):
                rep.fault(
                    "missing_breach_dependency_flag",
                    f"{where}.depends_on_other_party_breach must be true or false",
                )
            elif depends and isinstance(owner, str) and owner.strip():
                breach_dependent.add(owner)

    # --- brief prose (rendered by render_brief.py) ---------------------------
    brief = data.get("brief")
    if chat_method:
        rep.faults.extend(presentation_faults(data))
    elif not isinstance(brief, dict):
        rep.fault("missing_brief", "brief object required (Step 7 prose fields)")
    else:
        for field in BRIEF_FIELDS:
            if not brief.get(field):
                rep.fault("missing_brief_field", f"brief.{field} required")

    # --- coverage partition and containment --------------------------------
    cov = data.get("coverage") or {}
    selected = as_str_list(cov.get("selected", []), "coverage.selected", rep)
    parts = {
        k: as_str_list(cov.get(k, []), f"coverage.{k}", rep)
        for k in ("reviewed", "parked", "excluded", "unreadable")
    }
    sel_set = set(selected)
    if len(selected) != len(sel_set):
        rep.fault("coverage_duplicates", "coverage.selected contains duplicates")
    union: list[str] = sum(parts.values(), [])
    if len(union) != len(set(union)) or set(union) != sel_set:
        rep.fault(
            "coverage_partition",
            "selected must equal the disjoint union of reviewed/parked/excluded/unreadable",  # noqa: E501
        )
    if root is not None:
        for name in selected:
            path = contained(root, name)
            if path is None:
                rep.fault("selected_escapes_root", f"coverage.selected: {name}")
            elif not path.is_file():
                rep.fault(
                    "selected_not_found",
                    f"coverage.selected: {name} does not exist under root",
                )

    reviewed_set = set(parts["reviewed"])

    # --- checkpoint: what had been read when the map was shown -----------------
    checkpoint = data.get("checkpoint")
    if not isinstance(checkpoint, dict):
        rep.fault(
            "missing_checkpoint",
            "checkpoint object required: map_read (documents read when the map "
            "was shown) and map_changed_after_full_read",
        )
    else:
        map_read = as_str_list(
            checkpoint.get("map_read", []), "checkpoint.map_read", rep
        )
        if not map_read:
            rep.fault(
                "checkpoint_map_read_empty",
                "the map must rest on at least one read document",
            )
        for name in map_read:
            if name not in sel_set:
                rep.fault(
                    "checkpoint_map_read_unknown",
                    f"checkpoint.map_read: {name} is not a selected document",
                )
        changed = checkpoint.get("map_changed_after_full_read")
        if not isinstance(changed, bool):
            rep.fault(
                "bad_checkpoint_flag",
                "checkpoint.map_changed_after_full_read must be true or false",
            )
        elif changed and not str(checkpoint.get("change_note", "")).strip():
            rep.fault(
                "missing_change_note",
                "checkpoint.change_note required when the full read changed the map",
            )

    # --- routes and tests ---------------------------------------------------
    routes = data.get("routes") or {}
    r_parts = {
        k: as_str_list(routes.get(k, []), f"routes.{k}", rep)
        for k in ("tested", "parked", "indeterminate")
    }
    r_union = sum(r_parts.values(), [])
    if len(r_union) != len(set(r_union)):
        rep.fault(
            "route_overlap", "routes tested/parked/indeterminate must be disjoint"
        )
    tests = data.get("tests") or {}
    t_applied = as_str_list(tests.get("applied", []), "tests.applied", rep)
    t_parked = as_str_list(tests.get("parked", []), "tests.parked", rep)

    # --- strongest route ----------------------------------------------------
    cache: dict = {}
    route = data.get("strongest_route") or {}
    if (
        not isinstance(route.get("summary"), str)
        or not route.get("summary", "").strip()
    ):
        rep.fault("missing_route_summary", "strongest_route.summary is required")
    route_anchors = route.get("anchors") or []
    if not route_anchors:
        rep.fault("missing_route_anchors", "strongest_route needs at least one anchor")
    for i, anchor in enumerate(route_anchors):
        check_anchor(
            anchor, f"strongest_route.anchors[{i}]", reviewed_set, root, cache, rep
        )

    # --- findings -------------------------------------------------------------
    findings = data.get("findings")
    if not isinstance(findings, list):
        rep.fault("bad_findings", "findings must be a list")
        findings = []
    seen_ids: set[str] = set()
    pp_ids: list[str] = []
    class_counts: dict[str, int] = {}
    causation_seen: set[str] = set()
    flip_seen: dict[str, str] = {}
    for i, f in enumerate(findings):
        where = f"findings[{i}]"
        if not isinstance(f, dict):
            rep.fault("bad_finding", f"{where} must be an object")
            continue
        fid = f.get("id")
        if not isinstance(fid, str) or not fid:
            rep.fault("missing_finding_id", where)
            fid = None
        elif fid in seen_ids:
            rep.fault("duplicate_finding_id", fid)
        else:
            seen_ids.add(fid)
        cls = f.get("classification")
        if cls not in CLASSIFICATIONS:
            rep.fault("bad_classification", f"{where}: {cls!r}")
            continue
        class_counts[cls] = class_counts.get(cls, 0) + 1
        owner = f.get("position_owner")
        owner_valid = isinstance(owner, str) and owner in owners
        if not isinstance(owner, str) or not owner.strip():
            rep.fault("missing_position_owner", where)
        elif not owner_valid:
            rep.fault("unknown_position_owner", f"{where}: {owner!r}")
        against = f.get("against_position")
        if cls in PP_CLASSES or "against_position" in f:
            if not isinstance(against, str) or against not in owners:
                rep.fault(
                    "bad_against_position",
                    f"{where}: against_position must name a tested position owner",
                )
                owner_valid = False
            elif against != owner:
                rep.fault(
                    "position_owner_mismatch",
                    f"{where}: against_position must equal position_owner",
                )
                owner_valid = False
        if (
            not isinstance(f.get("statement"), str)
            or not f.get("statement", "").strip()
        ):
            rep.fault("missing_statement", where)
        if not str(f.get("title", "")).strip():
            rep.fault("missing_finding_title", f"{where}: title required")
        test_name = f.get("test")
        if test_name is not None and test_name not in t_applied:
            rep.fault(
                "unlisted_test", f"{where}: test {test_name!r} not in tests.applied"
            )
        family = f.get("test_family")
        if family is not None and family not in TEST_FAMILIES:
            rep.fault(
                "bad_test_family",
                f"{where}: test_family must be one of {sorted(TEST_FAMILIES)}",
            )
        elif family == "causation" and owner_valid:
            causation_seen.add(owner)
        anchors = f.get("anchors") or []
        if not anchors:
            rep.fault("missing_anchors", where)
        for j, anchor in enumerate(anchors):
            check_anchor(
                anchor, f"{where}.anchors[{j}]", reviewed_set, root, cache, rep
            )
        if cls in PP_CLASSES:
            if fid:
                pp_ids.append(fid)
            if not str(f.get("survives", "")).strip():
                rep.fault("missing_survives", f"{where}: {cls} requires survives")
            for field in PP_PROSE_FIELDS:
                if not str(f.get(field, "")).strip():
                    rep.fault(
                        "missing_pressure_point_prose",
                        f"{where}: {cls} requires {field}",
                    )
            if cls == "breaks_position":
                flip = normalise(str(f.get("flip_statement", ""))).lower()
                if not flip:
                    rep.fault(
                        "missing_flip_statement",
                        f"{where}: breaks_position requires flip_statement",
                    )
                elif flip in flip_seen:
                    rep.fault(
                        "duplicate_flip_statement",
                        f"{where}: same flip statement as {flip_seen[flip]} - "
                        "one Pressure Point, not two",
                    )
                else:
                    flip_seen[flip] = fid or where
            if cls == "internal_defect":
                if len(anchors) < 2:
                    rep.fault(
                        "internal_defect_needs_two_anchors",
                        f"{where}: internal_defect requires both conflicting anchors",
                    )
                if not str(f.get("defect_statement", "")).strip():
                    rep.fault(
                        "missing_defect_statement",
                        f"{where}: internal_defect requires defect_statement",
                    )
        else:
            if (
                cls in ("defeated", "weakens_route")
                and not str(f.get("dispositive_anchor_note", "")).strip()
            ):
                rep.fault(
                    "missing_dispositive_anchor_note",
                    f"{where}: {cls} requires dispositive_anchor_note",
                )
            scan_prose(
                {k: v for k, v in f.items() if k != "classification"}, where, rep
            )

    for owner in sorted(breach_dependent - causation_seen):
        rep.fault(
            "causation_attack_missing",
            f"position {owner!r} depends on breach, delay or non-performance "
            "but has no causation-family finding linked to that owner",
        )

    # --- verdict derivation ---------------------------------------------------
    n_pp = sum(class_counts.get(c, 0) for c in PP_CLASSES)
    accounted = reviewed_set | set(parts["excluded"]) | set(parts["unreadable"])
    if (
        chat_method
        and isinstance(checkpoint, dict)
        and checkpoint.get("status") == "unanswered"
    ):
        derived = "incomplete"
    elif n_pp > 0:
        derived = "pressure_points"
    elif (
        sel_set
        and accounted == sel_set
        and not parts["parked"]
        and not r_parts["parked"]
        and not r_parts["indeterminate"]
        and not t_parked
        and findings
        and r_parts["tested"]
        and t_applied
    ):
        derived = "position_holds"
    else:
        derived = "incomplete"
    declared = data.get("verdict")
    if declared in VERDICTS and declared != derived:
        rep.fault(
            "verdict_mismatch", f"declared {declared!r} but table derives {derived!r}"
        )
    if declared == "incomplete" and not str(data.get("incomplete_reason", "")).strip():
        rep.fault(
            "missing_incomplete_reason", "incomplete verdict requires incomplete_reason"
        )

    if chat_method:
        for path, output_format in (
            (args.chat, "chat"),
            (args.brief, "document"),
            (args.html, "html"),
            (args.handoff, "handoff"),
        ):
            if path is not None and declared in VERDICTS:
                check_result(Path(path), data, output_format, root, rep)
    elif args.chat is not None:
        rep.fault("legacy_chat_unsupported", "v2.8 records use --brief")
    if not chat_method and (args.html is not None or args.handoff is not None):
        rep.fault("legacy_html_unsupported", "v2.8 records use --brief")
    if not chat_method and args.brief is not None and declared in VERDICTS:
        has_breaks = any(
            isinstance(f, dict) and f.get("classification") == "breaks_position"
            for f in findings
        )
        check_brief(Path(args.brief), declared, pp_ids, has_breaks, rep)

    if args.docket is not None:
        try:
            docket = Path(args.docket).read_text(encoding="utf-8")
        except OSError as exc:
            rep.fault("docket_missing", str(exc))
        else:
            stripped = strip_quoted(re.sub(r"```.*?```", " ", docket, flags=re.DOTALL))
            match = BANNED_IMPACT.search(stripped)
            if match:
                rep.fault(
                    "docket_impact_vocabulary",
                    "docket contains impact vocabulary "
                    f"before adjudication: {match.group(0)!r}",
                )
            if re.search(r"verdict\s*[:—-]", stripped, re.IGNORECASE):
                rep.fault(
                    "docket_contains_verdict",
                    "the docket must not state or imply a verdict",
                )
            if re.search(r"(breaks_position|internal_defect)", stripped):
                rep.fault(
                    "docket_asserts_findings",
                    "the docket must pose attacks as questions, not asserted findings",
                )
            if not DOCKET_READ_LIST.search(docket):
                rep.fault(
                    "docket_missing_read_list",
                    "the docket must state what had been read when the map was "
                    "posted ('Read so far: ...')",
                )

    return finish(
        rep,
        {
            "derived_verdict": derived,
            "counts": {
                "selected": len(sel_set),
                "reviewed": len(reviewed_set),
                "excluded_or_unreadable": len(accounted - reviewed_set),
                "findings": len(findings),
                "by_class": class_counts,
                "pressure_points": n_pp,
                "routes_tested": len(r_parts["tested"]),
                "tests_applied": len(t_applied),
                "anchors_verified": rep.anchors_verified,
                "anchors_unverified": len(rep.anchors_unverified),
            },
            "unverified_anchor_details": rep.anchors_unverified,
        },
    )


def finish(rep: Report, summary: dict | None) -> int:
    if rep.faults:
        status, code = "contract_fault", 1
    elif rep.operational or rep.anchors_unverified:
        status, code = "operational_fault", 2
    else:
        status, code = "passed", 0
    payload = {
        "status": status,
        "faults": rep.faults,
        "operational": rep.operational,
        "anchor_check_scope": "normalised_text_occurrence",
        "pinpoints_verified": False,
        "entailment_verified": False,
    }
    if summary:
        payload.update(summary)
    json.dump(payload, sys.stdout, indent=1)
    print()
    return code


if __name__ == "__main__":
    sys.exit(main())
