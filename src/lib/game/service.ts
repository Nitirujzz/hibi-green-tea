import { randomInt } from 'crypto'
import { GAME_CONFIG, addDays, couponTerms, today, isDemoMode, type Move, type Opponent } from './config'
import { couponCode, judge, opponentMove, type Outcome } from './logic'
import { hashOtp } from './session'
import { sendOtpSms } from './otp'
import { getStore, type CouponRow } from './store'

export class GameError extends Error {
  constructor(public status: number, message: string) { super(message) }
}

export async function requestOtp(phone: string): Promise<{ demoCode?: string }> {
  const s = await getStore(), now = new Date(), C = GAME_CONFIG.otp
  const recent = await s.otpsForPhone(phone, new Date(now.getTime() - 24 * 3600 * 1000))
  const last = recent[recent.length - 1]
  if (last && now.getTime() - last.createdAt.getTime() < C.resendCooldownSeconds * 1000)
    throw new GameError(429, `รอสักครู่ แล้วขอรหัสใหม่ได้ใน ${C.resendCooldownSeconds} วินาที`)
  if (recent.length >= C.maxRequestsPerDay) throw new GameError(429, 'ขอรหัสครบจำนวนของวันนี้แล้ว ลองใหม่พรุ่งนี้นะ')
  const code = String(randomInt(0, 1_000_000)).padStart(6, '0')
  await s.addOtp({ phone, codeHash: hashOtp(phone, code), expiresAt: new Date(now.getTime() + C.ttlSeconds * 1000), attempts: 0, createdAt: now })
  await sendOtpSms(phone, code)
  return isDemoMode() ? { demoCode: code } : {}
}

export async function verifyOtp(phone: string, code: string): Promise<void> {
  const s = await getStore(), now = new Date()
  const rows = await s.otpsForPhone(phone, new Date(now.getTime() - GAME_CONFIG.otp.ttlSeconds * 1000))
  const last = rows[rows.length - 1]
  if (!last || last.expiresAt < now) throw new GameError(400, 'รหัสหมดอายุ กรุณาขอรหัสใหม่')
  if (last.attempts >= GAME_CONFIG.otp.maxVerifyAttempts) throw new GameError(429, 'กรอกผิดหลายครั้งเกินไป กรุณาขอรหัสใหม่')
  if (last.codeHash !== hashOtp(phone, code)) {
    await s.bumpOtpAttempts(phone, last.createdAt)
    throw new GameError(400, 'รหัสไม่ถูกต้อง')
  }
  await s.clearOtps(phone)
  await s.recordConsent(phone)
}

function publicCoupon(c: CouponRow) {
  return { code: c.code, label: c.label, percent: c.percent, expiresAt: c.expiresAt.toISOString(), redeemed: !!c.redeemedAt }
}

export function publicPrizes() {
  return { win1: GAME_CONFIG.win1.label, win2: GAME_CONFIG.win2.label, win1Percent: GAME_CONFIG.win1.percent, win2Percent: GAME_CONFIG.win2.percent,
    validDays: GAME_CONFIG.couponValidDays, terms: couponTerms() }
}

/** Register the receipt (last 5 digits + date) that unlocks today's play. One receipt plays once. */
export async function registerReceipt(phone: string, last5: string, date: string) {
  const s = await getStore(), day = today()
  if (!new RegExp(`^\\d{${GAME_CONFIG.receipt.digits}}$`).test(last5)) throw new GameError(400, `กรอกเลขท้ายใบเสร็จ ${GAME_CONFIG.receipt.digits} หลัก`)
  if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) throw new GameError(400, 'กรุณาเลือกวันที่ในใบเสร็จ')
  if (date > day) throw new GameError(400, 'วันที่ในใบเสร็จต้องไม่เกินวันนี้')
  if (date < addDays(day, -GAME_CONFIG.receipt.maxAgeDays))
    throw new GameError(400, GAME_CONFIG.receipt.maxAgeDays === 0 ? 'ใช้ได้เฉพาะใบเสร็จของวันนี้' : `ใช้ได้เฉพาะใบเสร็จภายใน ${GAME_CONFIG.receipt.maxAgeDays + 1} วันล่าสุด`)
  const existing = await s.getPlay(phone, day)
  if (existing?.receiptLast5) throw new GameError(409, 'วันนี้ลงทะเบียนใบเสร็จแล้ว')
  if (await s.findPlayByReceipt(last5, date)) throw new GameError(409, 'ใบเสร็จนี้ถูกใช้เล่นเกมไปแล้ว')
  await s.savePlay({ phone, day, stage: 'hibi', result: null, receiptLast5: last5, receiptDate: date })
  return getState(phone)
}

async function grandAvailable(day: string) {
  const s = await getStore()
  return (await s.countCoupons(GAME_CONFIG.win2.key, day)) < GAME_CONFIG.win2.dailyCap
}

export async function getState(phone: string) {
  const s = await getStore(), day = today()
  const play = await s.getPlay(phone, day)
  const coupons = (await s.couponsForPhone(phone)).filter(c => c.day === day)
  return {
    stage: play?.stage ?? 'hibi',
    result: play?.result ?? null,
    needReceipt: !play?.receiptLast5,
    receipt: play?.receiptLast5 ? { last5: play.receiptLast5, date: play.receiptDate } : null,
    receiptMinDate: addDays(day, -GAME_CONFIG.receipt.maxAgeDays),
    today: day,
    coupon: coupons[0] ? publicCoupon(coupons[0]) : null,
    grandAvailable: await grandAvailable(day),
    prizes: publicPrizes(),
  }
}

async function issue(phone: string, day: string, prize: typeof GAME_CONFIG.win1 | typeof GAME_CONFIG.win2): Promise<CouponRow | null> {
  const s = await getStore()
  if ((await s.countCoupons(prize.key, day)) >= prize.dailyCap) return null
  const now = new Date()
  const row: CouponRow = { code: couponCode(), phone, prizeKey: prize.key, label: prize.label, percent: prize.percent, day, createdAt: now,
    expiresAt: new Date(now.getTime() + GAME_CONFIG.couponValidDays * 86400 * 1000), redeemedAt: null, voided: false }
  await s.addCoupon(row)
  return row
}

export async function play(phone: string, move: Move) {
  const s = await getStore(), day = today()
  const row = await s.getPlay(phone, day)
  if (!row?.receiptLast5) throw new GameError(403, 'กรอกเลขท้ายใบเสร็จและวันที่ก่อนเล่นนะ')
  if (row.stage === 'done') throw new GameError(409, 'วันนี้เล่นครบแล้ว พรุ่งนี้มาเล่นใหม่นะ')
  const opponent = row.stage as Opponent
  const opp = opponentMove(move, (opponent === 'hibi' ? GAME_CONFIG.win1 : GAME_CONFIG.win2).winChance, GAME_CONFIG.tieChance)
  const outcome: Outcome = judge(move, opp)
  let coupon: CouponRow | null = null, note: string | null = null

  if (outcome === 'lose') {
    row.stage = 'done'
    row.result = opponent === 'hibi' ? 'lost_hibi' : 'lost_capy'   // a Hibi prize already won is kept
  } else if (outcome === 'win' && opponent === 'hibi') {
    coupon = await issue(phone, day, GAME_CONFIG.win1)
    if (!coupon) note = 'รางวัลรอบแรกของวันนี้หมดแล้ว แต่ยังท้า Capy ได้นะ'
    if (await grandAvailable(day)) { row.stage = 'capy'; row.result = 'beat_hibi' }
    else { row.stage = 'done'; row.result = 'beat_hibi'; note = (note ? note + ' · ' : '') + 'รางวัลใหญ่ของวันนี้หมดแล้ว' }
  } else if (outcome === 'win' && opponent === 'capy') {
    const grand = await issue(phone, day, GAME_CONFIG.win2)
    if (grand) {
      for (const c of (await s.couponsForPhone(phone)).filter(c => c.day === day && c.prizeKey === GAME_CONFIG.win1.key)) await s.voidCoupon(c.code)
      coupon = grand
    } else note = 'รางวัลใหญ่ของวันนี้หมดพอดี เก็บรางวัลรอบแรกไว้นะ'
    row.stage = 'done'; row.result = 'beat_both'
  }
  await s.savePlay(row)
  const state = await getState(phone)
  return { opponent, playerMove: move, opponentMove: opp, outcome, newCoupon: coupon ? publicCoupon(coupon) : null, note, state }
}

export async function adminAction(action: string, code?: string) {
  const s = await getStore(), day = today()
  if (action === 'stats') return { day, ...(await s.stats(day)), caps: { win1: GAME_CONFIG.win1.dailyCap, win2: GAME_CONFIG.win2.dailyCap } }
  const c = code ? await s.findCoupon(code.trim().toUpperCase()) : null
  if (!c || c.voided) throw new GameError(404, 'ไม่พบคูปองนี้')
  const p = await s.getPlay(c.phone, c.day)
  const info = { code: c.code, label: c.label, percent: c.percent, phone: c.phone, wonOn: c.day, expiresAt: c.expiresAt.toISOString(), redeemedAt: c.redeemedAt?.toISOString() ?? null,
    receipt: p?.receiptLast5 ? { last5: p.receiptLast5, date: p.receiptDate } : null, terms: couponTerms() }
  if (action === 'lookup') return info
  if (action === 'redeem') {
    if (c.redeemedAt) throw new GameError(409, 'คูปองนี้ถูกใช้ไปแล้ว')
    if (c.expiresAt < new Date()) throw new GameError(410, 'คูปองหมดอายุแล้ว')
    if (GAME_CONFIG.coupon.nextVisitOnly && c.day === day) throw new GameError(409, 'คูปองนี้ใช้ได้ในการมาครั้งถัดไป (ตั้งแต่พรุ่งนี้)')
    await s.redeemCoupon(c.code)
    return { ...info, redeemedAt: new Date().toISOString() }
  }
  throw new GameError(400, 'unknown action')
}
