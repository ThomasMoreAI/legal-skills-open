---
name: contrato-review-autodevx
title: Revisão de Contratos — Framework BR
description: Analisa contratos brasileiros identificando cláusulas problemáticas, riscos jurídicos e oportunidades de negociação. Use quando precisar fazer due diligence contratual, revisar minutas antes de assinatura, identificar cláusulas abusivas ou desequilibradas, verificar conformidade com CC/2002, CDC, LGPD ou legislação setorial, ou preparar um parecer jurídico estruturado. Aplicável a contratos de prestação de serviços, fornecimento, NDA, locação, licença de software e contratos de trabalho.
author: autodevx
author_url: https://github.com/autodevx/legal-skills/tree/main/skills/contrato-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
sources:
- title: Clausulas Abusivas
  path: references/clausulas-abusivas.md
- title: Contratos Tipicos Br
  path: references/contratos-tipicos-br.md
---

# Revisão de Contratos — Framework BR

## Contexto

Esta skill implementa um framework estruturado de análise contratual conforme legislação brasileira. O objetivo é identificar riscos, cláusulas problemáticas e oportunidades de negociação, gerando um parecer técnico auditável.

## Protocolo de análise

### Fase 1: Identificação do contrato

Antes de qualquer análise, identificar obrigatoriamente:

- **Tipo**: prestação de serviços / compra e venda / locação / NDA / licença software / trabalho / outro
- **Partes**: qualificação completa (PJ/PF, CNPJ/CPF, domicílio)
- **Vigência**: data de início, prazo, condições de renovação (tácita ou expressa)
- **Valor**: preço, forma de remuneração, índice de reajuste
- **Lei aplicável**: se declarada; na omissão, aplicar legislação brasileira

### Fase 2: Checklist de cláusulas críticas

#### Cláusulas essenciais (ausência = risco alto)

- [ ] Objeto claramente definido e delimitado
- [ ] Prazo de vigência + condições de renovação
- [ ] Preço, reajuste (índice + periodicidade) e forma de pagamento
- [ ] Multa por inadimplemento (deve ser bilateral)
- [ ] Condições de rescisão imotivada e prazo de aviso prévio
- [ ] Foro eleito (preferencialmente da sede do contratante mais fraco)
- [ ] Obrigações de cada parte detalhadas (não apenas genéricas)

#### Cláusulas potencialmente abusivas (verificar equilíbrio)

- [ ] Cláusula penal desproporcional
  - B2B: acima de 20% já é questionável
  - CDC (B2C): limite de 2% (art. 52, §1º, CDC)
  - Referência: STJ, REsp 1.119.740/RJ
- [ ] Exclusividade unilateral sem contrapartida financeira proporcional
- [ ] Limitação de responsabilidade que exclua dolo ou culpa grave (nulo — CC art. 422, boa-fé objetiva)
- [ ] Cessão de direitos/obrigações sem consentimento prévio
- [ ] Alteração unilateral de condições essenciais (preço, escopo, prazo)
- [ ] Renúncia antecipada a direitos indisponíveis
- [ ] Cláusula de não-concorrência sem limitação temporal/geográfica
- [ ] Eleição de foro que dificulte acesso à justiça (CDC art. 6º, VIII)
- [ ] Arbitragem imposta em contratos de adesão (questionável se consumidor)

#### Cláusulas LGPD (obrigatório se houver tratamento de dados pessoais)

- [ ] Base legal do tratamento identificada (LGPD art. 7º)
- [ ] Finalidade específica declarada (não genérica)
- [ ] Prazo de retenção definido
- [ ] Responsabilidades Controlador vs. Operador delimitadas (art. 39-40)
- [ ] Subprocessadores: necessidade de autorização prévia
- [ ] Cláusula de incidente: notificação em até 72h (recomendação ANPD)
- [ ] Transferência internacional: verificar adequação ou salvaguardas (art. 33-36)
- [ ] Direitos dos titulares: canal de atendimento definido
- [ ] Término do tratamento: devolução/eliminação de dados ao final do contrato

### Fase 3: Análise de risco por cláusula

Para cada cláusula problemática identificada, estruturar:

```
CLÁUSULA: [número ou título da cláusula]
TEXTO: [transcrever trecho relevante]
PROBLEMA: [descrição objetiva do risco]
FUNDAMENTO LEGAL: [dispositivo — CC art. X / CDC art. Y / LGPD art. Z / Súmula STJ nº W]
RISCO: [BAIXO / MÉDIO / ALTO / CRÍTICO]
IMPACTO: [financeiro / operacional / regulatório / reputacional]
SUGESTÃO DE REDAÇÃO: [texto alternativo proposto]
```

Critérios de classificação de risco:

| Nível | Critério |
|-------|----------|
| **CRÍTICO** | Nulidade absoluta; violação de norma cogente; exposição >R$1M |
| **ALTO** | Desequilíbrio significativo; jurisprudência consolidada contra; exposição financeira relevante |
| **MÉDIO** | Cláusula ambígua; jurisprudência dividida; risco litigioso moderado |
| **BAIXO** | Melhoria recomendável mas não essencial; risco residual |

### Fase 4: Output final

#### 4a. Parecer resumido (para não-jurídicos / gestores)

```
═══════════════════════════════════════════
RESULTADO: APROVADO / APROVADO COM RESSALVAS / REPROVADO

CONTRATO: [tipo e partes]
DATA DA ANÁLISE: [data]
VERSÃO DO DOCUMENTO: [se identificável]

RESUMO EXECUTIVO:
[3-5 linhas descrevendo os principais achados]

PONTOS CRÍTICOS:
1. [problema mais grave]
2. [segundo problema]
3. [terceiro problema]

RECOMENDAÇÃO: [assinar / negociar cláusulas X, Y, Z / não assinar sem alterações]
═══════════════════════════════════════════
```

#### 4b. Relatório técnico completo (para advogado / arquivo)

Estrutura:
1. Dados do contrato (partes, objeto, valor, prazo)
2. Metodologia de análise
3. Análise cláusula por cláusula (apenas as problemáticas)
4. Tabela de riscos consolidada
5. Sugestões de redação alternativa
6. Conclusão e recomendação
7. Ressalvas (skill não substitui consultoria jurídica)

### Fase 5: Pós-análise

Sempre finalizar com:
- Indicação de que a análise é automatizada e deve ser validada por advogado
- Lista de pontos que exigem análise humana especializada (ex: M&A, valor >R$1M)
- Sugestão de próximos passos

## Tipos de contrato — comportamento específico

### Prestação de serviços
- Verificar SLA definido e mensurável
- Verificar propriedade intelectual do produto/entrega
- Verificar cláusula de sigilo (especialmente para TI)

### NDA / Confidencialidade
- Prazo de vigência da obrigação (indefinido é questionável)
- Definição clara do que é "informação confidencial"
- Exceções padrão (domínio público, obrigação legal, pré-conhecimento)
- Penalidade proporcional ao porte das partes

### Licença de software / SaaS
- SLA de uptime e penalidades por descumprimento
- Propriedade dos dados do cliente
- Portabilidade e exportação de dados no término
- Limitação de responsabilidade vs. valor do contrato

### Contrato de trabalho
- Verificar conformidade com CLT
- Cláusula de não-concorrência: máx 2 anos, remuneração compensatória
- Propriedade intelectual: produção durante jornada vs. fora

## Referências

Ler `references/clausulas-abusivas.md` para jurisprudência STJ sobre abusos.
Ler `references/contratos-tipicos-br.md` para cláusulas padrão por tipo.

## Limites desta skill

- Não substitui consultoria jurídica formal
- Contratos acima de R$1M ou operações de M&A exigem advogado especialista
- Contratos internacionais exigem análise de DIPr adicional
- Análise limitada ao texto fornecido (não verifica aditivos, anexos não incluídos)
