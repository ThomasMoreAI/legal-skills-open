<!--
TEMPLATE: Model Card (publicado em /transparencia/ia)
=======================================================
Skill: lgpd-compliance (Parte 3)
Saída: <projeto>/transparencia/ia/{provedor}-{modelo}.md
Renderizado em: /transparencia/ia/{provedor}-{modelo}

Cumpre EU AI Act art. 50 + LGPD art. 20 + PL 2338 (quando virar lei).
Tradução do "model card" técnico pro leigo brasileiro.

Placeholders: {{...}}
-->

# {{PROVEDOR}} {{MODELO}}: Como usamos no {{APP_NOME}}

**Última atualização:** {{DATA_ATUALIZACAO}}

---

## Em 1 frase

Usamos **{{MODELO}}** da {{PROVEDOR}} pra **{{FINALIDADE_RESUMIDA}}** no {{APP_NOME}}.

## O que esse modelo é (sem juridiquês)

{{DESCRICAO_LEIGA}}

> Ex: "Programa que aprendeu a escrever lendo muito texto da internet. Recebe seu pedido em português e devolve uma resposta gerada palavra a palavra. Não tem opinião própria; só estatística sobre o que humanos já escreveram."

## O que ela faz BEM neste app

- {{EXEMPLO_BOM_1}}
- {{EXEMPLO_BOM_2}}
- {{EXEMPLO_BOM_3}}

## O que ela faz MAL (limitações reais)

- **Alucina:** pode inventar fatos com aparência de certeza. Confirme dados importantes em fonte oficial.
- {{LIMITACAO_2}}
- {{LIMITACAO_3}}

## Onde NÃO usar

- **Diagnóstico médico ou recomendação de tratamento.** Para isso, procure um médico.
- **Parecer jurídico ou decisão judicial.** Procure um advogado.
- **Decisão financeira (investimento, crédito).** Procure um profissional certificado.
- {{OUTRO_LIMITE}}

## Dados que enviamos ao modelo

Quando você usa esta feature, **enviamos ao {{PROVEDOR}}**:

- {{DADO_1}}, ex: "o texto que você digita no campo X"
- {{DADO_2}}, ex: "o anexo que você envia"
- {{DADO_3}}, ex: "histórico recente da conversa (últimas 10 mensagens)"

**NÃO enviamos:**
- {{NAO_ENVIADO_1}}, ex: "seu CPF, e-mail e telefone (removidos antes do envio via Microsoft Presidio)"
- {{NAO_ENVIADO_2}}

## Política do provedor sobre seus dados

| | |
|---|---|
| **Treinamento de modelo** | {{TREINAMENTO}}, ex: "Anthropic NÃO treina inputs/outputs da API com nossos dados." |
| **Retenção pelo provedor** | {{RETENCAO_PROVEDOR}}, ex: "7 dias (Anthropic API, desde 14/09/2025)" |
| **País de processamento** | {{PAIS}}, ex: "EUA" |
| **Base legal pra transferência internacional** | {{BASE_TRANSFERENCIA}}, ex: "SCC ANPD (Res. 19/2024)" |
| **Link pra política do provedor** | [{{LINK_POLITICA}}]({{LINK_POLITICA}}) |
| **Link pro system card oficial** | [{{LINK_SYSTEM_CARD}}]({{LINK_SYSTEM_CARD}}) |

## Decisão automatizada?

{{#IF DECISAO_AUTO}}

**Sim**, esta feature toma decisões automatizadas que podem afetar seus interesses (LGPD art. 20).

- **Tipo de decisão:** {{TIPO_DECISAO}}
- **Critérios principais:** {{CRITERIOS}}
- **Você tem direito a:**
  - Receber explicação dos critérios usados.
  - Solicitar **revisão humana** clicando em "Contestar esta decisão" ao lado do output.
  - SLA de resposta: **15 dias úteis** (regime geral) ou **30 dias** (se ATPP).
- **Canal:** [/decisoes/contestar](/decisoes/contestar) ou {{DPO_CONTATO}}

{{ELSE}}

**Não**, esta feature é apenas auxiliar. As decisões finais são suas. Não tomamos decisões automatizadas sobre você usando esta IA.

{{/IF}}

## Quando esse modelo foi treinado

- **Cutoff de conhecimento:** {{CUTOFF}}, ex: "janeiro/2026"
- **Implicação:** eventos posteriores podem não estar refletidos nas respostas.

## Vieses conhecidos

{{VIESES_CONHECIDOS}}

> Ex: "Modelos de linguagem treinados majoritariamente em inglês podem ter desempenho desigual entre dialetos do português. Estamos monitorando."

## Como reportar erro ou viés

- **Thumbs down** no próprio output já registra feedback.
- **Reporte detalhado:** {{DPO_CONTATO}}
- **Reclamação à ANPD:** [gov.br/anpd/peticao-de-titular](https://www.gov.br/anpd/pt-br/canais_atendimento/cidadao/peticao-de-titular)

## Continuidade

Se a {{PROVEDOR}} ficar indisponível, esta feature será desativada e você verá aviso na tela.
Trabalhamos com fallback configurável (LiteLLM / Vercel AI SDK) pra minimizar interrupções.

## Histórico de versões deste model card

| Versão | Data | Mudanças |
|---|---|---|
| 1.0 | {{DATA_ATUALIZACAO}} | Versão inicial |
