"""Read PSC release tables using only ZIP/XML from the Python standard library."""
from __future__ import annotations

import io
import re
import zipfile
from xml.etree import ElementTree as ET

NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
REL = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
MAX_BYTES = 8 * 1024 * 1024


def workbook_rows(body):
    if len(body) > MAX_BYTES:
        raise ValueError('OIA workbook exceeds the download bound')
    try:
        with zipfile.ZipFile(io.BytesIO(body)) as archive:
            if len(archive.infolist()) > 200 or sum(x.file_size for x in archive.infolist()) > 32 * MAX_BYTES:
                raise ValueError('OIA workbook exceeds the expansion bound')
            strings = []
            if 'xl/sharedStrings.xml' in archive.namelist():
                strings = [''.join(item.itertext()) for item in ET.fromstring(archive.read('xl/sharedStrings.xml'))]
            relations = {item.attrib['Id']: item.attrib['Target'] for item in
                         ET.fromstring(archive.read('xl/_rels/workbook.xml.rels'))}
            for sheet in ET.fromstring(archive.read('xl/workbook.xml')).findall('s:sheets/s:sheet', NS):
                target = relations[sheet.attrib['{' + REL + '}id']]
                path = target.lstrip('/') if target.startswith('/') else 'xl/' + target
                if '..' in path.split('/'):
                    raise ValueError('OIA workbook has an unsafe worksheet path')
                grid = []
                for row in ET.fromstring(archive.read(path)).findall('s:sheetData/s:row', NS):
                    values = {}
                    for cell in row.findall('s:c', NS):
                        letters = re.match(r'[A-Z]+', cell.attrib.get('r', ''))
                        if not letters:
                            raise ValueError('OIA cell has no column reference')
                        column = 0
                        for letter in letters[0]:
                            column = column * 26 + ord(letter) - ord('A') + 1
                        if column > 64:
                            raise ValueError('OIA worksheet exceeds the column bound')
                        node = cell.find('s:v', NS)
                        value = node.text if node is not None else ''
                        if cell.attrib.get('t') == 's':
                            value = strings[int(value)]
                        elif cell.attrib.get('t') == 'inlineStr':
                            value = ''.join(cell.find('s:is', NS).itertext())
                        values[column - 1] = ' '.join((value or '').split())
                    grid.append([values.get(col, '') for col in range(max(values, default=-1) + 1)])
                yield sheet.attrib['name'], grid
    except (zipfile.BadZipFile, ET.ParseError, KeyError, IndexError, TypeError) as exc:
        raise ValueError(f'OIA workbook schema changed: {exc}') from exc


def metric_key(heading, kind):
    text = heading.lower()
    percent = kind.lower() == 'percent'
    if 'within' in text and ('timeframe' in text or 'time frame' in text):
        return 'Percent_OIAs_CompletedWithinTimeframe' if percent else 'OIAs_CompletedWithinTimeframe'
    if 'published' in text:
        return 'OIAs_Published'
    if 'complaints' in text:
        return 'Ombudsman_Complaints'
    if 'final' in text and ('opinions' in text or 'views' in text):
        return 'FinalOpinionsbyOmbudsman'
    if 'extension' in text:
        return 'Percent_OIA_extension' if percent else 'OIA_extension'
    if 'transferred' in text:
        return 'Percent_OIA_transfer' if percent else 'OIA_transfer'
    if 'refused' in text:
        return 'Percent_OIAs_refused' if percent else 'OIA_refused'
    if 'average' in text:
        return 'OIA_average'
    if 'median' in text:
        return 'OIA_median'
    if 'requests completed' in text:
        return 'OIA_RequestsHandled'
    return None


def parse_release(body, period):
    """Join time/publication and complaints tables by exact agency identity."""
    combined = {}
    for name, rows in workbook_rows(body):
        headers = next((i for i, row in enumerate(rows[:12])
                        if row and row[0].lower() == 'agency type'), None)
        if headers is None:
            continue
        kinds = next((i for i in range(headers + 1, min(headers + 5, len(rows)))
                      if 'Number' in rows[i] and 'Percent' in rows[i]), None)
        if kinds is None:
            # Other-statistics sheets contain no mandatory percentage field in
            # early releases, but still expose the Number type row.
            kinds = next((i for i in range(headers + 1, min(headers + 5, len(rows)))
                          if rows[i].count('Number') >= 2), None)
        if kinds is None:
            raise ValueError(f'OIA release {name} has no metric type header')
        fields = {col: metric_key(text, rows[kinds][col] if col < len(rows[kinds]) else '')
                  for col, text in enumerate(rows[headers]) if col >= 2 and text}
        if 'OIA_RequestsHandled' not in fields.values():
            raise ValueError(f'OIA release {name} has no requests-completed column')
        agency_type = ''
        for row in rows[kinds + 1:]:
            if row and (re.fullmatch(r'\d+\.', row[0]) or row[0].lower() in {'notes', 'technical notes'}):
                break
            if row and row[0] and len(row) > 2 and not row[1] and not row[2]:
                agency_type = row[0]
            if len(row) < 3 or not row[1] or not re.fullmatch(r'\d+(?:\.0+)?', row[2]):
                continue
            agency = re.sub(r'\s*\(\d+\)$', '', row[1]).strip()
            if 'total' in agency.lower():
                continue
            item = combined.setdefault(agency, {'Agency': agency, 'Agency_Type': agency_type,
                                               'SurveyPeriodEndDate': period})
            if row[0].isdigit():
                item.setdefault('_org_ids', set()).add(row[0])
            for col, field in fields.items():
                if field and col < len(row) and row[col]:
                    if field in item and item[field] != row[col]:
                        raise ValueError(f'OIA release has conflicting {field} values for {agency}')
                    item[field] = row[col]
    if not combined or not any('OIAs_CompletedWithinTimeframe' in r for r in combined.values()):
        raise ValueError('OIA release contained no complete agency timeliness tables')
    for item in combined.values():
        ids = item.pop('_org_ids', set())
        if len(ids) == 1:
            item['OrgID'] = next(iter(ids))
        elif ids:
            # The December 2025 release has a shifted ID column in one sheet.
            # Do not choose between conflicting IDs; recovery must use the exact
            # agency name and counts in the all-data CSV instead.
            item['_identity_warning'] = 'Conflicting release-table IDs; exact name/count matching required.'
    return list(combined.values())
