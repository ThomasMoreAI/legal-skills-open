#!/usr/bin/env python3
"""
Render JEDNOHO dokumentu z docxtpl vzoru + HARD GATES per typ dokumentu.

Použití:
    python render_doc.py <vzor-dir> <data.json> <out-dir>

Gates (z researche — kritická procesní pravidla V KÓDU, ne jen v textu):
- predzalobni-vyzva: lhůta k plnění ≥ 7 dnů (§ 142a o.s.ř. — jinak žalobce ztrácí
  nárok na náhradu nákladů řízení) + povinná doručovací adresa dlužníka.
- plna-moc: upozornění na úředně ověřený podpis u úkonů vůči katastru.

Vyžaduje: pip install docxtpl. Konstanty kanceláře: config/kancelar.json.
"""
import json
import sys
from datetime import date
from pathlib import Path

from docxtpl import DocxTemplate

def _find_config() -> Path:
    """kancelar.json: nejdřív skill-lokální (samostatný skill upload), pak plugin root."""
    here = Path(__file__).resolve()
    for cand in (here.parents[1] / "config" / "kancelar.json",
                 here.parents[3] / "config" / "kancelar.json"):
        if cand.exists():
            return cand
    raise FileNotFoundError("config/kancelar.json nenalezen (skill ani plugin root)")


CONFIG = _find_config()


def gate_predzalobni(data: dict) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    lhuta = data.get("lhuta_k_plneni_dny")
    if not isinstance(lhuta, int):
        errors.append("lhuta_k_plneni_dny chybí nebo není číslo (celé dny)")
    elif lhuta < 7:
        errors.append(
            f"GATE §142a o.s.ř.: lhůta k plnění {lhuta} dnů je POD zákonným minimem 7 dnů "
            "— žalobce by ztratil nárok na náhradu nákladů řízení. Generování ZASTAVENO.")
    if not data.get("dluznik", {}).get("adresa_dorucovaci"):
        errors.append("GATE §142a: chybí dluznik.adresa_dorucovaci — výzva se zasílá na adresu "
                      "pro doručování, případně poslední známou adresu. Bez ní nárok na náklady padá.")
    if not data.get("lhuta_slovy"):
        # dopočítat z čísla: '7' -> 'sedmi (7) dnů' nechává AI; fallback prostý
        data["lhuta_slovy"] = f"{lhuta} dnů" if isinstance(lhuta, int) else None
        if not data["lhuta_slovy"]:
            errors.append("lhuta_slovy chybí (např. 'sedmi (7) dnů')")
    warnings.append("PŘIPOMENUTÍ §142a: výzvu je nutné ODESLAT nejméně 7 dnů PŘED podáním žaloby "
                    "a uchovat doklad o odeslání (doporučeně / datová schránka).")
    return errors, warnings


def gate_plna_moc(data: dict) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    rozsah = (data.get("rozsah_zmocneni") or "").lower()
    if not rozsah:
        errors.append("rozsah_zmocneni chybí — plná moc bez rozsahu je nepoužitelná")
    if any(k in rozsah for k in ("katastr", "vklad", "nemovit")):
        if not data.get("overeny_podpis"):
            warnings.append("GATE katastr: plná moc k úkonům vůči katastru nemovitostí vyžaduje "
                            "ÚŘEDNĚ OVĚŘENÝ podpis zmocnitele — nastavuji overeny_podpis=true.")
            data["overeny_podpis"] = True
    return errors, warnings


GATES = {
    "predzalobni-vyzva": gate_predzalobni,
    "plna-moc": gate_plna_moc,
}


def main() -> int:
    if len(sys.argv) != 4:
        print(__doc__)
        return 2
    vzor_dir, data_path, out_dir = (Path(a) for a in sys.argv[1:4])
    vzor_name = vzor_dir.name
    tpl_path = vzor_dir / f"{vzor_name}.docx"
    if not tpl_path.exists():
        print(f"Šablona {tpl_path} neexistuje.")
        return 2
    data = json.loads(data_path.read_text(encoding="utf-8"))
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    data.setdefault("advokat", cfg["advokat"])
    data.setdefault("rok", str(date.today().year))

    gate = GATES.get(vzor_name)
    warnings = []
    if gate:
        errors, warnings = gate(data)
        if errors:
            print("GATE SELHAL — dokument NEBYL vygenerován:")
            for e in errors:
                print(f"  ✗ {e}")
            return 1

    out_dir.mkdir(parents=True, exist_ok=True)
    tpl = DocxTemplate(str(tpl_path))
    tpl.render(data)
    out = out_dir / f"{vzor_name}-navrh.docx"
    tpl.save(str(out))
    print(f"  ✓ {out}")
    for w in warnings:
        print(f"  ⚠ {w}")
    print("\nHOTOVO — návrh ke kontrole advokátem, ne finální dokument.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
