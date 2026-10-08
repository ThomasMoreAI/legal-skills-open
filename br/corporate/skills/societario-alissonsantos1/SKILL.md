---
name: societario-alissonsantos1
title: 🏢 Societário — Empresas e Sociedades
description: Use para abertura de empresa, tipos jurídicos, direitos e deveres de sócios, resolução de conflitos societários, geração de contratos, alvarás, licenças, certidões negativas e análise se vale a pena ter sócio. Ativa em "abrir empresa", "LTDA", "contrato social", "conflito com sócio", "alvará", "certidão negativa".
author: AlissonSantos1
author_url: https://github.com/AlissonSantos1/brasil-legal-skills/tree/main/societario
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: corporate
language: pt
tags: [societario, empresa, ltda, socios, contrato-social, alvara, conflito-societario]
---

# 🏢 Societário — Empresas e Sociedades

> ⚠️ Orientação educativa. Para contratos e conflitos societários, consulte advogado na OAB.

---

## Vale a pena ter sócio?

Antes de escolher o tipo jurídico, orientar o usuário com as perguntas certas:

**Perguntar:**
- O sócio traz capital, conhecimento técnico ou rede de relacionamentos?
- Vocês têm papéis bem definidos e complementares?
- Têm alinhamento de valores e objetivos de longo prazo?
- Já trabalharam juntos antes?
- Como vão resolver desentendimentos?

**Quando sócio FAZ sentido:**
- Aportes financeiros que você não tem
- Expertise técnica que complementa a sua
- Rede de clientes que alavanca o negócio

**Quando sócio NÃO faz sentido:**
- Só para dividir responsabilidade emocional
- Sem papéis claros definidos
- Sem acordo sobre retiradas e lucros

---

## Comparativo dos Tipos de Empresa

| Tipo | Sócios | Faturamento | Responsabilidade | Indicado para |
|------|--------|-------------|-----------------|---------------|
| MEI | 1 | Até R$ 81k/ano | Ilimitada | Autônomo iniciante |
| SLU | 1 | Sem limite | Limitada | Profissional liberal solo |
| LTDA | 2+ (ou 1 unipessoal) | Sem limite | Limitada às cotas | A maioria das empresas |
| SA Fechada | 2+ | Sem limite | Limitada às ações | Grandes operações |
| SA Aberta | Acionistas | Sem limite | Limitada às ações | Capital na bolsa |

**Recomendação geral:**
- Autônomo solo → **SLU** (mais proteção que MEI, sem sócios)
- 2 ou mais pessoas → **LTDA** (mais simples que SA)
- Busca investimento/IPO → **SA**

---

## Direitos e Deveres dos Sócios

### Direitos fundamentais (Código Civil, art. 1.001–1.038)
- Participar dos lucros proporcionalmente às cotas
- Fiscalizar a gestão da empresa
- Votar nas deliberações sociais
- Retirar-se da sociedade (com aviso de 60 dias se prazo indeterminado)
- Preferência na compra de cotas de outro sócio que deseja sair

### Deveres fundamentais
- Integralizar o capital subscrito
- Não concorrer com a sociedade (cláusula de não concorrência)
- Lealdade à sociedade
- Sigilo das informações da empresa

### Responsabilidade dos sócios
- Em regra: **limitada** ao valor das cotas (LTDA)
- Exceções onde o sócio responde pessoalmente:
  - Fraude ou abuso de direito (desconsideração da personalidade jurídica)
  - Dívidas trabalhistas (solidariedade em alguns casos)
  - Débitos fiscais com dolo ou fraude

---

## Resolução de Conflitos Societários

### Etapas recomendadas (do mais simples ao mais formal):

1. **Conversa direta** — tentar resolver internamente
2. **Mediação** — mediador externo, solução consensual
3. **Arbitragem** — mais rápida que Judiciário, decisão vinculante
4. **Ação judicial** — Vara Cível ou Empresarial

### Cláusulas preventivas no contrato social:
- **Quórum para deliberações** (ex: 75% para decisões estratégicas)
- **Drag-along:** sócio majoritário pode obrigar minoritário a vender junto
- **Tag-along:** minoritário tem direito de vender nas mesmas condições
- **Vesting:** cotas liberadas gradualmente ao longo do tempo
- **Buy or Sell (Shot-gun):** um sócio propõe preço, o outro decide se compra ou vende

---

## Geração de Contratos Societários

Ao pedir para gerar um contrato, coletar:
- Nome(s) e qualificação dos sócios (nome, CPF, endereço, estado civil)
- Nome empresarial desejado
- Objeto social (atividades)
- Capital social e % de cada sócio
- Quem será o administrador
- Sede e endereço
- Prazo (recomendado: indeterminado)

Tipos de contratos gerados:
- **Contrato Social LTDA**
- **Contrato de Sócio Investidor** (Mútuo Conversível)
- **Acordo de Sócios** (shareholders agreement)
- **Distrato Social** (encerramento)

---

## Regularização: Alvarás, Licenças e Certidões

### Alvarás obrigatórios
| Alvará | Órgão | Quando obrigatório |
|--------|-------|-------------------|
| Alvará de Funcionamento | Prefeitura | Sempre |
| Vigilância Sanitária | ANVISA/Estadual | Alimentos, saúde, farmácias |
| Corpo de Bombeiros (AVCB) | CBPMESP/Estadual | Imóveis com público |
| Licença Ambiental | IBAMA/Estadual | Atividades com impacto ambiental |

### Certidões Negativas essenciais
- **CND Federal** — Receita Federal (impostos federais)
- **CND FGTS** — Caixa Econômica Federal
- **CND Estadual** — SEFAZ do estado (ICMS)
- **CND Municipal** — Prefeitura (ISS)
- **Certidão de Distribuição** — Tjustiça (ações judiciais)

> As certidões são exigidas em licitações, financiamentos e contratos com o governo.

---

## Scripts disponíveis

```bash
# Recomendar melhor tipo de empresa
python3 scripts/tipo_societario.py --faturamento 200000 --socios 2 --atividade servicos

# Calcular distribuição de cotas e lucros
python3 scripts/distribuicao_lucros.py --lucro 50000 --cotas "60,40"

# Gerar checklist de abertura por estado
python3 scripts/checklist_abertura.py --tipo ltda --estado SP
```
