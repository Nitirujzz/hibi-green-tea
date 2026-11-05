// Prize and limit settings for the Hibi & Capy rock-paper-scissors game.
// The shop edits these values (or the matching env vars) before going live.
export const GAME_CONFIG = {
  /** Beat Hibi only (round 1). Placeholder reward until the shop confirms it. */
  win1: {
    key: 'WIN1',
    label: process.env.GAME_WIN1_LABEL ?? 'ส่วนลด 10%',
    percent: Number(process.env.GAME_WIN1_PERCENT ?? 10),
    dailyCap: Number(process.env.GAME_WIN1_DAILY_CAP ?? 200),
  },
  /** Beat Hibi and Capy (both rounds): the grand prize. */
  win2: {
    key: 'WIN2',
    label: 'ส่วนลด 50%',
    percent: 50,
    dailyCap: Number(process.env.GAME_WIN2_DAILY_CAP ?? 20),
  },
  playsPerPhonePerDay: 1,
  couponValidDays: Number(process.env.GAME_COUPON_DAYS ?? 14),
  otp: {
    ttlSeconds: 300,
    resendCooldownSeconds: 60,
    maxRequestsPerDay: 5,
    maxVerifyAttempts: 5,
  },
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
