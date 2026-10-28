# 06 · Tools & limits — ข้อจำกัดที่เจอ และทางแก้

| ปัญหา | ทางแก้ |
|---|---|
| โหลดโมเดลถอดเสียง (Whisper/Vosk) ไม่ได้ — host ถูกบล็อก (openaipublic, huggingface, alphacephei, github releases) | ถอดเสียงด้วย Higgsfield `video_analysis` (เสียง → วิดีโอพื้นสี) ตัดเป็นช่วงสั้น |
| Higgsfield import วิดีโอจาก raw GitHub ไม่ได้ (octet-stream) | ใช้ jsDelivr + sha สั้น 7 ตัว (ถ้า 403 ให้ลองใหม่/เปลี่ยน sha) · จำกัด 20 MB |
| `upload.higgsfield.ai` ถูกบล็อก | ส่งไฟล์ให้ Buffer ด้วย raw GitHub โดยตรง |
| ไม่มีโมเดลแต่งเพลง AI ที่ใช้ได้ (Suno ไม่มีใน catalog · sonilo ใช้ได้แค่ game pipeline) | สังเคราะห์เพลง/เสียงพื้นหลังเองด้วย numpy (`ambient.py`, `music.py`) — ไม่ติดลิขสิทธิ์ |
| Buffer TikTok รับสูงสุด 10 ภาพ | ตัดสไลด์รอง (เช่น หน้าความหวาน/หน้าจบ) |
| heredoc ไม่ใส่เครื่องหมายคำพูด → backtick ถูกรันเป็นคำสั่ง | ใช้ `<<'EOF'` หรือเขียนไฟล์ด้วย Python |
| ไฟล์ overlay ชื่อซ้ำกับ art ทับกัน | ตั้งชื่อ art แยก (`art_end.png`) |
| ทรานซิชัน AI เริ่มที่เฟรมเดิม ดูเหมือนย้อนขั้น | ตัดหัวคลิปทรานซิชัน (`ss 0.9`) |
| Playwright/Chromium | มีติดตั้งแล้ว `require('playwright')` · `/opt/pw-browsers/chromium` · ห้าม `playwright install` |
| ดิสก์ | งานคลิปใช้ ~1–2 GB ต่อชิ้นใน scratchpad (เฟรม PNG) — ลบ `frames/` หลังเสร็จได้ |
| เครดิต Higgsfield หมดกลางงาน (วิดีโอ Seedance 4–5 วิ ใช้เครดิตมาก) | เช็ก `balance` ก่อนสั่งชุดใหญ่ · ช็อตที่ขาดใช้ภาพนิ่ง + zoompan + motion graphic แทนได้ |
| Seedance ตอบ `ip_detected` (ปฏิเสธบางช็อตตัวละคร) | ใช้ภาพนิ่ง fallback หรือเขียน prompt ใหม่ให้เลี่ยงคำที่ไวต่อระบบ |
| Seedance แนะนำ preset แทนการสร้าง (เช่น “Earth zoom out” เมื่อ prompt มีคำว่า zoom out) | ใส่ `declined_preset_id` ของ preset นั้น หรือเลี่ยงคำว่า zoom out |
