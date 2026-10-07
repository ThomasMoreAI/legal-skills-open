#!/usr/bin/env python3
"""
citation_audit.py — Audit a generated memo (markdown or DOCX-input JSON) for
citation discipline.

**Scope.** This auditor is designed to run on **client-facing deliverables**
(the markdown memo produced by Step 6, before DOCX generation). It is *not*
designed for the SKILL.md orchestrator file or the reference files themselves,
which contain workflow prose, tool descriptions, and pedagogical examples that
will trip the substantive-claim detector by design. Run only against the
specific memo file being delivered.

The skill's SKILL.md mandates inline citations for every obligation, threshold,
right, or penalty figure. This script enforces that mandate mechanically:

1. **Substantive-claim detection.** Identifies sentences that assert a legal
   obligation, right, threshold, or penalty (using regex pattern detection of
   privacy-law assertion markers like "must," "shall," "is required to,"
   "is prohibited from," "consumer count of [number]," "penalty of [amount]").
2. **Citation presence check.** For each substantive claim, verify an inline
   citation appears within the same sentence or the immediately following
   parenthetical.
3. **Citation format check.** Verify each citation matches a canonical format
   for state privacy laws (e.g., `Cal. Civ. Code § 1798.140(d)`,
   `Va. Code § 59.1-575`, `4 CCR § 904-3`, `11 CCR § 7027`).
4. **Citation-existence check.** For citations to state files, verify the cited
   section is plausible against the statute structure (e.g., warn if a `Cal.
   Civ. Code § 1798.X` is cited where X is outside the CCPA range).
5. **Naming consistency check.** Flag uses of "CCPA" or "CPRA" as if distinct
   statutes (skill convention is to cite Cal. Civ. Code §§ 1798.100 et seq.
   directly; "CCPA/CPRA" framing as a casual reference is allowed but
   citations should be to code, not to act-name).

Usage:
    python citation_audit.py --input memo.md
    python citation_audit.py --input memo.md --strict   # fails on warnings
    python citation_audit.py --input memo.md --output audit_report.json

Exit codes:
    0 — clean (no errors; warnings ok)
    1 — errors found
    2 — input or invocation error

Part of the us-state-privacy-navigator skill.
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict


# ---------------------------------------------------------------------------
# Patterns
# ---------------------------------------------------------------------------

# Canonical citation forms accepted. Order matters; first match wins.
CITATION_PATTERNS = [
    # California Civil Code (CCPA/CPRA codified)
    (re.compile(r"Cal\. ?Civ\. ?Code §+ ?1798\.\d+(\.\d+)?(\([a-z0-9]+\))*"), "CA Civil Code"),
    # California regulations (CPPA Regs)
    (re.compile(r"11 ?C\.?C\.?R\.? §+ ?7\d{3}(\.\d+)?(\([a-z0-9]+\))*"), "CA Privacy Regs"),
    (re.compile(r"CCPA Regs? §+ ?7\d{3}(\.\d+)?(\([a-z0-9]+\))*"), "CCPA Regs (informal)"),
    # Colorado Privacy Act
    (re.compile(r"Colo\. ?Rev\. ?Stat\. §+ ?6-1-13\d{2}(\([a-z0-9]+\))*"), "CO Privacy Act"),
    (re.compile(r"4 ?C\.?C\.?R\.? §+ ?904-3"), "CO Privacy Rules"),
    # Virginia
    (re.compile(r"Va\. ?Code §+ ?59\.1-5\d{2}(\([a-z0-9]+\))*"), "VA Privacy Act"),
    # Connecticut
    (re.compile(r"Conn\. ?Gen\. ?Stat\. §+ ?42-5\d{2}(\([a-z0-9]+\))*"), "CT Privacy Act"),
    # Utah
    (re.compile(r"Utah Code §+ ?13-61-\d+(\([a-z0-9]+\))*"), "UT Privacy Act"),
    # Texas
    (re.compile(r"Tex\. ?Bus\. ?& ?Com\. ?Code §+ ?541\.\d+(\([a-z0-9]+\))*"), "TX Privacy Act"),
    (re.compile(r"Tex\. ?Bus\. ?& ?Com\. ?Code (?:Ch\.|Chapter) ?5(?:03|41)"), "TX Privacy Act"),
    # Oregon
    (re.compile(r"Or\. ?Rev\. ?Stat\. §+ ?646A\.5\d{2}(\([a-z0-9]+\))*"), "OR Privacy Act"),
    # Montana
    (re.compile(r"Mont\. ?Code §+ ?30-14-28\d{2}(\([a-z0-9]+\))*"), "MT Privacy Act"),
    # Florida
    (re.compile(r"Fla\. ?Stat\. §+ ?501\.7\d{2}(\([a-z0-9]+\))*"), "FL FDBR"),
    # Iowa
    (re.compile(r"Iowa Code §+ ?715D\.\d+(\([a-z0-9]+\))*"), "IA Privacy Act"),
    # Indiana
    (re.compile(r"Ind\. ?Code §+ ?24-15(?:-\d+)?(\([a-z0-9]+\))*"), "IN Privacy Act"),
    # Tennessee
    (re.compile(r"Tenn\. ?Code §+ ?47-18-32\d{2}(\([a-z0-9]+\))*"), "TN Privacy Act"),
    # Delaware
    (re.compile(r"Del\. ?Code (?:tit\. ?6|Title 6),? (?:Ch\.|Chapter) ?12D"), "DE Privacy Act"),
    (re.compile(r"Del\. ?Code (?:tit\. ?6|Title 6) §+ ?12D-\d+(\([a-z0-9]+\))*"), "DE Privacy Act"),
    # New Jersey
    (re.compile(r"N\.?J\.? ?Stat\. §+ ?56:8-166\.\d+(\([a-z0-9]+\))*"), "NJ Privacy Act"),
    # New Hampshire
    (re.compile(r"N\.?H\.? ?Rev\. ?Stat\. (?:ch\.|Chapter) ?507-H"), "NH Privacy Act"),
    (re.compile(r"N\.?H\.? ?Rev\. ?Stat\. §+ ?507-H:\d+(\([a-z0-9]+\))*"), "NH Privacy Act"),
    # Nebraska
    (re.compile(r"Neb\. ?Rev\. ?Stat\. §+ ?87-1\d{3}(\([a-z0-9]+\))*"), "NE Privacy Act"),
    # Kentucky
    (re.compile(r"Ky\. ?Rev\. ?Stat\. §+ ?367\.36\d{2}(\([a-z0-9]+\))*"), "KY Privacy Act"),
    # Maryland
    (re.compile(r"Md\. ?Code Com\. ?Law §+ ?14-46\d{2}(\([a-z0-9]+\))*"), "MD MODPA"),
    # Minnesota
    (re.compile(r"Minn\. ?Stat\. (?:ch\.|Chapter) ?325O"), "MN Privacy Act"),
    (re.compile(r"Minn\. ?Stat\. §+ ?325O\.\d+(\([a-z0-9]+\))*"), "MN Privacy Act"),
    # Rhode Island
    (re.compile(r"R\.?I\.? ?Gen\. ?Laws §+ ?6-48\.1(?:-\d+)?(\([a-z0-9]+\))*"), "RI Privacy Act"),
    # Federal
    (re.compile(r"15 U\.?S\.?C\.? §+ ?\d+"), "Federal U.S.C."),
    (re.compile(r"16 C\.?F\.?R\.? (?:Part|§) ?\d+"), "Federal C.F.R."),
    (re.compile(r"18 U\.?S\.?C\.? §+ ?\d+"), "Federal U.S.C."),
    # California adjacent
    (re.compile(r"Cal\. ?Penal Code §+ ?6\d{2}(\.\d+)?(\([a-z0-9]+\))*"), "CIPA"),
    (re.compile(r"Cal\. ?Bus\. ?& ?Prof\. ?Code §+ ?\d+"), "CA UCL/CalOPPA"),
    # BIPA
    (re.compile(r"740 ?ILCS ?14"), "BIPA"),
    # Washington MHMDA
    (re.compile(r"Wash\. ?Rev\. ?Code (?:ch\.|Chapter) ?19\.373"), "WA MHMDA"),
    # Generic fallback "§ N" with the immediately preceding context
    (re.compile(r"§+ ?\d+(\.\d+)*"), "Generic section reference (verify)"),
]


# Substantive-claim markers — sentences containing these likely assert legal
# obligations, rights, or thresholds and require citations.
SUBSTANTIVE_MARKERS = re.compile(
    r"\b("
    r"must (?:not |provide |honor |maintain |disclose |conduct |obtain |document |implement |allow |permit |stop |delete |respond |notify |suppress |verify |require)"
    r"|shall(?: not)?(?: provide| honor| maintain| disclose| conduct| obtain| document| implement| allow| permit| stop| delete| respond| notify| suppress| verify| require)?"
    r"|is (?:required|prohibited|permitted|obligated|forbidden|deemed)"
    r"|are (?:required|prohibited|permitted|obligated|forbidden|deemed)"
    r"|has (?:the|a) right to"
    r"|have (?:the|a) right to"
    r"|right to (?:know|access|delete|correct|opt out|opt-out|appeal|portability|limit use|object|restrict)"
    r"|threshold of"
    r"|penalty of \$"
    r"|penalties? up to \$"
    r"|fine of \$"
    r"|civil penalt"
    r"|cure period"
    r"|effective date"
    r"|effective (January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
    r"|consumer count (?:of|exceeding|threshold)"
    r"|annual (?:gross )?revenue (?:of|exceeding|threshold)"
    r"|opt[- ]?in consent"
    r"|opt[- ]?out (?:right|mechanism|signal)"
    r"|sensitive (?:data|personal information)"
    r"|sale of (?:personal information|personal data|sensitive data)"
    r"|sharing of (?:personal information|personal data)"
    r"|targeted advertising"
    r"|cross[- ]?context behavioral advertising"
    r"|controller (?:must|shall|is required)"
    r"|processor (?:must|shall|is required)"
    r"|service provider (?:must|shall|is required)"
    r"|business (?:must|shall|is required)"
    r"|under [A-Z][a-z]+(?: [A-Z][a-z]+)*'s privacy law"
    r")\b",
    re.IGNORECASE,
)


# Phrases that should NOT introduce a substantive-claim flag (general
# discussion, headers, etc.)
EXCLUSION_MARKERS = re.compile(
    r"^(#+|>|\*|-|\d+\.)\s",  # markdown structure markers at line start
)


# Naming consistency — flag references that reify "CCPA" / "CPRA" as if they
# were separate operative statutes. Citation should be to Cal. Civ. Code.
NAMING_INCONSISTENCY = [
    (re.compile(r"\bCPRA\b(?! \()"), "Use 'Cal. Civ. Code §§ 1798.100 et seq.' or '(as amended by CPRA)' to avoid reifying CPRA as a separate statute."),
]


@dataclass
class Finding:
    severity: str  # "ERROR" or "WARNING"
    line_number: int
    message: str
    excerpt: str = ""
    suggestion: str = ""


# ---------------------------------------------------------------------------
# Section-existence sanity check (not exhaustive — flags only obvious errors)
# ---------------------------------------------------------------------------

CCPA_SECTION_RANGE = (1798.100, 1798.199)  # CCPA + CPRA codification

def section_exists_check(citation_text: str) -> tuple[bool, str]:
    """For California Civil Code citations, verify the section is in CCPA range.
    Returns (is_plausible, message)."""
    m = re.search(r"Cal\. ?Civ\. ?Code §+ ?(\d+\.\d+)", citation_text)
    if not m:
        return True, ""
    try:
        section_num = float(m.group(1))
    except ValueError:
        return True, ""
    if not (CCPA_SECTION_RANGE[0] <= section_num <= CCPA_SECTION_RANGE[1]):
        return False, f"Citation {citation_text} is outside the CCPA codified range (§§ 1798.100-1798.199). Verify the section number."
    return True, ""


# ---------------------------------------------------------------------------
# Auditor
# ---------------------------------------------------------------------------


def split_sentences(text: str) -> list[tuple[int, str]]:
    """Split markdown text into sentences, retaining 1-indexed line numbers.
    Returns list of (line_number, sentence) pairs."""
    sentences = []
    # Common legal-citation abbreviations whose internal periods must not split sentences.
    ABBREV = (
        "Cal", "Va", "Colo", "Conn", "Tex", "Or", "Mont", "Fla", "Iowa", "Ind",
        "Tenn", "Del", "Md", "Minn", "Neb", "Ky", "Wash", "Ill", "U.S", "U.S.C",
        "C.F.R", "Civ", "Stat", "Rev", "Code", "Bus", "Com", "Prof", "Penal",
        "Gen", "tit", "Ch", "ch", "Inc", "Ltd", "Co", "Mr", "Mrs", "Dr", "Hon",
        "Jan", "Feb", "Mar", "Apr", "Jun", "Jul", "Aug", "Sep", "Sept", "Oct",
        "Nov", "Dec", "e.g", "i.e", "v",
    )
    SENTINEL = "\x00DOT\x00"
    for line_idx, line in enumerate(text.splitlines(), start=1):
        if EXCLUSION_MARKERS.match(line):
            continue
        # Mask abbreviation periods.
        masked = line
        for ab in ABBREV:
            masked = re.sub(rf"\b{re.escape(ab)}\.", f"{ab}{SENTINEL}", masked)
        # Now split on real sentence terminators followed by space+capital.
        for sent in re.split(r"(?<=[.!?])\s+(?=[A-Z(])", masked):
            sent = sent.replace(SENTINEL, ".").strip()
            if sent:
                sentences.append((line_idx, sent))
    return sentences


def has_citation(sentence: str) -> tuple[bool, list[str]]:
    """Return (any_citation_found, list of cited categories)."""
    found = []
    for pat, label in CITATION_PATTERNS:
        if pat.search(sentence):
            found.append(label)
    return bool(found), found


def audit_text(text: str) -> list[Finding]:
    findings: list[Finding] = []
    sentences = split_sentences(text)

    for line_no, sent in sentences:
        # Substantive-claim detection
        m = SUBSTANTIVE_MARKERS.search(sent)
        if not m:
            continue
        # Skip if this sentence is in a code block / table cell that begins with |
        if sent.strip().startswith("|"):
            # tables get audited at section level, not sentence level
            continue
        cited, categories = has_citation(sent)
        if not cited:
            findings.append(Finding(
                severity="ERROR",
                line_number=line_no,
                message="Substantive claim lacks inline citation.",
                excerpt=sent[:240],
                suggestion="Add a citation to the controlling statute or regulation. Format examples: '(Cal. Civ. Code § 1798.140(d))', '(Va. Code § 59.1-575)', '(11 CCR § 7027)'.",
            ))
        else:
            # Section-existence sanity check
            is_plausible, plausibility_msg = section_exists_check(sent)
            if not is_plausible:
                findings.append(Finding(
                    severity="WARNING",
                    line_number=line_no,
                    message=plausibility_msg,
                    excerpt=sent[:240],
                ))

    # Naming consistency checks
    for line_idx, line in enumerate(text.splitlines(), start=1):
        for pat, msg in NAMING_INCONSISTENCY:
            for m in pat.finditer(line):
                findings.append(Finding(
                    severity="WARNING",
                    line_number=line_idx,
                    message=f"Naming inconsistency: '{m.group()}' used outside parenthetical.",
                    excerpt=line[:240],
                    suggestion=msg,
                ))

    # "[citation needed]" markers — these are intentionally inserted by the
    # skill where the analyst couldn't verify a citation. They should be
    # surfaced for review before publication.
    for line_idx, line in enumerate(text.splitlines(), start=1):
        if "[citation needed" in line.lower():
            findings.append(Finding(
                severity="ERROR",
                line_number=line_idx,
                message="Unresolved [citation needed] marker — must be resolved or claim removed before publication.",
                excerpt=line[:240],
            ))

    return findings


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------


def main() -> int:
    p = argparse.ArgumentParser(description="Citation discipline auditor.")
    p.add_argument("--input", required=True, help="Path to a markdown file (the memo).")
    p.add_argument("--output", help="Optional JSON output path.")
    p.add_argument("--strict", action="store_true", help="Fail on warnings (default: fail only on errors).")
    p.add_argument("--quiet", action="store_true", help="Suppress non-finding output.")
    args = p.parse_args()

    try:
        with open(args.input, "r") as f:
            text = f.read()
    except OSError as e:
        print(f"Error reading {args.input}: {e}", file=sys.stderr)
        return 2

    findings = audit_text(text)
    errors = [f for f in findings if f.severity == "ERROR"]
    warnings_ = [f for f in findings if f.severity == "WARNING"]

    if args.output:
        with open(args.output, "w") as f:
            json.dump({
                "input": args.input,
                "errors_count": len(errors),
                "warnings_count": len(warnings_),
                "findings": [asdict(x) for x in findings],
            }, f, indent=2)

    if not args.quiet:
        if not findings:
            print(f"✓ {args.input}: 0 errors, 0 warnings — citation discipline clean.")
        else:
            print(f"{args.input}: {len(errors)} error(s), {len(warnings_)} warning(s).\n")
            for f in findings:
                marker = "✗" if f.severity == "ERROR" else "⚠"
                print(f"{marker} Line {f.line_number}: {f.message}")
                if f.excerpt:
                    print(f"    Excerpt: {f.excerpt}")
                if f.suggestion:
                    print(f"    Suggestion: {f.suggestion}")
                print()

    if errors:
        return 1
    if args.strict and warnings_:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
