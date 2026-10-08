#!/usr/bin/env python3
"""
Phase 10.7 — Test for cross-reference builder logic.

Tests the citation regex extraction + law lookup logic without needing
to write to the actual DB. Verifies that the regex correctly extracts:
  - Thai digits (๑๑๘ → 118)
  - Law code prefixes (ป.อ., ป.พ.พ., พ.ร.บ.คุ้มครองแรงงาน, etc.)
  - Section references (มาตรา N, Section N, ม. N)
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from scripts.build_cross_references import (
    normalize_digits,
    SECTION_REF_RE,
    LAW_CODE_ALIASES,
)

def test_normalize_digits():
    print('[1] Thai digit normalization')
    assert normalize_digits('มาตรา ๑๑๘') == 'มาตรา 118'
    assert normalize_digits('๒๕๖๗') == '2567'
    assert normalize_digits('mixed 123 ๔๕๖') == 'mixed 123 456'
    assert normalize_digits('no digits') == 'no digits'
    print('    PASS')

def test_section_ref_extraction_basic():
    print('\n[2] Basic section reference extraction')
    text = normalize_digits('ตามมาตรา ๑๑๘ แห่งพระราชบัญญัติคุ้มครองแรงงาน')
    matches = list(SECTION_REF_RE.finditer(text))
    assert len(matches) >= 1, f'expected >=1 match, got {len(matches)}'
    m = matches[0]
    assert m.group('section_num') == '118', f"expected '118', got {m.group('section_num')!r}"
    print(f'    extracted: section_num={m.group("section_num")!r}')
    print('    PASS')

def test_section_ref_extraction_latin():
    print('\n[3] Latin section reference extraction')
    text = 'Section 57 of the Labor Protection Act'
    matches = list(SECTION_REF_RE.finditer(text))
    assert len(matches) >= 1
    m = matches[0]
    assert m.group('section_num') == '57'
    print(f'    extracted: section_num={m.group("section_num")!r}')
    print('    PASS')

def test_section_ref_extraction_with_law_code():
    print('\n[4] Section ref with law code prefix')
    text = normalize_digits('ป.พ.พ. มาตรา ๕๘๒')
    matches = list(SECTION_REF_RE.finditer(text))
    assert len(matches) >= 1
    m = matches[0]
    assert m.group('law_code') == 'ป.พ.พ.', f"expected 'ป.พ.พ.', got {m.group('law_code')!r}"
    assert m.group('section_num') == '582'
    print(f'    extracted: law_code={m.group("law_code")!r}, section_num={m.group("section_num")!r}')
    print('    PASS')

def test_section_ref_extraction_short_form():
    print('\n[5] Short form (ม. N)')
    text = normalize_digits('ม. ๕๗')
    matches = list(SECTION_REF_RE.finditer(text))
    assert len(matches) >= 1
    m = matches[0]
    assert m.group('section_num') == '57'
    print(f'    extracted: section_num={m.group("section_num")!r}')
    print('    PASS')

def test_law_code_aliases_complete():
    print('\n[6] Law code aliases coverage')
    expected_aliases = ['ป.อ.', 'ป.พ.พ.', 'ป.วิ.อ.', 'ป.วิ.แพ่ง',
                        'พ.ร.บ.คุ้มครองแรงงาน', 'พ.ร.บ.แรงงาน',
                        'พ.ร.บ.ประกันสังคม', 'พ.ร.บ.เงินทดแทน']
    for alias in expected_aliases:
        assert alias in LAW_CODE_ALIASES, f'missing alias: {alias}'
    print(f'    all {len(expected_aliases)} aliases present')
    print('    PASS')

def test_multiple_refs_in_text():
    print('\n[7] Multiple references in single text')
    text = normalize_digits(
        'คดีนี้อ้าง มาตรา ๑๑๘ และ มาตรา ๑๑๙ ของ พ.ร.บ.คุ้มครองแรงงาน '
        'รวมถึง ป.พ.พ. มาตรา ๕๘๒'
    )
    matches = list(SECTION_REF_RE.finditer(text))
    section_nums = [m.group('section_num') for m in matches]
    assert '118' in section_nums, f'expected 118 in {section_nums}'
    assert '119' in section_nums, f'expected 119 in {section_nums}'
    assert '582' in section_nums, f'expected 582 in {section_nums}'
    print(f'    extracted section_nums: {section_nums}')
    print('    PASS')

def test_no_false_positive_on_plain_text():
    print('\n[8] No false positives on plain text')
    text = 'ประกาศกระทรวงแรงงาน เรื่อง ค่าจ้างขั้นต่ำ พ.ศ. 2567'
    matches = list(SECTION_REF_RE.finditer(text))
    # Should not match — no "มาตรา" or "Section" prefix
    assert len(matches) == 0, f'expected 0 matches, got {len(matches)}: {[m.group(0) for m in matches]}'
    print('    PASS')

def main():
    print('--- Phase 10.7 cross-reference builder tests ---\n')
    test_normalize_digits()
    test_section_ref_extraction_basic()
    test_section_ref_extraction_latin()
    test_section_ref_extraction_with_law_code()
    test_section_ref_extraction_short_form()
    test_law_code_aliases_complete()
    test_multiple_refs_in_text()
    test_no_false_positive_on_plain_text()
    print('\n--- All tests passed ---')
    return 0

if __name__ == '__main__':
    sys.exit(main())
