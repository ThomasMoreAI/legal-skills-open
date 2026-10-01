#!/usr/bin/env python3
"""Ministry of Justice data-tables CLI.

Read-only stdlib wrapper around public Ministry of Justice justice-statistics
workbooks. No login, API key, browser automation, local cache, or data mutation.
"""

from __future__ import annotations

import argparse
import html
import json
import pathlib
import re
import ssl
import sys
import urllib.parse
import zipfile
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from io import BytesIO
from typing import Any

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "lib"))
import nzfetch  # noqa: E402

MOJ_TABLES_URL = "https://www.justice.govt.nz/justice-sector-policy/research-data/justice-statistics/data-tables/"
CKAN_PACKAGE_SEARCH = "https://catalogue.data.govt.nz/api/3/action/package_search"
MOJ_OWNER_ORG = "07e149dd-d4e7-43b5-aad2-29485d7afaf5"
UA = "justice-data-nz-skill/1.0 (+https://github.com/thecolab-ai/.skills)"
DEFAULT_TIMEOUT = 10

XML_NS = {
    "a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}
REL_ID = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"


class CliError(RuntimeError):
    """User-visible command failure."""

    def __init__(self, message: str, *, code: str = "error", source_url: str | None = None):
        super().__init__(message)
        self.code = code
        self.source_url = source_url


class UpstreamUnavailable(CliError):
    pass


def die(message: str, code: int = 1) -> None:
    print(f"justice-data-nz: {message}", file=sys.stderr)
    raise SystemExit(code)


def clean_text(value: Any) -> str:
    text = html.unescape(str(value or "")).replace("\xa0", " ")
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def key_text(value: Any) -> str:
    return re.sub(r"[^a-z0-9]+", " ", clean_text(value).lower()).strip()


def fetch_bytes(url: str, timeout: int = DEFAULT_TIMEOUT) -> tuple[bytes, str, str]:
    try:
        body, content_type, final_url = nzfetch.fetch_bytes(
            url,
            timeout=timeout,
            accept="text/html,application/json,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,*/*;q=0.8",
            headers={"Accept-Language": "en-NZ,en;q=0.9"},
            context=ssl.create_default_context(),
        )
        return body, final_url, content_type
    except nzfetch.Blocked as exc:
        raise UpstreamUnavailable(
            f"network error: the Ministry site may be bot-protected or rate-limiting this network. {exc}",
            code="upstream_blocked",
            source_url=url,
        ) from exc
    except nzfetch.FetchError as exc:
        raise CliError(f"upstream fetch failed for {url}. {exc}", code="upstream_http", source_url=url) from exc


def fetch_text(url: str, timeout: int = DEFAULT_TIMEOUT) -> tuple[str, str]:
    body, final_url, _ = fetch_bytes(url, timeout=timeout)
    return body.decode("utf-8", errors="replace"), final_url


def fetch_json(url: str, timeout: int = DEFAULT_TIMEOUT) -> dict[str, Any]:
    body, _, _ = fetch_bytes(url, timeout=timeout)
    try:
        return json.loads(body.decode("utf-8", errors="replace"))
    except json.JSONDecodeError as exc:
        raise CliError(f"invalid JSON from {url}: {exc}", code="invalid_json", source_url=url) from exc


def parse_period(url: str, title: str = "") -> dict[str, Any] | None:
    haystack = f"{urllib.parse.unquote(url)} {title}".lower()
    match = re.search(r"(?:^|[_\-\s])(dec|december|jun|june)(?:[_\-\s]?)(20\d{2}|\d{2})(?:[_\-\s.]|$)", haystack)
    if not match:
        return None
    month_token = match.group(1)
    raw_year = match.group(2)
    year = int(raw_year) if len(raw_year) == 4 else 2000 + int(raw_year)
    if month_token.startswith("dec"):
        return {
            "type": "calendar_year",
            "year": year,
            "month": 12,
            "label": f"year ending 31 December {year}",
        }
    return {
        "type": "financial_year",
        "year": year,
        "month": 6,
        "label": f"year ending 30 June {year}",
    }


def infer_topic_group(section: str, topic: str, url: str) -> str:
    haystack = key_text(f"{section} {topic} {url}")
    if "family violence" in haystack:
        return "family-violence"
    if "children and young people" in haystack or "youth court" in haystack:
        return "youth"
    if "family court" in haystack or "protection order" in haystack or "adopted" in haystack:
        return "family-court"
    if "legal aid" in haystack or "collections" in haystack or "programmes" in haystack:
        return "justice-services"
    if "offence" in haystack:
        return "offence-type"
    if "charges" in haystack or "convicted" in haystack:
        return "general"
    return "other"


class TableLinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.section = ""
        self.topic = ""
        self.links: list[dict[str, Any]] = []
        self._capture_tag: str | None = None
        self._capture_text: list[str] = []
        self._link_href: str | None = None
        self._link_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {name: value or "" for name, value in attrs}
        if tag in {"h3", "h4"}:
            self._capture_tag = tag
            self._capture_text = []
        elif tag == "a":
            self._link_href = attrs_dict.get("href")
            self._link_text = []

    def handle_data(self, data: str) -> None:
        if self._capture_tag:
            self._capture_text.append(data)
        if self._link_href:
            self._link_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == self._capture_tag:
            text = clean_text(" ".join(self._capture_text))
            if tag == "h3":
                self.section = text
                self.topic = ""
            elif tag == "h4":
                self.topic = text
            self._capture_tag = None
            self._capture_text = []
        elif tag == "a" and self._link_href:
            href = self._link_href
            link_text = clean_text(" ".join(self._link_text))
            if href.lower().split("?", 1)[0].endswith(".xlsx"):
                url = urllib.parse.urljoin(MOJ_TABLES_URL, href)
                topic = self.topic or link_text or urllib.parse.unquote(url.rsplit("/", 1)[-1])
                period = parse_period(url, topic)
                self.links.append(
                    {
                        "source": "ministry_of_justice",
                        "topic": topic,
                        "section": self.section,
                        "group": infer_topic_group(self.section, topic, url),
                        "link_text": link_text,
                        "period": period,
                        "url": url,
                        "filename": urllib.parse.unquote(url.rsplit("/", 1)[-1]),
                    }
                )
            self._link_href = None
            self._link_text = []


def discover_official_tables(timeout: int = DEFAULT_TIMEOUT) -> list[dict[str, Any]]:
    text, final_url = fetch_text(MOJ_TABLES_URL, timeout=timeout)
    parser = TableLinkParser()
    parser.feed(text)
    if not parser.links:
        raise CliError(f"could not find workbook links on {final_url}", code="no_workbooks", source_url=final_url)
    return parser.links


def discover_ckan_tables(query: str | None, timeout: int = DEFAULT_TIMEOUT) -> list[dict[str, Any]]:
    params = {
        "fq": f"owner_org:{MOJ_OWNER_ORG}",
        "q": query or "justice statistics data tables charged convicted family violence youth",
        "rows": "50",
    }
    url = CKAN_PACKAGE_SEARCH + "?" + urllib.parse.urlencode(params)
    data = fetch_json(url, timeout=timeout)
    if not data.get("success"):
        raise CliError("data.govt.nz package_search did not return success", code="ckan_error", source_url=url)
    items: list[dict[str, Any]] = []
    for pkg in data.get("result", {}).get("results", []):
        for resource in pkg.get("resources", []) or [{}]:
            items.append(
                {
                    "source": "catalogue.data.govt.nz",
                    "topic": clean_text(pkg.get("title") or resource.get("name") or pkg.get("name")),
                    "section": "CKAN metadata mirror",
                    "group": infer_topic_group("", f"{pkg.get('title')} {pkg.get('notes')}", resource.get("url") or ""),
                    "link_text": clean_text(resource.get("name") or ""),
                    "period": parse_period(f"{pkg.get('modified')} {pkg.get('metadata_modified')}", pkg.get("title") or ""),
                    "url": resource.get("url") or pkg.get("url") or "",
                    "format": resource.get("format") or "",
                    "resource_id": resource.get("id") or "",
                    "package_name": pkg.get("name") or "",
                    "notes": clean_text(pkg.get("notes") or "")[:300],
                    "metadata_only": True,
                }
            )
    return items


def find_table(tables: list[dict[str, Any]], required_terms: list[str], blocked_terms: list[str] | None = None) -> dict[str, Any]:
    required = [key_text(term) for term in required_terms]
    blocked = [key_text(term) for term in (blocked_terms or [])]
    for table in tables:
        haystack = key_text(" ".join(str(table.get(k, "")) for k in ("topic", "section", "link_text", "filename", "url")))
        if all(term in haystack for term in required) and not any(term in haystack for term in blocked):
            return table
    available = "; ".join(t.get("topic", "") for t in tables[:12])
    raise CliError(
        f"could not find MoJ table matching {', '.join(required_terms)}. Available examples: {available}",
        code="table_not_found",
        source_url=MOJ_TABLES_URL,
    )


def column_index(cell_ref: str) -> int:
    match = re.match(r"([A-Z]+)", cell_ref or "")
    if not match:
        return -1
    value = 0
    for char in match.group(1):
        value = value * 26 + (ord(char) - ord("A") + 1)
    return value - 1


class Workbook:
    def __init__(self, body: bytes, source_url: str) -> None:
        self.source_url = source_url
        try:
            self.zf = zipfile.ZipFile(BytesIO(body))
        except zipfile.BadZipFile as exc:
            raise CliError(f"invalid XLSX workbook from {source_url}: {exc}", code="invalid_xlsx", source_url=source_url) from exc
        self.shared_strings = self._read_shared_strings()
        self.sheets = self._read_sheet_paths()

    def _read_shared_strings(self) -> list[str]:
        if "xl/sharedStrings.xml" not in self.zf.namelist():
            return []
        root = ET.fromstring(self.zf.read("xl/sharedStrings.xml"))
        values: list[str] = []
        for si in root.findall("a:si", XML_NS):
            values.append("".join(t.text or "" for t in si.findall(".//a:t", XML_NS)))
        return values

    def _read_sheet_paths(self) -> dict[str, str]:
        workbook = ET.fromstring(self.zf.read("xl/workbook.xml"))
        rels = ET.fromstring(self.zf.read("xl/_rels/workbook.xml.rels"))
        relmap = {rel.attrib["Id"]: rel.attrib["Target"] for rel in rels}
        sheets: dict[str, str] = {}
        for sheet in workbook.findall("a:sheets/a:sheet", XML_NS):
            target = relmap[sheet.attrib[REL_ID]]
            path = target.lstrip("/")
            if not path.startswith("xl/"):
                path = "xl/" + path
            sheets[sheet.attrib["name"]] = path
        return sheets

    def cell_value(self, cell: ET.Element) -> str:
        cell_type = cell.attrib.get("t")
        if cell_type == "inlineStr":
            return "".join(t.text or "" for t in cell.findall(".//a:t", XML_NS))
        value = cell.find("a:v", XML_NS)
        if value is None or value.text is None:
            return ""
        raw = value.text
        if cell_type == "s":
            try:
                return self.shared_strings[int(raw)]
            except (ValueError, IndexError):
                return raw
        return raw

    def rows(self, sheet_name: str) -> list[list[str]]:
        path = self.sheets[sheet_name]
        root = ET.fromstring(self.zf.read(path))
        rows: list[list[str]] = []
        for row in root.findall("a:sheetData/a:row", XML_NS):
            values: list[str] = []
            next_index = 0
            for cell in row.findall("a:c", XML_NS):
                idx = column_index(cell.attrib.get("r", ""))
                if idx < 0:
                    idx = next_index
                while len(values) <= idx:
                    values.append("")
                values[idx] = clean_text(self.cell_value(cell))
                next_index = idx + 1
            rows.append(values)
        return rows


def load_workbook(table: dict[str, Any], timeout: int) -> Workbook:
    body, final_url, content_type = fetch_bytes(table["url"], timeout=timeout)
    if "html" in content_type and not table["url"].lower().endswith(".xlsx"):
        raise CliError(
            f"expected an XLSX workbook but got HTML from {final_url}",
            code="not_workbook",
            source_url=final_url,
        )
    return Workbook(body, final_url)


def find_sheet_name(workbook: Workbook, terms: str | list[str]) -> str:
    required = [key_text(terms)] if isinstance(terms, str) else [key_text(term) for term in terms]
    for name in workbook.sheets:
        haystack = key_text(name)
        if all(term in haystack for term in required):
            return name
    raise CliError(
        f"could not find worksheet matching {', '.join(required)} in {workbook.source_url}",
        code="sheet_not_found",
        source_url=workbook.source_url,
    )


def parse_number(raw: Any) -> int | float | None:
    text = clean_text(raw).replace(",", "")
    if not text or "%" in text or text.startswith("<"):
        return None
    try:
        value = float(text)
    except ValueError:
        return None
    if value.is_integer():
        return int(value)
    return value


def fmt_value(value: Any) -> str:
    if isinstance(value, int):
        return f"{value:,}"
    if isinstance(value, float):
        return f"{value:,.2f}"
    return str(value)


def row_year_columns(row: list[str]) -> list[tuple[int, int]]:
    years: list[tuple[int, int]] = []
    for index, value in enumerate(row):
        text = clean_text(value)
        if re.fullmatch(r"(19|20)\d{2}", text):
            years.append((index, int(text)))
    return years


def looks_like_year_header(year_columns: list[tuple[int, int]]) -> bool:
    if len(year_columns) < 3:
        return False
    years = [year for _, year in year_columns]
    run = 1
    best = 1
    for previous, current in zip(years, years[1:]):
        if current == previous + 1:
            run += 1
            best = max(best, run)
        else:
            run = 1
    return best >= 3


def find_year_header(rows: list[list[str]], year: int) -> tuple[int, int, int, list[int]]:
    wanted = str(year)
    available: set[int] = set()
    for row_index, row in enumerate(rows):
        year_columns = row_year_columns(row)
        if not looks_like_year_header(year_columns):
            continue
        available.update(value for _, value in year_columns)
        first_year_col = year_columns[0][0]
        for col_index, value in year_columns:
            if clean_text(value) == wanted:
                return row_index, first_year_col, col_index, [year for _, year in year_columns]
    if available:
        ordered = sorted(available)
        raise CliError(
            f"year {year} is not available; available years are {ordered[0]}-{ordered[-1]}",
            code="year_not_available",
        )
    raise CliError(f"could not find year columns for {year}", code="year_not_found")


def is_plain_total(dimensions: list[str]) -> bool:
    non_empty = [clean_text(value) for value in dimensions if clean_text(value)]
    return bool(non_empty) and non_empty[0].lower() == "total"


def extract_year_rows(
    workbook: Workbook,
    sheet_terms: str | list[str],
    year: int,
    *,
    counts_only: bool = True,
) -> tuple[str, list[int], list[dict[str, Any]]]:
    sheet_name = find_sheet_name(workbook, sheet_terms)
    rows = workbook.rows(sheet_name)
    header_index, first_year_col, year_col, available_years = find_year_header(rows, year)
    header = rows[header_index]
    dimensions = []
    for index in range(first_year_col):
        label = clean_text(header[index] if index < len(header) else "")
        dimensions.append(label or f"dimension_{index + 1}")

    records: list[dict[str, Any]] = []
    previous_dimensions: dict[int, str] = {}
    for row in rows[header_index + 1 :]:
        if not any(clean_text(value) for value in row):
            if records:
                break
            continue

        raw_value = clean_text(row[year_col] if year_col < len(row) else "")
        if not raw_value:
            continue
        parsed = parse_number(raw_value)
        if counts_only and parsed is None:
            continue
        if counts_only and isinstance(parsed, float) and not parsed.is_integer():
            continue

        dim_values: list[str] = []
        for index, label in enumerate(dimensions):
            value = clean_text(row[index] if index < len(row) else "")
            if value:
                previous_dimensions[index] = value
            elif index in previous_dimensions:
                value = previous_dimensions[index]
            dim_values.append(value)
        if not any(dim_values):
            continue

        record = {
            label: value
            for label, value in zip(dimensions, dim_values)
            if value and not label.startswith("dimension_")
        }
        for index, value in enumerate(dim_values):
            label = dimensions[index]
            if value and label.startswith("dimension_"):
                record[label] = value
        record["value"] = parsed if parsed is not None else raw_value
        record["raw_value"] = raw_value
        records.append(record)

        if is_plain_total(dim_values):
            break

    if not records:
        raise CliError(f"no records found for year {year} in worksheet {sheet_name}", code="no_records")
    return sheet_name, available_years, records


def filter_records(records: list[dict[str, Any]], query: str | None, *, key_contains: str | None = None) -> list[dict[str, Any]]:
    if not query or query.lower() == "all":
        return records
    needle = key_text(query)
    filtered: list[dict[str, Any]] = []
    for record in records:
        values = []
        for key, value in record.items():
            if key in {"value", "raw_value"}:
                continue
            if key_contains and key_contains not in key_text(key):
                continue
            values.append(str(value))
        if any(needle in key_text(value) for value in values):
            filtered.append(record)
    return filtered


def filter_age_group(records: list[dict[str, Any]], age_group: str) -> list[dict[str, Any]]:
    if age_group.lower() == "all":
        return records
    filtered = filter_records(records, age_group, key_contains="age group")
    return filtered or records


def source_info(table: dict[str, Any], workbook: Workbook | None = None) -> dict[str, Any]:
    info = {
        "publisher": "New Zealand Ministry of Justice",
        "page_url": MOJ_TABLES_URL,
        "workbook_url": workbook.source_url if workbook else table.get("url"),
        "workbook_title": table.get("topic"),
        "period": table.get("period"),
    }
    return info


def emit_json(data: dict[str, Any]) -> None:
    print(json.dumps(data, indent=2, ensure_ascii=False, sort_keys=False))


def print_record_list(title: str, records: list[dict[str, Any]], limit: int | None = None) -> None:
    print(title)
    shown = records if limit is None else records[:limit]
    for record in shown:
        labels = [str(value) for key, value in record.items() if key not in {"value", "raw_value"}]
        print(f"  {' | '.join(labels)}: {fmt_value(record.get('value'))}")
    if limit is not None and len(records) > limit:
        print(f"  ... {len(records) - limit} more")


def cmd_tables(args: argparse.Namespace) -> None:
    warning = None
    try:
        tables = discover_official_tables(timeout=args.timeout)
        source = "ministry_of_justice"
    except UpstreamUnavailable as exc:
        tables = discover_ckan_tables(args.query, timeout=args.timeout)
        source = "catalogue.data.govt.nz"
        warning = (
            f"MoJ direct page unavailable ({exc.code}); showing CKAN metadata only. "
            "Current workbook values still require MoJ direct downloads."
        )

    if args.query:
        query = key_text(args.query)
        tables = [
            table
            for table in tables
            if query in key_text(" ".join(str(table.get(k, "")) for k in ("topic", "section", "link_text", "filename", "notes")))
        ]
    if args.limit:
        tables = tables[: args.limit]

    payload = {
        "command": "tables",
        "status": "ok",
        "source": source,
        "source_url": MOJ_TABLES_URL if source == "ministry_of_justice" else CKAN_PACKAGE_SEARCH,
        "warning": warning,
        "count": len(tables),
        "tables": tables,
    }
    if args.json:
        emit_json(payload)
        return
    if warning:
        print(warning)
    print(f"{len(tables)} Ministry of Justice data table(s)")
    for table in tables:
        period = table.get("period") or {}
        period_label = period.get("label") or "period not parsed"
        print(f"- {table.get('topic')} [{table.get('group')}] - {period_label}")
        print(f"  {table.get('url')}")


def tables_for_data(timeout: int) -> list[dict[str, Any]]:
    return discover_official_tables(timeout=timeout)


def cmd_convictions(args: argparse.Namespace) -> None:
    tables = tables_for_data(args.timeout)
    people_table = find_table(tables, ["people with finalised charges"])
    charges_table = find_table(tables, ["all finalised charges", "convicted charges"])
    people_wb = load_workbook(people_table, args.timeout)
    charges_wb = load_workbook(charges_table, args.timeout)

    people_sheet, people_years, people = extract_year_rows(people_wb, "4.People convicted by offence", args.year)
    finalised_sheet, finalised_years, finalised = extract_year_rows(charges_wb, "1a.Charges by offence-division", args.year)
    convicted_sheet, convicted_years, convicted = extract_year_rows(charges_wb, "3a.Conv charges-offence-div", args.year)

    if args.offence:
        people = filter_records(people, args.offence)
        finalised = filter_records(finalised, args.offence)
        convicted = filter_records(convicted, args.offence)
        if not (people or finalised or convicted):
            raise CliError(f"no offence rows matched {args.offence!r} for {args.year}", code="no_matches")

    payload = {
        "command": "convictions",
        "status": "ok",
        "year": args.year,
        "offence_filter": args.offence,
        "people_convicted_by_offence": people,
        "finalised_charges_by_offence": finalised,
        "convicted_charges_by_offence": convicted,
        "worksheets": {
            "people_convicted_by_offence": people_sheet,
            "finalised_charges_by_offence": finalised_sheet,
            "convicted_charges_by_offence": convicted_sheet,
        },
        "available_years": {
            "people": [people_years[0], people_years[-1]],
            "charges": [finalised_years[0], finalised_years[-1]],
            "convicted_charges": [convicted_years[0], convicted_years[-1]],
        },
        "sources": [source_info(people_table, people_wb), source_info(charges_table, charges_wb)],
    }
    if args.json:
        emit_json(payload)
        return
    print(f"MoJ convictions and charges for {args.year}")
    print_record_list("People convicted by offence:", people, limit=12 if not args.offence else None)
    print_record_list("Finalised charges by offence:", finalised, limit=12 if not args.offence else None)
    print_record_list("Convicted charges by offence:", convicted, limit=12 if not args.offence else None)
    print(f"Source: {people_wb.source_url}")


def cmd_sentencing(args: argparse.Namespace) -> None:
    tables = tables_for_data(args.timeout)
    people_table = find_table(tables, ["people with finalised charges"])
    charges_table = find_table(tables, ["all finalised charges", "convicted charges"])
    people_wb = load_workbook(people_table, args.timeout)
    charges_wb = load_workbook(charges_table, args.timeout)

    people_sheet, people_years, people = extract_year_rows(people_wb, "5a.Convicted by sentence", args.year)
    charges_sheet, charges_years, charges = extract_year_rows(charges_wb, "4.Conv charges by sentence", args.year)
    payload = {
        "command": "sentencing",
        "status": "ok",
        "year": args.year,
        "people_convicted_by_most_serious_sentence": people,
        "convicted_charges_by_most_serious_sentence": charges,
        "worksheets": {
            "people_convicted_by_most_serious_sentence": people_sheet,
            "convicted_charges_by_most_serious_sentence": charges_sheet,
        },
        "available_years": {
            "people": [people_years[0], people_years[-1]],
            "charges": [charges_years[0], charges_years[-1]],
        },
        "sources": [source_info(people_table, people_wb), source_info(charges_table, charges_wb)],
    }
    if args.json:
        emit_json(payload)
        return
    print(f"MoJ sentencing outcomes for {args.year}")
    print_record_list("People convicted by most serious sentence:", people)
    print_record_list("Convicted charges by most serious sentence:", charges)
    print(f"Source: {people_wb.source_url}")


def cmd_family_violence(args: argparse.Namespace) -> None:
    tables = tables_for_data(args.timeout)
    table = find_table(tables, ["family violence offences"], blocked_terms=["programmes"])
    workbook = load_workbook(table, args.timeout)

    all_sheet, years, all_charges = extract_year_rows(workbook, "1a.All charges", args.year)
    offence_sheet, _, charges_by_offence = extract_year_rows(workbook, "1b.FV charges by offence", args.year)
    outcome_sheet, _, charges_by_outcome = extract_year_rows(workbook, "1c.d.e.FV charges outcome", args.year)
    people_sheet, _, people_charged = extract_year_rows(workbook, "2a.People charged by offence", args.year)
    convicted_sheet, _, people_convicted = extract_year_rows(workbook, "3a.People convicted by offence", args.year)
    sentence_sheet, _, people_sentenced = extract_year_rows(workbook, "3b.People convicted sentence", args.year)

    if args.offence:
        charges_by_offence = filter_records(charges_by_offence, args.offence)
        people_charged = filter_records(people_charged, args.offence)
        people_convicted = filter_records(people_convicted, args.offence)
        if not (charges_by_offence or people_charged or people_convicted):
            raise CliError(f"no family-violence offence rows matched {args.offence!r} for {args.year}", code="no_matches")

    payload = {
        "command": "family-violence",
        "status": "ok",
        "year": args.year,
        "offence_filter": args.offence,
        "family_violence_vs_other_charges": all_charges,
        "family_violence_charges_by_offence": charges_by_offence,
        "family_violence_charges_by_outcome": charges_by_outcome,
        "people_charged_by_offence": people_charged,
        "people_convicted_by_offence": people_convicted,
        "people_convicted_by_sentence": people_sentenced,
        "worksheets": {
            "family_violence_vs_other_charges": all_sheet,
            "family_violence_charges_by_offence": offence_sheet,
            "family_violence_charges_by_outcome": outcome_sheet,
            "people_charged_by_offence": people_sheet,
            "people_convicted_by_offence": convicted_sheet,
            "people_convicted_by_sentence": sentence_sheet,
        },
        "available_years": [years[0], years[-1]],
        "sources": [source_info(table, workbook)],
    }
    if args.json:
        emit_json(payload)
        return
    print(f"MoJ family-violence offence statistics for {args.year}")
    print_record_list("Family violence versus other finalised charges:", all_charges)
    print_record_list("Family-violence charges by outcome:", charges_by_outcome)
    print_record_list("People convicted by sentence:", people_sentenced)
    print(f"Source: {workbook.source_url}")


def cmd_youth(args: argparse.Namespace) -> None:
    tables = tables_for_data(args.timeout)
    if args.scope == "youth-court":
        table = find_table(tables, ["children and young people", "youth court"])
    else:
        table = find_table(tables, ["children and young people", "any court"])
    workbook = load_workbook(table, args.timeout)

    charges_sheet, years, charges_outcome = extract_year_rows(workbook, "1.Charges by outcome", args.year)
    people_sheet, _, people_outcome = extract_year_rows(workbook, "3.People by outcome", args.year)
    offence_sheet, _, people_offence = extract_year_rows(workbook, "4.People by offence", args.year)
    orders_sheet, _, people_orders = extract_year_rows(workbook, ["7", "people", "order"], args.year)

    charges_outcome = filter_age_group(charges_outcome, args.age_group)
    people_outcome = filter_age_group(people_outcome, args.age_group)
    people_offence = filter_age_group(people_offence, args.age_group)
    people_orders = filter_age_group(people_orders, args.age_group)
    if args.offence:
        people_offence = filter_records(people_offence, args.offence)
        if not people_offence:
            raise CliError(f"no youth offence rows matched {args.offence!r} for {args.year}", code="no_matches")

    payload = {
        "command": "youth",
        "status": "ok",
        "year": args.year,
        "scope": args.scope,
        "age_group_filter": args.age_group,
        "offence_filter": args.offence,
        "charges_by_outcome": charges_outcome,
        "children_and_young_people_by_outcome": people_outcome,
        "children_and_young_people_by_offence": people_offence,
        "children_and_young_people_with_orders_by_order": people_orders,
        "worksheets": {
            "charges_by_outcome": charges_sheet,
            "children_and_young_people_by_outcome": people_sheet,
            "children_and_young_people_by_offence": offence_sheet,
            "children_and_young_people_with_orders_by_order": orders_sheet,
        },
        "available_years": [years[0], years[-1]],
        "sources": [source_info(table, workbook)],
    }
    if args.json:
        emit_json(payload)
        return
    print(f"MoJ youth justice statistics for {args.year} ({args.scope})")
    print_record_list("Charges by outcome:", charges_outcome)
    print_record_list("Children and young people by offence:", people_offence, limit=12 if not args.offence else None)
    print_record_list("Children and young people with orders by order:", people_orders)
    print(f"Source: {workbook.source_url}")


def add_year_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--year", type=int, required=True, help="Calendar or table year, for example 2025")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Query public New Zealand Ministry of Justice data tables.")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="Network timeout in seconds")
    sub = parser.add_subparsers(dest="command", required=True)

    tables = sub.add_parser("tables", help="List current MoJ data-table workbooks")
    tables.add_argument("--query", help="Filter table list by text")
    tables.add_argument("--limit", type=int, help="Maximum rows to print")
    tables.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    tables.set_defaults(func=cmd_tables)

    convictions = sub.add_parser("convictions", help="Convictions and charges by offence")
    add_year_arg(convictions)
    convictions.add_argument("--offence", help="Filter offence rows by text, for example assault")
    convictions.set_defaults(func=cmd_convictions)

    sentencing = sub.add_parser("sentencing", help="Sentencing outcomes")
    add_year_arg(sentencing)
    sentencing.set_defaults(func=cmd_sentencing)

    family = sub.add_parser("family-violence", help="Family-violence offence statistics")
    add_year_arg(family)
    family.add_argument("--offence", help="Filter offence rows by text, for example assault")
    family.set_defaults(func=cmd_family_violence)

    youth = sub.add_parser("youth", help="Children and young people justice statistics")
    add_year_arg(youth)
    youth.add_argument("--scope", choices=["any-court", "youth-court"], default="any-court", help="Workbook scope")
    youth.add_argument("--age-group", default="Total", help="Age group filter, or 'all' for every age group")
    youth.add_argument("--offence", help="Filter offence rows by text")
    youth.set_defaults(func=cmd_youth)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        args.func(args)
        return 0
    except CliError as exc:
        suffix = f" ({exc.source_url})" if exc.source_url else ""
        die(f"{exc}{suffix}", 1)
    except KeyboardInterrupt:
        die("interrupted", 130)


if __name__ == "__main__":
    raise SystemExit(main())
