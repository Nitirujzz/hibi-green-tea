"""Storyboard pages for 'Matcha Honey Lemon · Hibi & Capy' (HTML -> Chromium screenshot)."""
import subprocess, os, sys
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__)); F=f"{D}/../frames"; O=f"{D}/../storyboard"
CH="/home/user/hibi-green-tea/docs/content-plan/campaigns/mbti-carousel/characters"
W,H=2400,1320
FONTS="".join(f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('file:///root/.fonts/{f}-{w}-{s}.woff2') format('woff2');}}"
  for fam,f in [("Prompt","Prompt"),("Plex","IBMPlexSansThai")] for w in ([400,500,600,700] if f=="Prompt" else [400,600]) for s in ["thai","latin"])
CSS=FONTS+f"""*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;font-family:'Plex';color:#3b3a2e;
 background:radial-gradient(circle at 12% 8%,#fff6cf 0,transparent 32%),radial-gradient(circle at 92% 96%,#ffe3ea 0,transparent 30%),#fffaf0}}
.hd{{position:absolute;left:80px;right:80px;top:48px;height:96px;display:flex;align-items:center;justify-content:space-between;border-bottom:3px dashed #e8dcb8}}
.hd h1{{font-family:'Prompt';font-weight:700;font-size:46px;color:#243e1b}} .hd h1 span{{color:#e0a800}}
.hd .meta{{font-size:24px;color:#6b6a55;text-align:right;line-height:1.35}}
.pill{{display:inline-block;padding:4px 16px;border-radius:30px;background:#243e1b;color:#fff;font-weight:600;font-size:20px;margin-left:8px}}
.row{{position:absolute;left:80px;right:80px;top:180px;display:flex;gap:30px}}
.p{{flex:1;background:#fff;border-radius:26px;box-shadow:0 10px 26px rgba(120,100,40,.13);overflow:hidden;display:flex;flex-direction:column}}
.p .im{{position:relative;width:100%;aspect-ratio:9/16;background:#eee center/cover no-repeat}}
.p .no{{position:absolute;left:14px;top:14px;background:#ffd23f;color:#3a2a00;font-family:'Prompt';font-weight:700;font-size:28px;padding:4px 16px;border-radius:16px;box-shadow:0 4px 10px rgba(0,0,0,.18)}}
.p .tc{{position:absolute;right:14px;top:14px;background:rgba(36,62,27,.85);color:#fff;font-weight:600;font-size:20px;padding:6px 14px;border-radius:14px}}
.p .ost{{position:absolute;left:50%;bottom:16%;transform:translateX(-50%);white-space:nowrap;background:rgba(255,252,244,.94);color:#243e1b;font-family:'Prompt';font-weight:700;font-size:22px;padding:8px 16px;border-radius:16px;box-shadow:0 6px 14px rgba(0,0,0,.18)}}
.p .tx{{padding:18px 20px 20px;font-size:22px;line-height:1.45}}
.p .tt{{font-family:'Prompt';font-weight:700;font-size:30px;color:#243e1b;margin-bottom:6px}}
.k{{display:flex;gap:8px;margin-top:5px}} .k b{{flex:none;width:30px;text-align:center}} 
.ft{{position:absolute;left:80px;right:80px;bottom:34px;display:flex;justify-content:space-between;font-size:20px;color:#9a9578}}
"""
SH=[ # no, timecode, title, action, camera, sound, on-screen text
 (1,"0:00–0:03","เก็บเลมอนจากต้น","Hibi เดินถือตะกร้าในสวนเลมอนยามเช้า เขย่งเก็บเลมอนลูกเหลืองสด","มุมต่ำ ไล่ขึ้นตามมือ · push-in ช้า","นกร้อง · ใบไม้ไหว · “ป๊อก” ตอนเด็ด","เริ่มจากต้น 🍋"),
 (2,"0:03–0:06","สไลซ์บาง ๆ","Hibi ตั้งใจสไลซ์เลมอนเป็นแผ่นบางใส น้ำเลมอนกระเซ็นเป็นประกาย","Close-up มือ+มีด · slow-mo ตอนแผ่นล้ม","ASMR มีดหั่น “ฉึบ ฉึบ”","สไลซ์บาง ๆ"),
 (3,"0:06–0:09","Capy ไปเก็บน้ำผึ้งสด","Capy ภูมิใจถือโหลน้ำผึ้งทองในทุ่งดอกไม้ ผึ้งน้อยบินรอบพร้อมหัวใจ","Pan จากผึ้ง → Capy · ซูมเข้าหน้า","ผึ้งบินเสียงน่ารัก · ระฆังเล็ก","น้ำผึ้งสดจาก Capy 🍯"),
 (4,"0:09–0:11","ส่งต่อด้วยความรัก","Capy ยื่นโหลน้ำผึ้งให้ Hibi ตาเป็นประกาย บนโต๊ะมีจานเลมอนสไลซ์","Two-shot ระดับสายตา · หัวใจลอย","“ติ๊ง✨” + หัวเราะเบา ๆ","—"),
 (5,"0:11–0:14","เลมอน + น้ำผึ้ง ลงโหล","Hibi เรียงเลมอนทีละแผ่น Capy ราดน้ำผึ้งเป็นสายทองลงโหลแก้ว","มุมข้าง → ตัดเป็น top-down","เสียงน้ำผึ้งไหลหนืด ๆ","เลมอน × น้ำผึ้ง"),
 (6,"0:14–0:18","หมักไว้ 20 วัน","โหลปิดผูกป้ายบนขอบหน้าต่าง Hibi & Capy นอนกอดกันข้าง ๆ กลางวัน–กลางคืนสลับ ปฏิทินขีดฆ่าทีละวัน","Time-lapse แสงหมุน · ตัวนับวันวิ่ง Day 1 → 20","ติ๊กต่อก · ลมหายใจหลับ","หมักไว้ 20 วัน ⏳"),
 (7,"0:18–0:20","วันที่ 20 — เปิดโหล!","Hibi เปิดฝา ไซรัปสีอำพันกับเลมอนเชื่อมเปล่งแสงทอง ทั้งคู่ว้าวตาโต","Punch-in ตอนเปิดฝา · แสง burst","“ป๊อก!” ฝาเปิด + ประกาย","Day 20 ✨"),
 (8,"0:20–0:23","ชงมัทฉะสด","Hibi ตีมัทฉะในถ้วยเขียวด้วยแปรงไม้ไผ่ ฟองละเอียด ประกายสีเขียว","Overhead → ระดับถ้วย","ASMR ตีมัทฉะ","ตีมัทฉะสด 🍵"),
 (9,"0:23–0:26","ตักไซรัป + แผ่นเลมอน","Hibi ตักไซรัปน้ำผึ้งเลมอนจากโหลใส่แก้วน้ำแข็ง แผ่นเลมอนแนบข้างแก้ว","Close-up แก้ว · rack focus จากโหลมาแก้ว","น้ำแข็งกระทบแก้ว “กริ๊ง”","ไซรัปหมัก 20 วัน"),
 (10,"0:26–0:30","ค่อย ๆ เทมัทฉะ (Hero)","เทมัทฉะเขียวสดลงบนไซรัปทอง เกิดเลเยอร์ไล่สีเขียว–ทองหมุนวน","Macro · slow motion 50% · หมุนรอบแก้วช้า ๆ","เพลงขึ้นเต็ม · เสียงเทนุ่ม","Matcha Honey Lemon"),
 (11,"0:30–0:33","จิบแรก แล้วส่งให้ Capy","Hibi จิบแล้วหลับตาฟิน ยื่นแก้วให้ Capy ที่มองตาวาว","Medium shot · ตามแก้วจาก Hibi → Capy","“อื้มม~” · หัวใจป๊อป","ชิมหน่อยไหม? 💚"),
 (12,"0:33–0:36","Capy ดื่มจนหมดแก้ว","Capy ถือแก้วเปล่าหน้าฟินสุด ๆ Hibi หัวเราะเอามือแตะแก้ม หัวใจลอยเต็มจอ","Two-shot · zoom-out เผยหัวใจ","“ซู้ดดด” + เสียงหัวเราะ","หมดแก้ว! 🥰"),
 (13,"0:36–0:40","End card","ชื่อเมนู + Hibi & Capy โบกมือ + 5 สาขา + Delivery","ภาพนิ่ง · ตัวหนังสือเด้ง","เพลงจบอบอุ่น","Matcha Honey Lemon · Hibi Matcha Cafe"),
]
def img(n):
    if n==13: return f"url('file://{F}/s10.png')"
    return f"url('file://{F}/s{n:02d}.png')"
def panel(s):
    n,tc,tt,a,cam,snd,ost=s
    extra=""
    if n==13:
        extra=('<div style="position:absolute;inset:0;backdrop-filter:blur(10px) brightness(1.05);background:rgba(255,250,235,.35)"></div>'
               '<div style="position:absolute;left:8%;right:8%;top:30%;background:rgba(255,252,244,.95);border-radius:22px;padding:22px 12px;text-align:center;box-shadow:0 8px 20px rgba(0,0,0,.15)">'
               '<div style="font-family:Prompt;font-weight:700;font-size:34px;color:#243e1b;line-height:1.1">Matcha<br>Honey Lemon</div>'
               '<div style="font-size:18px;color:#7a6a2a;margin-top:6px">🍋 เลมอนหมักน้ำผึ้ง 20 วัน × มัทฉะ</div>'
               '<div style="font-size:16px;color:#6b6a55;margin-top:10px">Hibi Matcha Cafe · 5 สาขา<br>LINE MAN · Grab · ShopeeFood</div></div>'
               f'<div style="position:absolute;left:6%;bottom:6%;width:34%;aspect-ratio:1;border-radius:50%;background:url(file://{CH}/hibi_face.png) center/cover,#fff;border:4px solid #fff"></div>'
               f'<div style="position:absolute;right:6%;bottom:6%;width:34%;aspect-ratio:1;border-radius:50%;background:url(file://{CH}/capy_face.png) center/cover,#fff;border:4px solid #fff"></div>')
    o=f'<div class="ost">{ost}</div>' if ost!="—" and n!=13 else ""
    return (f'<div class="p"><div class="im" style="background-image:{img(n)}">{extra}<div class="no">{n:02d}</div><div class="tc">{tc}</div>{o}</div>'
            f'<div class="tx"><div class="tt">{tt}</div><div>{a}</div>'
            f'<div class="k"><b>🎥</b><span>{cam}</span></div><div class="k"><b>🔊</b><span>{snd}</span></div></div></div>')
def page(name,body):
    p=f"{O}/{name}.html"; open(p,"w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>")
    subprocess.run(["/opt/pw-browsers/chromium","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--allow-file-access-from-files",
        "--virtual-time-budget=4000",f"--screenshot={O}/{name}_raw.png",f"--window-size={W},{H+150}","file://"+p],check=True,capture_output=True)
    Image.open(f"{O}/{name}_raw.png").crop((0,0,W,H)).convert("RGB").save(f"{O}/{name}.jpg",quality=92); os.remove(f"{O}/{name}_raw.png")
HD=lambda pg:(f'<div class="hd"><h1>Matcha Honey Lemon <span>·</span> Hibi &amp; Capy</h1>'
              f'<div class="meta">Storyboard · Reels/TikTok 9:16 · ~40 วิ<span class="pill">หน้า {pg}/4</span></div></div>')
FT='<div class="ft"><span>Hibi Matcha Cafe · Storyboard v1 · ต.ค. 2026</span><span>ภาพประกอบ: Higgsfield (อ้างอิงชีตตัวละครทางการ Hibi &amp; Capy)</span></div>'
# ---- cover
thumbs="".join(f'<div style="flex:1;text-align:center"><div style="aspect-ratio:9/16;border-radius:14px;background:{img(s[0])} center/cover;box-shadow:0 6px 14px rgba(0,0,0,.12);position:relative">'
               f'<div style="position:absolute;left:6px;top:6px;background:#ffd23f;font-family:Prompt;font-weight:700;font-size:16px;padding:1px 8px;border-radius:8px">{s[0]:02d}</div></div>'
               f'<div style="font-size:15px;margin-top:6px;color:#6b6a55">{s[1]}</div><div style="font-family:Prompt;font-weight:600;font-size:16px;color:#243e1b;line-height:1.2">{s[2]}</div></div>' for s in SH)
acts=[("🍋","เก็บ & สไลซ์","01–02"),("🍯","น้ำผึ้งจาก Capy","03–04"),("🫙","ลงโหล & หมัก 20 วัน","05–07"),("🍵","ชง & เท","08–10"),("💚","แบ่งกันดื่ม","11–13")]
actsH="".join(f'<div style="flex:1;background:#fff;border-radius:22px;padding:18px;text-align:center;box-shadow:0 8px 20px rgba(120,100,40,.1)"><div style="font-size:44px">{e}</div><div style="font-family:Prompt;font-weight:700;font-size:24px;color:#243e1b">{t}</div><div style="font-size:18px;color:#9a9578">ช็อต {r}</div></div>'+('<div style="align-self:center;font-size:30px;color:#e0a800">➜</div>' if i<4 else '') for i,(e,t,r) in enumerate(acts))
pal="".join(f'<div style="text-align:center"><div style="width:52px;height:52px;border-radius:50%;background:{c};box-shadow:0 4px 10px rgba(0,0,0,.12)"></div><div style="font-size:15px;margin-top:4px">{n}</div></div>' for c,n in [("#F8E9DD","ครีม Hibi"),("#F4C7C6","ชมพูแก้ม"),("#FFE066","เหลืองเลมอน"),("#E8A317","ทองน้ำผึ้ง"),("#7FB24A","เขียวมัทฉะ"),("#A7B895","เซจ"),("#B07A4A","น้ำตาล Capy")])
cover=HD(1)+f'''
<div style="position:absolute;left:80px;top:180px;width:1240px">
 <div style="font-family:Prompt;font-weight:700;font-size:34px;color:#e0a800">Logline</div>
 <div style="font-size:30px;line-height:1.5;margin-top:6px">Hibi เก็บเลมอนจากต้น สไลซ์บาง ๆ แล้วหมักกับน้ำผึ้งสดที่ Capy ไปเก็บมาให้ <b>20 วัน</b> ก่อนชงเป็น <b>Matcha Honey Lemon</b> แก้วพิเศษ — ยื่นให้ Capy ชิมคำเดียว… แต่ Capy ดื่มจนหมดแก้ว 🥰</div>
 <div style="display:flex;gap:40px;margin-top:30px;font-size:24px;line-height:1.6">
  <div><b style="font-family:Prompt;color:#243e1b">Mood</b><br>น่ารัก · สดใส · อบอุ่น · เต็มไปด้วยความรัก<br><b style="font-family:Prompt;color:#243e1b">สไตล์ภาพ</b><br>Storybook 3D นุ่มฟู แสงแดดเช้า–บ่ายสีทอง</div>
  <div><b style="font-family:Prompt;color:#243e1b">Key message</b><br>“ทำด้วยใจทุกขั้นตอน — เลมอนหมักน้ำผึ้ง 20 วัน”<br><b style="font-family:Prompt;color:#243e1b">เสียง</b><br>อูคูเลเล่/กล็อคเกนสปีลเบา ๆ + ASMR ทุกขั้นตอน</div>
 </div>
</div>
<div style="position:absolute;right:80px;top:180px;width:920px;background:#fff;border-radius:26px;padding:26px 30px;box-shadow:0 10px 26px rgba(120,100,40,.12)">
 <div style="font-family:Prompt;font-weight:700;font-size:28px;color:#243e1b">ตัวละคร</div>
 <div style="display:flex;gap:26px;margin-top:12px;align-items:center">
  <div style="width:96px;height:96px;border-radius:50%;background:url(file://{CH}/hibi_face.png) center/cover;border:5px solid #F4C7C6;flex:none"></div>
  <div style="font-size:21px;line-height:1.45"><b style="font-family:Prompt;font-size:24px">Hibi</b> — คนลงมือทำ ตั้งใจทุกขั้น ยิ้มง่าย</div></div>
 <div style="display:flex;gap:26px;margin-top:14px;align-items:center">
  <div style="width:96px;height:96px;border-radius:50%;background:url(file://{CH}/capy_face.png) center/cover;border:5px solid #E8C9A0;flex:none"></div>
  <div style="font-size:21px;line-height:1.45"><b style="font-family:Prompt;font-size:24px">Capy</b> — สายชิล ไปเก็บน้ำผึ้งมาให้ และเป็นคนปิดเรื่องด้วยการดื่มจนหมดแก้ว</div></div>
 <div style="font-family:Prompt;font-weight:700;font-size:22px;color:#243e1b;margin-top:12px">โทนสี</div>
 <div style="display:flex;gap:16px;margin-top:8px">{pal}</div>
</div>
<div style="position:absolute;left:80px;right:80px;top:660px;display:flex;gap:16px">{actsH}</div>
<div style="position:absolute;left:80px;right:80px;top:860px;display:flex;gap:14px">{thumbs}</div>
'''+FT
page("SB_01_overview",cover)
for pg,(a,b) in enumerate([(0,5),(5,9),(9,13)],start=2):
    notes=('<div class="p" style="padding:26px 24px;font-size:21px;line-height:1.5;background:#fffdf5">'
      '<div class="tt" style="font-size:30px">📝 Production notes</div>'
      '<div style="margin-top:6px"><b>ผลิตต่อ:</b> ทำแต่ละเฟรมเป็นวิดีโอ 3–5 วิด้วย Higgsfield Seedance (ภาพเริ่มต้น = เฟรมในบอร์ดนี้ → ตัวละครคงที่)</div>'
      '<div style="margin-top:8px"><b>Motion graphic:</b> ตัวนับ Day 1→20 · ป้ายข้อความเด้ง · หัวใจ/ประกาย · เลเยอร์สีเขียว–ทอง</div>'
      '<div style="margin-top:8px"><b>เสียง:</b> เพลงอบอุ่นเบา ๆ (แต่งเอง ไม่ติดลิขสิทธิ์) + ASMR ทุกขั้น · ไม่มีช่วงเงียบ</div>'
      '<div style="margin-top:8px"><b>Hook 3 วิแรก:</b> เลมอนลูกแรก + ข้อความ “เริ่มจากต้น 🍋”</div>'
      '<div style="margin-top:14px;padding:14px 16px;border-radius:16px;background:#fff3c4"><b>⚠️ รอยืนยันก่อนผลิต</b><br>• ชื่อเมนูทางการ + ราคา<br>• ร้านหมักไซรัปเอง 20 วันจริงไหม<br>• Delivery มีเมนูนี้ไหม</div></div>') if pg==4 else ''
    page(f"SB_0{pg}_shots",HD(pg)+'<div class="row">'+"".join(panel(s) for s in SH[a:b])+notes+(''.join('<div style="flex:1"></div>' for _ in range(5-(b-a)-(1 if pg==4 else 0))))+'</div>'+FT)
print("ok")
