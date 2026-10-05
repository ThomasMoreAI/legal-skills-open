"""Freeze expressly selected folders into bounded ordinary-file selections."""

from __future__ import annotations

import os
import stat
from pathlib import Path

from packet_core import LIMITS, PacketBuildError
from source_paths import SourcePathError, validate_relative_path, validate_source_root

MAX_FOLDER_ENTRIES = 1000
MAX_FOLDER_DEPTH = 20


def _ordinary_path(root: Path, relative: str) -> Path:
    """Check every lexical component before resolving or listing a directory."""
    current = root
    parts = () if relative == "." else validate_relative_path(relative).parts
    for part in parts:
        current /= part
        info = current.lstat()
        if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
            raise SourcePathError("selected folder contains a link or reparse point")
    current.resolve(strict=True).relative_to(root.resolve(strict=True))
    return current


def expand_folders(root: Path, folders: list[str], paths: list[str]) -> list[str]:
    """Select all ordinary files; never truncate or follow links, even in-root."""
    if not folders:
        return paths
    root = validate_source_root(root)
    selected = dict.fromkeys(paths)
    visited: set[str] = set()
    entries_seen = 0

    def visit(relative: str, depth: int) -> None:
        nonlocal entries_seen
        if relative in visited:
            return
        if depth > MAX_FOLDER_DEPTH:
            raise PacketBuildError("selected folder is too deep; select a subfolder")
        directory = _ordinary_path(root, relative)
        if not directory.is_dir():
            raise SourcePathError("selected folder is not an ordinary directory")
        visited.add(relative)
        # Bound collection before sorting, including empty directories and links.
        children = []
        with os.scandir(directory) as scan:
            for entry in scan:
                entries_seen += 1
                if entries_seen > MAX_FOLDER_ENTRIES:
                    raise PacketBuildError(
                        "selected folder is too large; narrow the selection"
                    )
                children.append(entry.name)
        for name in sorted(children):
            child = name if relative == "." else f"{relative}/{name}"
            path = _ordinary_path(root, child)
            info = path.lstat()
            if stat.S_ISDIR(info.st_mode):
                visit(child, depth + 1)
            elif stat.S_ISREG(info.st_mode):
                selected[child] = None
                if len(selected) > LIMITS["selectedRoots"]:
                    raise PacketBuildError(
                        "selected files exceed the packet limit; narrow the selection"
                    )
            else:
                raise SourcePathError("selected folder contains a non-ordinary file")

    try:
        for folder in folders:
            visit(folder, 0)
    except (OSError, ValueError) as exc:
        if isinstance(exc, (SourcePathError, PacketBuildError)):
            raise
        raise SourcePathError("selected folder is missing or unreadable") from exc
    return list(selected)
