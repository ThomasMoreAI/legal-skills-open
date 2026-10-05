"""New-only, link-safe publication boundaries for TimeNarratives artifacts.

On POSIX the staged tree is created with owner-only modes (0o700 / 0o600). On
Windows no mode is passed: since Python 3.12.4 a 0o700 directory mode becomes
an owner-only ACL, and under a sandboxed host the owner is the sandbox token
rather than the user, so the published run would be unreadable by the person
it was written for. Windows privacy is inherited from the output parent's ACL.
"""

from __future__ import annotations

import os
import secrets
import stat
import sys
import tempfile
from collections.abc import Callable, Iterable, Mapping
from pathlib import Path

from no_replace import rename_no_replace

POSIX_MODES = sys.platform != "win32"


class OutputSafetyError(OSError):
    """An output is not a new path inside an ordinary filesystem boundary."""


def _absolute(path: str | Path) -> Path:
    try:
        return Path(os.path.abspath(os.fspath(path)))
    except (OSError, TypeError, ValueError) as exc:
        raise OutputSafetyError("invalid_output_path") from exc


def _lexists(path: Path) -> bool:
    return os.path.lexists(os.fspath(path))


def _is_reparse(path: Path) -> bool:
    try:
        info = path.lstat()
    except OSError as exc:
        raise OutputSafetyError("unreadable_output_boundary") from exc
    attributes = getattr(info, "st_file_attributes", 0)
    reparse_flag = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
    return path.is_symlink() or bool(attributes & reparse_flag)


def _validate_parent_chain(target: Path) -> None:
    parent = target.parent
    if not _lexists(parent) or not parent.is_dir():
        raise OutputSafetyError("output_parent_unavailable")
    chain = [parent, *parent.parents]
    for ancestor in reversed(chain):
        if _lexists(ancestor) and _is_reparse(ancestor):
            raise OutputSafetyError("linked_output_boundary")


def _same_path(first: Path, second: Path) -> bool:
    if os.path.normcase(os.fspath(first)) == os.path.normcase(os.fspath(second)):
        return True
    if _lexists(first) and _lexists(second):
        try:
            return os.path.samefile(first, second)
        except OSError:
            return False
    return False


def _inside(target: Path, root: Path) -> bool:
    try:
        target.relative_to(root)
    except ValueError:
        return False
    return True


def validate_new_output(
    path: str | Path,
    *,
    protected_paths: Iterable[str | Path] = (),
    forbidden_roots: Iterable[str | Path] = (),
) -> Path:
    """Return an absolute new target after alias and reparse checks."""
    target = _absolute(path)
    _validate_parent_chain(target)
    if _lexists(target):
        raise OutputSafetyError("output_already_exists")
    for protected in protected_paths:
        if _same_path(target, _absolute(protected)):
            raise OutputSafetyError("output_aliases_input")
    for root_value in forbidden_roots:
        root = _absolute(root_value)
        if _inside(target, root):
            raise OutputSafetyError("output_inside_input_root")
    return target


def _write_staged_file(path: Path, data: bytes) -> None:
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
    except BaseException:
        path.unlink(missing_ok=True)
        raise


def write_new_bytes(
    path: str | Path,
    data: bytes,
    *,
    protected_paths: Iterable[str | Path] = (),
    forbidden_roots: Iterable[str | Path] = (),
) -> None:
    """Publish a fully staged file without replacing an existing target."""
    target = validate_new_output(
        path, protected_paths=protected_paths, forbidden_roots=forbidden_roots
    )
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{target.name}.stage-", dir=target.parent
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        validate_new_output(
            target,
            protected_paths=protected_paths,
            forbidden_roots=forbidden_roots,
        )
        os.link(temporary, target)
    finally:
        temporary.unlink(missing_ok=True)


def _make_stage_dir(parent: Path, prefix: str) -> Path:
    """Exclusive, unpredictable sibling stage; POSIX modes only where they apply."""
    if POSIX_MODES:
        try:
            staging = Path(tempfile.mkdtemp(prefix=prefix, dir=parent))
        except OSError as exc:
            raise OutputSafetyError("stage_directory_unavailable") from exc
        try:
            os.chmod(staging, 0o700)
        except OSError:
            pass
        return staging
    for _ in range(64):
        candidate = parent / f"{prefix}{secrets.token_hex(8)}"
        try:
            os.mkdir(candidate)  # default mode: inherits the parent's ACL
        except FileExistsError:
            continue
        except OSError as exc:
            raise OutputSafetyError("stage_directory_unavailable") from exc
        return candidate
    raise OutputSafetyError("stage_directory_unavailable")


def publish_owned_directory(
    path: str | Path,
    files: Mapping[str, bytes],
    *,
    protected_paths: Iterable[str | Path] = (),
    forbidden_roots: Iterable[str | Path] = (),
    before_publish: Callable[[], None] | None = None,
) -> Path:
    """Stage a private sibling tree, then atomically claim the new run path."""
    target = validate_new_output(
        path, protected_paths=protected_paths, forbidden_roots=forbidden_roots
    )
    if not files or any(Path(name).name != name for name in files):
        raise OutputSafetyError("invalid_output_file_set")
    staging = _make_stage_dir(target.parent, f".{target.name}.stage-")
    artifacts = staging / "artifacts"
    if POSIX_MODES:
        artifacts.mkdir(mode=0o700)
    else:
        artifacts.mkdir()
    for name, data in files.items():
        _write_staged_file(artifacts / name, data)
    validate_new_output(
        target,
        protected_paths=protected_paths,
        forbidden_roots=forbidden_roots,
    )
    if before_publish is not None:
        before_publish()
    rename_no_replace(staging, target)
    return target / "artifacts"
