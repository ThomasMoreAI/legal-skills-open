"""Atomic no-replace rename primitives for supported desktop platforms."""

from __future__ import annotations

import ctypes
import errno
import os
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Any

NativeRename = Callable[..., int]
LINUX_AT_FDCWD = -100
LINUX_RENAME_NOREPLACE = 1 << 0
MACOS_RENAME_EXCL = 0x00000004


class NoReplaceUnavailableError(OSError):
    """The platform cannot prove an atomic no-replace directory commit."""


def _native_symbol(name: str, argtypes: list[Any]) -> NativeRename:
    try:
        library = ctypes.CDLL(None, use_errno=True)
        function = getattr(library, name)
    except (AttributeError, OSError) as exc:
        raise NoReplaceUnavailableError(
            errno.ENOSYS, "atomic_no_replace_unavailable"
        ) from exc
    function.argtypes = argtypes
    function.restype = ctypes.c_int
    return function


def _raise_native_error(target: Path) -> None:
    error = ctypes.get_errno() or errno.EIO
    raise OSError(error, os.strerror(error), os.fspath(target))


def _linux_rename_no_replace(
    source: Path,
    target: Path,
    function: NativeRename | None = None,
) -> None:
    renameat2 = function or _native_symbol(
        "renameat2",
        [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_uint],
    )
    ctypes.set_errno(0)
    result = renameat2(
        LINUX_AT_FDCWD,
        os.fsencode(source),
        LINUX_AT_FDCWD,
        os.fsencode(target),
        LINUX_RENAME_NOREPLACE,
    )
    if result != 0:
        _raise_native_error(target)


def _macos_rename_no_replace(
    source: Path,
    target: Path,
    function: NativeRename | None = None,
) -> None:
    renamex_np = function or _native_symbol(
        "renamex_np", [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint]
    )
    ctypes.set_errno(0)
    result = renamex_np(os.fsencode(source), os.fsencode(target), MACOS_RENAME_EXCL)
    if result != 0:
        _raise_native_error(target)


def rename_no_replace(source: Path, target: Path) -> None:
    """Atomically rename a tree only when the destination name is absent."""
    if sys.platform == "win32":
        os.rename(source, target)
    elif sys.platform == "linux":
        _linux_rename_no_replace(source, target)
    elif sys.platform == "darwin":
        _macos_rename_no_replace(source, target)
    else:
        raise NoReplaceUnavailableError(
            errno.ENOSYS, "atomic_no_replace_unsupported_platform"
        )
