import { PrismaClient } from '@prisma/client'
import { PrismaLibSQL } from '@prisma/adapter-libsql'

const globalForPrisma = globalThis as unknown as {
  prisma: PrismaClient | undefined
}

// Detect Turso/production environment
const isTurso =
  typeof process !== 'undefined' &&
  process.env.DATABASE_URL?.startsWith('libsql://') &&
  !!process.env.TURSO_AUTH_TOKEN

function initDb(): PrismaClient {
  if (isTurso) {
    // Production: use libsql adapter for Turso
    // PrismaLibSQL accepts Config object directly (not a pre-created client)
    const adapter = new PrismaLibSQL({
      url: process.env.DATABASE_URL!,
      authToken: process.env.TURSO_AUTH_TOKEN!,
    })
    return new PrismaClient({ adapter })
  }

  // Local dev: SQLite file
  return new PrismaClient({
    log: process.env.NODE_ENV !== 'production' ? ['error', 'warn'] : ['error'],
  })
}

export const db = globalForPrisma.prisma ?? initDb()

if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = db
