// Persistence for the game. Uses Postgres via Prisma when DATABASE_URL is set,
// otherwise an in-memory store (fine for a single-server demo; resets on restart).
import type { Opponent } from './config'

export type Stage = Opponent | 'done'
export interface OtpRow { phone: string; codeHash: string; expiresAt: Date; attempts: number; createdAt: Date }
export interface PlayRow { phone: string; day: string; stage: Stage; result: string | null }
export interface CouponRow { code: string; phone: string; prizeKey: string; label: string; percent: number; day: string; createdAt: Date; expiresAt: Date; redeemedAt: Date | null; voided: boolean }

export interface GameStore {
  addOtp(row: OtpRow): Promise<void>
  otpsForPhone(phone: string, since: Date): Promise<OtpRow[]>
  bumpOtpAttempts(phone: string, createdAt: Date): Promise<void>
  clearOtps(phone: string): Promise<void>
  recordConsent(phone: string): Promise<void>
  getPlay(phone: string, day: string): Promise<PlayRow | null>
  savePlay(row: PlayRow): Promise<void>
  addCoupon(row: CouponRow): Promise<void>
  voidCoupon(code: string): Promise<void>
  couponsForPhone(phone: string): Promise<CouponRow[]>
  countCoupons(prizeKey: string, day: string): Promise<number>
  findCoupon(code: string): Promise<CouponRow | null>
  redeemCoupon(code: string): Promise<void>
  stats(day: string): Promise<{ players: number; plays: number; win1: number; win2: number; redeemed: number }>
}

class MemoryStore implements GameStore {
  otps: OtpRow[] = []; plays = new Map<string, PlayRow>(); coupons = new Map<string, CouponRow>(); players = new Map<string, Date>()
  async addOtp(r: OtpRow) { this.otps.push(r) }
  async otpsForPhone(p: string, since: Date) { return this.otps.filter(o => o.phone === p && o.createdAt >= since) }
  async bumpOtpAttempts(p: string, c: Date) { const o = this.otps.find(o => o.phone === p && o.createdAt.getTime() === c.getTime()); if (o) o.attempts++ }
  async clearOtps(p: string) { this.otps = this.otps.filter(o => o.phone !== p) }
  async recordConsent(p: string) { if (!this.players.has(p)) this.players.set(p, new Date()) }
  async getPlay(p: string, d: string) { return this.plays.get(`${p}|${d}`) ?? null }
  async savePlay(r: PlayRow) { this.plays.set(`${r.phone}|${r.day}`, { ...r }) }
  async addCoupon(r: CouponRow) { this.coupons.set(r.code, { ...r }) }
  async voidCoupon(c: string) { const r = this.coupons.get(c); if (r) r.voided = true }
  async couponsForPhone(p: string) { return [...this.coupons.values()].filter(c => c.phone === p && !c.voided) }
  async countCoupons(k: string, d: string) { return [...this.coupons.values()].filter(c => c.prizeKey === k && c.day === d && !c.voided).length }
  async findCoupon(c: string) { return this.coupons.get(c) ?? null }
  async redeemCoupon(c: string) { const r = this.coupons.get(c); if (r) r.redeemedAt = new Date() }
  async stats(d: string) {
    const cs = [...this.coupons.values()].filter(c => !c.voided)
    return { players: this.players.size, plays: [...this.plays.values()].filter(p => p.day === d).length,
      win1: cs.filter(c => c.prizeKey === 'WIN1' && c.day === d).length, win2: cs.filter(c => c.prizeKey === 'WIN2' && c.day === d).length,
      redeemed: cs.filter(c => c.redeemedAt).length }
  }
}

class PrismaStore implements GameStore {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  constructor(private db: any) {}
  async addOtp(r: OtpRow) { await this.db.gameOtp.create({ data: r }) }
  async otpsForPhone(phone: string, since: Date) { return this.db.gameOtp.findMany({ where: { phone, createdAt: { gte: since } }, orderBy: { createdAt: 'asc' } }) }
  async bumpOtpAttempts(phone: string, createdAt: Date) { await this.db.gameOtp.updateMany({ where: { phone, createdAt }, data: { attempts: { increment: 1 } } }) }
  async clearOtps(phone: string) { await this.db.gameOtp.deleteMany({ where: { phone } }) }
  async recordConsent(phone: string) { await this.db.gamePlayer.upsert({ where: { phone }, create: { phone }, update: {} }) }
  async getPlay(phone: string, day: string) { return this.db.gamePlay.findUnique({ where: { phone_day: { phone, day } } }) }
  async savePlay(r: PlayRow) { await this.db.gamePlay.upsert({ where: { phone_day: { phone: r.phone, day: r.day } }, create: r, update: { stage: r.stage, result: r.result } }) }
  async addCoupon(r: CouponRow) { await this.db.gameCoupon.create({ data: r }) }
  async voidCoupon(code: string) { await this.db.gameCoupon.update({ where: { code }, data: { voided: true } }) }
  async couponsForPhone(phone: string) { return this.db.gameCoupon.findMany({ where: { phone, voided: false }, orderBy: { createdAt: 'desc' } }) }
  async countCoupons(prizeKey: string, day: string) { return this.db.gameCoupon.count({ where: { prizeKey, day, voided: false } }) }
  async findCoupon(code: string) { return this.db.gameCoupon.findUnique({ where: { code } }) }
  async redeemCoupon(code: string) { await this.db.gameCoupon.update({ where: { code }, data: { redeemedAt: new Date() } }) }
  async stats(day: string) {
    const [players, plays, win1, win2, redeemed] = await Promise.all([
      this.db.gamePlayer.count(), this.db.gamePlay.count({ where: { day } }),
      this.countCoupons('WIN1', day), this.countCoupons('WIN2', day),
      this.db.gameCoupon.count({ where: { voided: false, redeemedAt: { not: null } } }),
    ])
    return { players, plays, win1, win2, redeemed }
  }
}

const g = globalThis as unknown as { hibiGameStore?: GameStore }

export async function getStore(): Promise<GameStore> {
  if (g.hibiGameStore) return g.hibiGameStore
  if (process.env.DATABASE_URL) {
    const { prisma } = await import('@/lib/prisma')
    g.hibiGameStore = new PrismaStore(prisma)
  } else {
    g.hibiGameStore = new MemoryStore()
  }
  return g.hibiGameStore
}
