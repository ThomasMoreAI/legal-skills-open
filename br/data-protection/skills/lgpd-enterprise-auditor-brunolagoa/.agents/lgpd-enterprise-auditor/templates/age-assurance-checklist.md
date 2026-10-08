# Checklist — aferição de idade (ECA Digital)

Roteiro auditável de mecanismos confiáveis de aferição de idade, alinhado aos **arts. 9º a 15 e 24 da Lei nº 15.211/2025**, às orientações preliminares da ANPD (março/2026) e ao Radar Tecnológico nº 5. Usar junto de [[eca-digital]].

Regra de leitura: a **vedação expressa à autodeclaração** está no art. 9º, §1º e alcança serviços com conteúdo impróprio, inadequado ou proibido a menores de 18 anos, exigindo verificação **a cada acesso**. Nos demais serviços, a autodeclaração isolada não satisfaz os arts. 10, 12 e 14 nem os "esforços razoáveis" do art. 14, §5º da LGPD.

## 1. Identificação de escopo
| Item | Resposta | Evidência |
|---|---|---|
| O serviço é direcionado a menores de 18 anos? | | |
| O serviço é provavelmente acessado por menores? | | |
| Há cadastro de usuário? | | |
| Quantos usuários menores de 18 anos registrados? | | |
| Classificação etária nas lojas de aplicativos | | |

Se qualquer resposta indicar presença de menores, o restante do checklist é obrigatório.

## 2. Mecanismo de aferição
| Requisito | Base | Status | Evidência |
|---|---|---|---|
| Existe mecanismo de aferição de idade | art. 10 | `CONFORME / PARCIAL / NAO_CONFORME` | |
| Conteúdo impróprio/adulto: verificação confiável **a cada acesso**, sem autodeclaração | art. 9º, §1º | | |
| Conteúdo pornográfico: criação de conta por menores é impedida | art. 9º, §3º | | |
| O mecanismo é proporcional, **auditável** e tecnicamente seguro | art. 12, I | | |
| Há trilha técnica do resultado da aferição (log/atributo de conta) | art. 12, I | | |
| O fornecedor consome o **sinal de idade** da loja/SO | art. 14 | | |
| Existe mecanismo **próprio** de bloqueio, independente da loja/SO | art. 14, par. único | | |
| Há reavaliação diante de fundados indícios de conta infantil | art. 24, §3º | | |

**Autodeclaração isolada = `NAO_CONFORME`.** Não aceitar checkbox "declaro ter mais de 18 anos" como evidência.

## 2.1 Lojas de aplicativos e sistemas operacionais (art. 12)
Preencher apenas quando o auditado for provedor de loja de aplicações ou de sistema operacional de terminal.

| Requisito | Base | Status | Evidência |
|---|---|---|---|
| Aferição de idade/faixa etária com medidas proporcionais e auditáveis | art. 12, I | | |
| Configuração de supervisão parental pelos responsáveis | art. 12, II | | |
| **API segura de sinal de idade** aos provedores de aplicações, privacy by default | art. 12, III | | |
| Minimização: vedado compartilhamento contínuo, automatizado e irrestrito | art. 12, §1º | | |
| Download por menores exige consentimento do responsável, sem presunção por silêncio | art. 12, §2º | | |

## 3. Minimização e finalidade
| Requisito | Base | Status | Evidência |
|---|---|---|---|
| Dados de aferição usados **exclusivamente** para verificar idade | art. 13 | | |
| Vedado reuso para marketing, perfilamento, antifraude ou treinamento de modelo | arts. 13 e 26 | | |
| Dados de confirmação de identidade em conta suspeita usados só para verificação | art. 24, §3º | | |
| Preferência por prova de faixa etária em vez de documento completo | art. 12, §1º | | |
| Documento/biometria descartado após a verificação, ou retenção justificada e prazada | art. 13 | | |
| Dado biométrico tratado como sensível, com base legal própria | LGPD art. 11 | | |
| Transferência internacional do provedor de verificação com mecanismo do art. 33 | LGPD art. 33 | | |

## 4. Vinculação a responsável (até 16 anos)
| Requisito | Base | Status | Evidência |
|---|---|---|---|
| Conta de usuário de **até 16 anos** vinculada à conta de um responsável legal | art. 24 | | |
| O vínculo é verificado, não apenas declarado | art. 24 | | |
| Diante de indícios de conta infantil irregular: suspensão de acesso | art. 24, §4º | | |
| Procedimento célere e acessível de apelação pelo responsável | art. 24, §4º | | |
| Sem conta de responsável, é vedado reduzir o nível de proteção padrão | art. 24, §5º | | |
| Responsável controla tempo de uso, contatos e conteúdos | arts. 17 e 18 | | |
| Consentimento parental específico e em destaque coletado | LGPD art. 14, §1º | | |

## 5. Efeitos da aferição no produto
| Requisito | Base | Status | Evidência |
|---|---|---|---|
| Perfil de menor nasce no modelo mais protetivo disponível | art. 7º | | |
| Geolocalização restrita por padrão, com aviso claro de rastreamento | art. 17, §4º, VI | | |
| Comunicação por usuários não autorizados restrita por padrão | art. 17, §4º, I | | |
| Recursos de uso compulsivo limitados (autoplay, recompensa por tempo, notificações) | arts. 8º, IV e 17, §4º, II | | |
| Recomendação personalizada controlável, com opção de desativação | art. 17, §4º, V | | |
| Publicidade por perfilamento, análise emocional ou RA/RV vedada para menores | arts. 22 e 26 | | |
| Compras e transações financeiras restringíveis pelo responsável | art. 18, II | | |
| Caixas de recompensa (loot boxes) ausentes em jogo de acesso provável | art. 20 | | |
| Ausência de dark patterns que enfraqueçam salvaguardas | art. 18, §2º | | |

## 6. Acessibilidade, inclusão e recurso
| Requisito | Status | Evidência |
|---|---|---|
| Existe rota alternativa para quem não possui documento | | |
| Existe canal de contestação de aferição incorreta | | |
| O mecanismo não discrimina por origem, deficiência ou condição socioeconômica (art. 6º, IX, LGPD) | | |
| Taxa de erro do mecanismo é medida e documentada | | |

## 7. Fecho de auditoria
- Severidade sugerida para conteúdo adulto sem verificação a cada acesso (art. 9º, §1º): `CRITICO`.
- Severidade sugerida para reuso indevido dos dados de aferição (art. 13): `ALTO`.
- Lembrar da **responsabilidade solidária** de toda a cadeia digital (art. 15): loja, SO e aplicação respondem cada um por sua parte.
- Fundamentação obrigatória: artigo do ECA Digital **+** art. 14 e art. 6º, I da LGPD.
- Registrar `evidence_type` (`ENCONTRADA | PARCIAL | AUSENTE`) e `evidence_source` (`TECNICA | DOCUMENTAL`) por linha preenchida.
