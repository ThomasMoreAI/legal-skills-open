#!/usr/bin/env python3
"""
Calculadora do Simples Nacional — LC 123/2006
Autor: Alisson Santos — github.com/AlissonSantos1/brasil-legal-skills
Copyright (c) 2026 Alisson Santos. Licença MIT.
"""
__author__ = "Alisson Santos"
__copyright__ = "Copyright (c) 2026 Alisson Santos"
__license__ = "MIT"
__source__ = "https://github.com/AlissonSantos1/brasil-legal-skills"

import argparse


# Tabelas Simples Nacional 2026 — (limite_faixa, aliquota_nominal, valor_deduzir)
ANEXOS = {
    1: {  # Comércio
        "nome": "Anexo I — Comércio",
        "faixas": [
            (180_000, 0.04, 0),
            (360_000, 0.073, 5_940),
            (720_000, 0.095, 13_860),
            (1_800_000, 0.107, 22_500),
            (3_600_000, 0.143, 87_300),
            (4_800_000, 0.19, 378_000),
        ],
    },
    3: {  # Serviços (maioria)
        "nome": "Anexo III — Serviços",
        "faixas": [
            (180_000, 0.06, 0),
            (360_000, 0.112, 9_360),
            (720_000, 0.135, 17_640),
            (1_800_000, 0.16, 35_640),
            (3_600_000, 0.21, 125_640),
            (4_800_000, 0.33, 648_000),
        ],
    },
    5: {  # Serviços profissionais (TI, publicidade)
        "nome": "Anexo V — Serviços Profissionais",
        "faixas": [
            (180_000, 0.155, 0),
            (360_000, 0.18, 4_500),
            (720_000, 0.195, 9_900),
            (1_800_000, 0.205, 17_100),
            (3_600_000, 0.23, 62_100),
            (4_800_000, 0.305, 540_000),
        ],
    },
}


def calcular_das(receita_mensal: float, rbt12: float, anexo: int) -> dict:
    """Calcula o DAS do Simples Nacional."""
    tabela = ANEXOS.get(anexo)
    if not tabela:
        return {"erro": f"Anexo {anexo} não encontrado. Use 1, 3 ou 5."}

    # Determina faixa pelo RBT12
    aliquota_nominal = 0
    valor_deduzir = 0
    faixa_atual = 0
    for i, (limite, aliq, ded) in enumerate(tabela["faixas"]):
        if rbt12 <= limite:
            aliquota_nominal = aliq
            valor_deduzir = ded
            faixa_atual = i + 1
            break
    else:
        return {"erro": "Faturamento acima do limite do Simples Nacional (R$ 4,8 mi)"}

    # Alíquota efetiva
    aliquota_efetiva = (rbt12 * aliquota_nominal - valor_deduzir) / rbt12
    das = receita_mensal * aliquota_efetiva

    return {
        "anexo": tabela["nome"],
        "faixa": faixa_atual,
        "rbt12": rbt12,
        "receita_mensal": receita_mensal,
        "aliquota_nominal": aliquota_nominal,
        "aliquota_efetiva": aliquota_efetiva,
        "das_mensal": das,
        "das_anual_estimado": das * 12,
    }


def main():
    parser = argparse.ArgumentParser(description="Calculadora Simples Nacional")
    parser.add_argument("--receita", type=float, required=True, help="Receita do mês (R$)")
    parser.add_argument("--rbt12", type=float, help="Receita bruta últimos 12 meses (padrão: receita × 12)")
    parser.add_argument("--anexo", type=int, default=3, choices=[1, 3, 5], help="Anexo do Simples (1, 3 ou 5)")
    args = parser.parse_args()

    rbt12 = args.rbt12 or args.receita * 12
    r = calcular_das(args.receita, rbt12, args.anexo)

    if "erro" in r:
        print(f"\n❌ Erro: {r['erro']}")
        return

    print("\n" + "=" * 52)
    print("  SIMPLES NACIONAL — DAS MENSAL")
    print("=" * 52)
    print(f"  Anexo:              {r['anexo']}")
    print(f"  Faixa:              {r['faixa']}ª faixa")
    print(f"  RBT12:              R$ {r['rbt12']:>10,.2f}")
    print(f"  Receita do mês:     R$ {r['receita_mensal']:>10,.2f}")
    print(f"  Alíquota nominal:   {r['aliquota_nominal']*100:.1f}%")
    print(f"  Alíquota efetiva:   {r['aliquota_efetiva']*100:.2f}%")
    print("  " + "-" * 38)
    print(f"  DAS MENSAL:         R$ {r['das_mensal']:>10,.2f}")
    print(f"  DAS anual estimado: R$ {r['das_anual_estimado']:>10,.2f}")
    print("=" * 52)
    print("\n⚠️  Cálculo estimado. Consulte seu contador.")
    print(f"\n  brasil-legal-skills · {__author__} · {__source__}")


if __name__ == "__main__":
    main()
