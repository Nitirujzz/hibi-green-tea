# 05 · Buffer publishing

## บัญชี
- Organization: **My Organization** `6a6a0f5be23ae9c056a5995a` · Timezone **Asia/Bangkok (+07:00)**
| ช่องทาง | Channel ID |
|---|---|
| Instagram | `6aca72736a5c39ccb67408e5` |
| Facebook | `6accb410778b240e2fe516ac` |
| TikTok | `6aca77bc6a5c39ccb6743911` |

| แท็ก | ID | ใช้เมื่อ |
|---|---|---|
| 🤖 AI Generate | `6accbff711bee99e6c9a0d48` | มีภาพ/วิดีโอจาก AI |
| 📷 ถ่ายจริงในร้าน | `6accbff732da9d8379ea82a9` | มี footage/รูปจริง |
| ให้น้อง Year ทำเด้อ | `6ad73a3c9bd5357216a3872d` | งานที่น้อง Year รับผิดชอบ (ทีมร้านใช้) |

## กฎแต่ละแพลตฟอร์ม
- **Instagram**: `metadata.instagram.type` = `reel` (+ `shouldShareToFeed: true`) หรือ `post` · `isAiGenerated: true` ถ้ามี AI · `firstComment` = คำถามชวนตอบ
- **Facebook**: `metadata.facebook.type` = `reel` / `post` · ไม่มีช่อง AI label
- **TikTok**: `schedulingType: notification` (กดโพสต์เองในแอป → ใส่เพลงได้) · photo mode **ไม่เกิน 10 ภาพ** · `isAiGenerated` ใช้ได้กับวิดีโอ
- Video thumbnail: `metadata.thumbnailOffset` (ms) เลือกเฟรมที่ข้อความ hook ขึ้นครบ
- `dueAt` ต้องมี offset `+07:00` และต้องอยู่ในอนาคต

## การส่งไฟล์ให้ Buffer
- ใช้ลิงก์ **raw.githubusercontent.com ที่ล็อก commit sha** (`.../hibi-green-tea/<sha>/docs/...`) — Buffer รับทั้งรูปและวิดีโอ mp4 (ทดสอบแล้ว 50 MB ผ่าน)
- ⚠️ **ต้องเปิด repo เป็น public** จนกว่าโพสต์ที่ใช้ลิงก์นั้นจะขึ้นครบ
- ❌ `upload.higgsfield.ai` ถูกบล็อกในเครือข่ายนี้ → อัปโหลดไฟล์ผ่าน Higgsfield ไม่ได้
- ❌ jsDelivr จำกัด 20 MB/ไฟล์ → ใช้กับวิดีโอใหญ่ไม่ได้

## ประวัติการตั้งเวลา (ที่ทำในงานนี้)
| วันที่ | เวลา | คอนเทนต์ | ช่องทาง |
|---|---|---|---|
| 17 ต.ค. | 10:30 / 19:30 | MBTI carousel (TikTok 10 ภาพ) | IG + FB / TikTok (แจ้งเตือน) |
| 25 ต.ค. | 19:30 | Coconut Cloud reel (เวอร์ชัน A) | IG + FB + TikTok (แจ้งเตือน) |
| 27 ต.ค. | 10:30 | Hojicha 101 carousel | IG + FB |
| 29 ต.ค. | 10:30 | Halloween “แต่งแบบ Hibi หรือ Capy” | IG + FB |
| 30 ต.ค. | 19:30 | 5 ความผิดพลาดที่ทำให้มัทฉะขม (VO reel 1:24) | IG + FB + TikTok (แจ้งเตือน) |
| 1 พ.ย. | 19:30 | มัทฉะตีมือ 4 ขั้น (reel 21 วิ) | IG + FB + TikTok (แจ้งเตือน) |
| 11 พ.ย. | 19:30 | Capy หัดตีมัทฉะ (Hibi & Capy reel 32 วิ) | IG + FB + TikTok (แจ้งเตือน) |
| 18 พ.ย. | 19:30 | หนาวนี้ Capy แช่ออนเซ็น (Hibi & Capy reel 33 วิ) | IG + FB + TikTok (แจ้งเตือน) |
| 12 พ.ย. | 12:00 / TikTok 18:00 | K01 (Done batch) | IG + FB / TikTok (แจ้งเตือน) |
| 14 พ.ย. | 15:00 / TikTok 19:00 | G14 (Done batch) | IG + FB / TikTok (แจ้งเตือน) |
| 16 พ.ย. | 12:00 / TikTok 18:00 | G13 (Done batch) | IG + FB / TikTok (แจ้งเตือน) |
| 17 พ.ย. | 12:00 / TikTok 17:00 | SQ01 (Done batch) | IG + FB / TikTok (แจ้งเตือน) |
| 20 พ.ย. | 12:00 / TikTok 18:00 | SQ02 (Done batch) | IG + FB / TikTok (แจ้งเตือน) |
| 21 พ.ย. | 15:00 / TikTok 19:00 | SQ03 (Done batch) | IG + FB / TikTok (แจ้งเตือน) |
| 23 พ.ย. | 12:00 / TikTok 18:00 | G12 (Done batch) | IG + FB / TikTok (แจ้งเตือน) |
| 26 พ.ย. | 12:00 / TikTok 18:00 | K09 (Done batch) | IG + FB / TikTok (แจ้งเตือน) |
| 29 พ.ย. | 15:00 / TikTok 19:00 | SQ05 (Done batch) | IG + FB / TikTok (แจ้งเตือน) |
- Done batch พ.ย.: รายละเอียด/Post IDs/งานที่ Hold → `../campaigns/done-batch-nov26/README.md` · TikTok รูปต้อง ≤ 2,073,600 px → ย่อเป็น 1080×1920 (พื้นหลังเบลอ)
- ทีมร้านตั้งเองด้วย (ดูใน Buffer): มัทฉะ vs ชาเขียว 28 ต.ค. · Nutty 30 ต.ค. 11:00 · Yame Saeakari 1 พ.ย. 11:00 · Hojicha Kokoro 2 พ.ย.
- ปฏิทินเดือน ต.ค. ฉบับเต็ม: `../calendar/2026-10-content-calendar.md`

## Ideas board (คอลัมน์งาน)
- คอลัมน์: Year ทำเด้อ `6ad1f4c6e806306083b75ba6` · **AI ทำเด้อ** `6ad72bba1c5e4ed095f1a9ca` · Post `6ad1f4da0f04519838670afa` · วางแผนโพสต์แล้ว `6aec010cca652320a86031d8` · Done `6a8c76f6e81a012e68e8975f`
- `create_idea` **เลือกคอลัมน์ไม่ได้** (Idea ใหม่ไม่มี group) → แจ้งเจ้าของให้ลากเข้าคอลัมน์เอง · แนบได้แค่รูป/เอกสาร (วิดีโอใส่เป็นลิงก์ใน text)
- แท็กที่ใช้: 🤖 AI Generate `6accbff711bee99e6c9a0d48` · ความรู้เรื่องชา `6ad79a175d596c451c9a9730` · Draft รอ Owner `6ad79a0e58d9946a79b849fa` · Hibi–Capy `6ad79a5a86ab4b10200c75c8`
- รูปแบบ Idea ของทีม: ชื่อ “รหัส | สถานะ | ผู้รับผิดชอบ | หัวข้อ” · เนื้อหา: สถานะ → ช่องทาง → ไฟล์ → สคริปต์/ข้อความบนภาพ → Caption Draft → ข้อควรระวัง → ไฟล์ต้นทาง
