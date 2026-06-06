// สรุปบทสนทนา Hibi Matcha Session — มิถุนายน 2026
export const SESSION_SUMMARY = `# สรุปบทสนทนา — Hibi Matcha Marketing Planning Session
## วันที่: มิถุนายน 2026 | ผู้เข้าร่วม: CMO + Claude AI

---

## สิ่งที่สร้างในเซสชันนี้

### 1. แผนการตลาด (MARKETING-PLAN.md)
สร้างแผนการตลาดครบรูปแบบปีงบประมาณ 2026–2027 ครอบคลุม:
- การวิเคราะห์ตลาดชาเขียวพรีเมียมในไทย มูลค่า ~8,500 ล้านบาท เติบโต 12–15%
- กลุ่มเป้าหมาย 4 Personas: สายสุขภาพ, คนรัก J-Culture, พ่อแม่ออร์แกนิก, B2B
- Product Lines 7 กลุ่ม ตั้งแต่ ฿399 ถึง ฿3,999
- กลยุทธ์ 5 ช่องทาง: Website, Shopee/Lazada, Social Commerce, B2B, Workshop
- งบประมาณรายปี 4,650,000 THB พร้อม ROI target > 300%
- KPI รายไตรมาส และ Action Plan 4 Phase ตลอด 12 เดือน

### 2. โครงสร้าง AI Agents (MARKETING-AGENTS.md v2.0)
ออกแบบระบบ AI Agent สำหรับแผนกการตลาด ประกอบด้วย:

**Orchestrator Agent (Marketing Brain)**
- ประสานงานทุก Agent ให้ทำงานสอดคล้องกัน
- รายงานผลถึง CMO รายสัปดาห์

**Creative Media Agent** + 3 Sub-Agents
- Sub-Agent A1: Facebook & Instagram Designer (ผลิต 20+ Feed Posts/เดือน)
- Sub-Agent A2: TikTok Creative Designer (สร้าง Script + Thumbnail 20+ ชิ้น/เดือน)
- Sub-Agent A3: Content Writer (Copy, Caption, Blog, Email 30+ ชิ้น/เดือน)

**Media Buyer Agent** + 3 Sub-Agents
- Sub-Agent B1: Meta Ads Buyer — งบ 145,000 THB/เดือน, target ROAS > 5x
- Sub-Agent B2: TikTok Ads Buyer — งบ 85,000 THB/เดือน, target ROAS > 3x
- Sub-Agent B3: Google Ads Buyer — งบ 60,000 THB/เดือน, target ROAS > 6x
- งบรวม Paid Media: 300,000 THB/เดือน

**Analytics Team** + 3 Sub-Agents
- Sub-Agent C1: Report Builder (Daily Pulse + Weekly + Monthly Executive)
- Sub-Agent C2: A/B Test Manager (≥ 4 tests/เดือน)
- Sub-Agent C3: Competitive Intelligence Analyst (Monitor คู่แข่งทุกวัน)

**Food Delivery Agent** + 3 Sub-Agents
- Sub-Agent D1: Grab Agent — target GMV 150,000 THB/เดือน, Rating ≥ 4.7★
- Sub-Agent D2: LINE MAN Agent — target GMV 100,000 THB/เดือน, LINE Friends +500/เดือน
- Sub-Agent D3: Wongnai Agent — target Rating ≥ 4.5★, Reviews ≥ 50/เดือน
- รวม Delivery GMV target: 300,000 THB/เดือน

**CRM Agent** + 2 Sub-Agents
- Email Automation: Welcome Series, Abandoned Cart, Post-Purchase, Win-Back
- Loyalty Program Manager: "Hibi Tea Club" 4 Tiers

**Growth Agent** + 2 Sub-Agents
- Influencer Tracker: Scorecard 5 มิติ, EMV > 200,000 THB/เดือน
- Campaign Manager: Referral + B2B + Marketplace

### 3. ระบบ AI Learning (MARKETING-AI-LEARNING-SYSTEM.md)
สร้างระบบ Data Pool + Audit + Learning ครบวงจร:

**Central Data Pool (CDP)**
- 5 Data Pools: Performance, Agent Activity, Content, Customer Intelligence, Knowledge Base
- Streaming Pipeline: Real-time (Kafka) + Batch (Airbyte → BigQuery)
- Data Retention ตาม PDPA

**AI Audit Agent — PEAR Model**
- P (Performance) 35%, E (Efficiency) 25%, A (Accuracy) 25%, R (Relevance) 15%
- Audit รายวัน/สัปดาห์/เดือน ทุก Agent
- Anomaly Detection Rules อัตโนมัติ
- Audit Report format มาตรฐาน

**AI Learning Orchestrator — OODA Loop**
- กระบวนการ 4 ด้าน: Prompt Optimization, Memory Store, Feedback Loop, Version Control
- Prompt Library พร้อม Performance Score และ Version History
- Memory Store 3 ระดับ: Short (7 วัน), Medium (90 วัน), Long-term (Permanent)
- Human-in-the-Loop Checkpoints ทุกระดับ
- Learning Maturity Model 5 ระดับ: Reactive → Autonomous

### 4. MCP Server สำหรับ Google Docs & Drive
สร้าง MCP Server ที่เชื่อมต่อ Claude AI กับ Google Workspace:
- Tools สำหรับ Google Docs: สร้าง, เขียน, อ่าน Documents
- Tools สำหรับ Google Drive: สร้าง Folder, อัปโหลดไฟล์, จัดโครงสร้าง
- Folder Structure 9 หมวดหลักตามโครงสร้างงาน
- OAuth2 Authentication Flow

---

## Folder Structure ที่สร้างใน Google Drive

- 📁 01 Marketing Plan (แผนการตลาด, Campaign Briefs, งบประมาณ)
- 🎨 02 Creative Assets (FB/IG, TikTok, Delivery Banners, Templates)
- 📢 03 Media Buying (Meta, TikTok, Google Ads + Reports)
- 📈 04 Analytics (Weekly/Monthly Reports, A/B Tests, AI Learning)
- 🛵 05 Food Delivery (Grab, LINE MAN, Wongnai + GMV Reports)
- 💌 06 CRM & Loyalty (Email Templates, LINE OA, Hibi Tea Club)
- 🌟 07 Influencer & Growth (KOL Database, Campaign Reports, B2B)
- 🤖 08 AI Agents (Docs, Prompts, Audit Reports, Learning Reports)
- 📝 09 Meeting Notes (Weekly Syncs, Campaign Reviews, Strategy)

---

## สรุป KPIs หลักที่กำหนด

| หมวด | KPI | เป้าหมาย |
|------|-----|---------|
| รายได้ปีที่ 1 | Total Revenue | 3,600,000 THB |
| Paid Media | ROAS รวม | > 4x |
| Social Media | Instagram Engagement | > 5% |
| Food Delivery | Delivery GMV/เดือน | 300,000 THB |
| CRM | Email Open Rate | > 30% |
| Growth | CAC | < 350 THB |
| AI System | PEAR Score | เพิ่ม ทุกเดือน |
| AI System | Human Override Rate | ลด 5%/ไตรมาส |

---

## ไฟล์ที่สร้างในระบบ

- MARKETING-PLAN.md — แผนการตลาดครบรูปแบบ
- MARKETING-AGENTS.md — โครงสร้าง AI Agents และ Job Descriptions
- MARKETING-AI-LEARNING-SYSTEM.md — ระบบ AI Learning
- mcp-google/ — MCP Server สำหรับ Google Workspace Integration

ทั้งหมด commit บน branch: claude/hibi-matcha-marketing-plan-MsBHU
Repository: Nitirujzz/hibi-green-tea
`;
export const SESSION_DATE = new Date().toLocaleDateString("th-TH", {
    year: "numeric",
    month: "long",
    day: "numeric",
});
