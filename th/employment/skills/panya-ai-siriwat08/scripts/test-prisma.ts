import { PrismaClient } from '@prisma/client';
const db = new PrismaClient({ log: ['query', 'error', 'warn'] });
try {
  const count = await db.law.count();
  console.log('Law count:', count);
  const sample = await db.law.findFirst();
  console.log('Sample law:', sample?.lawNameTh);
} catch (e: any) {
  console.error('ERR:', e.message);
  console.error('CODE:', e.code);
} finally {
  await db.$disconnect();
}
