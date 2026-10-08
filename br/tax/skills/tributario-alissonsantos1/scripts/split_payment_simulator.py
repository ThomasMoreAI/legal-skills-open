#!/usr/bin/env python3
"""
Simulador de Impacto do Split Payment — Reforma Tributária EC 132/2023
Compara fluxo de caixa no modelo atual vs. split payment por canal de pagamento.
Autor: Alisson Santos — github.com/AlissonSantos1/brasil-legal-skills
Copyright (c) 2026 Alisson Santos. Licença MIT.
"""
__author__ = "Alisson Santos"
__copyright__ = "Copyright (c) 2026 Alisson Santos"
__license__ = "MIT"
__source__ = "https://github.com/AlissonSantos1/brasil-legal-skills"

import argparse

# ---------------------------------------------------------------------------
# Tabelas tributárias
# ---------------------------------------------------------------------------

# Simples Nacional — alíquotas efetivas aproximadas por Anexo/faixa
# (usado apenas como referência para o regime atual)
SIMPLES_ALIQ = {
    1: 0.040,   # Comércio — Anexo I
    2: 0.045,   # Indústria — Anexo II
    3: 0.060,   # Serviços geral — Anexo III
    4: 0.045,   # Construção/limpeza — Anexo IV
    5: 0.155,   # TI/publicidade — Anexo V
}

# Alíquotas PIS+COFINS por regime (atual)
PIS_COFINS = {
    "simples":   0.000,   # já dentro do DAS
    "presumido": 0.0365,  # cumulativo
    "real":      0.0925,  # não-cumulativo
    "mei":       0.000,
}

# ICMS médio estimado por regime (simplificado)
ICMS_EST = {
    "simples":   0.000,   # dentro do DAS
    "presumido": 0.120,
    "real":      0.120,
    "mei":       0.000,
}

# ISS médio (serviços)
ISS_EST = {
    "simples":   0.000,
    "presumido": 0.040,
    "real":      0.040,
    "mei":       0.000,
}

# ---------------------------------------------------------------------------
# Split payment — projeção de alíquotas por fase (EC 132/2023 + LC 214/2025)
# ---------------------------------------------------------------------------

FASES_SPLIT = {
    2026: {"cbs": 0.009, "ibs": 0.001, "nota": "Ano-teste — recolhimento DISPENSADO"},
    2027: {"cbs": 0.018, "ibs": 0.002, "nota": "Início efetivo — alíquotas reduzidas"},
    2028: {"cbs": 0.040, "ibs": 0.010, "nota": "Transição acelerada"},
    2029: {"cbs": 0.060, "ibs": 0.020, "nota": "PIS/COFINS reduzem proporcionalmente"},
    2031: {"cbs": 0.080, "ibs": 0.100, "nota": "ICMS/ISS reduzem proporcionalmente"},
    2033: {"cbs": 0.088, "ibs": 0.177, "nota": "Plena vigência — estimativa Fazenda"},
}

# Taxa de split por canal (% do pagamento que passa pelo sistema financeiro)
SPLIT_TAXA_CANAL = {
    "pix":    1.00,   # 100% interceptado pelo Banco Central
    "cartao": 1.00,   # 100% interceptado pela adquirente
    "boleto": 1.00,   # 100% interceptado pelo banco emissor
    "dinheiro": 0.00, # autodeclaração — empresa recolhe normalmente
}

# Prazo médio de recolhimento no modelo atual (dias)
PRAZO_RECOLHIMENTO_ATUAL = {
    "simples":   30,
    "presumido": 25,
    "real":      20,
    "mei":       30,
}

# ---------------------------------------------------------------------------
# Cálculos
# ---------------------------------------------------------------------------

def aliquota_atual(regime: str, atividade: str, anexo: int) -> float:
    """Alíquota total aproximada de impostos sobre receita no modelo atual."""
    if regime == "simples":
        return SIMPLES_ALIQ.get(anexo, 0.06)
    elif regime == "mei":
        return 0.0
    elif regime == "presumido":
        base = PIS_COFINS["presumido"]
        if atividade == "servico":
            return base + ISS_EST["presumido"]
        else:
            return base + ICMS_EST["presumido"]
    else:  # real
        base = PIS_COFINS["real"]
        if atividade == "servico":
            return base + ISS_EST["real"]
        else:
            return base + ICMS_EST["real"]


def split_efetivo(
    faturamento: float,
    pix_pct: float,
    cartao_pct: float,
    boleto_pct: float,
    dinheiro_pct: float,
    cbs: float,
    ibs: float,
) -> dict:
    """Calcula quanto é retido pelo split e quanto chega para a empresa."""
    aliq_split = cbs + ibs
    total_pct = pix_pct + cartao_pct + boleto_pct + dinheiro_pct

    retido = 0.0
    por_canal = {}
    for canal, pct in [("pix", pix_pct), ("cartao", cartao_pct),
                        ("boleto", boleto_pct), ("dinheiro", dinheiro_pct)]:
        receita_canal = faturamento * (pct / 100)
        retido_canal = receita_canal * aliq_split * SPLIT_TAXA_CANAL[canal]
        recebido_canal = receita_canal - retido_canal
        por_canal[canal] = {
            "receita": receita_canal,
            "retido": retido_canal,
            "recebido": recebido_canal,
            "pct": pct,
        }
        retido += retido_canal

    recebido_total = faturamento - retido
    return {
        "retido_total": retido,
        "recebido_total": recebido_total,
        "aliquota_efetiva_split": (retido / faturamento) if faturamento else 0,
        "por_canal": por_canal,
    }


def calcular_float_atual(
    faturamento: float,
    aliq: float,
    prazo_dias: int,
    custo_capital_aa: float = 0.12,
) -> dict:
    """Valor financeiro do float (imposto que fica na empresa por prazo_dias)."""
    imposto_mensal = faturamento * aliq
    custo_dia = custo_capital_aa / 365
    valor_float = imposto_mensal * custo_dia * prazo_dias
    return {
        "imposto_mensal": imposto_mensal,
        "prazo_dias": prazo_dias,
        "valor_float": valor_float,
        "custo_capital_aa_pct": custo_capital_aa * 100,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description=f"Simulador Split Payment — Reforma Tributária 2026 | {__author__} | {__source__}"
    )
    parser.add_argument("--faturamento", type=float, required=True,
                        help="Faturamento mensal bruto (R$)")
    parser.add_argument("--regime", choices=["mei","simples","presumido","real"],
                        required=True, help="Regime tributário atual")
    parser.add_argument("--atividade", choices=["comercio","servico","industria"],
                        default="servico", help="Atividade principal (padrão: servico)")
    parser.add_argument("--anexo", type=int, choices=[1,2,3,4,5], default=3,
                        help="Anexo do Simples Nacional (padrão: 3 — serviços gerais)")
    parser.add_argument("--pix",      type=float, default=60,
                        help="Percentual recebido via Pix (padrão: 60%%)")
    parser.add_argument("--cartao",   type=float, default=30,
                        help="Percentual recebido via cartão (padrão: 30%%)")
    parser.add_argument("--boleto",   type=float, default=5,
                        help="Percentual recebido via boleto (padrão: 5%%)")
    parser.add_argument("--dinheiro", type=float, default=5,
                        help="Percentual recebido em dinheiro/TED (padrão: 5%%)")
    parser.add_argument("--custo-capital", type=float, default=12.0,
                        help="Custo de capital anual %% (padrão: 12%%)")
    parser.add_argument("--ano", type=int, choices=[2026,2027,2028,2029,2031,2033],
                        default=2027, help="Ano de referência para alíquotas split (padrão: 2027)")
    args = parser.parse_args()

    w = 70
    fat = args.faturamento
    pix = args.pix
    cartao = args.cartao
    boleto = args.boleto
    dinheiro = args.dinheiro
    custo_cap = args.custo_capital / 100

    # Validação soma %
    soma = pix + cartao + boleto + dinheiro
    if abs(soma - 100) > 0.5:
        print(f"\n⚠️  A soma dos percentuais de pagamento ({soma:.0f}%) deve ser 100%.")
        print("    Ajuste os valores de --pix, --cartao, --boleto e --dinheiro.")
        return

    print(f"\n{'='*w}")
    print(f"  SIMULADOR DE SPLIT PAYMENT — REFORMA TRIBUTÁRIA EC 132/2023")
    print(f"{'='*w}")
    print(f"  Faturamento mensal:  R$ {fat:,.2f}")
    print(f"  Regime:              {args.regime.upper()}" +
          (f" — Anexo {args.anexo}" if args.regime == "simples" else ""))
    print(f"  Atividade:           {args.atividade}")
    print(f"  Canais:              Pix {pix:.0f}% · Cartão {cartao:.0f}%"
          f" · Boleto {boleto:.0f}% · Dinheiro {dinheiro:.0f}%")
    print(f"  Ano referência:      {args.ano}")

    # --- Modelo atual ---
    aliq = aliquota_atual(args.regime, args.atividade, args.anexo)
    prazo = PRAZO_RECOLHIMENTO_ATUAL[args.regime]
    float_info = calcular_float_atual(fat, aliq, prazo, custo_cap)

    print(f"\n  {'─'*68}")
    print(f"  MODELO ATUAL")
    print(f"  {'─'*68}")
    print(f"  Alíquota efetiva estimada:   {aliq*100:.1f}%")
    print(f"  Imposto recolhido/mês:       R$ {float_info['imposto_mensal']:,.2f}")
    print(f"  Prazo para recolher:         {prazo} dias")
    print(f"  Valor do float (benefício):  R$ {float_info['valor_float']:,.2f}/mês")
    print(f"  (custo de capital {args.custo_capital:.0f}% a.a. aplicado aos {prazo} dias de float)")

    # --- Split payment ---
    fase = FASES_SPLIT.get(args.ano, FASES_SPLIT[2027])
    cbs, ibs = fase["cbs"], fase["ibs"]
    split = split_efetivo(fat, pix, cartao, boleto, dinheiro, cbs, ibs)

    print(f"\n  {'─'*68}")
    print(f"  SPLIT PAYMENT — ANO {args.ano}")
    print(f"  {fase['nota']}")
    print(f"  {'─'*68}")
    print(f"  CBS: {cbs*100:.1f}%  |  IBS: {ibs*100:.1f}%  |  Total split: {(cbs+ibs)*100:.1f}%")
    print(f"\n  Por canal de pagamento:")
    print(f"  {'Canal':<12} {'% receb':>7}  {'Receita':>12}  {'Retido split':>14}  {'Chega para vc':>14}")
    print(f"  {'─'*66}")
    for canal, d in split["por_canal"].items():
        if d["pct"] > 0:
            label = canal.capitalize()
            print(f"  {label:<12} {d['pct']:>6.0f}%  R$ {d['receita']:>10,.2f}"
                  f"  R$ {d['retido']:>12,.2f}  R$ {d['recebido']:>12,.2f}")

    print(f"\n  TOTAL:")
    print(f"  Faturamento bruto:           R$ {fat:,.2f}")
    print(f"  Retido pelo split:           R$ {split['retido_total']:,.2f}  "
          f"({split['aliquota_efetiva_split']*100:.1f}% do faturamento)")
    print(f"  Recebido pela empresa:       R$ {split['recebido_total']:,.2f}")

    # --- Impacto no capital de giro ---
    perda_float = float_info["valor_float"]
    imposto_split_mensal = split["retido_total"]
    imposto_atual_mensal = float_info["imposto_mensal"]

    print(f"\n  {'─'*68}")
    print(f"  IMPACTO NO CAPITAL DE GIRO")
    print(f"  {'─'*68}")

    if args.ano == 2026:
        print(f"\n  ✅ 2026 é ano-teste: CBS/IBS são destacados na nota, mas NÃO são recolhidos.")
        print(f"     Impacto real no fluxo de caixa: R$ 0,00")
        print(f"     Use este ano para se preparar para 2027.")
    else:
        delta_caixa = imposto_split_mensal - imposto_atual_mensal

        if delta_caixa > 0:
            print(f"\n  Você passará a pagar R$ {delta_caixa:,.2f}/mês a MAIS em tributos")
            print(f"  (alíquota nova CBS+IBS > regime atual para este perfil)")
        else:
            print(f"\n  Diferença de alíquota: R$ {abs(delta_caixa):,.2f}/mês a menos em tributos")
            print(f"  (alíquota nova CBS+IBS < regime atual — tendência benéfica)")

        print(f"\n  Perda do float (dinheiro que ficava na empresa antes de pagar):")
        print(f"  R$ {perda_float:,.2f}/mês (equivale a capital de giro que precisará repor)")

        necessidade_giro = imposto_split_mensal + perda_float
        print(f"\n  Necessidade de capital de giro adicional estimada:")
        print(f"  R$ {necessidade_giro:,.2f}/mês  |  R$ {necessidade_giro*12:,.2f}/ano")

        print(f"\n  Recomendações:")
        if necessidade_giro > fat * 0.05:
            print(f"  ⚠️  ALTO IMPACTO — {necessidade_giro/fat*100:.1f}% do faturamento em capital de giro")
            print(f"     → Renegociar prazos com fornecedores")
            print(f"     → Considerar linha de crédito de giro")
            print(f"     → Revisar pricing considerando custo de capital")
        else:
            print(f"  ✅ IMPACTO MODERADO — {necessidade_giro/fat*100:.1f}% do faturamento")
            print(f"     → Ajuste de fluxo de caixa deve ser suficiente")

        # Ajuste de preço sugerido
        ajuste_preco = (necessidade_giro / fat) * 100
        print(f"\n  Ajuste de preço para neutralizar o impacto: +{ajuste_preco:.2f}%")
        preco_atual = 1000
        preco_novo = preco_atual * (1 + ajuste_preco / 100)
        print(f"  Exemplo: serviço de R$ 1.000 → R$ {preco_novo:,.2f} com o ajuste")

    # --- Projeção 2026-2033 ---
    print(f"\n  {'─'*68}")
    print(f"  PROJEÇÃO ANUAL (split retido por ano, mesmo faturamento)")
    print(f"  {'─'*68}")
    print(f"  {'Ano':<6}  {'CBS':>6}  {'IBS':>6}  {'Split total':>11}  {'Retido/mês':>12}  Status")
    print(f"  {'─'*66}")
    for ano, f in sorted(FASES_SPLIT.items()):
        s = split_efetivo(fat, pix, cartao, boleto, dinheiro, f["cbs"], f["ibs"])
        marcador = " ◄" if ano == args.ano else ""
        dispensado = " (dispensado)" if ano == 2026 else ""
        print(f"  {ano:<6}  {f['cbs']*100:>5.1f}%  {f['ibs']*100:>5.1f}%"
              f"  {(f['cbs']+f['ibs'])*100:>9.1f}%"
              f"  R$ {s['retido_total']:>10,.2f}{dispensado}{marcador}")

    print(f"\n{'='*w}")
    print("\n⚠️  Projeções baseadas em estimativas do Ministério da Fazenda e LC 214/2025.")
    print("    Alíquotas definitivas serão fixadas em lei complementar.")
    print("    Consulte seu contador para planejamento tributário personalizado.")
    print(f"\n  brasil-legal-skills · {__author__} · {__source__}")


if __name__ == "__main__":
    main()
