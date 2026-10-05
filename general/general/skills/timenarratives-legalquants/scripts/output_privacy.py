"""Redacted path and normalized verbatim-excerpt gates for authored output."""

from __future__ import annotations

import re
from collections.abc import Iterable
from typing import Any

from prohibited_output import (
    AuthoredText,
    iter_model_authored_text,
    iter_rendered_authored_text,
    normalize_authored,
)
from prohibited_output import scan_model_output as _prohibited_model
from prohibited_output import scan_rendered as _prohibited_rendered

Issue = dict[str, str]
MIN_EXCERPT_WORDS = 8
MIN_EXCERPT_CHARS = 48
MIN_COMPLETE_SOURCE_WORDS = 5
MIN_COMPLETE_SOURCE_CHARS = 24
WORD = re.compile(r"\w+(?:['.-]\w+)*", re.UNICODE)
PATH_PATTERNS = (
    re.compile(r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]"),
    re.compile(r"\\\\[^\s\\/]+[\\/][^\s\\/]+"),
    re.compile(r"(?<!:)//[^\s/]+/[^\s/]+"),
    re.compile(r"\bfile://", re.IGNORECASE),
    re.compile(
        r"(?<![\w:/])/(?:home|users|tmp|var|etc|opt|usr|mnt|srv|root|"
        r"workspace|private|volumes|data)(?:/|\b)",
        re.IGNORECASE,
    ),
)


def _normalize_words(text: str) -> list[str]:
    return WORD.findall(normalize_authored(text))


def _contains_excerpt(text: str, sources: list[list[str]]) -> bool:
    words = _normalize_words(text)
    for source in sources:
        if (
            len(source) >= MIN_COMPLETE_SOURCE_WORDS
            and len(" ".join(source)) >= MIN_COMPLETE_SOURCE_CHARS
            and any(
                words[index : index + len(source)] == source
                for index in range(len(words) - len(source) + 1)
            )
        ):
            return True
    for start in range(len(words) - MIN_EXCERPT_WORDS + 1):
        for end in range(start + MIN_EXCERPT_WORDS, len(words) + 1):
            candidate = words[start:end]
            if len(" ".join(candidate)) < MIN_EXCERPT_CHARS:
                continue
            if any(
                source[index : index + len(candidate)] == candidate
                for source in sources
                for index in range(len(source) - len(candidate) + 1)
            ):
                return True
            break
    return False


def _packet_sources(packet: dict[str, Any] | None) -> list[list[str]]:
    if not isinstance(packet, dict):
        return []
    units = packet.get("units")
    if not isinstance(units, list):
        return []
    return [
        _normalize_words(row["canonicalText"])
        for row in units
        if isinstance(row, dict) and isinstance(row.get("canonicalText"), str)
    ]


def _scan_text(text: str, path: str, sources: list[list[str]]) -> list[Issue]:
    out: list[Issue] = []
    normalized = normalize_authored(text)
    if any(pattern.search(normalized) for pattern in PATH_PATTERNS):
        out.append({"code": "absolute_path_disclosure", "path": path})
    if sources and _contains_excerpt(text, sources):
        out.append({"code": "packet_excerpt", "path": path})
    return out


def _privacy(
    fields: Iterable[AuthoredText], packet: dict[str, Any] | None
) -> list[Issue]:
    sources = _packet_sources(packet)
    return [issue for path, text in fields for issue in _scan_text(text, path, sources)]


def scan_model_output(value: object, packet: dict[str, Any]) -> list[Issue]:
    return [
        *_prohibited_model(value),
        *_privacy(iter_model_authored_text(value), packet),
    ]


def scan_rendered(
    deliverable: object,
    markdown: str,
    packet: dict[str, Any] | None = None,
) -> list[Issue]:
    return [
        *_prohibited_rendered(deliverable, markdown),
        *_privacy(iter_rendered_authored_text(deliverable, markdown), packet),
    ]
