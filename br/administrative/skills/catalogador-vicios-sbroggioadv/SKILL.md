---
name: catalogador-vicios-sbroggioadv
title: catalogador-vicios — o ato tem vício? qual norma viola?
description: 'O catálogo dos vícios detectáveis num ato já publicado — camada de suporte C2 do opositor-os. Para cada vício diz três coisas: como ele aparece no diário × o que documentalmente confirma o vício × o artigo exato violado. Cobre dispensa/inexigibilidade fora de hipótese (Lei 14.133 arts. 75/74), edital restritivo (art. 5º; prazo do art. 164), aditivo acima do limite (art. 125), nomeação sem concurso (CF 37, II), nepotismo (SV 13), diária atípica, ausência de motivação (Lei 9.784 art. 50 [VERIFICAR]), estouro de gasto com pessoal (LRF arts. 19-20) e ausência/atraso de RREO/RGF (LRF art. 48). Rastreia cada citação ao lastro — verbatim no context/ ou número verificado na pesquisa — e é não exaustivo. Aciona: quando um ato foi extraído do diário e é preciso saber se configura vício.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/opositor-os-marketplace/tree/main/opositor-os/skills/catalogador-vicios
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: administrative
language: pt
---

# catalogador-vicios — o ato tem vício? qual norma viola?

Recebe os atos que o `leitor-diario-oficial` extraiu e responde, para cada um, **se configura vício e
qual artigo ele viola**. É a ponte entre a varredura (C2) e o roteamento (C3): sem a norma violada
nomeada, o `roteador-vicio-orgao` não tem o que rotear e nenhuma peça pode citar lastro (P1). Não diz
para qual órgão vai (é o roteador) nem redige (é C3) — só **classifica e cita a norma**.

## Quando esta skill entra

- Um ato foi extraído do diário e é preciso saber se é vício.
- O usuário descreveu um ato ("a prefeitura nomeou X sem concurso") e quer saber a norma violada.
- O `opositor-master` precisa da classificação antes de rotear.

## Como ler o lastro de cada linha

Cada citação abaixo carrega o **nível de lastro**, para a disciplina anti-alucinação (invariante #1):

- **✅ context/** — texto **verbatim** do anexo indicado; pode citar com firmeza.
- **📄 pesquisa §2.2** — número **verificado na pesquisa** (Planalto, 18/08/2026), mas o texto do artigo
  **não** está capturado num anexo `context/`; ao virar peça, o gerador de C3 **confirma o rol/limite
  na norma vigente antes de citar**. Cite o artigo; não invente o conteúdo do dispositivo.
- **[VERIFICAR]** — número mencionado em pesquisa, sem anexo verbatim; tratar como pendência de fonte.

## O catálogo (não exaustivo — pesquisa §2.2)

| Vício | Como aparece no diário | O que confirma o vício | Norma violada · lastro |
|---|---|---|---|
| **Dispensa de licitação fora de hipótese** | Extrato/termo de "Dispensa de Licitação nº..." publicado | O extrato **não enquadra** em nenhum inciso do rol de dispensa — vício formal provável | **Lei 14.133/2021, art. 75** · 📄 pesquisa §2.2 |
| **Inexigibilidade fora de hipótese** | "Inexigibilidade nº..." publicada | Não há a inviabilidade de competição que o art. 74 exige | **Lei 14.133/2021, art. 74** · 📄 pesquisa §2.2 |
| **Edital com cláusula restritiva de competitividade** | Aviso/edital de licitação | Leitura do edital contra os princípios de competitividade e isonomia | **Lei 14.133/2021, art. 5º** · 📄 pesquisa §2.2. **Prazo fatal para impugnar: até 3 dias úteis antes da abertura — Lei 14.133 art. 164 · ✅ `lei-14133-recorte-fiscalizador.md`; TV5** |
| **Aditivo contratual acima do limite** | "Extrato do Termo Aditivo ao Contrato nº..." | Percentual de acréscimo acima do limite legal (25% obras/serviços/compras; 50% reforma de edifício/equipamento) | **Lei 14.133/2021, art. 125** ✅ `context/lei-14133-recorte-fiscalizador.md` (cálculo fino pelo `calculosjudiciais-adv-os`) |
| **Nomeação sem concurso para cargo que o exige** | Portaria de nomeação | Cargo **efetivo** exige concurso; nomeação livre só cabe a cargo em comissão | **CF art. 37, II** · 📄 pesquisa §2.2 (não verbatim em `cf-ancoras-fiscalizador.md`) |
| **Nepotismo** | Portaria de nomeação para cargo comissionado/função gratificada | Nome do nomeado bate com o da autoridade nomeante ou de dirigente do mesmo órgão (até 3º grau; inclui nomeação cruzada) | **Súmula Vinculante 13/STF** · 📄 pesquisa §1 #11. **Via de leigo = representação administrativa, NÃO reclamação ao STF (técnica, exige advogado) — TV8** |
| **Diária ou verba de viagem atípica** | Portaria de concessão de diárias | Valor/frequência fora do normativo interno **+ ausência** de relatório de viagem/prestação de contas | Sem artigo único: confronto com normativo interno do ente. **Fluxo: pedir por LAI o relatório que falta → se confirmar, representar** (pesquisa §2.3) |
| **Ausência de motivação de ato discricionário** | Ato discricionário publicado sem fundamentação | Falta a fundamentação que a lei torna obrigatória em certas hipóteses | **Lei 9.784/1999, art. 50 [VERIFICAR]** — sem anexo verbatim no `context/`; confirmar o rol de hipóteses na norma antes de citar em peça |
| **Estouro do limite de gasto com pessoal** | RGF — Relatório de Gestão Fiscal (publicação quadrimestral, LRF art. 54) | Despesa com pessoal acima do teto da RCL: União 50%, Estados 60%, Municípios 60% (art. 19); e a repartição por Poder do art. 20 | **LC 101/2000, arts. 19-20** · ✅ `lc-101-lrf.md` (percentual pelo `calculosjudiciais-adv-os`) |
| **Ausência ou atraso de RREO/RGF** | RREO (bimestral, até 30 dias após o bimestre — art. 52) ou RGF (quadrimestral — art. 54) **não publicado no prazo** | A **própria ausência** já é o vício — violação do dever de transparência | **LC 101/2000, art. 48** · ✅ `lc-101-lrf.md` (arts. 48, 52, 54) |

## O que este catálogo NÃO cobre (e para onde vai)

O catálogo acima é o dos vícios que aparecem **num ato publicado**. A tabela completa de roteamento
(pesquisa §2.3) inclui casos que não nascem de um ato do diário — crime de responsabilidade do
prefeito (DL 201/67), infração político-administrativa (DL 201, art. 5º — denúncia por qualquer
eleitor), recusa/silêncio a pedido de LAI, ato lesivo já consumado (ação popular). **Esses vivem no
`roteador-vicio-orgao` (C3)**, não aqui. Quando um deles aparecer, aponte para o roteador, não force
no catálogo de detecção.

## Travas / limites

- **Não é exaustivo** — é o ponto de partida da pesquisa §2.2; um ato pode ter vício fora desta lista.
- **Respeite o nível de lastro.** ✅ cita com firmeza; 📄 cita o número mas o gerador confirma o
  rol/limite na norma vigente antes de a peça citar o dispositivo; [VERIFICAR] é pendência de fonte —
  nunca preencha o conteúdo do artigo de memória (invariante #1).
- **Classifica, não roteia nem redige.** Órgão é do `roteador-vicio-orgao`; peça é de C3; cálculo de
  percentual (aditivo, gasto com pessoal) é do `calculosjudiciais-adv-os`.
- **Sem lastro, não há vício classificável** — ato com `[LASTRO INCOMPLETO]` volta ao
  `leitor-diario-oficial` antes de classificar (P1/P5).
- **Nomeação sem concurso × nepotismo** podem coexistir na mesma portaria — cheque os dois.
- Autoria "IA Combativa". Classificação técnica de vício, não juízo de culpa: a culpa se apura, a peça
  de C3 é sempre pedido de apuração (P2).
