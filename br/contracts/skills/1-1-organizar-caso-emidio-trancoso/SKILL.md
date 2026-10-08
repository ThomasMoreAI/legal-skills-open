---
name: 1-1-organizar-caso-emidio-trancoso
title: Organizar Caso — Sumário dos Documentos
description: Lê todos os documentos de um caso (PDFs de processo, contratos, dossiês, anexos de cliente) e produz o SUMARIO.md com índice dos documentos, identificação das pessoas envolvidas, datas-chave e destaque dos mais relevantes. Use ao iniciar um caso novo ou ao receber documentos adicionais.
author: emidio-trancoso
author_url: https://github.com/emidio-trancoso/advocacia-aberta/tree/main/.agents/skills/1.1-organizar-caso
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
---

# Organizar Caso — Sumário dos Documentos

Esta skill orienta o agente a organizar a pilha de documentos de um caso. "Caso" aqui é qualquer conjunto de material jurídico: os autos de um processo judicial, mas também os documentos de um contrato, as peças de uma due diligence, um dossiê de investigação ou os anexos que um cliente enviou.

O resultado é um único arquivo — `casos/<caso>/analise/SUMARIO.md` — que serve de mapa do caso: uma tabela com todos os documentos, quem são as pessoas envolvidas, as datas que importam e quais documentos merecem atenção.

## Instrução

Esta skill funciona em dois modos, conforme o que você tem em mãos. Escolha pelo que o
usuário forneceu; na dúvida, pergunte.

- **Modo repositório** — você trabalha sobre a pasta de um caso no espaço de trabalho
  aberto no agente. Os documentos ficam em `casos/<caso>/autos/` e o resultado é
  gravado em `casos/<caso>/analise/SUMARIO.md`. Use este modo quando o usuário indicar
  um `<caminho-do-caso>` ou já existir uma pasta `casos/`.
- **Modo conversa** — não há pasta do caso: os documentos foram anexados diretamente na
  conversa. Use os anexos como entrada e, ao final, entregue o `SUMARIO.md` como
  arquivo para download. Use este modo quando o usuário apenas anexar documentos.

### Modo repositório

Considere `<caminho-do-caso>` o caminho relativo informado pelo usuário (ex.:
`casos/meu-caso`). Se não tiver sido informado, peça-o antes de continuar. Nos
comandos e arquivos abaixo, substitua o marcador pelo caminho real, sempre entre
aspas.

A raiz do projeto é a pasta aberta no agente. Todos os caminhos abaixo são relativos
a ela — nunca use caminhos absolutos.

Os documentos do caso ficam, por convenção, em `<caminho-do-caso>/autos/`. Se a pasta
não existir ou os arquivos estiverem soltos diretamente em `<caminho-do-caso>/`,
trabalhe com o que encontrar e siga em frente.

### Modo conversa

Trabalhe sobre os documentos anexados na conversa — não há estrutura de pastas. Os
passos abaixo foram escritos para o modo repositório; no modo conversa eles valem
assim:

- **Passo 1** — em vez de listar a pasta, relacione os documentos que você recebeu na
  conversa.
- **Passo 2** — pule; a divisão de PDF depende de script local e só existe no modo
  repositório.
- **Passos 3 e 4** — iguais: leia, classifique e levante pessoas, datas e objeto.
- **Passo 5** — em vez de gravar em `casos/<caso>/analise/`, produza o `SUMARIO.md` e
  entregue-o como arquivo para download.
- **Passo 6** — confirme o que foi lido e o que ficou de fora.

---

### Passo 1 — Listar os documentos do caso

Liste tudo o que existe na pasta do caso:

```bash
ls -1 "<caminho-do-caso>/autos/" 2>/dev/null || ls -1 "<caminho-do-caso>/"
```

Anote os arquivos que dá para ler como texto: PDFs, .docx, .txt, .md. Áudio e vídeo
(.mp4, .webm, .m4a, .wav) ficam de fora desta skill — para esses, execute primeiro a
skill `transcrever`.

---

### Passo 2 — (OPCIONAL) Dividir um PDF único e gigante

Pule este passo se os documentos já vierem separados em vários arquivos.

Faça este passo **somente** quando o material for **um único PDF enorme** com muitos documentos colados dentro — situação típica de autos de processo exportados de uma vez do PJe ou Projudi. Nesse caso, dividir o arquivo em um PDF por documento facilita a leitura:

```bash
python3 "${PLUGIN_ROOT:-${CLAUDE_PLUGIN_ROOT:-.}}/ferramentas/processamento/split-autos/split.py" "<caminho-do-caso>/autos/integra.pdf"
```

(Troque `integra.pdf` pelo nome real do PDF gigante.) O script grava os PDFs separados na mesma pasta. Depois, refaça a listagem do Passo 1.

Para qualquer outro tipo de caso — contrato, dossiê, anexos avulsos — ignore este passo.

---

### Passo 3 — Ler e classificar cada documento

Para cada documento, extraia e leia o texto com a capacidade disponível no agente.
Em documentos longos, leia as primeiras páginas para entender do que se trata; em
documentos curtos, leia tudo. Para cada um, levante:

| Campo | O que procurar |
|---|---|
| **Documento** | Nome do arquivo |
| **Data** | Data do documento (assinatura, protocolo, emissão) |
| **Tipo** | O que é: petição, contestação, decisão, sentença, ata, contrato, aditivo, parecer, notificação, e-mail, nota fiscal, comprovante, foto, planilha, procuração… |
| **Origem** | De quem veio / a quem se refere (uma das partes, o juízo, um terceiro, um órgão) |
| **Síntese** | 1 a 2 linhas com o conteúdo principal |
| **Relevância** | ⭐⭐⭐ = central para a tese ou prova decisiva · ⭐⭐ = importante · ⭐ = documental/acessório · — = mero expediente |

Leia por completo os documentos que tendem a ser decisivos, conforme o tipo de caso. Exemplos:
- Em processo judicial: petição inicial, contestação, impugnação, ata de audiência, decisões e sentenças.
- Em contrato: o contrato principal, aditivos, anexos e notificações entre as partes.
- Em due diligence / dossiê: o documento que define o objeto, somado às provas que sustentam ou derrubam cada ponto.

---

### Passo 4 — Identificar as pessoas e os dados do caso

Durante a leitura, vá anotando:
- Nome e documento (CPF/CNPJ) de cada pessoa ou empresa envolvida, e o papel de cada uma (autor, réu, contratante, contratada, cliente, terceiro…).
- Advogados ou representantes, quando houver (nome + OAB/UF + cidade).
- Identificadores do caso, quando houver: número do processo (CNJ), vara e comarca, ou número/objeto do contrato.
- Datas-chave: o que aconteceu e quando (assinatura, vencimento, fato gerador, citação, audiência, prazos).
- Objeto do caso em uma frase: o que se discute ou se pretende.

Anti-alucinação: registre apenas o que está escrito nos documentos. Se um dado não aparece, deixe o campo em branco — nunca invente nome, número, data ou valor.

---

### Passo 5 — Escrever o SUMARIO.md

Crie a pasta `analise/` se não existir e escreva
`<caminho-do-caso>/analise/SUMARIO.md` com esta estrutura (adapte os rótulos ao tipo
de caso — os exemplos entre colchetes são só orientação):

```markdown
# SUMÁRIO — [nome ou identificador do caso]

**Identificação:** [nº do processo + vara/comarca, ou nº/objeto do contrato — o que se aplicar]
**Objeto:** [1 frase: o que o caso discute ou pretende]
**Tarefa atual:** [o que está pendente agora; deixar em branco se ainda não souber]

## Pessoas envolvidas

| Papel | Nome | Documento (CPF/CNPJ) | Representante / Advogado |
|---|---|---|---|
| [ex.: Autor / Contratante / Cliente] | ... | ... | ... |
| [ex.: Réu / Contratada / Terceiro] | ... | ... | ... |

## Objeto resumido

[1 parágrafo descrevendo do que trata o caso]

## Documentos

| Data | Tipo | Origem | ⭐ | Arquivo | Síntese |
|---|---|---|---|---|---|
| dd/mm/aaaa | ... | ... | ⭐⭐⭐ | `nome-do-arquivo.pdf` | ... |
| ... | | | | | |

## Linha do tempo

- **dd/mm/aaaa** — [fato relevante]
- ...

## Posições / Teses

- **[parte ou ponto de vista A]:** [resumo do que sustenta]
- **[parte ou ponto de vista B]:** [resumo do que sustenta]

## Pendências

- [ ] [o que ainda falta esclarecer ou fazer]
```

Se já existir um `SUMARIO.md`, preserve "Tarefa atual" e "Pendências" e atualize apenas os documentos novos.

---

### Passo 6 — Confirmar com o usuário

Ao terminar, informe:
- Quantos documentos foram lidos e indexados.
- Quais não puderam ser lidos (PDF escaneado sem texto, áudio/vídeo, arquivo corrompido).
- Se algum documento relevante ficou sem síntese clara.
- Que o `SUMARIO.md` agora é o ponto de partida do caso: use a skill `diagnosticar`
  para mapear as fragilidades e a skill `redigir-peca` para produzir a peça.
