# Hibi Matcha — Google Workspace MCP Server Setup Guide

## ขั้นตอนการตั้งค่า

---

### Step 1: สร้าง Google Cloud Project & Credentials

1. ไปที่ [Google Cloud Console](https://console.cloud.google.com/)
2. สร้าง Project ใหม่ชื่อ **"Hibi Matcha"**
3. เปิดใช้งาน APIs ต่อไปนี้:
   - **Google Docs API**
   - **Google Drive API**
4. ไปที่ **APIs & Services → Credentials → Create Credentials → OAuth 2.0 Client IDs**
5. ตั้งค่า:
   - Application type: **Web application**
   - Authorized redirect URIs: `http://localhost:3001/oauth2callback`
6. คัดลอก **Client ID** และ **Client Secret**

---

### Step 2: ตั้งค่า Environment Variables

```bash
# Copy .env.example เป็น .env
cp mcp-google/.env.example mcp-google/.env

# แก้ไข .env ใส่ค่าจริง
nano mcp-google/.env
```

```env
GOOGLE_CLIENT_ID=xxxx.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=GOCSPX-xxxxxxxx
GOOGLE_REDIRECT_URI=http://localhost:3001/oauth2callback
GOOGLE_REFRESH_TOKEN=   # ยังไม่ต้องใส่ตอนนี้
```

---

### Step 3: ติดตั้ง Dependencies และ Build

```bash
cd mcp-google
npm install
npm run build
```

---

### Step 4: รับ Refresh Token (ทำครั้งเดียว)

```bash
cd mcp-google
node dist/index.js --auth
```

- เบราว์เซอร์จะเปิดขึ้นให้ล็อกอิน Google
- อนุญาต Permissions
- คัดลอก **Refresh Token** ที่แสดงในหน้าต่าง
- ใส่ลงใน `.env` ที่ `GOOGLE_REFRESH_TOKEN=`

---

### Step 5: ลงทะเบียน MCP Server กับ Claude Code

ไฟล์ `.claude/settings.json` ถูกสร้างไว้แล้ว แต่ต้องตั้ง Environment Variables:

```bash
# เพิ่มใน ~/.bashrc หรือ ~/.zshrc
export GOOGLE_CLIENT_ID="your_client_id"
export GOOGLE_CLIENT_SECRET="your_client_secret"
export GOOGLE_REFRESH_TOKEN="your_refresh_token"
```

หรือสร้าง `.env.local` ใน root project แล้วอ้างอิงจาก settings

---

### Step 6: ทดสอบการเชื่อมต่อ

เริ่ม Claude Code session ใหม่ แล้วลองพิมพ์:

```
ช่วยสร้าง Folder Structure ของ Hibi Matcha ใน Google Drive
```

Claude จะเรียก Tool `setup_hibi_drive` โดยอัตโนมัติ

---

## Tools ที่ใช้งานได้

| Tool | คำอธิบาย |
|------|---------|
| `setup_hibi_drive` | สร้าง Folder Structure 9 หมวดใน Google Drive |
| `create_session_summary` | สร้าง Doc สรุปบทสนทนาใน Meeting Notes |
| `create_google_doc` | สร้าง Google Doc ใน Folder ที่ต้องการ |
| `upload_to_drive` | อัปโหลดไฟล์จาก Repo ขึ้น Drive |
| `upload_all_marketing_docs` | อัปโหลดเอกสารการตลาดทั้งหมด |
| `list_drive_folder` | แสดงรายการไฟล์ใน Folder |
| `create_audit_report_doc` | สร้าง AI Audit Report Doc |

---

## โครงสร้าง Folder ที่จะสร้าง

```
📁 Hibi Matcha — Marketing Hub
├── 📊 01 — Marketing Plan
│   ├── 📅 Annual Plans
│   ├── 📋 Campaign Briefs
│   └── 💰 Budgets & Finance
├── 🎨 02 — Creative Assets
│   ├── 📸 Facebook & Instagram
│   ├── 🎵 TikTok Videos & Scripts
│   ├── 🛵 Delivery Platform Banners
│   ├── 🎨 Brand Guidelines
│   └── 📐 Design Templates
├── 📢 03 — Media Buying
│   ├── 💙 Meta Ads (FB + IG)
│   ├── 🎵 TikTok Ads
│   ├── 🔍 Google Ads
│   └── 📈 Ad Performance Reports
├── 📈 04 — Analytics & Data
│   ├── 📊 Weekly Reports
│   ├── 📅 Monthly Reports
│   ├── 🧪 A/B Test Results
│   ├── 🖥️ Dashboard Exports
│   └── 🤖 AI Audit & Learning Reports
├── 🛵 05 — Food Delivery Platforms
│   ├── 🟢 Grab
│   ├── 🟡 LINE MAN
│   ├── 🔴 Wongnai Food
│   └── 💰 GMV & Sales Reports
├── 💌 06 — CRM & Loyalty
│   ├── ✉️ Email Templates & Flows
│   ├── 💬 LINE Official Account
│   ├── ⭐ Hibi Tea Club
│   └── 👥 Customer Segments
├── 🌟 07 — Influencer & Growth
│   ├── 📋 KOL Database & Scorecards
│   ├── 📊 Campaign Reports
│   ├── 🤝 B2B & Partnerships
│   └── 🔗 Referral Program
├── 🤖 08 — AI Agents & Automation
│   ├── 📄 Agent Documentation
│   ├── 💡 Prompt Library
│   ├── 🔍 AI Audit Reports
│   └── 🧠 AI Learning Reports
└── 📝 09 — Meeting Notes & Summaries
    ├── 📅 Weekly Syncs
    ├── 🎯 Campaign Reviews
    └── 🗺️ Strategy Sessions
```

---

## Troubleshooting

**Token Expired Error:**
```bash
# รัน Auth Flow ใหม่
node dist/index.js --auth
```

**Permission Denied:**
- ตรวจสอบว่าเปิด Google Docs API และ Google Drive API แล้ว
- ตรวจสอบ OAuth Scopes

**MCP Server ไม่ขึ้นใน Claude:**
- Restart Claude Code session
- ตรวจสอบ `.claude/settings.json`
