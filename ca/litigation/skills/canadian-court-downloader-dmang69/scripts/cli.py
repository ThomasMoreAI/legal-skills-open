"""
CLI — Canadian Court Document Downloader v2

  python cli.py download --citation "2019 SCC 65" --out ../outputs
  python cli.py batch --file cases.json --out ../outputs --matter "Owings"
  python cli.py ocr --pdf path/to/file.pdf
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from court_engine import (  # noqa: E402
    DownloaderConfig,
    download_batch,
    is_scanned_pdf,
    ocr_pdf,
)


def main() -> int:
    ap = argparse.ArgumentParser(description="Canadian court document downloader v2")
    sub = ap.add_subparsers(dest="cmd", required=True)

    d = sub.add_parser("download")
    d.add_argument("--citation", action="append", required=True)
    d.add_argument("--name", action="append", default=[])
    d.add_argument("--proposition", action="append", default=[])
    d.add_argument("--out", type=Path, default=Path(__file__).resolve().parents[1] / "outputs")
    d.add_argument("--matter", default="")
    d.add_argument("--ocr", action="store_true")
    d.add_argument("--delay", type=float, default=0.5)

    b = sub.add_parser("batch")
    b.add_argument("--file", type=Path, required=True, help="JSON list of {citation,name,tab,proposition}")
    b.add_argument("--out", type=Path, default=Path(__file__).resolve().parents[1] / "outputs")
    b.add_argument("--matter", default="")
    b.add_argument("--ocr", action="store_true")
    b.add_argument("--delay", type=float, default=0.5)

    o = sub.add_parser("ocr")
    o.add_argument("--pdf", type=Path, required=True)

    args = ap.parse_args()
    cfg = DownloaderConfig(
        matter=getattr(args, "matter", "") or "",
        include_ocr=bool(getattr(args, "ocr", False)),
        batch_delay_seconds=float(getattr(args, "delay", 0.5) or 0.5),
    )

    if args.cmd == "download":
        cases = []
        for i, cit in enumerate(args.citation):
            cases.append(
                {
                    "citation": cit,
                    "name": args.name[i] if i < len(args.name) else None,
                    "proposition": args.proposition[i] if i < len(args.proposition) else "",
                    "tab": i + 1,
                }
            )
        results = download_batch(cases, args.out, config=cfg)
        print(json.dumps([r.to_dict() for r in results], indent=2))
        print(f"Reports: {args.out / 'manifest.json'}")
        return 0

    if args.cmd == "batch":
        data = json.loads(args.file.read_text(encoding="utf-8"))
        if isinstance(data, dict) and "cases" in data:
            cases = data["cases"]
            cfg.matter = data.get("matter", cfg.matter)
        else:
            cases = data
        results = download_batch(cases, args.out, config=cfg)
        print(json.dumps({"count": len(results), "out": str(args.out)}, indent=2))
        return 0

    if args.cmd == "ocr":
        pdf = args.pdf
        scanned = is_scanned_pdf(pdf)
        print(f"scanned={scanned}")
        out = pdf.with_suffix(".ocr.txt")
        print(json.dumps(ocr_pdf(pdf, out), indent=2))
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
