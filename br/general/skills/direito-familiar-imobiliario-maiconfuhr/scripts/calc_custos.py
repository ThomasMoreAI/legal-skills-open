#!/usr/bin/env python3
"""
Calculadora de Custos — Direito Imobiliário e de Família (Brasil, 2026).

Estimativa interativa de ITBI, ITCMD, emolumentos e honorários para casos
de compra/venda, doação, inventário, divórcio e usucapião.

IMPORTANTE: todas as estimativas são FAIXAS. Valores reais variam por
município (ITBI), estado (ITCMD), tabela cartorial estadual (emolumentos)
e perfil do caso. Confirme sempre com advogado e cartório local.

Base legal vigente em maio/2026:
- ITBI: municipal, 2-3% típico
- ITCMD: estadual, alíquota varia por UF (LC 227/2026 obriga progressividade
  até 8%, mas leis estaduais publicadas em 2026 só valem a partir de 01/01/2027)
- Emolumentos: tabela do TJ estadual, varia muito
- Honorários: livremente negociados (referencial OAB local)

Uso:
    python calc_custos.py
"""

from __future__ import annotations

from dataclasses import dataclass


# Alíquotas ITCMD vigentes em maio/2026 por UF (até a edição/eficácia das
# leis estaduais de adaptação à LC 227/2026 a partir de 01/01/2027).
# Fontes: legislação estadual consolidada; verificar sempre lei vigente.
ITCMD_POR_UF: dict[str, tuple[float, float, str]] = {
    # UF: (min%, max%, observação)
    "AC": (2.0, 4.0, "Progressiva"),
    "AL": (2.0, 4.0, "Progressiva"),
    "AP": (3.0, 4.0, "Fixa/Progressiva"),
    "AM": (2.0, 4.0, "Progressiva"),
    "BA": (3.5, 8.0, "Progressiva"),
    "CE": (2.0, 8.0, "Progressiva"),
    "DF": (4.0, 6.0, "Progressiva"),
    "ES": (4.0, 4.0, "Fixa 4%"),
    "GO": (2.0, 8.0, "Progressiva"),
    "MA": (3.0, 7.0, "Progressiva"),
    "MT": (2.0, 8.0, "Progressiva"),
    "MS": (3.0, 6.0, "Progressiva"),
    "MG": (5.0, 5.0, "Fixa 5% — adaptação prevista p/ 2027"),
    "PA": (2.0, 4.0, "Progressiva"),
    "PB": (2.0, 8.0, "Progressiva"),
    "PR": (4.0, 4.0, "Fixa 4% — adaptação prevista p/ 2027"),
    "PE": (2.0, 8.0, "Progressiva"),
    "PI": (2.0, 6.0, "Progressiva"),
    "RJ": (4.0, 8.0, "Progressiva"),
    "RN": (3.0, 6.0, "Progressiva"),
    "RS": (3.0, 6.0, "Progressiva (4-8% a partir de 2027)"),
    "RO": (2.0, 4.0, "Progressiva"),
    "RR": (4.0, 4.0, "Fixa"),
    "SC": (1.0, 8.0, "Progressiva"),
    "SP": (4.0, 4.0, "Fixa 4% — PL para progressividade em tramitação"),
    "SE": (2.0, 8.0, "Progressiva"),
    "TO": (2.0, 8.0, "Progressiva"),
}

# ITBI: alíquota média municipal típica (2-3%). Usa faixa.
ITBI_MIN = 0.02
ITBI_MAX = 0.03

# Honorários advocatícios — % indicativo sobre o patrimônio/operação.
HONORARIOS_FAIXAS: dict[str, tuple[float, float]] = {
    "compra_venda": (0.005, 0.02),  # 0.5-2%
    "divorcio_consensual": (0.02, 0.10),  # 2-10% sobre partilha
    "divorcio_litigioso": (0.10, 0.20),  # 10-20%
    "inventario_extrajudicial": (0.05, 0.10),  # 5-10% sobre espólio
    "inventario_judicial": (0.10, 0.15),  # 10-15%
    "usucapiao_extrajudicial": (0.02, 0.08),  # 2-8%, mais valor fixo
    "usucapiao_judicial": (0.05, 0.10),
    "doacao": (0.005, 0.02),
    "reurb_e": (0.01, 0.05),
    "retificacao_matricula": (0.005, 0.03),
}

# Emolumentos — faixa indicativa sobre o valor da operação (varia muito por UF).
EMOLUMENTOS_FAIXAS: dict[str, tuple[float, float]] = {
    "compra_venda": (0.005, 0.025),  # escritura + registro
    "divorcio_consensual": (0.003, 0.015),  # escritura
    "divorcio_litigioso": (0.005, 0.02),  # custas judiciais + registro
    "inventario_extrajudicial": (0.005, 0.025),  # escritura
    "inventario_judicial": (0.01, 0.025),  # custas + registro
    "usucapiao_extrajudicial": (0.003, 0.015),  # ata + registro
    "usucapiao_judicial": (0.01, 0.02),  # custas + registro
    "doacao": (0.005, 0.02),
    "reurb_e": (0.0, 0.005),  # taxa reduzida
    "retificacao_matricula": (0.001, 0.005),
}


@dataclass
class Estimativa:
    """Resultado consolidado de uma simulação de custos."""

    item: str
    valor_min: float
    valor_max: float
    observacao: str = ""

    def formatado(self) -> str:
        return (
            f"  {self.item:<32} R$ {self.valor_min:>12,.2f} — "
            f"R$ {self.valor_max:>12,.2f}"
            + (f"   ({self.observacao})" if self.observacao else "")
        )


def parse_uf(s: str) -> str:
    s = s.strip().upper()
    if s not in ITCMD_POR_UF:
        raise ValueError(
            f"UF inválida: {s}. Use sigla de 2 letras (ex.: SP, RJ, MG)."
        )
    return s


def parse_valor(s: str) -> float:
    s = s.strip().replace("R$", "").replace(".", "").replace(",", ".").strip()
    return float(s)


def parse_uf_input(prompt: str) -> str:
    while True:
        try:
            return parse_uf(input(prompt))
        except ValueError as e:
            print(f"  ⚠️  {e}")


def parse_valor_input(prompt: str) -> float:
    while True:
        try:
            v = parse_valor(input(prompt))
            if v <= 0:
                raise ValueError("Valor deve ser positivo.")
            return v
        except ValueError as e:
            print(f"  ⚠️  {e}")


def calc_itbi(valor: float) -> Estimativa:
    return Estimativa(
        item="ITBI (municipal)",
        valor_min=valor * ITBI_MIN,
        valor_max=valor * ITBI_MAX,
        observacao="2-3% típico — confirme com a prefeitura",
    )


def calc_itcmd(valor: float, uf: str) -> Estimativa:
    min_aliq, max_aliq, obs = ITCMD_POR_UF[uf]
    return Estimativa(
        item=f"ITCMD ({uf})",
        valor_min=valor * (min_aliq / 100),
        valor_max=valor * (max_aliq / 100),
        observacao=obs,
    )


def calc_emolumentos(valor: float, tipo: str) -> Estimativa:
    if tipo not in EMOLUMENTOS_FAIXAS:
        return Estimativa("Emolumentos", 0, 0, "tipo desconhecido")
    f_min, f_max = EMOLUMENTOS_FAIXAS[tipo]
    return Estimativa(
        item="Emolumentos cartoriais",
        valor_min=valor * f_min,
        valor_max=valor * f_max,
        observacao="tabela do TJ estadual — varia",
    )


def calc_honorarios(valor: float, tipo: str) -> Estimativa:
    if tipo not in HONORARIOS_FAIXAS:
        return Estimativa("Honorários advocatícios", 0, 0, "tipo desconhecido")
    f_min, f_max = HONORARIOS_FAIXAS[tipo]
    return Estimativa(
        item="Honorários advocatícios",
        valor_min=valor * f_min,
        valor_max=valor * f_max,
        observacao="negociável; pode ser fixo ou % ou por êxito",
    )


def imprimir_estimativas(titulo: str, estimativas: list[Estimativa]) -> None:
    print()
    print("=" * 90)
    print(f"  {titulo}")
    print("=" * 90)
    print()
    for e in estimativas:
        print(e.formatado())
    total_min = sum(e.valor_min for e in estimativas)
    total_max = sum(e.valor_max for e in estimativas)
    print()
    print(f"  {'TOTAL ESTIMADO':<32} R$ {total_min:>12,.2f} — R$ {total_max:>12,.2f}")
    print()
    print("  ⚠️  Esses valores são ESTIMATIVAS. Confirme com advogado e cartório local.")
    print("=" * 90)


def menu_principal() -> str:
    print()
    print("╔" + "═" * 88 + "╗")
    print("║  CALCULADORA DE CUSTOS — Direito Imobiliário, Família e Sucessões (Brasil/2026) ║")
    print("╚" + "═" * 88 + "╝")
    print()
    print("  Escolha o tipo de operação:")
    print()
    print("  1.  Compra e venda de imóvel")
    print("  2.  Doação de imóvel")
    print("  3.  Inventário extrajudicial (em cartório)")
    print("  4.  Inventário judicial")
    print("  5.  Divórcio consensual extrajudicial")
    print("  6.  Divórcio consensual judicial")
    print("  7.  Divórcio litigioso")
    print("  8.  Usucapião extrajudicial")
    print("  9.  Usucapião judicial")
    print(" 10.  Retificação de matrícula")
    print(" 11.  REURB-E (regularização específica)")
    print("  0.  Sair")
    print()
    return input("  Opção: ").strip()


def fluxo_compra_venda() -> None:
    print("\n--- Compra e venda de imóvel ---")
    valor = parse_valor_input("  Valor da operação (ex.: 500000 ou 500.000,00): R$ ")
    estimativas = [
        calc_itbi(valor),
        calc_emolumentos(valor, "compra_venda"),
        calc_honorarios(valor, "compra_venda"),
    ]
    imprimir_estimativas(
        f"Compra e venda — valor R$ {valor:,.2f}", estimativas
    )


def fluxo_doacao() -> None:
    print("\n--- Doação de imóvel ---")
    valor = parse_valor_input("  Valor do imóvel: R$ ")
    uf = parse_uf_input("  UF onde está o imóvel (ex.: SP, RJ, MG): ")
    estimativas = [
        calc_itcmd(valor, uf),
        calc_emolumentos(valor, "doacao"),
        calc_honorarios(valor, "doacao"),
    ]
    imprimir_estimativas(
        f"Doação de imóvel — valor R$ {valor:,.2f} ({uf})", estimativas
    )


def fluxo_inventario(extrajudicial: bool) -> None:
    print(f"\n--- Inventário {'extrajudicial' if extrajudicial else 'judicial'} ---")
    valor = parse_valor_input("  Valor TOTAL do patrimônio a inventariar: R$ ")
    uf = parse_uf_input("  UF do falecido (predominante; imóveis em outros estados pagam ITCMD lá): ")
    tipo = "inventario_extrajudicial" if extrajudicial else "inventario_judicial"
    estimativas = [
        calc_itcmd(valor, uf),
        calc_emolumentos(valor, tipo),
        calc_honorarios(valor, tipo),
    ]
    print()
    print("  ⚠️  Atenção: ITCMD deve ser pago em até 60 dias do óbito na maioria")
    print("     dos estados para evitar multa (10-20% sobre o tributo devido).")
    imprimir_estimativas(
        f"Inventário {'extrajudicial' if extrajudicial else 'judicial'} — patrimônio R$ {valor:,.2f} ({uf})",
        estimativas,
    )


def fluxo_divorcio(modalidade: str) -> None:
    print(f"\n--- Divórcio {modalidade.replace('_', ' ')} ---")
    valor = parse_valor_input("  Valor TOTAL do patrimônio comum a partilhar: R$ ")
    torna = parse_valor_input(
        "  Valor de torna (pagamento em dinheiro entre cônjuges; 0 se nenhum): R$ "
    )

    estimativas: list[Estimativa] = []
    if torna > 0:
        estimativas.append(
            Estimativa(
                "ITBI sobre torna",
                torna * ITBI_MIN,
                torna * ITBI_MAX,
                "incide se torna > meação",
            )
        )
    estimativas.append(calc_emolumentos(valor, f"divorcio_{modalidade}"))
    estimativas.append(calc_honorarios(valor, f"divorcio_{modalidade}"))
    imprimir_estimativas(
        f"Divórcio {modalidade.replace('_', ' ')} — patrimônio R$ {valor:,.2f}",
        estimativas,
    )


def fluxo_usucapiao(extrajudicial: bool) -> None:
    print(f"\n--- Usucapião {'extrajudicial' if extrajudicial else 'judicial'} ---")
    valor = parse_valor_input("  Valor estimado do imóvel: R$ ")
    tipo = "usucapiao_extrajudicial" if extrajudicial else "usucapiao_judicial"

    eng_min, eng_max = 1500.0, 15000.0
    estimativas = [
        Estimativa(
            "Levantamento topo/georreferenciamento",
            eng_min,
            eng_max,
            "varia se urbano/rural e por área",
        ),
        calc_emolumentos(valor, tipo),
        calc_honorarios(valor, tipo),
    ]
    print()
    print("  ⚠️  Usucapião não gera tributo (declaratório). Mas custos técnicos")
    print("     (engenheiro/topógrafo) podem ser significativos, sobretudo rural.")
    imprimir_estimativas(
        f"Usucapião {'extrajudicial' if extrajudicial else 'judicial'} — imóvel R$ {valor:,.2f}",
        estimativas,
    )


def fluxo_retificacao() -> None:
    print("\n--- Retificação de matrícula ---")
    valor = parse_valor_input("  Valor de referência do imóvel: R$ ")
    eng_min, eng_max = 1500.0, 8000.0
    estimativas = [
        Estimativa(
            "Levantamento topo + ART/RRT",
            eng_min,
            eng_max,
            "se urbano; rural mais caro",
        ),
        calc_emolumentos(valor, "retificacao_matricula"),
        calc_honorarios(valor, "retificacao_matricula"),
    ]
    imprimir_estimativas("Retificação de matrícula", estimativas)


def fluxo_reurb() -> None:
    print("\n--- REURB-E (regularização específica) ---")
    print("  Obs.: REURB-S (interesse social) é gratuita ao beneficiário.")
    valor = parse_valor_input("  Valor de referência do imóvel/lote: R$ ")
    estimativas = [
        calc_emolumentos(valor, "reurb_e"),
        calc_honorarios(valor, "reurb_e"),
        Estimativa(
            "Estudo técnico + projetos",
            3000.0,
            15000.0,
            "varia por complexidade",
        ),
    ]
    imprimir_estimativas(f"REURB-E — imóvel R$ {valor:,.2f}", estimativas)


def main() -> None:
    print()
    print("  Esta calculadora oferece ESTIMATIVAS de custos com base na")
    print("  legislação brasileira vigente em maio/2026.")
    print()
    print("  Os valores são FAIXAS e podem variar significativamente por")
    print("  município, estado, cartório e perfil específico do caso.")
    print()
    print("  Confirme sempre com advogado e cartório local.")

    while True:
        opcao = menu_principal()
        try:
            if opcao == "0":
                print("\n  Até logo!\n")
                break
            elif opcao == "1":
                fluxo_compra_venda()
            elif opcao == "2":
                fluxo_doacao()
            elif opcao == "3":
                fluxo_inventario(extrajudicial=True)
            elif opcao == "4":
                fluxo_inventario(extrajudicial=False)
            elif opcao == "5":
                fluxo_divorcio("consensual")
            elif opcao == "6":
                fluxo_divorcio("consensual")
            elif opcao == "7":
                fluxo_divorcio("litigioso")
            elif opcao == "8":
                fluxo_usucapiao(extrajudicial=True)
            elif opcao == "9":
                fluxo_usucapiao(extrajudicial=False)
            elif opcao == "10":
                fluxo_retificacao()
            elif opcao == "11":
                fluxo_reurb()
            else:
                print("\n  ⚠️  Opção inválida.")
        except (ValueError, KeyboardInterrupt) as e:
            print(f"\n  ⚠️  {e}")
            continue


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Cancelado pelo usuário.\n")
