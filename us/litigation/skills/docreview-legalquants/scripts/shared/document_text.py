#!/usr/bin/env python3
"""Shared visible-text extraction and quote normalization for diligence.

The reader, metadata merger, quote verifier, and model-edge verifier must use
the same text surface. HTML/SEC SGML is reduced to visible text with entities
decoded and script/style content removed. PDFs prefer pdftotext and fall back
to a small stdlib content-stream extractor.
"""

from __future__ import annotations

import html.parser
import posixpath
import re
import shutil
import subprocess
import unicodedata
import zipfile
import zlib
from email import policy
from email.parser import BytesParser
from xml.etree import ElementTree

HAVE_PDFTOTEXT = shutil.which("pdftotext") is not None
MARKUP_SUFFIXES = (".htm", ".html", ".xhtml", ".sgml")


class VisibleTextParser(html.parser.HTMLParser):
    BREAK_TAGS = {
        "address",
        "article",
        "aside",
        "blockquote",
        "br",
        "caption",
        "dd",
        "div",
        "dl",
        "dt",
        "footer",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "header",
        "hr",
        "li",
        "main",
        "nav",
        "ol",
        "p",
        "pre",
        "section",
        "table",
        "tbody",
        "td",
        "tfoot",
        "th",
        "thead",
        "tr",
        "ul",
    }
    SKIP_TAGS = {"script", "style", "noscript"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.skip_depth = 0

    def handle_starttag(self, tag, attrs):  # noqa: ARG002
        tag = tag.casefold()
        if tag in self.SKIP_TAGS:
            self.skip_depth += 1
        elif not self.skip_depth and tag in self.BREAK_TAGS:
            self.parts.append("\n")

    def handle_startendtag(self, tag, attrs):  # noqa: ARG002
        if not self.skip_depth and tag.casefold() in self.BREAK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        tag = tag.casefold()
        if tag in self.SKIP_TAGS and self.skip_depth:
            self.skip_depth -= 1
        elif not self.skip_depth and tag in self.BREAK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skip_depth:
            self.parts.append(data)


def clean_text(value: str) -> str:
    value = value.replace("\x00", "").replace("\u00ad", "")
    value = unicodedata.normalize("NFKC", value)
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    lines = [re.sub(r"[ \t\f\v]+", " ", line).strip() for line in value.split("\n")]
    out: list[str] = []
    blank = False
    for line in lines:
        if line:
            out.append(line)
            blank = False
        elif out and not blank:
            out.append("")
            blank = True
    return "\n".join(out).strip()


def normalize_quote(value: str) -> str:
    value = value.replace("\u00ad", "")
    value = unicodedata.normalize("NFKC", value)
    return re.sub(r"\s+", " ", value.casefold()).strip()


def visible_text(value: str) -> str:
    parser = VisibleTextParser()
    parser.feed(value)
    parser.close()
    return clean_text("".join(parser.parts))


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _zip_xml(archive: zipfile.ZipFile, member: str) -> ElementTree.Element:
    try:
        return ElementTree.fromstring(archive.read(member))
    except (
        KeyError,
        ElementTree.ParseError,
        zipfile.BadZipFile,
        NotImplementedError,
        OSError,
        zlib.error,
    ) as error:
        raise OSError(f"cannot parse {member}: {error}") from error


def docx_text(path: str) -> str:
    """Return the deterministic visible body-text surface for a DOCX file."""
    try:
        with zipfile.ZipFile(path) as archive:
            root = _zip_xml(archive, "word/document.xml")
    except (zipfile.BadZipFile, OSError) as error:
        raise OSError(f"cannot parse DOCX: {error}") from error

    paragraphs = []
    for paragraph in (node for node in root.iter() if _local_name(node.tag) == "p"):
        parts = []
        for node in paragraph.iter():
            name = _local_name(node.tag)
            if name == "t" and node.text:
                parts.append(node.text)
            elif name in {"tab", "br", "cr"}:
                parts.append(" ")
        paragraphs.append("".join(parts))
    return clean_text("\n".join(paragraphs))


def _xlsx_value_text(value: str) -> str:
    return re.sub(r"[\r\n\t]+", " ", value).strip()


def xlsx_text(path: str) -> str:
    """Return one deterministic, location-bound line per non-empty XLSX cell."""
    try:
        with zipfile.ZipFile(path) as archive:
            workbook = _zip_xml(archive, "xl/workbook.xml")
            relationships = _zip_xml(archive, "xl/_rels/workbook.xml.rels")
            rel_targets = {
                item.attrib.get("Id"): item.attrib.get("Target")
                for item in relationships
                if item.attrib.get("Id") and item.attrib.get("Target")
            }
            shared = []
            if "xl/sharedStrings.xml" in archive.namelist():
                strings = _zip_xml(archive, "xl/sharedStrings.xml")
                for item in strings:
                    if _local_name(item.tag) != "si":
                        continue
                    shared.append(
                        _xlsx_value_text(
                            "".join(
                                node.text or ""
                                for node in item.iter()
                                if _local_name(node.tag) == "t"
                            )
                        )
                    )

            lines = []
            for sheet in (
                node for node in workbook.iter() if _local_name(node.tag) == "sheet"
            ):
                sheet_name = _xlsx_value_text(sheet.attrib.get("name", ""))
                relation_id = next(
                    (
                        value
                        for key, value in sheet.attrib.items()
                        if _local_name(key) == "id"
                    ),
                    None,
                )
                target = rel_targets.get(relation_id)
                if not sheet_name or not target:
                    raise OSError("workbook sheet is missing a name or relationship")
                member = (
                    target.lstrip("/")
                    if target.startswith("/")
                    else posixpath.normpath(posixpath.join("xl", target))
                )
                worksheet = _zip_xml(archive, member)
                for cell in (
                    node for node in worksheet.iter() if _local_name(node.tag) == "c"
                ):
                    reference = cell.attrib.get("r")
                    if not reference:
                        raise OSError(
                            f"worksheet cell is missing a reference in {sheet_name}"
                        )
                    cell_type = cell.attrib.get("t")
                    if cell_type == "inlineStr":
                        value = "".join(
                            node.text or ""
                            for node in cell.iter()
                            if _local_name(node.tag) == "t"
                        )
                    else:
                        value_node = next(
                            (node for node in cell if _local_name(node.tag) == "v"),
                            None,
                        )
                        value = value_node.text if value_node is not None else ""
                        if cell_type == "s" and value:
                            try:
                                value = shared[int(value)]
                            except (IndexError, ValueError) as error:
                                raise OSError(
                                    "invalid shared-string index at "
                                    f"{sheet_name}!{reference}"
                                ) from error
                    value = _xlsx_value_text(value or "")
                    if value:
                        lines.append(f"{sheet_name}!{reference}: {value}")
    except (zipfile.BadZipFile, OSError) as error:
        raise OSError(f"cannot parse XLSX: {error}") from error
    return clean_text("\n".join(lines))


def eml_text(path: str) -> str:
    """Return selected headers and decoded message body text for an EML file."""
    try:
        with open(path, "rb") as handle:
            message = BytesParser(policy=policy.default).parse(handle)
        headers = [
            f"{name}: {message[name]}"
            for name in ("From", "To", "Cc", "Date", "Subject")
            if message[name] is not None
        ]
        plain_parts = []
        html_parts = []
        parts = message.walk() if message.is_multipart() else [message]
        for part in parts:
            if part.is_multipart() or part.get_content_disposition() == "attachment":
                continue
            content_type = part.get_content_type()
            if content_type not in {"text/plain", "text/html"}:
                continue
            content = part.get_content()
            if not isinstance(content, str):
                continue
            if content_type == "text/plain":
                plain_parts.append(content)
            else:
                html_parts.append(visible_text(content))
    except (OSError, UnicodeError, ValueError, LookupError) as error:
        raise OSError(f"cannot parse EML: {error}") from error
    body = plain_parts if plain_parts else html_parts
    blocks = ["\n".join(headers)] if headers else []
    if body:
        blocks.append("\n".join(body))
    return clean_text("\n\n".join(blocks))


def looks_like_markup(path: str, value: str) -> bool:
    low = value[:4096].casefold()
    return path.casefold().endswith(MARKUP_SUFFIXES) or any(
        marker in low for marker in ("<html", "<body", "<document", "<text")
    )


def pdf_text_stdlib(path: str) -> str:
    with open(path, "rb") as handle:
        data = handle.read()
    chunks = []
    for match in re.finditer(rb"(?m)^\d+\s+\d+\s+obj\b(.*?)endobj", data, re.S):
        body = match.group(1)
        stream = re.search(rb"stream\r?\n(.*?)endstream", body, re.S)
        if not stream:
            continue
        raw = stream.group(1)
        if b"/FlateDecode" in body:
            try:
                raw = zlib.decompress(raw.rstrip(b"\r\n"))
            except zlib.error:
                continue
        if b"Tj" not in raw and b"TJ" not in raw:
            continue
        for literal in re.findall(rb"\((?:[^()\\]|\\.)*\)", raw):
            chunks.append(literal[1:-1].replace(b"\\(", b"(").replace(b"\\)", b")"))
    # PDF generators commonly split a word into many adjacent literal strings
    # while retaining actual word spaces inside those strings. Adding a space
    # between every fragment turns `Taylor Vu` into `T a yl o r V u` and makes
    # exact-quote verification impossible. Preserve the stream's literal
    # continuity; clean_text still normalizes whitespace encoded by the PDF.
    decoded = b"".join(chunks).decode("utf-8", errors="replace")
    # A text-position change between sentence fragments may not carry a
    # literal space. Restore the common boundary without reintroducing spaces
    # inside the fragmented words handled above.
    decoded = re.sub(r"(?<=[.!?])(?=[A-Z])", " ", decoded)
    return clean_text(decoded)


def extract_document_text(path: str, extractor: str = "auto") -> str:
    suffix = path.casefold()
    if suffix.endswith(".docx"):
        return docx_text(path)
    if suffix.endswith(".xlsx"):
        return xlsx_text(path)
    if suffix.endswith(".eml"):
        return eml_text(path)
    if suffix.endswith(".pdf"):
        if extractor == "auto" and HAVE_PDFTOTEXT:
            proc = subprocess.run(
                ["pdftotext", "-q", "-enc", "UTF-8", path, "-"],
                capture_output=True,
            )
            if proc.returncode != 0:
                error = proc.stderr.decode("utf-8", errors="replace").strip()
                raise OSError(f"pdftotext failed on {path}: {error}")
            return clean_text(proc.stdout.decode("utf-8", errors="replace"))
        return pdf_text_stdlib(path)
    with open(path, encoding="utf-8", errors="replace") as handle:
        raw = handle.read()
    return visible_text(raw) if looks_like_markup(path, raw) else clean_text(raw)
