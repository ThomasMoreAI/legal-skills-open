#!/usr/bin/env python3
"""
check_standard.py - rules-based Israeli standards import checker.

Takes a product category keyword and returns:
  - applicable Israeli Standard (SI) numbers
  - whether the standard is declared mandatory (takan rishmi)
  - recommended approval route
  - required lab tests / documents
  - typical timeline band
  - fast-track eligibility

Facts baseline (as of August 2026): the EU-recognition route runs under
Amendment 19 to the Standards Law, phased from 2025 through 2028. The
parallel US-standards track (Amendment 21) was passed by the Knesset on
16 July 2026 and starts six months after publication, i.e. at the
beginning of 2027, so it is NOT yet usable; it also requires the product
to be manufactured in the United States (or in Israel) and excludes
food, motor vehicles, cosmetics and fire-safety products. Customs filing goes through
the Sha'ar Olami electronic clearance system. Import groups are
risk-tiered: Group 1 = highest risk (model approval + shipment
inspection), Group 2 = medium (model certificate + importer declaration),
Group 3 = low (importer declaration only), Group 4 = industrial use only
(no import conformity assessment). The rules below are hardcoded; verify
the live mandatory-standards list before filing.

Usage:
    python scripts/check_standard.py --list
    python scripts/check_standard.py --category toy
    python scripts/check_standard.py --category hair-dryer
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass, field


@dataclass
class StandardRule:
    category: str
    aliases: list[str]
    si_numbers: list[str]
    mandatory: bool
    import_group: str
    approval_route: str
    required_tests: list[str]
    timeline_band: str
    fast_track: str
    notes: str
    authority: str


RULES: list[StandardRule] = [
    StandardRule(
        category="toy",
        aliases=["toys", "children-toy", "ride-on", "plush", "doll", "finger-paint"],
        si_numbers=["SI 562 part 1", "SI 562 part 2", "SI 562 part 3", "SI 562 part 7"],
        mandatory=True,
        import_group="Group 1 for products intended for infants and young children; confirm the specific SI in the Commissioner search engine",
        approval_route="Type approval by SII, or the EU route via the Toy Safety Directive, adopted from 1 February 2025. For toys for children UNDER 3 the directive does not apply unless the trader holds a manufacturer declaration and a technical file as defined in section 10e, or a conformity approval under section 12.",
        required_tests=[
            "EN 71-1 mechanical/physical",
            "EN 71-2 flammability",
            "EN 71-3 chemical migration",
            "Hebrew user manual / labelling",
        ],
        timeline_band="Type approval: weeks. EU route: days after notification if dossier is complete.",
        fast_track="Toy Safety Directive 2009/48/EC adopted from 1 February 2025, subject to the under-3 condition above.",
        notes="SI 562 part 1 was revised November 2022 with transition until 16 April 2023. Battery-powered toys may also trigger SI 900 electrical safety.",
        authority="Standards Institution of Israel (SII), https://www.sii.org.il",
    ),
    StandardRule(
        category="household-electrical",
        aliases=["hair-dryer", "kettle", "dishwasher", "microwave", "blender", "toaster", "appliance"],
        si_numbers=["SI 900 (family)", "e.g., SI 900 part 2.5 dishwashers", "SI 900 part 2.29 battery chargers", "SI 32 (plug and socket-outlet, Type H)"],
        mandatory=True,
        import_group="Usually Group 3 (importer declaration). Confirm per SI in the Commissioner search engine",
        approval_route="Type approval by SII plus shipment approval, or Green/Gold/Diamond easement plan once eligible",
        required_tests=[
            "IEC 60335-1 safety",
            "Relevant IEC 60335-2-xx particular requirements",
            "EMC per SII EMC rules",
            "SI 32 plug compliance (Israeli Type H)",
            "Hebrew user manual",
        ],
        timeline_band="Type approval typically several weeks; subsequent shipments days with a valid product file.",
        fast_track="Available in principle: the Low Voltage Directive 2014/35/EU and the EMC Directive 2014/30/EU are adopted into the Fifth Appendix. The statute separately requires an electrical device to match the electricity network in use in Israel, so check SI 32 (Type H plug) first. Low-voltage electrical cables are deferred to 1 January 2027.",
        notes="Declaration-based entry (July 2024) possible with ILAC-accredited report but random surveillance applies.",
        authority="Standards Institution of Israel (SII), https://www.sii.org.il",
    ),
    StandardRule(
        category="external-power-supply",
        aliases=["charger", "power-supply", "adapter", "battery-charger", "psu"],
        si_numbers=["SI 900 part 2.29 (battery chargers)", "SI 32 if a mains plug is fitted"],
        mandatory=True,
        import_group="Group 2 (model certificate plus importer declaration) above the output threshold",
        approval_route="Group 2 treatment: a model certificate plus an importer declaration that the shipment conforms. Confirm the output threshold and the group for the specific model in the Commissioner's search engine before assuming Group 2 rather than Group 3.",
        required_tests=[
            "IEC 60335-1 / IEC 62368-1 safety per the applicable SI part",
            "EMC report",
            "SI 32 plug compliance (Israeli Type H)",
            "Hebrew user manual",
        ],
        timeline_band="Model certificate typically weeks; subsequent shipments clear on the declaration.",
        fast_track="The Low Voltage and EMC Directives are adopted into the Fifth Appendix, so the EU route is open in principle. The unit must still match the Israeli mains.",
        notes="Do not confuse the charger with the appliance it powers; they can sit in different import groups.",
        authority="Standards Institution of Israel (SII), https://www.sii.org.il",
    ),
    StandardRule(
        category="plug-socket",
        aliases=["plug", "socket", "socket-outlet", "extension-cord", "power-strip", "splitter"],
        si_numbers=["SI 32 part 1.1 (plugs and socket-outlets up to 16 A)", "SI 32 other parts per product type"],
        mandatory=True,
        import_group="Confirm per SI in the Commissioner search engine",
        approval_route="SII filing against SI 32. Israel uses the Type H plug and SI 32 is official on all its parts, so a European or Chinese plug fails regardless of the rest of the dossier.",
        required_tests=[
            "SI 32 part 1.1 requirements",
            "Hebrew marking",
        ],
        timeline_band="Weeks, depending on SII queue.",
        fast_track="Check the Fifth Appendix; the plug interface itself is an Israeli national requirement, since the statute requires an electrical device to match the electricity network in use in Israel.",
        notes="This is the most common single reason a container of mains-powered goods from Asia is rejected.",
        authority="Standards Institution of Israel (SII), https://www.sii.org.il",
    ),
    StandardRule(
        category="food-contact-plastic",
        aliases=["plastic-container", "food-packaging", "baby-bottle", "food-contact"],
        si_numbers=["SI 5113"],
        mandatory=True,
        import_group="Group 1 for products intended for infants (bottles, feeding accessories); otherwise confirm per SI",
        approval_route="SII filing, accepts US FDA or EU Directive dossier as fallback",
        required_tests=[
            "Migration testing per SI 5113",
            "FDA 21 CFR compliance documentation (if applicable)",
            "EU Regulation 10/2011 compliance (if applicable)",
        ],
        timeline_band="Varies with dossier completeness; usually weeks.",
        fast_track="Food-contact plastics under Regulation 10/2011 commence 1 March 2025, and FCM Regulation 1935/2004 likewise, both subject to holding a manufacturer or recognised-state supplier declaration.",
        notes="Use FDA 21 CFR where available; otherwise EU Directive; otherwise Israeli Ministry of Health rules.",
        authority="Standards Institution of Israel (SII), https://www.sii.org.il",
    ),
    StandardRule(
        category="cosmetic",
        aliases=["cosmetics", "skincare", "moisturiser", "shampoo", "cream", "makeup"],
        si_numbers=["Pharmacists' Regulations (Cosmetics) 5783-2023"],
        mandatory=True,
        import_group="Not an SII import group; regulated by the Ministry of Health",
        approval_route="Notification to the Israeli Ministry of Health (MoH) confirming EU compliance; no SII testing required if dossier is complete",
        required_tests=[
            "EU CPNP file",
            "EU safety assessment",
            "Manufacturing facility documentation",
        ],
        timeline_band="Immediate upon valid notification; registration fee cancelled after reform.",
        fast_track="Notification model replaces the old SII + MoH registration regime. Note the Standards Law EU route for cosmetics (Regulation 1223/2009) commences only three years from Amendment 19's commencement, so it is not the operative path today; the MoH notification is.",
        notes="Regulated by the Ministry of Health, not SII. Old SII testing + registration pathway is superseded.",
        authority="Israeli Ministry of Health, https://www.gov.il/en/service/application-for-cosmetic-import-permits",
    ),
    StandardRule(
        category="motor-vehicle",
        aliases=["car", "passenger-car", "truck", "motorcycle", "vehicle"],
        si_numbers=["Israeli Mandatory Requirements (IMR 2025)"],
        mandatory=True,
        import_group="Outside the import-group scheme; Ministry of Transport homologation",
        approval_route="Type approval via a licensed importer under the Ministry of Transport and Road Safety",
        required_tests=[
            "EU 2018/858 WVTA homologation (accepted)",
            "US or Canadian homologation (accepted as technical prerequisite)",
            "Notarised Israeli Registration Requirements",
        ],
        timeline_band="Homologation lead time typically months for a new model; personal imports follow a separate procedure.",
        fast_track="NOT in the January 2025 EU-regulation catalogue. IMR already recognises EU 2018/858.",
        notes="Personal imports have their own procedure at gov.il Ministry of Transport.",
        authority="Ministry of Transport and Road Safety, https://www.gov.il/en/departments/units/vehicle_division_maintenance_services",
    ),
    StandardRule(
        category="radio-wireless",
        aliases=["drone", "router", "bluetooth", "wifi", "iot", "radio"],
        si_numbers=["Wireless Telegraph (Compliance Certificates) Regulations 5781-2021, reg. 2(a) and reg. 5a"],
        mandatory=True,
        import_group="Ministry of Communications certificate plus the SII group applicable to the electrical portion",
        approval_route="Ministry of Communications compliance certificate (ishur hat'ama) under reg. 2(a) is REQUIRED for import; reg. 5a (7 July 2022) only lets an EU-conformity document replace the standard document set. SII filing for electrical safety and EMC.",
        required_tests=[
            "EU RED (2014/53/EU) test suite",
            "EMC report",
            "Electrical safety (if mains powered)",
        ],
        timeline_band="Days to weeks depending on MoC workload.",
        fast_track="Since 7 July 2022 an EU-conforming device may attach an EU conformity document instead of the full document set. This is a documentation easement, not an exemption from the certificate.",
        notes="Mains-powered radio devices still trigger SI 900 evaluation, and a mains plug triggers SI 32.",
        authority="Ministry of Communications and SII",
    ),
    StandardRule(
        category="food",
        aliases=["packaged-food", "grocery", "beverage", "dairy", "infant-formula"],
        si_numbers=["Public Health (Food) regulations; 2016 parallel-import framework (Model A/B)"],
        mandatory=True,
        import_group="Not an SII import group; Ministry of Health framework",
        approval_route="Ministry of Health parallel-import / declaration path; SII is not the regulator",
        required_tests=[
            "Hebrew labelling",
            "Ministry of Health notification / declaration",
            "Certificate of origin and manufacturer documentation",
        ],
        timeline_band="Varies by sub-category (fresh, processed, infant formula, etc.).",
        fast_track="Food is EXCLUDED from the January 2025 EU-regulation catalogue. Use the Ministry of Health framework instead.",
        notes="2016 reform enabled parallel imports; check Kol Zchut and Ministry of Health guidance.",
        authority="Israeli Ministry of Health",
    ),
    StandardRule(
        category="lighting",
        aliases=["led", "led-lamp", "lamp", "luminaire", "light-fitting", "bulb"],
        si_numbers=["Look the specific luminaire or lamp type up in the Commissioner's search engine; the family has many parts", "SI 32 if a mains plug is fitted"],
        mandatory=True,
        import_group="Confirm per SI in the Commissioner search engine",
        approval_route="Check the applicable SI part via the Commissioner's search engine, then either the EU route (the Low Voltage and EMC Directives are adopted) or type approval by SII / an easement plan if the dossier is thin.",
        required_tests=[
            "Electrical safety per the applicable SI part",
            "EMC report",
            "SI 32 plug compliance if a plug is fitted",
            "Hebrew labelling",
        ],
        timeline_band="Type approval typically several weeks.",
        fast_track="Available in principle via the adopted Low Voltage and EMC Directives; the unit must still match the Israeli mains, so verify SI 32 if a plug is fitted.",
        notes="Verify the exact SI part and its current revision before filing; the lighting family has many parts and they are revised often.",
        authority="Standards Institution of Israel (SII), https://www.sii.org.il",
    ),
    StandardRule(
        category="building-material",
        aliases=["cement", "rebar", "concrete", "tile", "insulation", "construction-material"],
        si_numbers=["Category-specific SI numbers; look the product up in the Commissioner's search engine"],
        mandatory=True,
        import_group="Frequently Group 1 (model approval plus shipment inspection)",
        approval_route="Many building materials sit in import Group 1 (model approval plus shipment inspection). The Construction Products Regulation 305/2011 is in the Fifth Appendix but commences two years from Amendment 19's commencement, so the EU route is NOT yet open for construction products; check the entry's date before relying on it.",
        required_tests=[
            "Tests specified by the applicable SI",
            "Manufacturer test report from an accredited lab",
            "Shipment sampling where Group 1 applies",
        ],
        timeline_band="Group 1 filings are the slowest; plan sampling before the container sails.",
        fast_track="Not yet: CPR 305/2011 commences two years from Amendment 19's commencement. Some building materials are also carved out of the international-standard route by the Third Appendix.",
        notes="Do not assume a single SI covers the product; building materials are heavily sub-divided. SII building-materials centre: 03-6465225.",
        authority="Standards Institution of Israel (SII), https://www.sii.org.il",
    ),
    StandardRule(
        category="ppe",
        aliases=["personal-protective-equipment", "helmet", "safety-goggles", "respirator", "gloves"],
        si_numbers=["Applicable SI standards aligned with EU PPE Regulation (EU) 2016/425"],
        mandatory=True,
        import_group="Confirm per SI; Category II and III PPE carries the heavier assessment",
        approval_route="EU-recognition route via PPE Regulation from 1 January 2025, or type approval fallback",
        required_tests=[
            "EU-notified body test report (Category II and III)",
            "EU Declaration of Conformity",
            "Instruction leaflet including Hebrew",
        ],
        timeline_band="EU route: days after filing. Type approval fallback: weeks.",
        fast_track="PPE is in the first wave of the January 2025 EU-recognition catalogue.",
        notes="PPE was named explicitly in the initial catalogue.",
        authority="SII and Ministry of Economy Commissioner of Standardization",
    ),
    StandardRule(
        category="chemical",
        aliases=["chemicals", "industrial-chemical", "cleaning-product"],
        si_numbers=["Israeli chemical-safety standards aligned with REACH"],
        mandatory=True,
        import_group="Confirm per SI and per substance",
        approval_route="EU-recognition route via REACH from 1 January 2025; specific SI standards apply for consumer products",
        required_tests=[
            "Evidence of compliance with the REACH restrictions adopted into Israeli law (note: REACH REGISTRATION is an obligation of EU manufacturers and importers; an Israeli importer of a non-EU product cannot hold one)",
            "Safety Data Sheet in Hebrew",
        ],
        timeline_band="Depends on category and volume.",
        fast_track="Chemical safety (REACH) is in the first wave of the 2025 EU-recognition catalogue.",
        notes="Hazardous substances may need a Ministry of Environmental Protection permit.",
        authority="SII and Ministry of Environmental Protection",
    ),
]


def find_rule(query: str) -> StandardRule | None:
    q = query.strip().lower().replace("_", "-")
    for rule in RULES:
        if q == rule.category or q in rule.aliases:
            return rule
    for rule in RULES:
        if q in rule.category or any(q in alias for alias in rule.aliases):
            return rule
    return None


def format_rule(rule: StandardRule) -> str:
    out = []
    out.append(f"Category: {rule.category}")
    out.append(f"Applicable SI numbers: {', '.join(rule.si_numbers)}")
    out.append(f"Mandatory (takan rishmi): {'yes' if rule.mandatory else 'no'}")
    out.append(f"Import group: {rule.import_group}")
    out.append(f"Recommended approval route: {rule.approval_route}")
    out.append("Required tests / documents:")
    for item in rule.required_tests:
        out.append(f"  - {item}")
    out.append(f"Typical timeline: {rule.timeline_band}")
    out.append(f"Fast-track: {rule.fast_track}")
    out.append(f"Authority: {rule.authority}")
    out.append(f"Notes: {rule.notes}")
    out.append("")
    out.append("Disclaimer: regulatory guidance only, not legal advice. Verify the current mandatory-standards list on https://www.sii.org.il before filing.")
    return "\n".join(out)


def list_categories() -> str:
    lines = ["Supported categories:"]
    for rule in RULES:
        alias_str = ", ".join(rule.aliases[:4])
        lines.append(f"  - {rule.category} (aliases: {alias_str})")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--category", help="Product category keyword (e.g., toy, hair-dryer, cosmetic)")
    parser.add_argument("--list", action="store_true", help="List supported categories")
    parser.add_argument("--json", action="store_true", help="Output result as JSON")
    args = parser.parse_args(argv)

    if args.list:
        print(list_categories())
        return 0

    if not args.category:
        parser.print_help()
        return 1

    rule = find_rule(args.category)
    if rule is None:
        print(f"No rule for category '{args.category}'. Run with --list to see supported categories.", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(asdict(rule), indent=2, ensure_ascii=False))
    else:
        print(format_rule(rule))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
