#!/usr/bin/env python3
"""Validate every published Akoma Ntoso pilot against the official OASIS XSD."""

from __future__ import annotations

import pathlib
import subprocess
import sys


ROOT = pathlib.Path(__file__).resolve().parent.parent
AKN_DIR = ROOT / "docs" / "datos" / "akoma-ntoso"
XSD_PATH = ROOT / "11_calidad" / "xsd" / "akomantoso30.xsd"


def main() -> int:
    """Run xmllint --schema over every pilot XML and report failures."""
    if not XSD_PATH.exists():
        print(f"No se encuentra el XSD: {XSD_PATH.relative_to(ROOT)}", file=sys.stderr)
        return 2
    xmls = sorted(AKN_DIR.glob("*.xml"))
    if not xmls:
        print(f"No hay XML en {AKN_DIR.relative_to(ROOT)}", file=sys.stderr)
        return 2
    failures = []
    for path in xmls:
        result = subprocess.run(
            [
                "xmllint",
                "--noout",
                "--nonet",
                "--schema",
                str(XSD_PATH),
                str(path),
            ],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            failures.append((path, result.stderr.strip()))
        else:
            print(f"OK: {path.relative_to(ROOT)}")
    if failures:
        for path, error in failures:
            print(f"FALLA: {path.relative_to(ROOT)}", file=sys.stderr)
            print(error, file=sys.stderr)
        print(
            f"{len(failures)} de {len(xmls)} XML no conformes al XSD "
            "Akoma Ntoso 3.0 (OASIS LegalDocML 1.0).",
            file=sys.stderr,
        )
        return 1
    print(f"{len(xmls)} XML conformes al XSD Akoma Ntoso 3.0.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
