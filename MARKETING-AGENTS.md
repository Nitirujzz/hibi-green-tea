# Hibi Matcha — Marketing Department Agents & Sub-Agents
## โครงสร้างทีมการตลาดและ AI Agent Architecture

---

## 1. ภาพรวมโครงสร้าง (Organizational Overview)

```
                    ┌─────────────────────────────┐
                    │   Chief Marketing Officer   │
                    │     (CMO / Head of Mktg)    │
                    └──────────────┬──────────────┘
                                   │
              ┌────────────────────▼────────────────────┐
              │         MARKETING ORCHESTRATOR AGENT     │
              │         🤖 Hibi Marketing Brain          │
              └──┬──────────┬──────────┬──────────┬─────┘
                 │          │          │          │
         ┌───────▼──┐ ┌─────▼────┐ ┌──▼──────┐ ┌▼──────────┐
         │ CONTENT  │ │ANALYTICS │ │   CRM   │ │  GROWTH   │
         │  AGENT   │ │  AGENT   │ │  AGENT  │ │  AGENT    │
         └───┬──────┘ └────┬─────┘ └──┬──────┘ └────┬──────┘
             │             │          │              │
        ┌────▼────┐   ┌────▼────┐ ┌──▼──────┐ ┌────▼────┐
        │Social   │   │Report   │ │Email    │ │Influencer│
        │Media    │   │Builder  │ │Auto     │ │Tracker  │
        │Sub-Agent│   │Sub-Agent│ │Sub-Agent│ │Sub-Agent│
        └─────────┘   └─────────┘ └─────────┘ └─────────┘
        ┌────▼────┐   ┌────▼────┐ ┌──▼──────┐ ┌────▼────┐
        │SEO      │   │A/B Test │ │Loyalty  │ │Campaign │
        │Writer   │   │Sub-Agent│ │Sub-Agent│ │Manager  │
        │Sub-Agent│   └─────────┘ └─────────┘ │Sub-Agent│
        └─────────┘                            └─────────┘
```

---

## 2. ORCHESTRATOR AGENT — Hibi Marketing Brain

### Job Title
**Chief Marketing Orchestrator Agent (CMOA)**
`agent-id: hibi-marketing-brain`

### Mission Statement
> ประสานงานและควบคุม Sub-Agents ทุกตัวให้ทำงานอย่างสอดคล้องกัน
> เพื่อบรรลุเป้าหมายการตลาดของ Hibi Matcha

### Core Responsibilities

| ความรับผิดชอบ | รายละเอียด | ความถี่ |
|-------------|----------|--------|
| **Strategic Planning** | แปลงเป้าหมายธุรกิจเป็น Marketing Roadmap | รายสัปดาห์ |
| **Agent Coordination** | มอบหมายงานให้ Sub-Agents และติดตามผล | ทุกวัน |
| **Cross-Channel Sync** | ทำให้ Message ทุก Channel สอดคล้องกัน | ทุกวัน |
| **Executive Reporting** | สรุปผลการตลาดรายสัปดาห์/รายเดือนถึง CMO | รายสัปดาห์ |
| **Budget Oversight** | ตรวจสอบการใช้งบประมาณทุก Agent | รายสัปดาห์ |
| **Crisis Management** | รับมือเหตุการณ์ที่ส่งผลต่อ Brand | Real-time |

### Input → Output

```
INPUT:
  - Business Goals จาก CMO
  - Market Data จาก Analytics Agent
  - Customer Signals จาก CRM Agent
  - Trend Reports จาก Social Listening

OUTPUT:
  - Weekly Marketing Brief
  - Campaign Instructions → Sub-Agents
  - Executive Dashboard
  - Escalation Alerts
```

### Tools & Integrations
- **Google Analytics 4** — Traffic & Conversion data
- **Meta Business Suite** — Ad performance
- **Notion** — Planning & Documentation
- **Slack** — Internal alerts
- **LINE Official API** — Customer messaging

### KPIs ที่รับผิดชอบ
- Overall Marketing ROI > 300%
- Monthly Active Campaign count
- Inter-agent Task Completion Rate > 95%
- Time-to-Campaign-Launch < 48 hours

---

## 3. SUB-AGENT A — Content Agent

### Job Title
**Content Creation & Strategy Agent**
`agent-id: hibi-content-agent`

### Mission
> สร้าง Content คุณภาพสูงที่สื่อสาร Brand Story ของ Hibi Matcha
> ในทุก Platform อย่างสม่ำเสมอและน่าสนใจ

### Job Description

Content Agent รับผิดชอบการผลิต ตรวจสอบ และกำหนดตารางเนื้อหาทุกชิ้น
ตั้งแต่ Caption Instagram จนถึง Blog Article และ Email Newsletter
โดยมุ่งเน้น Storytelling ที่สะท้อนความ Authentic ของแบรนด์

### Responsibilities

```
┌─────────────────────────────────────────────────────────┐
│  DAILY TASKS                                            │
│  ├── สร้าง 2–3 posts สำหรับ Social Media               │
│  ├── ตอบ Comment / DM template ให้ CS Team             │
│  └── Monitor Brand Mentions & UGC                       │
│                                                         │
│  WEEKLY TASKS                                           │
│  ├── จัดทำ Content Calendar สัปดาห์ถัดไป               │
│  ├── เขียน Blog Article 1 ชิ้น (SEO-optimized)         │
│  ├── Email Newsletter รายสัปดาห์                        │
│  └── รายงาน Content Performance ถึง Orchestrator        │
│                                                         │
│  MONTHLY TASKS                                          │
│  ├── Campaign Creative Brief                            │
│  ├── Content Audit & Refresh                            │
│  └── Brand Voice Consistency Review                     │
└─────────────────────────────────────────────────────────┘
```

### Sub-Agents ภายใต้

#### Sub-Agent A1 — Social Media Writer
- **Platform เชี่ยวชาญ:** Instagram, TikTok, Facebook, X
- **Output:** Captions, Hashtags, Stories scripts, Reel scripts
- **Tone:** Japanese-inspired, Warm, Educational
- **Daily Quota:** 3 Instagram posts, 1 TikTok script, 2 Stories

#### Sub-Agent A2 — SEO Content Writer
- **ความเชี่ยวชาญ:** Long-form articles, Product descriptions, Meta tags
- **Output:** Blog posts (800–2000 words), Product copy, FAQ pages
- **Target Keywords:** Matcha ไทย, ชาเขียวญี่ปุ่น, วิธีชงมัทฉะ
- **Weekly Quota:** 2 blog articles, 5 product descriptions

### Input → Output

```
INPUT:
  - Brand Guidelines จาก HIBI-BRAND-GUIDE.md
  - Campaign Brief จาก Orchestrator
  - Trending Topics จาก Analytics Agent
  - Product Info จาก Product Database

OUTPUT:
  → Social Posts (IG, TikTok, FB, X)
  → Blog Articles
  → Email Newsletters
  → Ad Copy
  → Product Descriptions
```

### Tools
- **Canva API** — Image template generation
- **ChatGPT / Claude API** — Draft generation
- **Grammarly** — Thai/English grammar
- **Buffer / Hootsuite** — Scheduling
- **SEMrush** — Keyword research

### KPIs
- Content Engagement Rate > 5%
- Blog Organic Traffic Growth > 20% MoM
- Email Open Rate > 30%
- Content Production: 40 pieces/เดือน

---

## 4. SUB-AGENT B — Analytics Agent

### Job Title
**Data Analytics & Insights Agent**
`agent-id: hibi-analytics-agent`

### Mission
> แปลงข้อมูลดิบให้เป็น Insights ที่นำไปปฏิบัติได้
> เพื่อช่วยให้ทุก Agent ตัดสินใจบนพื้นฐานข้อมูล

### Job Description

Analytics Agent ทำหน้าที่เป็น "สมองวิเคราะห์" ของแผนก รวบรวมข้อมูลจาก
ทุก Touch Point และแปลงเป็น Dashboard, Report, และ Recommendation
ที่ Agents อื่นสามารถนำไปใช้ได้ทันที

### Responsibilities

| งาน | รายละเอียด | Output |
|-----|----------|--------|
| **Performance Tracking** | ติดตาม KPI ทุก Channel แบบ Real-time | Live Dashboard |
| **Funnel Analysis** | วิเคราะห์ Customer Journey จาก Awareness → Purchase | Funnel Report |
| **Competitor Monitoring** | ติดตามคู่แข่งทุกสัปดาห์ | Competitive Intel |
| **Trend Detection** | จับเทรนด์ก่อนเพื่อนบน Social Media | Trend Alert |
| **ROI Attribution** | ระบุว่าช่องทางไหนให้ผลตอบแทนที่สุด | Attribution Report |
| **Predictive Modeling** | พยากรณ์ยอดขายรายเดือน | Forecast Model |

### Sub-Agents ภายใต้

#### Sub-Agent B1 — Report Builder
- **หน้าที่:** สร้าง Automated Reports รายวัน/รายสัปดาห์/รายเดือน
- **Output:** Executive Summary, Channel Performance, Budget Utilization
- **Delivery:** ส่งรายงานถึง Orchestrator ทุก จันทร์ 08:00

#### Sub-Agent B2 — A/B Test Manager
- **หน้าที่:** ออกแบบ ติดตาม และสรุปผล A/B Tests
- **ทดสอบ:** Email Subject Lines, Ad Creatives, Landing Pages, CTAs
- **Output:** Test Results + Statistical Significance + Recommendation

### Input → Output

```
INPUT:
  - GA4 Data
  - Meta Ads API
  - Shopee/Lazada Seller Center
  - LINE OA Analytics
  - Stripe Payment Data
  - CRM Data

OUTPUT:
  → Weekly Performance Dashboard
  → Monthly Executive Report
  → Campaign ROI Analysis
  → Audience Insights
  → Trend Alerts (Real-time)
  → A/B Test Recommendations
```

### Tools
- **Google Analytics 4** — Web & App analytics
- **Looker Studio** — Dashboard visualization
- **Meta Ads Manager API** — Ad performance
- **Hotjar** — Heatmaps & User behavior
- **Python/Pandas** — Data processing
- **BigQuery** — Data warehouse

### KPIs
- Dashboard Accuracy: 99.5%
- Report Delivery On-time: 100%
- Insights Acted Upon: > 80%
- A/B Tests per Month: ≥ 4

---

## 5. SUB-AGENT C — CRM Agent

### Job Title
**Customer Relationship Management Agent**
`agent-id: hibi-crm-agent`

### Mission
> รักษาและเพิ่มมูลค่าความสัมพันธ์กับลูกค้าทุกคน
> ตั้งแต่ First Touch จนถึง Brand Ambassador

### Job Description

CRM Agent ดูแลความสัมพันธ์กับลูกค้าทุกระยะของ Lifecycle
โดยใช้ข้อมูลจาก Analytics Agent เพื่อ Personalize การสื่อสาร
และเพิ่ม Lifetime Value ของลูกค้าแต่ละราย

### Responsibilities

```
CUSTOMER LIFECYCLE MANAGEMENT:

New Customer                Loyal Customer             VIP / Ambassador
     │                           │                           │
     ▼                           ▼                           ▼
Welcome Series           Retention Campaign           VIP Program
Onboarding Email         Re-engagement Flow           Exclusive Access
First Purchase           Upsell / Cross-sell          Referral Bonus
Review Request           Loyalty Points               Co-creation
     │                           │                           │
     └───────────────────────────┴───────────────────────────┘
                                 │
                         CRM Agent Oversees All
```

### Sub-Agents ภายใต้

#### Sub-Agent C1 — Email Automation
- **หน้าที่:** ออกแบบและบริหาร Email Flows ทั้งหมด
- **Flows ที่ดูแล:**
  - Welcome Series (5 emails, 14 วัน)
  - Abandoned Cart Recovery (3 emails, 24 ชั่วโมง)
  - Post-Purchase Flow (Review + Upsell)
  - Win-Back Campaign (Inactive > 60 วัน)
  - Birthday / Anniversary Emails
- **Output:** Personalized emails ส่งถึงลูกค้าถูกคนถูกเวลา

#### Sub-Agent C2 — Loyalty Program Manager
- **หน้าที่:** บริหาร "Hibi Tea Club" Loyalty Program
- **รับผิดชอบ:**
  - จัดการ Point Accumulation & Redemption
  - Tier Upgrades & Notifications
  - Exclusive Member Benefits Coordination
  - Monthly Loyalty Performance Report

### Input → Output

```
INPUT:
  - Customer Purchase History (Prisma DB)
  - Email Behavior (Open/Click data)
  - Loyalty Points Balance
  - Customer Service History
  - Segment Data จาก Analytics Agent

OUTPUT:
  → Personalized Email Campaigns
  → LINE Push Notifications
  → Loyalty Program Updates
  → Customer Segment Reports
  → Churn Risk Alerts
  → VIP Customer List → Event Agent
```

### Tools
- **Klaviyo / Mailchimp** — Email automation
- **LINE Messaging API** — Push notifications
- **Prisma ORM** — Customer database queries
- **Segment.io** — Customer data platform
- **Zendesk** — Customer service integration

### KPIs
- Email Open Rate > 30%
- Customer Retention Rate > 40%
- Repeat Purchase Rate > 35% (Month 12)
- Churn Rate < 5%/เดือน
- Net Promoter Score (NPS) > 50

---

## 6. SUB-AGENT D — Growth Agent

### Job Title
**Growth Marketing & Acquisition Agent**
`agent-id: hibi-growth-agent`

### Mission
> ขับเคลื่อนการเติบโตของลูกค้าใหม่ผ่านช่องทางที่หลากหลาย
> ด้วยต้นทุนต่อการได้มา (CAC) ที่ต่ำที่สุด

### Job Description

Growth Agent รับผิดชอบทุกกิจกรรมที่เกี่ยวกับการหาลูกค้าใหม่
ตั้งแต่ Paid Advertising, Influencer Marketing, Referral Programs
ไปจนถึง Partnership และ B2B Outreach

### Responsibilities

| หมวด | งาน | KPI |
|------|-----|-----|
| **Paid Ads** | บริหาร Google, Meta, TikTok, LINE Ads | ROAS > 4x |
| **Influencer** | Identify, Brief, Track, Report Influencers | EMV > 200K/เดือน |
| **Referral** | บริหาร Referral Program | 50 referrals/เดือน |
| **Partnership** | B2B outreach + Collaboration brands | 2 deals/ไตรมาส |
| **Marketplace** | Shopee/Lazada optimization + Flash Sales | Top 10 Category |
| **Events** | Coordinate Pop-ups + Market participation | 4 events/ปี |

### Sub-Agents ภายใต้

#### Sub-Agent D1 — Influencer Tracker
- **หน้าที่:** ค้นหา คัดเลือก และติดตามผล Influencer Collaborations
- **กระบวนการ:**
  1. **Discover** — สแกน Instagram, TikTok หา KOL ใหม่ทุกสัปดาห์
  2. **Evaluate** — ตรวจสอบ Engagement Rate, Audience Quality, Brand Fit
  3. **Brief** — ส่ง Campaign Brief + Product ให้ Influencer
  4. **Monitor** — ติดตามโพสต์ผ่าน Tracking Links
  5. **Report** — สรุป Reach, Impression, Conversion ทุกแคมเปญ
- **Scorecard ประเมิน KOL:**

```
INFLUENCER SCORECARD
├── Engagement Rate (30%) — เป้า > 3%
├── Audience Authenticity (25%) — ตรวจ Fake Followers
├── Content Quality (20%) — Aesthetic ตรงแบรนด์
├── Audience Demographics (15%) — Thai, 18–40 ปี
└── Past Campaign Performance (10%) — Conversion history
```

#### Sub-Agent D2 — Campaign Manager
- **หน้าที่:** บริหาร Paid Advertising ทุก Platform
- **รับผิดชอบ:**
  - Media Planning & Budget Allocation
  - Ad Creative Briefing → Content Agent
  - Campaign Launch & Optimization
  - Weekly Performance Review
  - Monthly Budget Reconciliation

**Campaign Types ที่บริหาร:**

```
AWARENESS         CONSIDERATION        CONVERSION
   │                    │                   │
Brand Video          Product Demo        Dynamic Product Ads
Reach Campaigns      Blog Promotion      Cart Abandonment
Hashtag Trends       Review Ads          Flash Sale Ads
   │                    │                   │
TikTok TopView    IG Story Swipe-up    Google Shopping
Meta Brand Lift   YouTube Pre-roll     META Retargeting
```

### Input → Output

```
INPUT:
  - Budget Approval จาก Orchestrator
  - Audience Segments จาก Analytics Agent
  - Content Assets จาก Content Agent
  - Product Launch Calendar
  - Competitor Intelligence

OUTPUT:
  → Live Ad Campaigns (Google/Meta/TikTok)
  → Influencer Campaign Reports
  → Referral Program Status
  → Growth Forecast
  → Weekly Spend Report
  → B2B Lead List → Sales Team
```

### Tools
- **Google Ads API** — Search & Shopping campaigns
- **Meta Ads Manager** — FB & IG advertising
- **TikTok Ads Manager** — Short-video ads
- **Influencer.co / Heepsy** — KOL discovery
- **Shopee Ads Portal** — Marketplace advertising
- **Notion** — Campaign tracking

### KPIs
- Customer Acquisition Cost (CAC) < 350 THB
- ROAS (Return on Ad Spend) > 4x
- New Customers/Month: Q1=500, Q4=1,200
- Influencer EMV > 200,000 THB/เดือน
- Referral Signups > 50/เดือน

---

## 7. โครงสร้างทีมมนุษย์ (Human Team Structure)

### 7.1 ตำแหน่งและความรับผิดชอบหลัก

```
CMO / Marketing Manager
│
├── Content Creator (1–2 คน)
│   ├── Photography & Videography
│   ├── Graphic Design (Canva/Figma)
│   └── Copywriting (ไทย + อังกฤษ)
│
├── Digital Marketing Specialist (1 คน)
│   ├── Paid Ads Management
│   ├── SEO Implementation
│   └── Email Marketing
│
├── Community Manager (1 คน)
│   ├── Social Media Posting & Engagement
│   ├── Influencer Coordination
│   └── Customer Service (Line/IG DM)
│
└── Data Analyst (Part-time / AI-assisted)
    ├── Performance Reporting
    ├── Dashboard Maintenance
    └── Insight Generation
```

### 7.2 RACI Matrix — ความรับผิดชอบต่อ AI Agents

| งาน | CMO | Content Creator | Digital Specialist | Community Mgr | AI Agent |
|-----|-----|----------------|-------------------|---------------|---------|
| กำหนดกลยุทธ์ | **R/A** | C | C | I | Support |
| สร้าง Content | I | **R/A** | C | C | Generate Draft |
| บริหาร Ads | A | I | **R** | I | Optimize |
| ดูแล Community | I | C | I | **R/A** | Auto-reply Draft |
| วิเคราะห์ข้อมูล | A | I | R | I | **Auto-generate** |
| Email/LINE | A | C | **R** | I | **Auto-send** |
| Influencer | A | C | C | **R** | Track & Score |

*R=Responsible, A=Accountable, C=Consulted, I=Informed*

---

## 8. Workflow อัตโนมัติ (Automation Workflows)

### Workflow 1: New Product Launch

```
CMO อนุมัติ Product Launch
        │
        ▼
Orchestrator Agent สร้าง Launch Brief
        │
        ├──► Content Agent: สร้าง 30 posts + Blog + Email
        ├──► Analytics Agent: ตั้ง Tracking & UTM
        ├──► CRM Agent: สร้าง Announcement Email Flow
        └──► Growth Agent: ตั้ง Ad Campaigns + Brief Influencers
                │
                ▼
        Launch Day — ทุก Agent ทำงานพร้อมกัน
                │
                ▼
        Day 7 — Analytics Agent รายงานผล
                │
                ▼
        Orchestrator สรุปถึง CMO + ปรับกลยุทธ์
```

### Workflow 2: Customer Win-Back

```
Analytics Agent ตรวจพบลูกค้าไม่ซื้อ > 60 วัน
        │
        ▼
CRM Agent รับ Segment → Email Win-Back Series
        │
        ├── Email 1 (Day 0): "We miss you" + 10% Off
        ├── Email 2 (Day 7): Best Sellers + Review
        └── Email 3 (Day 14): Last Chance + 15% Off
        │
        ▼
Analytics Agent ติดตาม Re-conversion Rate
        │
        ▼
Orchestrator รับ Report — Adjust Discount Strategy
```

### Workflow 3: Influencer Campaign Cycle

```
Growth Agent (Influencer Tracker) สแกน KOL ใหม่ (ทุกจันทร์)
        │
        ▼
ประเมิน Scorecard → เลือก Top 5
        │
        ▼
Content Agent เตรียม Campaign Brief + Talking Points
        │
        ▼
Community Manager ส่ง Brief + สินค้า → Influencer
        │
        ▼
Influencer โพสต์ Content (D+7–14)
        │
        ▼
Growth Agent ติดตาม Tracking Link + Mentions
        │
        ▼
Analytics Agent สร้าง Campaign ROI Report (D+30)
        │
        ▼
Orchestrator ตัดสินใจ: ทำแคมเปญต่อ หรือ เปลี่ยน KOL
```

---

## 9. SLA (Service Level Agreement) ของแต่ละ Agent

| Agent | Task Type | Response Time | Completion Time |
|-------|-----------|--------------|----------------|
| Orchestrator | Strategic Brief | < 2 ชั่วโมง | < 4 ชั่วโมง |
| Content Agent | Social Post | < 1 ชั่วโมง | < 3 ชั่วโมง |
| Content Agent | Blog Article | < 4 ชั่วโมง | < 24 ชั่วโมง |
| Analytics Agent | Daily Report | Auto 08:00 | สม่ำเสมอ |
| Analytics Agent | Ad-hoc Analysis | < 2 ชั่วโมง | < 8 ชั่วโมง |
| CRM Agent | Email Flow | < 1 ชั่วโมง | < 12 ชั่วโมง |
| CRM Agent | Crisis Communication | < 30 นาที | < 2 ชั่วโมง |
| Growth Agent | Ad Optimization | Real-time | Continuous |
| Growth Agent | Influencer Brief | < 4 ชั่วโมง | < 24 ชั่วโมง |

---

## 10. เครื่องมือและการเชื่อมต่อ (Tech Stack & Integrations)

```
┌──────────────────────────────────────────────────────────────┐
│                   HIBI MATCHA MARKETING STACK                │
│                                                              │
│  AI CORE                  DATA LAYER                         │
│  ├── Claude API (Anthropic)  ├── GA4                        │
│  ├── GPT-4 (backup)          ├── Prisma DB (PostgreSQL)     │
│  └── Stable Diffusion        └── BigQuery                   │
│                                                              │
│  COMMUNICATION               COMMERCE                        │
│  ├── LINE Messaging API      ├── Stripe API                 │
│  ├── Klaviyo (Email)         ├── Shopee Seller API          │
│  ├── Meta Graph API          ├── Lazada Open Platform       │
│  └── TikTok API              └── Next.js e-commerce         │
│                                                              │
│  CONTENT                     ANALYTICS                       │
│  ├── Canva API               ├── Looker Studio              │
│  ├── Buffer (Scheduling)     ├── Hotjar                     │
│  ├── SEMrush                 ├── Meta Pixel                 │
│  └── Grammarly API           └── Google Search Console     │
└──────────────────────────────────────────────────────────────┘
```

---

## 11. OKRs ของแต่ละ Agent (ไตรมาส 1)

### Orchestrator Agent
- **O:** สร้างระบบการตลาดที่ทำงานได้อัตโนมัติ 80%
- **KR1:** Deploy ครบทุก Sub-Agent ภายใน 30 วัน
- **KR2:** Inter-agent Task Completion > 95%
- **KR3:** Executive Report ตรงเวลา 100%

### Content Agent
- **O:** สร้าง Content ที่ engage ผู้ชมทุก Platform
- **KR1:** Engagement Rate > 5% บน Instagram
- **KR2:** Blog Traffic เพิ่ม 20% MoM
- **KR3:** ผลิต Content 40 ชิ้น/เดือน ตรงเวลา

### Analytics Agent
- **O:** ทำให้ทุก Decision ใช้ข้อมูลจริง
- **KR1:** Live Dashboard ใช้งานได้ 99.9% uptime
- **KR2:** Trend Alert ล่วงหน้า > 48 ชั่วโมง
- **KR3:** A/B Tests ≥ 4 ครั้ง/เดือน

### CRM Agent
- **O:** เพิ่ม Customer Lifetime Value ให้ทุกคน
- **KR1:** Email Open Rate > 30%
- **KR2:** Repeat Purchase Rate > 25%
- **KR3:** NPS Score > 45

### Growth Agent
- **O:** ได้ลูกค้าใหม่ 500 คนใน Q1
- **KR1:** CAC < 350 THB
- **KR2:** ROAS > 4x
- **KR3:** Influencer EMV > 200,000 THB/เดือน

---

## 12. Escalation Protocol

```
LEVEL 1 (Sub-Agent Handle):
  - Routine content creation
  - Standard email campaigns
  - Regular reporting
  - Normal ad optimization

LEVEL 2 (Main Agent Handle):
  - Budget reallocation > 10%
  - Campaign underperformance
  - KOL conflict/issue
  - Unusual data anomaly

LEVEL 3 (Human + Agent Collaborate):
  - Brand crisis / PR issue
  - Major product launch
  - Budget > 100,000 THB decision
  - New channel/strategy exploration

LEVEL 4 (CMO Decision Only):
  - Brand positioning change
  - Annual strategy pivot
  - Major partnership deal
  - Crisis communication to press
```

---

*เอกสารนี้จัดทำโดย: ทีม Hibi Matcha*
*ปรับปรุงล่าสุด: มิถุนายน 2026 | เวอร์ชัน: 1.0*
