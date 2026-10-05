"""Strict, non-fetching decoding helpers for stdlib email ingestion."""

from __future__ import annotations

import base64
import binascii
import codecs
import quopri
import re
from email import policy
from email.message import Message
from html.parser import HTMLParser

from email_attachments import leaf_record
from text_units import make_text_units


class EmailDecodeError(ValueError):
    def __init__(self, reason: str) -> None:
        super().__init__(reason)
        self.reason = reason


def _decode_transfer_bytes(raw: bytes, encoding: str, max_bytes: int) -> bytes:
    try:
        if encoding == "base64":
            payload = base64.b64decode(re.sub(rb"\s+", b"", raw), validate=True)
        elif encoding == "quoted-printable":
            if re.search(rb"=(?![0-9A-Fa-f]{2}|\r?\n)", raw):
                raise EmailDecodeError("transfer_decode_failed")
            payload = quopri.decodestring(raw)
        else:
            raise EmailDecodeError("unsupported_transfer_encoding")
    except EmailDecodeError:
        raise
    except (UnicodeError, ValueError, binascii.Error) as exc:
        raise EmailDecodeError("transfer_decode_failed") from exc
    if not isinstance(payload, bytes):
        raise EmailDecodeError("transfer_decode_failed")
    if len(payload) > max_bytes:
        raise EmailDecodeError("decoded_payload_oversize")
    return payload


def transfer_decode(part: Message, *, max_bytes: int) -> bytes:
    encoding = (part.get("Content-Transfer-Encoding") or "").strip().casefold()
    raw_value = part.get_payload(decode=False)
    if isinstance(raw_value, list) or isinstance(raw_value, Message):
        raise EmailDecodeError("malformed_mime")
    if not isinstance(raw_value, str | bytes):
        raise EmailDecodeError("malformed_mime")
    try:
        raw = (
            raw_value.encode("ascii", errors="strict")
            if isinstance(raw_value, str)
            else raw_value
        )
        if encoding in {"base64", "quoted-printable"}:
            return _decode_transfer_bytes(raw, encoding, max_bytes)
        if encoding not in {"", "7bit", "8bit", "binary"}:
            raise EmailDecodeError("unsupported_transfer_encoding")
        payload = part.get_payload(decode=True)
        if payload is None:
            payload = raw
    except EmailDecodeError:
        raise
    except (UnicodeError, ValueError, binascii.Error) as exc:
        raise EmailDecodeError("transfer_decode_failed") from exc
    if not isinstance(payload, bytes):
        raise EmailDecodeError("transfer_decode_failed")
    if len(payload) > max_bytes:
        raise EmailDecodeError("decoded_payload_oversize")
    return payload


def decode_nested_messages(part: Message, *, max_bytes: int) -> list[bytes]:
    messages = part.get_payload()
    if not isinstance(messages, list) or not messages:
        raise EmailDecodeError("malformed_rfc822")
    encoding = (part.get("Content-Transfer-Encoding") or "").strip().casefold()
    serialized: list[bytes] = []
    for message in messages:
        if not isinstance(message, Message):
            raise EmailDecodeError("malformed_rfc822")
        serialized.append(message.as_bytes(policy=policy.SMTP))
    if encoding in {"", "7bit", "8bit", "binary"}:
        if any(len(value) > max_bytes for value in serialized):
            raise EmailDecodeError("decoded_payload_oversize")
        return serialized
    if len(serialized) != 1:
        raise EmailDecodeError("malformed_rfc822")
    return [_decode_transfer_bytes(serialized[0], encoding, max_bytes)]


def decode_text_payload(part: Message, *, max_bytes: int) -> tuple[bytes, str]:
    payload = transfer_decode(part, max_bytes=max_bytes)
    charset = part.get_content_charset() or "us-ascii"
    try:
        canonical_charset = codecs.lookup(charset).name
    except LookupError as exc:
        raise EmailDecodeError("unknown_charset") from exc
    try:
        text = payload.decode(canonical_charset, errors="strict")
    except UnicodeDecodeError as exc:
        raise EmailDecodeError("charset_decode_failed") from exc
    if "\x00" in text:
        raise EmailDecodeError("charset_decode_failed")
    return payload, text.replace("\r\n", "\n").replace("\r", "\n")


class _VisibleHTML(HTMLParser):
    BLOCKS = {
        "address",
        "article",
        "aside",
        "blockquote",
        "br",
        "div",
        "footer",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "header",
        "li",
        "p",
        "pre",
        "section",
        "table",
        "td",
        "th",
        "tr",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.values: list[str] = []
        self.hidden: list[str] = []
        self.quote_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.casefold()
        values = {name.casefold(): (value or "").casefold() for name, value in attrs}
        if tag == "style" or (
            tag == "link" and "stylesheet" in values.get("rel", "").split()
        ):
            raise EmailDecodeError("html_visibility_ambiguous")
        style = re.sub(r"\s+", "", values.get("style", ""))
        hidden = (
            tag in {"script", "noscript", "template"}
            or "hidden" in values
            or values.get("aria-hidden") == "true"
            or (tag == "input" and values.get("type") == "hidden")
            or any(
                rule in style
                for rule in (
                    "display:none",
                    "visibility:hidden",
                    "visibility:collapse",
                    "content-visibility:hidden",
                    "mso-hide:all",
                )
            )
        )
        if self.hidden or hidden:
            self.hidden.append(tag)
            return
        if tag == "blockquote":
            self.quote_depth += 1
        if tag in self.BLOCKS:
            self.values.append("\n")
            if self.quote_depth:
                self.values.append("> ")

    def handle_endtag(self, tag: str) -> None:
        tag = tag.casefold()
        if self.hidden:
            if tag == self.hidden[-1]:
                self.hidden.pop()
            return
        if tag in self.BLOCKS:
            self.values.append("\n")
        if tag == "blockquote" and self.quote_depth:
            self.quote_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self.hidden:
            self.values.append(data)


def html_visible_text(value: str) -> str:
    parser = _VisibleHTML()
    try:
        parser.feed(value)
        parser.close()
    except EmailDecodeError:
        raise
    except (ValueError, AssertionError) as exc:
        raise EmailDecodeError("html_decode_failed") from exc
    lines = [
        re.sub(r"[ \t]+", " ", line).strip()
        for line in "".join(parser.values).splitlines()
    ]
    return "\n".join(line for line in lines if line)


def _outlook_history_start(lines: list[str]) -> int | None:
    for index, line in enumerate(lines):
        if not re.match(r"(?i)^from:\s*\S", line.strip()):
            continue
        names: list[str] = []
        for candidate in lines[index : index + 8]:
            stripped = candidate.strip()
            if not stripped:
                break
            match = re.match(r"(?i)^([a-z-]+):", stripped)
            if match:
                names.append(match.group(1).casefold())
        if len(names) >= 4 and names[:3] == ["from", "sent", "to"]:
            if "subject" in names[3:]:
                prior = index - 1
                if prior >= 0 and "original message" in lines[prior].casefold():
                    return prior
                return index
    return None


def split_body_roles(value: str) -> list[tuple[str, str]]:
    lines = value.splitlines(keepends=True)
    if not lines and value:
        lines = [value]
    history_start = _outlook_history_start(lines)
    grouped: list[tuple[str, str]] = []
    for index, line in enumerate(lines):
        stripped = line.lstrip()
        role = (
            "quoted"
            if stripped.startswith(">")
            or history_start is not None
            and index >= history_start
            else "current"
        )
        if grouped and grouped[-1][0] == role:
            grouped[-1] = (role, grouped[-1][1] + line)
        else:
            grouped.append((role, line))
    return [(role, text) for role, text in grouped if text]


def decode_body_leaf(
    part: Message,
    *,
    leaf_id: str,
    container_id: str,
    locator: str,
    parent: str | None,
    author: str | None,
    source_time: str | None,
    unit_start: int,
    max_bytes: int,
) -> tuple[dict, list[dict]]:
    content_type = part.get_content_type().casefold()
    if not content_type.startswith("text/"):
        return (
            leaf_record(
                leaf_id,
                container_id,
                locator,
                parent,
                part,
                "context",
                "unreadable",
                reason="unsupported_body_format",
                author=author,
            ),
            [],
        )
    payload, value = decode_text_payload(part, max_bytes=max_bytes)
    if content_type == "text/html":
        value = html_visible_text(value)
    if not value:
        return (
            leaf_record(
                leaf_id,
                container_id,
                locator,
                parent,
                part,
                "empty",
                "excluded",
                reason="empty",
                payload=payload,
                author=author,
            ),
            [],
        )
    leaf = leaf_record(
        leaf_id,
        container_id,
        locator,
        parent,
        part,
        "current",
        "ready",
        payload=payload,
        author=author,
    )
    units: list[dict] = []
    for segment_index, (role, segment) in enumerate(split_body_roles(value)):
        units.extend(
            make_text_units(
                container_id,
                segment.encode(),
                kind="email_text",
                role=role,
                eligibility="eligible" if role == "current" else "context_only",
                source_author=author,
                source_time=source_time,
                origin_id=leaf_id,
                locator_prefix=f"{locator}/segment{segment_index}",
                unit_start=unit_start + len(units),
            )
        )
    return leaf, units
