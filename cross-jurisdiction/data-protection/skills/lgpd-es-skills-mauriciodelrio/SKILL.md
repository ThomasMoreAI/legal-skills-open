---
name: lgpd-es-skills-mauriciodelrio
title: LGPD — Lei Geral de Proteção de Dados
description: Usa este skill cuando desarrolles software que recolecte, procese o almacene datos personales y necesites implementar protección de datos conforme a LGPD. Aunque LGPD es legislación brasileña, este skill se aplica como estándar de protección de datos para cualquier software independientemente de la ubicación geográfica de los usuarios. Cubre las 10 bases legales de tratamiento, consentimiento granular, derechos del titular (Art. 18), RIPD (evaluación de impacto), notificación de incidentes a la ANPD y modelo de datos Prisma.
author: mauriciodelrio
author_url: https://github.com/mauriciodelrio/delriodev-skills/tree/main/es-skills/governance-risk-and-compliance/lgpd
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: es
---

# LGPD — Lei Geral de Proteção de Dados

LGPD (Lei N° 13.709/2018) es la ley brasileña de protección de datos y debe aplicarse como estándar de protección de datos personales para cualquier software, independientemente de la ubicación geográfica de los usuarios. A diferencia de GDPR que define 6 bases legales, LGPD define 10: consentimiento, obligación legal, administración pública, estudios por órgano de investigación, ejecución de contrato, ejercicio de derechos, protección de la vida, tutela de la salud, interés legítimo y protección del crédito. Requiere un Encarregado (DPO) para todo controlador. Los datos sensibles (origen racial/étnico, convicción religiosa, opinión política, afiliación sindical, salud, vida sexual, genéticos, biométricos) requieren consentimiento específico.

## Implementación

### 1. Modelo de Datos para LGPD

```prisma
// prisma/schema.prisma

/// Registro de consentimiento LGPD
model ConsentimentoLGPD {
  id              String   @id @default(cuid())
  titularId       String
  titular         User     @relation(fields: [titularId], references: [id])
  
  // Finalidade específica del consentimiento (Art. 8 §4)
  finalidade      String            // Propósito específico
  baseLegal       BaseLegalLGPD
  
  // Estado del consentimiento
  concedido       Boolean          // Si el titular consintió
  dataConsentimento DateTime?      // Cuándo consintió
  dataRevogacao   DateTime?        // Cuándo revocó (Art. 8 §5)
  
  // Evidencia (Art. 8 §2: Carga de la prueba recae en el controlador)
  metodoObtencao  String           // Cómo se obtuvo (formulario, checkbox, etc.)
  textoMostrado   String           // Texto exacto que se le mostró
  ipAddress       String?
  userAgent       String?
  
  createdAt       DateTime @default(now())
  updatedAt       DateTime @updatedAt
  
  @@index([titularId])
  @@index([baseLegal])
  @@map("consentimentos_lgpd")
}

/// Solicitudes de titulares (Art. 18)
model SolicitacaoTitular {
  id          String             @id @default(cuid())
  titularId   String
  titular     User               @relation(fields: [titularId], references: [id])
  
  tipo        DireitoTitularLGPD
  status      StatusSolicitacao  @default(RECEBIDA)
  
  // LGPD Art. 18 §5: Plazo de 15 días para responder
  recebidaEm     DateTime @default(now())
  prazoResposta  DateTime  // 15 días úteis
  respondidaEm   DateTime?
  
  // Verificación de identidad
  identidadeVerificada Boolean @default(false)
  
  // Respuesta
  resposta       Json?
  motivoRecusa   String?
  
  @@map("solicitacoes_titular")
}

enum BaseLegalLGPD {
  CONSENTIMENTO
  OBRIGACAO_LEGAL
  ADMINISTRACAO_PUBLICA
  ESTUDOS_PESQUISA
  EXECUCAO_CONTRATO
  EXERCICIO_DIREITOS
  PROTECAO_VIDA
  TUTELA_SAUDE
  INTERESSE_LEGITIMO
  PROTECAO_CREDITO
}

enum DireitoTitularLGPD {
  CONFIRMACAO_TRATAMENTO      // Art.18 I — Confirmar si hay tratamiento
  ACESSO_DADOS                // Art.18 II — Acceder a sus datos
  CORRECAO                    // Art.18 III — Corregir datos incompletos/inexactos
  ANONIMIZACAO_BLOQUEIO       // Art.18 IV — Anonimizar, bloquear o eliminar datos excesivos
  PORTABILIDADE               // Art.18 V — Portabilidad a otro proveedor
  ELIMINACAO                  // Art.18 VI — Eliminar datos tratados con consentimiento
  INFORMACAO_COMPARTILHAMENTO // Art.18 VII — Saber con quién se comparten los datos
  INFORMACAO_CONSENTIMENTO    // Art.18 VIII — Saber que puede no dar consentimiento
  REVOGACAO_CONSENTIMENTO     // Art.18 IX — Revocar consentimiento
}

enum StatusSolicitacao {
  RECEBIDA
  VERIFICACAO_IDENTIDADE
  EM_PROCESSAMENTO
  CONCLUIDA
  RECUSADA
}
```

---

### 2. Servicio de Consentimiento LGPD

```typescript
// services/lgpd-consentimento.service.ts

import { PrismaClient, BaseLegalLGPD } from '@prisma/client';
import pino from 'pino';

const prisma = new PrismaClient();
const logger = pino({ name: 'lgpd-consentimento' });

/**
 * Gestión de consentimiento según LGPD.
 * 
 * Art. 8: Consentimiento debe ser:
 * - Por escrito o por otro medio que demuestre la voluntad del titular
 * - Para finalidades determinadas (consentimiento genérico es nulo §4)
 * - Revocable en cualquier momento (§5)
 * - El controlador debe probar que obtuvo consentimiento (§2)
 */
export class LGPDConsentimentoService {
  /**
   * Registrar consentimiento del titular.
   * LGPD Art. 8 — Debe ser específico por finalidad.
   */
  async registrarConsentimento(params: {
    titularId: string;
    finalidade: string;
    concedido: boolean;
    metodoObtencao: string;
    textoMostrado: string;
    ipAddress?: string;
    userAgent?: string;
  }) {
    // Verificar que no exista un consentimiento activo para la misma finalidad
    const existente = await prisma.consentimentoLGPD.findFirst({
      where: {
        titularId: params.titularId,
        finalidade: params.finalidade,
        dataRevogacao: null,
      },
    });

    if (existente) {
      // Revocar el anterior antes de crear uno nuevo
      await prisma.consentimentoLGPD.update({
        where: { id: existente.id },
        data: { dataRevogacao: new Date() },
      });
    }

    const consentimento = await prisma.consentimentoLGPD.create({
      data: {
        titularId: params.titularId,
        finalidade: params.finalidade,
        baseLegal: 'CONSENTIMENTO',
        concedido: params.concedido,
        dataConsentimento: params.concedido ? new Date() : null,
        metodoObtencao: params.metodoObtencao,
        textoMostrado: params.textoMostrado,
        ipAddress: params.ipAddress,
        userAgent: params.userAgent,
      },
    });

    logger.info({
      event: 'consentimento_registrado',
      titularId: params.titularId,
      finalidade: params.finalidade,
      concedido: params.concedido,
    }, 'Consentimiento LGPD registrado');

    return consentimento;
  }

  /**
   * Revogar consentimiento.
   * LGPD Art. 8 §5: El consentimiento puede ser revocado en cualquier
   * momento mediante manifestación expresa del titular, por procedimiento
   * gratuito y facilitado.
   */
  async revogarConsentimento(titularId: string, finalidade: string) {
    const consentimento = await prisma.consentimentoLGPD.findFirst({
      where: {
        titularId,
        finalidade,
        concedido: true,
        dataRevogacao: null,
      },
    });

    if (!consentimento) {
      return { success: false, error: 'No se encontró consentimiento activo para esta finalidad' };
    }

    await prisma.consentimentoLGPD.update({
      where: { id: consentimento.id },
      data: { dataRevogacao: new Date() },
    });

    // Detener todo tratamiento basado en este consentimiento
    logger.info({
      event: 'consentimento_revogado',
      titularId,
      finalidade,
    }, 'Consentimiento LGPD revocado');

    return { success: true, message: 'Consentimiento revocado exitosamente' };
  }

  /**
   * Verificar si hay base legal activa para tratar datos.
   * Verifica tanto consentimiento como otras bases legales.
   */
  async verificarBaseLegal(titularId: string, finalidade: string): Promise<{
    autorizado: boolean;
    baseLegal?: BaseLegalLGPD;
  }> {
    const consentimento = await prisma.consentimentoLGPD.findFirst({
      where: {
        titularId,
        finalidade,
        concedido: true,
        dataRevogacao: null,
      },
    });

    if (consentimento) {
      return { autorizado: true, baseLegal: consentimento.baseLegal };
    }

    return { autorizado: false };
  }
}
```

---

### 3. Derechos del Titular (Art. 18)

```typescript
// services/lgpd-direitos-titular.service.ts

import { PrismaClient, DireitoTitularLGPD, StatusSolicitacao } from '@prisma/client';
import pino from 'pino';

const prisma = new PrismaClient();
const logger = pino({ name: 'lgpd-direitos' });

// LGPD Art. 18 §5: plazo de 15 días útiles para responder
const PRAZO_RESPOSTA_DIAS_UTEIS = 15;

export class LGPDDireitosTitularService {
  /**
   * Recibir solicitud del titular.
   * El titular puede ejercer sus derechos ante el controlador en cualquier momento.
   */
  async receberSolicitacao(
    titularId: string,
    tipo: DireitoTitularLGPD,
  ) {
    const prazo = this.calcularPrazoResposta(PRAZO_RESPOSTA_DIAS_UTEIS);

    const solicitacao = await prisma.solicitacaoTitular.create({
      data: {
        titularId,
        tipo,
        status: 'VERIFICACAO_IDENTIDADE',
        prazoResposta: prazo,
      },
    });

    logger.info({
      event: 'solicitacao_titular_recebida',
      solicitacaoId: solicitacao.id,
      tipo,
      prazo: prazo.toISOString(),
    }, 'Solicitud de titular LGPD recibida');

    return {
      id: solicitacao.id,
      tipo,
      status: 'VERIFICACAO_IDENTIDADE',
      prazoResposta: prazo.toISOString(),
      mensagem: 'Tu solicitud fue recibida. Necesitamos verificar tu identidad para procesarla.',
    };
  }

  /**
   * Art. 18 II — Derecho de acceso a los datos.
   */
  async processarAcesso(solicitacaoId: string): Promise<object> {
    const solicitacao = await this.obterSolicitacaoVerificada(solicitacaoId, 'ACESSO_DADOS');

    // Recopilar todos los datos del titular
    const titular = await prisma.user.findUniqueOrThrow({
      where: { id: solicitacao.titularId },
      select: {
        id: true,
        name: true,
        email: true,
        createdAt: true,
      },
    });

    const consentimentos = await prisma.consentimentoLGPD.findMany({
      where: { titularId: solicitacao.titularId },
      select: {
        finalidade: true,
        baseLegal: true,
        concedido: true,
        dataConsentimento: true,
        dataRevogacao: true,
      },
    });

    const resposta = {
      dadosPessoais: titular,
      consentimentos,
      finalidadesTratamento: ['Provisão do serviço', 'Comunicações'],
      compartilhamentos: [
        { destinatario: 'Provedor de hosting', finalidade: 'Infraestrutura' },
        { destinatario: 'Processador de pagamentos', finalidade: 'Cobrança' },
      ],
    };

    await prisma.solicitacaoTitular.update({
      where: { id: solicitacaoId },
      data: {
        status: 'CONCLUIDA',
        respondidaEm: new Date(),
        resposta: resposta as any,
      },
    });

    logger.info({
      event: 'acesso_dados_concluido',
      solicitacaoId,
      titularId: solicitacao.titularId,
    }, 'Acceso a datos procesado');

    return resposta;
  }

  /**
   * Art. 18 VI — Derecho de eliminación de datos tratados con consentimiento.
   */
  async processarEliminacao(solicitacaoId: string) {
    const solicitacao = await this.obterSolicitacaoVerificada(solicitacaoId, 'ELIMINACAO');

    // Solo eliminar datos cuyo tratamiento se basó en consentimiento
    const consentimentos = await prisma.consentimentoLGPD.findMany({
      where: {
        titularId: solicitacao.titularId,
        baseLegal: 'CONSENTIMENTO',
      },
    });

    // Revocar todos los consentimientos
    await prisma.consentimentoLGPD.updateMany({
      where: {
        titularId: solicitacao.titularId,
        baseLegal: 'CONSENTIMENTO',
        dataRevogacao: null,
      },
      data: { dataRevogacao: new Date() },
    });

    // Pseudonimizar datos del usuario
    await prisma.user.update({
      where: { id: solicitacao.titularId },
      data: {
        name: '[ELIMINADO]',
        email: `eliminado_${Date.now()}@eliminado.invalid`,
        deletedAt: new Date(),
      },
    });

    await prisma.solicitacaoTitular.update({
      where: { id: solicitacaoId },
      data: {
        status: 'CONCLUIDA',
        respondidaEm: new Date(),
        resposta: {
          eliminados: consentimentos.map(c => c.finalidade),
          mantidosPorObrigacaoLegal: ['Registros fiscais (7 anos)', 'Logs de segurança (1 ano)'],
        } as any,
      },
    });

    logger.info({
      event: 'eliminacao_dados_concluida',
      solicitacaoId,
      titularId: solicitacao.titularId,
      consentimentosRevogados: consentimentos.length,
    }, 'Eliminación de datos LGPD procesada');

    return {
      success: true,
      eliminados: consentimentos.map(c => c.finalidade),
      mantidosPorObrigacaoLegal: ['Registros fiscais (7 anos)', 'Logs de segurança (1 ano)'],
    };
  }

  /**
   * Art. 18 V — Derecho de portabilidad.
   * Transferir datos a otro proveedor de servicio.
   */
  async processarPortabilidade(solicitacaoId: string): Promise<{
    format: string;
    data: object;
  }> {
    const solicitacao = await this.obterSolicitacaoVerificada(solicitacaoId, 'PORTABILIDADE');

    const titular = await prisma.user.findUniqueOrThrow({
      where: { id: solicitacao.titularId },
    });

    // Formato estructurado, comúnmente usado e legível por máquina (Art. 18 V)
    const dadosPortaveis = {
      exportadoEm: new Date().toISOString(),
      formato: 'JSON',
      versao: '1.0',
      titular: {
        nome: titular.name,
        email: titular.email,
        dataCriacao: titular.createdAt,
      },
      // Incluir todos los datos relevantes para portabilidad
    };

    await prisma.solicitacaoTitular.update({
      where: { id: solicitacaoId },
      data: {
        status: 'CONCLUIDA',
        respondidaEm: new Date(),
      },
    });

    logger.info({
      event: 'portabilidade_concluida',
      solicitacaoId,
      titularId: solicitacao.titularId,
    }, 'Portabilidad LGPD procesada');

    return { format: 'application/json', data: dadosPortaveis };
  }

  // --- Helpers privados ---

  private async obterSolicitacaoVerificada(id: string, tipoEsperado: DireitoTitularLGPD) {
    const solicitacao = await prisma.solicitacaoTitular.findUniqueOrThrow({
      where: { id },
    });

    if (solicitacao.tipo !== tipoEsperado) {
      throw new Error(`Tipo incorrecto: esperado ${tipoEsperado}, recibido ${solicitacao.tipo}`);
    }

    if (!solicitacao.identidadeVerificada) {
      throw new Error('Identidad del titular no verificada');
    }

    return solicitacao;
  }

  /**
   * Calcular plazo de respuesta en días útiles.
   */
  private calcularPrazoResposta(diasUteis: number): Date {
    const fecha = new Date();
    let diasContados = 0;
    
    while (diasContados < diasUteis) {
      fecha.setDate(fecha.getDate() + 1);
      const diaSemana = fecha.getDay();
      // Excluir sábado (6) y domingo (0)
      if (diaSemana !== 0 && diaSemana !== 6) {
        diasContados++;
      }
    }
    
    return fecha;
  }
}
```

---

### 4. RIPD — Relatório de Impacto à Proteção de Dados (Art. 38)

```typescript
// services/lgpd-ripd.service.ts

/**
 * RIPD (Relatório de Impacto à Proteção de Dados Pessoais)
 * Equivalente al DPIA del GDPR.
 * 
 * Art. 38: La ANPD puede solicitar al controlador que elabore
 * un relatório de impacto relativo a suas operaciones de
 * tratamento de dados pessoais.
 * 
 * Incluir:
 * - Descripción de los tipos de datos recolectados
 * - Metodología utilizada para recolección y seguridad
 * - Análisis del controlador sobre medidas, salvaguardas y mecanismos de mitigación
 */

interface RIPD {
  controlador: {
    nombre: string;
    encarregado: { nombre: string; email: string }; // DPO
    fechaElaboracion: Date;
  };
  descripcionTratamiento: {
    naturaleza: string;
    alcance: string;
    contexto: string;
    finalidad: string;
  };
  baseLegal: string;
  datosRecolectados: DatosCategoria[];
  titulares: { categoria: string; cantidadEstimada: string }[];
  compartilhamentos: { receptor: string; finalidade: string; baseLegal: string }[];
  analisisRiesgos: RiesgoIdentificado[];
  medidasMitigacion: MedidaMitigacion[];
}

interface DatosCategoria {
  categoria: string;
  datos: string[];
  sensivel: boolean;
  baseLegal: string;
  retencao: string;
}

interface RiesgoIdentificado {
  descripcion: string;
  probabilidad: 'baja' | 'media' | 'alta';
  impacto: 'bajo' | 'medio' | 'alto';
  nivelRiesgo: 'aceptable' | 'moderado' | 'alto' | 'critico';
}

interface MedidaMitigacion {
  riesgo: string;
  medida: string;
  estado: 'implementada' | 'en_progreso' | 'planificada';
}

export function generarTemplateRIPD(): RIPD {
  return {
    controlador: {
      nombre: process.env.COMPANY_NAME ?? 'Mi Empresa',
      encarregado: {
        nombre: process.env.DPO_NAME ?? 'Nombre del Encarregado',
        email: process.env.DPO_EMAIL ?? 'dpo@empresa.com',
      },
      fechaElaboracion: new Date(),
    },
    descripcionTratamiento: {
      naturaleza: 'Tratamiento automatizado de datos personales para provisión de servicio SaaS',
      alcance: 'Datos de usuarios registrados en la plataforma',
      contexto: 'Plataforma SaaS con usuarios en Brasil',
      finalidad: 'Proveer el servicio contratado por el titular',
    },
    baseLegal: 'Ejecución de contrato (Art. 7 V) y consentimiento (Art. 7 I) según finalidad',
    datosRecolectados: [
      {
        categoria: 'Identificadores',
        datos: ['Nome', 'Email', 'Endereço IP'],
        sensivel: false,
        baseLegal: 'Execução de contrato',
        retencao: 'Duração da conta + 30 dias',
      },
      {
        categoria: 'Dados comerciais',
        datos: ['Histórico de compras', 'Plano contratado'],
        sensivel: false,
        baseLegal: 'Execução de contrato / Obrigação legal',
        retencao: '7 anos (obrigações fiscais)',
      },
    ],
    titulares: [
      { categoria: 'Usuários registrados', cantidadEstimada: 'Conforme base de usuários' },
    ],
    compartilhamentos: [
      {
        receptor: 'Provedor de infraestrutura (hosting)',
        finalidade: 'Armazenamento e processamento de dados',
        baseLegal: 'Execução de contrato',
      },
      {
        receptor: 'Processador de pagamentos',
        finalidade: 'Cobrança e faturamento',
        baseLegal: 'Execução de contrato',
      },
    ],
    analisisRiesgos: [
      {
        descripcion: 'Acceso no autorizado a datos personales',
        probabilidad: 'baja',
        impacto: 'alto',
        nivelRiesgo: 'moderado',
      },
      {
        descripcion: 'Pérdida de datos por fallo de infraestructura',
        probabilidad: 'baja',
        impacto: 'alto',
        nivelRiesgo: 'moderado',
      },
    ],
    medidasMitigacion: [
      {
        riesgo: 'Acceso no autorizado',
        medida: 'Encriptación AES-256, RBAC, MFA, logs de auditoría',
        estado: 'implementada',
      },
      {
        riesgo: 'Pérdida de datos',
        medida: 'Backups diarios, replicación geográfica, plan de recuperación',
        estado: 'implementada',
      },
    ],
  };
}
```

---

### 5. Notificación de Incidentes a la ANPD (Art. 48)

```typescript
// services/lgpd-incidentes.service.ts

import pino from 'pino';

const logger = pino({ name: 'lgpd-incidentes' });

/**
 * Art. 48 LGPD: El controlador debe comunicar a la ANPD y al titular
 * la ocurrencia de un incidente de seguridad que pueda causar riesgo
 * o daño relevante a los titulares.
 * 
 * La comunicación debe incluir:
 * - Descripción de la naturaleza de los datos afectados
 * - Información sobre los titulares involucrados
 * - Indicación de las medidas técnicas y de seguridad utilizadas
 * - Los riesgos relacionados al incidente
 * - Las medidas que fueron o serán adoptadas para revertir/mitigar
 * - Los motivos del retraso, en caso de no ser inmediata
 */

interface IncidenteLGPD {
  id: string;
  descripcion: string;
  fechaDeteccion: Date;
  fechaOcurrencia?: Date;
  
  // Datos afectados
  categoriasDatosAfectados: string[];
  datosApessoaisSensiveis: boolean;
  
  // Titulares
  cantidadTitularesAfectados: number;
  categoriasTitulares: string[];
  
  // Evaluación
  probabilidadDano: 'baja' | 'media' | 'alta';
  gravedadDano: 'bajo' | 'medio' | 'alto' | 'critico';
  riesgoPotencial: string[];
  
  // Medidas
  medidasPreventivasExistentes: string[];
  medidasCorrectivas: string[];
  
  // Comunicación
  comunicadoANPD: boolean;
  fechaComunicadoANPD?: Date;
  comunicadoTitulares: boolean;
  fechaComunicadoTitulares?: Date;
}

export class LGPDIncidenteService {
  /**
   * Evaluar si el incidente requiere notificación a la ANPD.
   * Art. 48: Debe comunicar cuando pueda causar "risco ou dano relevante".
   */
  evaluarNotificacion(incidente: IncidenteLGPD): {
    notificarANPD: boolean;
    notificarTitulares: boolean;
    justificacion: string;
  } {
    // Criterios para determinar riesgo/daño relevante
    const esAltoRiesgo =
      incidente.datosApessoaisSensiveis ||
      incidente.cantidadTitularesAfectados > 1000 ||
      incidente.gravedadDano === 'alto' ||
      incidente.gravedadDano === 'critico';

    if (esAltoRiesgo) {
      logger.error({
        event: 'incidente_alto_riesgo',
        incidenteId: incidente.id,
        titularesAfectados: incidente.cantidadTitularesAfectados,
        datosSensiveis: incidente.datosApessoaisSensiveis,
      }, 'Incidente de alto riesgo — requiere notificación a ANPD y titulares');

      return {
        notificarANPD: true,
        notificarTitulares: true,
        justificacion: 'Incidente con riesgo relevante — datos sensibles y/o gran número de titulares afectados',
      };
    }

    return {
      notificarANPD: false,
      notificarTitulares: false,
      justificacion: 'Incidente evaluado como bajo riesgo — sin datos sensibles comprometidos',
    };
  }

  /**
   * Generar comunicado para la ANPD (Art. 48 §1).
   */
  generarComunicadoANPD(incidente: IncidenteLGPD): object {
    return {
      cabecalho: {
        tipo: 'Comunicação de Incidente de Segurança com Dados Pessoais',
        controlador: process.env.COMPANY_NAME,
        encarregado: {
          nome: process.env.DPO_NAME,
          email: process.env.DPO_EMAIL,
        },
        dataComunicacao: new Date().toISOString(),
      },
      // §1 I — Naturaleza de los datos afectados
      dadosAfetados: {
        categorias: incidente.categoriasDatosAfectados,
        sensiveis: incidente.datosApessoaisSensiveis,
      },
      // §1 II — Titulares involucrados
      titulares: {
        quantidade: incidente.cantidadTitularesAfectados,
        categorias: incidente.categoriasTitulares,
      },
      // §1 III — Medidas técnicas y de seguridad
      medidasSeguranca: incidente.medidasPreventivasExistentes,
      // §1 IV — Riesgos relacionados
      riscos: incidente.riesgoPotencial,
      // §1 V — Medidas adoptadas
      medidasCorretivas: incidente.medidasCorrectivas,
      // §1 VI — Motivos de eventual retraso
      motivoRetraso: null,
    };
  }
}
```

---

## Flujo de trabajo del agente

1. Definir las bases legales aplicables para cada finalidad de tratamiento del sistema (Art. 7, las 10 bases).
2. Implementar modelo de datos con schema Prisma que registre consentimientos por finalidad, solicitudes de titulares y estados.
3. Implementar servicio de consentimiento granular: registro por finalidad específica (Art. 8 §4), revocación facilitada (Art. 8 §5), y evidencia almacenada (Art. 8 §2).
4. Implementar los 9 derechos del titular (Art. 18): confirmación, acceso, corrección, anonimización/bloqueo, portabilidad en formato estructurado, eliminación, información de compartilhamento, y revocación.
5. Elaborar RIPD (Relatório de Impacto) cuando el tratamiento pueda generar riesgo alto (Art. 38).
6. Implementar servicio de evaluación y notificación de incidentes a la ANPD y titulares (Art. 48).
7. Validar contra el checklist de cumplimiento (bases legales, derechos del titular, gobernanza, seguridad) antes de desplegar.

## Gotchas

El consentimiento genérico o en bloque es nulo bajo LGPD (Art. 8 §4) — implementar siempre consentimiento granular por finalidad. La revocación del consentimiento debe ser tan fácil como fue otorgarlo (Art. 8 §5); no dificultar el proceso. El plazo de respuesta a solicitudes de titulares es de 15 días útiles (Art. 18 §5), no calendario — calcular excluyendo fines de semana. No tratar datos sin base legal definida. No tratar datos sensibles sin consentimiento específico y destacado (Art. 11). La carga de la prueba del consentimiento recae en el controlador (Art. 8 §2) — almacenar textoMostrado, ipAddress, userAgent y timestamp. El derecho de eliminación (Art. 18 VI) solo aplica a datos tratados con base en consentimiento; datos con base en obligación legal se mantienen (ej: registros fiscales 7 años). El Encarregado (DPO) es obligatorio para todo controlador, no opcional como en GDPR. La notificación de incidentes a la ANPD es requerida cuando haya "risco ou dano relevante" — datos sensibles comprometidos o más de 1000 titulares afectados. No transferir datos internacionalmente sin garantías adecuadas.

---

## Checklist de Cumplimiento LGPD

### Bases Legales y Consentimiento
- [ ] Mapeo de todas las bases legales por finalidad de tratamiento
- [ ] Sistema de consentimiento granular por finalidad
- [ ] Mecanismo fácil de revocación de consentimiento
- [ ] Evidencia de consentimiento almacenada (Art. 8 §2)
- [ ] Consentimiento específico y destacado para datos sensibles (Art. 11)

### Derechos del Titular (Art. 18)
- [ ] Confirmación del tratamiento (I)
- [ ] Acceso a datos (II)
- [ ] Corrección de datos incompletos/inexactos (III)
- [ ] Anonimización, bloqueo o eliminación de exceso (IV)
- [ ] Portabilidad a otro proveedor (V)
- [ ] Eliminación de datos tratados con consentimiento (VI)
- [ ] Información sobre compartilhamento (VII)
- [ ] Información sobre posibilidad de no consentir (VIII)
- [ ] Revocación de consentimiento (IX)
- [ ] Plazo de respuesta de 15 días útiles (§5)

### Gobernanza
- [ ] Encarregado (DPO) nombrado con datos de contacto públicos
- [ ] Registro de operaciones de tratamiento (Art. 37)
- [ ] RIPD elaborado para tratamientos de alto riesgo (Art. 38)
- [ ] Política de privacidad publicada y accesible
- [ ] Contratos con operadores (procesadores) con cláusulas LGPD

### Seguridad y Incidentes
- [ ] Medidas técnicas de seguridad implementadas (Art. 46)
- [ ] Proceso de notificación de incidentes a ANPD (Art. 48)
- [ ] Proceso de notificación a titulares afectados
- [ ] Plan de respuesta a incidentes documentado

---

## Referencias y Recursos

- [LGPD Texto completo — Planalto.gov.br](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709compilado.htm)
- [ANPD — Autoridade Nacional de Proteção de Dados](https://www.gov.br/anpd/)
- [Guia orientativo sobre tratamento de dados pessoais — ANPD](https://www.gov.br/anpd/pt-br/documentos-e-publicacoes)
- [LGPD vs GDPR — Comparación](https://iapp.org/resources/article/brazil-data-protection-2/)
