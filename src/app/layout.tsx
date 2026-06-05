import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Hibi Matcha | 日々 抹茶 — ชาญี่ปุ่นแท้จริงทุกวัน',
  description: 'นำประสบการณ์ชาญี่ปุ่นแท้จริงมาสู่ชีวิตประจำวันของคนไทย — Ceremonial Grade Matcha จาก Uji, Kyoto',
  keywords: ['matcha', 'มัทฉะ', 'ชาญี่ปุ่น', 'Hibi Matcha', 'ceremonial grade', 'uji matcha'],
  openGraph: {
    title: 'Hibi Matcha | 日々 抹茶',
    description: 'A Moment in Every Sip — ทุกวันมีเรื่องราว ทุกแก้วมีความสุข',
    siteName: 'Hibi Matcha',
    locale: 'th_TH',
    type: 'website',
  },
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="th">
      <head>
        <link rel="icon" href="/images/brand/logo-icon.png" />
      </head>
      <body className="font-brand antialiased">
        {children}
      </body>
    </html>
  )
}
