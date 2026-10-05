---
name: orientacao-pos-escritura-familiar-sbroggioadv
title: Orientação pós-escritura familiar
description: Organiza providências e acompanhamento após escritura real de divórcio, união estável ou inventário. Use para averbação, Livro E, transferência de bens, obrigações fiscais e comprovação de conclusão.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/orientacao-pos-escritura-familiar
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: family
language: pt
---

# Orientação pós-escritura familiar

> Camada C6. Preparação e acompanhamento pelo advogado dos interessados.

## Entrada

Escritura/traslado real e íntegro, ato e data, interessados e bens; registros anteriores e certidões reais; guias, pagamentos, comunicações e protocolos; UF(s) e fontes locais disponíveis. Sem escritura real, produzir somente plano prospectivo marcado como tal, sem declarar pós-ato concluído.

## Âncoras a ler

- `context/res-cnj-35-compilada.md`: arts. 3, 15, 40–43 e 46-A.
- `context/cnn-familia-centrais-eletronico.md`: arts. 539–546, com remissões e limites do título.
- `context/lc-227-2026-itcmd.md`: art. 163, II e destinatário; situação fiscal segue a skill de ITCMD.

## Procedimento

1. Conferir ato lavrado e eficácia real, sem presumir que minuta, agendamento ou protocolo sejam escritura. Não dar por satisfeita condição externa ausente, inclusive MP favorável. Divergência relevante do título exige revisão do advogado.
2. Inventário: mapear bem/direito e destinatário da transferência/levantamento, com escritura como título hábil (R35 3). Listar registros imobiliários, DETRAN, Junta, instituições financeiras e demais órgãos somente conforme acervo. Não afirmar que escritura transfere automaticamente tudo ou garante levantamento.
3. Divórcio: orientar apresentação do traslado ao RCPN do assento de casamento para averbação (40/43). Havendo nome alterado, distinguir anotação de nascimento/comunicação pelo oficial (41), sem atribuir ao advogado dever do serviço. Ausência de sigilo da escritura (42) não autoriza divulgação indiscriminada do dossiê privado.
4. União estável: orientação de registro do título no Livro E segundo competência do 539, sem enviar toda dissolução ao assento de casamento. Registro prévio não é exigível para registrar dissolução (544); se houver, averbação à margem. Preservar restrições de pessoas casadas (545), datas registráveis e limites das remissões (539/541); os 15/90 dias do 541 valem só para aquele registro no Livro E; não universalizar para outras providências (T11/ACHADOS C10); registro não converte união em casamento (546). Anotações e comunicações de 543 pertencem ao oficial. Não transformar orientação em módulo autônomo de conversão/alteração/certificação.
5. ITCMD: registrar obrigações principais/acessórias e situação comprovada; dispensa prévia do inventário não é quitação/isenção (15). Comunicação ao fisco em cinco dias ou conforme legislação é do tabelião na hipótese do §2º; art. 163, II da LC227 destina informações aos titulares dos serviços, não cria obrigação substitutiva do advogado. Acompanhar evidências sem gerar comprovante.
6. Para cada providência, indicar interessado/advogado/serviço/órgão competente, documento, fundamento, protocolo real ou pendente, próxima ação e prazo apenas com base aplicável. Tabelas, formulários, prazos e fluxos locais não capturados permanecem 🟡.
7. Encerrar apenas itens demonstrados por certidão/registro/recibo pertinente. Separar enviado, recebido, registrado e confirmado. Se surgirem exigências reais, chamar `cumprimento-de-exigencias-do-ato`; não considerar silêncio do órgão como êxito.

## Saída

Checklist por ato/bem: providência, responsável, destinatário, documento, fundamento, condição, protocolo, prova final e pendência. Entregar orientação ao cliente para revisão do advogado e quadro de acompanhamento; conclusão parcial explícita quando faltarem comprovantes.

## Limites

Não emite certidão, registra, averba, acessa central ou efetua pagamento. Não exige registro prévio de união, promete retroatividade de datas/regime, substitui obrigações do serviço nem declara cumprimento sem prova. 🔴 Tensão de cabimento ou eficácia no título deve continuar no relatório e receber análise humana.

## Fontes, sigilo e revisão obrigatória

Leia os anexos indicados em `context/` e o trecho literal antes de aplicar qualquer fundamento. Ausência de arquivo, redação, versão ou prova impede selo favorável; registre a lacuna. Use exclusivamente o corpus aprovado, sem Jusbrasil, Escavador, norma estadual presumida ou artigo conhecido apenas de memória. Data de captura não prova vigência atual: declare atualização/suspensão não conferida. Preserve números, negadores, ressalvas e marcadores de revogação; normalize apenas espaços e quebras de linha na comparação.

Guarde documentos e resultados somente na pasta privada escolhida pelo advogado, separados por cliente e matéria, fora do source compartilhado. Não transmita dados nem pratique ato externo por iniciativa própria. Estas instruções são guidance only, executadas pelo agente; não equivalem a enforcement por hook ou a aprovação de autoridade.

Ao final, inclusive em saída bloqueada, execute nesta ordem:
1. `anti-alucinacao-familia-extrajudicial`: conferir cada fato/citação e a prova de eventos externos; retirar afirmações sem lastro.
2. `validador-familia-extrajudicial`: registrar selo por fundamento com diploma/dispositivo, arquivo e trecho, versão/captura, data do fato/ato, destinatário, alcance e pendência; 🟡/🔴 nunca são aprovação automática.
3. `suprema-corte-familia-extrajudicial`: R1 fatos, provas, consenso e ator → R2 fundamentos, vigência e tensões → R3 documentos, cálculos, UF e condições externas → R4 postura, sigilo, fronteiras e encaminhamento.
Se qualquer controle estiver ausente ou não executado, declarar revisão pendente e bloquear entrega como pronta. Não converter revisão interna em fé pública, homologação fiscal ou confirmação de cartório.
