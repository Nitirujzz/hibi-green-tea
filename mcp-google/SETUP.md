# Hibi Matcha — Google Workspace MCP Server
## คู่มือติดตั้งแบบ Step-by-Step

---

## ภาพรวม: เลือกวิธีการ Auth

```
ใช้งานบน Remote/Cloud (claude.ai)  ──►  วิธีที่ 1: Service Account  ✅ แนะนำ
ใช้งานบน Local Machine             ──►  วิธีที่ 2: OAuth2 Flow
```

---

## วิธีที่ 1: Service Account (สำหรับ Remote/Cloud) ✅

### Step 1.1 — สร้าง Google Cloud Project

1. เปิด [https://console.cloud.google.com/](https://console.cloud.google.com/)
2. คลิก **Select a project** → **New Project**
3. ตั้งชื่อ: `hibi-matcha-workspace`
4. คลิก **Create**

---

### Step 1.2 — เปิดใช้งาน APIs

1. ไปที่ **APIs & Services** → **Library**
2. ค้นหาและ Enable:
   - ✅ **Google Docs API** → คลิก Enable
   - ✅ **Google Drive API** → คลิก Enable

---

### Step 1.3 — สร้าง Service Account

1. ไปที่ **APIs & Services** → **Credentials**
2. คลิก **+ Create Credentials** → **Service Account**
3. กรอก:
   - Service account name: `hibi-mcp-server`
   - Description: `MCP Server for Hibi Matcha marketing automation`
4. คลิก **Create and Continue** → **Done**

---

### Step 1.4 — ดาวน์โหลด JSON Key

1. คลิกที่ Service Account ที่สร้าง (`hibi-mcp-server@...`)
2. ไปที่ Tab **Keys**
3. คลิก **Add Key** → **Create New Key** → เลือก **JSON** → **Create**
4. ไฟล์ `.json` จะถูกดาวน์โหลดอัตโนมัติ
5. **คัดลอก Service Account Email** จากหน้านี้ (จะใช้ใน Step 1.5)
   - รูปแบบ: `hibi-mcp-server@hibi-matcha-workspace.iam.gserviceaccount.com`

---

### Step 1.5 — แชร์ Google Drive กับ Service Account

> Service Account เข้าถึง Drive ของคุณไม่ได้โดยตรง ต้อง Share Folder ให้ก่อน

1. เปิด [Google Drive](https://drive.google.com/)
2. สร้าง Folder ชื่อ `Hibi Matcha — Marketing Hub` (ถ้ายังไม่มี)
3. คลิกขวาที่ Folder → **Share**
4. ใส่ **Service Account Email** จาก Step 1.4
5. ตั้ง Permission เป็น **Editor**
6. คลิก **Send**

---

### Step 1.6 — ตั้งค่า .env

```bash
# อยู่ใน root ของ project
cp mcp-google/.env.example mcp-google/.env
```

แก้ไข `mcp-google/.env`:

```env
GOOGLE_SERVICE_ACCOUNT_KEY_PATH=./mcp-google/service-account-key.json
```

วาง JSON Key ที่ดาวน์โหลดไว้ที่ `mcp-google/service-account-key.json`

> ⚠️ ไฟล์ `service-account-key.json` อยู่ใน `.gitignore` แล้ว จะไม่ถูก commit

---

### Step 1.7 — ติดตั้งและ Build

```bash
cd mcp-google
npm install
npm run build
```

---

### Step 1.8 — ทดสอบการเชื่อมต่อ

```bash
# ทดสอบว่า auth ทำงานได้
node -e "
import('./dist/auth.js').then(m => {
  process.env.GOOGLE_SERVICE_ACCOUNT_KEY_PATH = './service-account-key.json';
  m.validateAuth().then(() => console.log('✅ เชื่อมต่อสำเร็จ!')).catch(console.error);
});
"
```

---

### Step 1.9 — ลงทะเบียน MCP กับ Claude Code

ไฟล์ `.claude/settings.json` ถูกสร้างไว้แล้ว แต่ต้องชี้ไปยัง env ที่ถูกต้อง:

**ตัวเลือก A: ใช้ Environment Variable ใน Shell**
```bash
export GOOGLE_SERVICE_ACCOUNT_KEY_PATH="/home/user/hibi-green-tea/mcp-google/service-account-key.json"
```

**ตัวเลือก B: แก้ไข `.claude/settings.json` ให้ชี้ไปที่ key path โดยตรง**
```json
{
  "mcpServers": {
    "hibi-google-workspace": {
      "type": "stdio",
      "command": "node",
      "args": ["/home/user/hibi-green-tea/mcp-google/dist/index.js"],
      "env": {
        "GOOGLE_SERVICE_ACCOUNT_KEY_PATH": "/home/user/hibi-green-tea/mcp-google/service-account-key.json"
      }
    }
  }
}
```

---

### Step 1.10 — ทดสอบใน Claude

Restart Claude Code session แล้วพิมพ์:

```
ตรวจสอบสถานะการเชื่อมต่อ Google
```

Claude จะเรียก `check_google_auth` และแสดงผล ✅ ถ้าทุกอย่างถูกต้อง

จากนั้นพิมพ์:

```
ช่วยสร้าง Folder Structure ของ Hibi Matcha ใน Google Drive
```

---

## วิธีที่ 2: OAuth2 (สำหรับ Local Machine เท่านั้น)

### Step 2.1 — สร้าง OAuth2 Credentials

1. ไปที่ [Google Cloud Console](https://console.cloud.google.com/) → **Credentials**
2. คลิก **+ Create Credentials** → **OAuth 2.0 Client IDs**
3. ตั้งค่า Application type: **Web application**
4. เพิ่ม Authorized redirect URI: `http://localhost:3001/oauth2callback`
5. คัดลอก **Client ID** และ **Client Secret**

### Step 2.2 — ตั้งค่า .env

```env
GOOGLE_CLIENT_ID=xxxx.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=GOCSPX-xxxxxxxx
GOOGLE_REDIRECT_URI=http://localhost:3001/oauth2callback
```

### Step 2.3 — รัน Auth Flow (เปิดเบราว์เซอร์)

```bash
cd mcp-google
npm run build
node dist/index.js --auth
```

เปิด URL ที่แสดงในเบราว์เซอร์ → อนุญาต → คัดลอก Refresh Token → ใส่ใน `.env`

```env
GOOGLE_REFRESH_TOKEN=1//xxxxxxxxxxxxxxxx
```

---

## Tools ที่ใช้งานได้หลัง Setup

| คำสั่งในการสนทนา | Tool ที่เรียก |
|-----------------|-------------|
| "ตรวจสอบการเชื่อมต่อ Google" | `check_google_auth` |
| "สร้าง Folder Structure ใน Drive" | `setup_hibi_drive` |
| "สรุปบทสนทนานี้ลง Google Docs" | `create_session_summary` |
| "สร้าง Doc ชื่อ X ใน Folder Y" | `create_google_doc` |
| "อัปโหลด MARKETING-PLAN.md ขึ้น Drive" | `upload_to_drive` |
| "อัปโหลดเอกสารทั้งหมดขึ้น Drive" | `upload_all_marketing_docs` |
| "แสดงไฟล์ใน Folder Analytics" | `list_drive_folder` |
| "สร้าง AI Audit Report สัปดาห์ที่ 24" | `create_audit_report_doc` |

---

## Folder Keys สำหรับ Tools

```
root
01_Marketing_Plan
01_Marketing_Plan/Annual_Plans
01_Marketing_Plan/Campaign_Briefs
01_Marketing_Plan/Budgets
02_Creative_Assets
02_Creative_Assets/Facebook_Instagram
02_Creative_Assets/TikTok
02_Creative_Assets/Grab_LineMan_Wongnai
02_Creative_Assets/Brand_Guidelines
02_Creative_Assets/Templates
03_Media_Buying
03_Media_Buying/Meta_Ads
03_Media_Buying/TikTok_Ads
03_Media_Buying/Google_Ads
03_Media_Buying/Reports
04_Analytics
04_Analytics/Weekly_Reports
04_Analytics/Monthly_Reports
04_Analytics/AB_Tests
04_Analytics/Dashboards
04_Analytics/AI_Learning
05_Food_Delivery
05_Food_Delivery/Grab
05_Food_Delivery/LINE_MAN
05_Food_Delivery/Wongnai
05_Food_Delivery/GMV_Reports
06_CRM_Loyalty
06_CRM_Loyalty/Email_Templates
06_CRM_Loyalty/LINE_OA
06_CRM_Loyalty/Loyalty_Program
06_CRM_Loyalty/Customer_Segments
07_Influencer
07_Influencer/KOL_Database
07_Influencer/Campaign_Reports
07_Influencer/Partnerships
07_Influencer/Referral_Program
08_AI_Agents
08_AI_Agents/Agent_Docs
08_AI_Agents/Prompts
08_AI_Agents/Audit_Reports
08_AI_Agents/Learning_Reports
09_Meeting_Notes
09_Meeting_Notes/Weekly
09_Meeting_Notes/Campaign_Reviews
09_Meeting_Notes/Strategy_Sessions
```

---

## Troubleshooting

**Permission denied บน Drive:**
→ ตรวจว่า Share Drive Folder กับ Service Account Email แล้ว (Step 1.5)

**Error: Could not load the default credentials:**
→ ตรวจ path ของ `service-account-key.json` ว่าถูกต้อง

**MCP Server ไม่ขึ้นใน Claude:**
→ ตรวจ `.claude/settings.json` ว่า path ถูกต้อง
→ Restart Claude Code session ใหม่

**Quota exceeded:**
→ Google Docs/Drive API มี Free Quota เพียงพอสำหรับใช้งานทั่วไป
→ ถ้าเกิน ไปตรวจสอบที่ Google Cloud Console → APIs → Quotas
