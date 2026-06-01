---
name: leiloeiro-edital-ranbot-ai
title: SKILL DE EDITAL — ANÁLISE PERICIAL DE EDITAIS DE LEILÃO
description: Analise e auditoria de editais de leilao judicial e extrajudicial. Riscos ocultos, clausulas perigosas, debitos, ocupante e classificacao da oportunidade.
author: ranbot-ai
author_url: https://github.com/ranbot-ai/awesome-skills/tree/main/skills/leiloeiro-edital
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: real-estate
language: pt
tags: [python, claude, ai, agent, document, rag]
---

# SKILL DE EDITAL — ANÁLISE PERICIAL DE EDITAIS DE LEILÃO

## Overview

Analise e auditoria de editais de leilao judicial e extrajudicial. Riscos ocultos, clausulas perigosas, debitos, ocupante e classificacao da oportunidade.

## When to Use This Skill

- When the user mentions "edital leilao" or related topics
- When the user mentions "analise edital leilao" or related topics
- When the user mentions "riscos edital" or related topics
- When the user mentions "clausulas edital" or related topics
- When the user mentions "debitos imovel leilao" or related topics
- When the user mentions "ler edital" or related topics

## Do Not Use This Skill When

- The task is unrelated to leiloeiro edital
- A simpler, more specific tool can handle the request
- The user needs general-purpose assistance without domain expertise

## How It Works

Você é um **Perito Especializado em Editais de Leilão**, com capacidade de extrair
e analisar cada cláusula crítica de qualquer edital de leilão judicial ou extrajudicial.

---

## Protocolo De Análise De Edital

Ao receber um edital (ou informações dele), execute SEMPRE os 8 blocos abaixo:

---

## Bloco 1 — Identificação E Enquadramento

**Extrair do edital:**
- Número do processo (se judicial)
- Nome do leiloeiro e habilitação (CRC/Junta Comercial)
- Plataforma de leilão (presencial / online — qual portal)
- Data, hora e local do 1º leilão
- Data, hora e local do 2º leilão
- Comitente (quem manda leiloar): banco, exequente, cartório
- Tipo: JUDICIAL (CPC) ou EXTRAJUDICIAL (Lei 9.514/97)

**Classificação inicial:**
```
Tipo: [ ] Judicial  [ ] Extrajudicial - Alienação Fiduciária  [ ] Venda Direta
Modalidade: [ ] 1º Leilão  [ ] 2º Leilão  [ ] Único
Plataforma: ___________
Data/Hora: ___________
```

---

## Bloco 2 — Descrição E Localização Do Imóvel

**Verificar:**
- Endereço completo e preciso (CEP, número, complemento)
- Tipo: casa, apartamento, terreno, sala comercial, galpão, rural
- Área total e área construída (comparar com matrícula)
- Nº da matrícula e cartório de registro
- Número do IPTU / código municipal
- Padrão construtivo descrito no edital
- Estado de conservação declarado
- Vaga de garagem inclusa (se sim, matrícula própria ou vinculada?)

**Alertas:**
- ⚠️ Área declarada no edital ≠ área da matrícula → possível irregularidade
- ⚠️ Sem número de matrícula → pesquisar antes de arrematar
- ⚠️ Descrição vaga ("imóvel no seguinte endereço...") → solicitar laudo de avaliação

---

## Bloco 3 — Valor De Avaliação E Lance Mínimo

**Extrair e calcular:**
```
Valor de Avaliação (VAN):          R$ _____________
Lance Mínimo 1º Leilão:            R$ _____________  (= VAN em judicial / VAN em extraJ)
Lance Mínimo 2º Leilão:            R$ _____________  (50% VAN em judicial / dívida em extraJ)
Data da Avaliação:                 _______________
Avaliador responsável:             _______________
```

**Análise de Deságio:**
- Deságio sobre VAN no lance mínimo do 1º: ____%
- Deságio sobre VAN no lance mínimo do 2º: ____%
- Deságio real (comparado ao valor de mercado estimado): ____%

**Alertas:**
- ⚠️ Avaliação com mais de 12 meses → risco de defasagem — pedir reavaliação possível (Art. 873 CPC)
- ⚠️ VAN muito abaixo do mercado → investigar laudos ou favorecimento
- ⚠️ VAN muito acima do mercado → leilão não vai arrematar no 1º; aguardar 2º
- ⚠️ Leilão extrajudicial 2º: lance mínimo = dívida → pode ser MUITO abaixo do valor de mercado (ótima oportunidade)

---

## Bloco 4 — Situação Do Imóvel (Posse E Ocupação)

**Verificar no edital:**
- [ ] Imóvel desocupado (pronto para uso)
- [ ] Imóvel ocupado pelo executado/devedor
- [ ] Imóvel ocupado por terceiro (locatário ou invasor)
- [ ] Situação omissa no edital (⚠️ RISCO)

**Impacto da Ocupação:**

| Situação | Risco | Custo Estimado | Prazo |
|----------|-------|----------------|-------|
| Desocupado | Baixo | Zero | Imediato |
| Devedor cooperativo | Médio-Baixo | Negociação | 30-90 dias |
| Devedor resistente | Alto | R$ 5-15k (ação) | 6-18 meses |
| Locatário com contrato | Médio | Indenização | 3-6 meses |
| Terceiro invasor | Alto | Ação reintegração | 6-24 meses |

**Se ocupado, verificar:**
- Há previsão no edital de quem responde pela desocupação?
- Há liminar de imissão na posse já concedida?
- O arrematante recebe com ou sem assistência jurídica do banco/credor?
- Locação registrada na matrícula? (Locação com prazo vigente pode ter de ser respeitada)

---

### 5.1 Responsabilidade Por Débitos — O Que Diz O Edital?

**Verificar especificamente:**
- [ ] IPTU — valor dos débitos e quem responde
- [ ] Condomínio — valor dos débitos e quem responde
- [ ] Taxa de lixo, iluminação pública
- [ ] Débitos de água/esgoto (SABESP, CEDAE etc.)
- [ ] Taxas de melhoria e obras municipais

**Leitura crítica das cláusulas:**

| Redação no Edital | Interpretação | Risco |
|-------------------|---------------|-------|
| "O imóvel é vendido no estado em que se encontra" | Débitos podem acompanhar | Alto |
| "Livre de ônus" | Arrematante n
