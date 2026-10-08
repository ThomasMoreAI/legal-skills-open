---
name: 3-2-diagramar-peca-emidio-trancoso
title: Diagramar Peça — Legal Design simples
description: Transforma qualquer peça já escrita (.md ou texto) em um PDF bem diagramado, com Legal Design simples — capa, destaques, citações em bloco, fundamentos e linha do tempo. Não altera o conteúdo, só a forma visual. Use quando quiser entregar uma petição, contrato, parecer ou notificação com aparência profissional e legível.
author: emidio-trancoso
author_url: https://github.com/emidio-trancoso/advocacia-aberta/tree/main/.agents/skills/3.2-diagramar-peca
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# Diagramar Peça — Legal Design simples

Pega uma peça já redigida (em `.md` ou texto) e gera um **PDF diagramado** usando
Typst e um template enxuto que acompanha esta skill. Serve para **qualquer peça**:
petição, contestação, recurso, parecer, contrato, notificação extrajudicial,
alegações finais.

## ⚠ Regra absoluta

**Não inventa, não adiciona, não parafraseia.** O conteúdo jurídico é exatamente o que
está na peça original. O que muda é só a forma visual — onde cada trecho fica mais
legível (um destaque, uma citação em bloco, uma linha do tempo). Nunca crie fatos,
números, citações de lei ou jurisprudência que não estejam no texto original.

---

## Pré-requisito

Esta skill usa o **Typst** para gerar o PDF. Verifique se está instalado com
`typst --version`. Se não estiver:
- macOS: `brew install typst`
- outros sistemas: ver https://github.com/typst/typst (há instaladores prontos)

Se o usuário não tiver e não quiser instalar, você ainda pode entregar a peça
formatada em Markdown limpo — mas o resultado bonito é o PDF.

---

## Instrução

Considere `<arquivo-da-peca>` o caminho relativo informado pelo usuário (ex.:
`casos/meu-caso/pecas/contestacao-v1.md`). Se não tiver sido informado, pergunte qual
peça deve ser diagramada.

### Passo 1 — Ler a peça inteira

Leia o arquivo do início ao fim. Identifique os dados de cabeçalho (juízo/destinatário,
partes, título da peça) e, para cada bloco do texto, que tipo de conteúdo é:

| Conteúdo no texto | Componente do template |
|---|---|
| O ponto-chave, a tese central, um alerta | `#destaque[...]` |
| Citação literal (transcrição, doutrina, artigo de lei, cláusula) | `#citacao(fonte: "...")[...]` |
| Lei ou jurisprudência usada como fundamento | `#fundamento(tipo: "...", ref: "...")[...]` |
| Sequência de fatos com datas | `#cronologia((("data", "evento"), ...))` |
| Título de seção | `= Título` (nível 1) e `== Subtítulo` (nível 2) |
| Texto argumentativo comum | parágrafo normal |
| Etiqueta curta para guiar a leitura (ex.: PEDIDO) | `#marcador("PEDIDO")` |

**Critério:** use o componente mais rico que o conteúdo permitir, mas **com moderação** —
um bom Legal Design respira. Não transforme tudo em caixa. Em geral, no máximo ~6
elementos visuais por página; o resto é texto bem espaçado.

### Passo 2 — Gerar o arquivo Typst

Crie um arquivo `.typ` ao lado da peça (mesma pasta, sufixo `-diagramada`). Estrutura:

```typst
#import "/.agents/skills/3.2-diagramar-peca/template.typ": *

#show: peca.with(
  titulo: "<título da peça>",
  juizo: "<juízo ou destinatário, se houver>",
  partes: "<partes, se houver>",
  rodape: "<advogado / OAB, se houver>",
)

// Conteúdo da peça, seção por seção, usando os componentes onde fizer sentido.
// Copie as palavras EXATAS da peça original.
```

Regras de geração:
- **Copie as palavras da peça** — não reescreva, não resuma, não "melhore".
- Preencha `#fundamento(...)` e `#citacao(...)` só com o que está no texto. Se a peça
  cita um precedente sem dados completos (sem número/link), deixe como está — não
  invente. Se quiser enriquecer com a fonte real, use antes as skills
  `buscar-fontes` ou `buscar-tjpr` e só então preencha.
- **Cuidado com o cifrão `$`** (no Typst ele inicia "modo matemático"):
  - No texto corrido, escreva `\$` para o símbolo de real — ex.: `R\$ 2.400,00`.
  - Mas **dentro de strings entre aspas** (como nos argumentos de `#cronologia(...)`),
    use `$` sem a barra — ex.: `"R$ 2.400"`. Em string, a barra apareceria literal no PDF.
- Outros caracteres a escapar no texto corrido quando necessário: `#`, `@`, `*`, `_`, `<`, `>`.

### Passo 3 — Compilar o PDF

Rode (a partir da raiz do projeto, por causa do `--root`):

```bash
typst compile --root . "casos/<caso>/pecas/<arquivo>-diagramada.typ" "casos/<caso>/pecas/<arquivo>-diagramada.pdf"
```

Se der erro de compilação, leia a mensagem, corrija o `.typ` (normalmente é um
caractere a escapar ou uma vírgula faltando) e recompile.

### Passo 4 — Entregar

Informe ao usuário:
1. Caminho do `.pdf` e do `.typ` gerados.
2. Quais componentes visuais você aplicou e em quais seções.
3. Sugira abrir o PDF e revisar seção por seção — e lembre que dá para ajustar as
   cores/fontes editando `template.typ`.

---

## Dica

Antes de diagramar, vale executar a skill `revisar-peca` — diagramar uma peça com erro
só deixa o erro mais bonito. A ordem natural é: `redigir-peca` → `revisar-peca` →
`diagramar-peca`.
