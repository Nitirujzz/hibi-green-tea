// SMS delivery for OTP codes. GAME_OTP_MODE selects the provider:
//   demo   - no SMS; the code is returned to the page (prototype/testing only)
//   twilio - Twilio Messages API (TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM)
// Other Thai providers (ThaiBulkSMS, etc.) plug in here the same way.
import { isDemoMode } from './config'

export async function sendOtpSms(phone: string, code: string): Promise<void> {
  if (isDemoMode()) return
  const mode = process.env.GAME_OTP_MODE
  const text = `Hibi Matcha Cafe: รหัส OTP ของคุณคือ ${code} (ใช้ได้ 5 นาที)`
  if (mode === 'twilio') {
    const sid = process.env.TWILIO_ACCOUNT_SID, token = process.env.TWILIO_AUTH_TOKEN, from = process.env.TWILIO_FROM
    if (!sid || !token || !from) throw new Error('Twilio env vars are missing')
    const to = '+66' + phone.slice(1)
    const res = await fetch(`https://api.twilio.com/2010-04-01/Accounts/${sid}/Messages.json`, {
      method: 'POST',
      headers: { Authorization: 'Basic ' + Buffer.from(`${sid}:${token}`).toString('base64'), 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({ To: to, From: from, Body: text }),
    })
    if (!res.ok) throw new Error(`Twilio send failed: ${res.status}`)
    return
  }
  throw new Error(`Unknown GAME_OTP_MODE: ${mode}`)
}
