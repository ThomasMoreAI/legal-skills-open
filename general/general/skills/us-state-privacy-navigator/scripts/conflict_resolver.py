#!/usr/bin/env python3
"""
conflict_resolver.py — Synthesize the binding constraint across applicable
state privacy laws.

Most multi-state privacy work product produces parallel state analyses without
synthesizing them. The hardest practical question is: given a controller subject
to N states, what is the *compliance ceiling* — the strictest applicable rule
for each duty that the controller must design to in order to be compliant
everywhere it operates?

For each compliance dimension below, the script returns:
  - The binding rule (the strictest one that controls if the controller wants
    a single uniform implementation).
  - The controlling state for that dimension.
  - Other applicable states' positions for context.
  - Whether a true *conflict* exists (rare — most "differences" are gradients
    where the strictest rule satisfies the others).
  - Implementation notes flagging operational tradeoffs.

Usage:
    python conflict_resolver.py --states CA,VA,CO,CT,TX
    python conflict_resolver.py --states CA,MD,CO --dimensions sensitive_data,minor_treatment
    python conflict_resolver.py --states-from applicability_output.json

Part of the us-state-privacy-navigator skill.
"""

import argparse
import json
import sys
from dataclasses import dataclass, asdict, field
from typing import Any


# ---------------------------------------------------------------------------
# Compliance dimensions and per-state positions
# ---------------------------------------------------------------------------
#
# Each "dimension" is an axis on which states have different rules. For each,
# we encode each state's position and a strictness ranking. The strictest
# position is the controlling one for a uniform multi-state implementation.
#
# Strictness scale: integers, higher = stricter. Where a state has no rule on
# the dimension, position is None and that state does not contribute to the
# ceiling.

ALL_STATES = ["CA", "VA", "CO", "CT", "UT", "TX", "OR", "MT", "FL", "IA",
              "DE", "NJ", "NH", "NE", "MN", "MD", "TN", "IN", "KY", "RI"]


DIMENSIONS: dict[str, dict] = {

    # --------------------------------------------------------------------
    # NOTICE & TRANSPARENCY
    # --------------------------------------------------------------------

    "notice_at_collection_required": {
        "description": "Whether a separate notice-at-collection (distinct from a privacy policy) is required at the point of data collection.",
        "category": "notice",
        "positions": {
            "CA": {"required": True, "strictness": 5,
                   "rule": "Separate notice-at-collection required at or before point of collection. CCPA Regs § 7012.",
                   "citation": "11 CCR § 7012"},
            **{s: {"required": False, "strictness": 1,
                   "rule": "Privacy notice is sufficient; no separate notice-at-collection.",
                   "citation": ""} for s in ALL_STATES if s != "CA"}
        },
        "implementation": "California is the only state that imposes a separate notice-at-collection. A privacy notice that satisfies CA's notice-at-collection content (categories, purposes, retention, sale/share, sensitive PI, third parties) and is presented at or before collection points satisfies all other states' notice content requirements.",
    },

    "privacy_notice_retention_disclosure": {
        "description": "Whether retention period or criteria must be disclosed in the privacy notice.",
        "category": "notice",
        "positions": {
            "CA": {"required": True, "strictness": 5, "rule": "Specific retention period or specific criteria required (CPRA amendment).", "citation": "Cal. Civ. Code § 1798.100(a)(3)"},
            "MD": {"required": True, "strictness": 5, "rule": "Retention period required and must be reasonably necessary and proportionate.", "citation": "Md. Code Com. Law § 14-4607"},
            "MN": {"required": True, "strictness": 4, "rule": "Specific retention period or criteria.", "citation": "Minn. Stat. § 325O.03"},
            "OR": {"required": True, "strictness": 4, "rule": "Specific retention period or criteria.", "citation": "Or. Rev. Stat. § 646A.578"},
            "TX": {"required": True, "strictness": 3, "rule": "Notice must address retention.", "citation": "Tex. Bus. & Com. Code § 541.102"},
            "DE": {"required": True, "strictness": 3, "rule": "Notice must address retention.", "citation": "Del. Code tit. 6 § 12D-105"},
            "NJ": {"required": True, "strictness": 3, "rule": "Notice must address retention.", "citation": "N.J. Stat. § 56:8-166.10"},
        },
        "implementation": "California's specific-period-or-criteria standard is the strictest. Drafting retention disclosures with specific periods (or specific criteria) per data category satisfies all states with retention disclosure requirements. Avoid 'as long as necessary' boilerplate.",
    },

    "specific_third_parties_disclosure": {
        "description": "Whether the privacy notice / right-to-know response must list specific third parties (vs. categories of third parties).",
        "category": "notice",
        "positions": {
            "OR": {"required": True, "strictness": 5, "rule": "Specific third parties on consumer request.", "citation": "Or. Rev. Stat. § 646A.578(1)(d)"},
            "MN": {"required": True, "strictness": 5, "rule": "Specific third parties on consumer request.", "citation": "Minn. Stat. § 325O.05"},
            "DE": {"required": True, "strictness": 5, "rule": "Specific third parties on consumer request.", "citation": "Del. Code tit. 6 § 12D-104"},
            "NJ": {"required": True, "strictness": 5, "rule": "Specific third parties on consumer request.", "citation": "N.J. Stat. § 56:8-166.7"},
            **{s: {"required": False, "strictness": 1, "rule": "Categories of third parties only.", "citation": ""} for s in ALL_STATES if s not in ("OR", "MN", "DE", "NJ")}
        },
        "implementation": "OR/MN/DE/NJ require disclosure of *specific* third parties (vendor names) on consumer request. This is operationally challenging — most controllers list categories. To satisfy these states, build the right-to-know workflow to maintain a current vendor list keyed to the consumer's data flows. Categories-only disclosure satisfies the other 16 states.",
    },

    # --------------------------------------------------------------------
    # SENSITIVE DATA
    # --------------------------------------------------------------------

    "sensitive_data_processing_standard": {
        "description": "Standard for processing sensitive data.",
        "category": "sensitive_data",
        "positions": {
            "MD": {"strictness": 6, "rule": "Express consent required AND data must be reasonably necessary and proportionate to specific product/service. No 'legitimate interest' alternative.", "citation": "Md. Code Com. Law § 14-4607(b)"},
            "VA": {"strictness": 5, "rule": "Opt-in consent required.", "citation": "Va. Code § 59.1-578(A)(5)"},
            "CO": {"strictness": 5, "rule": "Opt-in consent required.", "citation": "Colo. Rev. Stat. § 6-1-1308(7)"},
            "CT": {"strictness": 5, "rule": "Opt-in consent required.", "citation": "Conn. Gen. Stat. § 42-520(a)(4)"},
            "TX": {"strictness": 5, "rule": "Opt-in consent required.", "citation": "Tex. Bus. & Com. Code § 541.101(b)(4)"},
            "OR": {"strictness": 5, "rule": "Opt-in consent required.", "citation": "Or. Rev. Stat. § 646A.578(2)(a)"},
            "MT": {"strictness": 5, "rule": "Opt-in consent required.", "citation": "Mont. Code § 30-14-2811(2)(d)"},
            "DE": {"strictness": 5, "rule": "Opt-in consent required.", "citation": "Del. Code tit. 6 § 12D-104(d)(4)"},
            "NJ": {"strictness": 5, "rule": "Opt-in consent required.", "citation": "N.J. Stat. § 56:8-166.7"},
            "NH": {"strictness": 5, "rule": "Opt-in consent required.", "citation": "N.H. Rev. Stat. § 507-H:6"},
            "NE": {"strictness": 5, "rule": "Opt-in consent required.", "citation": "Neb. Rev. Stat. § 87-1107"},
            "MN": {"strictness": 5, "rule": "Opt-in consent required.", "citation": "Minn. Stat. § 325O.07"},
            "TN": {"strictness": 5, "rule": "Opt-in consent required.", "citation": "Tenn. Code § 47-18-3204(a)(4)"},
            "IN": {"strictness": 5, "rule": "Opt-in consent required.", "citation": "Ind. Code § 24-15-4"},
            "KY": {"strictness": 5, "rule": "Opt-in consent required.", "citation": "Ky. Rev. Stat. § 367.3613"},
            "RI": {"strictness": 5, "rule": "Opt-in consent required.", "citation": "R.I. Gen. Laws § 6-48.1-4"},
            "FL": {"strictness": 5, "rule": "Opt-in consent required.", "citation": "Fla. Stat. § 501.706"},
            "CA": {"strictness": 4, "rule": "Notice + right to limit use of sensitive PI (opt-out structure, not opt-in).", "citation": "Cal. Civ. Code § 1798.121; 11 CCR § 7027"},
            "UT": {"strictness": 3, "rule": "Notice + opt-out only (no consent required).", "citation": "Utah Code § 13-61-302(2)"},
            "IA": {"strictness": 3, "rule": "Notice + opt-out only.", "citation": "Iowa Code § 715D.4(2)"},
        },
        "implementation": "Three-tiered standard. Maryland requires consent AND minimization (strictest). Most states require opt-in consent. CA uses an opt-out structure with the unique 'Limit Use of Sensitive PI' right. UT/IA require notice + opt-out only. To satisfy MD, an opt-in consent flow alone is insufficient — the controller must also document that the processing is reasonably necessary and proportionate to the specific product/service requested. To satisfy all other states, opt-in consent with specific category-level granularity satisfies the binding constraint.",
        "true_conflict": False,  # All can be satisfied by an MD-strictness implementation
    },

    "sensitive_data_sale_treatment": {
        "description": "Whether sale of sensitive data is permitted with consent.",
        "category": "sensitive_data",
        "positions": {
            "MD": {"strictness": 10, "rule": "FLAT BAN on sale of sensitive data — consent does not cure.", "citation": "Md. Code Com. Law § 14-4607(b)(1)"},
            **{s: {"strictness": 5, "rule": "Sale of sensitive data permitted with opt-in consent (or, in CA, subject to general sale opt-out and limit-use right).", "citation": "Per state sensitive-data provision"} for s in ALL_STATES if s != "MD"}
        },
        "implementation": "Maryland is the binding constraint. Its flat ban means no controller can lawfully sell sensitive data of MD residents regardless of consent. Operationally: suppress sensitive-data sale at the data-flow level for MD residents. If state-of-residence cannot be reliably determined at the time of the sale, the conservative implementation suppresses sensitive-data sale across all consumers as a uniform compliance posture.",
        "true_conflict": False,
    },

    # --------------------------------------------------------------------
    # CONSUMER RIGHTS
    # --------------------------------------------------------------------

    "rights_response_time": {
        "description": "Initial deadline to respond to a verifiable consumer rights request.",
        "category": "rights",
        "positions": {
            "FL": {"strictness": 5, "rule": "45 days; one-time 15-day extension.", "citation": "Fla. Stat. § 501.713(2)"},
            **{s: {"strictness": 4, "rule": "45 days; 45-day extension permitted with notice.", "citation": "Per state act"} for s in ALL_STATES if s not in ("FL", "IA")},
            "IA": {"strictness": 3, "rule": "90 days; 45-day extension.", "citation": "Iowa Code § 715D.3(4)"},
        },
        "implementation": "FL has the shortest extension window (15 days vs. 45 elsewhere). The conservative ceiling: respond within 45 days without extension. Where extension is needed, FL caps it at 15 days. Build response-tracking to meet 45-day initial deadline universally.",
        "true_conflict": False,
    },

    "appeal_right_required": {
        "description": "Whether an internal appeal process must be provided when rights requests are denied.",
        "category": "rights",
        "positions": {
            **{s: {"strictness": 5, "required": True, "rule": "Appeal process required; consumer must be informed of process at denial.", "citation": "Per state act"} for s in ALL_STATES if s not in ("CA", "UT", "IA")},
            "CA": {"strictness": 1, "required": False, "rule": "No formal appeal right; CPPA complaint is the consumer's recourse.", "citation": "n/a"},
            "UT": {"strictness": 1, "required": False, "rule": "No appeal right.", "citation": "n/a"},
            "IA": {"strictness": 1, "required": False, "rule": "No appeal right.", "citation": "n/a"},
        },
        "implementation": "17 of 20 states require internal appeal. Build an appeal workflow that triggers on denial and provides 45-60 day response. CA/UT/IA have no statutory appeal but offering one as a uniform practice is operationally simpler than gating it by state.",
        "true_conflict": False,
    },

    "correction_right_provided": {
        "description": "Whether consumers have a right to correct inaccurate PD.",
        "category": "rights",
        "positions": {
            **{s: {"strictness": 5, "required": True, "rule": "Right to correct inaccurate PD.", "citation": "Per state act"} for s in ALL_STATES if s not in ("UT", "IA", "KY")},
            "UT": {"strictness": 1, "required": False, "rule": "No correction right.", "citation": "n/a"},
            "IA": {"strictness": 1, "required": False, "rule": "No correction right.", "citation": "n/a"},
            "KY": {"strictness": 1, "required": False, "rule": "No correction right.", "citation": "n/a"},
        },
        "implementation": "Most states require correction. Build it. UT/IA/KY are outliers; offering correction as a uniform practice is cheaper than state-gating.",
        "true_conflict": False,
    },

    # --------------------------------------------------------------------
    # OPT-OUT MECHANICS
    # --------------------------------------------------------------------

    "uoom_recognition_required": {
        "description": "Whether the controller must recognize Universal Opt-Out Mechanisms (e.g., Global Privacy Control).",
        "category": "opt_out",
        "positions": {
            "CO": {"strictness": 5, "required": True, "rule": "Must recognize UOOMs on AG-published list (currently includes GPC). 4 CCR § 904-3, § 5.06.", "citation": "Colo. Rev. Stat. § 6-1-1313(2); 4 CCR § 904-3"},
            "CA": {"strictness": 5, "required": True, "rule": "Must treat opt-out preference signals (incl. GPC) as valid opt-out of sale/share.", "citation": "11 CCR § 7025"},
            "CT": {"strictness": 5, "required": True, "rule": "UOOM recognition mandate effective Jan 2025.", "citation": "Conn. Gen. Stat. § 42-520(d)"},
            "OR": {"strictness": 5, "required": True, "rule": "UOOM recognition mandate.", "citation": "Or. Rev. Stat. § 646A.578(1)(b)"},
            "MT": {"strictness": 5, "required": True, "rule": "UOOM recognition mandate.", "citation": "Mont. Code § 30-14-2811"},
            "DE": {"strictness": 5, "required": True, "rule": "UOOM recognition mandate.", "citation": "Del. Code tit. 6 § 12D-104"},
            "NJ": {"strictness": 5, "required": True, "rule": "UOOM recognition mandate.", "citation": "N.J. Stat. § 56:8-166.7"},
            "NH": {"strictness": 5, "required": True, "rule": "UOOM recognition mandate.", "citation": "N.H. Rev. Stat. § 507-H:6"},
            "MN": {"strictness": 5, "required": True, "rule": "UOOM recognition mandate effective Jul 2025.", "citation": "Minn. Stat. § 325O.05"},
            "MD": {"strictness": 5, "required": True, "rule": "UOOM recognition mandate.", "citation": "Md. Code Com. Law § 14-4607"},
            "TX": {"strictness": 5, "required": True, "rule": "UOOM recognition mandate effective Jan 2025.", "citation": "Tex. Bus. & Com. Code § 541.055(e)"},
            "RI": {"strictness": 5, "required": True, "rule": "UOOM recognition mandate.", "citation": "R.I. Gen. Laws § 6-48.1"},
            **{s: {"strictness": 1, "required": False, "rule": "No UOOM recognition mandate.", "citation": ""} for s in ALL_STATES if s in ("VA", "UT", "FL", "IA", "TN", "IN", "KY", "NE")}
        },
        "implementation": "12 of 20 states mandate UOOM recognition. Configure the CMP and tag manager to treat GPC as a valid opt-out of sale/share/targeted advertising. This single fix produces multi-state benefit. Note: VA does not mandate UOOM but recognizes opt-out via a 'clear and conspicuous link' — recognizing GPC also satisfies VA.",
        "true_conflict": False,
    },

    "opt_out_persistence": {
        "description": "Persistence of opt-out across sessions and devices.",
        "category": "opt_out",
        "positions": {
            "CA": {"strictness": 5, "rule": "Opt-out must persist for at least 12 months; affirmative opt-in required to resume.", "citation": "Cal. Civ. Code § 1798.135(a)(2)"},
            "CO": {"strictness": 5, "rule": "Opt-out must persist; renewal request requires same affirmative process as initial opt-in.", "citation": "4 CCR § 904-3 § 5.04"},
            **{s: {"strictness": 4, "rule": "Opt-out must persist; specific renewal interval not enumerated.", "citation": "Per state act"} for s in ALL_STATES if s not in ("CA", "CO")}
        },
        "implementation": "12-month persistence (CA standard) is the conservative ceiling. The opt-out must apply across the consumer's known devices and accounts when made by an authenticated user. For unauthenticated users (browser-level GPC), persistence is per browser/device.",
        "true_conflict": False,
    },

    "opt_out_authorized_agent": {
        "description": "Whether consumers may use an authorized agent to submit opt-out requests.",
        "category": "opt_out",
        "positions": {
            "CA": {"strictness": 5, "required": True, "scope": "all rights", "rule": "Authorized agent for all rights; specific verification procedures.", "citation": "Cal. Civ. Code § 1798.140(d); 11 CCR § 7063"},
            "CO": {"strictness": 4, "required": True, "scope": "opt-out only", "rule": "Authorized agent for opt-out only.", "citation": "Colo. Rev. Stat. § 6-1-1306(1)(a)(IV)(D)"},
            "CT": {"strictness": 4, "required": True, "scope": "opt-out only", "rule": "Authorized agent for opt-out only.", "citation": "Conn. Gen. Stat. § 42-518(c)"},
            **{s: {"strictness": 2, "required": False, "scope": "varies", "rule": "Authorized agent permitted but not mandated.", "citation": ""} for s in ALL_STATES if s not in ("CA", "CO", "CT")}
        },
        "implementation": "CA's all-rights agent right is the broadest. To satisfy: build agent workflow with verification (written authorization from consumer; verify agent identity; optional verification with consumer). Agent infrastructure built for CA satisfies the others.",
        "true_conflict": False,
    },

    # --------------------------------------------------------------------
    # MINORS
    # --------------------------------------------------------------------

    "minor_treatment": {
        "description": "Treatment of personal data of consumers under 18.",
        "category": "minors",
        "positions": {
            "MD": {"strictness": 10, "rule": "FLAT BAN on sale and on processing for targeted advertising of PD of consumers known to be under 18 — regardless of consent.", "citation": "Md. Code Com. Law § 14-4607(b)(2)"},
            "CA": {"strictness": 7, "rule": "Affirmative opt-in required for sale/share of PD of known minors under 16; parental consent required for under 13.", "citation": "Cal. Civ. Code § 1798.120(c)"},
            "CO": {"strictness": 6, "rule": "Opt-in consent required for sale, targeted advertising, or profiling of PD of known minors under 18.", "citation": "Colo. Rev. Stat. § 6-1-1308(7)(c)"},
            "CT": {"strictness": 6, "rule": "Opt-in consent required for sale, targeted advertising of PD of known minors 13-17.", "citation": "Conn. Gen. Stat. § 42-520(a)(4)(C)"},
            "OR": {"strictness": 6, "rule": "Opt-in consent required for sale, targeted advertising, or profiling of PD of known minors under 16.", "citation": "Or. Rev. Stat. § 646A.578(2)(b)"},
            "MN": {"strictness": 6, "rule": "Opt-in consent required for sale, targeted advertising of PD of known minors under 18.", "citation": "Minn. Stat. § 325O.07"},
            "NJ": {"strictness": 6, "rule": "Opt-in consent required for sale, targeted advertising of PD of known minors 13-17.", "citation": "N.J. Stat. § 56:8-166.7"},
            "DE": {"strictness": 6, "rule": "Opt-in consent required for sale, targeted advertising of PD of known minors 13-17.", "citation": "Del. Code tit. 6 § 12D-104(d)(4)"},
            "NH": {"strictness": 6, "rule": "Opt-in consent for sale, targeted advertising of PD of known minors 13-17.", "citation": "N.H. Rev. Stat. § 507-H:6"},
            "TN": {"strictness": 6, "rule": "Opt-in consent for sale, targeted advertising of PD of known minors under 18.", "citation": "Tenn. Code § 47-18-3204"},
            "VA": {"strictness": 5, "rule": "Sensitive-data treatment (opt-in) for under-13 data; sale/targeted advertising treated as sensitive when known minor.", "citation": "Va. Code § 59.1-575"},
            "TX": {"strictness": 5, "rule": "Sensitive data treatment for known children's data (under 13).", "citation": "Tex. Bus. & Com. Code § 541.001(31)"},
            "MT": {"strictness": 5, "rule": "Opt-in for minors 13-15 sale/targeted advertising/profiling.", "citation": "Mont. Code § 30-14-2811"},
            "FL": {"strictness": 7, "rule": "Penalty trebled for knowing violations involving minor data; default-on personalization restrictions for under 18.", "citation": "Fla. Stat. § 501.713 + companion minor protection statutes"},
            **{s: {"strictness": 4, "rule": "Sensitive-data treatment for under-13 data; less prescriptive for 13-17.", "citation": ""} for s in ("UT", "IA", "IN", "KY", "RI", "NE")}
        },
        "implementation": "Maryland is the absolute ceiling — flat ban applies regardless of consent. To satisfy MD: identify known-under-18 users and suppress sale and targeted advertising entirely. CA/CO/CT/OR/MN/NJ/DE/NH/TN require opt-in consent for known minors. The conservative posture combines: (1) suppress sale/targeted advertising for any user known to be under 18 and resident in MD; (2) opt-in consent for any user known to be under 18 elsewhere; (3) parental consent under COPPA for known under-13 globally. 'Known' is the controller's actual knowledge or constructive knowledge from age-collection or behavioral signals.",
        "true_conflict": False,
        "note": "FL's penalty multiplier ($150k for minor violations) is independently the most severe per-violation exposure for minor missteps, even though the substantive standard is not the strictest.",
    },

    # --------------------------------------------------------------------
    # PROCESSOR / DPA
    # --------------------------------------------------------------------

    "processor_contract_requirements": {
        "description": "Required terms in controller-processor contracts.",
        "category": "processor",
        "positions": {
            "CA": {"strictness": 5, "rule": "Most prescriptive terms list (CCPA Regs § 7051): purpose limitation; confidentiality; deletion on directive; assistance with rights requests; assistance with security; subprocessor flowdown; audit; certification; immediate notification of inability to comply.", "citation": "11 CCR § 7051"},
            "CO": {"strictness": 4, "rule": "Detailed terms required.", "citation": "Colo. Rev. Stat. § 6-1-1305(5); 4 CCR § 904-3 § 8"},
            **{s: {"strictness": 4, "rule": "Substantially similar processor-contract terms.", "citation": "Per state act"} for s in ALL_STATES if s not in ("CA", "CO")}
        },
        "implementation": "CCPA Regs § 7051 has the most prescriptive list. A processor agreement that satisfies § 7051 satisfies the other states. Build a master DPA template against § 7051 and use everywhere.",
        "true_conflict": False,
    },

    # --------------------------------------------------------------------
    # RISK ASSESSMENTS / DPAs
    # --------------------------------------------------------------------

    "risk_assessment_required": {
        "description": "Whether controllers must conduct documented risk assessments / data protection assessments for high-risk processing.",
        "category": "assessments",
        "positions": {
            "CO": {"strictness": 5, "rule": "Most prescriptive: documented DPA required for sale, targeted advertising, profiling for legal/significant decisions, sensitive data processing, processing presenting heightened risk. Detailed contents specified in 4 CCR § 904-3 § 8.", "citation": "Colo. Rev. Stat. § 6-1-1309; 4 CCR § 904-3 § 8"},
            **{s: {"strictness": 4, "rule": "DPA required for high-risk processing including sale, targeted advertising, profiling, sensitive data.", "citation": "Per state act"} for s in ALL_STATES if s not in ("CO", "UT", "IA", "FL")},
            "UT": {"strictness": 1, "rule": "No DPA requirement.", "citation": "n/a"},
            "IA": {"strictness": 1, "rule": "No DPA requirement.", "citation": "n/a"},
            "FL": {"strictness": 4, "rule": "DPA required when applicability triggered.", "citation": "Fla. Stat. § 501.7012"},
        },
        "implementation": "CO's § 8 is the most prescriptive standard. A DPA conforming to CO's required contents (purposes, categories of data, sources, security measures, retention, risks identified, mitigation, balancing test) satisfies the other states' DPA requirements. UT/IA do not require DPAs but conducting them as a uniform practice supports defensibility (TIPA affirmative defense, defensibility in CT/NJ enforcement).",
        "true_conflict": False,
    },

    # --------------------------------------------------------------------
    # ENFORCEMENT POSTURE
    # --------------------------------------------------------------------

    "cure_period_status": {
        "description": "Whether a statutory cure period currently applies before AG can seek penalties.",
        "category": "enforcement",
        "positions": {
            "CA": {"cure_days": 0, "strictness": 5, "rule": "No cure period (CPRA sunset).", "citation": "Cal. Civ. Code § 1798.155"},
            "CO": {"cure_days": 0, "strictness": 5, "rule": "Cure period sunset Jan 1, 2025.", "citation": "Colo. Rev. Stat. § 6-1-1311"},
            "CT": {"cure_days": 0, "strictness": 5, "rule": "Cure period sunset Jan 1, 2025.", "citation": "Conn. Gen. Stat. § 42-525"},
            "OR": {"cure_days": 30, "strictness": 4, "rule": "30 days; sunset Jan 1, 2026.", "citation": "Or. Rev. Stat. § 646A.586"},
            "MT": {"cure_days": 30, "strictness": 4, "rule": "30 days; sunset April 1, 2026.", "citation": "Mont. Code § 30-14-2820"},
            "VA": {"cure_days": 30, "strictness": 4, "rule": "30 days, in effect.", "citation": "Va. Code § 59.1-583"},
            "UT": {"cure_days": 30, "strictness": 4, "rule": "30 days, in effect.", "citation": "Utah Code § 13-61-402"},
            "TX": {"cure_days": 30, "strictness": 4, "rule": "30 days, in effect.", "citation": "Tex. Bus. & Com. Code § 541.155"},
            "IA": {"cure_days": 90, "strictness": 3, "rule": "90 days, in effect.", "citation": "Iowa Code § 715D.8"},
            "FL": {"cure_days": 45, "strictness": 4, "rule": "45 days, in effect.", "citation": "Fla. Stat. § 501.722"},
            **{s: {"cure_days": 60, "strictness": 4, "rule": "Sunset or 60 days, varies.", "citation": ""} for s in ALL_STATES if s in ("DE", "NJ", "NH", "MD", "TN")},
            **{s: {"cure_days": 30, "strictness": 4, "rule": "30 days at enactment.", "citation": ""} for s in ALL_STATES if s in ("IN", "NE", "KY", "RI", "MN")},
        },
        "implementation": "CA, CO, CT have no cure period; FL/VA/UT/TX provide 30-45 days. For multi-state programs the conservative posture is to build and operate as if no cure period exists — the cure period is a temporary cushion at most.",
        "true_conflict": False,
    },
}


# ---------------------------------------------------------------------------
# Synthesis
# ---------------------------------------------------------------------------


@dataclass
class CeilingFinding:
    dimension: str
    category: str
    description: str
    binding_rule: str
    controlling_state: str | list[str]
    binding_citation: str
    other_states: list[dict]
    implementation_guidance: str
    true_conflict: bool = False
    note: str = ""


def synthesize(applicable_states: list[str], dimension_filter: list[str] | None = None) -> list[CeilingFinding]:
    findings = []
    for dim_key, dim in DIMENSIONS.items():
        if dimension_filter and dim_key not in dimension_filter:
            continue
        positions = dim["positions"]
        # Only consider positions for applicable states
        relevant = {s: positions[s] for s in applicable_states if s in positions}
        if not relevant:
            continue
        # Find max strictness
        max_strict = max(p["strictness"] for p in relevant.values())
        controlling = sorted([s for s, p in relevant.items() if p["strictness"] == max_strict])
        controlling_pos = relevant[controlling[0]]
        # Build "others" list (lower-strictness applicable states)
        others = []
        for s, p in relevant.items():
            if s not in controlling:
                others.append({"state": s, "rule": p["rule"], "citation": p.get("citation", "")})
        findings.append(CeilingFinding(
            dimension=dim_key,
            category=dim["category"],
            description=dim["description"],
            binding_rule=controlling_pos["rule"],
            controlling_state=controlling[0] if len(controlling) == 1 else controlling,
            binding_citation=controlling_pos.get("citation", ""),
            other_states=others,
            implementation_guidance=dim["implementation"],
            true_conflict=dim.get("true_conflict", False),
            note=dim.get("note", ""),
        ))
    return findings


def render_text(findings: list[CeilingFinding]) -> str:
    lines = []
    by_cat: dict[str, list[CeilingFinding]] = {}
    for f in findings:
        by_cat.setdefault(f.category, []).append(f)
    for cat, items in by_cat.items():
        lines.append(f"\n## {cat.upper().replace('_', ' ')}\n")
        for f in items:
            cs = f.controlling_state if isinstance(f.controlling_state, str) else ", ".join(f.controlling_state)
            lines.append(f"### {f.dimension}")
            lines.append(f"**Description:** {f.description}")
            lines.append(f"**Binding rule (controlling: {cs}):** {f.binding_rule}")
            if f.binding_citation:
                lines.append(f"**Citation:** {f.binding_citation}")
            if f.other_states:
                lines.append(f"**Other applicable states' positions:**")
                for o in f.other_states:
                    cite = f" ({o['citation']})" if o['citation'] else ""
                    lines.append(f"  - {o['state']}: {o['rule']}{cite}")
            lines.append(f"**Implementation:** {f.implementation_guidance}")
            if f.note:
                lines.append(f"**Note:** {f.note}")
            if f.true_conflict:
                lines.append(f"**⚠️ TRUE CONFLICT:** This dimension presents an irreconcilable conflict; satisfy each applicable state on a per-resident basis.")
            lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------


def main() -> int:
    p = argparse.ArgumentParser(description="Conflict-of-laws synthesizer for US state privacy laws.")
    p.add_argument("--states", help="Comma-separated list of applicable two-letter state codes (e.g., CA,VA,CO,CT).")
    p.add_argument("--states-from", help="Path to applicability_check.py JSON output; states with verdict 'Applies' or 'Likely Applies' will be used.")
    p.add_argument("--dimensions", help="Comma-separated dimension filter (default: all).")
    p.add_argument("--output", help="Write JSON output to path (default: human-readable to stdout).")
    p.add_argument("--format", choices=["json", "text"], default="text", help="Output format.")
    args = p.parse_args()

    if args.states:
        states = [s.strip().upper() for s in args.states.split(",") if s.strip()]
    elif args.states_from:
        with open(args.states_from, "r") as f:
            data = json.load(f)
        results = data.get("results", [])
        states = [r["state"] for r in results if r.get("verdict") in ("Applies", "Likely Applies")]
    else:
        p.error("Provide --states or --states-from.")

    dim_filter = [d.strip() for d in args.dimensions.split(",")] if args.dimensions else None

    findings = synthesize(states, dim_filter)

    if args.format == "json" or args.output:
        out_data = {
            "applicable_states": states,
            "findings_count": len(findings),
            "findings": [asdict(f) for f in findings],
        }
        text = json.dumps(out_data, indent=2, default=str)
    else:
        text = f"# Compliance Ceiling — applicable states: {', '.join(states)}\n" + render_text(findings)

    if args.output:
        with open(args.output, "w") as f:
            f.write(text)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
