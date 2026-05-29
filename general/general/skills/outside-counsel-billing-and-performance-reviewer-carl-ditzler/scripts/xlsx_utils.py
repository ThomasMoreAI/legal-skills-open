#!/usr/bin/env python3
"""XLSX reader/writer helper"""
"""Codex created this script"""

from __future__ import annotations

import datetime as _dt
import html
import io
import re
import zipfile
from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree as ET

NS = {
    "main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "rel": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "pkgrel": "http://schemas.openxmlformats.org/package/2006/relationships",
}


def _column_letters_to_index(value: str) -> int:
    total = 0
    for char in value:
        total = total * 26 + (ord(char.upper()) - 64)
    return total - 1


def _cell_ref_to_index(cell_ref: str) -> int:
    match = re.match(r"([A-Z]+)", cell_ref.upper())
    if not match:
        raise ValueError(f"Unsupported cell reference: {cell_ref}")
    return _column_letters_to_index(match.group(1))


def _load_shared_strings(zf: zipfile.ZipFile) -> list[str]:
    try:
        raw = zf.read("xl/sharedStrings.xml")
    except KeyError:
        return []
    root = ET.fromstring(raw)
    values: list[str] = []
    for si in root.findall("main:si", NS):
        text_parts = []
        for node in si.iter():
            if node.tag.endswith("}t") and node.text:
                text_parts.append(node.text)
        values.append("".join(text_parts))
    return values


def _sheet_target(zf: zipfile.ZipFile, sheet_name: str | None) -> str:
    workbook = ET.fromstring(zf.read("xl/workbook.xml"))
    rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    rel_map = {
        rel.attrib["Id"]: rel.attrib["Target"]
        for rel in rels.findall("pkgrel:Relationship", NS)
    }
    sheets = workbook.find("main:sheets", NS)
    if sheets is None:
        raise ValueError("Workbook has no sheets")
    sheet_nodes = sheets.findall("main:sheet", NS)
    if not sheet_nodes:
        raise ValueError("Workbook has no sheets")
    sheet = sheet_nodes[0]
    if sheet_name:
        for candidate in sheet_nodes:
            if candidate.attrib.get("name") == sheet_name:
                sheet = candidate
                break
        else:
            raise ValueError(f"Sheet not found: {sheet_name}")
    rel_id = sheet.attrib.get(f"{{{NS['rel']}}}id")
    if not rel_id or rel_id not in rel_map:
        raise ValueError("Could not resolve sheet relationship")
    target = rel_map[rel_id]
    if not target.startswith("xl/"):
        target = f"xl/{target}"
    return target


def read_xlsx(path: str | Path, sheet_name: str | None = None) -> list[dict[str, str]]:
    with zipfile.ZipFile(path) as zf:
        shared_strings = _load_shared_strings(zf)
        target = _sheet_target(zf, sheet_name)
        root = ET.fromstring(zf.read(target))

    rows: list[list[str]] = []
    sheet_data = root.find("main:sheetData", NS)
    if sheet_data is None:
        return []

    for row_node in sheet_data.findall("main:row", NS):
        row: list[str] = []
        for cell in row_node.findall("main:c", NS):
            ref = cell.attrib.get("r", "")
            index = _cell_ref_to_index(ref)
            while len(row) <= index:
                row.append("")

            cell_type = cell.attrib.get("t", "")
            value = ""
            if cell_type == "inlineStr":
                text_node = cell.find("main:is/main:t", NS)
                value = text_node.text if text_node is not None and text_node.text else ""
            else:
                value_node = cell.find("main:v", NS)
                raw_value = value_node.text if value_node is not None and value_node.text else ""
                if cell_type == "s" and raw_value:
                    value = shared_strings[int(raw_value)]
                else:
                    value = raw_value
            row[index] = value
        rows.append(row)

    if not rows:
        return []
    headers = [header.strip() or f"column_{i+1}" for i, header in enumerate(rows[0])]
    records: list[dict[str, str]] = []
    for values in rows[1:]:
        padded = list(values) + [""] * max(0, len(headers) - len(values))
        records.append({headers[i]: padded[i] for i in range(len(headers))})
    return records


def _xml_escape(value: object) -> str:
    return html.escape("" if value is None else str(value), quote=False)


def _worksheet_xml(rows: list[list[object]]) -> bytes:
    xml_rows = []
    for row_index, row in enumerate(rows, start=1):
        cells = []
        for col_index, value in enumerate(row, start=1):
            cell_ref = _index_to_col_letters(col_index - 1) + str(row_index)
            cell_text = _xml_escape(value)
            cells.append(
                f'<c r="{cell_ref}" t="inlineStr"><is><t>{cell_text}</t></is></c>'
            )
        xml_rows.append(f'<row r="{row_index}">{"".join(cells)}</row>')
    xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        f'<sheetData>{"".join(xml_rows)}</sheetData>'
        "</worksheet>"
    )
    return xml.encode("utf-8")


def _index_to_col_letters(index: int) -> str:
    result = []
    index += 1
    while index:
        index, remainder = divmod(index - 1, 26)
        result.append(chr(65 + remainder))
    return "".join(reversed(result))


def write_xlsx(path: str | Path, headers: list[str], rows: Iterable[Iterable[object]], sheet_name: str = "Sheet1") -> None:
    path = Path(path)
    rows_list = [list(headers)] + [list(row) for row in rows]
    workbook_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        f'<sheets><sheet name="{_xml_escape(sheet_name)}" sheetId="1" '
        'r:id="rId1"/></sheets></workbook>'
    ).encode("utf-8")
    workbook_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" '
        'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" '
        'Target="worksheets/sheet1.xml"/>'
        '<Relationship Id="rId2" '
        'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" '
        'Target="styles.xml"/>'
        '</Relationships>'
    ).encode("utf-8")
    root_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" '
        'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
        'Target="xl/workbook.xml"/>'
        '<Relationship Id="rId2" '
        'Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" '
        'Target="docProps/core.xml"/>'
        '<Relationship Id="rId3" '
        'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" '
        'Target="docProps/app.xml"/>'
        '</Relationships>'
    ).encode("utf-8")
    content_types = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/xl/workbook.xml" '
        'ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
        '<Override PartName="/xl/worksheets/sheet1.xml" '
        'ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
        '<Override PartName="/xl/styles.xml" '
        'ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'
        '<Override PartName="/docProps/core.xml" '
        'ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>'
        '<Override PartName="/docProps/app.xml" '
        'ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>'
        '</Types>'
    ).encode("utf-8")
    styles = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        '<fonts count="1"><font><sz val="11"/><name val="Calibri"/></font></fonts>'
        '<fills count="1"><fill><patternFill patternType="none"/></fill></fills>'
        '<borders count="1"><border/></borders>'
        '<cellStyleXfs count="1"><xf/></cellStyleXfs>'
        '<cellXfs count="1"><xf xfId="0"/></cellXfs>'
        '<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>'
        '</styleSheet>'
    ).encode("utf-8")
    now = _dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    core = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
        'xmlns:dc="http://purl.org/dc/elements/1.1/" '
        'xmlns:dcterms="http://purl.org/dc/terms/" '
        'xmlns:dcmitype="http://purl.org/dc/dcmitype/" '
        'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
        '<dc:creator>Codex Skill</dc:creator>'
        '<cp:lastModifiedBy>Codex Skill</cp:lastModifiedBy>'
        f'<dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created>'
        f'<dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified>'
        '</cp:coreProperties>'
    ).encode("utf-8")
    app = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" '
        'xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">'
        '<Application>Codex Skill</Application>'
        '</Properties>'
    ).encode("utf-8")

    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types)
        zf.writestr("_rels/.rels", root_rels)
        zf.writestr("docProps/core.xml", core)
        zf.writestr("docProps/app.xml", app)
        zf.writestr("xl/workbook.xml", workbook_xml)
        zf.writestr("xl/_rels/workbook.xml.rels", workbook_rels)
        zf.writestr("xl/styles.xml", styles)
        zf.writestr("xl/worksheets/sheet1.xml", _worksheet_xml(rows_list))
