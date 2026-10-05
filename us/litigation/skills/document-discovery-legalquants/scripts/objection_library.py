#!/usr/bin/env python3
"""Validate offline library curation and reconcile explicit, text-bound decisions.

Source checks verify selected files' bytes only, not passage accuracy, legal
correctness, or attorney identity. Source extraction and judgment stay with the
host model and the reviewing lawyer. This helper uses only the standard library.
"""

import argparse
import copy
import json
import re
from pathlib import Path, PurePosixPath, PureWindowsPath

import objection_review as core

EDITABLE = {
    "wording",
    "fields",
    "guidance",
    "conditions",
    "exclusions",
    "label",
    "variant",
}
DECISIONS = {"pending", "accept", "reject", "defer"}
SHA256 = re.compile(r"[a-f0-9]{64}")


def keys(record, required, label):
    core.require(isinstance(record, dict), f"{label} must be an object")
    core.require(
        set(record) == set(required.split()), f"Unexpected or missing {label} keys"
    )


def strings(values, label):
    core.require(isinstance(values, list), f"{label} must be a list")
    for value in values:
        core.nonempty(value, label)


def sha(value, label):
    core.require(isinstance(value, str) and SHA256.fullmatch(value), f"Invalid {label}")


def relative_source(value):
    core.nonempty(value, "source path")
    path = PurePosixPath(value)
    core.require(
        "\\" not in value
        and "\x00" not in value
        and not path.is_absolute()
        and not PureWindowsPath(value).drive
        and all(part not in {"", ".", ".."} for part in value.split("/")),
        "Source file must be a relative path without traversal",
    )


def entry_check(entry):
    """Check candidate structure, not legal atomicity or semantic equivalence.

    Each candidate represents one objection ground. Different source responses
    and styles can support one family; preserve variants for material scope
    differences. Full source responses belong in passage context, not as a
    substitute for identifying the reusable ground. These are review judgments,
    not phrase restrictions enforced by this helper.
    """
    core.require(isinstance(entry, dict), "Candidate entry must be an object")
    fields = entry.get("fields")
    core.require(
        isinstance(fields, dict) and all(isinstance(key, str) for key in fields),
        "Entry fields must use text keys",
    )
    core.entry_check(entry)
    remainder = core.FIELD.sub("", entry["wording"])
    core.require(
        "{{" not in remainder and "}}" not in remainder,
        "Malformed substitution placeholder; use {{lower_snake_case}}",
    )
    for name in ("conditions", "exclusions"):
        strings(entry[name], f"entry {name}")
    for source in entry["sources"]:
        core.require(isinstance(source, dict), "Entry source must be an object")
        for name in ("source_id", "locator"):
            core.nonempty(source.get(name), f"entry source {name}")
    return entry


def _trial(catalog, item):
    """Check a proposed result in memory. This does not approve or save anything."""
    proposal = copy.deepcopy(item)
    proposal.update(
        decision="accept",
        decision_record="INTERNAL VALIDATION ONLY; no user approval or saved decision",
    )
    batch = {**catalog["proposals"], "items": [proposal]}
    core.apply_proposals(catalog["library"], batch)


def catalog_check(catalog):
    keys(
        catalog,
        "kind format_version id title scope notes library proposals sources passages",
        "catalog",
    )
    core.header(catalog, "objection-library-catalog")
    for name in ("id", "title", "scope"):
        core.nonempty(catalog[name], f"catalog {name}")
    strings(catalog["notes"], "catalog notes")
    library = core.library_check(catalog["library"])
    for entry in library["entries"]:
        entry_check(entry)
    proposals = catalog["proposals"]
    core.header(proposals, "objection-library-proposals")
    core.nonempty(proposals.get("id"), "proposal batch id")
    core.require(
        proposals.get("base_sha256") == core.digest(library),
        "Catalog proposal base does not match its library snapshot",
    )
    core.require(
        proposals["id"] not in library.get("applied_batches", []),
        "Catalog proposal batch already applied",
    )
    items = core.indexed(proposals.get("items"))
    core.require(bool(items), "Catalog has no proposals")
    sources = core.indexed(catalog["sources"])
    for source in sources.values():
        keys(source, "id file title sha256", "source")
        core.nonempty(source["title"], "source title")
        relative_source(source["file"])
        sha(source["sha256"], "source SHA-256")
    mapped = set()
    for passage in core.indexed(catalog["passages"]).values():
        keys(
            passage,
            "id source_id locator request original context proposal_ids",
            "passage",
        )
        core.require(passage["source_id"] in sources, "Unknown passage source")
        for name in ("locator", "original"):
            core.nonempty(passage[name], f"passage {name}")
        for name in ("request", "context"):
            core.require(isinstance(passage[name], str), f"Passage {name} must be text")
        ids = passage["proposal_ids"]
        strings(ids, "passage proposal IDs")
        core.require(
            bool(ids) and len(ids) == len(set(ids)), "Invalid passage mappings"
        )
        core.require(set(ids) <= set(items), "Unknown passage proposal")
        mapped.update(ids)
    core.require(mapped == set(items), "Every proposal needs a source passage")
    old_sources = {
        source["source_id"]
        for entry in library["entries"]
        for source in entry["sources"]
    }
    for item in items.values():
        if "label" in item:
            core.nonempty(item["label"], "proposal label")
        core.require(
            item.get("classification") in core.CLASSIFICATIONS,
            "Unknown proposal classification",
        )
        core.require(
            item.get("decision") == "pending" and item.get("decision_record") is None,
            "Catalog proposals must be pending without preapproval",
        )
        core.require(
            "decision_record" in item, "Explicit null decision record required"
        )
        core.nonempty(item.get("reason"), "proposal reason")
        core.require(
            isinstance(item.get("evidence"), list) and bool(item["evidence"]),
            "Proposal needs source evidence",
        )
        core.require(
            all(key in item for key in ("target_id", "before", "after")),
            "Proposal must specify target, before and after",
        )
        after = item["after"]
        if after is not None:
            entry_check(after)
            core.require(
                {source["source_id"] for source in after["sources"]}
                <= (set(sources) | old_sources),
                "Unknown candidate entry source",
            )
            before = item["before"] or {}
            for name in ("status", "approval"):
                core.require(
                    name not in after
                    or (name in before and after[name] == before[name]),
                    "A pending candidate cannot introduce approval metadata",
                )
        if item["classification"] in core.REUSABLE:
            _trial(catalog, item)
    return catalog


def _draft_check(original, edited):
    if original is None:
        core.require(edited is None, "Cannot add an entry to a non-entry proposal")
        return
    core.require(isinstance(edited, dict), "Edited candidate must retain its entry")
    core.require(set(edited) == set(original), "Edited entry keys changed")
    core.require(
        all(
            edited[key] == value
            for key, value in original.items()
            if key not in EDITABLE
        ),
        "Candidate identity, sources and origin data cannot be edited",
    )
    for name in ("wording", "guidance", "label", "variant"):
        core.require(isinstance(edited[name], str), f"Edited {name} must be text")
    core.require(isinstance(edited["fields"], dict), "Edited fields must be an object")
    core.require(
        all(
            isinstance(k, str) and isinstance(v, str)
            for k, v in edited["fields"].items()
        ),
        "Edited field names and descriptions must be text",
    )
    for name in ("conditions", "exclusions"):
        core.require(
            isinstance(edited[name], list)
            and all(isinstance(value, str) for value in edited[name]),
            f"Edited {name} must be a text list",
        )


def decisions_check(catalog, decisions, application=False):
    catalog_check(catalog)
    keys(
        decisions,
        "kind format_version catalog_id catalog_sha256 base_sha256 purpose rows",
        "decisions",
    )
    core.header(decisions, "objection-library-decisions", 2)
    core.require(
        decisions["catalog_id"] == catalog["id"]
        and decisions["catalog_sha256"] == core.digest(catalog),
        "Wrong or changed catalog",
    )
    core.require(
        decisions["base_sha256"] == core.digest(catalog["library"]),
        "Wrong library snapshot",
    )
    core.require(decisions["purpose"] in {"progress", "application"}, "Unknown purpose")
    core.require(
        not application or decisions["purpose"] == "application",
        "Progress is not an application decision export",
    )
    rows = core.indexed(decisions["rows"], "proposal_id")
    items = core.indexed(catalog["proposals"]["items"])
    core.require(list(rows) == list(items), "Keep every proposal in original order")
    for proposal_id, row in rows.items():
        keys(
            row,
            "proposal_id decision after note action"
            + (" legacy" if "legacy" in row else ""),
            "decision row",
        )
        core.require(row["decision"] in DECISIONS, "Unknown curation decision")
        core.require(isinstance(row["note"], str), "Decision note must be text")
        item = items[proposal_id]
        _draft_check(item["after"], row["after"])
        if row["decision"] == "pending":
            core.require(row["action"] is None, "Pending row cannot carry an action")
        else:
            action = row["action"]
            keys(action, "kind at decision reviewed_content_sha256", "decision action")
            core.require(
                action["kind"] == "individual", "Individual curation action required"
            )
            core.nonempty(action["at"], "curation action timestamp")
            core.require(
                action["decision"] == row["decision"]
                and action["reviewed_content_sha256"]
                == core.digest(decision_content(row)),
                "Decision or wording changed after the recorded action; decide again",
            )
        if row["decision"] == "accept":
            core.require(
                item["classification"] in core.REUSABLE,
                "Non-reusable proposal cannot be approved",
            )
            entry_check(row["after"])
            _trial(catalog, {**item, "after": row["after"]})
    # Even a progress save must not claim mutually incompatible approvals.
    applied = _reconciled(catalog, decisions)
    if any(row["decision"] == "accept" for row in rows.values()):
        core.apply_proposals(catalog["library"], applied)
    return decisions


def decision_content(row):
    """Bind the disposition together with the exact candidate it acts upon."""
    return {"decision": row["decision"], "after": row["after"]}


def resume_decisions(catalog, decisions):
    """Retain legacy drafts and history, never upgrade an unbound disposition."""
    if decisions.get("format_version") == 2:
        return copy.deepcopy(decisions_check(catalog, decisions))
    core.header(decisions, "objection-library-decisions")
    result = copy.deepcopy(decisions)
    result.update(format_version=2, purpose="progress")
    for row in result["rows"]:
        keys(row, "proposal_id decision after note action", "legacy decision row")
        core.require(row["decision"] in DECISIONS, "Unknown legacy decision")
        row["legacy"] = {"decision": row["decision"], "action": row["action"]}
        row.update(decision="pending", action=None)
    return decisions_check(catalog, result)


def _reconciled(catalog, decisions):
    result = copy.deepcopy(catalog["proposals"])
    for item, row in zip(result["items"], decisions["rows"], strict=True):
        item["after"] = copy.deepcopy(row["after"])
        item["decision"] = row["decision"]
        item["decision_record"] = None
        if row["action"] is not None:
            item["decision_record"] = (
                f"Browser curation: individual {row['decision']} "
                f"at {row['action']['at']}; "
                "exact decision/entry SHA-256 "
                f"{row['action']['reviewed_content_sha256']}. "
                "Recorded action; not authenticated attorney identity."
                + (f" Note: {row['note']}" if row["note"] else "")
            )
    return result


def reconcile(catalog, decisions):
    """Return proposals only from an application export; never infer approval."""
    decisions_check(catalog, decisions, application=True)
    return _reconciled(catalog, decisions)


def apply_decisions(catalog, decisions):
    """Apply the exact approved subset without trusting an intermediate file."""
    return core.apply_proposals(catalog["library"], reconcile(catalog, decisions))


def check_sources(catalog, source_root):
    """Verify bytes under a user-selected root, not quote or legal accuracy."""
    catalog_check(catalog)
    root = Path(source_root).resolve(strict=True)
    core.require(root.is_dir(), "Source root must be a directory")
    for source in catalog["sources"]:
        candidate = root / source["file"]
        # Reject symlinks even when they resolve within the selected tree.
        cursor = root
        for part in PurePosixPath(source["file"]).parts:
            cursor /= part
            core.require(not cursor.is_symlink(), "Source symlinks are not permitted")
        path = candidate.resolve(strict=True)
        core.require(
            path.is_relative_to(root) and path.is_file(),
            "Source must be a file within the selected root",
        )
        core.require(
            core.file_digest(path) == source["sha256"],
            f"Source bytes changed: {source['file']}",
        )
    return catalog


def continue_catalog(catalog, decisions, library):
    """Carry unresolved decisions after the exact accepted subset was applied.

    Incomplete edited entries remain in the decision export. Repair those drafts
    before continuation; never silently replace draft wording with original text.
    """
    proposals = reconcile(catalog, decisions)
    core.library_check(library)
    accepted = any(item["decision"] == "accept" for item in proposals["items"])
    expected = (
        core.apply_proposals(catalog["library"], proposals)
        if accepted
        else catalog["library"]
    )
    core.require(
        library == expected,
        "Continuation library differs from the exact applied decision snapshot",
    )
    carry = [
        copy.deepcopy(item)
        for item in proposals["items"]
        if item["decision"] in {"pending", "defer"}
    ]
    core.require(bool(carry), "No pending or deferred candidates to continue")
    for item in carry:
        item.update(decision="pending", decision_record=None)
    retained = {item["id"] for item in carry}
    result = copy.deepcopy(catalog)
    suffix = core.digest({"decisions": decisions, "library": library})[:16]
    result["id"] = f"{catalog['id']}-continue-{suffix}"
    result["library"] = copy.deepcopy(library)
    result["scope"] = (
        f"Continue {len(carry)} pending or deferred candidates. "
        f"Library version {library['version']} already contains "
        f"{len(library['entries'])} approved entries."
    )
    result["notes"].insert(
        0,
        f"Earlier catalog scope: {catalog['scope']} "
        "The retained source/coverage notes describe that earlier catalog; "
        "current candidate and approved-entry counts appear above.",
    )
    result["proposals"].update(
        id=f"{catalog['proposals']['id']}-continue-{suffix}",
        base_sha256=core.digest(library),
        items=carry,
    )
    passages = []
    for passage in result["passages"]:
        passage["proposal_ids"] = [
            pid for pid in passage["proposal_ids"] if pid in retained
        ]
        if passage["proposal_ids"]:
            passages.append(passage)
    result["passages"] = passages
    result["notes"].append(
        "Continued pending/deferred candidates; each needs a new individual decision."
    )
    result["notes"].extend(
        f"Carried note for {row['proposal_id']}: {row['note']}"
        for row in decisions["rows"]
        if row["proposal_id"] in retained and row["note"].strip()
    )
    try:
        return catalog_check(result)
    except (ValueError, KeyError, TypeError) as error:
        raise ValueError(
            "Cannot continue this draft; repair invalid fields or changed targets: "
            f"{error}"
        ) from error


def render(catalog):
    catalog_check(catalog)
    assets = Path(__file__).resolve().parents[1] / "assets"
    payload = {
        "catalog": catalog,
        "catalog_sha256": core.digest(catalog),
        "base_sha256": core.digest(catalog["library"]),
    }
    data = json.dumps(payload, ensure_ascii=True).replace("<", "\\u003c")
    directory = assets / "objection-library"
    css = (
        (assets / "objection-review/review.css").read_text(encoding="utf-8")
        + "\n"
        + (directory / "catalog.css").read_text(encoding="utf-8")
    )
    return (
        (directory / "catalog.html")
        .read_text(encoding="utf-8")
        .replace("/* CATALOG_CSS */", css)
        .replace(
            "/* CATALOG_JS */", (directory / "catalog.js").read_text(encoding="utf-8")
        )
        .replace("CATALOG_DATA", data)
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in (
        "render",
        "check-decisions",
        "reconcile",
        "check-sources",
        "continue",
        "apply",
        "resume",
    ):
        command = sub.add_parser(name)
        command.add_argument("--catalog", required=True)
        if name in {"check-decisions", "reconcile", "continue", "apply", "resume"}:
            command.add_argument("--decisions", required=True)
        if name in {"render", "reconcile", "continue", "apply", "resume"}:
            command.add_argument("--out", required=True)
        if name == "check-sources":
            command.add_argument("--source-root", required=True)
        if name == "continue":
            command.add_argument("--library", required=True)
    args = parser.parse_args()
    try:
        catalog = core.read(args.catalog)
        if args.command == "render":
            core.write(args.out, render(catalog))
        elif args.command == "check-sources":
            check_sources(catalog, args.source_root)
        else:
            decisions = core.read(args.decisions)
            if args.command == "check-decisions":
                decisions_check(catalog, decisions)
            elif args.command == "reconcile":
                core.write(args.out, reconcile(catalog, decisions))
            elif args.command == "apply":
                core.write(args.out, apply_decisions(catalog, decisions))
            elif args.command == "resume":
                core.write(args.out, resume_decisions(catalog, decisions))
            else:
                core.write(
                    args.out,
                    continue_catalog(catalog, decisions, core.read(args.library)),
                )
        print("OK: " + args.command)
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.exit(2, f"Not applied: {error}\n")


if __name__ == "__main__":
    main()
