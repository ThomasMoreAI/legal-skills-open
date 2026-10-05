"""Construct selected-root and byte-container provenance records."""

from __future__ import annotations

import hashlib
from pathlib import PurePosixPath

from source_paths import media_type


def root_record(root_id: str, index: int, kind: str, path: str | None) -> dict:
    return {
        "rootId": root_id,
        "selectionIndex": index - 1,
        "kind": kind,
        "selectedPath": path,
        "containerId": root_id,
        "disposition": "ready",
        "reason": None,
    }


def container_record(
    container_id: str,
    root_id: str,
    parent_id: str | None,
    origin: str,
    source_type: str,
    declared_media_type: str,
    display_name: str,
    data: bytes,
) -> dict:
    return {
        "containerId": container_id,
        "parentContainerId": parent_id,
        "rootId": root_id,
        "originLocator": origin,
        "sourceType": source_type,
        "mediaType": declared_media_type,
        "displayName": display_name,
        "byteLength": len(data),
        "rawSha256": hashlib.sha256(data).hexdigest(),
        "sourceTime": None,
        "sourceTimeKind": None,
        "filterDisposition": "included",
        "disposition": "ready",
        "reason": None,
        "sourceAuthor": None,
    }


def unreadable_container_record(
    container_id: str,
    root_id: str,
    name: str,
    source_type: str,
    reason: str,
) -> dict:
    return {
        "containerId": container_id,
        "parentContainerId": None,
        "rootId": root_id,
        "originLocator": "selection",
        "sourceType": source_type,
        "mediaType": media_type(source_type, name),
        "displayName": PurePosixPath(name).name,
        "byteLength": None,
        "rawSha256": None,
        "sourceTime": None,
        "sourceTimeKind": None,
        "filterDisposition": "included",
        "disposition": "unreadable",
        "reason": reason,
        "sourceAuthor": None,
    }
