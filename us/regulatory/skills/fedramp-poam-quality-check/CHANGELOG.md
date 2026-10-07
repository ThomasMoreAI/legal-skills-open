# Changelog - fedramp-poam-qc

All notable changes to the FedRAMP POAM Quality Check skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-10-25

### Added
- Initial release of fedramp-poam-qc skill
- Tier 1: Header and format sanity checks (≤2k tokens)
- Tier 2: Naming convention validation and deduplication (≤6k tokens)
- Tier 3: Cross-sheet consistency analysis (≤12k tokens)
- Support for TSV-format POAM files
- FedRAMP remediation timeline validation (30/90/180 day rules)
- Duplicate detection using hash-based and similarity scoring
- JSON findings output with error/warning/stats structure
- Markdown fix suggestions with severity ranking
- Cited 4 authoritative sources (FedRAMP.gov, NIST)
- Example file demonstrating T1 validation flow
- Pre-check validation for file integrity and encoding

### Security
- Read-only file operations
- No external network calls
- No credential handling
- Local processing only

### Documentation
- Complete SKILL.md following CLAUDE.md §3 format
- Example usage in examples/fedramp-poam-qc-example.txt
- Resource links to FedRAMP and NIST official documentation
