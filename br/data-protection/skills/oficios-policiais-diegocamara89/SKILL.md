---
name: oficios-policiais-diegocamara89
title: Oficios Policiais
description: Redacao de oficios de requisicao de dados tecnicos a provedores de internet, aplicativos, bancos e operadoras para instruir procedimentos policiais. Use quando precisar gerar oficio requisitorio para Google, Meta, Apple, Microsoft, Uber, iFood, Mercado Livre, Amazon, Discord, Imgur, bancos, provedores de acesso (ISP) ou operadoras de telefonia, ou quando o usuario pedir "gerar oficio", "oficiar provedor", "requisitar dados", "oficio para banco", "oficio para operadora", ou quando o comando /oficios for invocado. Gera texto puro pronto para colar no PPE, com catalogo completo de pedidos por provedor e fundamentacao legal padronizada.
author: diegocamara89
author_url: https://github.com/diegocamara89/ai-skills-hub/tree/main/all-skills/oficios-policiais
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
sources:
- title: Catalogo Provedores
  path: references/catalogo-provedores.md
---

# Oficios Policiais

Gere oficios de requisicao de dados tecnicos a provedores, com lista de pedidos completa por provedor, fundamentacao legal e formatacao pronta para o PPE.

## Inputs obrigatorios

Antes de gerar, verifique se voce tem:

| Input | Exemplo |
|---|---|
| Numero do procedimento (BO ou IP) | BO 123/2025, IP 456/2024 |
| Provedor destinatario | Google, Uber, Banco X |
| Alvo (dado tecnico) | email, telefone, perfil, IP, CPF |
| Janela de busca (inicio e fim) | 01/01/2025 a 31/12/2025 |
| Email de retorno | email do investigador/cartorio |
| Telefone de contato | telefone/WhatsApp do investigador |
| Tipo penal | estelionato, invasao de dispositivo, etc. |

**Regra**: Se faltar dado critico (BO, crime), pergunte. Se for dedutivel (ex: usuario pediu "Bradesco" e nao tem no catalogo), NAO PARE — aplique roteamento automatico.

## Workflow

### Passo 1 — Validar inputs

Confira o checklist acima. Preencha o que o usuario forneceu e pergunte apenas o que for critico e nao dedutivel.

### Passo 2 — Identificar provedor

Carregue `references/catalogo-provedores.md` e localize o provedor pelo nome ou ID.

**Roteamento automatico (senso critico):**
- Provedor nao encontrado + e um BANCO → use `banco_generico`, substitua o nome
- Provedor nao encontrado + e um ISP/provedor de internet → use `isp_generico`, substitua o nome
- Provedor nao encontrado + e uma OPERADORA de telefonia → use `telefonia_generico`, substitua o nome
- Provedor totalmente desconhecido → informe que nao esta no catalogo e peca os dados manualmente

### Passo 3 — Montar o oficio

Monte o documento nesta ordem exata:

1. **Enderecamento**: "Ao Sr(a). Representante Legal da [NOME_EMPRESA]" + endereco/email juridico do catalogo
2. **LegalHeader**: texto padrao de fundamentacao (ver Boilerplate abaixo)
3. **Contextualizacao**: referencia ao procedimento (BO/IP), tipo penal e identificacao do alvo
4. **RequestList**: lista INTEGRAL de pedidos do provedor, referente ao alvo e janela de busca
5. **ConfidentialityNotice**: aviso de sigilo
6. **DesobedienceThreat**: advertencia sobre crime de desobediencia
7. **LersInstruction**: instrucao de envio via LERS ou email
8. **Prazo e contato**: prazo em dias + email e telefone de retorno

### Passo 4 — Entregar

Entregue o oficio em bloco de codigo, texto puro. Nada mais.

## Regras de execucao

### Copia integral (CRITICO)
- Copie TODOS os itens da RequestList do catalogo, ipsis litteris
- Se a lista tem 11 itens, o oficio TEM 11 itens
- NAO resuma, NAO filtre, NAO omita itens
- Mesmo que o usuario peca apenas "dados cadastrais", inclua a lista completa
- Doutrina: "Pecar pelo Excesso"

### Anti-alucinacao
- NUNCA invente enderecos de email juridico — use apenas o que esta no catalogo
- Se o catalogo nao tiver o provedor, peca os dados ao usuario

### Modo espelho
- Se o usuario fornecer uma RequestList manual, reproduza-a EXATAMENTE como recebida
- A lista manual do usuario prevalece sobre o catalogo

### Proibicao de inferencia de escopo
- NAO adeque, reduza ou interprete o escopo do pedido
- O unico escopo valido e o definido na RequestList do catalogo (ou a lista manual do usuario)

### Prioridade de entrega
- Se nao conseguir ler o catalogo ou houver duvida tecnica, NAO PARE
- Gere o oficio com a lista padrao do template generico mais proximo
- Prioridade e ENTREGAR O DOCUMENTO

## Formato de saida

- Texto puro dentro de bloco de codigo
- SEM formatacao markdown (sem `**`, `*`, `#`)
- SEM emojis
- SEM comentarios introdutorios ("Aqui esta o oficio...")
- Entregue APENAS o documento
- O texto vai do enderecamento ate o prazo/contato
- NAO inclua "Atenciosamente" nem assinatura (o PPE gera automaticamente)

## Boilerplate

### LegalHeader
```
Cumprimentando-o, este delegado de policia subscritor, no uso de suas atribuicoes legais e regulamentares conferidas pelo artigo 144, §4o, da Constituicao Federal, artigo 90, §3o, da Constituicao Estadual do Rio Grande do Norte, artigo 4o do CPP, Lei no 12.830/2013, artigo 15 da Lei no 12.850/2013 e artigo 10§3o da Lei no 12.965/2014, com o fito de instruirmos o procedimento policial em tramitacao nesta Delegacia.
```

### ConfidentialityNotice
```
Informo que deve haver SIGILO sobre as solicitacoes constantes neste oficio.
```

### DesobedienceThreat
```
O nao atendimento no prazo determinado ensejara a instauracao de procedimento criminal, em desfavor da pessoa identificada como sendo o responsavel direto pelo cumprimento da presente medida extrajudicial, por pratica de CRIME DE DESOBEDIENCIA, conforme previsao no Art. 330 do Codigo Penal Brasileiro.
```

### LersInstruction
```
As informacoes devem ser enviadas a esta circunscricao policial - Delegacia Especializada em Repressao a Crimes Ciberneticos (DRCC), para os e-mails oficiais: diegocamara@policiacivil.rn.gov.br; jessycafarias@policiacivil.rn.gov.br.
```

### Prazo e contato
```
Solicitamos que o atendimento a este oficio seja tratado com PRIORIDADE MAXIMA, considerando a gravidade da investigacao em curso.
As informacoes devem ser enviadas no prazo maximo de [PRAZO_DIAS] dias.

Para eventuais duvidas ou esclarecimentos, contactar:
E-mail: diegocamara@policiacivil.rn.gov.br; jessycafarias@policiacivil.rn.gov.br
Telefone/WhatsApp: (84) 98660-7726
```

**Prazo padrao**: 10 dias (salvo se o usuario especificar outro).

## Padroes por tipo de destinatario

### Oficio ao TJRN — Requisicao de IPs de acesso de terceiros ao PJe

Em casos de fraude/estelionato onde criminosos possam ter consultado o sistema judicial para obter dados reais de processos, o pedido ao TJRN deve ser LIMITADO a:
- Acessos de TERCEIROS ao processo especifico (nao pedir varredura geral do sistema)
- Periodo: data do golpe e aproximadamente 15 dias anteriores
- NAO pedir todos os logs de acesso, acessos anomalos genericos ou varreduras amplas

Modelo padrao:

    Registros de acessos de terceiros ao processo nº [NUMERO_PROCESSO] no sistema PJe, realizados no período de [DATA_INICIO] a [DATA_GOLPE] (datas imediatamente anteriores e incluindo o dia do golpe), com indicação de: data, horário, IP de origem, porta lógica (se disponível) e identificação do usuário que realizou a consulta (login, certificado digital ou acesso público).

    A requisição limita-se aos acessos de terceiros — ou seja, consultas realizadas por pessoas que não sejam partes, advogados constituídos ou servidores com atribuição no processo — a fim de verificar se os criminosos consultaram os autos para obter dados reais (nomes, valores, estágio processual) e conferir maior credibilidade à abordagem fraudulenta.

## Catalogo de provedores

Carregue `references/catalogo-provedores.md` para consultar nomes, enderecos e listas de pedidos de cada provedor.
