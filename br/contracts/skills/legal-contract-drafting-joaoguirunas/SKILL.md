---
name: legal-contract-drafting-joaoguirunas
title: Legal Contract Drafting — nenhuma cláusula sem origem
description: Método de redação e revisão de contratos, aditivos, distratos, termos e NDAs a partir de modelo da biblioteca e postura aprovada — anatomia em 15 blocos, linguagem clara, matriz de desvios, revisão de minuta da contraparte e versionamento com changelog. Use ao redigir, revisar ou versionar qualquer minuta que uma contraparte vá ler ou assinar.
author: joaoguirunas
author_url: https://github.com/joaoguirunas/team-os/tree/main/.claude/skills/legal-contract-drafting
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
---

# Legal Contract Drafting — nenhuma cláusula sem origem

Minuta é a postura da empresa escrita em obrigações. Cláusula sem origem é risco sem dono; desvio sem marca é concessão que ninguém decidiu; valor "a preencher" é contrato que assina sozinho. Esta skill dá a anatomia, a régua de linguagem e a **matriz de desvios** — o artefato que permite a IUSTITIA cruzar minuta ↔ modelo ↔ postura e a PRUDENTIA aprovar sabendo exatamente o que cedeu. Nada aqui é parecer; o advogado inscrito da empresa valida antes da assinatura.

## 1. Princípios

1. **Nenhuma cláusula sem origem.** Cada cláusula aponta para modelo da biblioteca (`M{N}.{c}`), para a postura (`legal-posture.md §`) ou para fonte de VERITAS (citação completa). Sem origem, não entra.
2. **Todo desvio marcado.** Texto que se afasta do modelo ou da postura leva `[DESVIO: motivo]` inline e uma linha na matriz — quem pediu, por quê, quem aprovou.
3. **Valores, partes e prazos vêm do brief ou do registro (`#K`).** Nunca "preencher depois", nunca `[●]` na versão que vai a gate. Campo sem dado = minuta não está pronta.
4. **Versão com PASS nunca é editada.** Mudança = `v{N+1}` com changelog; a anterior permanece intacta.
5. **Linguagem clara.** Obrigação com sujeito, verbo, objeto, prazo e consequência. Frase que exige releitura é frase a reescrever.
6. **Quem redige não decide ceder e não envia.** Ceder é PRUDENTIA/usuário; enviar é AEQUITAS com PASS + confirmação explícita do usuário.
7. **Dado sensível fora da smart-memory.** Partes por alias; dados completos só no arquivo final que AEQUITAS trava.

## 2. Pré-condições

| Pré-condição | Evidência | Sem ela |
|---|---|---|
| Postura APROVADA | `project/legal-posture.md` com `status: aprovada` | não há gate possível — não redigir |
| Modelo da relação existe | `agents/architecture/model-system.md` → `M{N}` `aprovada` | pedir a LEX; sem modelo, minuta é `[SEM MODELO]` e exige aprovação prévia de PRUDENTIA |
| Brief com partes, objeto, valores, prazos | story `L{N}` ou brief do lead | não redigir; devolver a pergunta exata |
| Base legal das cláusulas que exigem | research de VERITAS com `[ACHADO]` datado | cláusula fica `[BASE LEGAL PENDENTE]`; gate bloqueado |
| Aditivo/distrato: contrato-mãe no registro | `contracts-registry.md` `#K` | não há o que aditar |

## 3. Anatomia do contrato

| # | Bloco | Contém | Origem típica | Verificação |
|---|---|---|---|---|
| 1 | Qualificação das partes | denominação, tipo, registro (alias na smart-memory), representante, poderes | brief / `#K` | partes idênticas em todo o texto e anexos |
| 2 | Considerandos | contexto e intenção, sem obrigação | brief | nenhum "deverá" aqui |
| 3 | Definições | termos com inicial maiúscula, uma definição cada | `M{N}.def` | todo definido é usado; todo usado é definido |
| 4 | Objeto | o que se entrega/licencia/presta; o que está fora | brief + `M{N}.obj` | escopo fechado; exclusões explícitas |
| 5 | Obrigações das partes | lista por parte, com prazo e critério | `M{N}` | cada obrigação tem sujeito, prazo, consequência |
| 6 | Preço e pagamento | valor, moeda, forma, vencimento, reajuste, atraso, tributos | brief | numeral = por extenso; índice de reajuste nomeado |
| 7 | Prazo e rescisão | vigência, renovação, aviso prévio, hipóteses, efeitos | postura § + `M{N}` | datas registráveis por FIDES |
| 8 | Confidencialidade | o que é confidencial, exceções, prazo pós-término | postura § | prazo pós-término explícito |
| 9 | Propriedade intelectual | titularidade, licença, pré-existente, derivado | postura § | inegociável da postura intacto |
| 10 | Dados pessoais | papéis, finalidade, base legal, segurança, incidente, término | `/legal-compliance-lgpd` + fonte | base com fonte; sem "legítimo interesse" por padrão |
| 11 | Responsabilidade e limitação | teto, exclusões, indenização | postura piso/teto | teto dentro do negociável ou decisão escrita do usuário |
| 12 | Multas e penalidades | hipótese, base de cálculo, teto | postura piso/teto | nenhuma multa sem hipótese |
| 13 | Foro e lei aplicável | foro, lei, meio (negociação → mediação → arbitragem/judicial) | postura § | conforme preferência da postura |
| 14 | Disposições gerais | integralidade, cessão, notificações, tolerância, independência | `M{N}.ger` | endereço de notificação preenchido no arquivo final |
| 15 | Anexos | escopo, SLA, preços, ordem de serviço, política de dados | brief | numerados, referenciados no corpo, hierarquia declarada |

Bloco ausente sem motivo na matriz = desvio não marcado.

## 4. Linguagem clara

- **Obrigação:** "{Parte} {verbo no presente} {objeto} até {prazo}; descumprido, {consequência}." Proibido "envidará esforços", "sempre que possível", "em prazo razoável".
- **Um termo, um sentido.** Definido com maiúscula, usado sempre igual. Sinônimo é ambiguidade.
- **Valor:** numeral e por extenso, moeda, base (mensal/único), tributos incluídos ou não.
- **Prazo:** dias corridos ou úteis, marco inicial ("contados de …").
- **Referência cruzada:** número da cláusula, nunca "acima"/"abaixo".
- **Proibido:** latinismo sem necessidade, dupla negativa, "e/ou", frase com mais de 3 orações, adjetivo em obrigação ("adequado", "razoável") sem critério ao lado.

## 5. Matriz de desvios

Toda minuta sai com `{contrato-slug}-v{N}-desvios.md` — 100% das cláusulas, uma linha cada:

```
cláusula | título | origem (M{N}.{c}.{p|vk} | postura §X | fonte: citação) | status (= modelo | variante | DESVIO) | o que desvia | motivo | pedido por | aprovado por (PRUDENTIA / usuário) | data
```

`DESVIO` sem `aprovado por` = minuta não vai a gate. Inegociável da postura alterado = `DESVIO` que só o usuário aprova por escrito. Variantes e pisos/tetos: `/legal-clause-library` §4.

## 6. Revisão de minuta da contraparte

Cada cláusula recebe **uma** marca:

| Marca | Significado | Ação |
|---|---|---|
| `ACEITA` | igual ou mais favorável que o modelo | nenhuma |
| `NEGOCIÁVEL` | dentro do piso/teto da postura | aceitar ou contrapropor com a variante da biblioteca |
| `FORA DA POSTURA` | além do piso/teto sem ferir inegociável | contraproposta + decisão de PRUDENTIA |
| `INEGOCIÁVEL VIOLADO` | fere cláusula inegociável | contraproposta obrigatória; ceder só o usuário, por escrito |

Saída: `templates/revisao-contraparte.md` + contraproposta como nova versão com matriz. Comentário à contraparte é texto que sai — só via AEQUITAS com PASS + confirmação.

## 7. Versionamento e changelog

```
{contrato-slug}-v{N}.md            ← texto
{contrato-slug}-v{N}-desvios.md    ← matriz
## Changelog (no topo da minuta)
v{N} — {data} — {mudança, cláusula a cláusula} — origem (contraparte / PRUDENTIA / usuário / FAIL de IUSTITIA) — status do gate
```

`v1` = primeira versão a gate; toda rodada de IUSTITIA ou retorno da contraparte = `v{N+1}`; versão com PASS é imutável (AEQUITAS trava com hash); versão enviada e depois alterada é sempre nova versão, nunca "correção".

## 8. Checklist de coerência — antes de pedir gate

| # | Verificação | Como |
|---|---|---|
| C1 | Matriz cobre 100% das cláusulas, todas com origem | contagem cláusulas = linhas |
| C2 | Zero `[●]`, "a definir", "preencher", `____` | grep |
| C3 | Partes, datas, valores, prazos idênticos entre corpo, anexos e brief/`#K` | cruzamento manual |
| C4 | Todo termo definido é usado; todo usado é definido | grep dos termos com maiúscula |
| C5 | Referências cruzadas apontam para cláusula existente | leitura |
| C6 | Blocos 7, 8, 10, 11, 12 dentro do piso/teto ou `DESVIO` aprovado | matriz |
| C7 | Base legal com citação completa e vigente onde exigida | matriz, coluna origem |
| C8 | Changelog atualizado; versão anterior preservada | listagem do diretório |
| C9 | Zero dado sensível de terceiro na smart-memory | leitura; alias |
| C10 | Rodapé interno "Isto não é parecer; o advogado da empresa valida antes da assinatura" | grep |

Falha em C1–C3 ou C6 é bloqueante.

## 9. Templates

- `templates/contrato-estrutura.md` — os 15 blocos com origem, campos obrigatórios e changelog
- `templates/matriz-desvios.md` — a matriz §5 com base legal citada e prazos para FIDES
- `templates/revisao-contraparte.md` — cláusula a cláusula com as 4 marcas e contraproposta

## 10. Contrato com o resto da squad

- **Produz:** CONCORDIA (legal-drafter) — minuta `v{N}`, matriz de desvios, revisão da contraparte.
- **Consome:** LEX fornece o modelo `M{N}` e a story `L{N}`; VERITAS fornece a base legal (`/legal-research` §3); PRUDENTIA lê minuta + matriz inteiras e emite `APROVADA | AJUSTES | REPROVADA`; FIDES cadastra prazos e obrigações do bloco 7 e dos anexos no registro; AEQUITAS trava a versão com PASS e conduz a assinatura; CLEMENTIA parte do mesmo método para acordo e distrato.
- **Cruza:** IUSTITIA aplica os 12 pontos sobre minuta ↔ matriz ↔ modelo ↔ postura; desvio sem aprovador ou campo em branco = FAIL.
