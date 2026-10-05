#!/usr/bin/env python3
"""Build the deterministic unit/lens dispatch plan for issue-review makers."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import sys
from typing import Any

from document_text import extract_document_text
from finding_validation import dump_atomic
from reconcile_counts import unit_map

REVIEWABLE = {"native", "scanned"}
RASTER_EXTENSIONS = {"bmp", "gif", "heic", "jpeg", "jpg", "png", "tif", "tiff", "webp"}


def image_pages(document):
    """Return known visual inputs; a standalone raster is one image."""
    if document.get("readability") != "scanned":
        return 0
    pages = document.get("pages")
    if isinstance(pages, int):
        return pages
    if document.get("ext", "").lower() in RASTER_EXTENSIONS:
        return 1
    return 0


def image_count_unknown(document):
    """True only when a scanned, paginated input lacks a usable count."""
    return (
        document.get("readability") == "scanned"
        and not isinstance(document.get("pages"), int)
        and document.get("ext", "").lower() not in RASTER_EXTENSIONS
    )


def load(path, kind, required):
    try:
        with open(path, encoding="utf-8") as handle:
            value = json.load(handle)
    except (OSError, json.JSONDecodeError) as error:
        sys.exit(f"build_review_plan: cannot read {kind}: {error}")
    for key in required:
        if key not in value:
            sys.exit(f"build_review_plan: {kind} missing key {key!r}")
    return value


def write_json(path, value):
    dump_atomic(path, value)


def hash_id(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()[:12]


def selected_units(path):
    if not path:
        return None
    value = load(path, "unit selection", [])
    if isinstance(value, dict):
        value = value.get("units")
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        sys.exit("build_review_plan: unit selection must be an array or {units: [...]}")
    if len(value) != len(set(value)):
        sys.exit("build_review_plan: unit selection repeats a unit")
    return set(value)


def job_id(framework_version, unit_id, lens_id):
    raw = f"{framework_version}\0{unit_id}\0{lens_id}".encode()
    return hashlib.sha256(raw).hexdigest()[:16]


def plan_id(plan):
    payload = {
        "framework_digest": plan["framework_digest"],
        "framework_version": plan["framework_version"],
        "jobs": plan["jobs"],
        "parked_units": plan["parked_units"],
        "summary": plan["summary"],
        "tier": plan["tier"],
        "version": plan["version"],
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode()).hexdigest()[:16]


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--framework", required=True)
    parser.add_argument("--room-root", required=True)
    parser.add_argument("--families", default=None)
    parser.add_argument("--clusters", default=None)
    parser.add_argument("--units", default=None)
    parser.add_argument("--tier", choices=["sample", "targeted", "full"], required=True)
    parser.add_argument("--extractor", choices=["auto", "stdlib"], default="auto")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    manifest = load(args.manifest, "manifest", ["documents", "counts"])
    framework = load(
        args.framework, "framework", ["framework_version", "approved", "lenses"]
    )
    families = load(args.families, "families", ["families"]) if args.families else None
    clusters = load(args.clusters, "clusters", ["threads"]) if args.clusters else None
    errors = []
    to_unit = unit_map(manifest, families, clusters, errors)
    if errors:
        sys.exit("build_review_plan: " + "; ".join(errors))

    docs = {}
    for document in sorted(
        manifest["documents"], key=lambda item: (item["id"], item["path"])
    ):
        if document.get("review_role", "substantive") == "runner-control":
            continue
        docs.setdefault(document["id"], document)
    members = {}
    for doc_id in sorted(docs):
        members.setdefault(to_unit[doc_id], []).append(doc_id)

    selection = selected_units(args.units)
    if args.tier in {"sample", "targeted"} and selection is None:
        sys.exit(f"build_review_plan: --units is required for tier {args.tier}")
    if args.tier == "sample" and len(selection) > 5:
        sys.exit("build_review_plan: sample tier is capped at five units")
    if args.tier == "full" and selection is not None:
        sys.exit("build_review_plan: full tier cannot use --units")
    unknown = sorted((selection or set()) - set(members))
    if unknown:
        sys.exit("build_review_plan: selected units are unknown: " + ", ".join(unknown))
    planned_units = sorted(selection if selection is not None else members)

    family_units = {
        family.get("family_id")
        for family in (families or {}).get("families", [])
        if len(family.get("members", [])) > 1
    }
    relation_confirmed = all(
        artifact is None or artifact.get("confirmed") is True
        for artifact in (families, clusters)
    )

    text_chars = {}
    delivery_errors = {}
    room_root = os.path.abspath(args.room_root)
    for doc_id, document in sorted(docs.items()):
        if document.get("readability") != "native":
            continue
        path = os.path.join(room_root, document["path"])
        try:
            if hash_id(path) != doc_id:
                raise OSError("content hash no longer matches the manifest")
            text_chars[doc_id] = len(extract_document_text(path, args.extractor))
        except OSError as error:
            delivery_errors[doc_id] = str(error)

    jobs: list[dict[str, Any]] = []
    parked_units = [
        {
            "member_ids": sorted(members[unit_id]),
            "reason": f"outside-approved-{args.tier}-tier",
            "unit_id": unit_id,
        }
        for unit_id in sorted(set(members) - set(planned_units))
    ]
    for unit_id in planned_units:
        unit_members = sorted(members[unit_id])
        reviewable = [
            doc_id
            for doc_id in unit_members
            if docs[doc_id].get("readability") in REVIEWABLE
        ]
        parked_members = sorted(set(unit_members) - set(reviewable))
        failed_text = [doc_id for doc_id in reviewable if doc_id in delivery_errors]
        if not reviewable or failed_text:
            parked_units.append(
                {
                    "member_ids": unit_members,
                    "reason": (
                        "no-reviewable-members"
                        if not reviewable
                        else "native-text-delivery-failed: " + ", ".join(failed_text)
                    ),
                    "unit_id": unit_id,
                }
            )
            continue
        unit_chars = sum(text_chars.get(doc_id, 0) for doc_id in reviewable)
        image_page_total = sum(image_pages(docs[doc_id]) for doc_id in reviewable)
        unknown_image_docs = sum(
            1 for doc_id in reviewable if image_count_unknown(docs[doc_id])
        )
        for lens in framework["lenses"]:
            lens_json = json.dumps(lens, sort_keys=True, separators=(",", ":"))
            estimate = math.ceil((unit_chars + len(lens_json)) / 4)
            jobs.append(
                {
                    "contains_image": any(
                        docs[doc_id].get("readability") == "scanned"
                        for doc_id in reviewable
                    ),
                    "contains_unreadable": bool(parked_members),
                    "estimated_image_pages": image_page_total,
                    "estimated_input_tokens": estimate,
                    "estimated_text_chars": unit_chars,
                    "issue_ids": [item["issue_id"] for item in lens.get("items", [])],
                    "job_id": job_id(
                        framework["framework_version"], unit_id, lens["lens_id"]
                    ),
                    "lens_id": lens["lens_id"],
                    "member_ids": reviewable,
                    "parked_member_ids": parked_members,
                    "requires_current_position": unit_id in family_units,
                    "unit_id": unit_id,
                    "unknown_image_documents": unknown_image_docs,
                }
            )
    jobs.sort(key=lambda item: item["job_id"])
    plan = {
        "approved": False,
        "approval": None,
        "framework_approved": framework.get("approved") is True,
        "framework_digest": hashlib.sha256(
            json.dumps(framework, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest(),
        "framework_version": framework["framework_version"],
        "jobs": jobs,
        "parked_units": sorted(parked_units, key=lambda item: item["unit_id"]),
        "relationship_map_confirmed": relation_confirmed,
        "summary": {
            "estimated_image_pages": sum(
                item["estimated_image_pages"] for item in jobs
            ),
            "estimated_input_tokens": sum(
                item["estimated_input_tokens"] for item in jobs
            ),
            "estimated_text_chars": sum(item["estimated_text_chars"] for item in jobs),
            "jobs": len(jobs),
            "parked_units": len(parked_units),
            "unique_units": len({item["unit_id"] for item in jobs}),
            "unknown_image_documents": sum(
                item["unknown_image_documents"] for item in jobs
            ),
        },
        "tier": args.tier,
        "version": 1,
    }
    plan["plan_id"] = plan_id(plan)
    write_json(args.out, plan)
    print(
        f"Wrote {args.out}: {len(jobs)} unit/lens job(s), "
        f"{len(parked_units)} parked unit(s)"
    )


if __name__ == "__main__":
    main()
