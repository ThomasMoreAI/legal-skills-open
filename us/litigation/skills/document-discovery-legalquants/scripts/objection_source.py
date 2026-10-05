#!/usr/bin/env python3
"""Source spans and a frozen served-request census. No legal classification."""

import argparse
import copy
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile

from objection_review import digest, file_digest, indexed, read, require, write

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
METHODS = {"docx-body-text", "utf8-paragraph-text", "host-text-extraction"}


def capture(source, extracted_text=None):
    """Capture readable text once; rendered-source comparison remains separate."""
    source = Path(source)
    limitations = []
    if extracted_text:
        text = Path(extracted_text).read_text(encoding="utf-8")
        method = "host-text-extraction"
        limitations.append("Host extraction must be compared with the original source.")
        paragraphs = [part.strip("\r\n") for part in re.split(r"\n\s*\n", text)]
    elif source.suffix.lower() == ".docx":
        with ZipFile(source) as package:
            root = ET.fromstring(package.read("word/document.xml"))
        body = root.find(W + "body")
        if body is None:
            raise ValueError("DOCX has no document body")
        paragraphs = []
        for paragraph in body.iter(W + "p"):
            pieces = []
            for node in paragraph.iter():
                if node.tag == W + "t":
                    pieces.append(node.text or "")
                elif node.tag in {W + "br", W + "cr"}:
                    pieces.append("\n")
                elif node.tag == W + "tab":
                    pieces.append("\t")
            paragraphs.append("".join(pieces))
        for tag, message in (
            ("numPr", "Automatic numbering needs comparison with displayed labels."),
            ("tbl", "Table reading order needs comparison with the rendered source."),
            ("fldChar", "Fields need comparison with their displayed source values."),
            ("txbxContent", "Text boxes need comparison with source reading order."),
            ("del", "Tracked deletions need source review."),
            ("ins", "Tracked insertions need source review."),
        ):
            if body.find(".//" + W + tag) is not None:
                limitations.append(message)
        method = "docx-body-text"
        limitations.append(
            "Headers, footers, graphics and displayed page labels are not extracted."
        )
    else:
        require(
            source.suffix.lower() in {".txt", ".md"},
            "Use host text extraction for this source format",
        )
        paragraphs = [
            part.strip("\r\n")
            for part in re.split(r"\n\s*\n", source.read_text(encoding="utf-8"))
        ]
        method = "utf8-paragraph-text"
    result = {
        "kind": "discovery-source-extraction",
        "format_version": 1,
        "source": {"file": source.name, "sha256": file_digest(source)},
        "method": method,
        "blocks": [
            {"id": f"b{i + 1}", "locator": f"body block {i + 1}", "text": text}
            for i, text in enumerate(paragraphs)
            if text.strip()
        ],
        "limitations": limitations,
    }
    if extracted_text:
        result["text_sha256"] = file_digest(extracted_text)
    return result


def spans_text(spans, blocks, occupied):
    require(isinstance(spans, list) and spans, "Missing source spans")
    pieces, locators = [], []
    order = {key: i for i, key in enumerate(blocks)}
    previous_end = (-1, -1)
    for span in spans:
        require(
            isinstance(span, dict) and span.get("block") in blocks,
            "Unknown source block",
        )
        block = blocks[span["block"]]
        start, end = span.get("start", 0), span.get("end", len(block["text"]))
        require(
            type(start) is int
            and type(end) is int
            and 0 <= start < end <= len(block["text"]),
            "Invalid source span",
        )
        require(
            (order[block["id"]], start) >= previous_end,
            "Source spans must follow original source order",
        )
        previous_end = (order[block["id"]], end)
        for offset in range(start, end):
            if block["text"][offset].isspace():
                continue
            key = (block["id"], offset)
            require(key not in occupied, "Overlapping source spans")
            occupied.add(key)
        pieces.append(block["text"][start:end])
        locators.append(block["locator"] + f", characters {start + 1}–{end}")
    return "\n".join(pieces), "; ".join(locators)


def freeze(extraction, mapping, comparison):
    """Derive wording from source spans, never from a model's paraphrased review."""
    require(
        extraction.get("kind") == "discovery-source-extraction"
        and extraction.get("format_version") == 1,
        "Unsupported extraction",
    )
    require(
        re.fullmatch(r"[a-f0-9]{64}", extraction.get("source", {}).get("sha256", "")),
        "Missing source identity",
    )
    require(extraction.get("method") in METHODS, "Unsupported extraction method")
    if extraction["method"] == "host-text-extraction":
        require(
            re.fullmatch(r"[a-f0-9]{64}", extraction.get("text_sha256", "")),
            "Retained host text identity is required",
        )
    blocks = indexed(extraction.get("blocks"))
    require(blocks, "Empty source extraction")
    for block in blocks.values():
        require(
            isinstance(block.get("text"), str)
            and isinstance(block.get("locator"), str),
            "Invalid source block",
        )
    require(
        isinstance(comparison, dict), "Record the comparison with the original source"
    )
    for key in ("by", "method", "notes"):
        require(
            isinstance(comparison.get(key), str) and comparison[key].strip(),
            f"Missing source comparison {key}",
        )
    require(
        comparison.get("status") in {"checked", "partial"},
        "Source comparison status must be checked or partial",
    )
    require(
        isinstance(comparison.get("unresolved"), list),
        "List unresolved source issues explicitly",
    )
    occupied = set()
    context = []
    for item in indexed(mapping.get("context", [])).values():
        text, locator = spans_text(item.get("spans"), blocks, occupied)
        require(
            isinstance(item.get("title"), str) and item["title"].strip(),
            "Missing context title",
        )
        context.append(
            {"id": item["id"], "title": item["title"], "text": text, "locator": locator}
        )
    context_ids = {item["id"] for item in context}
    requests = []
    block_order = {key: i for i, key in enumerate(blocks)}
    previous_end = (-1, -1)
    for item in indexed(mapping.get("requests")).values():
        label, label_locator = spans_text(item.get("label_spans"), blocks, occupied)
        text, locator = spans_text(item.get("text_spans"), blocks, occupied)
        spans = item["label_spans"] + item["text_spans"]
        for span in spans:
            start = (block_order[span["block"]], span.get("start", 0))
            end = (start[0], span.get("end", len(blocks[span["block"]]["text"])))
            require(
                start >= previous_end,
                "Request spans must follow the original source order",
            )
            previous_end = end
        require(label.strip() and text.strip(), "Empty request label or wording")
        refs = item.get("context_ids", [])
        require(
            isinstance(refs, list) and set(refs) <= context_ids,
            "Unknown request context",
        )
        requests.append(
            {
                "id": item["id"],
                "label": label,
                "text": text,
                "locator": label_locator + "; " + locator,
                "context_ids": refs,
            }
        )
    require(requests, "No served requests mapped")
    for item in mapping.get("other", []):
        require(
            isinstance(item.get("reason"), str) and item["reason"].strip(),
            "Explain non-request source material",
        )
        spans_text(item.get("spans"), blocks, occupied)
    gaps = []
    for block in blocks.values():
        missing = [
            i
            for i, char in enumerate(block["text"])
            if not char.isspace() and (block["id"], i) not in occupied
        ]
        if missing:
            gaps.append(
                {
                    "block": block["id"],
                    "locator": block["locator"],
                    "text": block["text"],
                    "unmapped_characters": len(missing),
                }
            )
    require(
        not (gaps or comparison["unresolved"]) or comparison["status"] == "partial",
        "Unmapped or unresolved source material requires partial coverage",
    )
    return {
        "kind": "served-request-census",
        "format_version": 1,
        "extraction": copy.deepcopy(extraction),
        "extraction_sha256": digest(extraction),
        "mapping": copy.deepcopy(mapping),
        "comparison": copy.deepcopy(comparison),
        "requests": requests,
        "context": context,
        "gaps": gaps,
    }


def census_check(census):
    require(
        isinstance(census, dict)
        and census.get("kind") == "served-request-census"
        and census.get("format_version") == 1,
        "A frozen served-request census is required",
    )
    rebuilt = freeze(census["extraction"], census["mapping"], census["comparison"])
    require(census == rebuilt, "Source census changed after capture")
    return census


def verify_source(extraction, source, extracted_text=None):
    """Check source bytes and directly supported capture, separately from census."""
    require(
        file_digest(source) == extraction["source"]["sha256"],
        "Original source file changed",
    )
    require(extraction.get("method") in METHODS, "Unsupported extraction method")
    if extraction["method"] in {"docx-body-text", "utf8-paragraph-text"}:
        require(
            extraction == capture(source),
            "Captured text differs from the original source",
        )
    else:
        require(
            extracted_text is not None,
            "Retained host text is required for verification",
        )
        require(
            extraction == capture(source, extracted_text),
            "Captured text differs from retained host extraction",
        )
    return extraction


def check_review_source(review):
    require(
        review.get("format_version") == 2,
        "Legacy review: attach a source-checked census before rendering or assembly",
    )
    census = census_check(review.get("source_census"))
    require(
        review.get("source") == census["extraction"]["source"],
        "Review has a different source identity",
    )
    expected = census["requests"]
    served_context = {item["id"] for item in census["context"]}
    actual = []
    for request in review.get("requests", []):
        item = {key: request.get(key) for key in ("id", "label", "text", "locator")}
        item["context_ids"] = [
            key for key in request.get("context_ids", []) if key in served_context
        ]
        actual.append(item)
    require(
        actual == expected,
        "Served request census differs: changed, omitted or reordered request",
    )
    require(
        [item for item in review.get("context", []) if item["id"] in served_context]
        == census["context"],
        "Served context changed after capture",
    )
    return census


def attach(review, census):
    """Attach a checked census; preserve candidate work by exact occurrence."""
    census_check(census)
    require(
        review.get("source") == census["extraction"]["source"],
        "Census belongs to another source",
    )
    original = indexed(review.get("requests"))
    require(
        list(original) == [r["id"] for r in census["requests"]],
        "Review does not cover the source census in order",
    )
    result = copy.deepcopy(review)
    result["format_version"] = 2
    result["source_census"] = copy.deepcopy(census)
    served_context = {item["id"] for item in census["context"]}
    result["context"] = copy.deepcopy(census["context"]) + [
        copy.deepcopy(item)
        for item in review.get("context", [])
        if item["id"] not in served_context
    ]
    result["requests"] = []
    for request in census["requests"]:
        prior = original[request["id"]]
        require(
            all(prior.get(key) == request[key] for key in ("label", "text")),
            "Review wording does not match the source spans",
        )
        require(
            [key for key in prior.get("context_ids", []) if key in served_context]
            == request["context_ids"],
            "Review context does not match served context",
        )
        result["requests"].append(
            {
                **copy.deepcopy(request),
                "context_ids": copy.deepcopy(prior.get("context_ids", [])),
                "suggestions": copy.deepcopy(prior.get("suggestions", [])),
                **(
                    {"candidate_note": copy.deepcopy(prior["candidate_note"])}
                    if "candidate_note" in prior
                    else {}
                ),
            }
        )
    result["legacy_review_sha256"] = (
        digest(review)
        if review.get("format_version") == 1
        else review.get("legacy_review_sha256")
    )
    check_review_source(result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    cmd = sub.add_parser("capture")
    cmd.add_argument("--source", required=True)
    cmd.add_argument(
        "--text", help="Text extracted by host tools, for example from a PDF"
    )
    cmd.add_argument("--out", required=True)
    cmd = sub.add_parser("freeze")
    cmd.add_argument(
        "--text", help="Retained host text; required for host-text-extraction"
    )
    for flag in ("extraction", "mapping", "comparison", "source", "out"):
        cmd.add_argument("--" + flag, required=True)
    cmd = sub.add_parser("attach")
    for flag in ("review", "census", "out"):
        cmd.add_argument("--" + flag, required=True)
    args = parser.parse_args()
    try:
        if args.command == "capture":
            result = capture(args.source, args.text)
        elif args.command == "freeze":
            extraction = read(args.extraction)
            verify_source(extraction, args.source, args.text)
            result = freeze(extraction, read(args.mapping), read(args.comparison))
        else:
            result = attach(read(args.review), read(args.census))
        write(args.out, result)
        print("OK: " + args.command)
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.exit(2, f"Not applied: {error}\n")


if __name__ == "__main__":
    main()
