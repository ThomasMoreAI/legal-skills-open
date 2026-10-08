---
name: cessao-de-precatorio-sbroggioadv
title: Cessão de precatório
description: Estrutura a escritura e as duas comunicações da cessão notarial de precatório pelo art. 6º-A da Lei 8.935/1994, incluído pela Lei 14.711/2023, controlando os prazos imediato, de 3 dias úteis e de 15 dias corridos sem inventar rito nacional inexistente. Esta skill deve ser usada quando o pedido mencionar cessão de precatório, crédito reconhecido judicialmente, negociação em curso, comunicação ao tribunal, janela de exclusividade, central notarial, cessionário ou escritura de cessão de crédito judicial.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/tabelionato-os-marketplace/tree/main/tabelionato-os/skills/cessao-de-precatorio
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# Cessão de precatório

> Camada C5. Controlar duas comunicações e dois relógios; o instituto não passa pelo Registro de Imóveis.

## Anexos e skills obrigatórios

- `context/lei-8935-94.md` — art. 6º-A e competências notariais;
- `context/travas-defasagem.md` — trava T-82 e lacuna regulamentar;
- `context/sequencia-do-ato.md` — qualificação, escritura e comunicações;
- `varredura-de-vigencia-pre-lavratura`, `roteador-uf`, `escritura-publica` e `qualificacao-notarial-transversal`.

## Endereço normativo

Fixar que o art. 6º-A da Lei 8.935/1994 foi incluído pela **Lei 14.711/2023**. Não confundir essa competência com o art. 216-B da LRP, que veio da Lei 14.382/2022.

Declarar o estado do corpus: não há ocorrência de precatório no CNN nem rito nacional específico confirmado; a implementação da central notarial nacional do §2º também não está confirmada. Verificar norma superveniente, disciplina do tribunal e norma da UF antes de operacionalizar. Não alegar cobertura paulista porque a íntegra do Provimento CSM 2.753/2024 não integra o corpus canônico.

## Entradas bloqueantes

Confirmar UF, tribunal ou juízo, número e natureza do crédito, trânsito em julgado, credor atual, pessoa ou pessoas identificadas na negociação, cadeia de cessões, fração ou valor cedido, constrições conhecidas, data e prova de recebimento da primeira comunicação pelo juízo, data projetada da escritura e canal institucional disponível. Tratar dados do crédito com minimização e sigilo; não reproduzir dados sensíveis desnecessários.

## As duas comunicações

1. **Negociação em curso:** comunicar ao juiz da vara ou ao tribunal **imediatamente**, a pedido dos interessados, identificando quem participa da negociação.
2. **Cessão realizada:** depois da assinatura da escritura, comunicar ao mesmo destinatário em até **3 dias úteis**, contados da assinatura.

Não fundir as mensagens nem trocar o termo inicial. Registrar protocolo, destinatário, data, hora, conteúdo mínimo e comprovante de cada comunicação.

## Janela de 15 dias corridos

Contar **15 dias corridos desde o recebimento da comunicação de negociação pelo juízo**, não desde o envio nem desde a assinatura. Se a escritura for lavrada dentro da janela, são ineficazes as cessões feitas a pessoas não identificadas na comunicação notarial.

Apresentar a data-limite e a situação da janela sem dizer que o prazo convalida a cessão, bloqueia toda negociação ou substitui a qualificação do crédito. Passada a janela, cai a proteção específica do art. 6º-A; não inventar efeito adicional.

## Fase notarial × fase judicial

### Tabelião de notas

Qualificar o negócio, enviar a comunicação imediata, lavrar a escritura e enviar a segunda comunicação em 3 dias úteis.

### Juízo ou tribunal

Receber as comunicações, fazê-las constar das informações ou consultas e registrar a cessão segundo o regime judicial aplicável. Não atribuir essa atividade ao RI nem dizer que existe fase registral imobiliária.

## Saída

Entregar estado regulatório, qualificação da cadeia, quadro das comunicações, comprovante do recebimento inicial, contagem dos 15 dias corridos, prazo da comunicação pós-escritura, pendências do tribunal/UF e trilha de auditoria.

## Reprovação automática

- atribuir o art. 6º-A à Lei 14.382/2022;
- comunicar apenas depois da escritura;
- tratar 3 dias como corridos;
- tratar 15 dias como úteis ou contar do envio;
- omitir identificação da pessoa negociadora;
- inventar rito do CNN ou central nacional operante;
- atribuir fase ao Registro de Imóveis;
- expor dados sensíveis além do necessário.
