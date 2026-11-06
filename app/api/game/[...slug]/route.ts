// All game API endpoints live in this one route so they share one server instance (and its
// in-memory store) when no database is configured, e.g. a Vercel test deployment.
// Paths: otp/request, otp/verify, state, receipt, play, logout, admin.
import { NextResponse } from 'next/server'
import { timingSafeEqual } from 'crypto'
import { isDemoMode } from '@/lib/game/config'
import { isMove, maskPhone, normalizePhone } from '@/lib/game/logic'
import { adminAction, GameError, getState, play, publicPrizes, registerReceipt, requestOtp, verifyOtp } from '@/lib/game/service'
import { SESSION_COOKIE, sessionCookie } from '@/lib/game/session'
import { currentPhone, fail } from '../_util'

async function otpRequest(req: Request) {
  const { phone, consent } = await req.json()
  const p = normalizePhone(String(phone ?? ''))
  if (!p) throw new GameError(400, 'กรุณากรอกเบอร์มือถือ 10 หลักให้ถูกต้อง')
  if (consent !== true) throw new GameError(400, 'กรุณายอมรับนโยบายข้อมูลส่วนบุคคลก่อน')
  return NextResponse.json({ ok: true, phone: p, ...(await requestOtp(p)) })
}

async function otpVerify(req: Request) {
  const { phone, code } = await req.json()
  const p = normalizePhone(String(phone ?? ''))
  if (!p || !/^\d{6}$/.test(String(code ?? ''))) throw new GameError(400, 'กรุณากรอกรหัส 6 หลัก')
  await verifyOtp(p, String(code))
  const res = NextResponse.json({ ok: true, state: await getState(p) })
  const c = sessionCookie(p)
  res.cookies.set(c.name, c.value, c.options)
  return res
}

async function stateOf() {
  const phone = await currentPhone()
  if (!phone) return NextResponse.json({ loggedIn: false, prizes: publicPrizes() })
  return NextResponse.json({ loggedIn: true, phone: maskPhone(phone), state: await getState(phone) })
}

async function playMove(req: Request) {
  const phone = await currentPhone()
  if (!phone) throw new GameError(401, 'กรุณายืนยันเบอร์มือถือก่อนเล่น')
  const { move } = await req.json()
  if (!isMove(move)) throw new GameError(400, 'เลือก ค้อน กระดาษ หรือ กรรไกร')
  return NextResponse.json(await play(phone, move))
}

async function receipt(req: Request) {
  const phone = await currentPhone()
  if (!phone) throw new GameError(401, 'กรุณายืนยันเบอร์มือถือก่อน')
  const { last5, date } = await req.json()
  return NextResponse.json({ ok: true, state: await registerReceipt(phone, String(last5 ?? '').trim(), String(date ?? '')) })
}

async function logout() {
  const res = NextResponse.json({ ok: true })
  res.cookies.delete(SESSION_COOKIE)
  return res
}

function pinOk(pin: unknown): boolean {
  const expected = process.env.GAME_ADMIN_PIN ?? (isDemoMode() ? '1234' : '')
  if (!expected || typeof pin !== 'string') return false
  const a = Buffer.from(pin), b = Buffer.from(expected)
  return a.length === b.length && timingSafeEqual(a, b)
}

async function admin(req: Request) {
  const { pin, action, code } = await req.json()
  if (!pinOk(pin)) throw new GameError(401, 'PIN ไม่ถูกต้อง')
  return NextResponse.json(await adminAction(String(action), code ? String(code) : undefined))
}

const ROUTES: Record<string, { method: 'GET' | 'POST'; fn: (req: Request) => Promise<Response> }> = {
  'otp/request': { method: 'POST', fn: otpRequest },
  'otp/verify': { method: 'POST', fn: otpVerify },
  state: { method: 'GET', fn: stateOf },
  receipt: { method: 'POST', fn: receipt },
  play: { method: 'POST', fn: playMove },
  logout: { method: 'POST', fn: logout },
  admin: { method: 'POST', fn: admin },
}

type Ctx = { params: Promise<{ slug: string[] }> }

async function dispatch(method: 'GET' | 'POST', req: Request, ctx: Ctx) {
  const route = ROUTES[(await ctx.params).slug.join('/')]
  if (!route) return NextResponse.json({ error: 'not found' }, { status: 404 })
  if (route.method !== method) return NextResponse.json({ error: 'method not allowed' }, { status: 405 })
  try { return await route.fn(req) } catch (e) { return fail(e) }
}

export const GET = (req: Request, ctx: Ctx) => dispatch('GET', req, ctx)
export const POST = (req: Request, ctx: Ctx) => dispatch('POST', req, ctx)
