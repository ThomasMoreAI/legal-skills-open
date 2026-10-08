---
name: blindagem-pre-protocolo-sbroggioadv
title: blindagem-pre-protocolo — a triagem na SUA peça, antes do protocolo
description: 'Uso preventivo do blindagem-peticao-os — a triagem de integridade na SUA peça, antes do protocolo. O Conselho Federal da OAB recomenda verificar peça produzida com apoio de IA; este comando é o instrumento sistemático desse dever: (1) as mesmas varreduras determinísticas da peça recebida (texto oculto acidental, unicode de copy-paste, metadados vazando, revisões não aceitas — parser real, mesmo contrato JSON); (2) limpeza guiada pela higiene-de-metadados; (3) citações e dispositivos PRÓPRIOS roteados ao juris-adv-os (validar-jurisprudencia / auditoria-pre-envio) — a blindagem não duplica esse motor para a própria peça; (4) checklist final pré-protocolo com evidência por item. Aciona: quando o usuário pede /blindagem-propria, "auditar a minha peça", "conferir antes de protocolar", "limpar metadados antes de enviar", ou pergunta se a peça dele está segura para o protocolo.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/blindagem-peticao-os-marketplace/tree/main/blindagem-peticao-os/skills/blindagem-pre-protocolo
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
---

# blindagem-pre-protocolo — a triagem na SUA peça, antes do protocolo

Este é o uso preventivo do produto: o mesmo motor que varre a peça recebida da parte contrária,
apontado para a peça que **você** vai protocolar. O objetivo não é desconfiar do seu trabalho — é
impedir que um descuido técnico (um trecho de rascunho em fonte branca, um comentário interno
esquecido, uma revisão não aceita, uma citação que o modelo inventou) chegue ao juiz com o seu
nome embaixo.

## Por que isto é um dever prático, não paranoia

O Conselho Federal da OAB aprovou recomendações para o uso de IA generativa na prática jurídica
(`context/normas-ia-judiciario-oab.md` §2): legislação aplicável, confidencialidade, prática
jurídica ética e comunicação ao cliente sobre o uso de IA. **Verificar a peça produzida com apoio
de IA é dever prático do advogado** — e este comando é o instrumento sistemático dessa
verificação: parser e evidência, em vez de "passar o olho". Os casos-âncora do produto mostram o
custo de não verificar: em todas as sanções, a responsabilidade pelo que a peça afirma foi do
advogado, nunca da ferramenta.

## Quando esta skill entra

- O usuário pede `/blindagem-propria`, "audita a minha peça", "confere antes de protocolar".
- O onboarding registrou uso principal "as próprias peças" e chegou um arquivo.
- O `blindagem-master` identificou na triagem que a peça em análise é a **própria** do usuário.

> **🖱️ Escolha de lista fechada = botões:** pergunte com **AskUserQuestion** qual arquivo será
> auditado — **DOCX de trabalho** × **PDF final** × **os dois**. O ideal é auditar os dois: o DOCX
> carrega revisões e comentários; o PDF é o que o tribunal recebe.

## Etapa 1 — Varreduras determinísticas (as mesmas de C1, mesmo contrato)

Rode os mesmos parsers da peça recebida — `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/<parser>.py"
<arquivo>` → JSON no stdout com
`status: ok | missing_dependency | error | formato_nao_suportado` + `achados[]`. Vale a trava T1 sem exceção: sem lib
instalada, a skill **declara** que a varredura estrutural não rodou e instrui a instalação —
nunca finge ter varrido.

| Varredura | O que ela pega na SUA peça |
|---|---|
| `varredura-texto-oculto` | Trecho de rascunho ou prompt que ficou em fonte branca/corpo mínimo por acidente de edição |
| `varredura-unicode-invisivel` | Caracteres invisíveis que vieram de copy-paste (chat de IA, web, outro PDF) — zero-width, Tags |
| `varredura-homoglifos` | Confusáveis que entraram por colagem e quebram a busca textual do tribunal |
| `varredura-metadados` | Autor real ≠ assinante, revisões não aceitas, comentários internos, propriedades ocultas |
| `varredura-pdf-ativo` | `/OpenAction`, `/JS`, `/Launch` herdados de conversor ou modelo de PDF |

Na peça própria, a leitura do achado muda de tom: quase tudo aqui é **descuido, não malícia** —
mas o efeito no tribunal é o mesmo. Um comentário "conferir se esse prazo está certo" esquecido no
DOCX é lido pela parte contrária; um bloco de prompt em fonte branca vira o caso TRT-8 com o seu
nome. Anexe a cada achado o dado bruto do parser (cor/tamanho, codepoint, campo de metadado) e a
recomendação de correção.

## Etapa 2 — Limpeza guiada

Apareceu metadado estranho, revisão pendente ou comentário? Roteie para a **`higiene-de-metadados`**
— o guia de limpeza por ferramenta (Word, LibreOffice, Google Docs, PDF). A divisão de trabalho é
fixa: a blindagem **orienta** a limpeza e depois **verifica** o resultado; quem executa, no próprio
arquivo, é o advogado. Nada destrutivo roda por aqui.

## Etapa 3 — Citações e dispositivos PRÓPRIOS → `juris-adv-os`

Quem audita a **sua** citação é o **`juris-adv-os`**: `validar-jurisprudencia` para conferir cada
julgado com WebFetch real, `auditoria-pre-envio` para a varredura final de citações da peça. A
blindagem **não duplica esse motor para a própria peça** — a fronteira é de desenho: o juris audita
a SUA citação antes de enviar; a blindagem roda o mesmo rigor na peça RECEBIDA. Se o `juris-adv-os`
não estiver instalado, diga isso com todas as letras e recomende a instalação — **não improvise**
uma validação de citação "por leitura", que violaria a trava T2.

Dispositivos de lei próprios seguem a mesma lógica: conferência na fonte oficial (Planalto) antes
do protocolo, orientada por esta skill — sem selo da blindagem, que só sela dispositivo da peça
recebida (`dispositivos-da-peca-recebida`).

## Etapa 4 — Checklist final pré-protocolo

Só libere o "pronto para protocolo" com todas as caixas marcadas — e cada caixa com a **evidência**
ao lado, nunca de memória:

- [ ] **Metadados limpos?** — `varredura-metadados` re-rodada no arquivo final; `achados[]` vazio ou só o esperado (autor = assinante, datas coerentes)
- [ ] **Revisões aceitas?** — nenhum track change pendente no DOCX
- [ ] **Comentários removidos?** — zero comentários no arquivo final
- [ ] **Citações validadas?** — cada julgado com selo do `juris-adv-os`, ou declaradamente "não verificada"
- [ ] **PDF final regenerado?** — via impressão para PDF (não "salvar como"), e re-varrido depois

Caixa sem evidência = caixa aberta. O relatório sai na voz do perfil definido no onboarding
(individual: direta e prática; departamento jurídico: formal, com sumário executivo) e fecha
**sempre** com o aviso da trava T5: a conferência final antes do protocolo é do advogado.

## Travas / limites

- **T1** — nenhum selo estrutural sem o parser ter rodado e retornado o dado bruto; sem lib,
  declara e instrui.
- **T2** — nenhuma citação selada sem verificação real; citação própria é do `juris-adv-os`.
- **T5** — a conferência humana final é do advogado; o checklist organiza, não substitui.
- **Nada destrutivo:** esta skill não edita nem "limpa" o arquivo do usuário — orienta (via
  `higiene-de-metadados`) e verifica o resultado.
- **Sinal ≠ veredito** vale também na peça própria: achado técnico é achado técnico, com evidência.
- Autoria "IA Combativa". PT-BR com acentuação correta.
