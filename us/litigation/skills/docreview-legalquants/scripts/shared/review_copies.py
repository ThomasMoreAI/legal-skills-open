#!/usr/bin/env python3
"""Build and verify deterministic, hash-bound offline review copies.

The sidecar binds every manifest row to the complete source hash and to each
byte of every derivative.  It contains no timestamps or absolute paths.  The
same module also renders conservative HTML components from a successfully
revalidated sidecar; it never mutates findings or evidence receipts.

Usage:
    python3 review_copies.py build --manifest manifest.json \
        --source-root room --sidecar review-copies.json \
        --bundle-root review-copies --mode auto
    python3 review_copies.py verify --manifest manifest.json \
        --source-root room --sidecar review-copies.json
"""

from __future__ import annotations

import argparse
import hashlib
import html
import io
import json
import mimetypes
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.parse
import zipfile
import zlib
from dataclasses import dataclass
from email import policy
from email.parser import BytesParser
from pathlib import Path, PurePosixPath
from typing import Any
from xml.etree import ElementTree

SCHEMA_VERSION = "lq-review-copies-v1"
RENDERER_VERSION = "2"
TEXT_EXTENSIONS = {
    "csv",
    "htm",
    "html",
    "json",
    "log",
    "md",
    "text",
    "txt",
    "xml",
}
IMAGE_MEDIA_TYPES = {
    "bmp": "image/bmp",
    "gif": "image/gif",
    "jpeg": "image/jpeg",
    "jpg": "image/jpeg",
    "png": "image/png",
    "webp": "image/webp",
}
OFFICE_EXTENSIONS = {"docx", "pptx", "xlsx"}
MAX_ZIP_MEMBERS = 20_000
MAX_ZIP_UNCOMPRESSED_BYTES = 512 * 1024 * 1024
SHA256_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
DOC_ID_RE = re.compile(r"^sha256:[0-9a-f]{12}$")


class ReviewCopyError(ValueError):
    """A fail-closed path, schema, or containment error."""


@dataclass(frozen=True)
class ValidationResult:
    """Result of a full sidecar, source, and derivative revalidation."""

    integrity_ok: bool
    ready: bool
    errors: tuple[str, ...]
    sidecar: dict[str, Any] | None
    sidecar_path: Path


@dataclass(frozen=True)
class BuildResult:
    """Result returned after the sidecar has been written and revalidated."""

    sidecar: dict[str, Any]
    validation: ValidationResult


def canonical_json_bytes(value: Any) -> bytes:
    """Return the canonical bytes used by all digests in this contract."""

    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def canonical_digest(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def _bytes_digest(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def _file_digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ReviewCopyError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _load_json(path: Path) -> Any:
    try:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle, object_pairs_hook=_reject_duplicate_keys)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ReviewCopyError(f"could not read JSON {path.name}: {exc}") from exc


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _relative_parts(value: str, label: str) -> tuple[str, ...]:
    if not isinstance(value, str) or not value:
        raise ReviewCopyError(f"{label} must be a non-empty relative path")
    if "\\" in value:
        raise ReviewCopyError(f"{label} must use forward slashes")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise ReviewCopyError(f"{label} escapes its allowed root: {value}")
    return path.parts


def _is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _contained_source(root: Path, relative: str) -> Path:
    parts = _relative_parts(relative, "manifest document path")
    lexical = root.joinpath(*parts)
    try:
        resolved = lexical.resolve(strict=True)
    except OSError as exc:
        raise ReviewCopyError(f"source is missing or unreadable: {relative}") from exc
    if not _is_relative_to(resolved, root):
        raise ReviewCopyError(f"source symlink escapes the source root: {relative}")
    if not resolved.is_file():
        raise ReviewCopyError(f"source is not a regular file: {relative}")
    return resolved


def _assert_no_output_symlink(base: Path, parts: tuple[str, ...]) -> None:
    current = base
    for part in parts:
        current = current / part
        if current.is_symlink():
            raise ReviewCopyError(
                f"bundle path contains a symlink and is refused: {current.name}"
            )


def _bundle_directory(sidecar_path: Path, bundle_root: str, *, create: bool) -> Path:
    parts = _relative_parts(bundle_root, "bundle_root")
    sidecar_parent = sidecar_path.parent.resolve()
    _assert_no_output_symlink(sidecar_parent, parts)
    bundle = sidecar_parent.joinpath(*parts)
    if create:
        bundle.mkdir(parents=True, exist_ok=True)
    try:
        resolved = bundle.resolve(strict=True)
    except OSError as exc:
        raise ReviewCopyError("review-copy bundle is missing") from exc
    if not _is_relative_to(resolved, sidecar_parent):
        raise ReviewCopyError("bundle_root escapes the sidecar directory")
    if not resolved.is_dir():
        raise ReviewCopyError("bundle_root is not a directory")
    return resolved


def _renderer(name: str, version: str = RENDERER_VERSION) -> dict[str, str]:
    return {"name": name, "version": version}


def _safe_extension(value: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "", value.casefold())
    return cleaned[:12] or "bin"


def _write_derivative(
    bundle: Path,
    data: bytes,
    *,
    extension: str,
    media_type: str,
    role: str,
    renderer: dict[str, str],
    page: int | None = None,
) -> dict[str, Any]:
    digest = hashlib.sha256(data).hexdigest()
    extension = _safe_extension(extension)
    relative = f"objects/{digest[:2]}/{digest}.{extension}"
    parts = _relative_parts(relative, "derivative path")
    _assert_no_output_symlink(bundle, parts)
    target = bundle.joinpath(*parts)
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.is_symlink():
        raise ReviewCopyError("refusing to replace a symlinked derivative")
    if target.exists() and target.read_bytes() != data:
        raise ReviewCopyError("content-addressed derivative contains different bytes")
    target.write_bytes(data)
    derivative: dict[str, Any] = {
        "bytes": len(data),
        "media_type": media_type,
        "path": relative,
        "renderer": renderer,
        "role": role,
        "sha256": "sha256:" + digest,
    }
    if page is not None:
        derivative["page"] = page
    return derivative


def _decode_text(data: bytes) -> str:
    binary_signatures = (
        b"%PDF-",
        b"\x89PNG\r\n\x1a\n",
        b"\xff\xd8\xff",
        b"GIF87a",
        b"GIF89a",
        b"BM",
        b"PK\x03\x04",
        b"PK\x05\x06",
        b"PK\x07\x08",
        b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1",
    )
    if data.startswith(binary_signatures) or (
        data.startswith(b"RIFF") and data[8:12] == b"WEBP"
    ):
        raise ReviewCopyError("file bytes do not match a text format")
    utf16 = data.startswith((b"\xff\xfe", b"\xfe\xff"))
    if b"\x00" in data and not utf16:
        raise ReviewCopyError("file bytes do not match a text format")
    encodings = ["utf-16"] if utf16 else ["utf-8-sig", "cp1252", "latin-1"]
    for encoding in encodings:
        try:
            text = data.decode(encoding)
        except UnicodeDecodeError:
            continue
        non_text = sum(
            not character.isprintable() and character not in "\t\n\r\f"
            for character in text
        )
        if non_text > max(1, len(text) // 100):
            continue
        return text
    raise ReviewCopyError("text could not be decoded")


def _replace_surrogates(value: str) -> str:
    """Return UTF-8-safe text while preserving every valid Unicode scalar."""

    return "".join(
        "\ufffd" if 0xD800 <= ord(character) <= 0xDFFF else character
        for character in value
    )


def _text_review_html(title: str, text: str, *, label: str = "Full text") -> bytes:
    safe_title = html.escape(_replace_surrogates(title), quote=True)
    safe_label = html.escape(_replace_surrogates(label), quote=True)
    safe_text = html.escape(_replace_surrogates(text), quote=False)
    document = (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        f"<title>{safe_title}</title><style>"
        ":root{color-scheme:light dark}body{margin:0;padding:1rem;"
        "font:400 15px/1.55 system-ui,-apple-system,sans-serif;"
        "background:Canvas;color:CanvasText}h1{font-size:1rem;font-weight:500;"
        "margin:0 0 .75rem}pre{font:400 13px/1.55 ui-monospace,monospace;"
        "white-space:pre-wrap;overflow-wrap:anywhere;margin:0}"
        "</style></head><body>"
        f"<h1>{safe_label}: {safe_title}</h1><pre>{safe_text}</pre>"
        "</body></html>"
    )
    return document.encode("utf-8")


MAX_IMAGE_DECODE_BYTES = 256 * 1024 * 1024


def _subblocks_end(data: bytes, offset: int) -> tuple[int, bool]:
    while offset < len(data):
        size = data[offset]
        offset += 1
        if size == 0:
            return offset, True
        offset += size
        if offset > len(data):
            return offset, False
    return offset, False


def _subblocks_payload(data: bytes, offset: int) -> tuple[int, bytes | None]:
    payload = bytearray()
    while offset < len(data):
        size = data[offset]
        offset += 1
        if size == 0:
            return offset, bytes(payload)
        end = offset + size
        if end > len(data):
            return end, None
        payload.extend(data[offset:end])
        offset = end
    return offset, None


def _gif_lzw_size(data: bytes, minimum_code_size: int, limit: int) -> int | None:
    clear = 1 << minimum_code_size
    end = clear + 1
    table = {index: bytes([index]) for index in range(clear)}
    next_code = end + 1
    code_size = minimum_code_size + 1
    bit_offset = 0
    previous: bytes | None = None
    output_size = 0
    while bit_offset + code_size <= len(data) * 8:
        byte_offset = bit_offset // 8
        shift = bit_offset % 8
        window = int.from_bytes(data[byte_offset : byte_offset + 3], "little")
        code = (window >> shift) & ((1 << code_size) - 1)
        bit_offset += code_size
        if code == clear:
            table = {index: bytes([index]) for index in range(clear)}
            next_code = end + 1
            code_size = minimum_code_size + 1
            previous = None
            continue
        if code == end:
            return output_size
        if code in table:
            entry = table[code]
        elif code == next_code and previous is not None:
            entry = previous + previous[:1]
        else:
            return None
        output_size += len(entry)
        if output_size > limit:
            return None
        if previous is not None and next_code < 4096:
            table[next_code] = previous + entry[:1]
            next_code += 1
            if next_code == (1 << code_size) and code_size < 12:
                code_size += 1
        previous = entry
    return None


def _png_is_reviewable(data: bytes) -> bool:
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        return False
    offset = 8
    ihdr: bytes | None = None
    idat = bytearray()
    saw_iend = False
    while offset + 12 <= len(data):
        length = int.from_bytes(data[offset : offset + 4], "big")
        chunk_type = data[offset + 4 : offset + 8]
        end = offset + 12 + length
        if end > len(data):
            return False
        payload = data[offset + 8 : offset + 8 + length]
        expected_crc = int.from_bytes(data[offset + 8 + length : end], "big")
        if zlib.crc32(chunk_type + payload) & 0xFFFFFFFF != expected_crc:
            return False
        if ihdr is None:
            if chunk_type != b"IHDR" or length != 13:
                return False
            ihdr = payload
        elif chunk_type == b"IDAT":
            idat.extend(payload)
        elif chunk_type == b"IEND":
            if length != 0:
                return False
            saw_iend = True
            offset = end
            break
        offset = end
    if not saw_iend or offset != len(data) or ihdr is None or not idat:
        return False
    width = int.from_bytes(ihdr[0:4], "big")
    height = int.from_bytes(ihdr[4:8], "big")
    bit_depth, color_type, compression, filtering, interlace = ihdr[8:13]
    allowed_depths = {
        0: {1, 2, 4, 8, 16},
        2: {8, 16},
        3: {1, 2, 4, 8},
        4: {8, 16},
        6: {8, 16},
    }
    channels = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}
    if (
        width < 1
        or height < 1
        or bit_depth not in allowed_depths.get(color_type, set())
        or compression != 0
        or filtering != 0
        or interlace not in {0, 1}
    ):
        return False
    try:
        decompressor = zlib.decompressobj()
        decoded = decompressor.decompress(bytes(idat), MAX_IMAGE_DECODE_BYTES + 1)
        if len(decoded) > MAX_IMAGE_DECODE_BYTES or not decompressor.eof:
            return False
        decoded += decompressor.flush()
    except zlib.error:
        return False
    if len(decoded) > MAX_IMAGE_DECODE_BYTES:
        return False
    bits_per_pixel = channels[color_type] * bit_depth
    passes = (
        ((0, 0, 1, 1),)
        if interlace == 0
        else (
            (0, 0, 8, 8),
            (4, 0, 8, 8),
            (0, 4, 4, 8),
            (2, 0, 4, 4),
            (0, 2, 2, 4),
            (1, 0, 2, 2),
            (0, 1, 1, 2),
        )
    )
    cursor = 0
    for x_start, y_start, x_step, y_step in passes:
        pass_width = max(0, (width - x_start + x_step - 1) // x_step)
        pass_height = max(0, (height - y_start + y_step - 1) // y_step)
        if not pass_width or not pass_height:
            continue
        row_bytes = (pass_width * bits_per_pixel + 7) // 8
        for _row in range(pass_height):
            if cursor + 1 + row_bytes > len(decoded) or decoded[cursor] > 4:
                return False
            cursor += 1 + row_bytes
    return cursor == len(decoded)


def _jpeg_is_reviewable(data: bytes) -> bool:
    if (
        len(data) < 12
        or not data.startswith(b"\xff\xd8")
        or not data.endswith(b"\xff\xd9")
    ):
        return False
    offset = 2
    saw_frame = False
    saw_quantization = False
    saw_huffman = False
    while offset < len(data) - 2:
        if data[offset] != 0xFF:
            return False
        while offset < len(data) and data[offset] == 0xFF:
            offset += 1
        if offset >= len(data):
            return False
        marker = data[offset]
        offset += 1
        if marker == 0xDA:
            if offset + 2 > len(data):
                return False
            length = int.from_bytes(data[offset : offset + 2], "big")
            if (
                not saw_frame
                or not saw_quantization
                or not saw_huffman
                or length < 6
                or offset + length >= len(data) - 2
            ):
                return False
            cursor = offset + length
            entropy_bytes = 0
            while cursor < len(data) - 1:
                if data[cursor] != 0xFF:
                    entropy_bytes += 1
                    cursor += 1
                    continue
                if cursor + 1 >= len(data):
                    return False
                following = data[cursor + 1]
                if following == 0x00:
                    entropy_bytes += 1
                    cursor += 2
                    continue
                if 0xD0 <= following <= 0xD7:
                    cursor += 2
                    continue
                return (
                    following == 0xD9 and cursor + 2 == len(data) and entropy_bytes > 0
                )
            return False
        if marker in {0x01, *range(0xD0, 0xD9)}:
            continue
        if offset + 2 > len(data):
            return False
        length = int.from_bytes(data[offset : offset + 2], "big")
        if length < 2 or offset + length > len(data):
            return False
        if marker in {
            0xC0,
            0xC1,
            0xC2,
            0xC3,
            0xC5,
            0xC6,
            0xC7,
            0xC9,
            0xCA,
            0xCB,
            0xCD,
            0xCE,
            0xCF,
        }:
            if length < 8:
                return False
            height = int.from_bytes(data[offset + 3 : offset + 5], "big")
            width = int.from_bytes(data[offset + 5 : offset + 7], "big")
            saw_frame = width > 0 and height > 0
        elif marker == 0xDB:
            saw_quantization = True
        elif marker == 0xC4:
            saw_huffman = True
        offset += length
    return False


def _gif_is_reviewable(data: bytes) -> bool:
    if len(data) < 14 or not data.startswith((b"GIF87a", b"GIF89a")):
        return False
    if (
        int.from_bytes(data[6:8], "little") < 1
        or int.from_bytes(data[8:10], "little") < 1
    ):
        return False
    packed = data[10]
    offset = 13 + (3 * (2 ** ((packed & 0x07) + 1)) if packed & 0x80 else 0)
    saw_image = False
    while offset < len(data):
        marker = data[offset]
        offset += 1
        if marker == 0x3B:
            return saw_image and offset == len(data)
        if marker == 0x21:
            if offset >= len(data):
                return False
            offset, okay = _subblocks_end(data, offset + 1)
            if not okay:
                return False
            continue
        if marker != 0x2C or offset + 9 > len(data):
            return False
        width = int.from_bytes(data[offset + 4 : offset + 6], "little")
        height = int.from_bytes(data[offset + 6 : offset + 8], "little")
        packed = data[offset + 8]
        offset += 9
        if width < 1 or height < 1:
            return False
        if packed & 0x80:
            offset += 3 * (2 ** ((packed & 0x07) + 1))
        if offset >= len(data) or not 2 <= data[offset] <= 8:
            return False
        minimum_code_size = data[offset]
        offset, payload = _subblocks_payload(data, offset + 1)
        if (
            payload is None
            or _gif_lzw_size(payload, minimum_code_size, width * height)
            != width * height
        ):
            return False
        saw_image = True
    return False


def _webp_is_reviewable(data: bytes) -> bool:
    if (
        len(data) < 20
        or data[:4] != b"RIFF"
        or data[8:12] != b"WEBP"
        or int.from_bytes(data[4:8], "little") + 8 != len(data)
    ):
        return False
    offset = 12
    saw_image = False
    while offset + 8 <= len(data):
        kind = data[offset : offset + 4]
        size = int.from_bytes(data[offset + 4 : offset + 8], "little")
        payload_end = offset + 8 + size
        if payload_end > len(data):
            return False
        payload = data[offset + 8 : payload_end]
        if kind == b"VP8X" and len(payload) >= 10:
            if (
                int.from_bytes(payload[4:7], "little") + 1 < 1
                or int.from_bytes(payload[7:10], "little") + 1 < 1
            ):
                return False
        elif kind == b"VP8 " and len(payload) >= 10:
            frame_tag = int.from_bytes(payload[:3], "little")
            width = int.from_bytes(payload[6:8], "little") & 0x3FFF
            height = int.from_bytes(payload[8:10], "little") & 0x3FFF
            saw_image = (
                frame_tag & 1 == 0
                and payload[3:6] == b"\x9d\x01\x2a"
                and width > 0
                and height > 0
                and (frame_tag >> 5) <= len(payload) - 3
                and len(payload) > 10
            )
        elif kind == b"VP8L" and len(payload) >= 5:
            bits = int.from_bytes(payload[1:5], "little")
            width = (bits & 0x3FFF) + 1
            height = ((bits >> 14) & 0x3FFF) + 1
            saw_image = (
                payload[0] == 0x2F and width > 0 and height > 0 and len(payload) > 5
            )
        offset = payload_end + (size & 1)
    return saw_image and offset == len(data)


def _bmp_is_reviewable(data: bytes) -> bool:
    if len(data) < 30 or not data.startswith(b"BM"):
        return False
    file_size = int.from_bytes(data[2:6], "little")
    pixel_offset = int.from_bytes(data[10:14], "little")
    dib_size = int.from_bytes(data[14:18], "little")
    if file_size != len(data) or dib_size < 12 or 14 + dib_size > len(data):
        return False
    if dib_size == 12:
        width = int.from_bytes(data[18:20], "little")
        height = int.from_bytes(data[20:22], "little")
        planes = int.from_bytes(data[22:24], "little")
        bits_per_pixel = int.from_bytes(data[24:26], "little")
        compression = 0
    else:
        width = int.from_bytes(data[18:22], "little", signed=True)
        height = int.from_bytes(data[22:26], "little", signed=True)
        planes = int.from_bytes(data[26:28], "little")
        bits_per_pixel = int.from_bytes(data[28:30], "little")
        compression = int.from_bytes(data[30:34], "little") if dib_size >= 40 else 0
    if (
        width == 0
        or height == 0
        or planes != 1
        or bits_per_pixel not in {1, 4, 8, 16, 24, 32}
        or compression not in {0, 3}
        or not 14 + dib_size <= pixel_offset < len(data)
    ):
        return False
    if compression != 0:
        return len(data) - pixel_offset > 0
    row_bytes = ((abs(width) * bits_per_pixel + 31) // 32) * 4
    return pixel_offset + row_bytes * abs(height) <= len(data)


def _image_media_type(ext: str, data: bytes) -> str | None:
    ext = ext.casefold()
    validators = {
        "bmp": _bmp_is_reviewable,
        "gif": _gif_is_reviewable,
        "jpeg": _jpeg_is_reviewable,
        "jpg": _jpeg_is_reviewable,
        "png": _png_is_reviewable,
        "webp": _webp_is_reviewable,
    }
    validator = validators.get(ext)
    return IMAGE_MEDIA_TYPES.get(ext) if validator and validator(data) else None


def _xref_stream_is_reviewable(data: bytes, offset: int) -> bool:
    section = data[offset:]
    object_header = re.match(rb"(\d+)\s+(\d+)\s+obj\b", section)
    if object_header is None:
        return False
    stream_marker = re.search(
        rb"\bstream(?:\r\n|\r|\n)", section[object_header.end() :]
    )
    if stream_marker is None:
        return False
    stream_start = object_header.end() + stream_marker.end()
    dictionary = section[
        object_header.end() : object_header.end() + stream_marker.start()
    ]
    if not re.search(rb"/Type\s*/XRef\b", dictionary):
        return False
    length_match = re.search(rb"/Length\s+(\d+)\b", dictionary)
    widths_match = re.search(rb"/W\s*\[\s*(\d+)\s+(\d+)\s+(\d+)\s*\]", dictionary)
    root_match = re.search(rb"/Root\s+(\d+)\s+(\d+)\s+R\b", dictionary)
    size_match = re.search(rb"/Size\s+(\d+)\b", dictionary)
    if None in (length_match, widths_match, root_match, size_match):
        return False
    assert length_match is not None
    assert widths_match is not None
    assert root_match is not None
    assert size_match is not None
    length = int(length_match.group(1))
    stream_end = stream_start + length
    if stream_end > len(section):
        return False
    suffix = section[stream_end:]
    if not re.match(rb"(?:\r\n|\r|\n)endstream\s+endobj\b", suffix):
        return False
    payload = section[stream_start:stream_end]
    filters = re.findall(rb"/Filter\s*/([A-Za-z0-9]+)", dictionary)
    if filters:
        if filters != [b"FlateDecode"]:
            return False
        try:
            payload = zlib.decompress(payload)
        except zlib.error:
            return False
    widths = tuple(int(widths_match.group(index)) for index in range(1, 4))
    record_width = sum(widths)
    if record_width < 1:
        return False
    index_match = re.search(rb"/Index\s*\[([^]]+)\]", dictionary)
    if index_match is None:
        record_count = int(size_match.group(1))
    else:
        values = [int(value) for value in re.findall(rb"\d+", index_match.group(1))]
        if not values or len(values) % 2:
            return False
        record_count = sum(values[index] for index in range(1, len(values), 2))
    predictor_match = re.search(rb"/Predictor\s+(\d+)\b", dictionary)
    predictor = int(predictor_match.group(1)) if predictor_match else 1
    if predictor == 1:
        if len(payload) != record_count * record_width:
            return False
    elif 10 <= predictor <= 15:
        columns_match = re.search(rb"/Columns\s+(\d+)\b", dictionary)
        columns = int(columns_match.group(1)) if columns_match else 1
        row_width = columns + 1
        if (
            columns != record_width
            or len(payload) != record_count * row_width
            or any(payload[index] > 4 for index in range(0, len(payload), row_width))
        ):
            return False
    else:
        return False
    root_number = int(root_match.group(1))
    root_generation = int(root_match.group(2))
    root = re.search(
        rb"(?:^|[\r\n])"
        + str(root_number).encode("ascii")
        + rb"\s+"
        + str(root_generation).encode("ascii")
        + rb"\s+obj\b",
        data,
    )
    if root is None:
        return False
    root_end = data.find(b"endobj", root.end())
    if root_end <= root.end():
        return False
    root_body = data[root.end() : root_end]
    return bool(
        re.search(rb"/Type\s*/Catalog\b", root_body)
        and re.search(rb"/Pages\s+\d+\s+\d+\s+R\b", root_body)
    )


def _pdf_is_reviewable(data: bytes) -> bool:
    if not re.match(rb"%PDF-[12]\.\d", data[:16]) or b"%%EOF" not in data[-4096:]:
        return False
    start = re.search(rb"startxref\s+(\d+)\s+%%EOF\s*$", data, re.DOTALL)
    if start is None:
        return False
    offset = int(start.group(1))
    if offset < 0 or offset >= len(data):
        return False
    xref = data[offset:].lstrip()
    if not xref.startswith(b"xref"):
        return _xref_stream_is_reviewable(data, offset)
    if not (
        re.search(rb"/Type\s*/Pages\b", data)
        and re.search(rb"/Type\s*/Page\b", data)
        and re.search(rb"/(?:MediaBox|CropBox)\s*\[", data)
    ):
        return False
    cursor = 4
    live_entries: dict[int, int] = {}
    while True:
        while cursor < len(xref) and xref[cursor] in b" \t\r\n":
            cursor += 1
        if cursor >= len(xref):
            return False
        if xref[cursor : cursor + 7] == b"trailer":
            cursor += 7
            break
        subsection = re.match(rb"(\d+)\s+(\d+)\s*\r?\n", xref[cursor:])
        if subsection is None:
            return False
        first = int(subsection.group(1))
        count = int(subsection.group(2))
        cursor += subsection.end()
        for index in range(count):
            entry = re.match(rb"(\d{10})\s+(\d{5})\s+([nf])\s*\r?\n", xref[cursor:])
            if entry is None:
                return False
            object_offset = int(entry.group(1))
            generation = int(entry.group(2))
            cursor += entry.end()
            if entry.group(3) == b"n":
                object_number = first + index
                expected = f"{object_number} {generation} obj".encode("ascii")
                if object_offset >= len(data) or not data[object_offset:].startswith(
                    expected
                ):
                    return False
                live_entries[object_number] = object_offset
    trailer = re.match(rb"\s*<<(.*?)>>", xref[cursor:], re.DOTALL)
    if trailer is None:
        return False
    root = re.search(rb"/Root\s+(\d+)\s+(\d+)\s+R\b", trailer.group(1))
    if root is None:
        return False
    root_number = int(root.group(1))
    root_offset = live_entries.get(root_number)
    if root_offset is None:
        return False
    root_end = data.find(b"endobj", root_offset)
    return root_end > root_offset and bool(
        re.search(rb"/Type\s*/Catalog\b", data[root_offset:root_end])
    )


def _zip_parts(data: bytes) -> tuple[zipfile.ZipFile, list[zipfile.ZipInfo]]:
    stream = io.BytesIO(data)
    try:
        archive = zipfile.ZipFile(stream)
        infos = archive.infolist()
    except (OSError, zipfile.BadZipFile) as exc:
        raise ReviewCopyError("Office file is not a readable OOXML package") from exc
    if len(infos) > MAX_ZIP_MEMBERS:
        archive.close()
        raise ReviewCopyError("Office package has too many members")
    if sum(info.file_size for info in infos) > MAX_ZIP_UNCOMPRESSED_BYTES:
        archive.close()
        raise ReviewCopyError("Office package is too large to expand safely")
    for info in infos:
        if info.is_dir():
            name = info.filename.rstrip("/")
            if name:
                _relative_parts(name, "Office package member")
            continue
        try:
            _relative_parts(info.filename, "Office package member")
        except ReviewCopyError:
            archive.close()
            raise
    return archive, infos


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _numeric_suffix(value: str, pattern: str) -> int:
    match = re.search(pattern, value)
    if match is None:
        raise ReviewCopyError(f"expected numbered path, got {value!r}")
    return int(match.group(1))


def _xml_visible_text(data: bytes) -> str:
    try:
        root = ElementTree.fromstring(data)
    except ElementTree.ParseError as exc:
        raise ReviewCopyError("Office XML could not be parsed") from exc
    pieces: list[str] = []

    def walk(element: ElementTree.Element) -> None:
        name = _local_name(element.tag)
        if name in {"del", "delText", "instrText"}:
            return
        if name == "t" and element.text:
            pieces.append(element.text)
            return
        if name == "tab":
            pieces.append("\t")
            return
        if name in {"br", "cr"}:
            pieces.append("\n")
            return
        for child in element:
            walk(child)
        if name in {"p", "tr"}:
            pieces.append("\n")
        elif name == "tc":
            pieces.append("\t")

    walk(root)
    return "".join(pieces).strip()


def _docx_text(data: bytes) -> str:
    archive, infos = _zip_parts(data)
    try:
        names = {info.filename for info in infos}
        selected = ["word/document.xml"]
        selected.extend(
            sorted(
                name
                for name in names
                if re.fullmatch(
                    r"word/(header\d+|footer\d+|footnotes|endnotes|comments)\.xml",
                    name,
                )
            )
        )
        if "word/document.xml" not in names:
            raise ReviewCopyError("DOCX has no word/document.xml")
        sections = []
        for name in selected:
            text = _xml_visible_text(archive.read(name))
            if text:
                sections.append(f"[{PurePosixPath(name).name}]\n{text}")
        return "\n\n".join(sections)
    finally:
        archive.close()


def _xlsx_text(data: bytes) -> str:
    archive, infos = _zip_parts(data)
    try:
        names = {info.filename for info in infos}
        worksheets = sorted(
            (
                name
                for name in names
                if re.fullmatch(r"xl/worksheets/sheet\d+\.xml", name)
            ),
            key=lambda name: _numeric_suffix(name, r"(\d+)\.xml$"),
        )
        if not worksheets:
            raise ReviewCopyError("XLSX has no worksheets")
        shared: list[str] = []
        if "xl/sharedStrings.xml" in names:
            try:
                root = ElementTree.fromstring(archive.read("xl/sharedStrings.xml"))
            except ElementTree.ParseError as exc:
                raise ReviewCopyError(
                    "XLSX shared strings could not be parsed"
                ) from exc
            for item in root.iter():
                if _local_name(item.tag) == "si":
                    shared.append(
                        "".join(
                            node.text or ""
                            for node in item.iter()
                            if _local_name(node.tag) == "t"
                        )
                    )
        sections: list[str] = []
        for number, name in enumerate(worksheets, start=1):
            try:
                root = ElementTree.fromstring(archive.read(name))
            except ElementTree.ParseError as exc:
                raise ReviewCopyError(
                    f"XLSX worksheet {number} could not be parsed"
                ) from exc
            lines = [f"[Worksheet {number}: {PurePosixPath(name).name}]"]
            for row in root.iter():
                if _local_name(row.tag) != "row":
                    continue
                cells: list[str] = []
                for cell in row:
                    if _local_name(cell.tag) != "c":
                        continue
                    reference = cell.attrib.get("r", "cell")
                    cell_type = cell.attrib.get("t")
                    formula = next(
                        (
                            node.text or ""
                            for node in cell
                            if _local_name(node.tag) == "f"
                        ),
                        "",
                    )
                    value = next(
                        (
                            node.text or ""
                            for node in cell
                            if _local_name(node.tag) == "v"
                        ),
                        "",
                    )
                    if cell_type == "s" and value.isdigit():
                        index = int(value)
                        value = (
                            shared[index]
                            if index < len(shared)
                            else "[bad string index]"
                        )
                    elif cell_type == "inlineStr":
                        value = "".join(
                            node.text or ""
                            for node in cell.iter()
                            if _local_name(node.tag) == "t"
                        )
                    shown = f"={formula} -> {value}" if formula else value
                    cells.append(f"{reference}: {shown}")
                if cells:
                    lines.append("\t".join(cells))
            sections.append("\n".join(lines))
        return "\n\n".join(sections)
    finally:
        archive.close()


def _pptx_text(data: bytes) -> str:
    archive, infos = _zip_parts(data)
    try:
        names = {info.filename for info in infos}
        slides = sorted(
            (name for name in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)),
            key=lambda name: _numeric_suffix(name, r"(\d+)\.xml$"),
        )
        if not slides:
            raise ReviewCopyError("PPTX has no slides")
        sections = []
        for number, name in enumerate(slides, start=1):
            text = _xml_visible_text(archive.read(name))
            sections.append(f"[Slide {number}]\n{text}")
        return "\n\n".join(sections)
    finally:
        archive.close()


def _office_requires_visual_render(data: bytes, ext: str) -> bool:
    archive, infos = _zip_parts(data)
    try:
        names = {info.filename for info in infos}
        visual_prefixes = {
            "docx": ("word/media/", "word/embeddings/", "word/charts/"),
            "xlsx": ("xl/media/", "xl/drawings/", "xl/charts/", "xl/embeddings/"),
            "pptx": (
                "ppt/media/",
                "ppt/charts/",
                "ppt/diagrams/",
                "ppt/embeddings/",
            ),
        }
        if any(
            name.startswith(prefix) for name in names for prefix in visual_prefixes[ext]
        ):
            return True
        visual_tags = {
            "blip",
            "chart",
            "commentRangeEnd",
            "commentRangeStart",
            "commentReference",
            "del",
            "drawing",
            "graphic",
            "graphicFrame",
            "imagedata",
            "ins",
            "moveFrom",
            "moveTo",
            "object",
            "oleObj",
            "oleObject",
            "pic",
            "pict",
        }
        relevant_roots = {"docx": "word/", "xlsx": "xl/", "pptx": "ppt/"}
        if ext == "docx" and any(
            name.startswith("word/comments") and name.endswith(".xml") for name in names
        ):
            return True
        for name in sorted(names):
            if not name.startswith(relevant_roots[ext]) or not name.endswith(".xml"):
                continue
            try:
                root = ElementTree.fromstring(archive.read(name))
            except ElementTree.ParseError as exc:
                raise ReviewCopyError("Office XML could not be parsed") from exc
            if any(_local_name(element.tag) in visual_tags for element in root.iter()):
                return True
        return False
    finally:
        archive.close()


def _tool_version(tool: str) -> str:
    try:
        result = subprocess.run(
            [tool, "-v"], capture_output=True, text=True, timeout=10, check=False
        )
    except (OSError, subprocess.SubprocessError):
        return "unknown"
    combined = (result.stderr or result.stdout).strip().splitlines()
    if not combined:
        return "unknown"
    match = re.search(r"\d+(?:\.\d+)+", combined[0])
    return match.group(0) if match else "unknown"


def _poppler_pages(
    pdf_data: bytes,
    bundle: Path,
    *,
    role: str,
    renderer_override: dict[str, str] | None = None,
) -> list[dict[str, Any]]:
    tool = shutil.which("pdftoppm")
    if not tool:
        return []
    with tempfile.TemporaryDirectory(prefix="lq-review-pdf-") as temp_name:
        temp = Path(temp_name)
        source = temp / "source.pdf"
        prefix = temp / "page"
        source.write_bytes(pdf_data)
        try:
            result = subprocess.run(
                [tool, "-png", "-r", "144", str(source), str(prefix)],
                capture_output=True,
                timeout=120,
                check=False,
            )
        except (OSError, subprocess.SubprocessError):
            return []
        if result.returncode != 0:
            return []
        pages = sorted(
            temp.glob("page-*.png"),
            key=lambda path: _numeric_suffix(path.name, r"-(\d+)\.png$"),
        )
        renderer = renderer_override or _renderer(
            "poppler-pdftoppm", _tool_version(tool)
        )
        return [
            _write_derivative(
                bundle,
                page_path.read_bytes(),
                extension="png",
                media_type="image/png",
                role=role,
                renderer=renderer,
                page=page_number,
            )
            for page_number, page_path in enumerate(pages, start=1)
        ]


def _office_pdf_derivatives(
    source_data: bytes, ext: str, bundle: Path
) -> list[dict[str, Any]]:
    tool = shutil.which("libreoffice") or shutil.which("soffice")
    poppler = shutil.which("pdftoppm")
    if not tool or not poppler:
        return []
    with tempfile.TemporaryDirectory(prefix="lq-review-office-") as temp_name:
        temp = Path(temp_name)
        source = temp / f"source.{ext}"
        output = temp / "out"
        profile = temp / "profile"
        output.mkdir()
        profile.mkdir()
        source.write_bytes(source_data)
        try:
            result = subprocess.run(
                [
                    tool,
                    f"-env:UserInstallation={profile.as_uri()}",
                    "--headless",
                    "--convert-to",
                    "pdf",
                    "--outdir",
                    str(output),
                    str(source),
                ],
                capture_output=True,
                timeout=180,
                check=False,
            )
        except (OSError, subprocess.SubprocessError):
            return []
        pdfs = sorted(output.glob("*.pdf"))
        if result.returncode != 0 or len(pdfs) != 1:
            return []
        pdf_data = pdfs[0].read_bytes()
        if not pdf_data.startswith(b"%PDF-"):
            return []
        # LibreOffice injects volatile PDF metadata (including CreationDate), so
        # the temporary PDF is never persisted or receipted. Poppler raster
        # pages are the deterministic review derivatives.
        renderer = _renderer(
            "libreoffice+poppler-pdftoppm",
            f"{_tool_version(tool)}+{_tool_version(poppler)}",
        )
        return _poppler_pages(
            pdf_data,
            bundle,
            role="converted-page",
            renderer_override=renderer,
        )


def _render_payload(
    data: bytes,
    ext: str,
    title: str,
    bundle: Path,
    *,
    mode: str,
) -> tuple[str, str, str | None, list[dict[str, Any]]]:
    ext = ext.casefold()
    derivatives: list[dict[str, Any]] = []
    if ext in TEXT_EXTENSIONS:
        try:
            text = _decode_text(data)
        except ReviewCopyError as exc:
            return "text", "needs-rendering", str(exc), []
        review = _text_review_html(title, text)
        derivatives.append(
            _write_derivative(
                bundle,
                review,
                extension="html",
                media_type="text/html",
                role="full-text",
                renderer=_renderer("lq-escaped-text"),
            )
        )
        return "text", "ready", None, derivatives

    if ext == "eml":
        raise ReviewCopyError("EML payloads must use the message renderer")

    if ext in IMAGE_MEDIA_TYPES:
        media_type = _image_media_type(ext, data)
        if not media_type:
            return (
                "image",
                "needs-rendering",
                "Image is incomplete, corrupt, or does not match its extension.",
                [],
            )
        derivatives.append(
            _write_derivative(
                bundle,
                data,
                extension=ext,
                media_type=media_type,
                role="image",
                renderer=_renderer("browser-native-image"),
            )
        )
        return "image", "ready", None, derivatives

    if ext == "pdf":
        if not _pdf_is_reviewable(data):
            return (
                "pdf",
                "needs-rendering",
                "PDF structure is incomplete or not browser-reviewable.",
                [],
            )
        derivatives.append(
            _write_derivative(
                bundle,
                data,
                extension="pdf",
                media_type="application/pdf",
                role="browser-pdf",
                renderer=_renderer("browser-native-pdf"),
            )
        )
        if mode == "auto":
            derivatives.extend(_poppler_pages(data, bundle, role="pdf-page"))
        return "pdf", "ready", None, derivatives

    if ext in OFFICE_EXTENSIONS:
        try:
            visual_render_required = _office_requires_visual_render(data, ext)
            if ext == "docx":
                text = _docx_text(data)
            elif ext == "xlsx":
                text = _xlsx_text(data)
            else:
                text = _pptx_text(data)
        except ReviewCopyError as exc:
            return ext, "needs-rendering", str(exc), []
        review = _text_review_html(title, text, label="Safe visible-text review copy")
        derivatives.append(
            _write_derivative(
                bundle,
                review,
                extension="html",
                media_type="text/html",
                role="visible-text",
                renderer=_renderer(f"lq-{ext}-visible-text"),
            )
        )
        visual_derivatives = (
            _office_pdf_derivatives(data, ext, bundle) if mode == "auto" else []
        )
        derivatives.extend(visual_derivatives)
        if visual_render_required and not visual_derivatives:
            return (
                ext,
                "needs-rendering",
                "Office file contains visual or embedded content that requires a "
                "page-faithful renderer.",
                derivatives,
            )
        return ext, "ready", None, derivatives

    return (
        "unsupported",
        "needs-rendering",
        "No safe offline review-copy renderer is available for "
        f".{ext or 'unknown'} files.",
        [],
    )


def _safe_attachment_filename(message_part: Any, number: int) -> str:
    filename = message_part.get_filename()
    if filename:
        return PurePosixPath(str(filename).replace("\\", "/")).name
    guessed = mimetypes.guess_extension(message_part.get_content_type()) or ".bin"
    return f"attachment-{number}{guessed}"


def _eml_document(
    data: bytes,
    title: str,
    bundle: Path,
    *,
    mode: str,
) -> tuple[str, str | None, list[dict[str, Any]], list[dict[str, Any]]]:
    try:
        message = BytesParser(policy=policy.default).parsebytes(data)
    except Exception as exc:  # email defects vary by Python minor version
        return (
            "needs-rendering",
            f"EML could not be parsed: {type(exc).__name__}.",
            [],
            [],
        )

    header_lines = [f"{name}: {value}" for name, value in message.raw_items()]
    body_sections: list[str] = []
    attachments: list[dict[str, Any]] = []
    parts = list(message.walk()) if message.is_multipart() else [message]
    attachment_number = 0
    for part in parts:
        if part.is_multipart():
            continue
        disposition = part.get_content_disposition()
        filename = part.get_filename()
        content_type = part.get_content_type()
        is_safe_body = (
            content_type.startswith("text/")
            and disposition != "attachment"
            and not filename
        )
        if not is_safe_body:
            attachment_number += 1
            raw_payload = part.get_payload(decode=True)
            payload = raw_payload if isinstance(raw_payload, bytes) else b""
            safe_name = _safe_attachment_filename(part, attachment_number)
            ext = PurePosixPath(safe_name).suffix.lstrip(".").casefold()
            try:
                kind, status, reason, derivatives = _render_payload(
                    payload, ext, safe_name, bundle, mode=mode
                )
            except ReviewCopyError as exc:
                kind, status, reason, derivatives = (
                    "unsupported",
                    "needs-rendering",
                    str(exc),
                    [],
                )
            source_digest = _bytes_digest(payload)
            attachments.append(
                {
                    "attachment_id": source_digest,
                    "bytes": len(payload),
                    "derivatives": derivatives,
                    "filename": safe_name,
                    "kind": kind,
                    "reason": reason,
                    "source_sha256": source_digest,
                    "status": status,
                }
            )
            continue
        raw_payload = part.get_payload(decode=True)
        payload = (
            raw_payload
            if isinstance(raw_payload, bytes)
            else str(part.get_payload()).encode("utf-8", errors="replace")
        )
        charset = part.get_content_charset() or "utf-8"
        try:
            body = payload.decode(charset)
        except (LookupError, UnicodeDecodeError):
            body = _decode_text(payload)
        body_sections.append(f"[{content_type}]\n{body}")

    inventory = [
        f"- {item['filename']} ({item['bytes']} bytes; {item['source_sha256']})"
        for item in attachments
    ]
    text = "\n".join(header_lines)
    text += "\n\n" + ("\n\n".join(body_sections) or "[No safe text body found]")
    if inventory:
        text += "\n\n[Attachments]\n" + "\n".join(inventory)
    derivative = _write_derivative(
        bundle,
        _text_review_html(title, text, label="Safe email review copy"),
        extension="html",
        media_type="text/html",
        role="email",
        renderer=_renderer("lq-safe-eml"),
    )
    failed = [item for item in attachments if item["status"] != "ready"]
    if failed:
        names = ", ".join(item["filename"] for item in failed)
        return (
            "needs-rendering",
            f"Email attachment needs rendering: {names}.",
            [derivative],
            attachments,
        )
    return "ready", None, [derivative], attachments


def _manifest_documents(manifest: Any) -> list[dict[str, Any]]:
    if not isinstance(manifest, dict) or not isinstance(
        manifest.get("documents"), list
    ):
        raise ReviewCopyError("manifest must contain a documents array")
    documents = manifest["documents"]
    for index, row in enumerate(documents):
        if not isinstance(row, dict):
            raise ReviewCopyError(f"manifest documents[{index}] must be an object")
        for field in ("id", "path", "bytes"):
            if field not in row:
                raise ReviewCopyError(f"manifest documents[{index}] lacks {field}")
        if not DOC_ID_RE.fullmatch(str(row["id"])):
            raise ReviewCopyError(
                f"manifest documents[{index}].id is not a stable doc ID"
            )
        if (
            not isinstance(row["bytes"], int)
            or isinstance(row["bytes"], bool)
            or row["bytes"] < 0
        ):
            raise ReviewCopyError(f"manifest documents[{index}].bytes is invalid")
        _relative_parts(row["path"], f"manifest documents[{index}].path")
    return documents


def build_review_copies(
    manifest_path: str | os.PathLike[str],
    source_root: str | os.PathLike[str],
    sidecar_path: str | os.PathLike[str],
    *,
    bundle_root: str = "review-copies",
    mode: str = "auto",
) -> BuildResult:
    """Build a sidecar and bundle, then revalidate both from disk.

    ``bundle_root`` is a durable relative reference resolved beneath the
    sidecar's directory.  ``mode='text'`` disables optional external
    converters; ``mode='auto'`` adds Poppler/LibreOffice derivatives when the
    corresponding executable is already available.
    """

    if mode not in {"auto", "text"}:
        raise ReviewCopyError("mode must be auto or text")
    manifest_path = Path(manifest_path).resolve(strict=True)
    source_root_path = Path(source_root).resolve(strict=True)
    if not source_root_path.is_dir():
        raise ReviewCopyError("source_root is not a directory")
    sidecar_path = Path(sidecar_path).expanduser().absolute()
    sidecar_resolved = sidecar_path.resolve()
    bundle_parts = _relative_parts(bundle_root, "bundle_root")
    bundle_candidate = sidecar_path.parent.joinpath(*bundle_parts).resolve()
    if sidecar_resolved == manifest_path:
        raise ReviewCopyError("sidecar must not overwrite the manifest")
    if _is_relative_to(sidecar_resolved, source_root_path):
        raise ReviewCopyError("sidecar must be outside the immutable source root")
    if _is_relative_to(bundle_candidate, source_root_path) or _is_relative_to(
        source_root_path, bundle_candidate
    ):
        raise ReviewCopyError("review-copy bundle must not overlap the source root")
    if _is_relative_to(manifest_path, bundle_candidate):
        raise ReviewCopyError("review-copy bundle must not contain the manifest")
    sidecar_path.parent.mkdir(parents=True, exist_ok=True)
    manifest = _load_json(manifest_path)
    rows = _manifest_documents(manifest)
    bundle = _bundle_directory(sidecar_path, bundle_root, create=True)

    documents: list[dict[str, Any]] = []
    for row in rows:
        relative = row["path"]
        source = _contained_source(source_root_path, relative)
        data = source.read_bytes()
        source_digest = _bytes_digest(data)
        ext = PurePosixPath(relative).suffix.lstrip(".").casefold()
        manifest_ext = row.get("ext")
        reason: str | None = None
        derivatives: list[dict[str, Any]] = []
        attachments: list[dict[str, Any]] = []
        kind = ext or "unknown"

        if len(data) != row["bytes"]:
            status = "needs-rendering"
            reason = "Source size no longer matches the manifest; rebuild the manifest."
        elif row["id"] != "sha256:" + source_digest.removeprefix("sha256:")[:12]:
            status = "needs-rendering"
            reason = "Source hash no longer matches the manifest; rebuild the manifest."
        elif manifest_ext is not None and (
            not isinstance(manifest_ext, str) or manifest_ext.casefold() != ext
        ):
            status = "needs-rendering"
            reason = "Manifest extension does not match the source path."
        elif row.get("readability") in {"suspect", "encrypted", "corrupt"}:
            status = "needs-rendering"
            reason = (
                "Manifest marks this file "
                f"readability={row['readability']}; a complete review copy cannot "
                "be established."
            )
        elif ext == "eml":
            kind = "email"
            status, reason, derivatives, attachments = _eml_document(
                data, PurePosixPath(relative).name, bundle, mode=mode
            )
        else:
            try:
                kind, status, reason, derivatives = _render_payload(
                    data, ext, PurePosixPath(relative).name, bundle, mode=mode
                )
            except ReviewCopyError as exc:
                status = "needs-rendering"
                reason = str(exc)

        documents.append(
            {
                "attachments": attachments,
                "bytes": len(data),
                "derivatives": derivatives,
                "doc_id": row["id"],
                "kind": kind,
                "path": relative,
                "reason": reason,
                "source_sha256": source_digest,
                "status": status,
            }
        )

    documents.sort(key=lambda item: (item["doc_id"], item["path"]))
    body: dict[str, Any] = {
        "bundle_root": bundle_root,
        "documents": documents,
        "manifest_digest": canonical_digest(manifest),
        "schema_version": SCHEMA_VERSION,
        "status": (
            "ready"
            if all(document["status"] == "ready" for document in documents)
            else "needs-rendering"
        ),
    }
    sidecar = {**body, "digest": canonical_digest(body)}
    _write_json(sidecar_path, sidecar)
    validation = revalidate_review_copies(sidecar_path, manifest_path, source_root_path)
    return BuildResult(sidecar=sidecar, validation=validation)


def _exact_keys(
    value: Any,
    required: set[str],
    optional: set[str],
    where: str,
    errors: list[str],
) -> bool:
    if not isinstance(value, dict):
        errors.append(f"{where} must be an object")
        return False
    keys = set(value)
    missing = sorted(required - keys)
    extra = sorted(keys - required - optional)
    if missing:
        errors.append(f"{where} lacks keys: {', '.join(missing)}")
    if extra:
        errors.append(f"{where} has unexpected keys: {', '.join(extra)}")
    return not missing and not extra


def _validate_derivative_shape(value: Any, where: str, errors: list[str]) -> bool:
    if not _exact_keys(
        value,
        {"bytes", "media_type", "path", "renderer", "role", "sha256"},
        {"page"},
        where,
        errors,
    ):
        return False
    okay = True
    if (
        not isinstance(value["bytes"], int)
        or isinstance(value["bytes"], bool)
        or value["bytes"] < 0
    ):
        errors.append(f"{where}.bytes is invalid")
        okay = False
    if not isinstance(value["media_type"], str) or not value["media_type"]:
        errors.append(f"{where}.media_type is invalid")
        okay = False
    try:
        _relative_parts(value["path"], f"{where}.path")
    except ReviewCopyError as exc:
        errors.append(str(exc))
        okay = False
    if not isinstance(value["role"], str) or not value["role"]:
        errors.append(f"{where}.role is invalid")
        okay = False
    if not isinstance(value["sha256"], str) or not SHA256_RE.fullmatch(value["sha256"]):
        errors.append(f"{where}.sha256 is invalid")
        okay = False
    elif isinstance(value["path"], str):
        digest = value["sha256"].removeprefix("sha256:")
        path = PurePosixPath(value["path"])
        if (
            len(path.parts) != 3
            or path.parts[0] != "objects"
            or path.parts[1] != digest[:2]
            or path.stem != digest
            or not re.fullmatch(r"[a-z0-9]{1,12}", path.suffix.lstrip("."))
        ):
            errors.append(f"{where}.path is not content-addressed by its sha256")
            okay = False
    if "page" in value and (
        not isinstance(value["page"], int)
        or isinstance(value["page"], bool)
        or value["page"] < 1
    ):
        errors.append(f"{where}.page is invalid")
        okay = False
    if not _exact_keys(
        value["renderer"], {"name", "version"}, set(), f"{where}.renderer", errors
    ):
        okay = False
    elif not all(
        isinstance(value["renderer"][key], str) and value["renderer"][key]
        for key in ("name", "version")
    ):
        errors.append(f"{where}.renderer values must be non-empty strings")
        okay = False
    return okay


def _validate_item_shape(
    value: Any, where: str, errors: list[str], *, attachment: bool
) -> bool:
    identity = {"attachment_id", "filename"} if attachment else {"doc_id", "path"}
    required = identity | {
        "bytes",
        "derivatives",
        "kind",
        "reason",
        "source_sha256",
        "status",
    }
    if not attachment:
        required.add("attachments")
    if not _exact_keys(value, required, set(), where, errors):
        return False
    okay = True
    id_field = "attachment_id" if attachment else "doc_id"
    id_pattern = SHA256_RE if attachment else DOC_ID_RE
    if not isinstance(value[id_field], str) or not id_pattern.fullmatch(
        value[id_field]
    ):
        errors.append(f"{where}.{id_field} is invalid")
        okay = False
    if attachment:
        if (
            not isinstance(value["filename"], str)
            or not value["filename"]
            or value["filename"] in {".", ".."}
            or "/" in value["filename"]
            or "\\" in value["filename"]
        ):
            errors.append(f"{where}.filename is invalid")
            okay = False
    else:
        try:
            _relative_parts(value["path"], f"{where}.path")
        except ReviewCopyError as exc:
            errors.append(str(exc))
            okay = False
    if (
        not isinstance(value["bytes"], int)
        or isinstance(value["bytes"], bool)
        or value["bytes"] < 0
    ):
        errors.append(f"{where}.bytes is invalid")
        okay = False
    if not isinstance(value["kind"], str) or not value["kind"]:
        errors.append(f"{where}.kind is invalid")
        okay = False
    if value["status"] not in {"ready", "needs-rendering"}:
        errors.append(f"{where}.status is invalid")
        okay = False
    if value["status"] == "ready" and value["reason"] is not None:
        errors.append(f"{where}.reason must be null when ready")
        okay = False
    if value["status"] == "needs-rendering" and (
        not isinstance(value["reason"], str) or not value["reason"]
    ):
        errors.append(f"{where}.reason must explain the rendering blocker")
        okay = False
    if not isinstance(value["source_sha256"], str) or not SHA256_RE.fullmatch(
        value["source_sha256"]
    ):
        errors.append(f"{where}.source_sha256 is invalid")
        okay = False
    elif attachment and value["attachment_id"] != value["source_sha256"]:
        errors.append(f"{where}.attachment_id must equal its full source hash")
        okay = False
    elif not attachment:
        expected_doc_id = "sha256:" + value["source_sha256"][7:19]
        if value["doc_id"] != expected_doc_id:
            errors.append(f"{where}.doc_id does not match its full source hash")
            okay = False
    if not isinstance(value["derivatives"], list):
        errors.append(f"{where}.derivatives must be an array")
        okay = False
    else:
        if value["status"] == "ready" and not value["derivatives"]:
            errors.append(f"{where} is ready but has no review derivative")
            okay = False
        seen_derivatives: set[tuple[str, str, int | None]] = set()
        pages_by_role: dict[str, list[int]] = {}
        for index, derivative in enumerate(value["derivatives"]):
            if not _validate_derivative_shape(
                derivative, f"{where}.derivatives[{index}]", errors
            ):
                okay = False
                continue
            identity = (
                derivative["path"],
                derivative["role"],
                derivative.get("page"),
            )
            if identity in seen_derivatives:
                errors.append(f"{where}.derivatives contains a duplicate receipt")
                okay = False
            seen_derivatives.add(identity)
            if "page" in derivative:
                pages_by_role.setdefault(derivative["role"], []).append(
                    derivative["page"]
                )
        for role, pages in pages_by_role.items():
            if pages != list(range(1, len(pages) + 1)):
                errors.append(f"{where} page order is not contiguous for role {role}")
                okay = False
    return okay


def _validate_sidecar_shape(sidecar: Any, errors: list[str]) -> bool:
    if not _exact_keys(
        sidecar,
        {
            "bundle_root",
            "digest",
            "documents",
            "manifest_digest",
            "schema_version",
            "status",
        },
        set(),
        "sidecar",
        errors,
    ):
        return False
    okay = True
    if sidecar["schema_version"] != SCHEMA_VERSION:
        errors.append("sidecar.schema_version is unsupported")
        okay = False
    if sidecar["status"] not in {"ready", "needs-rendering"}:
        errors.append("sidecar.status is invalid")
        okay = False
    for field in ("digest", "manifest_digest"):
        if not isinstance(sidecar[field], str) or not SHA256_RE.fullmatch(
            sidecar[field]
        ):
            errors.append(f"sidecar.{field} is invalid")
            okay = False
    try:
        _relative_parts(sidecar["bundle_root"], "sidecar.bundle_root")
    except ReviewCopyError as exc:
        errors.append(str(exc))
        okay = False
    if not isinstance(sidecar["documents"], list):
        errors.append("sidecar.documents must be an array")
        return False
    for index, document in enumerate(sidecar["documents"]):
        where = f"sidecar.documents[{index}]"
        if not _validate_item_shape(document, where, errors, attachment=False):
            okay = False
            continue
        if not isinstance(document.get("attachments"), list):
            errors.append(f"{where}.attachments must be an array")
            okay = False
            continue
        for attachment_index, attachment in enumerate(document["attachments"]):
            if not _validate_item_shape(
                attachment,
                f"{where}.attachments[{attachment_index}]",
                errors,
                attachment=True,
            ):
                okay = False
        if document.get("status") == "ready" and any(
            isinstance(attachment, dict) and attachment.get("status") != "ready"
            for attachment in document["attachments"]
        ):
            errors.append(f"{where} is ready while an attachment needs rendering")
            okay = False
    if isinstance(sidecar.get("documents"), list):
        order = [
            (document.get("doc_id", ""), document.get("path", ""))
            for document in sidecar["documents"]
            if isinstance(document, dict)
        ]
        if order != sorted(order):
            errors.append("sidecar.documents are not in canonical doc_id/path order")
            okay = False
    if isinstance(sidecar.get("documents"), list):
        computed_status = (
            "ready"
            if all(
                isinstance(document, dict) and document.get("status") == "ready"
                for document in sidecar["documents"]
            )
            else "needs-rendering"
        )
        if sidecar.get("status") != computed_status:
            errors.append("sidecar.status does not match document statuses")
            okay = False
    return okay


def _iter_derivatives(document: dict[str, Any]):
    yield from document["derivatives"]
    for attachment in document["attachments"]:
        yield from attachment["derivatives"]


def _bundle_files(bundle: Path, errors: list[str]) -> set[str]:
    files: set[str] = set()
    for directory, dirnames, filenames in os.walk(bundle, followlinks=False):
        directory_path = Path(directory)
        safe_dirs = []
        for dirname in sorted(dirnames):
            child = directory_path / dirname
            if child.is_symlink():
                relative = child.relative_to(bundle).as_posix()
                errors.append(f"bundle contains a symlinked directory: {relative}")
            else:
                safe_dirs.append(dirname)
        dirnames[:] = safe_dirs
        for filename in sorted(filenames):
            child = directory_path / filename
            relative = child.relative_to(bundle).as_posix()
            if child.is_symlink():
                errors.append(f"bundle contains a symlinked file: {relative}")
            elif child.is_file():
                files.add(relative)
            else:
                errors.append(f"bundle contains a non-regular entry: {relative}")
    return files


def revalidate_review_copies(
    sidecar_path: str | os.PathLike[str],
    manifest_path: str | os.PathLike[str],
    source_root: str | os.PathLike[str],
) -> ValidationResult:
    """Revalidate schema, exact coverage, sources, derivatives, and bundle set."""

    sidecar_path = Path(sidecar_path).absolute()
    errors: list[str] = []
    try:
        sidecar = _load_json(sidecar_path)
        manifest = _load_json(Path(manifest_path).resolve(strict=True))
        rows = _manifest_documents(manifest)
        source_root_path = Path(source_root).resolve(strict=True)
    except (OSError, ReviewCopyError) as exc:
        return ValidationResult(False, False, (str(exc),), None, sidecar_path)

    if not _validate_sidecar_shape(sidecar, errors):
        return ValidationResult(
            False, False, tuple(sorted(set(errors))), sidecar, sidecar_path
        )

    body = {key: value for key, value in sidecar.items() if key != "digest"}
    if sidecar["digest"] != canonical_digest(body):
        errors.append("sidecar self-digest mismatch")
    if sidecar["manifest_digest"] != canonical_digest(manifest):
        errors.append("manifest canonical digest mismatch")

    expected_coverage = sorted((row["id"], row["path"], row["bytes"]) for row in rows)
    actual_coverage = sorted(
        (document["doc_id"], document["path"], document["bytes"])
        for document in sidecar["documents"]
    )
    if actual_coverage != expected_coverage:
        errors.append("sidecar does not exactly cover the manifest rows")

    try:
        bundle = _bundle_directory(sidecar_path, sidecar["bundle_root"], create=False)
    except ReviewCopyError as exc:
        errors.append(str(exc))
        return ValidationResult(
            False, False, tuple(sorted(set(errors))), sidecar, sidecar_path
        )

    expected_files: set[str] = set()
    for document in sidecar["documents"]:
        try:
            source = _contained_source(source_root_path, document["path"])
        except ReviewCopyError as exc:
            errors.append(str(exc))
            continue
        actual_size = source.stat().st_size
        actual_digest = _file_digest(source)
        if actual_size != document["bytes"]:
            errors.append(f"source byte count drift: {document['path']}")
        if actual_digest != document["source_sha256"]:
            errors.append(f"source hash drift: {document['path']}")
        expected_id = "sha256:" + actual_digest.removeprefix("sha256:")[:12]
        if document["doc_id"] != expected_id:
            errors.append(f"source doc_id drift: {document['path']}")

        for derivative in _iter_derivatives(document):
            relative = derivative["path"]
            expected_files.add(relative)
            try:
                parts = _relative_parts(relative, "derivative path")
                _assert_no_output_symlink(bundle, parts)
            except ReviewCopyError as exc:
                errors.append(str(exc))
                continue
            target = bundle.joinpath(*parts)
            if not target.exists():
                errors.append(f"derivative is missing: {relative}")
                continue
            if target.is_symlink() or not target.is_file():
                errors.append(f"derivative is not a regular file: {relative}")
                continue
            if target.stat().st_size != derivative["bytes"]:
                errors.append(f"derivative byte count mismatch: {relative}")
            if _file_digest(target) != derivative["sha256"]:
                errors.append(f"derivative hash mismatch: {relative}")

    actual_files = _bundle_files(bundle, errors)
    for missing in sorted(expected_files - actual_files):
        message = f"derivative is missing: {missing}"
        if message not in errors:
            errors.append(message)
    for extra in sorted(actual_files - expected_files):
        errors.append(f"extra file in review-copy bundle: {extra}")

    integrity_ok = not errors
    ready = integrity_ok and sidecar["status"] == "ready"
    return ValidationResult(
        integrity_ok,
        ready,
        tuple(sorted(set(errors))),
        sidecar,
        sidecar_path,
    )


def _component_alert(message: str) -> str:
    return (
        '<div class="lq-review-copy lq-needs-rendering" role="alert">'
        "<strong>Needs rendering</strong> " + html.escape(message) + "</div>"
    )


def _derivative_html(derivative: dict[str, Any], bundle_root: str, title: str) -> str:
    relative = f"{bundle_root}/{derivative['path']}"
    href = html.escape(urllib.parse.quote(relative, safe="/"), quote=True)
    title_attr = html.escape(title, quote=True)
    media_type = derivative["media_type"]
    if media_type == "text/html":
        return (
            f'<iframe class="lq-review-copy-frame" src="{href}" title="{title_attr}" '
            'sandbox="" loading="lazy" referrerpolicy="no-referrer"></iframe>'
        )
    if media_type.startswith("image/"):
        return (
            f'<img class="lq-review-copy-image" src="{href}" alt="{title_attr}" '
            'loading="lazy" referrerpolicy="no-referrer">'
        )
    if media_type == "application/pdf":
        return (
            f'<object class="lq-review-copy-pdf" data="{href}" '
            f'type="application/pdf" aria-label="{title_attr}">'
            f'<a href="{href}">Open verified PDF review copy</a></object>'
        )
    return f'<a href="{href}">Open verified review copy</a>'


def render_review_copy_component(
    validation: ValidationResult,
    doc_id: str,
    *,
    path: str | None = None,
    title: str | None = None,
) -> str:
    """Render a safe component only after full bundle revalidation.

    A path is required when duplicate manifest rows share a content-derived
    doc_id.  References are relative to the sidecar directory and point only
    to bytes included in the successful validation.
    """

    if not validation.integrity_ok or validation.sidecar is None:
        detail = "; ".join(validation.errors[:3]) or "Review-copy receipt is invalid."
        return _component_alert(detail)
    matches = [
        document
        for document in validation.sidecar["documents"]
        if document["doc_id"] == doc_id and (path is None or document["path"] == path)
    ]
    if len(matches) != 1:
        return _component_alert(
            "The document is absent from the verified receipt or its duplicate "
            "path is ambiguous."
        )
    document = matches[0]
    if document["status"] != "ready":
        return _component_alert(document["reason"])
    heading = title or PurePosixPath(document["path"]).name
    safe_heading = html.escape(heading)
    safe_hash = html.escape(document["source_sha256"])
    content = [
        '<section class="lq-review-copy" data-review-copy-status="verified">',
        f"<h3>{safe_heading}</h3>",
        '<p class="lq-review-copy-receipt">Verified source '
        f"<code>{safe_hash}</code></p>",
    ]
    for derivative in document["derivatives"]:
        content.append(
            _derivative_html(derivative, validation.sidecar["bundle_root"], heading)
        )
    for attachment in document["attachments"]:
        attachment_name = html.escape(attachment["filename"])
        content.append(f"<details><summary>Attachment: {attachment_name}</summary>")
        if attachment["status"] != "ready":
            content.append(_component_alert(attachment["reason"]))
        else:
            for derivative in attachment["derivatives"]:
                content.append(
                    _derivative_html(
                        derivative,
                        validation.sidecar["bundle_root"],
                        f"Attachment {attachment['filename']}",
                    )
                )
        content.append("</details>")
    content.append("</section>")
    return "".join(content)


def _build_command(args: argparse.Namespace) -> int:
    try:
        result = build_review_copies(
            args.manifest,
            args.source_root,
            args.sidecar,
            bundle_root=args.bundle_root,
            mode=args.mode,
        )
    except (OSError, ReviewCopyError) as exc:
        print(f"FATAL: {exc}", file=sys.stderr)
        return 2
    ready = sum(
        document["status"] == "ready" for document in result.sidecar["documents"]
    )
    total = len(result.sidecar["documents"])
    print(f"Wrote {args.sidecar}: {ready}/{total} documents review-ready")
    if not result.validation.integrity_ok:
        for error in result.validation.errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 2
    return 0 if result.validation.ready else 1


def _verify_command(args: argparse.Namespace) -> int:
    result = revalidate_review_copies(args.sidecar, args.manifest, args.source_root)
    if result.integrity_ok:
        print("Review-copy sidecar and bundle integrity verified.")
        return 0 if result.ready else 1
    for error in result.errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 2


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build or verify deterministic, hash-bound review copies."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    build = subparsers.add_parser("build")
    verify = subparsers.add_parser("verify")
    for command in (build, verify):
        command.add_argument("--manifest", required=True)
        command.add_argument("--source-root", required=True)
        command.add_argument("--sidecar", required=True)
    build.add_argument("--bundle-root", default="review-copies")
    build.add_argument("--mode", choices=["auto", "text"], default="auto")
    build.set_defaults(function=_build_command)
    verify.set_defaults(function=_verify_command)
    args = parser.parse_args()
    return args.function(args)


if __name__ == "__main__":
    raise SystemExit(main())
