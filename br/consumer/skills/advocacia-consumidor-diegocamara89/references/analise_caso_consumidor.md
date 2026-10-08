# Metodologia de Análise do Caso Consumerista

---

## Etapa 1 — Triagem Inicial

Antes de qualquer análise, responder às quatro perguntas fundamentais:

```
1. Existe relação de consumo? (consumidor + fornecedor + produto/serviço)
2. O prazo está em dia? (prescrição/decadência — art. 26/27, CDC)
3. Há prova mínima do fato? (ao menos um documento)
4. O dano é concreto e demonstrável?
```

Se qualquer resposta for negativa → alertar o usuário **antes** de prosseguir.

---

## Etapa 2 — Mapeamento Completo do Caso

### 2.1 Identificação das Partes

**Consumidor (autor):**
```
- Pessoa física ou jurídica?
- Destinatário final do produto/serviço? (essencial para caracterizar relação de consumo)
- É vulnerável? (idoso, pessoa com deficiência, hipossuficiente técnico)
  → Vulnerabilidade agrava a conduta do fornecedor e pode elevar os danos morais
```

**Fornecedor (réu):**
```
- Quem é o responsável direto? (fabricante, importador, distribuidor, varejista)
- Há solidariedade passiva? (arts. 12 e 18, CDC)
  → Incluir todos os responsáveis solidários como réus aumenta as chances de execução
- O fornecedor é pessoa jurídica de grande porte?
  → Maior poder econômico justifica valor mais elevado de dano moral (caráter pedagógico)
```

**Cadeia de Fornecimento — Mapa de Solidariedade:**
```
Fabricante/Importador → Distribuidor → Varejista → CONSUMIDOR
     (art. 12, CDC)         (art. 13, CDC)

Regra: O consumidor pode acionar QUALQUER elo da cadeia.
Estratégia: acionar o de maior porte OU o mais fácil de executar.
```

### 2.2 Cronologia dos Fatos

Construir linha do tempo completa:

```
DATA         — EVENTO                        — DOCUMENTO DE PROVA
XX/XX/XXXX  — Contratação do serviço       — Contrato / boleto
XX/XX/XXXX  — Entrega do produto           — NF / comprovante de recebimento
XX/XX/XXXX  — Descoberta do vício/dano     — Print / foto / laudo
XX/XX/XXXX  — Reclamação ao fornecedor     — Protocolo / e-mail / print
XX/XX/XXXX  — Resposta (ou silêncio)       — E-mail / print / ausência
XX/XX/XXXX  — Dano consumado               — Comprovante de prejuízo
XX/XX/XXXX  — Data de hoje                 — Marco para cálculo de prazo
```

**Verificação de prazo a partir da cronologia:**
```
Data do dano/vício: XX/XX/XXXX
Prazo aplicável: [ ] 30 dias  [ ] 90 dias  [ ] 5 anos
Prazo expira em: XX/XX/XXXX
Status: [ ] DENTRO DO PRAZO  [ ] ⚠️ PRESTES A VENCER  [ ] ❌ PRESCRITO/DECAÍDO
```

### 2.3 Classificação do Problema

Identificar com precisão o tipo de violação:

| Categoria | Descrição | Base Legal | Prazo |
|-----------|-----------|------------|-------|
| Fato do produto | Acidente de consumo — produto causou dano pessoal ou material | Art. 12, CDC | Prescrição 5 anos |
| Fato do serviço | Acidente de consumo — serviço causou dano | Art. 14, CDC | Prescrição 5 anos |
| Vício do produto | Produto impróprio, inadequado, sem funcionar | Art. 18, CDC | Decadência 30/90 dias |
| Vício do serviço | Serviço mal executado, inadequado | Art. 20, CDC | Decadência 30/90 dias |
| Prática abusiva | Cláusula abusiva, cobrança indevida, publicidade enganosa | Arts. 39–51, CDC | Prescrição 5 anos |
| Negativação indevida | Inscrição em SPC/Serasa sem dívida legítima | Art. 43, CDC | Prescrição 5 anos |
| Negativa de cobertura | Plano de saúde / seguro que recusa o que deve cobrir | Art. 51, CDC | Prescrição 5 anos |
| Dado pessoal | Vazamento, uso indevido de dados | LGPD, Arts. 42–44 | Verificar |

---

## Etapa 3 — Inventário de Provas

Para cada documento fornecido pelo cliente, registrar:

```
DOCUMENTO: [nome/descrição]
TIPO: [ ] Contrato  [ ] NF/recibo  [ ] Print  [ ] Protocolo  [ ] Laudo
      [ ] E-mail  [ ] Foto  [ ] Extrato  [ ] Outro
PROVA: O que este documento demonstra?
VINCULAÇÃO: A qual alegação da peça se conecta?
SUFICIÊNCIA: [ ] Suficiente  [ ] Complementa outro  [ ] Insuficiente — precisa de mais
```

**Matriz de provas mínimas por tipo de caso:**

| Caso | Prova mínima necessária | Prova ideal |
|------|------------------------|-------------|
| Produto defeituoso | NF de compra + foto/descrição do defeito | + Laudo técnico |
| Serviço mal executado | Contrato + NF + descrição do problema | + Orçamento de reparo |
| Cobrança indevida | Extrato / fatura com a cobrança | + Protocolo de reclamação |
| Negativação indevida | Print da consulta no bureau | + Ausência de contrato/dívida |
| Negativa de cobertura | Contrato do plano + negativa por escrito | + Relatório médico |
| Não entrega de produto | NF + rastreamento sem entrega | + Print do site |

---

## Etapa 4 — Análise de Viabilidade e Estratégia

### 4.1 Viabilidade da Ação

```
FORÇA DO CASO:
[ ] Forte   — fatos claros, provas sólidas, jurisprudência consolidada
[ ] Médio   — fatos claros, provas parciais, jurisprudência existe mas varia
[ ] Fraco   — fatos controvertidos, provas frágeis, tese não consolidada
[ ] Inviável — prazo vencido, ausência de relação de consumo, sem prova
```

Se o caso for **fraco ou inviável** → informar o cliente antes de redigir qualquer peça.

### 4.2 Escolha do Rito e Foro

```
CÁLCULO DO VALOR:
  Dano material: R$ _______
  Dano moral:    R$ _______
  Total:         R$ _______

RITO:
[ ] JEC (até 40 SM = R$ _______ em [mês/ano])
    → Vantagem: gratuidade, rapidez, sem honorários em 1º grau
    → Desvantagem: sem perícia complexa, limite de valor

[ ] Vara Cível Comum
    → Quando: valor > 40 SM, caso complexo, réu no exterior
    → Honorários em caso de derrota (risco ao cliente)

FORO:
[ ] Domicílio do consumidor (art. 101, I, CDC — regra geral)
[ ] Local do dano (quando mais conveniente)
[ ] Foro de eleição do contrato → arguir nulidade (art. 51, IV, CDC)
```

### 4.3 Estratégia Pré-Processual

Avaliar se vale tentar resolução antes da ação:

```
[ ] Notificação extrajudicial
    → Constituir o fornecedor em mora
    → Prazo para resposta: 15 dias (razoável)
    → Usar como prova de tentativa de resolução amigável

[ ] Reclamação ao PROCON
    → Gratuita, rápida para casos simples
    → Gera registro que pode ser usado como prova
    → Não interrompe prescrição (atenção ao prazo)

[ ] Reclamação no consumidor.gov.br
    → Plataforma federal — empresas geralmente respondem
    → Gera prova de contato e posição do fornecedor

[ ] Ação judicial direta
    → Quando o prazo é curto ou o fornecedor é reconhecidamente omisso
```

---

## Etapa 5 — Identificação de Argumentos Adicionais

Verificar se o caso comporta argumentos de reforço:

**Inversão do ônus da prova (art. 6º, VIII, CDC):**
- Requerer sempre quando o consumidor é hipossuficiente técnico
- Requerer quando a prova está em poder do fornecedor
- Exemplos: logs de sistema, gravações de atendimento, dados internos

**Tutela de urgência (art. 300, CPC):**
- Urgência: risco de dano grave e de difícil reparação
- Evidência: direito líquido e certo com documentos que afastem a controvérsia
- Casos típicos: corte de serviço essencial, negativa de cobertura médica urgente,
  bloqueio indevido de conta bancária, negativação ativa gerando dano em curso

**Desconsideração da personalidade jurídica (art. 28, CDC):**
- Padrão do CDC: mais amplo que o do CC — basta abuso, excesso de poder, infração legal,
  fato ou ato ilícito, violação de estatutos, falência, estado de insolvência,
  encerramento irregular ou quando a personalidade for obstáculo ao ressarcimento
- Usar quando há suspeita de encerramento irregular ou esvaziamento patrimonial

**Dano moral coletivo:**
- Aplicável quando a conduta do fornecedor atinge um grupo determinável
- Legitimidade: MP, Defensoria, associações (ação coletiva)
- Não usar em ação individual

---

## Etapa 6 — Resumo Executivo do Caso

Antes de iniciar a redação, produzir internamente:

```
RESUMO DO CASO

Partes:
  Consumidor: [nome]
  Fornecedor: [razão social]

Problema: [descrição em 2 linhas]

Classificação: [fato/vício de produto/serviço / prática abusiva / outro]

Prazo: [dentro / atenção / vencido]

Provas disponíveis:
  - [documento 1]: prova [o quê]
  - [documento 2]: prova [o quê]

Danos:
  Material: R$ [valor] — provado por [documento]
  Moral: R$ [valor] — fundamentado em [jurisprudência STJ]
  Total: R$ [valor]

Rito: [JEC / Vara Cível]
Foro: [comarca]

Peça a ser elaborada: [tipo]

Estratégia: [argumentos principais / pedidos / tutela de urgência?]
```

Este resumo é o briefing que o Orquestrador usa para acionar o Agente 1 com os temas certos de jurisprudência.
