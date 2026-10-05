"""Reconcile EML MIME leaves and derive source-bound text units."""

from __future__ import annotations

from email import policy
from email.message import Message
from email.parser import BytesParser
from email.utils import parsedate_to_datetime

from email_attachments import attachment_type, is_inline_resource, leaf_record
from email_decode import (
    EmailDecodeError,
    decode_body_leaf,
    decode_nested_messages,
    transfer_decode,
)

MAX_DECODED_PAYLOAD = 8 * 1024 * 1024
MAX_MIME_NODES = 500
MAX_NESTING_DEPTH = 12
MAX_CHILDREN = 100
FATAL_DEFECTS = {
    "CloseBoundaryNotFoundDefect",
    "MultipartInvariantViolationDefect",
    "NoBoundaryInMultipartDefect",
    "StartBoundaryNotFoundDefect",
}


class EmailParseError(ValueError):
    pass


def _provenance_time(value: str | None) -> str | None:
    if not value:
        return None
    try:
        parsed = parsedate_to_datetime(value)
    except (TypeError, ValueError, OverflowError):
        return None
    if parsed.tzinfo is None:
        return None
    return parsed.isoformat()


def _source_author(message: Message) -> str | None:
    header = message.get("From")
    if header is None:
        return None
    value = str(header)
    if (
        not value.strip()
        or len(value) > 200
        or any(ord(character) < 32 or ord(character) == 127 for character in value)
    ):
        return None
    return value


class _Walk:
    def __init__(
        self, container_id: str, author: str | None, source_time: str | None
    ) -> None:
        self.container_id = container_id
        self.author = author
        self.source_time = source_time
        self.leaves: list[dict] = []
        self.units: list[dict] = []
        self.children: list[dict] = []
        self.limitations: list[str] = []
        self.nodes = 0

    def _next_leaf_id(self) -> str:
        return f"{self.container_id}-M{len(self.leaves) + 1:04d}"

    def _next_child_id(self) -> str:
        if len(self.children) >= MAX_CHILDREN:
            raise EmailParseError("derived child container cap exceeded")
        return f"{self.container_id}-A{len(self.children) + 1:04d}"

    def walk(
        self, part: Message, locator: str, parent: str | None, depth: int = 0
    ) -> None:
        self.nodes += 1
        if self.nodes > MAX_MIME_NODES or depth > MAX_NESTING_DEPTH:
            raise EmailParseError("MIME node or depth cap exceeded")
        defect_names = {type(defect).__name__ for defect in part.defects}
        if defect_names & FATAL_DEFECTS:
            raise EmailParseError("malformed MIME structure")
        content_type = part.get_content_type().casefold()
        if content_type == "message/rfc822":
            self._nested_messages(part, locator, parent)
            return
        if part.is_multipart():
            payload = part.get_payload()
            children = payload if isinstance(payload, list) else []
            before = len(self.units)
            for index, child in enumerate(children):
                if not isinstance(child, Message):
                    raise EmailParseError("multipart child is malformed")
                self.walk(child, f"{locator}/p{index}", locator, depth + 1)
            if content_type == "multipart/alternative":
                relevant = self.units[before:]
                variants = {unit["canonicalText"].strip() for unit in relevant}
                if len(variants) > 1:
                    for unit in relevant:
                        unit["eligibility"] = "requires_confirmation"
                    if "divergent_multipart_alternative" not in self.limitations:
                        self.limitations.append("divergent_multipart_alternative")
            return
        self._terminal(part, locator, parent)

    def _nested_messages(self, part: Message, locator: str, parent: str | None) -> None:
        try:
            messages = decode_nested_messages(part, max_bytes=MAX_DECODED_PAYLOAD)
        except EmailDecodeError as exc:
            self.leaves.append(
                leaf_record(
                    self._next_leaf_id(),
                    self.container_id,
                    locator,
                    parent,
                    part,
                    "nested_message",
                    "unreadable",
                    reason=exc.reason,
                    author=self.author,
                )
            )
            return
        for index, child_data in enumerate(messages):
            child_id = self._next_child_id()
            child_locator = f"{locator}/r{index}"
            self.children.append(
                {
                    "containerId": child_id,
                    "parentContainerId": self.container_id,
                    "originLocator": child_locator,
                    "displayName": part.get_filename() or "nested-message.eml",
                    "sourceType": "email",
                    "mediaType": "message/rfc822",
                    "rawBytes": child_data,
                }
            )
            self.leaves.append(
                leaf_record(
                    self._next_leaf_id(),
                    self.container_id,
                    child_locator,
                    parent,
                    part,
                    "nested_message",
                    "expanded",
                    payload=child_data,
                    child_id=child_id,
                    author=self.author,
                )
            )

    def _terminal(self, part: Message, locator: str, parent: str | None) -> None:
        leaf_id = self._next_leaf_id()
        disposition = part.get_content_disposition()
        filename = part.get_filename()
        role = (
            "inline"
            if disposition == "inline"
            else "attachment"
            if disposition == "attachment" or filename
            else "current"
        )
        try:
            if role in {"attachment", "inline"}:
                payload = transfer_decode(part, max_bytes=MAX_DECODED_PAYLOAD)
                source_type = attachment_type(part, payload, filename)
                if role == "inline" and is_inline_resource(part):
                    leaf = leaf_record(
                        leaf_id,
                        self.container_id,
                        locator,
                        parent,
                        part,
                        role,
                        "excluded",
                        reason="inline_resource",
                        payload=payload,
                        author=self.author,
                    )
                elif source_type is None:
                    leaf = leaf_record(
                        leaf_id,
                        self.container_id,
                        locator,
                        parent,
                        part,
                        role,
                        "unreadable",
                        reason="unsupported_attachment_format",
                        payload=payload,
                        author=self.author,
                    )
                else:
                    child_id = self._next_child_id()
                    self.children.append(
                        {
                            "containerId": child_id,
                            "parentContainerId": self.container_id,
                            "originLocator": locator,
                            "displayName": filename
                            or f"attachment-{len(self.children):04d}",
                            "sourceType": source_type,
                            "mediaType": part.get_content_type().casefold(),
                            "rawBytes": payload,
                        }
                    )
                    leaf = leaf_record(
                        leaf_id,
                        self.container_id,
                        locator,
                        parent,
                        part,
                        role,
                        "expanded",
                        payload=payload,
                        child_id=child_id,
                        author=self.author,
                    )
                self.leaves.append(leaf)
                return
            leaf, units = decode_body_leaf(
                part,
                leaf_id=leaf_id,
                container_id=self.container_id,
                locator=locator,
                parent=parent,
                author=self.author,
                source_time=self.source_time,
                unit_start=len(self.units) + 1,
                max_bytes=MAX_DECODED_PAYLOAD,
            )
            self.leaves.append(leaf)
            self.units.extend(units)
        except EmailDecodeError as exc:
            if exc.reason == "html_visibility_ambiguous":
                self.limitations.append(exc.reason)
            self.leaves.append(
                leaf_record(
                    leaf_id,
                    self.container_id,
                    locator,
                    parent,
                    part,
                    role,
                    "unreadable",
                    reason=exc.reason,
                    author=self.author,
                )
            )


def parse_email(container_id: str, data: bytes) -> dict:
    try:
        message = BytesParser(
            policy=policy.default.clone(raise_on_defect=False)
        ).parsebytes(data)
    except (ValueError, TypeError) as exc:
        raise EmailParseError("EML parser rejected the selected bytes") from exc
    defect_names = {type(defect).__name__ for defect in message.defects}
    if defect_names & FATAL_DEFECTS:
        raise EmailParseError("malformed MIME structure")
    author = _source_author(message)
    source_time = _provenance_time(
        str(message.get("Date")) if message.get("Date") else None
    )
    walk = _Walk(container_id, author, source_time)
    walk.walk(message, f"eml:{container_id}/m0", None)
    if author is None:
        for unit in walk.units:
            if unit["eligibility"] == "eligible":
                unit["eligibility"] = "requires_confirmation"
        walk.limitations.append("source_author_missing_or_invalid")
    return {
        "leaves": walk.leaves,
        "units": walk.units,
        "children": walk.children,
        "sourceAuthor": author,
        "sourceTime": source_time,
        "limitations": walk.limitations,
    }
