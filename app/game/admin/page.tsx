'use client'
import { useState } from 'react'

type Stats = { day: string; players: number; plays: number; win1: number; win2: number; redeemed: number; caps: { win1: number; win2: number } }
type Info = { code: string; label: string; percent: number; phone: string; expiresAt: string; redeemedAt: string | null }

async function call<T>(body: object): Promise<T> {
  const res = await fetch('/api/game/admin', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) })
  const data = await res.json()
  if (!res.ok) throw new Error(data.error ?? 'เกิดข้อผิดพลาด')
  return data
}

export default function GameAdmin() {
  const [pin, setPin] = useState('')
  const [stats, setStats] = useState<Stats | null>(null)
  const [code, setCode] = useState('')
  const [info, setInfo] = useState<Info | null>(null)
  const [msg, setMsg] = useState<string | null>(null)

  const act = async (action: string) => {
    setMsg(null)
    try {
      if (action === 'stats') setStats(await call<Stats>({ pin, action }))
      else { const r = await call<Info>({ pin, action, code }); setInfo(r); if (action === 'redeem') { setMsg('✅ ใช้สิทธิ์เรียบร้อย'); setStats(await call<Stats>({ pin, action: 'stats' })) } }
    } catch (e) { setMsg('❌ ' + (e as Error).message); if (action !== 'stats') setInfo(null) }
  }

  return (
    <main className="mx-auto max-w-[480px] px-4 py-8">
      <h1 className="text-[26px] font-bold text-[#243e1b]">หลังร้าน · เกมเป่ายิ้งฉุบ</h1>
      <p className="mb-4 text-[14px] text-[#6b6a55]">สำหรับพนักงาน: ตรวจและใช้สิทธิ์คูปองของลูกค้า</p>
      {!stats ? (
        <div className="hg-card p-5">
          <input className="hg-input" type="password" inputMode="numeric" placeholder="PIN พนักงาน" value={pin} onChange={e => setPin(e.target.value)} />
          <button className="hg-btn hg-primary mt-4 w-full" onClick={() => act('stats')}>เข้าสู่ระบบ</button>
        </div>
      ) : (
        <>
          <div className="hg-card grid grid-cols-2 gap-3 p-5 text-center">
            <div><div className="text-[13px] text-[#6b6a55]">เล่นวันนี้</div><div className="text-[28px] font-bold">{stats.plays}</div></div>
            <div><div className="text-[13px] text-[#6b6a55]">ผู้ลงทะเบียนทั้งหมด</div><div className="text-[28px] font-bold">{stats.players}</div></div>
            <div><div className="text-[13px] text-[#6b6a55]">รางวัลรอบแรกวันนี้</div><div className="text-[28px] font-bold">{stats.win1}<span className="text-[14px] text-[#9a9578]"> / {stats.caps.win1}</span></div></div>
            <div><div className="text-[13px] text-[#6b6a55]">ส่วนลด 50% วันนี้</div><div className="text-[28px] font-bold text-[#e5484d]">{stats.win2}<span className="text-[14px] text-[#9a9578]"> / {stats.caps.win2}</span></div></div>
            <div className="col-span-2 text-[13px] text-[#6b6a55]">ใช้สิทธิ์แล้วทั้งหมด {stats.redeemed} ใบ · {stats.day}</div>
          </div>
          <div className="hg-card mt-4 p-5">
            <input className="hg-input uppercase tracking-[2px]" placeholder="HIBI-XXXX-XXXX" value={code} onChange={e => setCode(e.target.value)} />
            <div className="mt-3 flex gap-3">
              <button className="hg-btn hg-soft flex-1" onClick={() => act('lookup')}>ตรวจสอบ</button>
              <button className="hg-btn hg-primary flex-1" onClick={() => act('redeem')}>ใช้สิทธิ์</button>
            </div>
            {msg && <p className="mt-3 font-semibold">{msg}</p>}
            {info && (
              <div className="mt-3 rounded-2xl bg-[#f6f2e6] p-4 text-[15px] leading-relaxed">
                <div><b>{info.label}</b> · {info.code}</div>
                <div>เบอร์ {info.phone.slice(0, 3)}-xxx-{info.phone.slice(6)}</div>
                <div>หมดอายุ {new Date(info.expiresAt).toLocaleDateString('th-TH')}</div>
                <div>{info.redeemedAt ? `ใช้แล้วเมื่อ ${new Date(info.redeemedAt).toLocaleString('th-TH')}` : 'ยังไม่ได้ใช้'}</div>
              </div>
            )}
          </div>
        </>
      )}
    </main>
  )
}
