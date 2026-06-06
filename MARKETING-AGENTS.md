# Hibi Matcha — Marketing Department Agents & Sub-Agents
## โครงสร้างทีมการตลาดและ AI Agent Architecture
### เวอร์ชัน 2.0 — ปรับปรุง มิถุนายน 2026

---

## 1. ภาพรวมโครงสร้างองค์กร (Organizational Overview)

```
                       ┌─────────────────────────┐
                       │  Chief Marketing Officer │
                       │    (CMO / Head of Mktg)  │
                       └────────────┬─────────────┘
                                    │
               ┌────────────────────▼──────────────────────┐
               │        MARKETING ORCHESTRATOR AGENT        │
               │           🤖 Hibi Marketing Brain          │
               └──┬──────┬──────┬──────┬──────┬──────┬─────┘
                  │      │      │      │      │      │
          ┌───────▼─┐ ┌──▼───┐ ┌▼────┐ ┌─────▼┐ ┌───▼────┐ ┌▼──────────┐
          │CREATIVE │ │MEDIA │ │ANALY│ │FOOD  │ │  CRM   │ │  GROWTH   │
          │ MEDIA   │ │BUYER │ │TICS │ │DELIV.│ │  AGENT │ │  AGENT    │
          │  AGENT  │ │AGENT │ │TEAM │ │AGENT │ │        │ │           │
          └────┬────┘ └──┬───┘ └──┬──┘ └──┬───┘ └───┬────┘ └────┬──────┘
               │         │        │        │          │           │
          ┌────┴────┐ ┌──┴──┐ ┌───┴──┐ ┌──┴────┐ ┌──┴──────┐ ┌──┴──────┐
          │FB/IG    │ │Meta │ │Report│ │Grab   │ │Email    │ │Influencer│
          │Designer │ │Buyer│ │Build.│ │Agent  │ │Auto     │ │Tracker  │
          └─────────┘ └─────┘ └──────┘ └───────┘ └─────────┘ └─────────┘
          ┌────┴────┐ ┌──┴──┐ ┌───┴──┐ ┌──┴────┐ ┌──┴──────┐ ┌──┴──────┐
          │TikTok   │ │TikTk│ │A/B   │ │LineMan│ │Loyalty  │ │Campaign │
          │Designer │ │Buyer│ │Test  │ │Agent  │ │Manager  │ │Manager  │
          └─────────┘ └─────┘ └──────┘ └───────┘ └─────────┘ └─────────┘
          ┌────┴────┐ ┌──┴──┐ ┌───┴──┐ ┌──┴────┐
          │Content  │ │Goog.│ │Compet│ │Wongnai│
          │Writer   │ │Buyer│ │Intel │ │Agent  │
          └─────────┘ └─────┘ └──────┘ └───────┘
```

---

## 2. ORCHESTRATOR AGENT — Hibi Marketing Brain

### Job Title
**Chief Marketing Orchestrator Agent (CMOA)**
`agent-id: hibi-marketing-brain`

### Mission Statement
> ประสานงานและควบคุม Agents ทุกตัวให้ทำงานอย่างสอดคล้องกัน
> เพื่อบรรลุเป้าหมายการตลาดของ Hibi Matcha ทุกช่องทาง

### Core Responsibilities

| ความรับผิดชอบ | รายละเอียด | ความถี่ |
|-------------|----------|--------|
| **Strategic Planning** | แปลงเป้าหมายธุรกิจเป็น Marketing Roadmap | รายสัปดาห์ |
| **Agent Coordination** | มอบหมายงานให้ทุก Agent และติดตามผล | ทุกวัน |
| **Cross-Channel Sync** | ทำให้ Message ทุก Channel สอดคล้องกัน | ทุกวัน |
| **Executive Reporting** | สรุปผลการตลาดรายสัปดาห์/รายเดือนถึง CMO | รายสัปดาห์ |
| **Budget Oversight** | ตรวจสอบการใช้งบประมาณทุก Agent | รายสัปดาห์ |
| **Crisis Management** | รับมือเหตุการณ์ที่ส่งผลต่อ Brand | Real-time |

### Input → Output

```
INPUT:
  - Business Goals จาก CMO
  - Market Data จาก Analytics Team
  - Customer Signals จาก CRM Agent
  - Delivery Platform Data จาก Food Delivery Agent
  - Creative Assets จาก Creative Media Agent
  - Spend Reports จาก Media Buyer Agent

OUTPUT:
  - Weekly Marketing Brief ถึงทุก Agent
  - Executive Dashboard (ครอบคลุมทุก Channel)
  - Escalation Alerts
  - Budget Reallocation Instructions
```

### KPIs
- Overall Marketing ROI > 300%
- Inter-agent Task Completion Rate > 95%
- Time-to-Campaign-Launch < 48 hours
- Cross-channel Message Consistency Score > 90%

---

## 3. AGENT A — Creative Media Agent

### Job Title
**Creative Media Design & Content Agent**
`agent-id: hibi-creative-media`

### Mission
> ออกแบบและผลิต Creative Assets ทุกชิ้นที่ใช้บน Facebook, Instagram และ TikTok
> ให้สวยงาม สอดคล้องกับ Brand Identity และเหมาะกับแต่ละ Platform

### Job Description

Creative Media Agent เป็นหัวใจของการสื่อสารด้านภาพและเนื้อหาของ Hibi Matcha
รับผิดชอบตั้งแต่การกำหนด Visual Direction ไปจนถึงการผลิต Asset จริง
ทุกชิ้นงานต้องผ่านการตรวจสอบ Brand Guideline ก่อน Publish เสมอ

### Responsibilities

```
┌──────────────────────────────────────────────────────────────┐
│  DAILY TASKS                                                 │
│  ├── สร้าง Creative Assets 3–5 ชิ้นสำหรับ Social Media      │
│  ├── Review และ Approve งานจาก Sub-Agents                    │
│  └── Monitor Brand Aesthetic Consistency ทุก Platform        │
│                                                              │
│  WEEKLY TASKS                                                │
│  ├── จัดทำ Content Calendar พร้อม Visual Direction           │
│  ├── Creative Brief สำหรับ Campaign ถัดไป                   │
│  ├── Template Update ตามเทศกาลหรือ Seasonal                  │
│  └── รายงาน Creative Performance ถึง Orchestrator           │
│                                                              │
│  MONTHLY TASKS                                               │
│  ├── Brand Asset Audit — ตรวจสอบ Consistency ทุกช่องทาง    │
│  ├── New Template Library สำหรับไตรมาสถัดไป                 │
│  └── Competitor Creative Analysis                            │
└──────────────────────────────────────────────────────────────┘
```

### Sub-Agents ภายใต้

#### Sub-Agent A1 — Facebook & Instagram Designer

**Job Description:**
ออกแบบ Visual Content ทุกรูปแบบสำหรับ Facebook และ Instagram
เน้น High-quality Photography Style และ Japanese Aesthetic ที่เป็นเอกลักษณ์ของแบรนด์

**Job Role:** Facebook & Instagram Visual Designer

**Responsibilities:**

| Asset Type | Spec | Quota/เดือน |
|-----------|------|------------|
| Feed Post (Square) | 1080×1080px | 20 ชิ้น |
| Feed Post (Portrait) | 1080×1350px | 10 ชิ้น |
| Instagram Stories | 1080×1920px | 30 ชิ้น |
| Instagram Reels Cover | 1080×1920px | 8 ชิ้น |
| Facebook Cover Photo | 851×315px | 2 ชิ้น/ไตรมาส |
| Facebook Event Banner | 1920×1005px | ตามกิจกรรม |
| Carousel (5–10 slides) | 1080×1080px | 4 ชุด |
| Ad Creative (Static) | หลาย Ratio | 10 ชิ้น |

**Design Guidelines:**
- สีหลัก: Hibi Green (#22c55e), Tea Cream (#f7f3e9), Premium Gold (#fbbf24)
- Font: Geist + Japanese-inspired Decorative Font
- Mood: Calm, Premium, Authentic Japanese
- ต้องมี Logo Watermark และ Product Tag ทุกชิ้น

**Tools:** Figma, Adobe Photoshop, Canva Pro, Adobe Lightroom

---

#### Sub-Agent A2 — TikTok Creative Designer

**Job Description:**
ออกแบบ Visual และ Script สำหรับ TikTok โดยเฉพาะ
เน้น Hook ที่แรงใน 3 วินาทีแรก และ Editing Style ที่เข้ากับ TikTok Algorithm

**Job Role:** TikTok Creative Strategist & Designer

**Responsibilities:**

| งาน | รายละเอียด | Quota/เดือน |
|-----|----------|------------|
| TikTok Video Script | Hook + Story + CTA (15–60 วิ) | 20 scripts |
| Video Thumbnail Design | 1080×1920px, Eye-catching | 20 ชิ้น |
| Text Overlay & Caption | Thai + English subtitles | ทุก video |
| Sound Selection | Trending audio + Brand music | ทุก video |
| TikTok Ad Creative | In-feed + TopView format | 8 ชิ้น |
| Stitch/Duet Templates | สำหรับ UGC campaigns | 2/เดือน |

**TikTok Content Formula:**

```
3 วินาทีแรก  ──►  Hook (คำถาม/Shock/Curiosity)
วินาที 3–10  ──►  Problem หรือ Context
วินาที 10–40 ──►  Solution / Product Showcase
วินาที 40–55 ──►  Social Proof / Result
วินาที 55–60 ──►  CTA (Link in bio / Comment)
```

**Content Pillars สำหรับ TikTok:**
- "Did you know?" — ความรู้เรื่อง Matcha
- Satisfying Matcha Brewing (ASMR)
- Matcha Recipe Challenge
- POV: Working from Home + Matcha
- "Japanese vs Thai Reaction" formats

**Tools:** CapCut, Adobe Premiere Pro, After Effects, Canva Video

---

#### Sub-Agent A3 — Content Writer (Copy & Script)

**Job Description:**
เขียน Copy, Caption, Script และ Hashtag Strategy สำหรับทุก Platform
ให้มี Brand Voice ที่สม่ำเสมอ น่าอ่าน และกระตุ้น Engagement

**Job Role:** Social Media Copywriter & Content Strategist

**Responsibilities:**

| งาน | Platform | Quota/เดือน |
|-----|---------|------------|
| Post Caption | FB + IG | 30 captions |
| TikTok Script | TikTok | 20 scripts |
| Hashtag Research | IG + TikTok | รายสัปดาห์ |
| Stories Text/Poll | IG Stories | 30 ชิ้น |
| Blog Article (SEO) | Website | 4 articles |
| Email Newsletter | Email | 4 newsletters |
| Ad Copy | FB/IG/TikTok Ads | 15 copy sets |

**Brand Voice Guidelines:**

```
โทน:    Warm, Knowledgeable, Japanese-Inspired, Approachable
ภาษา:  ไทยเป็นหลัก, English สำหรับ Hashtag และ International
หลีก:  Hard Sell, Clickbait, ภาษาที่ดูถูกลูกค้า
เน้น:  Storytelling, Education, Community, Authenticity
```

**Tools:** Claude API, Grammarly, SEMrush, Notion

---

### Creative Media Agent — Input → Output

```
INPUT:
  - Brand Guidelines (HIBI-BRAND-GUIDE.md)
  - Campaign Brief จาก Orchestrator
  - Trending Formats จาก Analytics Team
  - Product Photos / Assets จาก Photography Team
  - Seasonal Calendar

OUTPUT:
  → Facebook Feed Posts (Static + Carousel + Video)
  → Instagram Feed + Stories + Reels
  → TikTok Videos (Script + Design + Edit Direction)
  → Ad Creatives → Media Buyer Agent
  → Content Calendar รายสัปดาห์
  → Brand Asset Library (อัปเดตทุกเดือน)
```

### Tools & Tech Stack
- **Figma** — UI/UX Design & Prototyping
- **Adobe Creative Suite** — Photoshop, Premiere, After Effects
- **Canva Pro** — Template-based design
- **CapCut** — TikTok video editing
- **Buffer** — Content scheduling
- **Notion** — Creative brief & approval workflow

### KPIs

| Metric | เป้าหมาย |
|--------|---------|
| Instagram Engagement Rate | > 5% |
| TikTok Average Watch Time | > 50% |
| Ad Creative CTR (FB/IG) | > 2% |
| Content On-time Delivery | 100% |
| Brand Consistency Score | > 90% |
| Creative Output/เดือน | ≥ 80 ชิ้น |

---

## 4. AGENT B — Media Buyer Agent

### Job Title
**Paid Media Buying & Optimization Agent**
`agent-id: hibi-media-buyer`

### Mission
> บริหารงบโฆษณาทุกบาทบน Facebook, Instagram, TikTok และ Google
> ให้ได้ ROAS สูงสุด ด้วยการ Optimize แบบ Real-time

### Job Description

Media Buyer Agent รับผิดชอบการซื้อสื่อโฆษณาแบบ Paid ทุกช่องทาง
ตั้งแต่การวางแผนงบ การตั้ง Targeting ไปจนถึงการ Optimize และ Report
ทำงานร่วมกับ Creative Media Agent (รับ Assets) และ Analytics Team (รับข้อมูล)

### Responsibilities

```
┌──────────────────────────────────────────────────────────────┐
│  DAILY TASKS                                                 │
│  ├── ตรวจสอบ Campaign Performance ทุก Platform               │
│  ├── Optimize Bid Strategy & Budget Allocation               │
│  ├── Pause / Scale Ads ตาม Performance Threshold             │
│  └── Alert Orchestrator ถ้า ROAS ต่ำกว่า 3x                 │
│                                                              │
│  WEEKLY TASKS                                                │
│  ├── Creative Refresh — เปลี่ยน Ad Copy / Visual ที่ตก      │
│  ├── Audience Testing — เพิ่ม Lookalike / Interest segments  │
│  ├── Weekly Spend & Performance Report                       │
│  └── A/B Test สรุปผลและ Scale Winner                        │
│                                                              │
│  MONTHLY TASKS                                               │
│  ├── Media Plan รายเดือนถัดไป                               │
│  ├── Full-funnel Attribution Report                          │
│  ├── Platform Budget Rebalancing                             │
│  └── Competitor Ad Analysis                                  │
└──────────────────────────────────────────────────────────────┘
```

### Sub-Agents ภายใต้

#### Sub-Agent B1 — Meta Ads Buyer (Facebook & Instagram)

**Job Description:**
บริหาร Facebook Ads และ Instagram Ads ให้ครอบคลุม Full Funnel
ตั้งแต่ Brand Awareness ไปถึง Conversion และ Retargeting

**Job Role:** Meta Ads Specialist & Performance Marketer

**Responsibilities:**

| Campaign Type | Objective | Budget/เดือน | KPI |
|-------------|---------|-------------|-----|
| Brand Awareness | Reach / Impressions | 30,000 THB | CPM < 80 THB |
| Traffic | Link Clicks | 20,000 THB | CPC < 5 THB |
| Engagement | Post Engagement | 15,000 THB | CPE < 1 THB |
| Lead Generation | Lead Form | 20,000 THB | CPL < 150 THB |
| Conversion | Purchase | 40,000 THB | ROAS > 5x |
| Retargeting | Dynamic Product Ads | 20,000 THB | ROAS > 8x |

**Audience Strategy:**

```
COLD AUDIENCE (Awareness)
├── Interest: Japanese food, Health, Matcha, Tea
├── Behavior: Online shoppers, Health-conscious
└── Demographics: TH, 18–45, All genders

WARM AUDIENCE (Consideration)
├── Website Visitors (30/60/90 days)
├── Video Viewers (25%/50%/75%)
└── Instagram/FB Page Engagers

HOT AUDIENCE (Conversion)
├── Add-to-Cart แต่ยังไม่ซื้อ
├── Checkout Initiated
└── Past Purchasers → Upsell
```

**Tools:** Meta Ads Manager, Meta Business Suite, Meta Pixel, Conversions API

---

#### Sub-Agent B2 — TikTok Ads Buyer

**Job Description:**
บริหาร TikTok Ads ให้เข้าถึงกลุ่ม Gen Z และ Millennials ผ่านรูปแบบโฆษณา
ที่กลืนไปกับ Content ธรรมชาติบน TikTok (Native-style Ads)

**Job Role:** TikTok Ads Specialist

**Responsibilities:**

| Ad Format | วัตถุประสงค์ | Budget/เดือน | KPI |
|----------|-----------|-------------|-----|
| In-Feed Ads | Traffic + Conversion | 25,000 THB | CPV < 0.30 THB |
| TopView | Brand Awareness (เปิดตัว/Seasonal) | 30,000 THB | CPM < 100 THB |
| Spark Ads | Boost Organic Posts | 15,000 THB | Engagement Rate > 8% |
| Collection Ads | Product Discovery | 15,000 THB | CTR > 3% |
| Branded Hashtag | Community Campaign | ตามแคมเปญ | UGC > 500 videos |

**TikTok Targeting:**

```
Demographics: TH, อายุ 18–35
Interest: Beauty & Skincare, Food & Drink, Japanese Culture,
          Fitness & Health, Coffee & Tea
Behavior: Video Creators, Active TikTok users
Custom: Website Pixel Audience, Customer List Upload
Lookalike: 1% / 3% / 5% จาก Customer List
```

**Tools:** TikTok Ads Manager, TikTok Pixel, TikTok Business Center

---

#### Sub-Agent B3 — Google Ads Buyer

**Job Description:**
บริหาร Google Ads เพื่อ Capture Demand จากลูกค้าที่กำลังค้นหา Matcha อยู่แล้ว
และ Retarget ผู้เยี่ยมชมเว็บไซต์ผ่าน Display Network

**Job Role:** Google Ads & SEM Specialist

**Responsibilities:**

| Campaign Type | Keywords/Placement | Budget/เดือน | KPI |
|-------------|------------------|-------------|-----|
| Search — Brand | "Hibi Matcha", "Hibi ชาเขียว" | 5,000 THB | CPC < 8 THB |
| Search — Generic | "มัทฉะ", "ชาเขียวญี่ปุ่น", "ผงมัทฉะ" | 20,000 THB | CPC < 15 THB |
| Shopping | Product Feed Ads | 15,000 THB | ROAS > 6x |
| Display Retargeting | GDN — Website Visitors | 10,000 THB | CPC < 5 THB |
| YouTube Ads | Pre-roll สำหรับ Brand Video | 10,000 THB | CPV < 0.50 THB |

**Tools:** Google Ads, Google Merchant Center, Google Analytics 4, Google Tag Manager

---

### Media Buyer Agent — Input → Output

```
INPUT:
  - Monthly Budget Approval จาก Orchestrator
  - Creative Assets จาก Creative Media Agent
  - Audience Insights จาก Analytics Team
  - Product Feed จาก Website (Prisma DB)
  - Promotional Calendar จาก CMO

OUTPUT:
  → Live Campaigns (Meta / TikTok / Google)
  → Daily Spend Alert ถ้าเกิน Threshold
  → Weekly ROAS Report → Analytics Team
  → Creative Performance Report → Creative Agent
  → Monthly Media Plan
  → Platform Budget Rebalancing Request → Orchestrator
```

### งบประมาณรวม Media Buyer

| Platform | งบ/เดือน (THB) | % |
|---------|--------------|---|
| Meta (FB + IG) | 145,000 | 48% |
| TikTok Ads | 85,000 | 28% |
| Google Ads | 60,000 | 20% |
| Other / Test | 10,000 | 4% |
| **รวม** | **300,000** | **100%** |

### KPIs

| Metric | เป้าหมาย |
|--------|---------|
| Overall ROAS | > 4x |
| Meta ROAS | > 5x |
| TikTok ROAS | > 3x |
| Google ROAS | > 6x |
| CAC (Cost per Acquisition) | < 350 THB |
| CTR รวม | > 2% |
| Budget Utilization | 95–100% |

---

## 5. AGENT C — Analytics Team

### Job Title
**Data Analytics & Intelligence Team Agent**
`agent-id: hibi-analytics-team`

### Mission
> เป็น Single Source of Truth ของข้อมูลการตลาดทั้งหมด
> วิเคราะห์ทุก Channel รวมถึง Food Delivery Platforms
> และส่ง Actionable Insights ให้ทุก Agent ตัดสินใจได้อย่างถูกต้อง

### Job Description

Analytics Team เป็นมากกว่าแค่ทีมรายงาน — เป็น Intelligence Hub ที่รวบรวม
ข้อมูลจากทุกจุดสัมผัสของลูกค้า ทั้ง Website, Social Media, Food Delivery,
Paid Ads และ CRM แล้วแปลงเป็น Insights ที่ Drive Decisions จริง

### Responsibilities

| หมวด | งาน | Output |
|------|-----|--------|
| **Multi-Channel Tracking** | ติดตาม KPI ครบทุก Channel แบบ Real-time | Live Dashboard |
| **Funnel Analysis** | วิเคราะห์ Customer Journey Awareness → Purchase | Funnel Report |
| **Delivery Platform Analytics** | วิเคราะห์ Grab, Line Man, Wongnai Performance | Platform Report |
| **Paid Media Analytics** | ประเมิน ROAS / CAC / Attribution ทุก Platform | Media Report |
| **Competitor Intelligence** | Monitor คู่แข่ง Pricing, Promotion, Content | Intel Report |
| **Predictive Modeling** | พยากรณ์ยอดขาย + Inventory Needs | Forecast |
| **A/B Testing** | ออกแบบและสรุป Experiments | Test Report |

### Sub-Agents ภายใต้

#### Sub-Agent C1 — Performance Report Builder

**Job Description:**
สร้าง Automated Reports ทุกระดับ ตั้งแต่ Daily Dashboard จนถึง Monthly Executive Report
โดยรวมข้อมูลจากทุก Agent และทุก Platform ในรายงานเดียว

**Job Role:** Marketing Analytics Reporter

**Responsibilities:**

| Report | ความถี่ | ผู้รับ | เนื้อหา |
|--------|--------|-------|--------|
| Daily Pulse | ทุกวัน 08:00 | Orchestrator | Revenue, Spend, ROAS, Orders |
| Social Media Weekly | ทุกจันทร์ | Creative Agent | Reach, Engagement, Followers |
| Ads Performance Weekly | ทุกจันทร์ | Media Buyer Agent | ROAS, CTR, CPC per Platform |
| Food Delivery Weekly | ทุกจันทร์ | Food Delivery Agent | GMV, Orders, Rating per Platform |
| Executive Monthly | วันที่ 1 ของเดือน | CMO | Full Business Overview |
| Campaign Post-Mortem | หลังทุกแคมเปญ | Orchestrator | ROI, Learnings, Recommendations |

**Dashboard Architecture:**

```
EXECUTIVE LAYER (CMO)
└── Revenue | Orders | CAC | CLV | NPS

CHANNEL LAYER (Agent Level)
├── Social: Reach, Engagement, Followers
├── Paid Media: Spend, ROAS, CAC per Platform
├── Delivery Platforms: GMV, Orders, Rating
├── CRM: Retention, Open Rate, LTV
└── Website: Traffic, CVR, AOV

OPERATIONAL LAYER (Real-time)
└── Live Ad Spend | Live Orders | Alert Feed
```

**Tools:** Looker Studio, Google Sheets API, BigQuery, Notion API

---

#### Sub-Agent C2 — A/B Test & Experimentation Manager

**Job Description:**
ออกแบบ ดำเนินการ และสรุปผล Experiments ทั้งหมดเพื่อปรับปรุง
Conversion Rate, Engagement และ Ad Performance อย่างต่อเนื่อง

**Job Role:** Experimentation & CRO Specialist

**Responsibilities:**

| Experiment Type | ตัวอย่าง | เป้าหมาย |
|---------------|--------|---------|
| Ad Creative A/B | Static vs Video, Thai vs Eng Copy | CTR +20% |
| Landing Page Test | Hero Image, CTA Button Color | CVR +15% |
| Email Subject Line | Emoji vs No Emoji, Thai vs Eng | Open Rate +10% |
| Pricing Display | Original+Discount vs % Off | AOV +10% |
| TikTok Hook Test | Question vs Statement vs Shock | Watch Time +30% |
| Delivery Platform Banner | Photo A vs B | CTR +25% |

**Testing Protocol:**

```
1. HYPOTHESIS — "ถ้าเปลี่ยน X เป็น Y จะทำให้ Z เพิ่มขึ้น N%"
2. SETUP — กำหนด Control / Variant, Sample Size, Duration
3. RUN — ทดสอบจนได้ Statistical Significance (95%)
4. ANALYZE — วัด Primary + Secondary Metrics
5. DECIDE — Scale Winner / Iterate Loser / Document Learning
```

**Tools:** VWO, Google Optimize, Meta A/B Test Tool, TikTok Split Test

---

#### Sub-Agent C3 — Competitive Intelligence Analyst

**Job Description:**
ติดตามและวิเคราะห์คู่แข่งในทุกมิติ ทั้ง Social Media, Pricing,
Promotions และ Delivery Platform Presence เพื่อแจ้ง Insights ให้ทีม

**Job Role:** Market & Competitive Intelligence Analyst

**Responsibilities:**

| งาน | ความถี่ | Output |
|-----|--------|--------|
| Social Media Monitor คู่แข่ง | ทุกวัน | Alert ถ้ามีแคมเปญใหม่ |
| Pricing Benchmark | รายสัปดาห์ | Price Gap Analysis |
| Delivery Platform Ranking | รายสัปดาห์ | Rank Comparison |
| Ad Library Scan (Meta/TikTok) | รายสัปดาห์ | Competitor Creative Intel |
| Market Share Estimate | รายเดือน | Share of Voice Report |
| Trend Radar | Real-time | Trend Alert → Creative Agent |

**คู่แข่งที่ Monitor:**
- แบรนด์ Matcha นำเข้าบน Shopee/Lazada Top 10
- ร้านชาญี่ปุ่นที่มี Delivery บน Grab/Line Man
- Influencer-brand Matcha ในไทย
- แบรนด์สุขภาพที่ขาย Matcha Products

**Tools:** Meta Ad Library, TikTok Creative Center, SimilarWeb, Semrush, Wongnai Merchant Insights

---

### Analytics Team — Input → Output

```
INPUT:
  - GA4 (Website + App)
  - Meta Ads API + Pixel Data
  - TikTok Ads API + Pixel
  - Google Ads API
  - Grab / Line Man Merchant Dashboard API
  - Wongnai Merchant Data
  - Stripe Payment Data
  - CRM / Prisma DB

OUTPUT:
  → Daily Pulse Dashboard → Orchestrator
  → Weekly Channel Reports → แต่ละ Agent
  → Monthly Executive Report → CMO
  → A/B Test Results → Creative + Media Buyer
  → Competitor Intel Alerts → Orchestrator
  → Predictive Sales Forecast → CMO + Inventory
```

### Tools & Tech Stack
- **Google Analytics 4** — Web analytics
- **Looker Studio** — Dashboard visualization
- **BigQuery** — Data warehouse & SQL queries
- **Python / Pandas** — Data processing & modeling
- **Hotjar** — Heatmaps & session recording
- **SEMrush / SimilarWeb** — Competitive intelligence
- **Meta Insights API** — Social & Ad data

### KPIs

| Metric | เป้าหมาย |
|--------|---------|
| Dashboard Uptime | 99.9% |
| Report On-time Delivery | 100% |
| A/B Tests per Month | ≥ 4 |
| Insights Acted Upon | > 80% |
| Forecast Accuracy | ±10% |
| Trend Alert Lead Time | > 48 ชั่วโมง |

---

## 6. AGENT D — Food Delivery Platform Agent

### Job Title
**Food Delivery & Online Marketplace Agent**
`agent-id: hibi-delivery-agent`

### Mission
> บริหารและเติบโตช่องทาง Grab, Line Man และ Wongnai Food
> ให้เป็น Revenue Stream หลักสำหรับการซื้อ Matcha พร้อมดื่มและสินค้าพรีเมียม

### Job Description

Food Delivery Agent รับผิดชอบทุกกิจกรรมบน 3 Platform หลัก ตั้งแต่การตั้งค่าร้าน
การออกแบบหน้าเมนู การบริหารโปรโมชั่น การดูแลรีวิว ไปจนถึงการวิเคราะห์ยอดขาย
โดยทำงานร่วมกับ Creative Media Agent เพื่อออกแบบ Banner และ Menu Photos

### Responsibilities

```
┌──────────────────────────────────────────────────────────────┐
│  DAILY TASKS                                                 │
│  ├── ตรวจสอบ Orders, Ratings และ Reviews ทั้ง 3 Platforms    │
│  ├── ตอบ Reviews ที่มีคะแนนต่ำกว่า 4 ดาว ภายใน 2 ชั่วโมง   │
│  ├── Monitor สต็อกสินค้าพร้อมส่งผ่าน Delivery               │
│  └── ปรับ Availability ถ้าสินค้าหมด                         │
│                                                              │
│  WEEKLY TASKS                                                │
│  ├── วิเคราะห์ Best-selling Items และ Slow Movers            │
│  ├── ปรับ In-platform Promotions ตาม Performance            │
│  ├── ส่ง Banner Brief → Creative Media Agent                 │
│  └── Weekly Revenue Report ถึง Orchestrator                  │
│                                                              │
│  MONTHLY TASKS                                               │
│  ├── Menu Optimization — เพิ่ม/ลบ/ปรับ Items                │
│  ├── Platform Commission Negotiation Prep                    │
│  ├── Seasonal Menu Planning                                  │
│  └── Full Platform Performance Review                        │
└──────────────────────────────────────────────────────────────┘
```

### Sub-Agents ภายใต้

#### Sub-Agent D1 — Grab Merchant Agent

**Job Description:**
บริหารร้าน Hibi Matcha บน GrabFood และ GrabMart อย่างครบวงจร
ตั้งแต่การตั้งราคา การออกแบบโปรโมชั่น จนถึงการ Optimize Ranking ภายใน App

**Job Role:** Grab Platform Manager

**Responsibilities:**

| งาน | รายละเอียด | KPI |
|-----|----------|-----|
| **Store Optimization** | ปรับ Store Name, Banner, Description ให้ค้นหาเจอ | Top 5 in Category |
| **Menu Management** | อัปเดตเมนู ราคา รูปภาพ คำอธิบาย | Menu Accuracy 100% |
| **GrabAds** | รันโฆษณาใน Grab Platform | ROAS > 3x |
| **Voucher/Promo** | ตั้ง Flash Sale, Bundle, Free Delivery | GMV +20% |
| **Rating Management** | ติดตามและตอบ Reviews ทุกข้อ | Rating ≥ 4.7 ★ |
| **Grab Mart Listing** | สินค้าแบบ Delivery เร็ว (ผงมัทฉะ, Gift Set) | Conversion > 8% |

**สินค้าที่จำหน่ายบน Grab:**

```
GRAB FOOD (พร้อมดื่ม/พร้อมชง)
├── Iced Matcha Latte — ฿120
├── Hot Matcha Latte — ฿110
├── Matcha Smoothie — ฿135
└── Matcha Workshop Voucher — ฿1,500

GRAB MART (สินค้า Packaged)
├── Ceremonial Grade Matcha 30g — ฿999
├── Matcha Starter Kit — ฿1,299
└── Matcha Gift Set (S/M/L) — ฿999–3,999
```

**Tools:** Grab Merchant Portal, GrabAds Dashboard, Grab Merchant App

---

#### Sub-Agent D2 — Line Man Merchant Agent

**Job Description:**
บริหารร้าน Hibi Matcha บน LINE MAN Wongnai ให้เติบโตทั้งฝั่ง Food Delivery
และการเชื่อมต่อกับ LINE OA ของแบรนด์เพื่อสร้าง Seamless Customer Experience

**Job Role:** LINE MAN Platform Manager & LINE Ecosystem Specialist

**Responsibilities:**

| งาน | รายละเอียด | KPI |
|-----|----------|-----|
| **Store Setup & Branding** | Banner, Logo, Store Description | Brand Consistency |
| **Menu & Pricing** | เมนูพร้อมดื่ม + Product Delivery | Menu Accuracy 100% |
| **LINE MAN Ads** | Sponsored Listing ใน App | CTR > 5% |
| **Promotion Management** | Coupon, Flash Deal, Free Delivery | Orders +25% MoM |
| **LINE OA Integration** | เชื่อม Order ถึง LINE OA เพื่อ CRM | LINE Friends > 20K |
| **Rating & Review** | ตอบรีวิว ดูแล Reputation | Rating ≥ 4.7 ★ |

**LINE Ecosystem Synergy:**

```
ลูกค้าสั่งผ่าน LINE MAN
        │
        ▼
Auto-add เป็น LINE OA Friend
        │
        ├── ส่ง Order Confirmation + Tracking
        ├── หลังรับสินค้า: ขอ Review + ให้ Points
        └── 7 วันถัดมา: Recommend ผลิตภัณฑ์ถัดไป
```

**Tools:** LINE MAN Merchant Portal, LINE Official Account Manager, LINE Ads Platform

---

#### Sub-Agent D3 — Wongnai Food Merchant Agent

**Job Description:**
บริหารการปรากฏตัวของ Hibi Matcha บน Wongnai ทั้งในฐานะร้านอาหาร/คาเฟ่
และในฐานะแบรนด์สินค้า ให้มีรีวิวที่ดีและ Visibility สูง

**Job Role:** Wongnai Platform Manager & Community Builder

**Responsibilities:**

| งาน | รายละเอียด | KPI |
|-----|----------|-----|
| **Restaurant Profile** | ตั้งข้อมูลร้าน, เวลาเปิด, ที่อยู่, รูปภาพ | Profile Completeness 100% |
| **Menu Photos** | อัปโหลดรูปทุกเมนูด้วย Professional Photos | ทุก Item มีรูป |
| **Review Management** | ตอบรีวิวทุกข้อ, ขอบคุณรีวิวบวก, แก้ไขรีวิวลบ | Rating ≥ 4.5 ★ |
| **Wongnai Delivery** | บริหารออเดอร์ Delivery ผ่าน Wongnai | Order Accuracy 100% |
| **Wongnai Ads** | Sponsored Listing + Banner Ads | Impression +50K/เดือน |
| **Content on Wongnai** | โพสต์ News, Promotions, Events | 4 posts/เดือน |
| **Food Photography Brief** | ส่ง Brief รูปเมนูให้ Creative Agent | อัปเดตทุกไตรมาส |

**Wongnai Content Strategy:**

```
รีวิวจาก Micro-Influencer (Wongnai Top Reviewer)
        │
        ▼
Food Photography โดย Professional Photographer
        │
        ▼
Menu Description ที่ SEO-friendly บน Wongnai
        │
        ▼
Regular Promotion Posts (เทศกาล, Flash Deal)
        │
        ▼
Wongnai Pro Package สำหรับ Premium Placement
```

**Wongnai-Specific Features ที่ใช้:**
- **Wongnai for Business** — Analytics + Promotion tools
- **Wongnai Premier** — Featured Restaurant Listing
- **Menu Highlight** — Pin Best-seller ไว้ด้านบน
- **Special Offer Badge** — แสดงโปรโมชั่นพิเศษ

**Tools:** Wongnai Merchant Dashboard, Wongnai Partner App, Wongnai Ads Portal

---

### Food Delivery Agent — Integrated Media Strategy

Creative Assets ที่ต้องการจาก Creative Media Agent:

| Platform | Asset | Size | ความถี่ |
|---------|-------|------|--------|
| Grab | Store Banner | 1125×375px | รายเดือน |
| Grab | Menu Item Photos | 1200×900px | ทุกเมนูใหม่ |
| Grab | Promotion Banner | 1125×375px | รายสัปดาห์ |
| LINE MAN | Store Banner | 1200×400px | รายเดือน |
| LINE MAN | Menu Photos | 1200×900px | ทุกเมนูใหม่ |
| Wongnai | Cover Photo | 1200×628px | รายไตรมาส |
| Wongnai | Menu Photos | 1200×900px | ทุกเมนูใหม่ |
| Wongnai | Promotion Post | 1200×628px | 4/เดือน |

### Food Delivery Agent — Input → Output

```
INPUT:
  - Menu Updates จาก Product Team
  - Creative Assets จาก Creative Media Agent
  - Promotion Calendar จาก Orchestrator
  - Reviews & Ratings (Real-time)
  - Competitor Pricing จาก Analytics Team

OUTPUT:
  → Live Store Listings (Grab / LINE MAN / Wongnai)
  → Weekly GMV Report → Analytics Team
  → Review Escalation Alert (ถ้ามีรีวิว < 3 ดาว) → Orchestrator
  → Asset Request → Creative Media Agent
  → Best-seller Data → CRM Agent (สำหรับ Upsell)
```

### KPIs

| Platform | Metric | เป้าหมาย |
|---------|--------|---------|
| Grab | GMV/เดือน | 150,000 THB |
| Grab | Rating | ≥ 4.7 ★ |
| LINE MAN | GMV/เดือน | 100,000 THB |
| LINE MAN | New LINE Friends/เดือน | 500 คน |
| Wongnai | Rating | ≥ 4.5 ★ |
| Wongnai | Monthly Reviews | ≥ 50 รีวิว |
| **รวมทุก Platform** | **Total Delivery GMV** | **300,000 THB/เดือน** |

---

## 7. AGENT E — CRM Agent

### Job Title
**Customer Relationship Management Agent**
`agent-id: hibi-crm-agent`

### Mission
> รักษาและเพิ่มมูลค่าความสัมพันธ์กับลูกค้าทุกคน
> ตั้งแต่ First Touch จนถึง Brand Ambassador

### Sub-Agents ภายใต้

#### Sub-Agent E1 — Email Automation
- **Flows:** Welcome Series, Abandoned Cart (3 emails), Post-Purchase, Win-Back, Birthday
- **KPI:** Open Rate > 30%, Click Rate > 8%

#### Sub-Agent E2 — Loyalty Program Manager
- **หน้าที่:** บริหาร "Hibi Tea Club" — 4 Tiers (Seedling / Sprout / Brewer / Master)
- **KPI:** Repeat Purchase Rate > 35%, NPS > 50

### KPIs
- Customer Retention Rate > 40%
- Churn Rate < 5%/เดือน
- Email Open Rate > 30%
- NPS Score > 50

---

## 8. AGENT F — Growth Agent

### Job Title
**Growth Marketing & Acquisition Agent**
`agent-id: hibi-growth-agent`

### Mission
> ขับเคลื่อนการเติบโตของลูกค้าใหม่ผ่านช่องทางที่หลากหลาย
> ด้วย CAC ที่ต่ำที่สุด

### Sub-Agents ภายใต้

#### Sub-Agent F1 — Influencer Tracker
- ค้นหา คัดเลือก (Scorecard 5 มิติ) และติดตามผล KOL ทุกระดับ
- KPI: Influencer EMV > 200,000 THB/เดือน

#### Sub-Agent F2 — Campaign Manager
- บริหาร Referral Program, Marketplace Ads, Partnership
- KPI: Referral Signups > 50/เดือน, B2B 2 deals/ไตรมาส

### KPIs
- CAC < 350 THB
- New Customers: Q1=500, Q4=1,200
- ROAS > 4x (ร่วมกับ Media Buyer)

---

## 9. โครงสร้างทีมมนุษย์ที่อัปเดต (Updated Human Team)

```
CMO / Marketing Director
│
├── Creative Team (2–3 คน)
│   ├── Graphic Designer / Art Director
│   │   ├── FB + IG Design (Sub-Agent A1 Support)
│   │   └── Wongnai / Delivery Banner Design
│   ├── Video Editor / TikTok Creator
│   │   └── TikTok Content (Sub-Agent A2 Support)
│   └── Copywriter (ไทย + อังกฤษ)
│
├── Media Buyer Team (1–2 คน)
│   ├── Meta Ads Specialist (Sub-Agent B1 Support)
│   ├── TikTok Ads Specialist (Sub-Agent B2 Support)
│   └── Google Ads Specialist (Sub-Agent B3 Support)
│
├── Analytics Team (1–2 คน)
│   ├── Data Analyst (Sub-Agent C1/C3 Support)
│   └── CRO Specialist (Sub-Agent C2 Support)
│
├── Delivery Platform Manager (1 คน)
│   ├── Grab + LINE MAN + Wongnai (Sub-Agent D1/D2/D3 Support)
│   └── ประสานงาน Creative สำหรับ Platform Banners
│
└── CRM & Community Manager (1 คน)
    ├── Email + LINE OA (Sub-Agent E1 Support)
    └── Social Engagement + Influencer Coordination
```

---

## 10. RACI Matrix (อัปเดต)

| งาน | CMO | Creative Team | Media Buyer | Analytics | Delivery Mgr | CRM Mgr | AI Agent |
|-----|-----|--------------|-------------|-----------|-------------|---------|---------|
| Brand Strategy | **R/A** | C | C | C | I | I | Support |
| FB/IG Creative | A | **R** | C | I | I | I | Generate Draft |
| TikTok Creative | A | **R** | C | I | I | I | Script Draft |
| Meta Ads | A | C | **R** | C | I | I | Auto-optimize |
| TikTok Ads | A | C | **R** | C | I | I | Auto-optimize |
| Google Ads | A | I | **R** | C | I | I | Auto-optimize |
| Grab Store | A | C | I | I | **R** | I | Monitor |
| LINE MAN | A | C | I | I | **R** | C | Monitor |
| Wongnai | A | C | I | I | **R** | I | Monitor |
| Analytics Report | A | I | C | **R** | C | C | Auto-generate |
| Email/LINE | A | I | I | C | I | **R** | Auto-send |
| Influencer | A | C | C | C | I | **R** | Track & Score |

*R=Responsible, A=Accountable, C=Consulted, I=Informed*

---

## 11. Workflow: Food Delivery Campaign

```
Orchestrator กำหนด "Delivery Platform Campaign" (เช่น Songkran)
        │
        ▼
Creative Media Agent ออกแบบ Banner ทุก Platform (D-14)
  ├── Grab Banner 1125×375px
  ├── LINE MAN Banner 1200×400px
  └── Wongnai Cover 1200×628px
        │
        ▼
Food Delivery Agent ตั้ง Promotion บน 3 Platforms (D-7)
  ├── Grab: Flash Deal + Free Delivery
  ├── LINE MAN: Discount Voucher + LINE Points
  └── Wongnai: Featured Listing + Promotion Badge
        │
        ▼
Media Buyer Agent รัน Ads ใน Platform (D-day)
  ├── GrabAds Sponsored Listing
  └── LINE MAN Promoted Store
        │
        ▼
Analytics Team ติดตาม GMV Real-time
        │
        ▼
Campaign End: Analytics สรุป GMV, New Customers, Rating
        │
        ▼
Orchestrator + CMO รับ Post-Mortem Report
```

---

## 12. SLA อัปเดต (ครบทุก Agent)

| Agent | Task Type | Response Time | Completion Time |
|-------|-----------|--------------|----------------|
| Orchestrator | Strategic Brief | < 2 ชั่วโมง | < 4 ชั่วโมง |
| Creative — FB/IG | Static Post Design | < 2 ชั่วโมง | < 8 ชั่วโมง |
| Creative — TikTok | Video Script | < 2 ชั่วโมง | < 6 ชั่วโมง |
| Creative — Copy | Social Caption | < 1 ชั่วโมง | < 3 ชั่วโมง |
| Media Buyer | Campaign Launch | < 4 ชั่วโมง | < 24 ชั่วโมง |
| Media Buyer | Ad Optimization | Real-time | Continuous |
| Analytics | Daily Report | Auto 08:00 | สม่ำเสมอ |
| Analytics | Ad-hoc Analysis | < 2 ชั่วโมง | < 8 ชั่วโมง |
| Food Delivery | Review Response | < 2 ชั่วโมง | < 2 ชั่วโมง |
| Food Delivery | Menu Update | < 4 ชั่วโมง | < 24 ชั่วโมง |
| CRM | Email Flow | < 1 ชั่วโมง | < 12 ชั่วโมง |
| CRM | Crisis Comms | < 30 นาที | < 2 ชั่วโมง |
| Growth | Influencer Brief | < 4 ชั่วโมง | < 24 ชั่วโมง |

---

## 13. Tech Stack (อัปเดต)

```
┌──────────────────────────────────────────────────────────────────┐
│               HIBI MATCHA — FULL MARKETING TECH STACK            │
│                                                                  │
│  AI CORE                      CREATIVE TOOLS                     │
│  ├── Claude API (Anthropic)   ├── Figma                         │
│  ├── GPT-4 (backup)           ├── Adobe Creative Suite          │
│  └── Stable Diffusion (img)   ├── Canva Pro                     │
│                               └── CapCut                        │
│  PAID MEDIA                   DATA & ANALYTICS                   │
│  ├── Meta Ads Manager         ├── Google Analytics 4            │
│  ├── TikTok Ads Manager       ├── Looker Studio                 │
│  ├── Google Ads               ├── BigQuery                      │
│  └── LINE Ads Platform        ├── Hotjar                        │
│                               └── Python / Pandas               │
│  FOOD DELIVERY                CRM & COMMUNICATION                │
│  ├── Grab Merchant Portal     ├── Klaviyo (Email)               │
│  ├── GrabAds Dashboard        ├── LINE Messaging API            │
│  ├── LINE MAN Merchant        ├── Prisma ORM (Customer DB)      │
│  └── Wongnai Business         └── Zendesk (Support)            │
│                                                                  │
│  SCHEDULING & WORKFLOW        COMPETITIVE INTEL                  │
│  ├── Buffer / Hootsuite       ├── SEMrush                       │
│  ├── Notion (Planning)        ├── SimilarWeb                    │
│  └── Slack (Alerts)           └── Meta Ad Library               │
└──────────────────────────────────────────────────────────────────┘
```

---

## 14. OKRs รายไตรมาส (ครบทุก Agent)

| Agent | Objective | KR1 | KR2 | KR3 |
|-------|---------|-----|-----|-----|
| Orchestrator | ระบบอัตโนมัติ 80% | Deploy ครบ 30 วัน | Task Completion > 95% | Report ตรงเวลา 100% |
| Creative Media | Content คุณภาพสูงทุก Platform | IG Engagement > 5% | TikTok Watch Time > 50% | ผลิต 80 ชิ้น/เดือน |
| Media Buyer | ใช้งบให้ได้ ROAS สูงสุด | Overall ROAS > 4x | CAC < 350 THB | CTR > 2% |
| Analytics Team | ทุก Decision ใช้ข้อมูลจริง | Dashboard Uptime 99.9% | Forecast ±10% | A/B Tests ≥ 4/เดือน |
| Food Delivery | Delivery GMV 300K THB/เดือน | Grab Rating ≥ 4.7★ | LINE Friends +500/เดือน | Wongnai Reviews ≥ 50/เดือน |
| CRM | เพิ่ม CLV ทุกลูกค้า | Retention Rate > 40% | Email Open Rate > 30% | NPS > 50 |
| Growth | ลูกค้าใหม่ 500 คน Q1 | CAC < 350 THB | Influencer EMV > 200K | Referrals > 50/เดือน |

---

## 15. Escalation Protocol

```
LEVEL 1 — Agent Handle Automatically:
  ├── Routine content creation
  ├── Standard ad optimization
  ├── Delivery platform review responses
  └── Regular reporting

LEVEL 2 — Senior Agent Escalate to Orchestrator:
  ├── Budget reallocation > 10%
  ├── ROAS ต่ำกว่า 2x ต่อเนื่อง 3 วัน
  ├── Delivery Platform Rating ต่ำกว่า 4.0
  └── Unusual data anomaly

LEVEL 3 — Human + Agent Collaborate:
  ├── Brand crisis / Viral negative review
  ├── Major product launch
  ├── Budget decision > 100,000 THB
  └── Platform policy change (Grab/LINE MAN/Wongnai)

LEVEL 4 — CMO Decision Only:
  ├── Brand repositioning
  ├── Annual strategy pivot
  ├── Major partnership deal
  └── Crisis communication to media
```

---

*เอกสารนี้จัดทำโดย: ทีม Hibi Matcha*
*ปรับปรุงล่าสุด: มิถุนายน 2026 | เวอร์ชัน: 2.0*
