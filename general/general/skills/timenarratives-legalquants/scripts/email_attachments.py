"""Classify EML attachments and construct terminal MIME-leaf records."""

from __future__ import annotations

import hashlib
from email.message import Message
from pathlib import PurePosixPath


def attachment_type(part: Message, payload: bytes, filename: str | None) -> str | None:
    suffix = PurePosixPath(filename or "").suffix.casefold()
    content_type = part.get_content_type().casefold()
    if content_type == "message/rfc822" or suffix == ".eml":
        return "email"
    if content_type in {"text/plain", "text/markdown"} or suffix in {
        ".txt",
        ".md",
        ".markdown",
    }:
        return "text"
    if (
        content_type
        == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        or suffix == ".docx"
    ) and payload.startswith(b"PK"):
        return "docx"
    return None


def is_inline_resource(part: Message) -> bool:
    content_type = part.get_content_type().casefold()
    return bool(part.get("Content-ID") or part.get("Content-Location")) or any(
        content_type.startswith(prefix)
        for prefix in ("image/", "audio/", "video/", "font/")
    )


def leaf_record(
    leaf_id: str,
    container_id: str,
    locator: str,
    parent: str | None,
    part: Message,
    role: str,
    disposition: str,
    *,
    reason: str | None = None,
    payload: bytes | None = None,
    child_id: str | None = None,
    author: str | None = None,
) -> dict:
    return {
        "mimeLeafId": leaf_id,
        "containerId": container_id,
        "locator": locator,
        "parentLocator": parent,
        "contentType": part.get_content_type().casefold(),
        "contentDisposition": part.get_content_disposition(),
        "filename": part.get_filename(),
        "contentId": part.get("Content-ID"),
        "payloadSha256": hashlib.sha256(payload).hexdigest()
        if payload is not None
        else None,
        "byteLength": len(payload) if payload is not None else None,
        "role": role,
        "childContainerId": child_id,
        "disposition": disposition,
        "reason": reason,
        "sourceAuthor": author,
    }
