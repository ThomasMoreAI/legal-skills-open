"""Strict text decoding and lossless, bounded canonical units."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass


class TextDecodeError(ValueError):
    """Bytes cannot be represented by the v1 strict UTF-8 contract."""


@dataclass(frozen=True)
class DecodedText:
    text: str
    had_bom: bool


def decode_text(data: bytes) -> DecodedText:
    had_bom = data.startswith(b"\xef\xbb\xbf")
    payload = data[3:] if had_bom else data
    try:
        text = payload.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise TextDecodeError("text is not strict UTF-8") from exc
    if "\x00" in text:
        raise TextDecodeError("text contains a NUL character")
    return DecodedText(
        text=text.replace("\r\n", "\n").replace("\r", "\n"), had_bom=had_bom
    )


def _chunks(text: str, max_bytes: int) -> list[tuple[str, int, int]]:
    if max_bytes <= 0:
        raise ValueError("max_unit_bytes must be positive")
    chunks: list[tuple[str, int, int]] = []
    buffer: list[str] = []
    buffer_bytes = 0
    byte_offset = 0
    for character in text:
        encoded_length = len(character.encode("utf-8"))
        if encoded_length > max_bytes:
            raise TextDecodeError("one character exceeds the unit byte limit")
        if buffer and buffer_bytes + encoded_length > max_bytes:
            value = "".join(buffer)
            chunks.append((value, byte_offset, byte_offset + buffer_bytes))
            byte_offset += buffer_bytes
            buffer = []
            buffer_bytes = 0
        buffer.append(character)
        buffer_bytes += encoded_length
    if buffer:
        value = "".join(buffer)
        chunks.append((value, byte_offset, byte_offset + buffer_bytes))
    return chunks


def make_text_units(
    container_id: str,
    data: bytes,
    *,
    kind: str,
    role: str,
    eligibility: str = "eligible",
    source_class: str = "documentary_supported",
    source_author: str | None = None,
    source_time: str | None = None,
    origin_id: str | None = None,
    locator_prefix: str | None = None,
    unit_start: int = 1,
    max_unit_bytes: int = 64 * 1024,
) -> list[dict]:
    decoded = decode_text(data)
    prefix = locator_prefix or f"text:{container_id}"
    units = []
    for offset, (value, start, end) in enumerate(
        _chunks(decoded.text, max_unit_bytes), start=unit_start
    ):
        canonical = value.encode("utf-8")
        units.append(
            {
                "unitId": f"{container_id}-U{offset:04d}",
                "containerId": container_id,
                "originId": origin_id or container_id,
                "kind": kind,
                "role": role,
                "locator": f"{prefix}#utf8={start}:{end}",
                "canonicalText": value,
                "canonicalUtf8Sha256": hashlib.sha256(canonical).hexdigest(),
                "utf8Start": start,
                "utf8End": end,
                "eligibility": eligibility,
                "coverageDisposition": "pending",
                "sourceClass": source_class,
                "sourceAuthor": source_author,
                "sourceTime": source_time,
            }
        )
    return units
