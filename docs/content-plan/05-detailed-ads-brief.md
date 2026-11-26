# Hibi Matcha Cafe — Ads Brief ละเอียดรายองค์ประกอบ (สำหรับทีมกราฟิก)

> ต่อยอดจาก [03 Ads Brief](./03-ads-brief.md) · Prompt ที่อ้างถึง (I*, V*, A*, T*) อยู่ใน [04 AI vs Graphics + Prompt Library](./04-ai-vs-graphics-and-prompts.md)
> สัญลักษณ์แหล่งที่มาของแต่ละ Layer: 🤖 AI สร้าง · 📷 ถ่ายจริง · 🎨 กราฟิกทำ · 🔀 AI ทำฐาน → กราฟิกจบ
> พิกัดทั้งหมดเป็น **px บนแคนวาส Master 1080×1350 (4:5)** วัดจากมุมซ้ายบน `(x, y, w, h)` ยกเว้นระบุเป็นอื่น

---

## PART A — Global Design Spec (ใช้ทุกชิ้น)

### A1. Canvas & Grid
| รายการ | ค่า |
|---|---|
| Master | 1080×1350 (4:5), 72 dpi, sRGB |
| Margin | 60 px ทุกด้าน → Live area `(60, 60, 960, 1230)` |
| Column | 6 คอลัมน์ กว้าง 140 / gutter 24 |
| Baseline | 8 px (ระยะทุกอย่างเป็นเลขคูณ 8) |
| 9:16 | 1080×1920 · Live area `(60, 250, 960, 1330)` — **บน 250 / ล่าง 340 / ขวา 120 ห้ามมีข้อความ** |
| 1:1 | 1080×1080 · margin 60 |

### A2. Color Tokens
| Token | HEX | ใช้ |
|---|---|---|
| `matcha-700` | `#15803d` | ตัวหนังสือบนพื้นอ่อนที่ต้องการคอนทราสต์สูง |
| `matcha-600` | `#16a34a` | Headline, ปุ่ม, แถบแบรนด์ |
| `matcha-500` | `#22c55e` | ไอคอน/เส้นไฮไลต์เล็ก ≤ 5% |
| `cream` | `#fef7cd` | พื้นหลังหลัก |
| `pearl` | `#f8fafc` | พื้นหลัง Infographic |
| `clay` | `#92400e` | Sub-headline, เส้น, ชื่อเมนู EN |
| `stone` | `#78716c` | Fine print |
| `gold` | `#fbbf24` | Badge, ราคา, คูปอง |
| `copper` | `#c2410c` | Limited / หมดเขต ≤ 5% |
| `white` | `#ffffff` | ตัวหนังสือบนปุ่ม |

คอนทราสต์ขั้นต่ำ: ตัวหนังสือ ≥ 4.5:1 (ขาวบน `matcha-600` ผ่านที่ขนาด ≥ 28px Bold; ถ้าเล็กกว่าให้ใช้ `matcha-700`)

### A3. Type Scale
| Style | Font | Size / Line height | Weight | สี default |
|---|---|---|---|---|
| H1 Headline | Kanit | 84 / 100 | Bold | `matcha-600` |
| H2 | Kanit | 56 / 68 | SemiBold | `matcha-600` |
| Sub | Kanit | 40 / 52 | Medium | `clay` |
| EN Label | Inter | 34 / 40 · tracking +2% | SemiBold | `clay` |
| Body | IBM Plex Sans Thai | 30 / 44 | Regular | `#3f3f46` |
| Feature | IBM Plex Sans Thai | 28 / 36 | Medium | `clay` |
| Price | Kanit | 56 (ตัวเลข) + 28 (฿) | Bold | `clay` บน `gold` |
| CTA | Kanit | 34 / 40 | SemiBold | `white` |
| Fine print | IBM Plex Sans Thai | 20 / 28 | Regular | `stone` |

กฎ: Headline ≤ 2 บรรทัด ≤ 7 คำ · ห้ามตัวหนังสือเล็กกว่า 20px · ห้ามจัดกึ่งกลางเกิน 3 บรรทัดติดกัน

### A4. Component Spec
| Component | Spec |
|---|---|
| **CTA Button** | สูง 88 · กว้างตามข้อความ + padding ซ้ายขวา 48 (ขั้นต่ำ 360) · radius 44 · `matcha-600` · ไอคอนลูกศร → 28px ขาว ห่างข้อความ 12 · เงา `0 8 24 rgba(22,163,74,.25)` |
| **Badge "ใหม่!/NEW"** | Pill 140×56 · radius 28 · `gold` · Kanit Bold 30 `clay` · หมุน -6° |
| **Price Tag** | วงกลม Ø 160 · `gold` · ขอบขาว 6 · ตัวเลข Kanit Bold 56 `clay` · "฿" 28 ยกขึ้น |
| **Coupon** | สี่เหลี่ยม 760×300 · radius 24 · พื้น `matcha-600` · ขอบปรุครึ่งวงกลม Ø 40 ทั้งสองข้างที่ 60% ความกว้าง · ตัวเลขส่วนลด Kanit Bold 120 `gold` |
| **Info Icon row** | ไอคอนเส้น 3px ขนาด 40 สี `clay` · ข้อความ Feature 28 · ระยะระหว่างชุด 40 |
| **Brand Bar** | แถบเต็มกว้าง สูง 96 · `matcha-600` · ข้อความขาว Kanit SemiBold 36 |
| **Logo** | ขนาดกว้าง 180 (Feed) / 200 (Story) · clear space รอบโลโก้ = ความสูงตัว "H" · ใช้เวอร์ชันเขียวบนพื้นอ่อน, ขาวบนพื้นเขียว/ภาพเข้ม |
| **Slide counter** | "02/06" Inter Medium 24 `stone` มุมซ้ายบน (60,60) |

### A5. Image Treatment
| ประเภท | การปรับ |
|---|---|
| ภาพสินค้าจริง 📷 | Temp +5 (อุ่น), Exposure +0.2, Highlights −20, Shadows +15, Saturation **เฉพาะเขียว** +5 (ห้ามเกิน +10 — กันเขียวนีออน), Clarity +5 ที่ฟอง · ตัดพื้น (cutout) เมื่อวางบนฉาก AI · เงาตก `0 24 48 rgba(146,64,14,.18)` |
| ฉาก AI 🤖 | Gaussian blur 4–8px ถ้าอยู่หลังสินค้า · ลด saturation −10 ให้สินค้าเด่นกว่า · Overlay gradient `cream` 0→80% จากบนลง 40% แรก (เพื่อวางข้อความ) |
| Capy 🔀 | PNG โปร่งใส · เงาวงรีใต้ตัว `clay` 15% blur 12 · ขนาด 15–30% ของแคนวาส |

### A6. Capy Placement Rules
1. Capy **มอง/ชี้เข้าหา** สินค้าหรือ CTA เสมอ (พาสายตา)
2. ห้ามทับ: หน้าแก้ว, ราคา, CTA, โลโก้
3. ตำแหน่งที่อนุญาต: มุมขวาล่าง (default), ซ้ายล่าง, หรือ "โผล่" จากขอบภาพ
4. 1 ภาพ = Capy 1 ตัว (ยกเว้น Family)

---

## PART B — Base Assets (ทำครั้งเดียว ใช้ทั้งแคมเปญ)

### B1. 🎨 Hibi-Capy Master Model Sheet (ต้องเสร็จก่อนทุกงาน)
| รายการ | Spec |
|---|---|
| มุมมอง | หน้าตรง, 3/4 ซ้าย, 3/4 ขวา, ข้าง, หลัง |
| สัดส่วน | ตัว 2.2 หัว · ตา = จุด/เส้นโค้งสั้น · จมูกกว้าง 30% ของหน้า · ขายาว 15% ของความสูง |
| สี | ขน `#C8935A` · เงา `#A0703F` · จมูก `#5C3A1E` · แก้ม `#F4B6A6` · เส้น `clay` 4px (ที่ 3000px) |
| ถ้วยบนหัว | ถ้วยเซรามิกครีม ปากถ้วยเห็นมัทฉะ `matcha-600` กว้าง 35% ของหัว |
| Expression | 7 แบบ (ดู 04 – I2) วาด master ให้ครบ 7 แบบเพื่อใช้เป็น reference ให้ AI |
| ชุดสาขา | 5 ชุด (ดู 04 – I3) |
| ส่งมอบ | AI/SVG + PNG โปร่งใส 3000px ทุกท่า + ไฟล์ reference รวม 1 หน้า (ใช้ upload เป็น `--cref`/reference) |

### B2. 🎨 Logo Lockups
แนวนอน (โลโก้ + Capy หน้า) · แนวตั้ง · โลโก้อย่างเดียว · ไอคอน Capy (Avatar 1:1) — แต่ละแบบมีสีเขียว/ขาว/ครีม

### B3. 📷 Product & Branch Shoot List (สาขาถ่ายส่ง)
| Shot | มุม | ฉาก | ใช้กับ |
|---|---|---|---|
| P1 Hero แก้วเดี่ยว | ระดับสายตา 0° · 85mm หรือมือถือ 2× | พื้นหลังครีม/ไม้เรียบ · แสงหน้าต่างด้านซ้าย | A2, A6 |
| P2 Layer pour | ระดับสายตา · 120fps slow-mo | เทนมลงมัทฉะ เห็น layer | A1, A2 Story |
| P3 ตีมัทฉะ | Top-down 90° + 45° | ถ้วย + ฉะเซ็น · เสียงชัด (ไมค์ใกล้) | A1, A4 |
| P4 ร่อนผง | Macro | ผงเขียวโปรยผ่านตะแกรง แสงย้อน | A1 |
| P5 บรรยากาศสาขา | Wide 0.5× + Medium | ช่วงคนน้อย แสงธรรมชาติ ไม่มีหน้าลูกค้า (หรือมีใบยินยอม) | A3 |
| P6 มุมเด่นสาขา | ตามบทบาทสาขา | Bar / โซนครอบครัว / เคาน์เตอร์ Pick-up / โต๊ะปลั๊ก / Photo spot | A3 |
| P7 หน้าร้าน | ระดับสายตา ตรง | ป้ายร้านชัด | A1 V5, GBP |
ไฟล์: RAW/HEIC + JPG สูงสุด, วิดีโอ 4K 60fps แนวตั้ง, ถ่ายเผื่อพื้นที่ว่างด้านบน 30%

### B4. 🎨 Icon Set (เส้น 3px, มุมมน, สี `clay`)
ใบชา · ไม้ตี (chasen) · ถ้วย · ความหวาน (หยดน้ำ) · นาฬิกา · หมุดแผนที่ · รถ · คนเดิน · ปลั๊ก · Wi-Fi · ของขวัญ · แสตมป์ · LINE (ใช้ไอคอนทางการตามแนวทางของ LINE)

### B5. 🔀 Pattern & Texture
ลายใบชาโปร่ง (opacity 5–8%) · ลายคลื่นญี่ปุ่น seigaiha (opacity 5%) · พื้นผิวกระดาษวาชิ — AI สร้างฐาน (prompt: `seamless subtle washi paper texture, cream color, no text`) แล้วกราฟิกทำให้ต่อกันไร้รอย

---

## PART C — Ads Brief รายชิ้น

---

### 🟢 A1 · "Meet Hibi-Capy" — Brand Video 15s

**Job Info**
| รายการ | รายละเอียด |
|---|---|
| Code | `HIBI_A1` |
| Funnel / Objective | TOFU / Reach + ThruPlay |
| Audience | 18–40 ปี · รัศมี 7 กม. รอบ 5 สาขา · สนใจคาเฟ่ ญี่ปุ่น คาปิบาร่า |
| Placement | Reels · TikTok · Story (9:16 master) · Feed 4:5 (เวอร์ชัน crop) |
| Key Message | **"เหนื่อยแค่ไหน แวะชิลกับมัทฉะของ Hibi"** |
| Key Takeaway | ① จำ Hibi-Capy ได้ ② Hibi = มัทฉะตีสด ③ มี 5 สาขาใกล้ฉัน |
| Mood | ช้า อบอุ่น ขำเบา ๆ → ผ่อนคลาย |
| CTA | "ดูสาขาใกล้คุณ" |

**Shot-by-shot Spec (1080×1920, 30fps)**
| # | เวลา | ภาพ | Source | ข้อความบนจอ (Kanit, กราฟิกพิมพ์) | ตำแหน่งข้อความ | เสียง | Motion |
|---|---|---|---|---|---|---|---|
| S1 | 0.0–2.0 | Capy (Sleepy) โต๊ะทำงานกองเอกสาร | 🔀 V3 + Capy master | "วันนี้เหนื่อยไหม…" H2 56 ขาว เงาดำ 30% | กลาง `(60, 300, 960)` | คีย์บอร์ด + แจ้งเตือน | Push-in 105% · ข้อความ typewriter 0.6s |
| S2 | 2.0–5.0 | Capy เดินเข้าหน้าร้านจริง | 🔀 V5 + 📷 P7 | — | — | กระดิ่งประตู · เพลงเริ่ม (A2) | ตัด Hard cut · ประตูเปิดแสงอุ่น |
| S3 | 5.0–6.5 | ร่อนผง Macro | 📷 P4 | "ตีสดทุกแก้ว 🍵" H2 56 `matcha-600` บนแถบครีม 80% | ล่าง `(60, 1400, 960)` | ผงโปรย | Slow-mo 50% |
| S4 | 6.5–8.0 | ตีมัทฉะ Top-down | 📷 P3 | (ค้างข้อความ S3) | — | **ASMR ฉะเซ็น** (ดังสุดของคลิป) | — |
| S5 | 8.0–9.0 | เทนม Layer | 📷 P2 | — | — | เสียงเท | Speed ramp 100→40% |
| S6 | 9.0–12.0 | Capy Onsen ในแก้วยักษ์ | 🔀 V4 | "ชิลแล้ว~" H1 84 `matcha-600` | บน `(60, 320, 960)` | "ฮ่าาา" + เพลงเต็ม | Bounce-in scale 0→110→100% 0.4s |
| S7 | 12.0–15.0 | End card | 🎨 | ดูตาราง End card | — | Jingle chime | ดูด้านล่าง |

**End card Layer Spec (1080×1920)**
| # | Layer | Content | Source | Position (x,y,w,h) | Style | Motion (เริ่มที่ 12.0s) |
|---|---|---|---|---|---|---|
| 1 | Background | พื้น `cream` + texture วาชิ 6% | 🎨 B5 | 0,0,1080,1920 | — | Fade จาก S6 0.3s |
| 2 | Logo | โลโก้แนวตั้ง เขียว | 🎨 B2 | 440,300,200,auto | — | Fade-up 20px 0.4s |
| 3 | Tagline EN | "Every day, a little calm." | 🎨 | 60,560,960 | Inter SemiBold 44 `clay` center | +0.2s fade |
| 4 | Capy | Onsen pose | 🔀 I2-⑥ | 290,700,500,500 | เงาวงรี | Float loop ±8px 2s |
| 5 | Branch line | "📍 5 สาขา: [BR1] · [BR2] · [BR3] · [BR4] · [BR5]" | 🎨 | 60,1260,960 | Feature 28 `clay` center, 2 บรรทัดได้ | +0.4s |
| 6 | CTA | "ดูสาขาใกล้คุณ →" | 🎨 A4 | 270,1400,540,88 | CTA Button | Scale pulse 100→104% ทุก 1s |
| 7 | Safe zone | ว่าง | — | y 0–250 / 1580–1920 | — | — |

**Feed 4:5 Adaptation:** crop กลางของแต่ละช็อต · ข้อความขยับให้อยู่ใน live area 4:5 · End card: Logo (450,140) · Tagline y380 · Capy (330,470,420,420) · Branch y940 · CTA (300,1080)

**ซับไตเติล:** IBM Plex Sans Thai SemiBold 36 ขาว ขอบดำ 3px · y 1450 (9:16) · ทุกประโยคพากย์

**Deliverables:** `HIBI_A1_ALL_Reels_15s_v1.mp4` · `_Feed45_15s` · `_Bumper_6s` (S4+S6+End card) · ไฟล์ซับ .srt · Project file

---

### 🟢 A2 · "Menu Hero" — Signature Drink

**Job Info**
| รายการ | รายละเอียด |
|---|---|
| Code | `HIBI_A2` |
| Funnel / Objective | TOFU→MOFU / Engagement + Traffic |
| เมนู | `[ชื่อเมนูซิกเนเจอร์]` เช่น "Capy Cloud Matcha" · ราคา `[xx]` บาท |
| Key Message | **"มัทฉะเข้ม × ครีมนุ่มเหมือนเมฆ — แก้วที่ Capy เลือก"** |
| Key Takeaway | ① ชื่อ+หน้าตาเมนู ② รส: เข้ม-นุ่ม-หวานเลือกได้ ③ มีทุกสาขา ราคา `[xx]` |
| CTA | "ไปลองที่สาขาใกล้คุณ" |
| ลำดับสายตา | ① แก้ว (Hero) → ② Headline → ③ ราคา → ④ CTA |

**Layer Spec — Master Feed 4:5 (1080×1350)**
| # | Layer | Content | Source | Position (x,y,w,h) | Style / Spec |
|---|---|---|---|---|---|
| 1 | Background | โต๊ะไม้ข้างหน้าต่าง เว้นกลาง | 🤖 I1 | 0,0,1080,1350 | blur 6px · sat −10 · gradient `cream` 85%→0 จาก y0→y540 |
| 2 | Pattern | ลายใบชา | 🎨 B5 | 0,0,1080,1350 | opacity 5% · blend Multiply |
| 3 | Logo | แนวนอน เขียว | 🎨 B2 | 60,60,180,auto | — |
| 4 | Badge | "ใหม่!" | 🎨 A4 | 880,60,140,56 | Badge spec · หมุน −6° |
| 5 | Headline | "มัทฉะเข้ม × ครีมเมฆ" | 🎨 (copy จาก T8) | 60,156,960,200 | H1 84/100 `matcha-600` · ซ้าย · 2 บรรทัดสูงสุด |
| 6 | Menu name EN | "Capy Cloud Matcha" | 🎨 | 60,364,960,40 | EN Label 34 `clay` |
| 7 | Hero product | แก้วจริง cutout | 📷 P1 → 🎨 retouch | 270,430,540,640 | Image treatment A5 · เงาตก · แก้วตั้งตรง ไม่บิดมุม |
| 8 | Cloud accent | ก้อนเมฆครีมเล็ก 2 ก้อนรอบแก้ว | 🎨 vector | ~230,470 / ~800,520 · Ø 80–120 | ขาว 90% · ห้ามทับฟองจริง |
| 9 | Capy | Point (ชี้ซ้ายไปที่แก้ว) — **flip แนวนอน** | 🔀 I2-⑦ | 800,800,240,280 | เงาวงรี · ตัวโผล่ทับขอบขวาได้ |
| 10 | Feature row | 🍃 มัทฉะ `[อุจิ]` · 🍵 ตีสดทุกแก้ว · 💧 หวานเลือกได้ | 🎨 B4 | 60,1094,960,40 | Info icon row · กระจายเท่ากัน |
| 11 | Price tag | "฿[xx]" | 🎨 A4 | 60,1150,160,160 | Price spec |
| 12 | CTA | "ไปลองที่สาขาใกล้คุณ →" | 🎨 A4 | 560,1186,460,88 | CTA spec |
| 13 | Fine print | "*ราคาไซซ์ [M] · ทุกสาขา · ตั้งแต่ [วันที่]" | 🎨 | 240,1290,780,28 | Fine print 20 `stone` ชิดขวา |

**9:16 Story Adaptation (1080×1920)**
| Layer | Position ใหม่ |
|---|---|
| BG | ใช้ I5 ต่อพื้นหลังภาพเป็น 9:16 หรือ I1 `--ar 9:16` |
| Logo | 60,260 · Badge 880,260 |
| Headline | 60,360 (H1 84) · EN 60,568 |
| Hero | 240,660,600,720 |
| Capy | 800,1120,240,280 |
| Feature | 60,1420 |
| Price | 60,1480 Ø140 · CTA 520,1490,500,88 |
| Fine print | ย้ายไปแคปชันแอด (พื้นที่ล่าง 340 ห้ามใช้) |

**Motion Story 8s:** 0–2s P2 เทครีม (Hook ไม่มีข้อความ) → 2.0s Headline slide-up 24px 0.4s ease-out → 3.0s Capy pop-in (scale 0→110→100) → 4.0s Feature row stagger 0.15s → 5.0s Price spin-in 0.3s → 5.5s CTA fade + pulse → ค้างถึง 8s

**1:1 Adaptation (1080×1080):** ตัด Feature row · Headline 1 บรรทัด (H1 72) · Hero 300,250,480,560 · Price 60,880 Ø140 · CTA 560,906

**Do / Don't**
| ✅ | ❌ |
|---|---|
| ฟองครีมและ layer มัทฉะเห็นชัด | ใช้ภาพแก้วที่ AI วาด |
| แก้วกินพื้นที่ 40–50% | ใส่ข้อความทับแก้ว |
| ราคาชัด อ่านได้ใน 1 วิ | เขียว saturate จนนีออน |

**Deliverables:** `HIBI_A2_ALL_Feed45_v1/v2(B)` · `_Story916_v1` · `_Story916_motion_8s.mp4` · `_Feed11_v1`
**A/B:** v1 Headline อารมณ์ ("แก้วที่ Capy เลือก") vs v2 Headline รสชาติ ("เข้ม นุ่ม หวานน้อย") — copy จาก T8

---

### 🟢 A3 · "Branch Finder" — 5 เวอร์ชัน (1 Master + 5 Variants)

**Job Info**
| รายการ | รายละเอียด |
|---|---|
| Code | `HIBI_A3_BR1…BR5` |
| Funnel / Objective | BOFU / Store traffic (คลิกเส้นทาง) |
| Audience | Geo 3–5 กม. ต่อสาขา (แยก Ad set) |
| Key Message (โครง) | **"Hibi สาขา [ชื่อ] — [จุดเด่น] ห่างจากคุณแค่ [x] นาที"** |
| Key Takeaway | ① สาขาอยู่ไหน ② เหมาะกับฉันเพราะอะไร ③ มีสิทธิพิเศษเฉพาะสาขา |
| CTA | "ดูเส้นทาง →" |
| วัดผล | โค้ด `HIBI-BR1` … `HIBI-BR5` บนภาพ |
| ลำดับสายตา | ① ชื่อสาขา (Brand bar) → ② ภาพสาขา → ③ Headline → ④ Offer → ⑤ CTA |

**Master Layer Spec — Feed 4:5** (★ = ช่องที่เปลี่ยนตามสาขา)
| # | Layer | Content | Source | Position (x,y,w,h) | Style |
|---|---|---|---|---|---|
| 1 | Background | `cream` | 🎨 | 0,0,1080,1350 | texture วาชิ 6% |
| 2 | Brand bar | "📍 Hibi สาขา ★[ชื่อสาขา]" | 🎨 A4 | 0,0,1080,96 | Brand bar · ข้อความ 60,28 · โลโก้ขาว ขวา 880,24,140 |
| 3 | Branch photo | ★ภาพบรรยากาศสาขาจริง | 📷 P5/P6 → 🎨 | 60,128,960,680 | radius 24 · Image treatment |
| 4 | Capy | ★Capy ชุดสาขา | 🔀 I3 | 780,600,260,300 | วางทับมุมขวาล่างของภาพ ล้นขอบภาพลงมา 90px · มองซ้าย |
| 5 | Headline | ★Headline สาขา | 🎨 | 60,848,700,160 | H2 56/68 `matcha-600` · 2 บรรทัดสูงสุด |
| 6 | Sub | ★Sub 1 บรรทัด | 🎨 | 60,1016,960,40 | Feature 28 `clay` |
| 7 | Info row | 🕗 ★[เวลา] · 🚗 ★[ที่จอด] · 🚶 ★[x] นาทีจาก ★[จุดสังเกต] | 🎨 B4 | 60,1072,960,40 | Info row · ไอคอน 36 |
| 8 | Offer box | 🎁 ★[Offer] + "โค้ด ★HIBI-BRx" | 🎨 | 60,1144,500,146 | radius 20 · `gold` · Offer Kanit SemiBold 34 `clay` · โค้ด Inter Bold 24 `clay` |
| 9 | CTA | "ดูเส้นทาง →" | 🎨 A4 | 600,1172,420,88 | CTA spec |
| 10 | Fine print | "*เฉพาะสาขา ★[ชื่อ] ถึง ★[วันที่] · 1 สิทธิ์/บิล" | 🎨 | 60,1302,960,24 | Fine print 20 |

**ค่าที่เปลี่ยนต่อสาขา (★)**
| ★ | BR1 Flagship | BR2 ห้าง | BR3 ออฟฟิศ | BR4 มหาลัย | BR5 ท่องเที่ยว |
|---|---|---|---|---|---|
| ชื่อ | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Headline | "มัทฉะแบบพิธีชา ใจกลาง [ย่าน]" | "เดินห้างเหนื่อย? พักขากับ Capy" | "มัทฉะเช้า ไม่ต้องต่อคิว" | "มุมอ่านหนังสือ + มัทฉะดี ๆ" | "Matcha & Capy photo spot" |
| Sub | Matcha Bar + Workshop ทุกเดือน | ชั้น [x] [ชื่อห้าง] | Pre-order LINE ก่อน 8:30 | ปลั๊กทุกโต๊ะ · Wi-Fi แรง | เมนู Limited เฉพาะสาขา (TH/EN) |
| ภาพ (P6) | Bar + Usucha | โซนครอบครัว + Float | เคาน์เตอร์ Pick-up | โต๊ะปลั๊ก + หนังสือ | Photo spot หน้าร้าน |
| Capy | Sensei | Family | Salaryman | Student | Traveler |
| Offer | [ลด Workshop x%] | [Kids cup ฟรี] | [ลด x บาท 7–9 โมง] | [ลด x% บัตรนศ.] | [ฟรี Postcard Capy] |
| ช่วงยิง | ศ.–อา. | ศ.เย็น–อา. | จ.–ศ. 6:30–9:00 | จ.–ศ. 14:00–20:00 | ทุกวัน (เน้นวันหยุด) |
| ภาษา | TH | TH | TH | TH | **TH + EN 2 ไฟล์** |

**9:16 Adaptation:** Brand bar y250 (ใต้ safe zone) สูง 96 · Photo 60,370,960,760 · Capy 780,960 · Headline 60,1170 · Sub 60,1340 · Info 60,1396 · Offer 60,1460,500,110 (ตัด fine print ไปแคปชัน) · CTA 600,1470,420,88

**GBP 4:3 (1200×900):** ใช้ภาพสาขาเต็มเฟรม + ข้อความไม่เกิน Brand bar ล่าง (Google ไม่แนะนำข้อความเยอะบนภาพ)

**Deliverables:** 5 สาขา × (4:5 + 9:16 + GBP) = 15 ไฟล์ (+ BR5 EN อีก 2) · ชื่อ `HIBI_A3_BR[1-5]_[Placement]_v1`

---

### 🟢 A4 · "Matcha 101" — Carousel 6 สไลด์

**Job Info**
| รายการ | รายละเอียด |
|---|---|
| Code | `HIBI_A4` |
| Funnel / Objective | MOFU / Engagement (Save) |
| Audience | Retarget ดู A1/A2 ≥ 50% |
| Key Message | **"มัทฉะแท้ไม่ใช่แค่ชาเขียว — Capy สรุปให้"** |
| Key Takeaway | ① ต่างจากชาเขียวยังไง ② ดูมัทฉะดียังไง ③ Hibi ใช้มัทฉะแบบนั้น |
| Copy | ร่างด้วย T5 → Content lead ตรวจข้อเท็จจริง |
| CTA | สไลด์ 6 "ลองความต่างที่ Hibi →" |

**Slide Template (ใช้ร่วมสไลด์ 2–5) — 1080×1350**
| # | Layer | Source | Position | Style |
|---|---|---|---|---|
| 1 | BG `pearl` + seigaiha 5% | 🎨 | full | — |
| 2 | Counter "0X/06" | 🎨 | 60,60 | Slide counter |
| 3 | Capy icon (หัว Capy เล็ก) | 🔀 B2 | 960,52,60,60 | — |
| 4 | Headline | 🎨 | 60,150,960,200 | H1 76/92 `matcha-600` |
| 5 | Illustration | 🔀 I6 → vector | 120,380,840,640 | สีแบรนด์เท่านั้น · พื้นขาว rounded 32 |
| 6 | Body | 🎨 | 60,1070,960,100 | Body 30/44 · ≤ 2 บรรทัด · คำสำคัญ Bold `matcha-700` |
| 7 | Swipe hint "ปัด →" | 🎨 | 900,1260 | Inter Medium 24 `stone` |

**รายสไลด์**
| # | Headline | Illustration / ภาพ | Body | หมายเหตุ |
|---|---|---|---|---|
| 1 Cover | "มัทฉะ ≠ ชาเขียว ?!" (H1 104 center 2 บรรทัด, y 220) | Capy Surprised 🔀 I2-④ ถือ 2 แก้ว (กราฟิกประกอบแก้วเขียวสด vs เขียวหม่น) กลาง 240,520,600,600 | "Capy สรุปให้ใน 6 สไลด์ 📌" (y 1180 center) | พื้น `cream` ต่างจากสไลด์อื่น |
| 2 | "ปลูกใต้ร่ม 20–30 วัน" | I6-2 ไร่ชาคลุมผ้า + Capy หมวกชาวไร่ | "ใบชาสร้างคลอโรฟิลล์และ **แอล-ธีอะนีน** มากขึ้น → **เขียวสด หวานนุ่ม**" | ไอคอน ☀️→🌑 มุมภาพ |
| 3 | "บดทั้งใบเป็นผง" | I6-3 หินโม่ | "ดื่ม **ทั้งใบ** ไม่ใช่แค่น้ำชา" | — |
| 4 | "ตี ไม่ใช่แช่" | 📷 P3 Top-down + ลูกศร M/W 🎨 | "ตีเป็นรูป **M/W** 15–20 วิ จนฟองละเอียด" | ภาพจริงใน frame วงกลม Ø 640 |
| 5 | "มัทฉะดีดูยังไง" | ตาราง 3 แถว × 2 คอลัมน์ ✅/❌ (I6-5) | — (ข้อความอยู่ในตาราง: สี / ฟอง / กลิ่น) | ✅ `matcha-600` ❌ `stone` (ห้ามแดง) |
| 6 End | "ลองความต่างที่ Hibi 🍵" | 📷 P1 แก้ว Hibi 300,360,480,560 + Capy Happy 760,700,240 | "📍 5 สาขา" + CTA (300,1110,480,88) + "เซฟไว้ก่อนไป 📌" y 1230 | พื้น `cream` |

**Lemon8 3:4 (1080×1440):** ใช้ template เดิม เพิ่ม 90px ส่วนล่างให้ Body · ปกสไลด์ 1 headline ใหญ่ขึ้น 112

**Deliverables:** `HIBI_A4_ALL_Carousel45_S01–S06` · `_Lemon8_S01–S06` · ไฟล์ Illustration vector แยก

---

### 🟢 A5 · "Add LINE รับคูปอง"

**Job Info**
| รายการ | รายละเอียด |
|---|---|
| Code | `HIBI_A5` |
| Funnel / Objective | BOFU / Messages – LINE add friend |
| Audience | Engage IG/FB 30 วัน + Profile visitors |
| Key Message | **"แอดไลน์ Hibi รับส่วนลด [x] บาททันที"** |
| Key Takeaway | ① แอดแล้วได้คูปองทันที ② ใช้ได้ 5 สาขา ③ สมาชิกได้สิทธิ์ต่อเนื่อง |
| CTA | "แอดเพื่อนเลย" |
| ลำดับสายตา | ① ตัวเลขส่วนลด → ② Headline → ③ Mockup LINE → ④ CTA |

**Layer Spec — Story 9:16 (Master, 1080×1920)**
| # | Layer | Content | Source | Position (x,y,w,h) | Style |
|---|---|---|---|---|---|
| 1 | BG | `cream` + ลายใบชา 6% | 🎨 | full | — |
| 2 | Logo | เขียว | 🎨 | 60,260,180 | — |
| 3 | Headline | "แอดไลน์ Hibi รับส่วนลด" | 🎨 | 60,360,960,200 | H1 84/100 `matcha-600` center |
| 4 | Coupon | "฿[x] OFF" + "ใช้ได้ทุก 5 สาขา" | 🎨 A4 | 160,600,760,300 | Coupon spec · บรรทัดล่าง Feature 28 ขาว |
| 5 | Capy | Point ชี้ลง (หมุน pose ให้ชี้ลงล่าง) | 🔀 I2-⑦ | 780,880,240,280 | ทับขอบคูปองขวาล่างได้ ไม่ทับตัวเลข |
| 6 | Phone mockup | หน้าจอแชต Hibi OA + การ์ดคูปอง | 🎨 (screenshot จริงจาก OA) | 300,960,480,560 | กรอบมือถือ radius 48 · เงา |
| 7 | Benefit row | ✔ คูปองทันที ✔ เมนูลับสมาชิก ✔ สะสมแต้ม | 🎨 | 60,1500,960,40 | Feature 28 `clay` |
| 8 | CTA | "แอดเพื่อนเลย" | 🎨 | 270,1560,540,88 | **ปุ่มสีเขียวแบรนด์ ไม่ใช้สีเขียว LINE** เพื่อไม่ให้ดูเป็นปุ่ม UI ปลอม |
| 9 | Safe zone | ว่าง | — | y 1580+ ใช้ได้เฉพาะ CTA ที่จบก่อน 1648 | — |

**Feed 1:1 Adaptation (1080×1080):** Headline 60,80 (H1 72) · Coupon 160,260,760,280 · Capy 800,440,220 · Mockup ตัดออก → ใช้ไอคอน LINE 60px ข้าง CTA · Benefit 60,640 · CTA 270,880,540,88 · Fine print 60,1000 "*1 สิทธิ์/บัญชี · ถึง [วันที่]"

**LINE Rich message (1040×1040):** Coupon เต็มครึ่งบน · Capy Happy · ปุ่ม tap-area ครึ่งล่าง (ทั้งภาพกดได้)

**Deliverables:** `HIBI_A5_ALL_Story916_v1` · `_Feed11_v1` · `_LINERich1040_v1`

---

### 🟢 A6 · "Hibi Member — Stamp Card"

**Job Info**
| รายการ | รายละเอียด |
|---|---|
| Code | `HIBI_A6` |
| Funnel / Objective | Loyalty / Repeat purchase |
| Audience | LINE friends · ลูกค้าเดิม (Custom audience) |
| Key Message | **"ครบ [8] แก้ว Capy เลี้ยง 1 แก้ว"** |
| Key Takeaway | ① สะสมผ่าน LINE ทุกสาขา ② ครบได้แก้วฟรี ③ สมาชิกได้เมนูลับ/สิทธิ์ก่อนใคร |
| CTA | "เริ่มสะสมเลย" |

**Layer Spec — Feed 1:1 (1080×1080)**
| # | Layer | Content | Source | Position (x,y,w,h) | Style |
|---|---|---|---|---|---|
| 1 | BG | `matcha-600` เต็ม + seigaiha ขาว 6% | 🎨 | full | — |
| 2 | Label | "Hibi Member 💚" | 🎨 | 60,60 | EN Label 34 ขาว |
| 3 | Headline | "ครบ 8 แก้ว Capy เลี้ยง 1 แก้ว!" | 🎨 | 60,120,960,180 | H1 72/88 ขาว · 2 บรรทัด |
| 4 | Card | การ์ดสะสมแต้ม | 🎨 | 120,330,840,440 | `cream` radius 32 · เงา |
| 5 | Stamps | 4×2 วงกลม Ø 150 · ช่อง 1–7 = หน้า Capy (เส้น `clay` 40% = ยังไม่ได้), ตัวอย่างประทับแล้ว 3 ช่อง (สีเต็ม) · ช่อง 8 = แก้วมัทฉะ `gold` + "FREE" | 🎨 + 🔀 Capy head | ภายในการ์ด grid เริ่ม 170,380 ระยะห่าง 30 | — |
| 6 | Benefit | ✔ สะสมผ่าน LINE ✔ ใช้ได้ 5 สาขา | 🎨 | 60,810,700,40 | Feature 28 ขาว |
| 7 | Capy | Happy | 🔀 I2-② | 800,740,240,280 | — |
| 8 | CTA | "เริ่มสะสมเลย" | 🎨 | 60,900,440,88 | ปุ่มกลับสี: พื้น `cream` ตัวหนังสือ `matcha-700` |
| 9 | Fine print | "*เงื่อนไขตามที่ร้านกำหนด · [ระยะเวลา]" | 🎨 | 60,1010 | Fine print 20 ขาว 70% |

**Adaptations:** LINE Rich message 1040×1040 (layout เดียวกัน) · Rich menu 2500×1686 ช่อง "สะสมแต้ม" ใช้การ์ดย่อ · โปสเตอร์ A3 หน้าร้าน (297×420mm, 300dpi, CMYK, bleed 3mm) + QR code LINE ขนาด ≥ 40mm มุมขวาล่าง

**Deliverables:** `HIBI_A6_ALL_Feed11_v1` · `_LINERich1040` · `_RichMenuTile` · `_PosterA3_print.pdf`

---

### 🟡 Seasonal Overlay (ใช้ Layer spec ของ A2/A3 เดิม — เปลี่ยนเฉพาะ)
| เทศกาล | เปลี่ยน Layer | Source | Accent |
|---|---|---|---|
| ลอยกระทง | BG → ฉากแม่น้ำกลางคืน bokeh · Capy → บนกระทง | 🔀 I7 | `gold` แสงเทียน; ตัวหนังสือบนพื้นเข้มใช้ `cream` |
| Christmas | Capy → หมวกซานต้า + กล่อง Gift · เพิ่มไฟประดับ | 🔀 I7 | `copper` ≤ 5% |
| ปีใหม่ | Capy → ฮาโอริโค้ง · Kadomatsu มุมซ้าย | 🔀 I7 | `gold` |

---

## PART D — Handoff Package (สิ่งที่ Content lead ต้องส่งให้กราฟิกทุกงาน)

| # | รายการ | ตัวอย่าง |
|---|---|---|
| 1 | Brief code + Placement | `HIBI_A3_BR3` · 4:5 + 9:16 + GBP |
| 2 | Copy ที่อนุมัติแล้ว (ไฟล์ข้อความ ไม่ใช่รูป) | Headline / Sub / Offer / CTA / Fine print |
| 3 | ข้อมูลจริงที่ยืนยันแล้ว | ราคา · วันที่ · โค้ด · ชื่อสาขา · เวลาเปิด |
| 4 | ภาพ AI ที่ผ่านการเลือกแล้ว (+ prompt ที่ใช้) | `I1_v3.png` + prompt text |
| 5 | ภาพถ่ายจริงจากสาขา | P1–P7 ตาม Shoot list |
| 6 | Deadline + ผู้อนุมัติ | ส่งร่าง พ. 17:00 · อนุมัติ พฤ. |

## PART E — QC Checklist (กราฟิกตรวจก่อนส่ง)

**ข้อมูล**
- [ ] ราคา / วันที่ / โค้ด / ชื่อสาขา ตรงกับ Handoff #3 ทุกตัวอักษร
- [ ] ภาษาไทยไม่มีสระลอย วรรณยุกต์ทับ คำตัดผิดบรรทัด (อ่านออกเสียงทวน)

**ภาพ**
- [ ] สินค้า Hero เป็นภาพจริง สี/ฟอง/ขนาดไม่ถูก AI เปลี่ยน (เทียบกับต้นฉบับ)
- [ ] Capy ตรง Model sheet (สัดส่วน สี ถ้วยบนหัว 1 ใบ) และมองไปที่สินค้า/CTA
- [ ] ภาพ AI ไม่มีตัวอักษรมั่ว นิ้ว/อุ้งเท้าเพี้ยน โลโก้แบรนด์อื่น
- [ ] สีอยู่ใน Color tokens · เขียวไม่นีออน · ≤ 3 สีหลัก

**Layout**
- [ ] ทุกข้อความอยู่ใน live area · 9:16 ไม่ทับ safe zone
- [ ] ลำดับสายตาตรงกับ brief (ทดสอบ: ปิดตา 1 วิ เปิดดู — เห็นอะไรก่อน)
- [ ] ตัวหนังสือเล็กสุด ≥ 20px · คอนทราสต์ ≥ 4.5:1
- [ ] ดูบนมือถือจริงขนาด 100% แล้วอ่าน Headline ได้ใน 2 วินาที

**วิดีโอ**
- [ ] Hook ใน 0–2s · โลโก้/Capy ภายใน 3s · End card 1.5s+
- [ ] ซับครบทุกประโยค · เสียง −14 LUFS · เพลงมีสิทธิ์เชิงพาณิชย์

**ไฟล์**
- [ ] ชื่อไฟล์ `HIBI_[Code]_[Branch]_[Placement]_[v]_[YYMMDD]`
- [ ] PNG/JPG ≤ 5MB · MP4 H.264 ≤ 30MB · แนบไฟล์ต้นฉบับ
- [ ] ติดป้าย AI-generated ในระบบแอดเมื่อมีภาพ/วิดีโอ AI ที่ดูสมจริง
