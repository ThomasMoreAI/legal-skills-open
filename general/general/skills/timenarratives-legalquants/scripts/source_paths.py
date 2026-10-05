"""Safe, bounded access to expressly selected packet files."""

from __future__ import annotations

import hashlib
import json
import os
import stat
import tempfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any

WINDOWS_DEVICES = {
    "AUX",
    "CLOCK$",
    "CON",
    "NUL",
    "PRN",
    *(f"COM{i}" for i in range(1, 10)),
    *(f"LPT{i}" for i in range(1, 10)),
}


class SourcePathError(ValueError):
    """The selected path is not a safe, ordinary relative file path."""


class SourceReadError(OSError):
    """The selected file could not be read exactly within its bound."""


def source_type_for_name(name: str) -> str:
    suffix = PurePosixPath(name).suffix.casefold()
    if suffix in {".txt", ".md", ".markdown"}:
        return "text"
    if suffix == ".eml":
        return "email"
    if suffix == ".docx":
        return "docx"
    return "unsupported"


def media_type(source_type: str, name: str) -> str:
    if source_type == "conversation":
        return "application/json"
    if source_type == "email":
        return "message/rfc822"
    if source_type == "docx":
        return "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    if source_type == "text":
        suffix = PurePosixPath(name).suffix.casefold()
        return "text/markdown" if suffix in {".md", ".markdown"} else "text/plain"
    if source_type == "user_note":
        return "text/plain"
    return "application/octet-stream"


@dataclass(frozen=True)
class SourceBytes:
    relative_path: str
    display_name: str
    data: bytes
    byte_length: int
    sha256: str


def _is_reparse(path: Path) -> bool:
    try:
        info = path.lstat()
    except OSError as exc:
        raise SourcePathError(
            f"source path is missing or unreadable: {path.name}"
        ) from exc
    attributes = getattr(info, "st_file_attributes", 0)
    reparse_flag = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
    return path.is_symlink() or bool(attributes & reparse_flag)


def validate_relative_path(value: str) -> PurePosixPath:
    """Validate portable lexical form before touching the filesystem."""
    if not isinstance(value, str) or not value or "\\" in value or ":" in value:
        raise SourcePathError("source path must be a safe POSIX-relative path")
    if value.startswith("/") or "//" in value:
        raise SourcePathError("source path must be a safe POSIX-relative path")
    if any(ord(char) < 32 or char == "\x7f" for char in value):
        raise SourcePathError("source path contains a control character")
    relative = PurePosixPath(value)
    if relative.is_absolute() or any(
        part in {"", ".", ".."} for part in relative.parts
    ):
        raise SourcePathError("source path contains an unsafe segment")
    for part in relative.parts:
        stem = part.rstrip(" .").split(".", 1)[0].upper()
        if part != part.rstrip(" .") or stem in WINDOWS_DEVICES:
            raise SourcePathError("source path uses a reserved Windows name")
    return relative


def validate_source_root(root: Path) -> Path:
    """Resolve an invocation root without accepting links or reparse points."""
    try:
        lexical_root = Path(os.path.abspath(os.fspath(root)))
    except (OSError, ValueError) as exc:
        raise SourcePathError("source root is invalid") from exc
    if _is_reparse(lexical_root) or not lexical_root.is_dir():
        raise SourcePathError("source root is not an ordinary directory")
    return lexical_root


def resolve_selected_path(root: Path, value: str) -> Path:
    relative = validate_relative_path(value)
    try:
        lexical_root = validate_source_root(root)
        current = lexical_root
        for part in relative.parts:
            current /= part
            if _is_reparse(current):
                raise SourcePathError("source path contains a symlink or reparse point")
        resolved_root = lexical_root.resolve(strict=True)
        resolved = current.resolve(strict=True)
        resolved.relative_to(resolved_root)
    except SourcePathError:
        raise
    except (OSError, ValueError) as exc:
        raise SourcePathError("source path resolves outside the selected root") from exc
    if not resolved.is_file():
        raise SourcePathError("selected source is not an ordinary file")
    return resolved


def _fingerprint(info: os.stat_result) -> tuple[int, int, int, int]:
    return (info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns)


def read_bounded_file(root: Path, relative: str, *, max_bytes: int) -> SourceBytes:
    if max_bytes < 0:
        raise ValueError("max_bytes must be non-negative")
    path = resolve_selected_path(root, relative)
    try:
        before = path.stat()
        if before.st_size > max_bytes:
            raise SourceReadError(
                f"selected source exceeds {max_bytes} bytes; it was not truncated"
            )
        with path.open("rb") as stream:
            opened = os.fstat(stream.fileno())
            data = stream.read(max_bytes + 1)
            after_open = os.fstat(stream.fileno())
        after_path = path.stat()
    except SourceReadError:
        raise
    except OSError as exc:
        raise SourceReadError("selected source could not be read") from exc
    if len(data) > max_bytes:
        raise SourceReadError(
            f"selected source exceeds {max_bytes} bytes; it was not truncated"
        )
    fingerprints = {
        _fingerprint(item) for item in (before, opened, after_open, after_path)
    }
    if len(fingerprints) != 1 or len(data) != before.st_size:
        raise SourceReadError("selected source changed during read")
    return SourceBytes(
        relative_path=relative,
        display_name=PurePosixPath(relative).name,
        data=data,
        byte_length=len(data),
        sha256=hashlib.sha256(data).hexdigest(),
    )


def _checked_output(path: Path, output_root: Path) -> Path:
    root = Path(os.path.abspath(os.fspath(output_root)))
    target = Path(os.path.abspath(os.fspath(path)))
    try:
        target.relative_to(root)
    except ValueError as exc:
        raise SourcePathError(
            "output must remain inside its owned run directory"
        ) from exc
    if _is_reparse(root) or not root.is_dir():
        raise SourcePathError("output root is not an ordinary directory")
    current = root
    for part in target.relative_to(root).parent.parts:
        current /= part
        if current.exists() and _is_reparse(current):
            raise SourcePathError("output path contains a symlink or reparse point")
        current.mkdir(exist_ok=True)
    if target.is_symlink() or (target.exists() and _is_reparse(target)):
        raise SourcePathError("output target is a symlink or reparse point")
    return target


def atomic_write_json(path: Path, value: Any, *, output_root: Path) -> None:
    target = _checked_output(path, output_root)
    temporary: Path | None = None
    try:
        descriptor, name = tempfile.mkstemp(
            prefix=f".{target.name}.", dir=target.parent
        )
        temporary = Path(name)
        try:
            os.chmod(temporary, 0o600)
        except OSError:
            pass
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
        os.replace(temporary, target)
    finally:
        if temporary is not None:
            try:
                temporary.unlink()
            except FileNotFoundError:
                pass
