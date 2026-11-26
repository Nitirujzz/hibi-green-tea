"""KOL recruitment carousel (3 × 1080x1350) + story (1080x1920): Higgsfield art + HTML text -> Chromium screenshots."""
import subprocess, os
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__)); A=os.path.abspath(f"{D}/../art"); O=os.path.abspath(f"{D}/../out")
FONTS=open("/root/.fonts/extra/cormorant_local.css").read()+"".join(
  f"@font-face{{font-family:'Prompt';font-weight:{w};src:url('file:///root/.fonts/Prompt-{w}-thai.woff2') format('woff2');unicode-range:U+0E00-0E7F;}}"
  f"@font-face{{font-family:'Prompt';font-weight:{w};src:url('file:///root/.fonts/Prompt-{w}-latin.woff2') format('woff2');unicode-range:U+0000-0DFF,U+0E80-FFFF;}}" for w in (400,500,600,700))
BASE="""*{margin:0;padding:0;box-sizing:border-box} body{position:relative;width:WWpx;height:HHpx;overflow:hidden;font-family:Prompt;color:#243e1b;background:#f6f1e6 center/cover no-repeat}
.tag{display:inline-block;font-family:'Cormorant Garamond';font-size:30px;letter-spacing:5px;color:#fff;background:#4e7c3a;padding:6px 26px;border-radius:30px}
.brand{position:absolute;font-family:'Cormorant Garamond';font-size:30px;letter-spacing:7px;color:#4e7c3a}
.serif{font-family:'Cormorant Garamond';font-style:italic;font-weight:400}
.card{background:rgba(255,252,244,.93);border-radius:30px;box-shadow:0 10px 30px rgba(60,90,40,.12)}
h2{font-weight:700;font-size:44px;display:flex;align-items:center;gap:12px} h2 i{font-family:'Cormorant Garamond';font-style:italic;font-weight:400;color:#4e7c3a;font-size:46px}
ul{list-style:none} li{font-size:31px;line-height:1.45;padding-left:44px;position:relative;margin-top:8px} li:before{content:'';position:absolute;left:6px;top:17px;width:16px;height:16px;border-radius:50%;background:#a8d48a;box-shadow:0 0 0 4px #e3f0d6}
.small{font-size:26px;color:#6b6a55}
"""
def page(name,w,h,bg,body):
    css=FONTS+BASE.replace("WW",str(w)).replace("HH",str(h))
    p=f"{O}/{name}.html"
    open(p,"w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{css} body{{background-image:url('file://{A}/{bg}')}}</style></head><body>{body}</body></html>")
    subprocess.run(["/opt/pw-browsers/chromium","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--allow-file-access-from-files",
        "--virtual-time-budget=5000",f"--screenshot={O}/{name}_raw.png",f"--window-size={w},{h+150}","file://"+p],check=True,capture_output=True)
    Image.open(f"{O}/{name}_raw.png").crop((0,0,w,h)).convert("RGB").save(f"{O}/{name}.jpg",quality=93); os.remove(f"{O}/{name}_raw.png"); os.remove(p)
# 1 · cover
page("kol_01_cover",1080,1350,"bg1.png",'''
<div style="position:absolute;left:0;right:0;top:70px;text-align:center">
 <span class="tag">CREATOR CALL · DEC 2026</span>
 <div class="serif" style="font-size:140px;line-height:1;margin-top:34px;color:#243e1b">Matcha Friends</div>
 <div style="font-weight:700;font-size:62px;letter-spacing:14px;color:#4e7c3a;margin-top:2px">WANTED</div>
 <div style="font-weight:600;font-size:46px;margin-top:26px">Hibi กับ Capy ชวนครีเอเตอร์<br>มาส่งท้ายปีด้วยกัน 🎄</div>
 <div style="font-size:30px;color:#4e7c3a;margin-top:10px">สายคาเฟ่มัทฉะ · สายขนม · Lifestyle</div>
</div>
<div style="position:absolute;right:46px;bottom:44px;font-size:28px;color:#fff;background:rgba(36,62,27,.78);padding:10px 26px;border-radius:30px">ปัดดูรายละเอียด →</div>
<div class="brand" style="left:50px;bottom:52px;color:#fff;text-shadow:0 2px 10px rgba(0,0,0,.35)">HIBI MATCHA CAFE</div>''')
# 2 · what you get / what we want  (Hibi bottom-right)
page("kol_02_details",1080,1350,"bg2.png",'''
<div class="brand" style="left:70px;top:60px">HIBI MATCHA CAFE · 2/3</div>
<div class="card" style="position:absolute;left:60px;top:130px;width:700px;padding:34px 38px">
 <h2>🌿 เราดูแลคุณ <i>— perks</i></h2>
 <ul><li>เครื่องดื่มมัทฉะ + ขนม 1 เซต</li><li>ค่าตอบแทนตามขนาดช่อง</li><li>เลือกถ่ายได้ทุกสาขา (5 สาขา)</li></ul></div>
<div class="card" style="position:absolute;left:60px;top:560px;width:600px;padding:34px 38px">
 <h2>🎬 อยากได้ <i>— brief</i></h2>
 <ul><li>คลิปแนวตั้ง ~60 วิ · 1 คลิป<br><span class="small">เล่าในสไตล์ของคุณเอง</span></li>
 <li>ลงได้หลายแพลตฟอร์ม<br><span class="small" style="white-space:nowrap">มี Lemon8 / RedNote = พิจารณาพิเศษ</span></li>
 <li>โพสต์ภายใน 3–5 วันหลังถ่าย<br><span class="small">แท็ก @hibimatchacafe</span></li></ul>
 <div style="margin-top:18px;font-size:27px;color:#4e7c3a;line-height:1.45">💡 ไอเดียตั้งต้น: โมเมนต์เล็ก ๆ กับคนสำคัญ ·<br>“1 แก้ว หลายมุม” · ของขวัญให้ตัวเอง</div></div>''')
# 3 · budget / timeline / apply  (Capy bottom-left)
tiers=[("Micro","10K–50K","500.-"),("Mid","50K–100K","1,000.-"),("Rising","100K–250K","1,500.-"),("Macro","250K–500K","2,500.-"),("500K+","","คุยกันรายคน")]
tier="".join(f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:12px 4px;border-bottom:2px dashed #dfe8d2"><span><b class="serif" style="font-size:42px;color:#4e7c3a">{a}</b> <span style="font-size:27px;color:#6b6a55">{b}</span></span><b style="font-size:34px">{c}</b></div>' for a,b,c in tiers)
page("kol_03_apply",1080,1350,"bg3.png",f'''
<div class="brand" style="left:70px;top:60px">HIBI MATCHA CAFE · 3/3</div>
<div class="card" style="position:absolute;left:60px;right:60px;top:125px;padding:30px 40px">
 <h2>💚 ค่าตอบแทน <i>— rates</i></h2>{tier}
 <div class="small" style="margin-top:12px">*เราดูความเข้ากันของสไตล์คอนเทนต์ ไม่ใช่แค่ยอดผู้ติดตาม</div></div>
<div class="card" style="position:absolute;left:470px;right:60px;top:790px;padding:28px 34px">
 <h2 style="font-size:38px">🗓️ ไทม์ไลน์</h2>
 <div style="font-size:28px;line-height:1.6;margin-top:6px">ส่งใบสมัครถึง <b>30 พ.ย.</b><br>แจ้งผลภายใน <b>5 ธ.ค.</b><br>ถ่ายทำ <b>10–15 ธ.ค. 69</b></div>
 <div style="margin-top:16px;padding-top:14px;border-top:2px dashed #dfe8d2;font-size:28px;line-height:1.5"><b>📩 สมัคร:</b> DM / คอมเมนต์<br>ชื่อ + ลิงก์ช่อง · ยอดผู้ติดตาม<br>+ คลิปที่ภูมิใจที่สุด 1 คลิป</div></div>''')
# story 9:16
page("kol_story",1080,1920,"bg_story.png",'''
<div style="position:absolute;left:0;right:0;top:220px;text-align:center">
 <span class="tag">CREATOR CALL · DEC 2026</span>
 <div class="serif" style="font-size:150px;line-height:1;margin-top:30px">Matcha Friends</div>
 <div style="font-weight:700;font-size:60px;letter-spacing:14px;color:#4e7c3a">WANTED</div>
 <div style="font-weight:600;font-size:46px;margin-top:22px">Hibi กับ Capy ชวนครีเอเตอร์<br>มาส่งท้ายปีด้วยกัน 🎄</div>
 <div class="card" style="display:inline-block;margin-top:34px;padding:24px 40px;text-align:left;font-size:40px;line-height:1.6">
  🍵 มัทฉะ + ขนม 1 เซต + ค่าตอบแทน<br>🎬 คลิปแนวตั้ง ~60 วิ · ถ่าย 10–15 ธ.ค.<br>📩 สมัครถึง 30 พ.ย. · DM @hibimatchacafe</div>
</div>
<div class="brand" style="left:0;right:0;text-align:center;bottom:70px;color:#fff;text-shadow:0 2px 10px rgba(0,0,0,.35)">HIBI MATCHA CAFE</div>''')
print("ok")
