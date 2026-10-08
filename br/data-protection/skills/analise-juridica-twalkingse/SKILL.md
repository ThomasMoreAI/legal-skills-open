---
name: analise-juridica-twalkingse
title: Análise Jurídica de Técnica Investigativa (Ação H)
description: Mapear uma técnica OSINT específica contra a legislação brasileira aplicável (LGPD, Marco Civil, CP, Lei 12.850, Lei 14.155, CPP 158-A, CPC 369) e classificar como 🟢 passivo, 🟡 ativo com autorização ou 🔴 invasivo. Corresponde à Ação H do system prompt v1.0. Use quando o usuário perguntar "qual autorização preciso para X?", "posso usar Y sem ordem judicial?", "essa técnica é legal?". Orientativo — nunca substitui assessoria jurídica institucional.
author: TWalkingSE
author_url: https://github.com/TWalkingSE/osint-sentinel/tree/main/.github/skills/analise-juridica
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
---

# Análise Jurídica de Técnica Investigativa (Ação H)

## Quando usar

- Usuário quer saber quais autorizações legais aplicam a uma técnica OSINT específica
- Complementa `/planejar-investigacao` (autorizações necessárias) e `/tecnica-especifica` (gatilhos de autorização)
- Antes de decisão sobre representar por quebra de sigilo, pedir decisão judicial ou prosseguir passivo

## Protocolo

### 1. Identifique a técnica específica

Se ambígua, peça detalhe. Não analise técnica genérica.

### 2. Mapeie contra a legislação brasileira

Dispositivos mais frequentes (não exaustivo — consulte `references/23-frameworks-metodologias.md` e `25-processo-penal-cadeia-custodia.md`):

| Dispositivo | Aplicação típica |
|---|---|
| **LGPD (Lei 13.709/2018)** art. 7º | Bases legais de tratamento de dados pessoais |
| LGPD art. 7º VI | Execução de políticas públicas / finalidade investigativa |
| LGPD art. 14 | Dados de crianças/adolescentes — proteção reforçada |
| LGPD art. 46 | Segurança no tratamento (breach handling) |
| **Marco Civil da Internet (Lei 12.965/2014)** art. 7º IX | Dado publicamente disponível (base para OSINT passivo) |
| MCI art. 10–11 | Preservação de registros de conexão |
| MCI art. 13–15 | Retenção de logs pelo ISP; identificação via ofício |
| MCI art. 22 | Judicial para conteúdo de comunicações |
| **Lei de Interceptação (Lei 9.296/1996)** | Interceptação telefônica / telemática — judicial |
| **Código Penal art. 154-A** | Invasão de dispositivo informático — crime |
| **CP art. 171 §2º-A / Lei 14.155/2021** | Fraude eletrônica |
| **CP art. 180** | Receptação (dado de breach ilícito) |
| **CP art. 307** | Falsa identidade (sockpuppet sem amparo) |
| **Lei 12.850/2013 art. 10-A** | Agente infiltrado / sockpuppet digital (autorização judicial) |
| **Lei 13.869/2019** | Abuso de autoridade |
| **CPP art. 158-A a 158-F** | Cadeia de custódia |
| **CPC art. 369** | Admissibilidade de prova digital |
| **ECA art. 240–241** | Pornografia infantil (orientação = Protocolo CSAM) |

### 3. Classifique a técnica

| Classe | Autorização | Exemplos |
|---|---|---|
| 🟢 **OSINT passivo** | Nenhuma específica (base: MCI art. 7º IX) | WHOIS, Wayback, Shodan lookup sem scan, busca em redes sociais públicas |
| 🟡 **OSINT ativo / com implicação** | IPL/PIC + compatibilidade LGPD | PIX reverso, WhatsApp Web em alvo, painel legítimo com CNPJ, recuperação de senha parcial |
| 🔴 **Invasivo / restrito** | Autorização judicial específica | Interceptação, acesso a conteúdo de comunicação, sockpuppet ativo, reconhecimento facial em plataforma, scraping contra TOS |

### 4. Cite dispositivo aplicável

Nunca invente jurisprudência específica. Pode citar doutrina e legislação; evitar afirmações categóricas sobre decisões de tribunais sem fonte.

### 5. Disclaimer obrigatório ao final

## Formato de saída obrigatório

```markdown
# ⚖️ ANÁLISE JURÍDICA — [Nome da técnica]

**Fonte técnica:** `references/NN-*.md §Y.Z`
**Classificação:** 🟢 passivo / 🟡 ativo (requer autorização) / 🔴 invasivo (requer decisão judicial)

---

## 1. Descrição da técnica
[O que a técnica faz, do ponto de vista técnico — 1 parágrafo]

## 2. Bens jurídicos potencialmente afetados
- [Privacidade / sigilo de comunicações / dado pessoal / honra / etc.]

## 3. Legislação aplicável

| Dispositivo | Aplicação ao caso | Interpretação |
|---|---|---|
| [Lei/artigo] | [como incide] | [suporte à técnica / impõe autorização / veda sem respaldo] |
| ... |

## 4. Autorização mínima necessária

- **Se 🟢:** nenhuma específica, mas:
  - Documentar motivação investigativa
  - Compatibilidade LGPD (finalidade legítima + proporcionalidade)
  - Preservação via cadeia de custódia

- **Se 🟡:** 
  - Procedimento formal (IPL, PIC, representação)
  - Motivação explícita da proporcionalidade
  - Compatibilidade LGPD art. 7º VI
  - Documentação no procedimento

- **Se 🔴:**
  - Decisão judicial específica citando a técnica
  - Fundamentação da autoridade representante
  - Prazo de execução delimitado

## 5. Riscos de uso indevido
- [Qual crime pode configurar se aplicada sem respaldo — ex: art. 154-A CP, art. 307 CP]
- [Consequências administrativas — ex: abuso de autoridade]
- [Risco probatório — prova ilícita (CPP 157), ilicitude por derivação]

## 6. Recomendação
[Operacional — "prosseguir em modo passivo com documentação X", "representar por decisão judicial citando art. Y", "não prosseguir, redirecionar para via Z"]

---

## ⚠️ Disclaimer

Esta análise é **orientativa**, baseada em legislação vigente até a data da KB
carregada (v3.0/2026). Decisões sobre amparo legal devem ser **validadas pelo
responsável processual** (delegado, promotor, juiz) e pela **assessoria
jurídica da instituição**.

O OSINT-Sentinel **não substitui** advogado, promotor, delegado ou assessoria
jurídica.
```

## Regras

- **NUNCA** cite jurisprudência específica sem que esteja documentada na KB. Prefira legislação vigente + doutrina genérica.
- **NUNCA** afirme "a técnica X é 100% legal" ou "proibida em qualquer cenário" — sempre condicionada ao respaldo processual.
- **SEMPRE** inclua disclaimer orientativo ao final.
- **Para técnicas 🔴:** deixar explícito que prosseguir sem decisão judicial pode gerar **prova ilícita** (CPP 157) e responsabilização pessoal.
- **Para dados de crianças/adolescentes:** citar **ECA + LGPD art. 14** em conjunto.
- **Para CSAM:** ativar Protocolo CSAM de `AGENTS.md` — não é análise jurídica, é interrupção.
- **Para painéis clandestinos:** citar `references/27-paineis-clandestinos-persecucao.md` — operador de painel clandestino é **alvo** da persecução, não fonte.
