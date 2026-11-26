import { createHmac, timingSafeEqual } from 'crypto'

const COOKIE = 'hibi_game'
const MAX_AGE = 60 * 60 * 12

function secret(): string {
  const s = process.env.GAME_SECRET
  if (!s && process.env.NODE_ENV === 'production') throw new Error('GAME_SECRET is required in production')
  return s ?? 'dev-only-insecure-secret'
}

function sign(payload: string): string {
  return createHmac('sha256', secret()).update(payload).digest('base64url')
}

export function hashOtp(phone: string, code: string): string {
  return createHmac('sha256', secret()).update(`otp:${phone}:${code}`).digest('hex')
}

export function sessionCookie(phone: string) {
  const exp = Math.floor(Date.now() / 1000) + MAX_AGE
  const payload = `${phone}.${exp}`
  return {
    name: COOKIE,
    value: `${payload}.${sign(payload)}`,
    options: { httpOnly: true, sameSite: 'lax' as const, secure: process.env.NODE_ENV === 'production', path: '/', maxAge: MAX_AGE },
  }
}

/** Returns the verified phone number from the session cookie, or null. */
export function readSession(value: string | undefined): string | null {
  if (!value) return null
  const [phone, exp, sig] = value.split('.')
  if (!phone || !exp || !sig) return null
  const expected = Buffer.from(sign(`${phone}.${exp}`))
  const got = Buffer.from(sig)
  if (expected.length !== got.length || !timingSafeEqual(expected, got)) return null
  if (Number(exp) < Date.now() / 1000) return null
  return phone
}

export const SESSION_COOKIE = COOKIE
