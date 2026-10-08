---
name: fundamentacao-letradalei
title: Fundamentação Judicial
description: Estrutura a fundamentação de sentença, decisão interlocutória ou despacho conforme o art. 489 do CPC (esp. § 1º), com dispositivos verificados. Use para "monta a fundamentação", "fundamentar a sentença", "estrutura a decisão sobre [tese]". Não use para peças de parte ou parecer ministerial.
author: letradalei
author_url: https://github.com/letradalei/skills/tree/main/plugins/letradalei/skills/fundamentacao
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
---

# Fundamentação Judicial

Esta skill **estrutura** a fundamentação e **fornece a base legal verificada**, nunca decide. A convicção do(a) juiz(a) é insubstituível; o texto produzido é um andaime que a magistrada(o) preenche, ajusta, contraria e firma.

O que resolve bem: o risco de anulação por falta de fundamentação (CPC art. 489, § 1º — checa cada um dos seis incisos), o erro de citação legal (toda lei vem do MCP) e o esquecimento de argumento (art. 489, § 1º, IV — força o mapeamento explícito das teses).

O que **não** resolve:
- **Convicção judicial.** A skill propõe; o(a) juiz(a) decide. Cada bloco de mérito leva `[CONVICÇÃO JUDICIAL, confirmar ou substituir]`.
- **Jurisprudência fora do MCP.** O MCP cobre legislação federal e jurisprudência federal (STF/STJ/TST/CARF) + IRDRs estaduais. O que não for encontrado fica `[JURISPRUDÊNCIA NÃO VERIFICADA VIA MCP, conferir manualmente no STJ/STF/tribunal]`.
- **Política de uso de IA no Judiciário.** Resoluções do CNJ e atos do tribunal local estão **fora do corpus**; consulte-os antes de usar IA na atividade-fim.

## Contratos compartilhados (leia antes de redigir)

- **`letradalei:pesquisa`** — como buscar e verificar lei e jurisprudência no MCP (ferramentas, parâmetros, vigência, texto integral). Nenhuma citação vem de memória: decisão que cita artigo inexistente é embargo declaratório certo, e em casos sérios, cassação.
- **`../_shared/intake.md`** — disciplina de entrevista (em blocos de até 4 perguntas/rodada), protocolo "Informar manualmente" e fallback não-interativo.
- **`../_shared/citacao-e-formato.md`** — regras de verificação (vigência, `source_url`, `eficacia`, truncamento) e o bloco de citação padrão. **Especificidades desta minuta:** (a) a transcrição de dispositivo na fundamentação vai **entre aspas** (estilo próprio desta skill, distinto das peças de parte); (b) ao citar precedente, identifique os **fundamentos determinantes** e demonstre a adequação ao caso (exigência do art. 489, § 1º, V).
- **`../_shared/saida.md`** — mecânica de saída (dois arquivos, `montar_docx.py`, `colorir_marcadores.py`). O aviso ao usuário e o `NOTAS.md` desta minuta são os do Passo 6 (orientados à **publicação**, não ao protocolo).

Regras desta decisão, além da `pesquisa`: `situacao` ≠ `vigente` → `[VERIFICAR VIGÊNCIA, situação: <X>]`; norma estadual, regimento interno, resolução de CNJ/CNMP → `[FORA DO CORPUS]`; busca vazia/contraditória → registre via `acervo · reclame_aqui` antes de seguir.

## Fluxo

1. **Leia os autos** (Passo 1) — inicial, contestação, provas. Sem isso, a fundamentação é genérica e cai no inciso III do § 1º do art. 489.
2. **Mapeie as teses** das partes (Passo 1) — o gatilho do art. 489, § 1º, IV.
3. **Pesquise** (`letradalei:pesquisa`) cada dispositivo aplicado.
4. **Estruture** relatório + fundamentação + dispositivo (Passo 4).
5. **Cheque contra o art. 489, § 1º** (Passo 5) e gere a saída (Passo 6).

## Passo 1, Ler os autos

**Pré-requisito não-negociável.** Peça ao usuário:

> "Para fundamentar com qualidade preciso, no mínimo, da petição inicial, da contestação, e, se houver, das principais provas (depoimento, perícia, documentos chave). Quanto mais completos os autos, menor o risco do art. 489, § 1º, IV (deixar de enfrentar argumento capaz de infirmar a conclusão). Pode anexar PDF/DOCX ou colar os trechos relevantes."

Extraia e devolva ao usuário para confirmação: **partes** e qualificação resumida; **pedidos** da inicial (letra por letra); **causa de pedir** (fatos + fundamentos); **preliminares** da contestação (art. 337, uma a uma); **defesa de mérito**; **reconvenção / pedido contraposto**; **provas produzidas** (documental, testemunhal com síntese, pericial com conclusão); **pareceres** (MP, amicus curiae).

**Mapeamento de teses.** Antes de redigir, liste explicitamente:

```
Teses do(a) autor(a) a enfrentar:
  T1: [...]
  T2: [...]

Teses da(o) ré(u) a enfrentar:
  D1: [...]
  D2: [...]

Questões processuais pendentes (preliminares):
  P1: [...]
```

**Esse mapa é a vacina contra o art. 489, § 1º, IV.** Toda tese listada precisa ser enfrentada na fundamentação, ou expressamente declarada prejudicada (e por quê).

## Passo 2, Tipo de pronunciamento

| Tipo | Quando | Estrutura mínima |
|---|---|---|
| Sentença (art. 203, § 1º, do CPC) | Põe fim à fase cognitiva em 1º grau, com ou sem mérito | Relatório + fundamentação + dispositivo |
| Decisão interlocutória (art. 203, § 2º) | Resolve questão incidente | Fundamentação + dispositivo (relatório dispensado) |
| Despacho fundamentado | Apenas impulso, mas a lei exige motivação | Síntese + fundamento |

Busque art. 203 do CPC via MCP e cole o texto na sua nota interna, não na decisão.

## Passo 3, Pesquisa legal

Para **cada norma** que vai aparecer na fundamentação, siga `letradalei:pesquisa`: identifique o instituto (ex.: "responsabilidade civil objetiva do fornecedor", "ônus da prova", "boa-fé objetiva"), busque com `norma` (sigla/slug), verifique `situacao` e transcreva o texto literal **entre aspas** na fundamentação, com `source_url`. Norma fora do corpus → `[FORA DO CORPUS, verificar manualmente]`. **Sem suplementação silenciosa:** cobertura fina no MCP → pergunte ao usuário antes de buscar fora.

## Passo 4, Estrutura da decisão

```
SENTENÇA

Processo nº [...]
Autor: [...]
Réu(s/é(s)): [...]

I, RELATÓRIO

[Síntese cronológica do processo. Não confundir relatório com fundamentação, aqui
descreve-se o que ocorreu nos autos, sem juízo de valor.]

  [Pedidos da inicial, citar inicial fls. [...]]
  [Defesa apresentada, citar contestação fls. [...]]
  [Réplica, se houver]
  [Saneamento, fls. [...]]
  [Instrução, provas produzidas]
  [Memoriais / alegações finais]
  [É o relatório.]

II, FUNDAMENTAÇÃO

  [Sequência sugerida:
   1. Questões processuais pendentes (preliminares da contestação, questões
      conhecíveis de ofício).
   2. Mérito, por tese, na ordem lógica (prejudiciais primeiro).
   3. Pedidos cumulados / sucessivos / acessórios.]

II.1, DAS PRELIMINARES

II.1.1, [Preliminar P1, ex.: Da alegada incompetência relativa]

A(O) Ré(u) sustentou, com fundamento no art. 337, II, do CPC, a incompetência
relativa deste juízo, ao argumento de que [...].

Dispõe o art. 337, II, do CPC:

  "[texto literal via MCP]"

[Análise concreta dos elementos do caso. Por que a regra do art. 63 do CPC se
aplica ou não. Cita arts. 63 e 64 via MCP. Conclusão: acolhe-se / rejeita-se a
preliminar.]

II.2, DO MÉRITO

II.2.1, Da [tese de fundo principal, ex.: existência da relação de consumo]

[Identifica a controvérsia. Cita art. 2º e 3º do CDC via MCP. Enquadra os fatos.
Conclui.]

II.2.2, Do [próximo ponto controvertido, ex.: defeito do serviço]

  Tese da parte autora (T1): [...]
  Tese da defesa (D1): [...]

Dispõe o art. 14 do CDC:

  "[texto literal via MCP]"

[Análise concreta. Subsunção. Em decisão monocrática, este é o item central, não
economize. Enfrente cada elemento normativo aplicado ao fato. Se a prova
documental ou pericial conduz a determinada conclusão, descreva o caminho.]

II.2.3, Da [tese D2, defesa que precisa ser enfrentada mesmo se já há
            convicção formada, art. 489, § 1º, IV]

[Enfrentamento explícito, com fundamento. Não é necessário concordar, é
necessário responder.]

II.2.4, Do dano moral (e/ou material)

[Cita arts. 186 e 927 do CC via MCP, ou os do CDC conforme caso. Análise do dano,
nexo, prova. Quantum: critério (capacidade econômica do ofensor, gravidade,
caráter pedagógico), cita arts. via MCP se houver tabelamento ou parâmetro
legal.]

II.2.5, Dos juros e correção monetária

[Cita art. 405 do CC (juros legais) ou súmulas aplicáveis, flag estas como
`[JURISPRUDÊNCIA NÃO VERIFICADA VIA MCP]` para o(a) juiz(a) conferir.]

II.2.6, Da sucumbência

Cita art. 85 e parágrafos do CPC via MCP. Critério de fixação.

III, DISPOSITIVO

Ante o exposto, JULGO [PROCEDENTE / PARCIALMENTE PROCEDENTE / IMPROCEDENTE] o(s)
pedido(s) formulado(s) na inicial, extinguindo o processo COM RESOLUÇÃO DE MÉRITO,
nos termos do art. 487, I, do CPC, para:

  a) [...]
  b) [...]

CONDENO a(o) [parte] ao pagamento das custas processuais e dos honorários
advocatícios, que fixo em [...]% sobre [base], com fundamento no art. 85, §§ 2º
e 3º, do CPC.

[Se aplicável] CONCEDO a gratuidade de justiça nos termos do art. 98 do CPC,
restando suspensa a exigibilidade na forma do § 3º.

P.R.I.

[Cidade], [data].

_______________________________________
[JUIZ(A) DE DIREITO]
```

## Passo 5, Checagem obrigatória contra o art. 489, § 1º, do CPC

**Sem isto, a fundamentação é não-fundamentação.** Antes de devolver o `.docx`, rode esta checagem item por item. Para cada inciso, reporte explicitamente:

> Busque o texto do art. 489, § 1º, do CPC via MCP e mantenha-o aberto durante a checagem.

**Inciso I**, não se considera fundamentada a decisão que se limita à indicação, à reprodução ou à paráfrase de ato normativo, sem explicar sua relação com a causa.
- [ ] Cada dispositivo citado tem aplicação concreta explicada (1+ parágrafo de subsunção)?

**Inciso II**, empregar conceitos jurídicos indeterminados sem explicar o motivo concreto.
- [ ] "Boa-fé", "função social", "manifesta improcedência", "interesse público", vieram acompanhadas de razão concreta no caso?

**Inciso III**, invocar motivos que se prestariam a justificar qualquer outra decisão.
- [ ] Trocando "Procedente" por "Improcedente", a fundamentação ainda fecharia? Se sim, ela é vazia.

**Inciso IV**, deixar de enfrentar todos os argumentos deduzidos no processo capazes de infirmar a conclusão.
- [ ] **Para cada T_n e D_n do mapa do Passo 1, há item correspondente na fundamentação?** Se uma tese ficou de fora, ou (a) foi enfrentada (mesmo sumariamente) ou (b) foi declarada prejudicada com motivo. Lacuna silenciosa = anulação.

**Inciso V**, limitar-se a invocar precedente ou enunciado de súmula sem identificar seus fundamentos determinantes e demonstrar adequação ao caso.
- [ ] Cada súmula/precedente citado tem (a) fundamentos determinantes resumidos + (b) demonstração de que o caso se enquadra?

**Inciso VI**, deixar de seguir enunciado de súmula, jurisprudência ou precedente invocado pela parte sem demonstrar distinguishing ou superação.
- [ ] Súmula/precedente invocado pela parte e afastado tem justificativa explícita?

A checagem é parte da entrega, vai listada no bloco de notas, com cada item resolvido ou explicitamente sinalizado.

## Passo 6, Saída

Mecânica em `../_shared/saida.md` (dois arquivos, `montar_docx.py`, `colorir_marcadores.py`), com `<tipo> = fundamentacao-[tipo]`: salve `outputs/fundamentacao-[tipo]-[slug]-[data].docx` + `outputs/fundamentacao-[tipo]-[slug]-NOTAS.md` e rode o `colorir_marcadores.py`. **Esta minuta é orientada à publicação, não ao protocolo** — use o aviso e o `NOTAS.md` abaixo (não os genéricos de `saida.md`):

**Aviso obrigatório ao usuário, incluir sempre após entregar a minuta:**

> ⚠️ **ITENS EM VERMELHO, VERIFICAÇÃO NECESSÁRIA ANTES DA PUBLICAÇÃO**
> Os trechos marcados em vermelho na minuta indicam pontos que exigem decisão ou conferência do(a) magistrado(a) antes de publicar. Revise cada marcador:
> - `[CONVICÇÃO JUDICIAL, confirmar ou substituir]`, bloco de mérito que exige convicção pessoal do(a) juiz(a); substituir pelo texto definitivo
> - `[JURISPRUDÊNCIA NÃO VERIFICADA VIA MCP]`, súmula ou precedente a confirmar manualmente no STJ/STF/tribunal
> - `[FORA DO CORPUS]`, norma estadual, regimental ou resolução do CNJ; verificar na fonte local
> - `[A REVISAR]`, ponto sinalizado durante a redação que precisa de atenção
>
> Nenhum desses marcadores pode permanecer na decisão no momento da publicação.

```
## Notas de revisão, Fundamentação Judicial, [data]

**Skill:** fundamentacao (Letra da Lei)
**Fonte da legislação:** MCP Letra da Lei (texto verbatim do Planalto)

### Mapa de teses (do Passo 1) e onde foram enfrentadas
- T1: [...], enfrentada em II.2.[N]
- D1: [...], enfrentada em II.2.[N]
- D2: [...], declarada prejudicada em II.2.[N] (motivo: [...])

### Checagem do art. 489, § 1º (status item por item)
- I: OK / Pendente em [...]
- II: OK
- III: OK
- IV: OK
- V: N/A (sem precedente invocado nesta minuta)
- VI: OK

### Dispositivos citados (todos verificados via MCP)
- [lei_slug]-[Art-N], [source_url]

### Marcadores que exigem decisão judicial
- `[CONVICÇÃO JUDICIAL, confirmar ou substituir]`, N
- `[JURISPRUDÊNCIA NÃO VERIFICADA VIA MCP]`, N
- `[FORA DO CORPUS]`, N
- `[A REVISAR]`, N

### O que esta skill NÃO fez
- Não decidiu. Sugestões de provimento são placeholders.
- Não pesquisou jurisprudência fora do MCP.
- Não conferiu resoluções do CNJ / atos do tribunal sobre uso de IA.
- Não conferiu prevenção, conflito de competência, impedimentos/suspeição.
- Não calculou quantum indenizatório, propôs critérios; cabe ao(à) juiz(a) fixar.
```

## O que esta skill NÃO faz

- **Não decide.** A convicção é do(a) juiz(a). Cada bloco de mérito leva `[CONVICÇÃO JUDICIAL, confirmar ou substituir]`.
- **Não pesquisa jurisprudência fora do MCP.** Súmulas/REsps/temas não encontrados ficam marcados para conferência manual.
- **Não dispensa a leitura dos autos pelo(a) magistrado(a).** A leitura é o ato indelegável; a skill apenas estrutura o que o(a) juiz(a) já compreendeu.
- **Não substitui ato decisório.** Produz minuta; a decisão é proferida quando o(a) juiz(a) assina.
- **Não decide sobre uso permitido de IA no gabinete.** Resoluções do CNJ e atos do tribunal local devem ser consultados pelo(a) magistrado(a) antes de adotar a minuta.
