#!/usr/bin/env python3
"""
Phase 10.3 test — verify RSS monitor parses a fake feed correctly.
This is a unit test for the parsing/classification logic.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from scripts.monitor_law_updates import (
    parse_rss, is_labor_related, classify_update_type,
    extract_reference_number, normalize_pub_date,
)

FAKE_RSS = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Royal Gazette RSS</title>
    <link>https://ratchakitcha.soc.go.th</link>
    <description>Test feed</description>
    <item>
      <title>ประกาศกระทรวงแรงงาน เรื่อง ค่าจ้างขั้นต่ำ (ฉบับที่ ๑๐) พ.ศ. ๒๕๖๗</title>
      <link>https://ratchakitcha.soc.go.th/DATA/PDF/2567/0/57/1.PDF</link>
      <pubDate>Mon, 15 Jul 2024 00:00:00 GMT</pubDate>
      <description>ปรับอัตราค่าจ้างขั้นต่ำทั่วประเทศเป็นวันละ 400 บาท สำหรับลูกจ้างและนายจ้างในทุกจังหวัด</description>
      <guid>https://ratchakitcha.soc.go.th/DATA/PDF/2567/0/57/1.PDF</guid>
    </item>
    <item>
      <title>พระราชบัญญัติแก้ไขเพิ่มเติมประมวลกฎหมายอาญา (ฉบับที่ ๒)</title>
      <link>https://ratchakitcha.soc.go.th/DATA/PDF/2566/0/30/1.PDF</link>
      <pubDate>Wed, 01 Nov 2023 00:00:00 GMT</pubDate>
      <description>แก้ไขมาตรา ๒๘๙ ว่าด้วยความผิดเกี่ยวกับชีวิต</description>
      <guid>test-2</guid>
    </item>
    <item>
      <title>พระราชบัญญัติยกเลิกกฎหมายฉบับเก่า</title>
      <link>https://ratchakitcha.soc.go.th/DATA/PDF/2565/0/10/1.PDF</link>
      <pubDate>Fri, 10 Mar 2022 00:00:00 GMT</pubDate>
      <description>ยกเลิก พ.ร.บ.เก่าที่ไม่สอดคล้องกับยุคสมัย</description>
      <guid>test-3</guid>
    </item>
  </channel>
</rss>
""".encode('utf-8')

def main():
    print("--- Phase 10.3 unit test ---\n")
    items = parse_rss(FAKE_RSS)
    print(f"[1] Parsed {len(items)} items (expected 3)")
    assert len(items) == 3, f"expected 3, got {len(items)}"
    print("    PASS")

    print(f"\n[2] Labor-related filtering:")
    labor_count = sum(1 for it in items if is_labor_related(it))
    print(f"    labor-related items: {labor_count} (expected 1 — only the wage one)")
    assert labor_count == 1, f"expected 1 labor item, got {labor_count}"
    print("    PASS")

    print(f"\n[3] Classification:")
    for it in items:
        ut, sev = classify_update_type(it['title'])
        print(f"    [{sev:>8}] [{ut:>14}] {it['title'][:60]}")
    # Item 1: ประกาศกระทรวงแรงงาน → new_regulation / warning
    ut1, sev1 = classify_update_type(items[0]['title'])
    assert ut1 == 'new_regulation', f"item 1: expected new_regulation, got {ut1}"
    assert sev1 == 'warning', f"item 1: expected warning, got {sev1}"
    # Item 2: แก้ไขเพิ่มเติม → amendment / warning
    ut2, sev2 = classify_update_type(items[1]['title'])
    assert ut2 == 'amendment', f"item 2: expected amendment, got {ut2}"
    # Item 3: ยกเลิก → repeal / critical
    ut3, sev3 = classify_update_type(items[2]['title'])
    assert ut3 == 'repeal', f"item 3: expected repeal, got {ut3}"
    assert sev3 == 'critical', f"item 3: expected critical, got {sev3}"
    print("    PASS")

    print(f"\n[4] Reference number extraction:")
    ref1 = extract_reference_number(items[0]['title'], items[0]['description'])
    print(f"    item 1 ref: {ref1!r}")
    assert ref1 is not None, "expected a reference number"
    print("    PASS")

    print(f"\n[5] Date normalization:")
    d = normalize_pub_date('Mon, 15 Jul 2024 00:00:00 GMT')
    print(f"    normalized: {d!r}")
    assert '2024-07-15' in d, f"expected 2024-07-15 in date, got {d}"
    print("    PASS")

    print("\n--- All tests passed ---")
    return 0

if __name__ == "__main__":
    sys.exit(main())
