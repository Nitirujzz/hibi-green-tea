// Prize and limit settings for the Hibi & Capy rock-paper-scissors game.
// The shop edits these values (or the matching env vars) before going live.
export const GAME_CONFIG = {
  /** Beat Hibi only (round 1). */
  win1: {
    key: 'WIN1',
    label: process.env.GAME_WIN1_LABEL ?? 'ส่วนลด 15%',
    percent: Number(process.env.GAME_WIN1_PERCENT ?? 15),
    dailyCap: Number(process.env.GAME_WIN1_DAILY_CAP ?? 200),
    /** Chance the player wins a decided round against Hibi (ties are replayed). */
    winChance: Number(process.env.GAME_HIBI_WIN_CHANCE ?? 2 / 3),
  },
  /** Beat Hibi and Capy (both rounds): the grand prize. */
  win2: {
    key: 'WIN2',
    label: process.env.GAME_WIN2_LABEL ?? 'ส่วนลด 35%',
    percent: Number(process.env.GAME_WIN2_PERCENT ?? 35),
    dailyCap: Number(process.env.GAME_WIN2_DAILY_CAP ?? 20),
    /** Chance the player wins a decided round against Capy (ties are replayed). */
    winChance: Number(process.env.GAME_CAPY_WIN_CHANCE ?? 1 / 3),
  },
  playsPerPhonePerDay: 1,
  couponValidDays: Number(process.env.GAME_COUPON_DAYS ?? 30),
  coupon: {
    /** Max bill value (baht) the discount applies to. */
    maxBillBaht: Number(process.env.GAME_COUPON_MAX_BILL ?? 1000),
    /** "Use on your next visit": a coupon cannot be redeemed on the day it was won. */
    nextVisitOnly: (process.env.GAME_COUPON_SAME_DAY ?? 'no') !== 'yes',
  },
  receipt: {
    /** Players type the last 5 digits of their receipt number plus the receipt date to play. */
    digits: 5,
    /** How many days back a receipt date may be (0 = today only). */
    maxAgeDays: Number(process.env.GAME_RECEIPT_MAX_AGE_DAYS ?? 1),
  },
  otp: {
    ttlSeconds: 300,
    resendCooldownSeconds: 60,
    maxRequestsPerDay: 5,
    maxVerifyAttempts: 5,
  },
  /** Share of throws that come out as a tie (replayed), as in a real game. */
  tieChance: 1 / 3,
  timeZone: 'Asia/Bangkok',
} as const

export type Move = 'rock' | 'paper' | 'scissors'
export type Opponent = 'hibi' | 'capy'
export const MOVES: Move[] = ['rock', 'paper', 'scissors']

/** Calendar day in Bangkok time, used for the daily play limit and prize caps. */
export function today(now = new Date()): string {
  return new Intl.DateTimeFormat('en-CA', { timeZone: GAME_CONFIG.timeZone }).format(now)
}

export function isDemoMode(): boolean {
  return (process.env.GAME_OTP_MODE ?? 'demo') === 'demo'
}

/** Coupon conditions shown to players and staff. */
export function couponTerms(): string[] {
  const c = GAME_CONFIG.coupon
  return [
    c.nextVisitOnly ? 'ใช้ได้ในการมาครั้งถัดไป (ไม่ใช้กับบิลที่ใช้เล่นเกม)' : 'ใช้ได้ตั้งแต่วันนี้',
    `ใช้ได้ภายใน ${GAME_CONFIG.couponValidDays} วัน นับจากวันที่ได้รับ`,
    'ใช้ได้เฉพาะหน้าร้าน',
    `ใช้กับยอดมูลค่าไม่เกิน ${c.maxBillBaht.toLocaleString('en-US')} บาทต่อบิล`,
  ]
}

/** Shift a YYYY-MM-DD day string by n days. */
export function addDays(day: string, n: number): string {
  const d = new Date(day + 'T00:00:00Z'); d.setUTCDate(d.getUTCDate() + n)
  return d.toISOString().slice(0, 10)
}
