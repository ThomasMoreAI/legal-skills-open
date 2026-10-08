"""Deterministic monetary recalculations — Phase 5 Step 5.3.

Runs at the very end of the agents pipeline, after juriscan-sintetizador
and scripts/confidence_rules.py. Reads ``auditor_findings`` and for each
entry with ``tipo == "RECALCULO_NECESSARIO"`` applies the appropriate
deterministic formula. Everything here uses ``decimal.Decimal`` to avoid
the rounding traps of binary floats on money.

Two recalculations are supported in this version:

1. **Lei 14.905/2024 (juros mistos)** — from ``2024-08-30`` onward the
   legal interest rate changed from 1% a.m. (Código Civil art. 406) to
   SELIC - IPCA. Condemnations whose update period straddles that date
   must be split in two and each half computed independently. We do NOT
   have a SELIC/IPCA time series bundled with the repo; we emit the
   **structure** (two periods with periods, taxas, and placeholders) so
   that the practitioner or a specialized module can fill in the rates
   without touching the pipeline plumbing. The first period is fully
   computable because 1% a.m. is deterministic.

2. **Honorários após reforma parcial** — when a lower-court condemnation
   is reformed on appeal and the appellate decision is silent about the
   honorarios base, this script emits the alternative calculations for
   both possible bases (original vs. reformed) so the practitioner sees
   the quantitative delta behind the art. 1022 CPC omission.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


LEI_14905_CUTOVER = date(2024, 8, 30)
LEGAL_RATE_BEFORE_CUTOVER = Decimal("0.01")  # 1% per month, CC art. 406
MONEY_PRECISION = Decimal("0.01")


class FinalizeError(Exception):
    pass


def _to_decimal(value: object) -> Decimal:
    if isinstance(value, Decimal):
        return value
    if isinstance(value, (int, float)):
        return Decimal(str(value))
    if isinstance(value, str):
        cleaned = value.replace("R$", "").strip().replace(".", "").replace(",", ".")
        return Decimal(cleaned)
    raise FinalizeError(f"cannot coerce to Decimal: {value!r}")


def _parse_date(value: str | date) -> date:
    if isinstance(value, date):
        return value
    return date.fromisoformat(value)


def _money(d: Decimal) -> Decimal:
    return d.quantize(MONEY_PRECISION, rounding=ROUND_HALF_UP)


def _months_between(start: date, end: date) -> Decimal:
    """Whole months + fractional month based on days in the final month.

    Matches the convention used in civil monetary updates: cada mês cheio
    conta inteiro, e o mês parcial é fracionado por dias corridos.
    """
    if end < start:
        return Decimal("0")
    years = end.year - start.year
    months = end.month - start.month
    full_months = years * 12 + months
    # Fractional remainder based on day delta.
    if end.day < start.day:
        full_months -= 1
        # Compute leftover as a fraction of the final month length.
        # Approximate the final-month length as 30 days.
        day_delta = (end - date(end.year, end.month, 1)).days + (
            30 - start.day + 1
        )
        fractional = Decimal(day_delta) / Decimal(30)
    else:
        day_delta = end.day - start.day
        fractional = Decimal(day_delta) / Decimal(30)
    return Decimal(full_months) + fractional


# ---------- Lei 14.905 ----------

@dataclass
class Lei14905Period:
    de: str
    ate: str
    taxa: str
    base: str
    juros: str | None
    valor_com_juros: str | None
    note: str = ""


def recalcular_juros_lei_14905(
    base_value: object,
    data_inicio: str | date,
    data_fim: str | date,
) -> dict:
    """Split the interest period around 2024-08-30 and compute period 1 fully.

    Returns a dict with ``periodo_1`` (fully computable at 1% a.m.) and
    ``periodo_2`` (structurally present but with ``valor_com_juros=None``
    because SELIC - IPCA is not bundled here).
    """
    base = _to_decimal(base_value)
    start = _parse_date(data_inicio)
    end = _parse_date(data_fim)
    if end <= start:
        raise FinalizeError(f"data_fim must be after data_inicio: {start}..{end}")
    if base <= 0:
        raise FinalizeError(f"base must be positive, got {base}")

    periods: list[Lei14905Period] = []

    if end <= LEI_14905_CUTOVER:
        # Entirely before the cutover — simple case.
        months = _months_between(start, end)
        juros = base * LEGAL_RATE_BEFORE_CUTOVER * months
        periods.append(Lei14905Period(
            de=start.isoformat(),
            ate=end.isoformat(),
            taxa="1% a.m. (CC art. 406 — redação anterior à Lei 14.905/2024)",
            base=str(_money(base)),
            juros=str(_money(juros)),
            valor_com_juros=str(_money(base + juros)),
            note="Sem incidência da Lei 14.905/2024 — período totalmente anterior a 30/08/2024.",
        ))
    elif start >= LEI_14905_CUTOVER:
        # Entirely after the cutover — structure only, rates not bundled.
        periods.append(Lei14905Period(
            de=start.isoformat(),
            ate=end.isoformat(),
            taxa="SELIC - IPCA (Lei 14.905/2024)",
            base=str(_money(base)),
            juros=None,
            valor_com_juros=None,
            note="Regime pós-Lei 14.905/2024. Requer série histórica SELIC/IPCA para o cálculo final.",
        ))
    else:
        # Straddles the cutover — split.
        p1_end = LEI_14905_CUTOVER
        p1_months = _months_between(start, p1_end)
        p1_juros = base * LEGAL_RATE_BEFORE_CUTOVER * p1_months
        base_after = base + p1_juros
        periods.append(Lei14905Period(
            de=start.isoformat(),
            ate=p1_end.isoformat(),
            taxa="1% a.m. (CC art. 406 — redação anterior)",
            base=str(_money(base)),
            juros=str(_money(p1_juros)),
            valor_com_juros=str(_money(base_after)),
            note="Período anterior à Lei 14.905/2024.",
        ))
        periods.append(Lei14905Period(
            de=p1_end.isoformat(),
            ate=end.isoformat(),
            taxa="SELIC - IPCA (Lei 14.905/2024)",
            base=str(_money(base_after)),
            juros=None,
            valor_com_juros=None,
            note="Período pós-Lei 14.905/2024. Requer série histórica SELIC/IPCA.",
        ))

    return {
        "tipo": "JUROS_LEI_14905",
        "base_original": str(_money(base)),
        "data_inicio": start.isoformat(),
        "data_fim": end.isoformat(),
        "cutover": LEI_14905_CUTOVER.isoformat(),
        "periods": [p.__dict__ for p in periods],
    }


# ---------- Honorários após reforma ----------

def recalcular_honorarios(
    percentual: object,
    base_original: object,
    base_reformada: object,
) -> dict:
    """Compute both candidate honorarios amounts after a partial reform.

    When the appellate decision is silent about the base of honorarios,
    practitioners need the quantitative delta to justify embargos de
    declaração by omission (CPC art. 1022).
    """
    pct = _to_decimal(percentual)
    if pct > Decimal("1"):
        # Accept 15 for 15% as well as 0.15.
        pct = pct / Decimal("100")
    base_orig = _to_decimal(base_original)
    base_ref = _to_decimal(base_reformada)
    hon_original = base_orig * pct
    hon_reformada = base_ref * pct
    return {
        "tipo": "HONORARIOS_APOS_REFORMA",
        "percentual": f"{(pct * 100).quantize(Decimal('0.01'))}%",
        "base_original": str(_money(base_orig)),
        "base_reformada": str(_money(base_ref)),
        "honorarios_sobre_base_original": str(_money(hon_original)),
        "honorarios_sobre_base_reformada": str(_money(hon_reformada)),
        "delta": str(_money(abs(hon_original - hon_reformada))),
        "note": (
            "O acórdão é silente sobre a base de cálculo dos honorários. "
            "Ambas as bases são plausíveis sem esclarecimento expresso — "
            "cabem embargos de declaração por omissão (CPC art. 1022)."
        ),
    }


# ---------- Top-level apply ----------

def apply_recalculations(analysis: dict) -> dict:
    """Read auditor_findings and emit monetary_recalculations[] in-place."""
    findings = analysis.get("auditor_findings") or []
    recalculations: list[dict] = []

    for f in findings:
        if f.get("tipo") != "RECALCULO_NECESSARIO":
            continue
        fundamento = (f.get("fundamento") or "").lower()
        payload = f.get("payload") or {}
        try:
            if "14.905" in fundamento or "14905" in fundamento:
                recalc = recalcular_juros_lei_14905(
                    base_value=payload.get("base"),
                    data_inicio=payload.get("data_inicio"),
                    data_fim=payload.get("data_fim"),
                )
                recalc["source_finding"] = f.get("fundamento")
                recalculations.append(recalc)
            elif "1022" in fundamento or "honorár" in fundamento or "honorar" in fundamento:
                recalc = recalcular_honorarios(
                    percentual=payload.get("percentual"),
                    base_original=payload.get("base_original"),
                    base_reformada=payload.get("base_reformada"),
                )
                recalc["source_finding"] = f.get("fundamento")
                recalculations.append(recalc)
        except FinalizeError as e:
            recalculations.append({
                "tipo": "ERROR",
                "source_finding": f.get("fundamento"),
                "error": str(e),
            })

    analysis["monetary_recalculations"] = recalculations
    return analysis


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Apply deterministic monetary recalculations to analyzed.json"
    )
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)

    doc = json.loads(Path(args.input).read_text(encoding="utf-8"))
    apply_recalculations(doc)
    Path(args.output).write_text(
        json.dumps(doc, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"[OK] finalize: {len(doc.get('monetary_recalculations') or [])} recálculo(s) aplicado(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
