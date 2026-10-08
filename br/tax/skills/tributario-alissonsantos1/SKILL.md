---
name: tributario-alissonsantos1
title: 🏛️ Tributário Brasileiro — 2026
description: 'Use para tributação empresarial: Simples Nacional, MEI (abertura de CNPJ, CNAE), Reforma Tributária 2026 (CBS/IBS), PIS/COFINS, ICMS, ISS, emissão de nota fiscal, comparação de regimes. Ativa em "MEI", "CNPJ", "Simples Nacional", "nota fiscal", "CNAE", "reforma tributária", "CBS", "IBS", "regime tributário".'
author: AlissonSantos1
author_url: https://github.com/AlissonSantos1/brasil-legal-skills/tree/main/tributario
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: tax
language: pt
tags: [tributario, simples-nacional, mei, cnpj, cnae, reforma-tributaria, cbs, ibs, nfe]
---

# 🏛️ Tributário Brasileiro — 2026

> ⚠️ Orientação educativa. Não substitui contador registrado no CRC.

---

## Reforma Tributária 2026 — O que muda AGORA

### CBS e IBS (substituem PIS/COFINS e ICMS/ISS gradualmente)
A partir de **1° de janeiro de 2026**, todos os contribuintes devem emitir documentos
fiscais eletrônicos com **destaque individualizado de CBS e IBS** por operação.

**Documentos afetados:**
NF-e · NFC-e · CT-e · NFS-e · NFCom · NF3e · BP-e

**2026 é ano de teste:**
> Quem emitir documentos fiscais conforme as normas vigentes está **dispensado do
> recolhimento** de CBS e IBS neste período de transição.

### PIS/COFINS — Mudanças 2026
- Produtos que tinham **alíquota zero** de PIS/COFINS passaram a ter tributação
  equivalente a **10% da alíquota padrão**
- PIS cumulativo: 0,65% → verificar se seu produto foi afetado
- COFINS cumulativo: 3% → verificar se seu produto foi afetado

### MEI e Autônomos — Nova Obrigação
A partir de **julho de 2026**, MEIs e autônomos contribuintes de CBS/IBS precisam
registrar **CNPJ para fins fiscais** (não vira pessoa jurídica — é apenas cadastro).

---

## Regimes Tributários

### MEI — Microempreendedor Individual
**Limite:** R$ 81.000/ano | **DAS mensal fixo**

| Atividade | Total estimado 2026 |
|-----------|-------------------|
| Comércio | ~R$ 76,90/mês |
| Serviços | ~R$ 80,90/mês |
| Comércio + Serviços | ~R$ 81,90/mês |

**Vedações:** sem sócios · não pode ser sócio de outra empresa · máximo 1 funcionário

**Como abrir MEI:**
1. Acesse [gov.br/mei](https://www.gov.br/mei)
2. Clique em "Formalize-se"
3. Informe CPF e dados pessoais
4. Escolha a atividade pelo **CNAE**
5. CNPJ emitido na hora — gratuito

### Escolhendo o CNAE correto
O CNAE define o anexo do Simples e as obrigações do MEI. Exemplos comuns:

| Atividade | CNAE | Regime MEI |
|-----------|------|-----------|
| Desenvolvimento de software | 6201-5/01 | Serviços |
| Designer gráfico | 7410-2/02 | Serviços |
| Vendas online | 4791-1/00 | Comércio |
| Consultoria | 7020-4/00 | Serviços |
| Barbeiro/Cabeleireiro | 9602-5/01 | Serviços |

> Consulte a lista completa em: [gov.br/mei → Atividades Permitidas](https://www.gov.br/mei)

### Simples Nacional (até R$ 4,8 mi/ano)
**Alíquota efetiva = (RBT12 × Alíquota nominal − Parcela a deduzir) ÷ RBT12**

| Anexo | Atividade principal | Alíquota inicial |
|-------|-------------------|-----------------|
| I | Comércio | 4,0% |
| II | Indústria | 4,5% |
| III | Serviços em geral | 6,0% |
| IV | Construção civil, limpeza | 4,5% |
| V | TI, publicidade, engenharia | 15,5% |

### Lucro Presumido (até R$ 78 mi/ano)
- IRPJ: 15% + 10% adicional sobre lucro presumido
- CSLL: 9%
- Presunção: 8% comércio, 32% serviços

### Lucro Real (acima de R$ 78 mi ou por opção)
- PIS/COFINS não cumulativos: 9,25%
- IRPJ/CSLL sobre lucro contábil ajustado

---

## Emissão de Nota Fiscal

### NF-e (Nota Fiscal Eletrônica — produtos)
1. Ter certificado digital (e-CNPJ A1 ou A3)
2. Cadastrar-se na SEFAZ do estado
3. Usar sistema emissor (DANFE online, NFe.io, ou ERP)
4. Informar: CFOP, NCM, ICMS, IPI, PIS, COFINS
5. Transmitir para a SEFAZ e aguardar autorização

### NFS-e (Nota Fiscal de Serviços — municipal)
1. Acessar o portal da prefeitura do município
2. MEI pode emitir pelo [nfse.gov.br](https://www.nfse.gov.br) (gratuito)
3. Informar: CNAE, valor, tomador, descrição do serviço, ISS

### Quando MEI deve emitir nota:
- **Obrigatório** para pessoa jurídica (CNPJ)
- **Facultativo** para pessoa física (CPF), mas recomendado

---

## Obrigações Acessórias por Regime

| Obrigação | MEI | Simples | Lucro Presumido | Lucro Real |
|-----------|-----|---------|----------------|-----------|
| DAS/DARF mensal | ✅ | ✅ | ✅ | ✅ |
| DASN-SIMEI (anual) | ✅ | — | — | — |
| DEFIS (anual) | — | ✅ | — | — |
| ECD | — | — | ✅ | ✅ |
| ECF | — | — | ✅ | ✅ |
| SPED Fiscal | — | Alguns | ✅ | ✅ |
| DCTF mensal | — | — | ✅ | ✅ |

---

## Scripts disponíveis

```bash
# Calcular DAS Simples Nacional
python3 scripts/simples_nacional.py --receita 25000 --anexo 3

# Calcular DAS MEI
python3 scripts/mei_calculator.py --atividade servicos

# Comparar regimes tributários
python3 scripts/comparar_regimes.py --faturamento 500000 --atividade servicos
```
