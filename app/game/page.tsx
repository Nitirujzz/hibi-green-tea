'use client'
import { useEffect, useMemo, useState } from 'react'
import { AnimatePresence, motion } from 'framer-motion'

type Move = 'rock' | 'paper' | 'scissors'
type Opp = 'hibi' | 'capy'
type Coupon = { code: string; label: string; percent: number; expiresAt: string; redeemed: boolean }
type State = { stage: Opp | 'done'; result: string | null; coupon: Coupon | null; grandAvailable: boolean; prizes: { win1: string; win2: string } }
type PlayRes = { opponent: Opp; playerMove: Move; opponentMove: Move; outcome: 'win' | 'lose' | 'tie'; newCoupon: Coupon | null; note: string | null; state: State }
type Screen = 'loading' | 'intro' | 'phone' | 'otp' | 'lobby' | 'pick' | 'count' | 'reveal'

const HAND: Record<Move, string> = { rock: '✊', paper: '✋', scissors: '✌️' }
const NAME: Record<Move, string> = { rock: 'ค้อน', paper: 'กระดาษ', scissors: 'กรรไกร' }
const OPP = { hibi: { name: 'Hibi', round: 1, line: 'มาเลย! Hibi ไม่ยอมแพ้ง่าย ๆ นะ 🐰' }, capy: { name: 'Capy', round: 2, line: 'Capy ใจเย็นที่สุดในสามโลก… ลองดูสิ 🍊' } }

async function api<T>(url: string, body?: unknown): Promise<T> {
  const res = await fetch(url, body === undefined ? { cache: 'no-store' } : { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) })
  const data = await res.json()
  if (!res.ok) throw new Error(data.error ?? 'เกิดข้อผิดพลาด')
  return data
}

function Char({ who, mood, size = 240 }: { who: Opp | 'both'; mood?: 'ready' | 'win' | 'lose'; size?: number }) {
  const src = who === 'both' ? '/game/both_cheer.webp' : `/game/${who}_${mood ?? 'ready'}.webp`
  return (
    <motion.img key={src} src={src} alt={who} width={size} height={size} draggable={false}
      initial={{ scale: 0.8, opacity: 0 }} animate={{ scale: 1, opacity: 1, y: [0, -8, 0] }}
      transition={{ scale: { type: 'spring', stiffness: 260, damping: 14 }, y: { repeat: Infinity, duration: 2.4, ease: 'easeInOut' } }}
      style={{ width: size, height: size, objectFit: 'contain', margin: '0 auto', filter: 'drop-shadow(0 12px 18px rgba(0,0,0,.12))' }} />
  )
}

function Confetti() {
  const bits = useMemo(() => Array.from({ length: 46 }, (_, i) => ({ i, x: Math.random() * 100, d: 1.8 + Math.random() * 1.6, delay: Math.random() * 0.8,
    c: ['#ff7aa2', '#ffd23f', '#7fb24a', '#a8d48a', '#e07b39'][i % 5], r: Math.random() * 360 })), [])
  return (
    <div className="pointer-events-none fixed inset-0 overflow-hidden">
      {bits.map(b => (
        <motion.div key={b.i} initial={{ y: -40, x: `${b.x}vw`, rotate: b.r, opacity: 1 }} animate={{ y: '105vh', rotate: b.r + 540 }}
          transition={{ duration: b.d, delay: b.delay, ease: 'easeIn', repeat: Infinity, repeatDelay: 0.6 }}
          style={{ position: 'absolute', width: 10, height: 16, borderRadius: 3, background: b.c }} />
      ))}
    </div>
  )
}

function CouponCard({ c, phone }: { c: Coupon; phone: string }) {
  const exp = new Date(c.expiresAt).toLocaleDateString('th-TH', { day: 'numeric', month: 'short', year: '2-digit' })
  return (
    <div className="hg-card hg-coupon p-5 text-center">
      <div className="display text-[15px] font-semibold text-[#e5484d]">🎟️ คูปองของคุณ</div>
      <div className="display mt-1 text-[40px] font-bold leading-none text-[#243e1b]">{c.label}</div>
      <div className="display mt-3 select-all rounded-2xl bg-[#243e1b] px-3 py-2 text-[24px] font-bold tracking-[2px] text-white">{c.code}</div>
      <div className="mt-3 text-[14px] text-[#6b6a55]">เบอร์ {phone} · ใช้ได้ถึง {exp} · ทุกสาขา</div>
      <div className="mt-1 text-[14px] font-semibold text-[#3f8f3a]">📸 แคปหน้าจอนี้ แล้วโชว์พนักงานตอนสั่งเครื่องดื่ม</div>
      {c.redeemed && <div className="mt-2 font-semibold text-[#e5484d]">ใช้สิทธิ์แล้ว</div>}
    </div>
  )
}

export default function GamePage() {
  const [screen, setScreen] = useState<Screen>('loading')
  const [state, setState] = useState<State | null>(null)
  const [maskedPhone, setMaskedPhone] = useState('')
  const [phone, setPhone] = useState('')
  const [consent, setConsent] = useState(false)
  const [code, setCode] = useState('')
  const [demoCode, setDemoCode] = useState<string | null>(null)
  const [err, setErr] = useState<string | null>(null)
  const [busy, setBusy] = useState(false)
  const [last, setLast] = useState<PlayRes | null>(null)
  const [beat, setBeat] = useState(0)
  const [prizes, setPrizes] = useState<State['prizes'] | null>(null)

  async function refresh() {
    const s = await api<{ loggedIn: boolean; phone?: string; state?: State; prizes?: State['prizes'] }>('/api/game/state')
    if (s.prizes) setPrizes(s.prizes)
    if (s.loggedIn && s.state) { setState(s.state); setMaskedPhone(s.phone ?? ''); setScreen('lobby') } else setScreen('intro')
  }
  useEffect(() => { refresh().catch(() => setScreen('intro')) }, [])

  async function run<T>(fn: () => Promise<T>) {
    setErr(null); setBusy(true)
    try { return await fn() } catch (e) { setErr((e as Error).message) } finally { setBusy(false) }
  }

  const sendOtp = () => run(async () => {
    const r = await api<{ phone: string; demoCode?: string }>('/api/game/otp/request', { phone, consent })
    setDemoCode(r.demoCode ?? null); setCode(''); setScreen('otp')
  })
  const verify = () => run(async () => {
    await api('/api/game/otp/verify', { phone, code })
    await refresh()
  })
  const choose = (m: Move) => run(async () => {
    setScreen('count'); setBeat(0)
    const res = api<PlayRes>('/api/game/play', { move: m })
    res.catch(() => {})   // handled after the countdown
    for (let i = 1; i <= 3; i++) { await new Promise(r => setTimeout(r, 650)); setBeat(i) }
    try { const r = await res; setLast(r); setState(r.state); setScreen('reveal') } catch (e) { setScreen('lobby'); throw e }
  })

  const opp: Opp = state?.stage === 'capy' ? 'capy' : (last?.opponent ?? 'hibi')
  const grand = state?.result === 'beat_both' && state.coupon?.percent === 50

  return (
    <main className="mx-auto flex min-h-[100dvh] max-w-[440px] flex-col px-4 pb-10 pt-6">
      <header className="mb-2 flex items-center justify-between">
        <div className="display text-[18px] font-bold text-[#243e1b]">Hibi Matcha Cafe</div>
        {maskedPhone && <div className="text-[13px] text-[#9a9578]">📱 {maskedPhone}</div>}
      </header>

      <AnimatePresence mode="wait">
        <motion.section key={screen + (last?.outcome ?? '')} initial={{ opacity: 0, y: 16 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -12 }} transition={{ duration: 0.25 }} className="flex flex-1 flex-col">

          {screen === 'loading' && <div className="m-auto text-[#9a9578]">กำลังโหลด…</div>}

          {screen === 'intro' && <>
            <div className="mt-2 text-center">
              <h1 className="text-[34px] font-bold leading-tight text-[#243e1b]">เป่ายิ้งฉุบ<br /><span className="text-[#e0a800]">กับ Hibi & Capy</span></h1>
            </div>
            <div className="flex justify-center"><Char who="both" size={260} /></div>
            <div className="hg-card space-y-2 p-5 text-[16px]">
              <div>🥇 <b>ชนะ Hibi</b> → {state?.prizes.win1 ?? prizes?.win1 ?? ''}</div>
              <div>🏆 <b>ชนะทั้ง Hibi และ Capy</b> → <b className="text-[#e5484d]">ส่วนลด 50%</b></div>
              <div className="text-[14px] text-[#6b6a55]">เล่นได้วันละ 1 ครั้งต่อเบอร์ · เสมอเล่นใหม่ได้ · คูปองใช้ได้ทุกสาขา</div>
            </div>
            <button className="hg-btn hg-primary mt-5" onClick={() => setScreen('phone')}>เริ่มเล่นเลย! ✊✋✌️</button>
          </>}

          {screen === 'phone' && <>
            <div className="flex justify-center"><Char who="hibi" mood="ready" size={200} /></div>
            <h2 className="text-center text-[24px] font-bold text-[#243e1b]">ลงทะเบียนด้วยเบอร์มือถือ</h2>
            <p className="mb-4 text-center text-[15px] text-[#6b6a55]">เราจะส่งรหัส OTP ไปทาง SMS</p>
            <input className="hg-input" inputMode="tel" placeholder="08x-xxx-xxxx" value={phone} maxLength={13} onChange={e => setPhone(e.target.value)} />
            <label className="mt-4 flex gap-3 text-[14px] leading-snug text-[#5b5a48]">
              <input type="checkbox" className="mt-1 h-5 w-5 accent-[#3f8f3a]" checked={consent} onChange={e => setConsent(e.target.checked)} />
              <span>ฉันยินยอมให้ Hibi Matcha Cafe เก็บและใช้เบอร์มือถือเพื่อยืนยันตัวตน ส่งรหัส OTP และใช้สิทธิ์รางวัลของเกมนี้ ตาม<a className="underline" href="#privacy">นโยบายความเป็นส่วนตัว</a></span>
            </label>
            {err && <p className="mt-3 text-center font-semibold text-[#e5484d]">{err}</p>}
            <button className="hg-btn hg-primary mt-5" disabled={busy || !consent || phone.replace(/\D/g, '').length < 10} onClick={sendOtp}>{busy ? 'กำลังส่ง…' : 'ขอรหัส OTP'}</button>
          </>}

          {screen === 'otp' && <>
            <div className="flex justify-center"><Char who="capy" mood="ready" size={200} /></div>
            <h2 className="text-center text-[24px] font-bold text-[#243e1b]">กรอกรหัส OTP 6 หลัก</h2>
            <p className="mb-4 text-center text-[15px] text-[#6b6a55]">ส่งไปที่ {phone}</p>
            {demoCode && <div className="mb-3 rounded-2xl bg-[#fff3c4] p-3 text-center text-[14px]">🧪 โหมดทดลอง (ยังไม่ส่ง SMS จริง) — รหัสคือ <b className="text-[18px] tracking-[3px]">{demoCode}</b></div>}
            <input className="hg-input text-center text-[28px] tracking-[10px]" inputMode="numeric" autoComplete="one-time-code" maxLength={6} value={code} onChange={e => setCode(e.target.value.replace(/\D/g, ''))} />
            {err && <p className="mt-3 text-center font-semibold text-[#e5484d]">{err}</p>}
            <button className="hg-btn hg-primary mt-5" disabled={busy || code.length !== 6} onClick={verify}>{busy ? 'กำลังตรวจสอบ…' : 'ยืนยันแล้วเล่นเลย'}</button>
            <button className="mt-3 text-[14px] text-[#6b6a55] underline" disabled={busy} onClick={sendOtp}>ไม่ได้รับรหัส? ขอใหม่</button>
          </>}

          {screen === 'lobby' && state && <>
            {state.stage !== 'done' ? <>
              <div className="mt-2 text-center display text-[16px] font-semibold text-[#9a9578]">รอบที่ {OPP[state.stage].round} / 2</div>
              <h2 className="text-center text-[28px] font-bold text-[#243e1b]">เจอกับ {OPP[state.stage].name}!</h2>
              <div className="flex justify-center"><Char who={state.stage} mood="ready" size={250} /></div>
              <p className="text-center text-[16px]">{OPP[state.stage].line}</p>
              {!state.grandAvailable && <p className="mt-2 rounded-2xl bg-[#fff3c4] p-2 text-center text-[14px]">รางวัลส่วนลด 50% ของวันนี้หมดแล้ว · ยังลุ้นรางวัลรอบแรกได้นะ</p>}
              {state.coupon && <p className="mt-2 text-center text-[14px] text-[#3f8f3a]">คุณได้ {state.coupon.label} แล้ว · ชนะ Capy อัปเกรดเป็นส่วนลด 50%!</p>}
              <button className="hg-btn hg-primary mt-5" onClick={() => setScreen('pick')}>พร้อมแล้ว! เป่า ยิ้ง ฉุบ</button>
            </> : <>
              {grand && <Confetti />}
              <h2 className="mt-2 text-center text-[28px] font-bold text-[#243e1b]">{grand ? 'ชนะทั้งคู่! 🎉' : state.coupon ? 'เก่งมาก! 🎉' : 'วันนี้ยังไม่ใช่วันของเรา'}</h2>
              <div className="flex justify-center"><Char who={grand ? 'both' : state.result === 'lost_capy' ? 'capy' : 'hibi'} mood="win" size={220} /></div>
              {state.coupon ? <CouponCard c={state.coupon} phone={maskedPhone} /> : <p className="hg-card p-5 text-center text-[16px]">พรุ่งนี้มาท้า Hibi & Capy ใหม่ได้นะ 💚<br />ระหว่างนี้แวะมาดื่มมัทฉะที่ร้านได้ทุกสาขา 🍵</p>}
              <p className="mt-4 text-center text-[13px] text-[#9a9578]">เล่นได้วันละ 1 ครั้งต่อเบอร์</p>
            </>}
          </>}

          {screen === 'pick' && state && state.stage !== 'done' && <>
            <div className="mt-2 text-center display text-[16px] font-semibold text-[#9a9578]">รอบที่ {OPP[state.stage].round} / 2 · {OPP[state.stage].name}</div>
            <div className="flex justify-center"><Char who={state.stage} mood="ready" size={230} /></div>
            <h2 className="mb-4 text-center text-[24px] font-bold text-[#243e1b]">เลือกเลย!</h2>
            <div className="flex justify-center gap-4">
              {(['rock', 'paper', 'scissors'] as Move[]).map(m => (
                <motion.button key={m} whileTap={{ scale: 0.9 }} whileHover={{ y: -4 }} className="hg-move" disabled={busy} onClick={() => choose(m)}>
                  {HAND[m]}<span>{NAME[m]}</span>
                </motion.button>
              ))}
            </div>
            {err && <p className="mt-3 text-center font-semibold text-[#e5484d]">{err}</p>}
          </>}

          {screen === 'count' && <>
            <div className="flex justify-center"><Char who={opp} mood="ready" size={230} /></div>
            <div className="mt-6 flex items-center justify-center gap-10 text-[80px]">
              <motion.div animate={{ y: [0, -30, 0] }} transition={{ repeat: Infinity, duration: 0.65 }}>✊</motion.div>
              <motion.div animate={{ y: [0, -30, 0] }} transition={{ repeat: Infinity, duration: 0.65 }}>✊</motion.div>
            </div>
            <motion.div key={beat} initial={{ scale: 1.6, opacity: 0 }} animate={{ scale: 1, opacity: 1 }} className="display mt-4 text-center text-[44px] font-bold text-[#243e1b]">
              {['เป่า…', 'ยิ้ง…', 'ฉุบ!', 'ฉุบ!'][beat]}
            </motion.div>
          </>}

          {screen === 'reveal' && last && <>
            {last.outcome === 'win' && last.opponent === 'capy' && last.newCoupon?.percent === 50 && <Confetti />}
            <div className="flex justify-center"><Char who={last.opponent} mood={last.outcome === 'win' ? 'lose' : last.outcome === 'lose' ? 'win' : 'ready'} size={220} /></div>
            <div className="mt-2 flex items-center justify-center gap-6">
              <div className="text-center"><motion.div initial={{ scale: 0, rotate: -40 }} animate={{ scale: 1, rotate: 0 }} className="text-[72px]">{HAND[last.playerMove]}</motion.div><div className="text-[14px] text-[#6b6a55]">คุณ</div></div>
              <div className="display text-[24px] font-bold text-[#9a9578]">VS</div>
              <div className="text-center"><motion.div initial={{ scale: 0, rotate: 40 }} animate={{ scale: 1, rotate: 0 }} className="text-[72px]">{HAND[last.opponentMove]}</motion.div><div className="text-[14px] text-[#6b6a55]">{OPP[last.opponent].name}</div></div>
            </div>
            <motion.h2 initial={{ scale: 0.6, opacity: 0 }} animate={{ scale: 1, opacity: 1 }} transition={{ delay: 0.25, type: 'spring' }}
              className={`mt-3 text-center text-[32px] font-bold ${last.outcome === 'win' ? 'text-[#3f8f3a]' : last.outcome === 'lose' ? 'text-[#e5484d]' : 'text-[#e0a800]'}`}>
              {last.outcome === 'tie' ? 'เสมอ! เอาใหม่ 🤝' : last.outcome === 'win' ? (last.opponent === 'capy' ? 'ชนะ Capy! 🏆' : 'ชนะ Hibi! 🎉') : `${OPP[last.opponent].name} ชนะ 😝`}
            </motion.h2>
            {last.note && <p className="mt-1 text-center text-[14px] text-[#8a5a2a]">{last.note}</p>}
            {last.newCoupon && <div className="mt-3"><CouponCard c={last.newCoupon} phone={maskedPhone} /></div>}
            <div className="mt-5 flex flex-col gap-3">
              {last.outcome === 'tie' && <button className="hg-btn hg-primary" onClick={() => setScreen('pick')}>เป่า ยิ้ง ฉุบ อีกครั้ง</button>}
              {last.state.stage === 'capy' && last.outcome === 'win' && <button className="hg-btn hg-primary" onClick={() => setScreen('lobby')}>ท้า Capy ต่อ! ลุ้นส่วนลด 50% 🍊</button>}
              {last.state.stage === 'done' && <button className="hg-btn hg-soft" onClick={() => setScreen('lobby')}>ดูผลของวันนี้</button>}
            </div>
          </>}
        </motion.section>
      </AnimatePresence>

      <footer id="privacy" className="mt-8 text-center text-[12px] leading-relaxed text-[#9a9578]">
        เกมนี้จัดโดย Hibi Matcha Cafe · เราใช้เบอร์มือถือเพื่อยืนยันตัวตนและการใช้สิทธิ์รางวัลเท่านั้น<br />เงื่อนไขการใช้คูปองเป็นไปตามที่ร้านกำหนด
      </footer>
    </main>
  )
}
