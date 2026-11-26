# Hibi Matcha Cafe — แบ่งงาน AI vs ทีมกราฟิก + AI Prompt Library

> อ่านคู่กับ [01 Strategy](./01-content-strategy.md) · [02 Caption](./02-platform-captions.md) · [03 Ads Brief (ภาพรวม)](./03-ads-brief.md) · [05 Ads Brief ละเอียดรายองค์ประกอบ](./05-detailed-ads-brief.md)
> ช่อง `[ ]` = ข้อมูลจริงที่ต้องเติม

---

## PART 1 — หลักการแบ่งงาน

### 1.1 กฎ 6 ข้อ (ตัดสินว่าใครทำ)

| # | กฎ | เหตุผล |
|---|---|---|
| R1 | **ตัวหนังสือภาษาไทยบนภาพ = ทีมกราฟิกเสมอ** | โมเดลสร้างภาพยังสะกดไทยผิด/สระลอย/วรรณยุกต์เพี้ยน |
| R2 | **ภาพเครื่องดื่ม/ขนมที่เป็น Hero ในแอด = ถ่ายจริง** (AI ใช้ได้แค่ปรับแสง/ต่อพื้นหลัง/ลบฝุ่น) | ห้ามโฆษณาให้สินค้าดูต่างจากของจริง — เสี่ยงร้องเรียนและเสียความเชื่อใจ |
| R3 | **Hibi-Capy Master Character (Model sheet) = ทีมกราฟิกออกแบบ** แล้ว AI ใช้เป็น reference สร้าง pose เพิ่ม | ให้แบรนด์เป็นเจ้าของลิขสิทธิ์ตัวละครชัดเจน + หน้าตาคงที่ทุกงาน |
| R4 | **ราคา โปร เงื่อนไข ชื่อสาขา เวลาเปิด = กราฟิกพิมพ์จากข้อมูลที่อนุมัติแล้ว** | ข้อมูลผิด = ความเสียหายตรง |
| R5 | **AI ทำ "ร่างแรก + ปริมาณ + ตัวแปร"** (ไอเดีย, แคปชัน, พื้นหลัง, B-roll, เวอร์ชัน A/B) | ประหยัดเวลาทีมไปทำงานที่ต้องใช้วิจารณญาณ |
| R6 | **ทุกชิ้นที่ AI ทำ ต้องผ่านคนตรวจก่อนโพสต์** (Content lead ตรวจคำ, กราฟิกตรวจภาพ) และติดป้าย "AI-generated" เมื่อแพลตฟอร์มกำหนด (ภาพ/วิดีโอสมจริง) | ความถูกต้อง + ตามนโยบาย Meta/TikTok |

### 1.2 Production Matrix — ใครทำอะไร

สัญลักษณ์: 🤖 = AI ทำ (คนตรวจ) · 🎨 = ทีมกราฟิกทำ · 📷 = ถ่ายจริง (สาขา/ช่างภาพ) · ✍️ = Content lead · 🔀 = AI ทำฐาน → กราฟิกประกอบจบ

| ชิ้นงาน | ผู้ทำ | เครื่องมือแนะนำ | Prompt / Brief ที่ใช้ |
|---|---|---|---|
| ไอเดียคอนเทนต์รายเดือน, Content calendar ร่าง | 🤖 → ✍️ | Claude / ChatGPT | T1, T2 |
| Hook 10 แบบ / หัวข้อโพสต์ | 🤖 → ✍️ | Claude / ChatGPT | T3 |
| แคปชันทุกแพลตฟอร์ม (ร่าง) | 🤖 → ✍️ | Claude / ChatGPT | T4 |
| บทความ Lemon8 / เนื้อหา Carousel ความรู้ | 🤖 → ✍️ ตรวจข้อเท็จจริง | Claude / ChatGPT | T5 |
| ตอบคอมเมนต์ / รีวิว Google (ร่าง) | 🤖 → แอดมิน | Claude / ChatGPT | T6 |
| แปล EN / JP สำหรับสาขาท่องเที่ยว | 🤖 → ✍️ | Claude / ChatGPT | T7 |
| Ad copy A/B variants | 🤖 → ✍️ | Claude / ChatGPT | T8 |
| สคริปต์วิดีโอ + Shot list ร่าง | 🤖 → ✍️ | Claude / ChatGPT | T9 |
| **Hibi-Capy Master Model Sheet** | 🎨 | Illustrator / Procreate | 05 §B1 |
| Capy pose / expression เพิ่มเติม (หลังมี master) | 🔀 | Nano Banana / Midjourney `--cref` / Flux + LoRA | I2 |
| Capy ชุดประจำสาขา 5 ชุด | 🔀 (AI ร่าง → กราฟิก redraw ให้ตรง master) | เหมือนข้างบน | I3 |
| ภาพพื้นหลัง / ฉาก / Mood (ไม่มีสินค้า) | 🤖 | Midjourney / Flux / Nano Banana | I1, I4 |
| ภาพสินค้า Hero (เครื่องดื่ม/ขนม) | 📷 → 🎨 retouch | กล้อง/มือถือ + Photoshop | 05 §B3 |
| ต่อพื้นหลัง/ขยายภาพสินค้าจริง (Outpaint) | 🔀 | Photoshop Generative Fill / Nano Banana edit | I5 |
| Illustration ประกอบ Infographic (ไร่ชา, หินโม่) | 🤖 → 🎨 vectorize/ปรับสี | Midjourney / Ideogram | I6 |
| ภาพเทศกาล (ฉาก+Capy) | 🔀 | Midjourney + Capy ref | I7 |
| **Layout + Typography + ข้อความไทย + ราคา + CTA** | 🎨 | Figma / Photoshop / Canva Pro | 05 ทั้งหมด |
| Master template (Branch, Menu, Carousel, Story) | 🎨 | Figma / Canva Brand Kit | 05 §C |
| Resize ทุกขนาด (หลังมี master) | 🔀 | Canva Magic Resize / Figma + ตรวจ safe zone | — |
| B-roll วิดีโอ (ไร่ชา, ไอน้ำ, ฉากญี่ปุ่น) | 🤖 | Veo 3 / Kling / Runway | V1–V3 |
| วิดีโอ Capy Animation สั้น | 🔀 (AI animate จากภาพ Capy master) | Kling / Runway image-to-video | V4 |
| ฟุตเทจตีมัทฉะ / เทนม / หน้าร้าน (ของจริง) | 📷 | มือถือ 4K 60fps | 05 §B3 |
| ตัดต่อ + ซับไทย + End card | 🎨 | CapCut / Premiere | 05 |
| Voice-over (เสียง Capy / ผู้บรรยาย) | 🤖 → ✍️ ฟังตรวจ | ElevenLabs | A1 |
| เพลงประกอบ / SFX | 🤖 (ใช้แผนแบบเสียเงินที่ให้สิทธิ์เชิงพาณิชย์) | ElevenLabs Music/SFX หรือคลังเพลงลิขสิทธิ์ | A2 |
| QC สุดท้าย + Export + ตั้งชื่อไฟล์ | 🎨 | — | 05 §E |

### 1.3 สัดส่วนงานโดยประมาณ (ต่อเดือน ~80 ชิ้น)

| ประเภท | จำนวน/เดือน | 🤖 AI | 🔀 Hybrid | 🎨/📷 Human |
|---|---|---|---|---|
| แคปชัน + ข้อความ | 80 | 80% ร่าง | — | 20% (แก้/อนุมัติ) |
| ภาพนิ่ง Organic (Feed/Story) | 40 | 30% (ฉาก, มีม Capy, ความรู้) | 45% | 25% (เมนู/สาขา) |
| วิดีโอสั้น | 25 | 15% (B-roll ล้วน) | 35% | 50% (ฟุตเทจจริง) |
| Ads creative | 15 | 0% ปล่อยตรง | 40% | 60% |

> สรุป: **AI ช่วยลดเวลา ~40–50%** แต่ทุก Ads และทุกภาพที่มีราคา/ข้อความไทย จบที่ทีมกราฟิก

### 1.4 Workflow รายชิ้น (Hybrid)

```
✍️ Content lead เลือก Brief (05) ──► 🤖 ร่างแคปชัน+ข้อความบนภาพ (T4/T8)
                                   ──► 🤖 สร้างฉาก/Capy/B-roll (I*, V*)  ×4 ตัวเลือก
                                   ──► 📷 สาขาส่งภาพสินค้าจริง
🎨 กราฟิก: เลือกภาพ AI ที่ดีที่สุด → retouch/vectorize → ประกอบใน Master template
        → พิมพ์ข้อความไทย/ราคา/CTA → Export ทุกขนาด
✍️ ตรวจ Checklist (05 §E) ──► อนุมัติ ──► ตั้งโพสต์/แอด
```

---

## PART 2 — Style DNA (บล็อกที่ต้องแปะในทุก Image Prompt)

> Prompt ภาพเขียนเป็น **ภาษาอังกฤษ** (โมเดลเข้าใจดีกว่า) — คำอธิบายภาษาไทยอยู่ด้านบนแต่ละ prompt
> ใช้ `[STYLE]` และ `[NEG]` แทนบล็อกด้านล่างเวลาคัดลอก

**[STYLE] — Hibi Visual DNA**
```
soft natural window light, warm and calm Japanese café mood, matcha green (#16a34a) and tea cream (#fef7cd) color palette with clay brown (#92400e) accents, clean minimal composition with generous negative space, light wood, linen and handmade ceramic textures, gentle shadows, cozy, peaceful, slightly film-like warmth, high detail, editorial food photography quality
```

**[CAPY] — Hibi-Capy Character Description** (ใช้คู่กับภาพ reference ของ Model sheet ทุกครั้ง)
```
Hibi-Capy: a round, chubby, cute capybara mascot, light caramel-brown fur, small sleepy half-closed eyes, big soft nose, tiny ears, short stubby legs, calm content smile, a small ceramic matcha cup resting on top of its head, simple clean 2D illustration style with soft cel shading, thin clay-brown outlines, kawaii but understated, no text
```

**[NEG] — Negative prompt / สิ่งที่ห้ามมี**
```
text, letters, watermark, logo, signature, neon green, oversaturated, harsh flash, plastic look, cluttered background, extra limbs, deformed paws, multiple cup on head, aggressive expression, beaver, rat, hamster, other brand cups, coffee beans, dark moody lighting
```

**พารามิเตอร์แนะนำ**
| เครื่องมือ | พารามิเตอร์ |
|---|---|
| Midjourney v7 | `--ar 4:5` (Feed) / `--ar 9:16` (Story) / `--ar 1:1` · `--style raw` สำหรับภาพถ่าย · `--cref [URL Capy master] --cw 80` สำหรับ Capy · `--no` + [NEG] |
| Nano Banana (Gemini Image) | อัปภาพ Capy master + ภาพสินค้าจริงเป็น reference แล้วสั่งแบบประโยค "Keep the character exactly as in image 1…" |
| Flux | เทรน LoRA จาก Capy master 15–25 ภาพ → trigger word `hibicapy` |
| Ideogram | ใช้เฉพาะเมื่อต้องการตัวอักษร **ภาษาอังกฤษ** ในภาพ (เช่น ป้าย "Hibi") |

---

## PART 3 — Image Prompts

### I1 · ฉากพื้นหลังสำหรับโพสต์เมนู (ไม่มีสินค้า — เว้นที่ให้กราฟิกวางแก้วจริง)
ใช้กับ: A2 Menu Hero, โพสต์ #HibiMenu
```
Empty light-oak café table surface by a large window, morning sunlight casting soft leaf shadows, a folded linen napkin and a bamboo matcha whisk (chasen) placed at the far left, blurred Japanese café interior background with plants, empty space in the center for product placement, eye-level camera, 50mm lens, shallow depth of field, [STYLE] --ar 4:5 --style raw --no [NEG]
```

### I2 · Hibi-Capy Expression Set (7 ท่า — ต้องแนบ Capy master)
ใช้กับ: ทุกงาน — สร้างครั้งเดียวเก็บเป็นไลบรารี (ทำพื้นหลังโปร่งใสต่อด้วย Remove BG)

| Expression | Prompt (ต่อท้าย [CAPY]) |
|---|---|
| ① Chill | `[CAPY], sitting relaxed, eyes half closed, gentle smile, full body, front view, plain white background` |
| ② Happy | `[CAPY], eyes closed in happy upward curves, pink blush cheeks, tiny sparkles around, full body, plain white background` |
| ③ Sleepy / Tired | `[CAPY], slumped and droopy, heavy eyelids, small sweat drop, holding a stack of papers, full body, plain white background` |
| ④ Surprised | `[CAPY], eyes wide open round, small "o" mouth, ears perked up, tiny exclamation lines, full body, plain white background` |
| ⑤ Sip | `[CAPY], holding a matcha latte glass with both front paws, sipping through a straw, content face, three-quarter view, plain white background` |
| ⑥ Onsen | `[CAPY], bathing up to its chest inside a giant ceramic cup of frothy green matcha, steam rising, blissful closed eyes, small towel on head instead of cup, plain white background` |
| ⑦ Point | `[CAPY], standing on hind legs, pointing to the right with one front paw, friendly confident smile, full body, side three-quarter view, plain white background` |

> 🎨 กราฟิก: เลือกภาพที่ตรง master ที่สุด → แก้สัดส่วน/เส้นให้ตรง Model sheet → บันทึกเป็น PNG โปร่งใส 3000px ชื่อ `CAPY_EXP_01_Chill.png` …

### I3 · Capy ประจำ 5 สาขา (ต่อท้าย [CAPY])
| สาขา | Prompt |
|---|---|
| BR1 Sensei | `[CAPY], wearing a dark green haori jacket, holding a bamboo chasen whisk, dignified calm pose, plain white background` |
| BR2 Family | `[CAPY], with a smaller baby Hibi-Capy riding on its back, both smiling, baby holding a mini soft-serve cone, plain white background` |
| BR3 Salaryman | `[CAPY], wearing a small navy necktie and holding an iced matcha latte to-go cup, walking briskly but calm, plain white background` |
| BR4 Student | `[CAPY], wearing round glasses and a small backpack, sitting with an open book and a matcha latte, plain white background` |
| BR5 Traveler | `[CAPY], wearing a straw bucket hat and a vintage camera strap around its neck, a tiny yuzu next to the matcha cup on its head, waving, plain white background` |

### I4 · ฉากบรรยากาศ 5 สาขา (Mood / พื้นหลัง Story — ไม่ใช่ภาพแทนสาขาจริงในแอด)
> ⚠️ แอด A3 ต้องใช้ **ภาพถ่ายสาขาจริง** — prompt นี้ใช้ทำ Mood board / พื้นหลัง Quiz "สาขาไหนเป็นคุณ"

| สาขา | Prompt |
|---|---|
| BR1 | `Minimalist Japanese matcha bar counter, ceramic chawan bowls lined up, a barista's hands whisking matcha, warm pendant lights, wabi-sabi interior, [STYLE] --ar 9:16` |
| BR2 | `Bright cheerful café corner inside a modern shopping mall, family-friendly seating, soft-serve matcha cones on a tray, warm daylight, [STYLE] --ar 9:16` |
| BR3 | `Early morning grab-and-go café counter in a business district, iced matcha lattes lined up for pickup, city glass towers outside the window, crisp morning light, [STYLE] --ar 9:16` |
| BR4 | `Quiet study café table with laptop, notebook, highlighters and a matcha latte, power outlet visible, afternoon sunlight, students blurred in background, [STYLE] --ar 9:16` |
| BR5 | `Charming street-side Japanese-style café facade with wooden sliding door, noren curtain, potted plants, a photo-spot bench, golden hour light, [STYLE] --ar 9:16` |

### I5 · ขยาย/ต่อพื้นหลังภาพสินค้าจริง (Edit ไม่ใช่ Generate)
ใช้กับ: เปลี่ยนภาพแนวตั้ง 4:5 → 9:16, เติมพื้นที่ว่างให้วางข้อความ
```
(แนบภาพถ่ายสินค้าจริง)
Extend this photo to a 9:16 vertical frame. Keep the drink, glass, foam, colors and lighting EXACTLY unchanged — do not redraw, restyle or beautify the product. Continue the same wooden table and blurred café background naturally upward and downward, leaving clean empty space at the top third for text.
```
> 🎨 ตรวจ: ซูม 100% ว่าแก้ว/ฟอง/สีเครื่องดื่ม **ไม่ถูกเปลี่ยน** — ถ้าเปลี่ยน ให้ mask สินค้าจริงทับกลับ

### I6 · Illustration สำหรับ Carousel "Matcha 101" (A4)
| สไลด์ | Prompt |
|---|---|
| 2 ปลูกใต้ร่ม | `Flat vector illustration of Japanese tea field rows covered with black shade cloth, gentle hills of Uji in background, Hibi-Capy wearing a farmer's straw hat standing beside, simple shapes, matcha green and cream palette, clay brown outlines, white background, no text` |
| 3 บดทั้งใบ | `Flat vector illustration of a traditional granite stone mill grinding tea leaves into bright green powder, small pile of vivid matcha powder, clean minimal, matcha green and cream palette, white background, no text` |
| 4 ตีไม่ใช่แช่ | `Flat vector illustration top view of a ceramic bowl with frothy matcha and a bamboo whisk, motion arrows in a zigzag M shape, minimal, matcha green and cream palette, white background, no text` |
| 5 มัทฉะดีดูยังไง | `Three side-by-side flat icons: vivid green powder vs dull yellow-green powder, fine micro-foam vs large bubbles, a nose with soft sweet aroma lines, consistent icon style, matcha green and clay brown, white background, no text` |

> 🎨 กราฟิก: นำเข้า Illustrator → Image Trace/วาดทับ → ปรับเป็นสีแบรนด์เป๊ะ → ใส่หัวข้อ/คำอธิบายไทยเอง

### I7 · Seasonal (ต่อท้าย [CAPY])
| เทศกาล | Prompt |
|---|---|
| ลอยกระทง | `[CAPY], floating peacefully on a krathong made of banana leaves and lotus petals, holding a tiny matcha cup, candle and incense glowing, calm river at night with soft bokeh lantern lights, warm gold reflections, --ar 4:5` |
| Christmas | `[CAPY], wearing a small red-and-cream santa hat, hugging a wrapped matcha gift box with a green ribbon, cozy café with a small pine tree and warm fairy lights, --ar 4:5` |
| ปีใหม่ | `[CAPY], wearing a festive haori, bowing politely, kadomatsu bamboo decoration and red-white mochi beside, morning sunrise light, --ar 4:5` |

---

## PART 4 — Video Prompts

> ใช้ทำ **B-roll / ฉากประกอบ** เท่านั้น ฟุตเทจเครื่องดื่มจริงต้องถ่ายจริง (R2)
> ความยาวต่อคลิป 5–8 วินาที แล้วไปตัดต่อรวมใน CapCut/Premiere

### V1 · B-roll ไร่ชาญี่ปุ่น (สำหรับ Brand story / A4)
```
Slow cinematic drone shot gliding over lush green Japanese tea fields in Uji at sunrise, rows of tea bushes partially covered with shade cloth, soft morning mist, warm golden light, calm and peaceful, 24fps film look, no people, no text. Vertical 9:16.
```

### V2 · ไอน้ำ / บรรยากาศสงบ (Transition)
```
Extreme close-up of gentle steam rising from a handmade ceramic cup on a light wooden table, soft window backlight, slow motion, shallow depth of field, warm cream and green tones, tranquil mood, no text. Vertical 9:16.
```

### V3 · Hook ออฟฟิศวุ่นวาย (A1 Shot 0–2s — แบบ illustration)
```
2D animation in soft cel-shaded style: Hibi-Capy (round caramel capybara with a tiny matcha cup on its head, sleepy eyes) slumped at a desk piled with papers, laptop notifications popping, little sweat drop, camera slowly pushes in, muted colors, no text. Vertical 9:16, 2 seconds.
```

### V4 · Capy Onsen Animation (image-to-video — แนบ CAPY_EXP_06_Onsen.png)
```
Animate this exact character without changing its design: Hibi-Capy sinks slowly deeper into the giant cup of frothy matcha, steam swirls upward, eyes close blissfully, small happy bubbles rise, gentle loop. Keep colors, outlines and proportions identical to the input image. 4 seconds, seamless loop.
```

### V5 · Capy เดินเข้าร้าน (A1 Shot 2–5s — แนบภาพหน้าร้านจริง + Capy)
```
Composite 2D character animation over the provided real café storefront photo: Hibi-Capy walks slowly from the left toward the café door, small calm steps, door opens with warm light spilling out. Character design must match the reference exactly. Keep the storefront photo unchanged. 3 seconds, vertical 9:16.
```

---

## PART 5 — Audio Prompts

### A1 · Voice-over (ElevenLabs)
| ตัวละคร | ตั้งค่า |
|---|---|
| เสียง Capy | Voice: นุ่ม ช้า อบอุ่น โทนกลาง ไม่แหลม · Stability 55–65 · Style 20 · Speed 0.9 · ภาษาไทย (Multilingual v2/v3) |
| สคริปต์ A1 15s | "วันนี้เหนื่อยไหม… (เว้น) …แวะมาชิลกันหน่อยนะ (เว้น) มัทฉะตีสดทุกแก้ว ที่ Hibi (เว้น) Every day, a little calm." |

> ใช้เฉพาะเสียงสังเคราะห์ที่ไม่เลียนแบบคนจริง — ถ้าโคลนเสียงพนักงาน ต้องมีหนังสือยินยอม

### A2 · Music / SFX
```
Music: Calm lo-fi Japanese café beat, soft koto and warm Rhodes piano, gentle brushed drums, 80 BPM, cozy and peaceful, no vocals, 15 seconds with a soft 1-second ending chime.
SFX: bamboo whisk whisking matcha (ASMR, close mic) / café door bell / soft relieved sigh "haaa" / gentle water bubble pop
```
> ห้ามใช้เพลงฮิต/Trend sound ในแอดที่ยิงเงิน — ใช้ได้เฉพาะ Organic ผ่านคลังเพลงของแพลตฟอร์ม

---

## PART 6 — Text Prompts (LLM: Claude / ChatGPT)

> วิธีใช้: แปะ **[BRAND CONTEXT]** ไว้ใน Project/Custom instructions ครั้งเดียว แล้วใช้ T1–T9 ตามงาน

**[BRAND CONTEXT]**
```
คุณคือ Content writer ของ "Hibi Matcha Cafe" ร้านมัทฉะญี่ปุ่น 5 สาขาในประเทศไทย
- Brand idea: "มัทฉะดี ๆ ที่ดื่มได้ทุกวัน — ชิลแบบคาปิบาร่า" | Tagline: "ชิลทุกวัน กับมัทฉะของ Hibi" / "Every day, a little calm."
- Mascot: Hibi-Capy คาปิบาร่าใจเย็น แทนตัวเองว่า "Capy" เรียกผู้อ่านว่า "เพื่อน ๆ" ลงท้าย "นะ~ / เนอะ / กันน้า" พอประมาณ
- Tone: อบอุ่น ขี้เล่นนิด ๆ รู้จริงแต่ไม่อวดรู้ พูดแบบเพื่อน
- Emoji ที่ใช้: 🍵 🌿 ☁️ ♨️ 🍃 💚 (1–4 ตัว/โพสต์) ห้ามใช้ 🦫 🔥 💯
- สาขา: BR1 [Flagship – Matcha Bar/Workshop], BR2 [ห้าง – ครอบครัว], BR3 [ออฟฟิศ – Grab&Go/Pre-order], BR4 [ใกล้มหาวิทยาลัย – นั่งอ่านหนังสือ], BR5 [ย่านท่องเที่ยว – Photo spot]
- เมนูหลัก: [ใส่รายการเมนู + ราคา]
- Content pillars: Hibi-Capy 25%, Menu 20%, Matcha Knowledge 15%, Branch 15%, Branding 10%, Customer Curiosity/UGC 15%
- Funnel: TOFU 40%, MOFU 30%, BOFU 20%, Loyalty 10%
ข้อห้าม: ห้ามกล่าวอ้างสุขภาพเกินจริง (รักษา ลดน้ำหนัก ล้างพิษ เผาผลาญ), ห้ามแต่งตัวเลข ราคา โปร หรือข้อมูลสาขาที่ไม่ได้ให้ไว้ ถ้าไม่มีข้อมูลให้ใส่ [ ] ไว้ให้เติม
```

### T1 · วางแผนคอนเทนต์รายเดือน
```
วางแผนคอนเทนต์เดือน [เดือน/ปี] สำหรับ Hibi Matcha Cafe จำนวน [20] ชิ้นหลัก
เงื่อนไข:
- ใช้ธีมรายวัน: จันทร์ #CapyMonday, อังคาร #MatchaClass, พุธ #HibiBranch (หมุนสาขา BR[x]), พฤหัส #AskHibi, ศุกร์ #HibiMenu, เสาร์ #HibiMoments, อาทิตย์ #SlowSunday
- เทศกาล/โอกาสในเดือนนี้: [ระบุ]
- เมนู/โปรที่ต้องดัน: [ระบุ]
- สัดส่วน pillar และ funnel ตาม BRAND CONTEXT (±5%)
ตอบเป็นตาราง: วันที่ | วัน | Pillar | Funnel | แพลตฟอร์มหลัก | หัวข้อ | Hook บรรทัดแรก | Format | ผู้ผลิต (🤖/🔀/🎨/📷) | CTA
ท้ายตาราง: สรุปสัดส่วน pillar/funnel ที่ได้จริงเป็น %
```

### T2 · แตกไอเดียจากหัวข้อเดียว
```
หัวข้อ: "[เช่น มัทฉะ vs ชาเขียว]"
คิดไอเดีย 10 แบบ แบ่งเป็น TOFU 4 / MOFU 3 / BOFU 2 / Loyalty 1
แต่ละไอเดียบอก: ชื่อ, Format (Reels/Carousel/Story/ภาพเดี่ยว), Capy ใช้ท่าไหน (Chill/Happy/Sleepy/Surprised/Sip/Onsen/Point), แพลตฟอร์มที่เหมาะสุด, ทำไมคนจะหยุดดู (1 ประโยค)
```

### T3 · Hook Generator
```
เขียน Hook 10 แบบสำหรับ [แพลตฟอร์ม] เรื่อง "[หัวข้อ]"
ใช้สูตรอย่างละ 2: POV / คำถาม / ตัวเลข / ความเชื่อผิด ("อย่า…ถ้า…") / ความลับ ("บาริสต้าไม่บอก…")
ข้อกำหนด: ยาวไม่เกิน 12 คำ, อ่านจบใน 2 วินาที, มี keyword "[มัทฉะ/ย่าน]"
ให้คะแนนตัวเอง 1–5 ว่าแบบไหนน่าจะหยุดนิ้วได้ดีสุดพร้อมเหตุผลสั้น ๆ
```

### T4 · Caption ทุกแพลตฟอร์มในครั้งเดียว
```
เขียนแคปชันโพสต์เรื่อง: "[หัวข้อ]" | Pillar: [ ] | Funnel: [ ] | สาขา: [ALL/BRx] | ข้อมูลจริงที่ใช้ได้: [เมนู ราคา โปร วันที่]
เขียนแยก 6 เวอร์ชันตามสูตร:
1) Facebook: Hook → bullet รายละเอียด → ข้อมูลสาขา/เวลา → CTA → 3–5 hashtag (80–200 คำ)
2) Instagram: Hook 1 บรรทัด → 2–4 บรรทัดคุณค่า → CTA Save/Share → 📍สาขา → 5–8 hashtag
3) TikTok: ข้อความบนจอ (≤10 คำ) + แคปชัน 1–2 บรรทัด + 3–5 hashtag
4) LINE OA: 2–4 บรรทัด ประโยชน์ทันที + ข้อความปุ่ม 1 ปุ่ม
5) Lemon8: หัวข้อแบบ SEO + สรุป 1 บรรทัด + หัวข้อย่อย + ข้อมูลร้าน (150–300 คำ)
6) Google Business Profile: 50–100 คำ มี keyword ย่าน
Hashtag บังคับ: #HibiMatchaCafe #HibiCapy
สุดท้าย: list ข้อมูลที่ต้องยืนยันก่อนโพสต์ (ราคา/วันที่/เงื่อนไข)
```

### T5 · Carousel / บทความความรู้
```
เขียนเนื้อหา Carousel [6] สไลด์ เรื่อง "[หัวข้อความรู้มัทฉะ]" ให้ Capy เป็นผู้เล่า
แต่ละสไลด์: Headline (≤7 คำ) | Body (≤2 บรรทัด, ≤25 คำ) | คำแนะนำภาพประกอบ (สำหรับทีมกราฟิก/AI)
สไลด์ 1 = Hook, สไลด์สุดท้าย = CTA "เซฟไว้" + ชวนมาลองที่ Hibi
ท้ายสุด: ระบุทุกข้อเท็จจริงที่ใช้ + ระดับความมั่นใจ (สูง/กลาง/ต้องตรวจ) เพื่อให้ทีมตรวจก่อนลง
```

### T6 · ตอบคอมเมนต์ / รีวิว
```
ร่างคำตอบ 3 แบบ (สั้น/กลาง/เป็นทางการ) สำหรับข้อความนี้: "[วางคอมเมนต์/รีวิว]" | แพลตฟอร์ม: [ ] | ดาว: [ ] | สาขา: [ ]
- เชิงบวก: ขอบคุณเฉพาะเจาะจง + ชวนกลับมา
- เชิงลบ: ขอโทษจริงใจ ไม่แก้ตัว ไม่โทษลูกค้า ชวนคุยต่อทาง LINE @[id] ห้ามสัญญาชดเชยที่ยังไม่อนุมัติ
- คำถาม: ตอบตรง ถ้าไม่มีข้อมูลให้ใส่ [ ]
ใช้เสียง Capy แบบสุภาพขึ้นเมื่อเป็นรีวิวเชิงลบ
```

### T7 · แปลสำหรับสาขาท่องเที่ยว
```
แปลแคปชันนี้เป็น English และ 日本語 แบบ localize (ไม่แปลตรงตัว) ให้น่ารักแบบ Hibi-Capy เหมาะกับนักท่องเที่ยว
คงชื่อเมนู ราคา hashtag ไว้ และเพิ่ม hashtag ภาษานั้น 3 ตัว: "[วางแคปชัน]"
```

### T8 · Ad Copy Variants (สำหรับทดสอบ A/B)
```
แอด: [A1–A6 ชื่อแอด] | Objective: [ ] | Key Message: "[ ]" | Offer: [ ] | Audience: [ ]
เขียน:
- Primary text 5 แบบ (สั้น ≤125 ตัวอักษร 3 แบบ, ยาว 2 แบบ) แต่ละแบบใช้มุมต่างกัน: อารมณ์ / เหตุผล / ราคา / ความอยากรู้ / Social proof
- Headline บนภาพ 5 แบบ (≤7 คำ, ภาษาไทย)
- Headline ช่องแอด 5 แบบ (≤40 ตัวอักษร)
- CTA บนภาพ 3 แบบ (≤3 คำ)
ระบุคู่ A/B ที่แนะนำให้ทดสอบก่อน + สมมติฐานที่ทดสอบ
```

### T9 · สคริปต์วิดีโอ + Shot List
```
เขียนสคริปต์วิดีโอ [15/30] วินาที แนวตั้ง 9:16 เรื่อง "[ ]" สำหรับ [TikTok/Reels]
ตาราง: เวลา | ภาพ (ระบุ 📷 ถ่ายจริง หรือ 🤖 AI B-roll หรือ 🔀 Capy animation) | ข้อความบนจอ (≤8 คำ) | เสียงพากย์ | SFX/เพลง
กฎ: Hook ใน 0–2s, โลโก้/Capy ภายใน 3s, End card 1.5s, มีซับทุกประโยค
แถม: Shot list สำหรับสาขาถ่าย (มุม, ระยะ, ความเร็ว, แสง) และ prompt วิดีโอภาษาอังกฤษสำหรับช็อตที่เป็น 🤖
```
