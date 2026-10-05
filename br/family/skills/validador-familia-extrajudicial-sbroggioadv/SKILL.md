---
name: validador-familia-extrajudicial-sbroggioadv
title: Validador normativo — advogado dos interessados
description: Esta skill deve ser usada pelo advogado dos interessados para conferir redação, vigência, temporalidade, destinatário, alcance federal e estadual e tensões de cada fundamento do familia-extrajudicial-os. Emite selo rastreável por fundamento; não cria prova dos fatos nem substitui o guard.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/validador-familia-extrajudicial
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: family
language: pt
---

# Validador normativo — advogado dos interessados

## Conferir cada fundamento

Receber rascunho/matriz, resultado do guard, datas do fato/ato, UFs e arquivos literais/manifesto de `context/`. Se ausentes, listar dependência e suspender conclusão correspondente. Não buscar artigo por memória nem usar fonte secundária. Conferir presença do **dispositivo**, não somente do arquivo; apontar recorte e remissão não capturada. Guidance only: controle por instrução, sem enforcement por hook.

Para cada fundamento registrar: diploma/dispositivo; arquivo e URL oficial de proveniência; versão/publicação/captura; hash quando disponível e conferência de integridade; trecho literal; data do fato/ato; alteradores/revogações/remissões; destinatário/objeto; federal×UF; alcance e pendência. Se manifesto/hash faltar, não certificar integridade. Se atualização/suspensão não foi varrida, registrar como não comprovada; silêncio de recorte não prova inexistência.

Classificar **✅ texto conferido no alcance indicado**, **🟡 fonte, atualização, prova ou aplicação pendente**, **🔴 contradição, formulação superada ou hipótese bloqueada**. ✅ não significa cabimento do caso nem aprovação de lavratura. Inferência recebe essa identificação e aplicação humana pendente. Não dar selo de versão atual só pela data do arquivo. Usar somente corpus local desta entrega; atualização externa ausente fica pendente, sem consulta a Jusbrasil/Escavador.

## Travas normativas obrigatórias

| Conferência | Arquivo literal em `context/` e dispositivo |
|---|---|
| CPC histórico não governa o atual; assistência e fronteira | `cpc-familia-extrajudicial.md`: 610/733/1.046; `lei-11441-historica.md` somente histórica |
| Menor/incapaz, testamento e conflito de textos | `res-cnj-35-compilada.md`: 12-A/12-B/21; `cpc-familia-extrajudicial.md`: 610; `cc-familia-sucessoes.md`: 2.016. Preservar C2/C4; administrativo não revoga lei por inferência |
| Nascituro/filhos na dissolução | CPC 733; R35 34/35/46-A; `cnn-familia-centrais-eletronico.md`: 537, §6º. Nascituro bloqueado no produto; filhos incapazes exigem análise humana explícita e prova. Não inventar trânsito geral no 34, §2º. Assistência da escritura = CPC 733, §2º / R35 8 e 46-A; CNN 537, §3º, IV não se transporta para a escritura (é termo RCPN) |
| Consulta RCTO não se generaliza a divórcio | CNN 441, II; `prov-cnj-56-rcto.md`: 1º–2º, no âmbito de inventário |
| ITCMD prévio e fração transferida | R35 15 na redação 695/2026, 22, g/38. Não exigir prévio universal no inventário nem estender dispensa ao divórcio ou chamar dispensa de isenção |
| Fato gerador e efeitos da LC227 | `lc-227-2026-itcmd.md`: 147/150/151/160/182, III. Publicação 14/01/2026, não data da lei 13/01; óbito distinto de excesso na escritura; homologação pertence à administração |
| CTN em seu âmbito atual | `ctn-itbi-contraste.md`: 35–42; preservar revogados; não usar antigo bloco como ITCMD vigente |
| Renúncia/cessão | CC 1.793–1.795/1.806/1.808–1.813: preferência/ineficácia, irrevogabilidade, acrescimento na sucessão legítima e direito próprio por cabeça, sem representação do renunciante |
| Seguro e benefício por morte | `lei-15040-seguro.md`: 116/133/134; LC227 150, III. Não incluir automaticamente na herança. CC arts. 757 a 802 revogados pelo art. 133 da Lei 15.040/2024 (`lei-15040-seguro.md`); regra vigente = art. 116 da mesma lei |
| Registro/certidões/rito | R35 40; CNN 537/539/541/544–548; `lrp-familia-duvida.md`: 198–204/296. Não criar assento de casamento para união nem importar prazo/rito registral para notas |
| Meação, vocação e poderes | CC 1.658–1.659/1.725/1.829; 1.829 não é rol de herdeiros necessários; R35 11, §2º = busca bancária/fiscal e levantamento para despesas do inventário pelo inventariante nomeado nos termos do §1º; R35 11-A, §2º = extinção da garantia após cumprimento da obrigação, não poder de levantamento |
| Proteção de dados e ética | `lgpd.md`: 6º/7º/11; `codigo-etica-oab.md`: 19/20/22/35–38; conferir literal e conflito real, sem presumir representação conjunta |

## Limites que não recebem selo automático

Normas/tabelas/alíquotas/prazos/ritos de UF, inteiro teor jurisprudencial não capturado, decisões suspensivas e operação real do e-Notariado. Não criar cobertura nacional pela ausência de regra localizada. CNN eletrônico 286–319 é recorte; competência concreta requer conferência por ato, não algoritmo universal. Fonte inacessível mantém 🟡 e bloqueia a conclusão dependente; não emitir selo fictício de atualização.

## Saída

Entregar matriz **fundamento → trecho/arquivo/versão → selo → alcance → pendência → etapa impedida**. Destacar C2 (lei×R35 e III×IV), C3 (nascituro) e C4 (negativa de testamento); análise humana registrada não autoriza hipótese proibida nem fabrica solução oficial. Remeter à Suprema Corte R1→R4 na cadeia, sem chamada recursiva. Nunca substituir o exame de documentos pelo selo da norma. Para a entrega final usar os estados do master e manter responsável externo explícito.
