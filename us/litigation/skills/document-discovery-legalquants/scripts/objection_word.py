#!/usr/bin/env python3
"""Bind a saved Word baseline and extract changes; never classify legal reuse."""

import argparse
import copy
import difflib
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

from objection_review import (
    digest,
    file_digest,
    header,
    materialize,
    read,
    require,
    write,
)

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def text_of(node, accepted=True):
    if node.tag in (
        {W + "del", W + "moveFrom"} if accepted else {W + "ins", W + "moveTo"}
    ):
        return ""
    if node.tag in {W + "t", W + "delText"}:
        return node.text or ""
    if node.tag == W + "tab":
        return "\t"
    if node.tag in {W + "br", W + "cr"}:
        return "\n"
    if node.tag == W + "instrText":
        return ""
    return "".join(text_of(child, accepted) for child in node)


def snapshot(path, accepted=True):
    """Main body and tables; disclose other stories instead of silently checking."""
    with zipfile.ZipFile(path) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))
        body = root.find(W + "body")
        require(body is not None, "No Word document body")
        # A text box paragraph nested in a paragraph is not a second body paragraph.
        paragraphs = []

        def collect(node):
            if node.tag in (
                {W + "del", W + "moveFrom"} if accepted else {W + "ins", W + "moveTo"}
            ):
                return
            if node.tag == W + "p":
                paragraphs.append(text_of(node, accepted))
                return
            for child in node:
                collect(child)

        collect(body)
        comments = []
        if "word/comments.xml" in archive.namelist():
            for comment in ET.fromstring(archive.read("word/comments.xml")):
                comments.append(
                    {
                        "id": comment.get(W + "id"),
                        "author": comment.get(W + "author"),
                        "text": text_of(comment),
                    }
                )
        other = [
            name
            for name in archive.namelist()
            if name.startswith(
                ("word/header", "word/footer", "word/footnotes", "word/endnotes")
            )
            and name.endswith(".xml")
        ]
        revisions = sum(
            1
            for n in root.iter()
            if n.tag in {W + "ins", W + "del", W + "moveFrom", W + "moveTo"}
        )
        return {
            "paragraphs": paragraphs,
            "comments": comments,
            "revision_elements": revisions,
            "other_stories": other,
        }


def occurrences(paragraphs, text, start=0, end=None):
    """Match exact visible wording across whole paragraphs; do not normalize spaces."""
    end = len(paragraphs) if end is None else end
    result = []
    for i in range(start, end):
        candidate = ""
        for j in range(i, end):
            candidate += ("\n" if j > i else "") + paragraphs[j]
            if candidate == text:
                result.append([i, j + 1])
            if not text.startswith(candidate + "\n"):
                break
    return result


def bind_legacy(assembly, docx):
    """Historical passage-only binding for retained feedback exercises, not delivery."""
    header(assembly, "objection-assembly")
    require(assembly.get("baseline") is None, "Baseline already bound; preserve it")
    result = copy.deepcopy(assembly)
    snap = snapshot(docx)
    require(snap["revision_elements"] == 0, "Baseline contains unresolved revisions")
    paragraphs = snap["paragraphs"]
    request_spans = []
    cursor = 0
    for request in assembly["requests"]:
        found = occurrences(paragraphs, request["text"], cursor)
        require(bool(found), f"Exact request not found: {request['id']}")
        # Sequential occurrence identity handles repeated source wording and labels.
        span = found[0]
        request_spans.append(span)
        cursor = span[1]
    mapping = []
    for i, request in enumerate(assembly["requests"]):
        start = request_spans[i][1]
        end = request_spans[i + 1][0] if i + 1 < len(request_spans) else len(paragraphs)
        components = []
        for component in request["components"]:
            found = occurrences(paragraphs, component["wording"], start, end)
            require(
                len(found) == 1,
                f"Missing/ambiguous component: {component['component_id']}",
            )
            span = found[0]
            components.append(
                {
                    "component_id": component["component_id"],
                    "entry_id": component["entry_id"],
                    "span": span,
                    "wording": component["wording"],
                }
            )
            start = span[1]
        mapping.append(
            {
                "request_id": request["id"],
                "request_span": request_spans[i],
                "section_end": end,
                "components": components,
            }
        )
    result["baseline"] = {
        "file": Path(docx).name,
        "sha256": file_digest(docx),
        "paragraphs": paragraphs,
        "mapping": mapping,
        "other_stories": snap["other_stories"],
        "limits": (
            "Exact main-body matches only; inspect all stories and render separately."
        ),
    }
    return result


def layout_text(text):
    """Allow layout whitespace, preserving every non-whitespace character."""
    return " ".join(text.split())


def layout_occurrences(paragraphs, text, start=0, end=None):
    """Match whole paragraph ranges, including a paragraph split at whitespace."""
    expected = layout_text(text)
    end = len(paragraphs) if end is None else end
    found = []
    for i in range(start, end):
        if not layout_text(paragraphs[i]):
            continue
        for j in range(i, end):
            if not layout_text(paragraphs[j]):
                continue
            candidate = layout_text("\n".join(paragraphs[i : j + 1]))
            if candidate == expected:
                found.append([i, j + 1])
                break
            if not expected.startswith(candidate + " "):
                break
    return found


def plain_response_region(docx, start, end):
    """This initial check supports ordinary body paragraphs, not every Word object."""
    with zipfile.ZipFile(docx) as archive:
        body = ET.fromstring(archive.read("word/document.xml")).find(W + "body")
    if body is None:
        raise ValueError("No Word document body")
    position = 0
    unsupported = set()
    special = {
        W + name
        for name in (
            "drawing",
            "pict",
            "object",
            "fldSimple",
            "fldChar",
            "instrText",
            "footnoteReference",
            "endnoteReference",
        )
    }

    def collect(node, ordinary=False):
        nonlocal position
        if node.tag == W + "p":
            if not ordinary or any(child.tag in special for child in node.iter()):
                unsupported.add(position)
            position += 1
            return
        for child in node:
            collect(child)

    for child in body:
        if child.tag == W + "sectPr":
            continue
        if child.tag != W + "p":
            unsupported.add(position)
        collect(child, ordinary=child.tag == W + "p")
    require(
        not any(start <= p < end for p in unsupported),
        "Initial response-region check supports ordinary body paragraphs only; "
        "use host inspection for tables, text boxes, fields or other objects",
    )


def bind(assembly, docx, review=None, selections=None, layout=None):
    """Check the initial response region against its original reviewed decisions.

    The host supplies exact headings and drafting prompts from the chosen format,
    plus the first post-response paragraph as a boundary. They are layout, never
    a place to add objection or substantive-response text. Caption, later service
    forms and other stories require separate host inspection. This check places
    no restriction on the lawyer's subsequent Word edits.
    """
    if review is None or selections is None or layout is None:
        raise ValueError(
            "Initial Word binding requires the original review, "
            "decisions and Word layout"
        )
    expected = materialize(review, selections)
    require(
        assembly == expected, "Assembly differs from the original reviewed decisions"
    )
    header(layout, "objection-word-layout")
    require(
        layout.get("review_sha256") == expected["review_sha256"]
        and layout.get("selections_sha256") == expected["selections_sha256"],
        "Word layout belongs to a different review or decisions",
    )
    frames = layout.get("requests")
    require(
        isinstance(frames, list) and all(isinstance(frame, dict) for frame in frames),
        "Word layout requires request frames",
    )
    require(
        [f.get("request_id") for f in frames]
        == [r["id"] for r in expected["requests"]],
        "Word layout must retain every request occurrence in served order",
    )
    require(bool(frames), "No requests to bind")
    for frame in frames:
        require(
            set(frame)
            == {"request_id", "request_heading", "response_heading", "drafting_prompt"},
            "Word frames contain only request/response headings and a drafting prompt",
        )
        require(
            all(isinstance(value, str) for value in frame.values()),
            "Word frame values must be text",
        )
    marker = layout.get("after_responses")
    require(
        isinstance(marker, str) and bool(layout_text(marker)), "Missing end boundary"
    )
    snap = snapshot(docx)
    require(snap["revision_elements"] == 0, "Baseline contains unresolved revisions")
    paragraphs = snap["paragraphs"]
    anchor = frames[0]["request_heading"] or expected["requests"][0]["text"]
    starts = layout_occurrences(paragraphs, anchor)
    require(bool(starts), "First request heading/text not found")
    start = starts[0][0]
    cursor = start
    spans = []
    expected_text = []
    for request, frame in zip(expected["requests"], frames, strict=True):
        require(
            layout_text(frame["request_heading"]) == layout_text(request["label"]),
            f"Word request heading differs from the served label: {request['id']}",
        )
        found = layout_occurrences(paragraphs, request["text"], cursor)
        require(bool(found), f"Exact request not found: {request['id']}")
        spans.append(found[0])
        cursor = found[0][1]
        expected_text.extend(
            [frame["request_heading"], request["text"], frame["response_heading"]]
        )
        expected_text.extend(c["wording"] for c in request["components"])
        expected_text.append(frame["drafting_prompt"])
    ends = layout_occurrences(paragraphs, marker, cursor)
    require(len(ends) == 1, "Missing or ambiguous post-response boundary")
    end = ends[0][0]
    plain_response_region(docx, start, end)
    require(
        layout_text("\n".join(paragraphs[start:end]))
        == layout_text("\n".join(expected_text)),
        "Saved request/response region differs from accepted decisions "
        "or template prompts",
    )
    mapping = []
    for i, request in enumerate(expected["requests"]):
        cursor = spans[i][1]
        section_end = spans[i + 1][0] if i + 1 < len(spans) else end
        components = []
        for component in request["components"]:
            found = layout_occurrences(
                paragraphs, component["wording"], cursor, section_end
            )
            # The complete region already matches. Sequential occurrence identity
            # also supports two deliberately selected components with equal wording.
            require(
                bool(found),
                f"Component paragraph not found: {component['component_id']}",
            )
            components.append(
                {
                    "component_id": component["component_id"],
                    "entry_id": component["entry_id"],
                    "span": found[0],
                    "wording": component["wording"],
                }
            )
            cursor = found[0][1]
        mapping.append(
            {
                "request_id": request["id"],
                "request_span": spans[i],
                "section_end": section_end,
                "components": components,
            }
        )
    result = copy.deepcopy(expected)
    result["baseline"] = {
        "file": Path(docx).name,
        "sha256": file_digest(docx),
        "paragraphs": paragraphs,
        "mapping": mapping,
        "other_stories": snap["other_stories"],
        "initial_fidelity": {
            "layout_sha256": digest(layout),
            "response_region": [start, end],
            "review_sha256": expected["review_sha256"],
            "selections_sha256": expected["selections_sha256"],
        },
        "limits": (
            "Initial ordinary-body request/response region only; whitespace may vary. "
            "Template headings/prompts are host-supplied. "
            "Inspect caption, service forms, "
            "other stories and rendering separately. Later Word edits are unrestricted."
        ),
    }
    return result


def compare(assembly, baseline, returned):
    header(assembly, "objection-assembly")
    saved = assembly.get("baseline") or {}
    require(saved.get("sha256") == file_digest(baseline), "Wrong delivered baseline")
    old = snapshot(baseline)["paragraphs"]
    require(old == saved.get("paragraphs"), "Stored baseline text does not match")
    after = snapshot(returned)
    new = after["paragraphs"]
    all_components = [(m, c) for m in saved["mapping"] for c in m["components"]]
    observations = []
    matcher = difflib.SequenceMatcher(None, old, new, autojunk=False)
    for operation, a, b, c, d in matcher.get_opcodes():
        if operation == "equal":
            continue
        overlaps = [
            (m, component)
            for m, component in all_components
            if a < component["span"][1] and b > component["span"][0]
        ]
        origin = None
        # A change crossing boundaries or inserted at an edge does not establish origin.
        if len(overlaps) == 1:
            m, component = overlaps[0]
            lo, hi = component["span"]
            if lo <= a < b <= hi:
                origin = {
                    "request_id": m["request_id"],
                    "component_id": component["component_id"],
                    "entry_id": component["entry_id"],
                    "original_component": component["wording"],
                }
        request = next(
            (
                m
                for m in saved["mapping"]
                if m["request_span"][1] <= a < m["section_end"]
            ),
            None,
        )
        observations.append(
            {
                "id": f"edit-{len(observations) + 1}",
                "operation": operation,
                "before": "\n".join(old[a:b]),
                "after": "\n".join(new[c:d]),
                "baseline_span": [a, b],
                "returned_span": [c, d],
                "origin": origin,
                "request_context": request["request_id"] if request else None,
                "mapping": "component_overlap"
                if origin
                else "unresolved_or_outside_objection",
                "preceding_text": old[max(0, a - 2) : a],
                "following_text": old[b : b + 2],
            }
        )
    return {
        "kind": "objection-word-observations",
        "format_version": 1,
        "baseline_sha256": saved["sha256"],
        "returned_sha256": file_digest(returned),
        "returned_file": Path(returned).name,
        "observations": observations,
        "comments": after["comments"],
        "revision_elements": after["revision_elements"],
        "limits": [
            "Main-body paragraph comparison; legal reuse is not classified.",
            "Component overlap needs contextual confirmation, especially moved text.",
            "Comments are unanchored context; do not attribute them by proximity.",
            "Headers, footers, notes, fields and graphics require host-tool review.",
        ],
        "other_stories": after["other_stories"],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["bind", "compare"])
    parser.add_argument("--assembly", required=True)
    parser.add_argument("--docx", required=True)
    parser.add_argument("--baseline")
    parser.add_argument("--review")
    parser.add_argument("--selections")
    parser.add_argument("--layout")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    try:
        assembly = read(args.assembly)
        if args.command == "bind":
            require(
                args.review and args.selections and args.layout,
                "Initial binding requires --review, --selections and --layout",
            )
            result = bind(
                assembly,
                args.docx,
                read(args.review),
                read(args.selections),
                read(args.layout),
            )
        else:
            require(args.baseline, "Comparison requires the delivered baseline file")
            result = compare(assembly, args.baseline, args.docx)
        write(args.out, result)
        print("OK: " + args.command)
    except (ValueError, KeyError, TypeError, OSError, zipfile.BadZipFile) as error:
        parser.exit(2, f"Not applied: {error}\n")


if __name__ == "__main__":
    main()
