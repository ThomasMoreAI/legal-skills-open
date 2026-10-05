#!/usr/bin/env python3
"""Offline review records and exact, version-bound decision handoffs. Stdlib only."""

import argparse
import copy
import hashlib
import json
import re
from pathlib import Path

FORMAT = 1
STATES = {"not_reviewed", "reviewed", "needs_input"}
REUSABLE = {"replacement", "new_variant", "guidance", "new_entry"}
CLASSIFICATIONS = REUSABLE | {
    "matter_only",
    "substantive_response",
    "formatting_only",
    "unresolved",
}
FIELD = re.compile(r"\{\{([a-z][a-z0-9_]*)\}\}")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(value):
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode()).hexdigest()


def file_digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def read(path):
    return json.loads(Path(path).read_text(), object_pairs_hook=unique_pairs)


def write(path, value):
    """Never replace a source, an earlier snapshot, or another session's file."""
    data = value if isinstance(value, str) else json.dumps(value, indent=2) + "\n"
    with Path(path).open("x", encoding="utf-8") as stream:
        stream.write(data)


def nonempty(value, label):
    require(isinstance(value, str) and bool(value.strip()), f"Missing {label}")


def header(record, kind, version=FORMAT):
    require(isinstance(record, dict), "Expected a JSON object")
    require(record.get("kind") == kind, f"Expected {kind}")
    require(record.get("format_version") == version, "Unsupported format version")


def indexed(items, key="id"):
    require(isinstance(items, list), "Expected a list")
    result = {}
    for item in items:
        require(isinstance(item, dict), "Expected an object in list")
        nonempty(item.get(key), key)
        require(item[key] not in result, f"Duplicate {key}: {item[key]}")
        result[item[key]] = item
    return result


def entry_check(entry):
    """Check record structure, not whether wording is one coherent legal ground.

    Family identifies the semantic objection type; a variant records a material
    scope difference. Source excerpts may contain several grounds, but an entry
    is reusable wording for one ground. Consolidation and atomicity need review;
    neither string similarity nor a valid hash establishes them.
    """
    for key in ("id", "family", "label", "variant", "wording", "guidance"):
        nonempty(entry.get(key), f"entry {key}")
    fields = entry.get("fields")
    require(isinstance(fields, dict), "Entry fields must be an object")
    require(set(FIELD.findall(entry["wording"])) == set(fields), "Field mismatch")
    for key, label in fields.items():
        require(FIELD.fullmatch("{{" + key + "}}"), "Invalid field name")
        nonempty(label, "field description")
    for key in ("conditions", "exclusions", "sources"):
        require(isinstance(entry.get(key), list), f"Missing entry {key}")
    require(bool(entry["sources"]), "Entry needs source provenance")


def library_check(library):
    """Validate an approved snapshot; empty snapshots are curation starters only.

    An approval record and content binding do not establish who approved it.
    Existing user-supplied approved snapshots keep their original provenance.
    Raw precedent responses must go through pending curation, not be relabeled
    approved by the host to satisfy this shape check.
    """
    header(library, "objection-library")
    nonempty(library.get("id"), "library id")
    require(
        type(library.get("version")) is int and library["version"] > 0,
        "Library version must be a positive integer",
    )
    for entry in indexed(library.get("entries")).values():
        entry_check(entry)
        require(entry.get("status") == "approved", "Only approved entries selectable")
        approval = entry.get("approval")
        require(isinstance(approval, dict), "Approval must be a recorded object")
        nonempty(approval.get("record"), "approval record")
    return library


def wording(entry, params):
    require(isinstance(params, dict), "Substitutions must be an object")
    require(set(params) == set(entry["fields"]), "Substitution fields do not match")
    for value in params.values():
        nonempty(value, "substitution value; use a visible drafting slot if unresolved")
    return FIELD.sub(lambda m: params[m[1]], entry["wording"])


def review_check(review):
    from objection_source import check_review_source

    header(review, "objection-review", review.get("format_version"))
    check_review_source(review)
    for key in ("id", "title"):
        nonempty(review.get(key), key)
    source = review.get("source", {})
    nonempty(source.get("file"), "source file")
    require(
        re.fullmatch(r"[a-f0-9]{64}", source.get("sha256", "")),
        "Source SHA-256 required",
    )
    library_check(review["library"])
    entries = indexed(review["library"]["entries"])
    require(
        bool(entries),
        "Request review requires a nonempty approved objection library; "
        "curate and approve a useful subset first",
    )
    context = indexed(review.get("context"))
    for item in context.values():
        for key in ("title", "text", "locator"):
            nonempty(item.get(key), f"context {key}")
    requests = indexed(review.get("requests"))
    require(bool(requests), "No served requests")
    for request in requests.values():
        for key in ("label", "text", "locator"):
            nonempty(request.get(key), f"request {key}")
        require(set(request.get("context_ids", [])) <= set(context), "Unknown context")
        if "candidate_note" in request:
            nonempty(request["candidate_note"], "candidate assessment note")
        for s in indexed(request.get("suggestions"), "entry_id").values():
            require(s["entry_id"] in entries, "Unknown suggested library entry")
            wording(entries[s["entry_id"]], s["params"])
            nonempty(s.get("rationale"), "suggestion rationale")
            require(isinstance(s.get("basis"), list) and s["basis"], "Basis required")
            for item in s["basis"]:
                nonempty(item, "candidate basis")
            require(isinstance(s.get("missing"), list), "Missing-input list required")
            for item in s["missing"]:
                require(isinstance(item, str), "Missing inputs must be text")
            require(type(s.get("preselected")) is bool, "Preselection must be boolean")
    return review


def choice_check(choice, entries, complete=True):
    require("entry_id" in choice, "Explicit library origin or null one-off required")
    nonempty(choice.get("component_id"), "component id")
    require(isinstance(choice.get("wording"), str), "Wording must be text")
    if complete:
        nonempty(choice["wording"], "selected wording")
    require(type(choice.get("edited")) is bool, "Explicit edited flag required")
    for key in ("scope", "notes"):
        require(isinstance(choice.get(key), str), f"Choice {key} must be text")
    entry_id = choice.get("entry_id")
    if entry_id is None:
        require(
            choice.get("edited") and choice.get("params") == {},
            "One-off text must be explicitly edited and have no library fields",
        )
    else:
        require(entry_id in entries, "Selected entry absent from original library")
        entry = entries[entry_id]
        params = choice.get("params")
        require(isinstance(params, dict), "Substitutions must be an object")
        require(set(params) == set(entry["fields"]), "Substitution fields do not match")
        require(
            all(isinstance(value, str) for value in params.values()),
            "Substitutions must be text",
        )
        if complete and not choice["edited"]:
            for value in params.values():
                nonempty(
                    value,
                    "substitution value; use a visible drafting slot if unresolved",
                )
        expected = FIELD.sub(lambda m: params[m[1]], entry["wording"])
        require(
            choice["edited"] or choice["wording"] == expected,
            "Changed library wording must be marked as a request-specific edit",
        )


def reviewed_content(review, row):
    """Exact review snapshot, excluding the action that records its acceptance."""
    return {
        "review_sha256": digest(review),
        "request_id": row["request_id"],
        "choices": row["choices"],
        "notes": row["notes"],
    }


def _selection_identity(review, selections, legacy=False):
    review_check(review)
    require(
        selections.get("review_id") == review["id"]
        and (
            selections.get("review_sha256") == digest(review)
            or legacy
            and review.get("legacy_review_sha256")
            and selections.get("review_sha256") == review["legacy_review_sha256"]
        ),
        "Wrong or changed review",
    )
    require(
        selections.get("source_sha256") == review["source"]["sha256"],
        "Wrong served source",
    )
    require(
        selections.get("library_sha256") == digest(review["library"]),
        "Wrong library snapshot",
    )
    require(
        selections.get("purpose") in {"progress", "assembly"}, "Unknown export purpose"
    )


def selections_check(review, selections, assembly=False):
    header(selections, "objection-selections", 2)
    _selection_identity(review, selections)
    require(
        not assembly or selections["purpose"] == "assembly",
        "Progress is not an assembly decision export",
    )
    rows = indexed(selections.get("rows"), "request_id")
    require(
        list(rows) == [r["id"] for r in review["requests"]],
        "Export must retain every request in served order",
    )
    entries = indexed(review["library"]["entries"])
    component_ids = set()
    for row in rows.values():
        require(row.get("state") in STATES, "Unknown review state")
        require(isinstance(row.get("notes"), str), "Row notes must be text")
        drafts = indexed(row.get("drafts"), "component_id")
        selected_ids = row.get("selected_ids")
        require(
            isinstance(selected_ids, list), "Ordered selected component IDs required"
        )
        require(
            all(isinstance(key, str) and key in drafts for key in selected_ids)
            and len(set(selected_ids)) == len(selected_ids),
            "Unknown or repeated selected component",
        )
        require(
            row.get("choices") == [drafts[key] for key in selected_ids],
            "Selected wording differs from its saved draft or order",
        )
        origins = set()
        for draft in drafts.values():
            choice_check(draft, entries, complete=False)
            require(
                draft["component_id"] not in component_ids, "Duplicate component id"
            )
            component_ids.add(draft["component_id"])
            if draft["entry_id"]:
                require(draft["entry_id"] not in origins, "Repeated library draft")
                origins.add(draft["entry_id"])
        if row["state"] == "reviewed":
            action = row.get("action") or {}
            require(
                action.get("kind") in {"individual", "batch"},
                "Reviewed row requires an explicit review action",
            )
            nonempty(action.get("at"), "review action timestamp")
            require(
                action.get("reviewed_content_sha256")
                == digest(reviewed_content(review, row)),
                "Wording changed after the recorded review; review this request again",
            )
            for choice in row["choices"]:
                choice_check(choice, entries)
        else:
            require(row.get("action") is None, "Unfinished row cannot carry approval")
    return selections


def resume_selections(review, selections):
    """Migrate available legacy edits as drafts without inventing reviewed content."""
    if selections.get("format_version") == 2:
        return copy.deepcopy(selections_check(review, selections))
    header(selections, "objection-selections")
    _selection_identity(review, selections, legacy=True)
    result = copy.deepcopy(selections)
    result.update(format_version=2, purpose="progress", review_sha256=digest(review))
    for row in result["rows"]:
        row["drafts"] = copy.deepcopy(row["choices"])
        row["selected_ids"] = [choice["component_id"] for choice in row["choices"]]
        row["legacy_action"] = row.get("action")
        row["state"] = (
            "needs_input" if row.get("state") == "needs_input" else "not_reviewed"
        )
        row["action"] = None
    return selections_check(review, result)


def materialize(review, selections):
    selections_check(review, selections, assembly=True)
    rows = indexed(selections["rows"], "request_id")
    requests = []
    for request in review["requests"]:
        row = rows[request["id"]]
        choices = row["choices"] if row["state"] == "reviewed" else []
        requests.append(
            {
                "id": request["id"],
                "label": request["label"],
                "text": request["text"],
                "locator": request["locator"],
                "state": row["state"],
                "components": copy.deepcopy(choices),
                "objection_text": "\n\n".join(c["wording"] for c in choices),
                "open_review": row["state"] != "reviewed",
                "notes": row["notes"],
            }
        )
    return {
        "kind": "objection-assembly",
        "format_version": FORMAT,
        "review_id": review["id"],
        "review_sha256": digest(review),
        "selections_sha256": digest(selections),
        "source": review["source"],
        "source_coverage": {
            "comparison": copy.deepcopy(review["source_census"]["comparison"]),
            "gaps": copy.deepcopy(review["source_census"]["gaps"]),
            "capture_limits": copy.deepcopy(
                review["source_census"]["extraction"]["limitations"]
            ),
        },
        "library": copy.deepcopy(review["library"]),
        "requests": requests,
        "baseline": None,
    }


def render(review):
    review_check(review)
    assets = Path(__file__).resolve().parents[1] / "assets" / "objection-review"
    payload = {
        "review": review,
        "review_sha256": digest(review),
        "library_sha256": digest(review["library"]),
    }
    # Less-than escaping also prevents closing a script element from source data.
    data = json.dumps(payload, ensure_ascii=True).replace("<", "\\u003c")
    template = (assets / "review.html").read_text()
    return (
        template.replace("/* REVIEW_CSS */", (assets / "review.css").read_text())
        .replace("/* REVIEW_JS */", (assets / "review.js").read_text())
        .replace("REVIEW_DATA", data)
    )


def apply_proposals(library, proposals):
    library_check(library)
    header(proposals, "objection-library-proposals")
    nonempty(proposals.get("id"), "proposal batch id")
    require(
        proposals["id"] not in library.get("applied_batches", []),
        "This proposal batch is already applied",
    )
    require(
        proposals.get("base_sha256") == digest(library),
        "Library changed; reconcile this proposal against the current snapshot",
    )
    updated = copy.deepcopy(library)
    original_entries = indexed(library["entries"])
    entries = indexed(updated["entries"])
    changed = set()
    accepted = []
    for item in indexed(proposals.get("items")).values():
        require(item.get("classification") in CLASSIFICATIONS, "Unknown classification")
        require(
            item.get("decision") in {"pending", "accept", "reject", "defer"},
            "Unknown proposal decision",
        )
        if item["decision"] != "accept":
            continue
        require(
            item["classification"] in REUSABLE, "Non-reusable proposal cannot apply"
        )
        nonempty(item.get("decision_record"), "Explicit library approval record")
        require(bool(item.get("evidence")), "Proposal needs source evidence")
        after = copy.deepcopy(item.get("after"))
        require(
            isinstance(after, dict), "Accepted proposal needs exact resulting entry"
        )
        entry_check(after)
        target = item.get("target_id")
        if item["classification"] in {"replacement", "guidance"}:
            require(
                target in original_entries
                and item.get("before") == original_entries[target],
                "Proposal before-entry does not match the library",
            )
            require(after["id"] == target, "Replacement must retain variant identity")
            if item["classification"] == "guidance":
                require(
                    after["wording"] == original_entries[target]["wording"],
                    "Guidance-only update changes wording",
                )
        else:
            require(after["id"] not in entries, "New entry/variant id already exists")
            if item["classification"] == "new_variant":
                require(
                    target in original_entries
                    and item.get("before") == original_entries[target],
                    "New variant must identify its original entry",
                )
                require(
                    after["family"] == original_entries[target]["family"],
                    "Variant family mismatch",
                )
            else:
                require(
                    target is None and item.get("before") is None,
                    "New entry cannot replace an existing entry",
                )
        require(
            after["id"] not in changed, "Conflicting accepted proposals for one entry"
        )
        changed.add(after["id"])
        after["status"] = "approved"
        after["approval"] = {
            "record": item["decision_record"],
            "proposal_batch": proposals["id"],
            "proposal_id": item["id"],
        }
        entries[after["id"]] = after
        accepted.append(item["id"])
    require(bool(accepted), "No accepted reusable changes; no new version created")
    updated["entries"] = list(entries.values())
    updated["version"] += 1
    updated["parent_sha256"] = digest(library)
    updated["applied_batches"] = [*library.get("applied_batches", []), proposals["id"]]
    updated["last_decisions"] = {
        "batch": proposals["id"],
        "accepted": accepted,
        "proposals_sha256": digest(proposals),
    }
    return library_check(updated)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("render", "materialize", "check-selections", "resume"):
        cmd = sub.add_parser(command)
        cmd.add_argument("--review", required=True)
        if command != "render":
            cmd.add_argument("--selections", required=True)
        if command != "check-selections":
            cmd.add_argument("--out", required=True)
    cmd = sub.add_parser("apply-library")
    cmd.add_argument("--library", required=True)
    cmd.add_argument("--proposals", required=True)
    cmd.add_argument("--out", required=True)
    args = parser.parse_args()
    try:
        if args.command == "apply-library":
            write(args.out, apply_proposals(read(args.library), read(args.proposals)))
        else:
            review = read(args.review)
            if args.command == "render":
                write(args.out, render(review))
            elif args.command == "materialize":
                write(args.out, materialize(review, read(args.selections)))
            elif args.command == "resume":
                write(args.out, resume_selections(review, read(args.selections)))
            else:
                selections_check(review, read(args.selections))
        print("OK: " + args.command)
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.exit(2, f"Not applied: {error}\n")


if __name__ == "__main__":
    main()
