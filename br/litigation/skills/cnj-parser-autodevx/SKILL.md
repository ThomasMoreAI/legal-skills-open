---
name: cnj-parser-autodevx
title: Parser de Número CNJ
description: Valida, normaliza e extrai componentes de números de processos judiciais brasileiros no formato CNJ (NNNNNNN-DD.AAAA.J.TT.OOOO). Use quando receber números de processo em formatos variados (com ou sem máscara, colados de sistemas diferentes), precisar validar dígitos verificadores, identificar tribunal, instância e órgão julgador, ou preparar dados para consulta em APIs judiciais (DataJud, e-SAJ, PJe, Escavador).
author: autodevx
author_url: https://github.com/autodevx/legal-skills/tree/main/skills/cnj-parser
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# Parser de Número CNJ

## Formato oficial

O número unificado de processos judiciais segue a Resolução CNJ nº 65/2008:

```
NNNNNNN-DD.AAAA.J.TT.OOOO
│         │     │ │  └── Órgão julgador (4 dígitos)
│         │     │ └───── Tribunal (2 dígitos)
│         │     └─────── Justiça (1 dígito)
│         └───────────── Ano de distribuição (4 dígitos)
│         └───────────── Dígitos verificadores (2 dígitos)
└─────────────────────── Número sequencial (7 dígitos)
```

## Comportamento esperado

### Input aceito
- Número com máscara: `0002150-34.2023.8.13.0024`
- Número sem máscara: `00021503420238130024`
- Número com espaços ou caracteres extras: `0002150-34.2023.8.13.0024 (TJMG)`
- Lote de números (lista, planilha, texto livre com múltiplos processos)

### Passos de processamento

1. **Normalizar**: remover tudo que não é dígito
2. **Validar tamanho**: deve resultar em exatamente 20 dígitos
3. **Segmentar**: separar nos campos NNNNNNN, DD, AAAA, J, TT, OOOO
4. **Validar dígito verificador**: algoritmo módulo 97 (Resolução CNJ 65/2008)
5. **Enriquecer**: identificar segmento de justiça, tribunal e formatar

### Algoritmo de validação (módulo 97)

```python
# Dois passos conforme Resolução CNJ 65/2008
r1 = int(nnnnnnn) % 97
r2 = int(f"{r1:02d}{aaaa}{j}{tt}") % 97
dv_calculado = 98 - (int(f"{r2:02d}{oooo}") % 97)
valido = (dv_calculado == int(dd))
```

### Mapa de segmentos de justiça (campo J)

| J | Segmento |
|---|----------|
| 1 | Supremo Tribunal Federal |
| 2 | Conselho Nacional de Justiça |
| 3 | Superior Tribunal de Justiça |
| 4 | Justiça Federal (TRFs 1-6) |
| 5 | Justiça do Trabalho (TRTs 1-24) |
| 6 | Justiça Eleitoral (TREs) |
| 7 | Justiça Militar da União |
| 8 | Justiça dos Estados e DF (TJs) |
| 9 | Justiça Militar Estadual |

### Mapa de tribunais (campo TT para J=8 — Justiça Estadual)

| TT | Tribunal |
|----|----------|
| 01 | TJAC | 02 | TJAL | 03 | TJAP | 04 | TJAM |
| 05 | TJBA | 06 | TJCE | 07 | TJDF | 08 | TJES |
| 09 | TJGO | 10 | TJMA | 11 | TJMT | 12 | TJMS |
| 13 | TJMG | 14 | TJPA | 15 | TJPB | 16 | TJPR |
| 17 | TJPE | 18 | TJPI | 19 | TJRJ | 20 | TJRN |
| 21 | TJRS | 22 | TJRO | 23 | TJRR | 24 | TJSC |
| 25 | TJSE | 26 | TJSP | 27 | TJTO |

### Output padrão (processo único)

```json
{
  "input_original": "0002150-34.2023.8.13.0024",
  "valido": true,
  "numero_formatado": "0002150-34.2023.8.13.0024",
  "componentes": {
    "sequencial": "0002150",
    "digito_verificador": "34",
    "ano": "2023",
    "justica_codigo": "8",
    "justica_nome": "Justiça dos Estados e DF",
    "tribunal_codigo": "13",
    "tribunal_sigla": "TJMG",
    "orgao_julgador": "0024"
  },
  "erro": null
}
```

### Output para lote

Ao receber múltiplos números:
1. Extrair todos os padrões de 20 dígitos do texto (com ou sem máscara)
2. Validar cada um individualmente
3. Retornar tabela consolidada com status de cada número
4. Destacar inválidos com causa específica do erro

Formato tabela:
```
| # | Número CNJ | Válido | Tribunal | Ano | Erro |
```

## Limites

- Não consulta APIs externas (DataJud, PJe, eSAJ) — apenas parse local
- Não infere dados além do que o número contém
- Mapa de tribunais pode não cobrir novos TRFs (ex: TRF-6 criado em 2022)

## Script auxiliar

Ver `scripts/cnj_validator.py` para implementação Python completa com
suporte a batch processing e output JSON/CSV.
