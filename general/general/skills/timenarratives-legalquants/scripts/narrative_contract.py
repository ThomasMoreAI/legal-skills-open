"""Deterministic shape and size rules for copy-ready narrative text."""

from __future__ import annotations

import re
import unicodedata
from typing import Any

MAX_PARAGRAPHS = 2
MAX_PARAGRAPH_WORDS = 60
MAX_PARAGRAPH_CODEPOINTS = 600
MAX_TEXT_CODEPOINTS = 1202

_MARKDOWN_BLOCK = re.compile(r"^[#>*+_`~<\[\-]")
_MARKDOWN_ESCAPE = re.compile(r"\\[!\"#$%&'()*+,\-./:;<=>?@\[\]^_`{|}~]")
_MARKDOWN_INLINE = re.compile(r"[<>\[\]]")
_MARKDOWN_ENTITY = re.compile(
    r"&(?:#\d{1,7}|#x[0-9A-Fa-f]{1,6}|[A-Za-z][A-Za-z0-9]{1,31});"
)
_RENDERER_LABELS = (
    "status:",
    "support:",
    "packet scope:",
    "packet reconciliation:",
    "workday completeness:",
    "posting state:",
    "exceptions recorded:",
)


def _noncanonical_character(character: str) -> bool:
    """Return whether a character can conceal layout or machine-visible content."""
    if character in {"\n", " "}:
        return False
    category = unicodedata.category(character)
    codepoint = ord(character)
    invisible_mark = (
        character == "\u034f"
        or 0x115F <= codepoint <= 0x1160
        or 0x17B4 <= codepoint <= 0x17B5
        or 0x180B <= codepoint <= 0x180F
        or codepoint in {0x2065, 0x3164, 0xFFA0}
        or 0xFE00 <= codepoint <= 0xFE0F
        or 0xFFF0 <= codepoint <= 0xFFF8
        or 0xE0000 <= codepoint <= 0xE0FFF
    )
    return (
        character.isspace()
        or category in {"Cc", "Cf", "Cs"}
        or category in {"Zl", "Zp"}
        or invisible_mark
    )


def narrative_text_faults(value: Any) -> list[str]:
    """Return stable fault codes for a model-authored narrative string."""
    if not isinstance(value, str) or not value or value != value.strip():
        return ["narrative_layout"]
    if "  " in value or any(_noncanonical_character(char) for char in value):
        return ["narrative_layout"]

    paragraphs = value.split("\n\n")
    if (
        not 1 <= len(paragraphs) <= MAX_PARAGRAPHS
        or any(
            not paragraph or paragraph != paragraph.strip() for paragraph in paragraphs
        )
        or any("\n" in paragraph for paragraph in paragraphs)
    ):
        return ["narrative_layout"]

    faults: list[str] = []
    for paragraph in paragraphs:
        if re.search(r"[A-Za-z]", paragraph) is None:
            faults.append("narrative_layout")
        if len(paragraph) > MAX_PARAGRAPH_CODEPOINTS:
            faults.append("narrative_character_limit")
        if len(paragraph.split(" ")) > MAX_PARAGRAPH_WORDS:
            faults.append("narrative_word_limit")
        folded = paragraph.casefold()
        if (
            _MARKDOWN_ESCAPE.search(paragraph)
            or _MARKDOWN_ENTITY.search(paragraph)
            or _MARKDOWN_INLINE.search(paragraph)
            or _MARKDOWN_BLOCK.match(paragraph)
            or folded.startswith(_RENDERER_LABELS)
        ):
            faults.append("narrative_markdown_block")
    return list(dict.fromkeys(faults))
