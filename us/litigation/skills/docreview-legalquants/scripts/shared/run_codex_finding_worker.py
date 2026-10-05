#!/usr/bin/env python3
"""Run one compact finding assignment through an isolated Codex context."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

DEFAULT_ISSUE_BATCH_SIZE = 12
MAX_ISSUES_PER_CALL = 12
LOW_EFFORTS = {"none", "minimal", "low"}


def load_object(path: Path, label: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise OSError(f"cannot read {label}: {error}") from error
    if not isinstance(value, dict):
        raise OSError(f"{label} must be an object")
    return value


def usage_from_events(stream: str) -> dict[str, int] | None:
    totals = {
        "input_tokens": 0,
        "cached_input_tokens": 0,
        "output_tokens": 0,
        "reasoning_output_tokens": 0,
    }
    completed_turns = 0
    for line in stream.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(event, dict) or event.get("type") != "turn.completed":
            continue
        usage = event.get("usage")
        if not isinstance(usage, dict):
            continue
        values: dict[str, int] = {}
        for key in totals:
            value = usage.get(key, 0)
            if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                break
            values[key] = value
        else:
            completed_turns += 1
            for key, value in values.items():
                totals[key] += value
    if completed_turns == 0:
        return None
    totals["model_calls"] = completed_turns
    totals["total_tokens"] = totals["input_tokens"] + totals["output_tokens"]
    return totals


def write_usage(
    path: Path,
    assignment: dict[str, Any],
    model: str,
    effort: str,
    usage: dict[str, int],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(
        json.dumps(
            {
                "contract": "codex-usage/1",
                "effort": effort,
                "job_id": assignment.get("job_id"),
                "model": model,
                **usage,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def verified_images(
    assignment: dict[str, Any], sidecar_path: Path
) -> list[tuple[int, int, Path]]:
    sidecar = load_object(sidecar_path, "review-copy sidecar")
    bundle_root = sidecar.get("bundle_root")
    documents = sidecar.get("documents")
    if not isinstance(bundle_root, str) or not isinstance(documents, list):
        raise OSError("review-copy sidecar is malformed")
    bundle = (sidecar_path.parent / bundle_root).resolve()
    copies = {
        item.get("doc_id"): item
        for item in documents
        if isinstance(item, dict) and isinstance(item.get("doc_id"), str)
    }
    images: list[tuple[int, int, Path]] = []
    assigned = assignment.get("documents")
    if not isinstance(assigned, list):
        raise OSError("assignment documents must be an array")
    for ordinal, document in enumerate(assigned, 1):
        if not isinstance(document, dict) or not isinstance(document.get("id"), str):
            raise OSError("assignment contains a malformed document")
        copy = copies.get(document["id"])
        if not isinstance(copy, dict) or copy.get("status") != "ready":
            raise OSError(f"review copy is not ready for document {ordinal}")
        derivatives = copy.get("derivatives")
        if not isinstance(derivatives, list):
            raise OSError(
                f"review copy derivatives are malformed for document {ordinal}"
            )
        doc_images: list[tuple[int, int, Path]] = []
        for derivative in derivatives:
            if not isinstance(derivative, dict):
                continue
            media_type = derivative.get("media_type")
            relative = derivative.get("path")
            expected_hash = derivative.get("sha256")
            if not isinstance(media_type, str) or not media_type.startswith("image/"):
                continue
            if not isinstance(relative, str) or not isinstance(expected_hash, str):
                raise OSError(f"image derivative is malformed for document {ordinal}")
            path = (bundle / relative).resolve()
            try:
                path.relative_to(bundle)
            except ValueError as error:
                raise OSError("review-copy path escapes the bundle") from error
            if not path.is_file():
                raise OSError(f"review-copy image is missing for document {ordinal}")
            actual = "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()
            if actual != expected_hash:
                raise OSError(f"review-copy image hash drifted for document {ordinal}")
            page = derivative.get("page")
            if not isinstance(page, int) or isinstance(page, bool) or page < 1:
                page = 1
            doc_images.append((ordinal, page, path))
        if document.get("readability") == "scanned" and not doc_images:
            raise OSError(f"scanned document {ordinal} has no image review copy")
        images.extend(
            sorted(doc_images, key=lambda item: (item[1], item[2].as_posix()))
        )
    return images


def batched_assignments(
    assignment: dict[str, Any], batch_size: int
) -> list[tuple[int, dict[str, Any]]]:
    if not 1 <= batch_size <= MAX_ISSUES_PER_CALL:
        raise OSError(f"issue batch size must be 1..{MAX_ISSUES_PER_CALL}")
    issues = assignment.get("issue_items")
    if (
        not isinstance(issues, list)
        or not issues
        or not all(isinstance(item, dict) for item in issues)
    ):
        raise OSError("assignment issue_items must be a non-empty object array")
    return [
        (offset, {**assignment, "issue_items": issues[offset : offset + batch_size]})
        for offset in range(0, len(issues), batch_size)
    ]


def batch_prompt(
    prompt: str,
    original_assignment: str,
    assignment: dict[str, Any],
    batch_number: int,
    batch_count: int,
) -> str:
    encoded = json.dumps(assignment, indent=2, sort_keys=True) + "\n"
    if original_assignment in prompt:
        rendered = prompt.replace(original_assignment, encoded, 1)
    else:
        rendered = prompt + "\n\n# Assignment\n\n```json\n" + encoded + "```\n"
    return (
        rendered
        + "\n\n# Bounded request batch\n\n"
        + f"This is request batch {batch_number} of {batch_count}. Review every "
        "supplied document page against every issue in this batch. Number this "
        "batch locally from 1 in the returned `n` fields; the adapter restores "
        "the approved full-lens order after validating every issue ID.\n"
    )


def validate_batch_result(
    value: object,
    assignment: dict[str, Any],
    offset: int,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    if not isinstance(value, dict):
        raise OSError("batch result must be an object")
    if value.get("contract") != "finding-worker/2":
        raise OSError("batch result has the wrong contract")
    if value.get("review_plan_id") != assignment.get("review_plan_id") or value.get(
        "job_id"
    ) != assignment.get("job_id"):
        raise OSError("batch result has drifted run identifiers")
    issues = assignment.get("issue_items")
    determinations = value.get("determinations")
    candidates = value.get("privilege_candidates")
    if not isinstance(issues, list) or not isinstance(determinations, list):
        raise OSError("batch result has no determination array")
    if len(determinations) != len(issues):
        raise OSError("batch result did not cover every batched request")
    normalized: list[dict[str, Any]] = []
    pairs = zip(determinations, issues)  # noqa: B905 - lengths checked; Python 3.9
    for local_index, (raw, issue) in enumerate(pairs, 1):
        if not isinstance(raw, dict) or not isinstance(issue, dict):
            raise OSError("batch result contains a malformed determination")
        if raw.get("n") != local_index or raw.get("issue_id") != issue.get("issue_id"):
            raise OSError("batch result changed request order or identity")
        normalized.append({**raw, "n": offset + local_index})
    if not isinstance(candidates, list) or not all(
        isinstance(candidate, dict) for candidate in candidates
    ):
        raise OSError("batch result has a malformed privilege candidate array")
    return normalized, candidates


def dump_atomic(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    temporary.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--assignment", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--schema", required=True)
    parser.add_argument("--room-root", required=True)
    parser.add_argument("--review-copies", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--effort", required=True)
    parser.add_argument(
        "--issue-batch-size", type=int, default=DEFAULT_ISSUE_BATCH_SIZE
    )
    parser.add_argument("--allow-low-effort", action="store_true")
    parser.add_argument("--usage-out")
    parser.add_argument("--require-usage", action="store_true")
    parser.add_argument("--codex", default="codex")
    args = parser.parse_args()
    try:
        assignment = load_object(Path(args.assignment), "assignment")
        images = verified_images(assignment, Path(args.review_copies))
        batches = batched_assignments(assignment, args.issue_batch_size)
    except OSError as error:
        print(f"run_codex_finding_worker: {error}", file=sys.stderr)
        return 2
    if not 1 <= args.issue_batch_size <= MAX_ISSUES_PER_CALL:
        print(
            "run_codex_finding_worker: --issue-batch-size must be "
            f"1..{MAX_ISSUES_PER_CALL}",
            file=sys.stderr,
        )
        return 2
    if args.effort.lower() in LOW_EFFORTS and not args.allow_low_effort:
        print(
            "run_codex_finding_worker: substantive mapping requires at least medium "
            "reasoning effort; --allow-low-effort is reserved for an explicit "
            "user override",
            file=sys.stderr,
        )
        return 2
    prompt = sys.stdin.read()
    original_assignment = Path(args.assignment).read_text(encoding="utf-8")
    page_map = "\n".join(
        f"- Attachment {index}: Document {ordinal}, page {page}"
        for index, (ordinal, page, _) in enumerate(images, 1)
    )
    all_determinations: list[dict[str, Any]] = []
    all_candidates: list[dict[str, Any]] = []
    event_streams: list[str] = []
    with tempfile.TemporaryDirectory(prefix="lq-review-batches-") as temporary:
        temporary_root = Path(temporary)
        for batch_index, (offset, batch) in enumerate(batches, 1):
            batch_output = temporary_root / f"batch-{batch_index:04d}.json"
            rendered_prompt = batch_prompt(
                prompt, original_assignment, batch, batch_index, len(batches)
            )
            if images:
                rendered_prompt += (
                    "\n\n# Attached verified review pages\n\n"
                    + page_map
                    + "\nInspect every attachment. Use its mapped document ordinal "
                    "and page.\n"
                )
            command = [
                args.codex,
                "exec",
                "--json",
                "--ephemeral",
                "--ignore-user-config",
                "--ignore-rules",
                "--skip-git-repo-check",
                "--sandbox",
                "read-only",
                "--model",
                args.model,
                "-c",
                f'model_reasoning_effort="{args.effort}"',
                "--output-schema",
                args.schema,
                "--output-last-message",
                str(batch_output),
                "--cd",
                str(Path(args.room_root).resolve()),
            ]
            for _, _, path in images:
                command.extend(["--image", str(path)])
            command.extend(["--", "-"])
            completed = subprocess.run(
                command,
                input=rendered_prompt,
                text=True,
                check=False,
                capture_output=True,
            )
            event_streams.append(completed.stdout)
            if completed.stdout:
                print(completed.stdout, end="")
            if completed.stderr:
                print(completed.stderr, end="", file=sys.stderr)
            if completed.returncode != 0:
                return completed.returncode
            try:
                raw_batch = load_object(batch_output, f"batch {batch_index} result")
                determinations, candidates = validate_batch_result(
                    raw_batch, batch, offset
                )
            except OSError as error:
                print(f"run_codex_finding_worker: {error}", file=sys.stderr)
                if batch_output.exists():
                    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(batch_output, args.output)
                    break
                return 3
            all_determinations.extend(determinations)
            all_candidates.extend(candidates)
        else:
            unique_candidates = {
                json.dumps(candidate, sort_keys=True, separators=(",", ":")): candidate
                for candidate in all_candidates
            }
            dump_atomic(
                Path(args.output),
                {
                    "contract": "finding-worker/2",
                    "determinations": all_determinations,
                    "job_id": assignment.get("job_id"),
                    "privilege_candidates": [
                        unique_candidates[key] for key in sorted(unique_candidates)
                    ],
                    "review_plan_id": assignment.get("review_plan_id"),
                },
            )
    usage = usage_from_events("\n".join(event_streams))
    if usage is not None and args.usage_out:
        write_usage(Path(args.usage_out), assignment, args.model, args.effort, usage)
    if completed.returncode == 0 and args.require_usage and usage is None:
        print(
            "run_codex_finding_worker: completed without token telemetry",
            file=sys.stderr,
        )
        return 3
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
