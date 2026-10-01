#!/usr/bin/env python3
"""Regenerate sources/MANIFEST.json from the canonical CEV download URLs.

Computes sha256 + bytes for each downloadable unit so fetch_sources.sh can
verify. The 10 individual digital-edition PDFs are hashed from a local corpus
dir (--corpus); the Colombia-adentro volume ships as a single ZIP that extracts
to 14 territorial books, so it is fetched to a temp file, hashed, then discarded
(the raw zip is not kept after extraction). Maintenance script — run when the
source set changes; not needed at skill runtime.

Usage:
  python3 scripts/build_manifest.py --corpus ~/Downloads/comision-de-la-verdad-informe-final
  python3 scripts/build_manifest.py --no-zip   # skip the 86 MB zip re-fetch (sha256=null)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import tempfile
import urllib.request
from pathlib import Path

BASE = "https://www.comisiondelaverdad.co"
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "sources" / "MANIFEST.json"

# (url_path, output_filename, local_corpus_name | None for the zip)
UNITS = [
    ("/sites/default/files/descargables/2022-08/IF_CONVOCATORIA-A-LA-PAZ-GRANDE_DIGITAL_2022.pdf",
     "01-Convocatoria-a-la-paz-grande.pdf", "01-Convocatoria-a-la-paz-grande.pdf"),
    ("/sites/default/files/descargables/2022-08/FINAL%20CEV_HALLAZGOS_DIGITAL_2022.pdf",
     "02-Hallazgos-y-recomendaciones.pdf", "02-Hallazgos-y-recomendaciones.pdf"),
    ("/sites/default/files/descargables/2022-08/CEV_NARRATIVA%20HISTORICA_DIGITAL_2022.pdf",
     "03-No-mataras-narrativa-historica.pdf", "03-No-mataras-narrativa-historica.pdf"),
    ("/sites/default/files/descargables/2022-08/CEV_VIOLACIONES_DIGITAL_2022.pdf",
     "04-Hasta-la-guerra-tiene-limites-violaciones.pdf", "04-Hasta-la-guerra-tiene-limites-violaciones.pdf"),
    ("/sites/default/files/descargables/2022-08/CEV_SUFRIR%20LA%20GUERRA%20Y%20REHACER%20LA%20VIDA_DIGITAL_2022.pdf",
     "06-Sufrir-la-guerra-y-rehacer-la-vida-impactos.pdf", "06-Sufrir-la-guerra-y-rehacer-la-vida-impactos.pdf"),
    ("/sites/default/files/descargables/2022-08/CEV_TESTIMONIAL_DIGITAL_2022.pdf",
     "07-Cuando-los-pajaros-no-cantaban-testimonial.pdf", "07-Cuando-los-pajaros-no-cantaban-testimonial.pdf"),
    ("/sites/default/files/descargables/2022-08/CEV_ETNICO_DIGITAL_2022.pdf",
     "08-Resistir-no-es-aguantar-pueblos-etnicos.pdf", "08-Resistir-no-es-aguantar-pueblos-etnicos.pdf"),
    ("/sites/default/files/descargables/2022-08/CEV_MI%20CUERPO%20ES%20LA%20VERDAD_DIGITAL_2022.pdf",
     "09-Mi-cuerpo-es-la-verdad-mujeres-y-LGBTIQ.pdf", "09-Mi-cuerpo-es-la-verdad-mujeres-y-LGBTIQ.pdf"),
    ("/sites/default/files/descargables/2022-08/CEV_NNA_DIGITAL_2022.pdf",
     "10-No-es-un-mal-menor-ninos-ninas-adolescentes.pdf", "10-No-es-un-mal-menor-ninos-ninas-adolescentes.pdf"),
    ("/sites/default/files/descargables/2022-09/CEV_LA%20COLOMBIA%20FUERA%20DE%20COLOMBIA_DIGITAL_2022%20corr.pdf",
     "11-La-Colombia-fuera-de-Colombia-exilio.pdf", "11-La-Colombia-fuera-de-Colombia-exilio.pdf"),
    ("/sites/default/files/descargables/2022-08/IF_territorios_digital.zip",
     "05-Colombia-adentro_digital.zip", None),
]


def _sha256(path: Path) -> tuple[str, int]:
    h, n = hashlib.sha256(), 0
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
            n += len(chunk)
    return h.hexdigest(), n


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", type=Path,
                    default=Path.home() / "Downloads" / "comision-de-la-verdad-informe-final")
    ap.add_argument("--no-zip", action="store_true", help="skip the 86 MB zip re-fetch")
    a = ap.parse_args(argv)

    downloads = []
    for url_path, out_name, local in UNITS:
        url = BASE + url_path
        sha, nbytes = None, None
        if local:
            p = a.corpus / local
            if p.is_file():
                sha, nbytes = _sha256(p)
            else:
                print(f"[warn] local missing, sha256 null: {local}", file=sys.stderr)
        elif not a.no_zip:
            print(f"[info] fetching zip to hash: {url}", file=sys.stderr)
            try:
                with tempfile.NamedTemporaryFile(delete=True) as tmp:
                    with urllib.request.urlopen(url, timeout=300) as r:  # noqa: S310
                        while chunk := r.read(1 << 20):
                            tmp.write(chunk)
                    tmp.flush()
                    sha, nbytes = _sha256(Path(tmp.name))
            except Exception as e:  # noqa: BLE001
                print(f"[warn] zip fetch failed ({e}); sha256 null", file=sys.stderr)
        downloads.append({"url": url, "filename": out_name,
                          "sha256": sha, "bytes": nbytes,
                          "extract": "zip -> skills/.../05-Colombia-adentro/ (14 territorial books)" if local is None else None})

    manifest = {
        "_meta": {
            "source": "Comisión para el Esclarecimiento de la Verdad (CEV) — Informe Final 'Hay Futuro Si Hay Verdad' (2022)",
            "base_url": BASE,
            "license": "CC BY-NC-SA 4.0",
            "note": "11 downloadable units = 10 Spanish digital-edition PDFs + the Colombia-adentro ZIP (extracts to 14 territorial books). Other editions (print, French/English, Indigenous-language) exist on comisiondelaverdad.co. Full text is bundled gzipped under references/fulltext/; these PDFs are the provenance binaries, fetched on demand via scripts/fetch_sources.sh.",
            "units": len(downloads),
        },
        "downloads": downloads,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    have = sum(1 for d in downloads if d["sha256"])
    print(f"wrote {OUT.relative_to(ROOT)} — {len(downloads)} units, {have} with sha256")
    return 0


if __name__ == "__main__":
    sys.exit(main())
