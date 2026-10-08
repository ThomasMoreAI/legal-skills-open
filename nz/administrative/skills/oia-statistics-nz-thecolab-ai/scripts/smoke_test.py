#!/usr/bin/env python3
"""Smoke tests for oia-statistics-nz.

Network-dependent commands return upstream_unavailable on blocked/outage states and
are treated as skip conditions.
"""
from __future__ import annotations

import json
import io
import zipfile
from xml.etree import ElementTree as ET
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "cli.py"


def run(args: list[str], timeout: int = 120) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(CLI), *args], text=True, capture_output=True, timeout=timeout)


def parse_json_output(proc: subprocess.CompletedProcess[str]) -> dict:
    payload = (proc.stdout or proc.stderr).strip()
    return json.loads(payload or "{}") if payload else {}


def is_upstream_skip(proc: subprocess.CompletedProcess[str]) -> tuple[bool, str]:
    if proc.returncode != 2:
        return False, ""
    try:
        data = parse_json_output(proc)
    except Exception:
        return False, ""
    if data.get("error") == "upstream_unavailable":
        return True, str(data.get("message", ""))
    return False, ""


def main() -> int:
    import importlib.util

    spec = importlib.util.spec_from_file_location("oia_statistics_cli", CLI)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    record = module.row_enriched(
        {
            "OrgID": "42",
            "Agency": "Synthetic Agency",
            "Agency_Type": "Department",
            "SurveyPeriodEndDate": "2025-12-31T00:00:00",
            "OIA_RequestsHandled": "200",
            "OIAs_CompletedWithinTimeframe": "180",
            "OIA_refused": "10",
        }
    )
    if record["org_id"] != 42 or record["timeliness_pct"] != 90.0 or record["refusals_pct"] != 5.0:
        print("[FAIL] fixture OIA CSV row normalisation", file=sys.stderr)
        return 1
    print("[PASS] fixture OIA CSV row normalisation")

    # Small synthetic OOXML workbook in the current published response shape.
    from oia_workbooks import parse_release
    tables = json.loads((ROOT / 'tests/fixtures/release-tables.json').read_text())
    ns = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'
    relns = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
    workbook = ET.Element('workbook', xmlns=ns)
    sheets = ET.SubElement(workbook, 'sheets')
    relations = ET.Element('Relationships', xmlns='http://schemas.openxmlformats.org/package/2006/relationships')
    body = io.BytesIO()
    with zipfile.ZipFile(body, 'w') as archive:
        for index, (name, rows) in enumerate(tables.items(), 1):
            ET.SubElement(sheets, 'sheet', name=name, sheetId=str(index), attrib={'{' + relns + '}id': f'rId{index}'})
            ET.SubElement(relations, 'Relationship', Id=f'rId{index}', Target=f'worksheets/sheet{index}.xml')
            sheet = ET.Element('worksheet', xmlns=ns)
            data = ET.SubElement(sheet, 'sheetData')
            for number, values in enumerate(rows, 1):
                row = ET.SubElement(data, 'row', r=str(number))
                for col, value in enumerate(values):
                    if value is None:
                        continue
                    cell = ET.SubElement(row, 'c', r=f'{chr(65 + col)}{number}')
                    if isinstance(value, str):
                        cell.set('t', 'inlineStr')
                        ET.SubElement(ET.SubElement(cell, 'is'), 't').text = value
                    else:
                        ET.SubElement(cell, 'v').text = str(value)
            archive.writestr(f'xl/worksheets/sheet{index}.xml', ET.tostring(sheet))
        archive.writestr('xl/workbook.xml', ET.tostring(workbook))
        archive.writestr('xl/_rels/workbook.xml.rels', ET.tostring(relations))
    workbook_body = body.getvalue()
    parsed = parse_release(workbook_body, '2026-06-30')
    assert len(parsed) == 3 and parsed[0]['OIA_extension'] == '4'
    assert parsed[0]['Ombudsman_Complaints'] == '3' and parsed[0]['OIA_refused'] == '10'
    assert 'OrgID' not in parsed[0] and parsed[0]['_identity_warning']
    assert parsed[2]['Agency'] == 'Unmatched Police' and 'OrgID' not in parsed[2]
    # The CSV row for the unmatched agency has a different name and different
    # counts, so it cannot be joined and must stay undated (no double count).
    unmatched_csv = dict(parsed[2], OrgID='77', Agency='New Zealand Police', OIA_RequestsHandled='499',
                         SurveyPeriodEndDate='00:00.0')
    raw = [dict(parsed[0], OrgID='42', SurveyPeriodEndDate='00:00.0'),
           dict(parsed[1], SurveyPeriodEndDate='00:00.0'),
           dict(parsed[1], SurveyPeriodEndDate='00:00.0'),
           unmatched_csv]
    repaired = module.recover_release_periods(raw, [('2026-06-30', 'https://www.publicservice.govt.nz/assets/synthetic.xlsx', '2026-10-08T00:00:00Z', parsed)])
    assert repaired[0]['SurveyPeriodEndDate'] == '2026-06-30'
    assert repaired[-1]['SurveyPeriodEndDate'] == '00:00.0'
    period_rows = module.agency_rows(module._rows_by_period(repaired)['2026-06-30'])
    assert len(period_rows) == 3
    summary = module.periods_summary(repaired)[0]
    assert summary['period_end'] == '2026-06-30'
    # Period totals equal the release workbook: 200 + 20 + 500, not 220.
    assert summary['requests_handled'] == 720 and summary['rows'] == 3 and summary['agency_count'] == 3
    assert module.row_enriched(repaired[0])['source_url'].endswith('synthetic.xlsx')
    kept = next(module.row_enriched(row) for row in period_rows if row['Agency'] == 'Unmatched Police')
    assert kept['org_id'] is None and kept['requests_handled'] == 500 and kept['complaints'] == 30
    assert kept['identity_warning'] == module.UNMATCHED_IDENTITY_WARNING
    assert not any(row.get('_identity_warning', '').startswith('The published sources reuse') for row in period_rows)
    print('[PASS] fixture unmatched no-OrgID release record is kept and period totals equal the workbook')

    # cached_release: fetch once, serve the validated cache, refetch when stale,
    # and fail closed on a non-XLSX body. No network: fetch_bytes is stubbed.
    import os
    import tempfile
    calls = []
    responses = [workbook_body]

    def fake_fetch(url, **kwargs):
        calls.append(url)
        return responses[-1], 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', url

    original_fetch, original_cache = module.nzfetch.fetch_bytes, module.CACHE_DIR
    url = 'https://www.publicservice.govt.nz/assets/synthetic.xlsx'
    try:
        with tempfile.TemporaryDirectory() as cache_dir:
            module.CACHE_DIR = Path(cache_dir)
            module.nzfetch.fetch_bytes = fake_fetch
            first, _stamp = module.cached_release(url, 5)
            second, _stamp = module.cached_release(url, 5)
            assert first == second == workbook_body and len(calls) == 1
            cached = next(Path(cache_dir).glob('*.xlsx'))
            os.utime(cached, (0, 0))
            module.cached_release(url, 5)
            assert len(calls) == 2
            os.utime(cached, (0, 0))
            responses.append(b'<html>not a workbook</html>')
            try:
                module.cached_release(url, 5)
            except ValueError:
                pass
            else:
                raise AssertionError('non-XLSX release download must fail closed')
            assert cached.read_bytes() == workbook_body
    finally:
        module.nzfetch.fetch_bytes, module.CACHE_DIR = original_fetch, original_cache
    print('[PASS] fixture cached_release reuses fresh cache, refetches stale entries and rejects non-XLSX bodies')
    assert module._norm_period('2026-99-99') == ''
    assert module._norm_period('00:00.0') == ''
    assert module.infer_period_from_text('OIA Statistics: 1 January to 30 June 2026(XLSX)') == '2026-06-30'
    try:
        parse_release(b'broken workbook', '2026-06-30')
    except ValueError:
        pass
    else:
        raise AssertionError('invalid workbook must fail closed')
    print('[PASS] fixture official release discovery, stdlib OOXML, exact date recovery, conflicting IDs and ambiguous matches')

    import argparse
    release = {'_source_url': 'https://www.publicservice.govt.nz/assets/synthetic.xlsx',
               '_retrieved_at': '2026-10-08T00:00:00Z'}
    original_load = module.load_rows
    try:
        # A blank on-time cell (NZ Police, Jul-Dec 2018) is unreported, not 0%.
        missing_on_time = [
            dict(release, OrgID='390', Agency='New Zealand Police', SurveyPeriodEndDate='2018-12-31',
                 OIA_RequestsHandled='21225', OIAs_Published='29'),
            dict(release, OrgID='10', Agency='Small Agency', SurveyPeriodEndDate='2018-12-31',
                 OIA_RequestsHandled='100', OIAs_CompletedWithinTimeframe='50'),
            dict(release, OrgID='11', Agency='Other Agency', SurveyPeriodEndDate='2018-12-31',
                 OIA_RequestsHandled='300', OIAs_CompletedWithinTimeframe='290'),
        ]
        module.load_rows = lambda timeout: (missing_on_time, 'fixture')
        police = module.row_enriched(missing_on_time[0])
        assert police['requests_completed_within_timeframe'] is None and police['timeliness_pct'] is None
        summary = module.periods_summary(missing_on_time)[0]
        assert summary['requests_handled'] == 21625 and summary['requests_completed_within_timeframe'] == 340
        assert summary['timeliness_pct'] == 85.0 and summary['on_time_coverage']['requests_handled'] == 400
        totals = module.command_totals(argparse.Namespace(timeout=5, period='2018-12-31'))
        coverage = totals['totals']['on_time_coverage']
        assert totals['totals']['requests_handled'] == 21625 and totals['totals']['timeliness_pct'] == 85.0
        assert coverage == {'agency_count': 2, 'requests_handled': 400, 'missing_agency_count': 1,
                            'missing_requests_handled': 21225, 'missing_agencies': ['New Zealand Police']}
        assert 'New Zealand Police' in totals['warnings'][0]
        worst = module.command_timeliness(argparse.Namespace(timeout=5, period='2018-12-31', sort='worst', limit=0))
        assert [r['agency'] for r in worst['records']] == ['Small Agency', 'Other Agency', 'New Zealand Police']
        assert worst['records'][-1]['timeliness_pct'] is None and worst['on_time_coverage'] == coverage
        best = module.command_timeliness(argparse.Namespace(timeout=5, period='2018-12-31', sort='best', limit=1))
        assert best['records'][0]['agency'] == 'Other Agency'
        print('[PASS] fixture missing on-time count stays null and is excluded from on-time percentages')

        # Release records without an OrgID merge into the matching OrgID history.
        def rec(org, agency, period, requests, preferred=''):
            return dict(release, OrgID=org, Agency=agency, Agency_Preffered_Name=preferred,
                        SurveyPeriodEndDate=period, OIA_RequestsHandled=str(requests),
                        OIAs_CompletedWithinTimeframe=str(requests))
        tpk = 'Te Puni K?kiri-Ministry of M?ori Development'
        history = [
            rec('377', 'Te Puni Kōkiri-Ministry of Māori Development', '2026-06-30', 69, tpk),
            rec('', 'Te Puni Kōkiri', '2025-12-31', 84),
            rec('377', 'Te Puni Kōkiri-Ministry of Māori Development', '2025-06-30', 91, tpk),
            rec('', 'Ministry of Maori Development', '2018-12-31', 30),
            rec('3029', 'Natural Hazards Commission – Toka Tū Ake', '2025-06-30', 8405),
            rec('3029', 'Earthquake Commission', '2021-12-31', 8454),
            rec('', 'Earthquake Commission', '2021-06-30', 9690),
            rec('', 'Earthquake Commission', '2020-12-31', 8467),
            rec('2370', 'Toka Tū Ake EQC', '2022-06-30', 7176),
            # Same normalised name as two OrgID agencies: never merged.
            rec('50', 'Shared Name Board', '2025-06-30', 5),
            rec('51', 'Shared Name Board', '2024-06-30', 5),
            rec('', 'Shared Name Board', '2023-06-30', 5),
        ]
        module.load_rows = lambda timeout: (history, 'fixture')

        def lookup(query):
            return module.command_agency(argparse.Namespace(timeout=5, agency_query=query, period=None, limit=0))
        tpk_result = lookup('Te Puni Kōkiri')
        assert tpk_result['agency']['org_id'] == 377
        assert [r['survey_period_end'] for r in tpk_result['records']] == ['2026-06-30', '2025-12-31', '2025-06-30', '2018-12-31']
        assert tpk_result['records'][1]['org_id'] is None and tpk_result['records'][1]['inferred_org_id'] == 377
        eqc = lookup('Earthquake Commission')
        assert eqc['agency']['org_id'] == 3029
        assert [r['survey_period_end'] for r in eqc['records']] == ['2025-06-30', '2021-12-31', '2021-06-30', '2020-12-31']
        assert len(lookup('377')['records']) == 4
        listed = {a['org_id']: a['period_count'] for a in module.list_agencies(history)}
        assert listed[377] == 4 and listed[3029] == 4 and None not in listed
        for query in ('Shared Name Board', 'Toka Tū Ake'):
            try:
                lookup(query)
            except ValueError as exc:
                assert 'ambiguous' in str(exc)
            else:
                raise AssertionError(f'{query} must stay ambiguous')
        # Period totals are unchanged by the name merge.
        assert module.periods_summary(history)[0]['requests_handled'] == 69
        print('[PASS] fixture null-OrgID release records merge into the matching agency history')
    finally:
        module.load_rows = original_load

    help_proc = run(["--help"], timeout=20)
    if help_proc.returncode != 0 or "list-agencies" not in (help_proc.stdout or ""):
        print("FAIL: --help should list available commands", file=sys.stderr)
        print(help_proc.stdout)
        print(help_proc.stderr, file=sys.stderr)
        return 1

    periods = run(["periods", "--limit", "1", "--json"])
    if periods.returncode == 2:
        skip, message = is_upstream_skip(periods)
        if skip:
            print(f"SKIP: upstream unavailable ({message})")
            return 0
        print(periods.stderr or periods.stdout, file=sys.stderr)
        return 1
    if periods.returncode != 0:
        print(periods.stderr or periods.stdout, file=sys.stderr)
        return 1

    periods_data = parse_json_output(periods)
    if periods_data.get("kind") != "oia-periods" or not isinstance(periods_data.get("periods"), list):
        print("FAIL: periods command did not return expected JSON shape", file=sys.stderr)
        print(periods.stdout, file=sys.stderr)
        return 1
    latest_period = periods_data.get("latest_period")
    if not latest_period or not periods_data['periods']:
        print('[FAIL] live periods must contain dated source records', file=sys.stderr)
        return 1
    print(f"[PASS] live periods returned {periods_data.get('count')} period(s)")

    agencies = run(["list-agencies", "--limit", "3", "--json"])
    if agencies.returncode == 2:
        skip, message = is_upstream_skip(agencies)
        if skip:
            print(f"SKIP: upstream unavailable ({message})")
            return 0
        print(agencies.stderr or agencies.stdout, file=sys.stderr)
        return 1
    if agencies.returncode != 0:
        print(agencies.stderr or agencies.stdout, file=sys.stderr)
        return 1
    agencies_data = parse_json_output(agencies)
    agency_rows = agencies_data.get("agencies") or []
    if agencies_data.get("kind") != "oia-list-agencies" or not agency_rows:
        print("FAIL: list-agencies command did not return expected agency rows", file=sys.stderr)
        print(agencies.stdout, file=sys.stderr)
        return 1

    org_id = agency_rows[0].get("org_id")
    if isinstance(org_id, int):
        agency = run(["agency", str(org_id), "--json"], timeout=180)
        if agency.returncode == 2:
            skip, message = is_upstream_skip(agency)
            if skip:
                print(f"SKIP: upstream unavailable ({message})")
                return 0
            print(agency.stderr or agency.stdout, file=sys.stderr)
            return 1
        if agency.returncode != 0:
            print(agency.stderr or agency.stdout, file=sys.stderr)
            return 1
        agency_data = parse_json_output(agency)
        if agency_data.get("kind") != "oia-agency" or not agency_data.get("records"):
            print("FAIL: agency command did not return expected records", file=sys.stderr)
            print(agency.stdout, file=sys.stderr)
            return 1
        print(f"[PASS] live agency lookup by OrgID {org_id} returned {len(agency_data['records'])} rows")

    totals = run(["totals", "--period", latest_period or "latest", "--json"], timeout=120)
    if totals.returncode == 2:
        skip, message = is_upstream_skip(totals)
        if skip:
            print(f"SKIP: upstream unavailable ({message})")
            return 0
        print(totals.stderr or totals.stdout, file=sys.stderr)
        return 1
    if totals.returncode != 0:
        print(totals.stderr or totals.stdout, file=sys.stderr)
        return 1
    totals_data = parse_json_output(totals)
    if totals_data.get("kind") != "oia-totals" or not isinstance(totals_data.get("totals"), dict):
        print("FAIL: totals command did not return expected shape", file=sys.stderr)
        print(totals.stdout, file=sys.stderr)
        return 1
    if totals_data['totals'].get('requests_handled', 0) <= 0:
        print("FAIL: totals command returned no handled requests", file=sys.stderr)
        return 1
    print(f"[PASS] live totals returned requests_handled={totals_data['totals'].get('requests_handled')}")

    complaints = run(["complaints", "--period", latest_period or "latest", "--sort", "complaints", "--limit", "5", "--json"], timeout=120)
    if complaints.returncode != 0:
        print(complaints.stderr or complaints.stdout, file=sys.stderr)
        return 1
    complaints_data = parse_json_output(complaints)
    records = complaints_data.get("records", [])
    # Release-only records may legitimately have org_id null (see identity_warning);
    # CSV-only rows still need an ID; aggregate rows are excluded by type.
    if any(r.get("agency_type") == "Agency Type Totals"
           or (r.get("org_id") in (0, None) and not r.get("source_url")) for r in records):
        print("FAIL: complaints includes aggregate rows", file=sys.stderr)
        return 1
    counts = [r.get("complaints", 0) for r in records]
    if counts != sorted(counts, reverse=True):
        print("FAIL: complaints sort is not descending", file=sys.stderr)
        return 1
    print("[PASS] live complaints excludes aggregate rows and sorts descending")

    return 0


if __name__ == "__main__":
    sys.exit(main())
