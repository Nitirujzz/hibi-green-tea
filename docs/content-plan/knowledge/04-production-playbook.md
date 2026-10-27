# 04 · Production playbook — ขั้นตอนผลิตที่พิสูจน์แล้ว

> สคริปต์ต้นแบบอยู่ในแต่ละแคมเปญ: `campaigns/*/build_slides.py` (carousel) · `matcha-process-reel/src/compose.py` (reel จาก footage) · `vo-matcha-reel/src/build/` (reel จากเสียงพากย์: timing · mg · compose · sfx · ambient)

## 1) Higgsfield (ภาพ/วิดีโอ AI)
| งาน | โมเดล | ค่าที่ใช้ |
|---|---|---|
| ภาพนิ่ง/ตัวละคร/ฉากสาธิต | `gpt_image_2_5` | aspect 9:16 (reel) หรือ 4:5 (carousel) · ส่งชีตตัวละครเป็น reference |
| วิดีโอจากภาพ | `seedance_2_5` | `mode: omni_reference` · `medias: start_image` (+ `end_image` สำหรับทรานซิชัน) · 9:16 · 1080p · 5 วิ · **ใส่ `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612` เสมอ** |
| ถอดเสียง/จับเวลา | `video_analysis_create` | แปลงเสียงเป็นวิดีโอพื้นเขียวแล้วอัปโหลด · **ตัดเป็นช่วง ~10–18 วิ** จะแม่นกว่าทั้งไฟล์ · คำบรรยายภาพที่ได้ “มั่ว” ใช้แค่ audio |
- งานหลายชิ้นพร้อมกัน → `generate_image_batch` / `generate_video_batch` แล้ว `jobs_wait`
- ทำภาพนิ่งก่อน (ถูก/เร็ว) ดูคอนแทกต์ชีต → เลือกเฉพาะช็อตสำคัญไปทำวิดีโอ ที่เหลือใช้ Ken Burns
- Prompt ที่ได้ผล: ระบุ “bright minimal Japanese cafe counter, light oak wood, soft window daylight, white ceramic chawan, no text, no logos” → โทนตรงร้าน
- นำไฟล์เข้า Higgsfield: รูปใช้ `raw.githubusercontent.com/.../<sha>/path` ได้ · **วิดีโอใช้ jsDelivr** `cdn.jsdelivr.net/gh/Nitirujzz/hibi-green-tea@<sha สั้น 7 ตัว>/path` (sha ยาวบางครั้ง 403 · ไฟล์ต้อง < 20 MB)
- ใช้ฟุตเทจจริงเป็น start_image เพื่อสร้าง **มุมกล้องใหม่** (มาโคร/มุมต่ำ) ที่ดูกลมกลืนกับของจริง

## 2) ตัดต่อวิดีโอ (ffmpeg)
- ฟังก์ชัน `seg()/shot()`: scale 2× → `zoompan` → 1080×1920 · โหมดซูม: `ramp` (ดันช้า) · `punch` (1.16→1.0 ใน 8 เฟรม) · `punchramp`
- **Stabilizer**: `vidstabdetect` → `vidstabtransform` (2 pass) ลดการสั่น ~60%
- ซ่อนสิ่งที่ไม่ต้องการในเฟรม (เช่น ป้าย) ด้วย `z0` (ซูมเริ่มต้น 1.3) + `zy` (เลื่อนจุดกึ่งกลางลง)
- ภาพนิ่ง: `-loop 1` + zoompan · ช็อตยาว > 3.3 วิ แบ่งครึ่ง ครึ่งหลังซูมกระแทก (jump-cut)
- ตัดความยาวเป็นจำนวนเฟรมเป๊ะ (`round(t*30)`) แล้ว `concat -c copy`
- Safe zone Reels/TikTok: **x 70–950 · y 190–1440** (ล่างกว่านี้โดนปุ่ม/แคปชันบัง)

## 3) เสียงพากย์ (สูตร v2 ที่ผ่าน)
```
highpass=f=80, afftdn=nf=-50:nr=8:tn=1, deesser=i=0.35,
equalizer=f=250:t=q:w=1.2:g=-3, equalizer=f=140:t=q:w=1:g=1.5,
equalizer=f=3500:t=q:w=1.2:g=3, highshelf=f=10000:g=2,
dynaudnorm=f=200:g=11:p=0.9:m=8, acompressor=threshold=-20dB:ratio=3:attack=6:release=90:makeup=2,
loudnorm=I=-15:TP=-2:LRA=6
```
- ❌ อย่าใช้ `agate` แรง (เสียงขาด) · ใช้แค่ gate อ่อน `range=0.3` ตอนตัดต่อ
- **ตัด dead air** (`vo-matcha-reel/src/build/timing.py`):
  1. หา pause ด้วย `silencedetect=n=-42dB:d=0.10` บนไฟล์ที่ gate แล้ว (เพื่อให้เจอช่วงเงียบชัด)
  2. เก็บเสียงพูด + pad 0.04 วิ · ช่องว่างใหม่: ระหว่างคำ 0.06 · ระหว่างประโยค (>0.6 วิ เดิม) 0.16 · ก่อนข้อใหม่ 0.30
  3. `rubberband=tempo=1.1:formant=preserved` (เร็วขึ้นแต่โทนเดิม)
  4. ตรวจว่าไม่มีคำหลุด: ส่วนที่ตัดทิ้งต้องเบากว่าเสียงพูด > 30 dB · ตรวจ `silencedetect d=0.35` ต้องไม่เหลือช่วงเงียบ
  5. ฟังก์ชัน `m(t)` แปลงเวลาเดิม → เวลาใหม่ ใช้กับภาพ/กราฟิก/เสียงเอฟเฟกต์ทั้งหมด → ทุกอย่างตรงจังหวะอัตโนมัติ
- **Sound background**: `ambient.py` (pad + EP arpeggio + sub bass, 80 BPM, ไม่มีกลอง, reverb, ตัดช่วง 1–4 kHz) · ระดับ −24 LUFS ใต้เสียงพูด −14 · `sidechaincompress=threshold=0.05:ratio=2:attack=40:release=600` (หลบ ~3 dB)
  - ทางเลือกคึกคัก: `music.py` lo-fi 100 BPM มีกลอง ดรอปบีตตอนเข้าข้อ 1
- เสียงเอฟเฟกต์ (`sfx.py`): pop = sine sweep 0.18 วิ −17 dB · whoosh = pink noise band-pass −19 dB
- ส่งออกสุดท้าย: **−14 LUFS · true peak ≤ −1.5 dBTP** · AAC 192k

## 4) Motion graphic (HTML → PNG โปร่งใส → overlay)
- เขียน HTML 1080×1920 + ฟังก์ชัน JS `render(t)` คุมทุกองค์ประกอบตามเวลา (pop/slam/up/slide/wobble/shake/flash) → Playwright ถ่ายทีละเฟรม 30fps (`render_mg.js`, 4 หน้าเว็บขนาน ~2,500 เฟรม ≈ 3 นาที) → `overlay` ทับวิดีโอ
- องค์ประกอบมาตรฐาน: แถบความคืบหน้า ①–⑤ · การ์ดหัวข้อพร้อมวงเลข · การ์ด ❌/✅ · ตัวเลขนับขึ้น · เส้น SVG วาดตามจังหวะ (ตัว M) · ไอคอน SVG เด้ง · สติกเกอร์ 📌 · หน้าสรุป cheat sheet
- ใส่ **scrim ไล่เฉดมืดด้านบน** (alpha ~150→0, สูง 760px) ให้ตัวหนังสือขาวอ่านได้บนพื้นสว่าง
- ทดสอบด้วยการเรนเดอร์ไม่กี่เฟรม (`node render_mg.js out 30 0 <t1> <t2>…`) ทำคอนแทกต์ชีตก่อนเรนเดอร์จริง

## 5) Carousel / ตัวหนังสือไทย
- จัดหน้าเป็น HTML แล้ว Chromium headless screenshot (`/opt/pw-browsers/chromium --headless=new --screenshot --window-size=1080,<สูง+150>` แล้ว crop) — ภาษาไทยสระ/วรรณยุกต์ถูกต้อง ดีกว่าวาดด้วย PIL
- ฟอนต์: `@font-face` ชี้ `file:///root/.fonts/Prompt-<w>-thai.woff2` (+latin)
- ตัดพื้นหลังภาพสินค้า: `rembg` โมเดล `isnet-general-use` + remap alpha
- ปก/ภาพสินค้าจริง ลบเศษที่ไม่ต้องการด้วยการปรับ alpha เฉพาะโซน

## 6) QC ก่อนส่ง
- [ ] คอนแทกต์ชีต 16–24 เฟรมตลอดคลิป: ภาพตรงเสียง · ตัวหนังสือไม่ล้น · อยู่ใน safe zone
- [ ] Loudness −14 LUFS · ไม่มีช่วงเงียบ > 0.35 วิ
- [ ] ข้อมูลร้าน/ราคา/โปรตรงกับ 01-brand-facts · ไม่มีเรื่องที่ “รอยืนยัน” หลุดเป็นข้อเท็จจริง
- [ ] ระบุช็อต AI → เปิดป้าย AI-generated
- [ ] ทำปก (`cover.jpg`) + README แคมเปญ (โครงคลิป · แคปชัน · ก่อนโพสต์)
