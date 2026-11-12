'use client'
import { useEffect, useMemo, useState } from 'react'
import { AnimatePresence, motion } from 'framer-motion'
import { gameAudio, type Sfx } from './sound'
import { buildCard, shareText, shareUrl, type ShareKind } from './share'

type Move = 'rock' | 'paper' | 'scissors'
type Opp = 'hibi' | 'capy'
type Coupon = { code: string; label: string; percent: number; expiresAt: string; redeemed: boolean }
type Prizes = { win1: string; win2: string; win1Percent: number; win2Percent: number; validDays: number; terms: string[] }
type State = { stage: Opp | 'done'; result: string | null; coupon: Coupon | null; grandAvailable: boolean; prizes: Prizes
  needReceipt: boolean; receipt: { last5: string; date: string } | null; receiptMinDate: string; today: string }
type PlayRes = { opponent: Opp; playerMove: Move; opponentMove: Move; outcome: 'win' | 'lose' | 'tie'; newCoupon: Coupon | null; note: string | null; state: State }
type Screen = 'loading' | 'intro' | 'phone' | 'otp' | 'receipt' | 'lobby' | 'pick' | 'count' | 'reveal'

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

/** Looping character animation (Higgsfield clip on a cream card); falls back to the still pose. */
function Loop({ who, size = 260 }: { who: 'both' | Opp; size?: number }) {
  const [failed, setFailed] = useState(false)
  if (failed) return <Char who={who} mood="ready" size={size} />
  return (
    <motion.div initial={{ scale: 0.85, opacity: 0 }} animate={{ scale: 1, opacity: 1 }} transition={{ type: 'spring', stiffness: 220, damping: 16 }}
      className="mx-auto overflow-hidden rounded-[36px] shadow-[0_14px_30px_rgba(120,100,40,.15)]"
      style={{ width: `min(${size}px, 34dvh)`, height: `min(${size}px, 34dvh)`, background: '#fff6e0' }}>
      <video poster={`/game/loop_${who}.jpg`} autoPlay muted loop playsInline
        style={{ width: '100%', height: '100%', objectFit: 'cover', transform: `scale(${who === 'both' ? 1.32 : 1.22})`, transformOrigin: 'center 58%' }}>
        <source src={`/game/loop_${who}.webm`} type="video/webm" />
        <source src={`/game/loop_${who}.mp4`} type="video/mp4" onError={() => setFailed(true)} />
      </video>
    </motion.div>
  )
}

/** Soft floating leaves, hearts and sparkles behind every screen. */
function Floaties() {
  const items = useMemo(() => Array.from({ length: 14 }, (_, i) => ({ i, e: ['🍃', '💚', '✨', '🌸', '🍵'][i % 5], x: (i * 37) % 100, s: 14 + (i % 4) * 6, d: 9 + (i % 5) * 2.5, delay: (i % 7) * 1.3 })), [])
  return (
    <div className="pointer-events-none fixed inset-0 -z-0 overflow-hidden" aria-hidden>
      {items.map(f => (
        <motion.div key={f.i} initial={{ y: '105vh', x: `${f.x}vw`, opacity: 0 }} animate={{ y: '-10vh', opacity: [0, 0.55, 0.55, 0], rotate: [0, 25, -20, 0] }}
          transition={{ duration: f.d, delay: f.delay, repeat: Infinity, ease: 'linear' }} style={{ position: 'absolute', fontSize: f.s }}>{f.e}</motion.div>
      ))}
    </div>
  )
}

/** Speech bubble that types its text out. */
function Bubble({ text }: { text: string }) {
  const [n, setN] = useState(0)
  useEffect(() => { setN(0); const t = setInterval(() => setN(v => (v >= text.length ? v : v + 1)), 28); return () => clearInterval(t) }, [text])
  return (
    <motion.div initial={{ scale: 0.6, opacity: 0, y: 10 }} animate={{ scale: 1, opacity: 1, y: 0 }} transition={{ type: 'spring', stiffness: 300, damping: 18 }}
      className="relative mx-auto mt-3 max-w-[320px] rounded-[22px] bg-white px-4 py-3 text-center text-[16px] shadow-[0_8px_20px_rgba(120,100,40,.12)]">
      <span className="absolute -top-2 left-1/2 h-4 w-4 -translate-x-1/2 rotate-45 bg-white" />
      <span className="relative">{text.slice(0, n)}</span>
    </motion.div>
  )
}

const buzz = (ms: number | number[]) => { try { navigator.vibrate?.(ms) } catch {} }
const sfx = (name: Sfx, v?: number) => gameAudio().play(name, v)

function shareKind(result: string | null): ShareKind {
  return result === 'beat_both' ? 'grand' : result === 'beat_hibi' ? 'beat_hibi' : result === 'lost_capy' ? 'lost_capy' : 'lost_hibi'
}

/** In-app browsers (IG, FB, LINE, TikTok) cannot hand files to other apps, so they get save-the-image steps. */
function inAppBrowser(): boolean {
  if (typeof navigator === 'undefined') return false
  return /Instagram|FBAN|FBAV|FB_IAB|Line\/|TikTok|musical_ly|BytedanceWebview/i.test(navigator.userAgent)
}

/**
 * "Share my result". The story card is built as soon as the result shows, so the tap calls
 * navigator.share straight away (iOS Safari drops the share sheet if the tap waits on async work).
 * Instagram needs the image on its own: sending text with the file hides IG or drops the image,
 * so the caption + link go to the clipboard for a Link sticker instead.
 */
function ShareButton({ kind, prizes }: { kind: ShareKind; prizes: Prizes }) {
  const [open, setOpen] = useState(false)
  const [file, setFile] = useState<File | null>(null)
  const [img, setImg] = useState<string | null>(null)
  const [copied, setCopied] = useState(false)
  const [inApp, setInApp] = useState(false)
  const url = typeof window !== 'undefined' ? shareUrl() : ''
  const text = shareText(kind, prizes)

  useEffect(() => {
    let alive = true, obj: string | null = null
    setInApp(inAppBrowser())
    buildCard(kind, prizes).then(b => {
      if (!alive) return
      obj = URL.createObjectURL(b); setImg(obj)
      setFile(new File([b], 'hibi-capy-result.jpg', { type: b.type || 'image/jpeg' }))
    }).catch(() => {})
    return () => { alive = false; if (obj) URL.revokeObjectURL(obj) }
  }, [kind, prizes])

  async function copyCaption() {
    try { await navigator.clipboard.writeText(`${text} ${url}`); setCopied(true); return true } catch { return false }
  }

  async function shareImage() {
    sfx('tap'); buzz(15)
    copyCaption()   // not awaited: keeps the tap's user activation for navigator.share
    if (file && !inApp && navigator.canShare?.({ files: [file] })) {
      try { await navigator.share({ files: [file] }); return } catch (e) { if ((e as Error).name === 'AbortError') return }
    }
    setOpen(true)
  }

  async function shareLink() {
    sfx('tap')
    if (navigator.share) { try { await navigator.share({ text, url, title: 'เป่ายิ้งฉุบกับ Hibi & Capy' }); return } catch (e) { if ((e as Error).name === 'AbortError') return } }
    setOpen(true)
  }

  const enc = encodeURIComponent
  const links = [
    { label: 'Facebook', bg: '#1877F2', href: `https://www.facebook.com/sharer/sharer.php?u=${enc(url)}` },
    { label: 'LINE', bg: '#06C755', href: `https://line.me/R/share?text=${enc(text + ' ' + url)}` },
    { label: 'X', bg: '#111', href: `https://twitter.com/intent/tweet?text=${enc(text)}&url=${enc(url)}` },
  ]
  return (
    <>
      <motion.button className="hg-btn mt-3 bg-gradient-to-r from-[#f58529] via-[#dd2a7b] to-[#8134af] text-white" animate={{ rotate: [0, -2, 2, 0] }} transition={{ duration: 1.2, repeat: Infinity, repeatDelay: 1.5 }} onClick={shareImage} disabled={!file && !inApp}>
        {file || inApp ? 'แชร์ลง IG Story 📸' : 'กำลังเตรียมภาพ…'}
      </motion.button>
      <button className="hg-btn hg-soft mt-2" onClick={shareLink}>แชร์ลิงก์ให้เพื่อน 📣</button>
      <AnimatePresence>
        {open && (
          <motion.div className="fixed inset-0 z-50 flex items-end justify-center bg-black/40" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} onClick={() => setOpen(false)}>
            <motion.div className="max-h-[92dvh] w-full max-w-[440px] overflow-y-auto rounded-t-[32px] bg-[#fffaf0] p-5 pb-8" initial={{ y: 400 }} animate={{ y: 0 }} exit={{ y: 400 }} transition={{ type: 'spring', damping: 24 }} onClick={e => e.stopPropagation()}>
              <div className="display mb-1 text-center text-[20px] font-bold text-[#243e1b]">แชร์ลง IG Story</div>
              <p className="mb-3 text-center text-[13px] text-[#6b6a55]">{inApp ? 'กดค้างที่ภาพ แล้วเลือก "บันทึกรูปภาพ"' : 'กดค้างที่ภาพ หรือกดปุ่มบันทึกด้านล่าง'}</p>
              {img && <img src={img} alt="การ์ดผลการเล่น" className="mx-auto mb-3 h-[300px] rounded-2xl shadow-lg" style={{ WebkitTouchCallout: 'default' }} />}
              {!inApp && <a className="hg-btn hg-primary mb-3 block text-center" href={img ?? '#'} download="hibi-capy-result.jpg" onClick={() => sfx('tap')}>⬇️ บันทึกภาพ</a>}
              <ol className="hg-card mb-3 list-decimal space-y-1 p-4 pl-8 text-[14px] text-[#243e1b]">
                <li>บันทึกภาพลงเครื่อง</li>
                <li>เปิด Instagram → สร้าง Story → เลือกภาพนี้</li>
                <li>กดสติกเกอร์ <b>Link</b> แล้ววางลิงก์ที่คัดลอกไว้ ให้เพื่อนกดมาเล่นได้</li>
              </ol>
              {inApp && <p className="mb-3 rounded-2xl bg-[#fff3c4] p-3 text-center text-[13px] text-[#6b5a00]">เปิดจากในแอปอยู่ ถ้าบันทึกภาพไม่ได้ กด ⋯ มุมขวาบน → &quot;เปิดในเบราว์เซอร์&quot;</p>}
              <button className="hg-btn hg-soft mb-3 w-full" onClick={copyCaption}>{copied ? 'คัดลอกข้อความ + ลิงก์แล้ว ✓' : '🔗 คัดลอกข้อความ + ลิงก์'}</button>
              <div className="grid grid-cols-3 gap-2">
                {links.map(l => <a key={l.label} href={l.href} target="_blank" rel="noopener noreferrer" className="hg-btn block text-center text-white" style={{ background: l.bg, fontSize: 16 }} onClick={() => sfx('tap')}>{l.label}</a>)}
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
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

function CouponCard({ c, phone, terms }: { c: Coupon; phone: string; terms?: string[] }) {
  const exp = new Date(c.expiresAt).toLocaleDateString('th-TH', { day: 'numeric', month: 'short', year: '2-digit' })
  return (
    <motion.div initial={{ rotateY: 90, scale: 0.8 }} animate={{ rotateY: 0, scale: 1 }} transition={{ type: 'spring', stiffness: 160, damping: 14, delay: 0.3 }}
      className="hg-card hg-coupon relative overflow-hidden p-5 text-center" style={{ perspective: 800 }}>
      <motion.div className="pointer-events-none absolute inset-y-0 w-1/3" style={{ background: 'linear-gradient(100deg,transparent,rgba(255,255,255,.75),transparent)' }}
        initial={{ x: '-120%' }} animate={{ x: '420%' }} transition={{ duration: 1.6, delay: 0.9, repeat: Infinity, repeatDelay: 2.4 }} />
      <div className="display text-[15px] font-semibold text-[#e5484d]">🎟️ คูปองของคุณ</div>
      <div className="display mt-1 text-[40px] font-bold leading-none text-[#243e1b]">{c.label}</div>
      <div className="display mt-3 select-all rounded-2xl bg-[#243e1b] px-3 py-2 text-[24px] font-bold tracking-[2px] text-white">{c.code}</div>
      <div className="mt-3 text-[14px] text-[#6b6a55]">เบอร์ {phone} · ใช้ได้ถึง {exp}</div>
      <div className="mt-1 text-[14px] font-semibold text-[#3f8f3a]">📸 แคปหน้าจอนี้ แล้วโชว์พนักงานตอนมาครั้งถัดไป</div>
      {terms && <ul className="mt-3 space-y-0.5 rounded-2xl bg-[#fffaf0] p-3 text-left text-[12.5px] leading-snug text-[#6b6a55]">{terms.map(t => <li key={t}>• {t}</li>)}</ul>}
      {c.redeemed && <div className="mt-2 font-semibold text-[#e5484d]">ใช้สิทธิ์แล้ว</div>}
    </motion.div>
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
  const [prizes, setPrizes] = useState<Prizes | null>(null)
  const [last5, setLast5] = useState('')
  const [rDate, setRDate] = useState('')
  const [muted, setMutedState] = useState(false)
  useEffect(() => {
    setMutedState(gameAudio().muted)
    const unlock = () => gameAudio().unlock()
    window.addEventListener('pointerdown', unlock, { once: true })
    return () => window.removeEventListener('pointerdown', unlock)
  }, [])
  const toggleMute = () => { gameAudio().unlock(); const m = !gameAudio().muted; gameAudio().setMuted(m); setMutedState(m) }

  async function refresh() {
    const s = await api<{ loggedIn: boolean; phone?: string; state?: State; prizes?: Prizes }>('/api/game/state')
    if (s.prizes) setPrizes(s.prizes)
    if (s.loggedIn && s.state) {
      setState(s.state); setPrizes(s.state.prizes); setMaskedPhone(s.phone ?? '')
      if (s.state.needReceipt) { setRDate(d => d || s.state!.today); setScreen('receipt') } else setScreen('lobby')
    } else setScreen('intro')
  }
  useEffect(() => { refresh().catch(() => setScreen('intro')) }, [])

  async function run<T>(fn: () => Promise<T>) {
    setErr(null); setBusy(true)
    try { return await fn() } catch (e) { setErr((e as Error).message) } finally { setBusy(false) }
  }

  const sendOtp = () => run(async () => {
    sfx('tap')
    const r = await api<{ phone: string; demoCode?: string }>('/api/game/otp/request', { phone, consent })
    setDemoCode(r.demoCode ?? null); setCode(''); setScreen('otp')
  })
  const verify = () => run(async () => {
    sfx('tap')
    await api('/api/game/otp/verify', { phone, code })
    await refresh()
  })
  const submitReceipt = () => run(async () => {
    sfx('tap')
    const r = await api<{ state: State }>('/api/game/receipt', { last5, date: rDate })
    setState(r.state); buzz(20); setScreen('lobby')
  })
  const choose = (m: Move) => run(async () => {
    setScreen('count'); setBeat(0)
    const res = api<PlayRes>('/api/game/play', { move: m })
    res.catch(() => {})   // handled after the countdown
    buzz(30); sfx('beat')
    for (let i = 1; i <= 3; i++) { await new Promise(r => setTimeout(r, 650)); setBeat(i); buzz(i === 3 ? 60 : 30); sfx(i === 1 ? 'beat2' : i === 2 ? 'beat' : 'shoot') }
    try { const r = await res; setLast(r); setState(r.state); setScreen('reveal'); buzz(r.outcome === 'win' ? [40, 60, 120] : r.outcome === 'lose' ? 120 : [30, 40, 30])
      sfx('clash', 0.7)
      setTimeout(() => sfx(r.outcome === 'win' ? 'win' : r.outcome === 'lose' ? 'lose' : 'tie'), 380)
      if (r.newCoupon && r.newCoupon.percent === r.state.prizes.win2Percent) setTimeout(() => { gameAudio().duck(); sfx('grand', 0.9) }, 900)
      else if (r.newCoupon) setTimeout(() => sfx('coupon'), 1000) } catch (e) { setScreen('lobby'); throw e }
  })

  const opp: Opp = state?.stage === 'capy' ? 'capy' : (last?.opponent ?? 'hibi')
  const grand = state?.result === 'beat_both' && state.coupon?.percent === state.prizes.win2Percent
  const P = state?.prizes ?? prizes

  return (
    <main className="relative mx-auto flex min-h-[100dvh] max-w-[440px] flex-col px-4 pb-10 pt-6">
      <Floaties />
      <header className="mb-2 flex items-center justify-between">
        <div className="display text-[18px] font-bold text-[#243e1b]">Hibi Matcha Cafe</div>
        <div className="flex items-center gap-3">
          {maskedPhone && <div className="text-[13px] text-[#9a9578]">📱 {maskedPhone}</div>}
          <button aria-label={muted ? 'เปิดเสียง' : 'ปิดเสียง'} onClick={toggleMute} className="flex h-9 w-9 items-center justify-center rounded-full bg-white text-[18px] shadow">{muted ? '🔇' : '🔊'}</button>
        </div>
      </header>

      <AnimatePresence mode="wait">
        <motion.section key={screen + (last?.outcome ?? '')} style={{ position: 'relative', zIndex: 1 }} initial={{ opacity: 0, y: 16 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -12 }} transition={{ duration: 0.25 }} className="flex flex-1 flex-col">

          {screen === 'loading' && <div className="m-auto text-[#9a9578]">กำลังโหลด…</div>}

          {screen === 'intro' && <>
            <div className="mt-2 text-center">
              <h1 className="text-[34px] font-bold leading-tight text-[#243e1b]">
                {['เป่า', 'ยิ้ง', 'ฉุบ'].map((w, i) => (
                  <motion.span key={w} className="inline-block" animate={{ y: [0, -10, 0] }} transition={{ duration: 0.6, delay: i * 0.18, repeat: Infinity, repeatDelay: 1.6 }}>{w}</motion.span>
                ))}
                <br /><span className="text-[#e0a800]">กับ Hibi & Capy</span></h1>
            </div>
            <div className="my-3"><Loop who="both" size={270} /></div>
            <div className="hg-card space-y-1.5 px-5 py-4 text-[16px]">
              <div>🥇 <b>ชนะ Hibi</b> → {P?.win1 ?? ''}</div>
              <div>🏆 <b>ชนะทั้ง Hibi และ Capy</b> → <b className="text-[#e5484d]">{P?.win2 ?? ''}</b></div>
              <div className="text-[14px] leading-snug text-[#6b6a55]">🧾 ใช้เลขท้ายใบเสร็จ 5 หลัก + วันที่ · 1 ใบเสร็จเล่นได้ 1 ครั้ง</div>
            </div>
            <motion.button className="hg-btn hg-primary mt-5" animate={{ scale: [1, 1.04, 1] }} transition={{ duration: 1.4, repeat: Infinity }}
              onClick={() => { sfx('tap'); buzz(20); setScreen('phone') }}>เริ่มเล่นเลย! ✊✋✌️</motion.button>
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

          {screen === 'receipt' && state && <>
            <div className="flex justify-center"><Char who="both" size={190} /></div>
            <h2 className="text-center text-[24px] font-bold text-[#243e1b]">กรอกข้อมูลใบเสร็จ 🧾</h2>
            <p className="mb-4 text-center text-[15px] text-[#6b6a55]">ดูเลขที่ใบเสร็จ แล้วกรอก <b>5 หลักท้าย</b> และ<b>วันที่</b>ในใบเสร็จ</p>
            <label className="mb-1 text-[14px] font-semibold text-[#5b5a48]" htmlFor="r5">เลขท้ายใบเสร็จ 5 หลัก</label>
            <input id="r5" className="hg-input text-center text-[28px] tracking-[10px]" inputMode="numeric" maxLength={5} placeholder="•••••" value={last5} onChange={e => setLast5(e.target.value.replace(/\D/g, '').slice(0, 5))} />
            <label className="mb-1 mt-4 text-[14px] font-semibold text-[#5b5a48]" htmlFor="rd">วันที่ในใบเสร็จ</label>
            <input id="rd" type="date" className="hg-input text-center" min={state.receiptMinDate} max={state.today} value={rDate} onChange={e => setRDate(e.target.value)} />
            <p className="mt-2 text-center text-[13px] text-[#9a9578]">1 ใบเสร็จใช้เล่นได้ 1 ครั้ง · เก็บใบเสร็จไว้ให้พนักงานตรวจตอนใช้คูปอง</p>
            {err && <p className="mt-3 text-center font-semibold text-[#e5484d]">{err}</p>}
            <button className="hg-btn hg-primary mt-5" disabled={busy || last5.length !== 5 || !rDate} onClick={submitReceipt}>{busy ? 'กำลังตรวจสอบ…' : 'ยืนยันแล้วเล่นเลย! ✊✋✌️'}</button>
          </>}

          {screen === 'lobby' && state && <>
            {state.stage !== 'done' ? <>
              <div className="mt-2 text-center display text-[16px] font-semibold text-[#9a9578]">รอบที่ {OPP[state.stage].round} / 2</div>
              <h2 className="text-center text-[28px] font-bold text-[#243e1b]">เจอกับ {OPP[state.stage].name}!</h2>
              <div className="my-2"><Loop who={state.stage} size={250} /></div>
              <Bubble text={OPP[state.stage].line} />
              {!state.grandAvailable && <p className="mt-2 rounded-2xl bg-[#fff3c4] p-2 text-center text-[14px]">รางวัล{state.prizes.win2}ของวันนี้หมดแล้ว · ยังลุ้นรางวัลรอบแรกได้นะ</p>}
              {state.coupon && <p className="mt-2 text-center text-[14px] text-[#3f8f3a]">คุณได้ {state.coupon.label} แล้ว · ชนะ Capy อัปเกรดเป็น{state.prizes.win2}!</p>}
              <motion.button className="hg-btn hg-primary mt-5" animate={{ scale: [1, 1.04, 1] }} transition={{ duration: 1.4, repeat: Infinity }}
                onClick={() => { sfx('tap'); buzz(20); setScreen('pick') }}>พร้อมแล้ว! เป่า ยิ้ง ฉุบ</motion.button>
            </> : <>
              {grand && <Confetti />}
              <h2 className="mt-2 text-center text-[28px] font-bold text-[#243e1b]">{grand ? 'ชนะทั้งคู่! 🎉' : state.coupon ? 'เก่งมาก! 🎉' : 'วันนี้ยังไม่ใช่วันของเรา'}</h2>
              <div className="flex justify-center"><Char who={grand ? 'both' : state.result === 'lost_capy' ? 'capy' : 'hibi'} mood="win" size={220} /></div>
              {state.coupon ? <CouponCard c={state.coupon} phone={maskedPhone} terms={state.prizes.terms} /> : <p className="hg-card p-5 text-center text-[16px]">มาดื่มมัทฉะครั้งหน้า เอาใบเสร็จมาท้า Hibi & Capy ใหม่ได้นะ 💚🍵</p>}
              <ShareButton kind={shareKind(state.result)} prizes={state.prizes} />
              <p className="mt-4 text-center text-[13px] text-[#9a9578]">1 ใบเสร็จเล่นได้ 1 ครั้ง · วันละ 1 ครั้งต่อเบอร์</p>
            </>}
          </>}

          {screen === 'pick' && state && state.stage !== 'done' && <>
            <div className="mt-2 text-center display text-[16px] font-semibold text-[#9a9578]">รอบที่ {OPP[state.stage].round} / 2 · {OPP[state.stage].name}</div>
            <div className="my-2"><Loop who={state.stage} size={220} /></div>
            <h2 className="mb-4 text-center text-[24px] font-bold text-[#243e1b]">เลือกเลย!</h2>
            <div className="flex justify-center gap-4">
              {(['rock', 'paper', 'scissors'] as Move[]).map((m, i) => (
                <motion.button key={m} initial={{ y: 40, opacity: 0 }} animate={{ y: [0, -6, 0], opacity: 1, rotate: [0, -4, 4, 0] }}
                  transition={{ y: { duration: 1.6, repeat: Infinity, delay: i * 0.2 }, rotate: { duration: 1.6, repeat: Infinity, delay: i * 0.2 }, opacity: { duration: 0.3, delay: i * 0.08 } }}
                  whileTap={{ scale: 0.85 }} className="hg-move" disabled={busy} onClick={() => { sfx('tap'); buzz(15); choose(m) }}>
                  {HAND[m]}<span>{NAME[m]}</span>
                </motion.button>
              ))}
            </div>
            {err && <p className="mt-3 text-center font-semibold text-[#e5484d]">{err}</p>}
          </>}

          {screen === 'count' && <>
            <motion.div key={'c' + beat} animate={{ y: [0, -22, 0], rotate: [0, beat % 2 ? 6 : -6, 0], scaleY: [1, 0.94, 1] }} transition={{ duration: 0.45 }} className="flex justify-center">
              <Char who={opp} mood="ready" size={230} />
            </motion.div>
            <div className="mt-6 flex items-center justify-center gap-10 text-[80px]">
              <motion.div animate={{ y: [0, -34, 0], rotate: [0, -12, 0] }} transition={{ repeat: Infinity, duration: 0.65 }}>✊</motion.div>
              <motion.div animate={{ y: [0, -34, 0], rotate: [0, 12, 0] }} transition={{ repeat: Infinity, duration: 0.65 }}>✊</motion.div>
            </div>
            <motion.div key={beat} initial={{ scale: 1.6, opacity: 0 }} animate={{ scale: 1, opacity: 1 }} className="display mt-4 text-center text-[44px] font-bold text-[#243e1b]">
              {['เป่า…', 'ยิ้ง…', 'ฉุบ!', 'ฉุบ!'][beat]}
            </motion.div>
          </>}

          {screen === 'reveal' && last && <>
            {last.outcome === 'win' && last.opponent === 'capy' && last.newCoupon?.percent === last.state.prizes.win2Percent && <Confetti />}
            <motion.div className="flex justify-center"
              animate={last.outcome === 'win' ? { x: [0, -10, 10, -8, 8, 0] } : last.outcome === 'lose' ? { y: [0, -26, 0, -16, 0] } : { rotate: [0, -5, 5, 0] }}
              transition={{ duration: 0.9, delay: 0.5, repeat: Infinity, repeatDelay: 1.4 }}>
              <Char who={last.opponent} mood={last.outcome === 'win' ? 'lose' : last.outcome === 'lose' ? 'win' : 'ready'} size={220} />
            </motion.div>
            <div className="mt-2 flex items-center justify-center gap-6">
              <div className="text-center"><motion.div initial={{ x: -140, rotate: -60, scale: 0.6 }} animate={{ x: [-140, 12, 0], rotate: [-60, 8, 0], scale: [0.6, 1.15, 1] }} transition={{ duration: 0.45 }} className="text-[72px]">{HAND[last.playerMove]}</motion.div><div className="text-[14px] text-[#6b6a55]">คุณ</div></div>
              <motion.div initial={{ scale: 0 }} animate={{ scale: [0, 1.6, 1] }} transition={{ delay: 0.35, duration: 0.35 }} className="display text-[24px] font-bold text-[#9a9578]">💥</motion.div>
              <div className="text-center"><motion.div initial={{ x: 140, rotate: 60, scale: 0.6 }} animate={{ x: [140, -12, 0], rotate: [60, -8, 0], scale: [0.6, 1.15, 1] }} transition={{ duration: 0.45 }} className="text-[72px]">{HAND[last.opponentMove]}</motion.div><div className="text-[14px] text-[#6b6a55]">{OPP[last.opponent].name}</div></div>
            </div>
            <motion.h2 initial={{ scale: 0.6, opacity: 0 }} animate={{ scale: 1, opacity: 1 }} transition={{ delay: 0.25, type: 'spring' }}
              className={`mt-3 text-center text-[32px] font-bold ${last.outcome === 'win' ? 'text-[#3f8f3a]' : last.outcome === 'lose' ? 'text-[#e5484d]' : 'text-[#e0a800]'}`}>
              {last.outcome === 'tie' ? 'เสมอ! เอาใหม่ 🤝' : last.outcome === 'win' ? (last.opponent === 'capy' ? 'ชนะ Capy! 🏆' : 'ชนะ Hibi! 🎉') : `${OPP[last.opponent].name} ชนะ 😝`}
            </motion.h2>
            {last.note && <p className="mt-1 text-center text-[14px] text-[#8a5a2a]">{last.note}</p>}
            {last.newCoupon && <div className="mt-3"><CouponCard c={last.newCoupon} phone={maskedPhone} terms={last.state.prizes.terms} /></div>}
            <div className="mt-5 flex flex-col gap-3">
              {last.outcome === 'tie' && <button className="hg-btn hg-primary" onClick={() => { sfx('tap'); setScreen('pick') }}>เป่า ยิ้ง ฉุบ อีกครั้ง</button>}
              {last.state.stage === 'capy' && last.outcome === 'win' && <button className="hg-btn hg-primary" onClick={() => { sfx('tap'); setScreen('lobby') }}>ท้า Capy ต่อ! ลุ้น{last.state.prizes.win2} 🍊</button>}
              {last.state.stage === 'done' && <><ShareButton kind={shareKind(last.state.result)} prizes={last.state.prizes} /><button className="hg-btn hg-soft" onClick={() => { sfx('tap'); setScreen('lobby') }}>ดูผลของวันนี้</button></>}
            </div>
          </>}
        </motion.section>
      </AnimatePresence>

      <footer id="privacy" className="mt-8 text-center text-[12px] leading-relaxed text-[#9a9578]">
        เกมนี้จัดโดย Hibi Matcha Cafe · เราใช้เบอร์มือถือเพื่อยืนยันตัวตนและการใช้สิทธิ์รางวัลเท่านั้น<br />เงื่อนไขคูปอง: {(P?.terms ?? []).join(' · ')}
      </footer>
    </main>
  )
}
