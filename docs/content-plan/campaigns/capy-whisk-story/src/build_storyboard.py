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
.row{{position:absolute;left:80px;right:80px;top:180px;display:flex;gap:24px}}
.p{{flex:1;background:#fff;border-radius:26px;box-shadow:0 10px 26px rgba(120,100,40,.13);overflow:hidden;display:flex;flex-direction:column}}
.p .im{{position:relative;width:100%;aspect-ratio:9/16;background:#eee center/cover no-repeat}}
.p .no{{position:absolute;left:14px;top:14px;background:#ffd23f;color:#3a2a00;font-family:'Prompt';font-weight:700;font-size:28px;padding:4px 16px;border-radius:16px;box-shadow:0 4px 10px rgba(0,0,0,.18)}}
.p .tc{{position:absolute;right:14px;top:14px;background:rgba(36,62,27,.85);color:#fff;font-weight:600;font-size:20px;padding:6px 14px;border-radius:14px}}
.p .ost{{position:absolute;left:50%;bottom:16%;transform:translateX(-50%);white-space:nowrap;font-size:18px !important;background:rgba(255,252,244,.94);color:#243e1b;font-family:'Prompt';font-weight:700;font-size:22px;padding:8px 16px;border-radius:16px;box-shadow:0 6px 14px rgba(0,0,0,.18)}}
.p .tx{{padding:16px 16px 18px;font-size:19px;line-height:1.42}}
.p .tt{{font-family:'Prompt';font-weight:700;font-size:25px;color:#243e1b;margin-bottom:5px}}
.k{{display:flex;gap:8px;margin-top:5px}} .k b{{flex:none;width:30px;text-align:center}} 
.ft{{position:absolute;left:80px;right:80px;bottom:34px;display:flex;justify-content:space-between;font-size:20px;color:#9a9578}}
"""
SH=[ # no, timecode, title, action, camera, sound, on-screen text
 (1,"0:00–0:03","Capy ขอลองเอง!","Capy ชูแปรงไม้ไผ่เหมือนดาบฮีโร่ หน้ามุ่งมั่น ตรงหน้ามีถ้วยผงมัทฉะ","มุมต่ำ · push-in เร็ว (HOOK)","“ติ๊ง✨” + “ฮึ่ม!” เบา ๆ","Capy ขอตีมัทฉะเอง! 💪"),
 (2,"0:03–0:06","วน… วน… วน…","Capy ตั้งใจตีวนเป็นวงกลมช้า ๆ มีเส้นหมุนการ์ตูน","Medium · เส้น motion วงกลม","แปรงครูดถ้วยช้า ๆ","วน… วน… วน… 🌀"),
 (3,"0:06–0:08","ฟองไม่ขึ้นเลย","มุมบนลงถ้วย มัทฉะแบนหม่น มีฟองใหญ่ไม่กี่ลูก","Top-down · ซูมช้า","“ปุ๊ด” ฟองแตก + เสียงเศร้าตลก","ฟองไม่ขึ้นเลย 🥲"),
 (4,"0:08–0:10","Capy เศร้า","Capy หูตก น้ำตาซึมนิด ๆ เมฆฝนจิ๋วบนหัว (ใช้ถ้วยมัทฉะแบน ไม่มีลาย)","Close-up หน้า · นิ่ง","“หงิง~”","—"),
 (5,"0:10–0:13","Hibi มาช่วย!","Hibi กระโดดเข้ามา ลูบหัว Capy ชูแปรงไม้ไผ่ Capy เงยหน้าตาวาว","Two-shot · หัวใจลอย","“ปุ๊ง” กระโดด + ระฆังเล็ก","Hibi มาช่วย! 🐰"),
 (6,"0:13–0:16","สอนตีรูปตัว M","Hibi วาดตัว M กลางอากาศด้วยแปรง เกิดเส้นประกายทอง Capy อ้าปากทึ่ง","Medium · เส้น M วาดตามจังหวะ","วิ้ง ✨ ตามเส้น","ตีซิกแซกเป็นตัว M ✨"),
 (7,"0:16–0:19","ตีด้วยกัน","Hibi จับมือ Capy ตีซิกแซกเร็ว ๆ ฟองค่อย ๆ ฟูขึ้น","ระดับถ้วย · ตัดเร็วตามจังหวะ","ASMR ตีมัทฉะเร็ว","เร็ว ๆ จากข้อมือ"),
 (8,"0:19–0:22","ฟองเนียนกริบ","มาโครฟองเขียวสดเนียนละเอียด ยกแปรงขึ้นเป็นยอดฟอง","Macro · slow-mo 50%","เสียงฟองนุ่ม + “ว้าว”","ฟองเนียนกริบ! 🍵"),
 (9,"0:22–0:25","ตีเพลินไปหน่อย","Capy ตีเพลินจนฟองล้นถ้วย มีหนวดฟองเขียว Hibi หัวเราะ","Two-shot · ฟองลอยฟุ้ง","“ฟุ่บ!” + เสียงหัวเราะ","ตีเพลินไปหน่อย 😂"),
 (10,"0:25–0:28","สำเร็จ! ชนแก้ว","Hibi & Capy ชนแก้ว Matcha Latte เย็น ยิ้มหลับตา หัวใจลอย","Medium · แสงทองอบอุ่น","“กริ๊ง!” แก้วชนกัน","สำเร็จ! 🥂"),
 (11,"0:28–0:32","End card · เซฟไว้","การ์ดสรุป 3 เคล็ดลับ + 📌 เซฟไว้ + Matcha Latte · Hibi 5 สาขา","ภาพนิ่ง · ตัวหนังสือเด้งทีละบรรทัด","เพลงจบอบอุ่น","📌 เซฟไว้ ตีมัทฉะแบบ Capy"),
]
def img(n):
    if n==11: return f"url('file://{F}/s08.png')"
    return f"url('file://{F}/s{n:02d}.png')"
def panel(s):
    n,tc,tt,a,cam,snd,ost=s
    extra=""
    if n==11:
        extra=('<div style="position:absolute;inset:0;backdrop-filter:blur(10px) brightness(1.05);background:rgba(255,250,235,.35)"></div>'
               '<div style="position:absolute;left:8%;right:8%;top:30%;background:rgba(255,252,244,.95);border-radius:22px;padding:22px 12px;text-align:center;box-shadow:0 8px 20px rgba(0,0,0,.15)">'
               '<div style="font-family:Prompt;font-weight:700;font-size:24px;color:#243e1b;line-height:1.15">📌 เซฟไว้<br>ตีมัทฉะแบบ Capy</div>'
               '<div style="font-size:15px;color:#3f8f3a;margin-top:6px;text-align:left;padding-left:8px">① ร่อนผงก่อน<br>② ตีซิกแซกรูปตัว M<br>③ เร็ว ๆ จากข้อมือ</div>'
               '<div style="font-size:16px;color:#6b6a55;margin-top:10px">Hibi Matcha Cafe · 5 สาขา<br>LINE MAN · Grab · ShopeeFood</div></div>'
               f'<div style="position:absolute;left:6%;bottom:6%;width:34%;aspect-ratio:1;border-radius:50%;background:url(file://{CH}/hibi_face.png) center/cover,#fff;border:4px solid #fff"></div>'
               f'<div style="position:absolute;right:6%;bottom:6%;width:34%;aspect-ratio:1;border-radius:50%;background:url(file://{CH}/capy_face.png) center/cover,#fff;border:4px solid #fff"></div>')
    o=f'<div class="ost">{ost}</div>' if ost!="—" and n!=11 else ""
    return (f'<div class="p"><div class="im" style="background-image:{img(n)}">{extra}<div class="no">{n:02d}</div><div class="tc">{tc}</div>{o}</div>'
            f'<div class="tx"><div class="tt">{tt}</div><div>{a}</div>'
            f'<div class="k"><b>🎥</b><span>{cam}</span></div><div class="k"><b>🔊</b><span>{snd}</span></div></div></div>')
def page(name,body):
    p=f"{O}/{name}.html"; open(p,"w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>")
    subprocess.run(["/opt/pw-browsers/chromium","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--allow-file-access-from-files",
        "--virtual-time-budget=4000",f"--screenshot={O}/{name}_raw.png",f"--window-size={W},{H+150}","file://"+p],check=True,capture_output=True)
    Image.open(f"{O}/{name}_raw.png").crop((0,0,W,H)).convert("RGB").save(f"{O}/{name}.jpg",quality=92); os.remove(f"{O}/{name}_raw.png")
HD=lambda pg:(f'<div class="hd"><h1>Capy หัดตีมัทฉะ <span>·</span> Hibi &amp; Capy</h1>'
              f'<div class="meta">Storyboard · Reels/TikTok 9:16 · ~32 วิ<span class="pill">หน้า {pg}/3</span></div></div>')
FT='<div class="ft"><span>Hibi Matcha Cafe · Storyboard v1 · พ.ย. 2026</span><span>ภาพประกอบ: Higgsfield (อ้างอิงชีตตัวละครทางการ Hibi &amp; Capy)</span></div>'
# ---- cover
thumbs="".join(f'<div style="flex:1;text-align:center"><div style="aspect-ratio:9/16;border-radius:14px;background:{img(s[0])} center/cover;box-shadow:0 6px 14px rgba(0,0,0,.12);position:relative">'
               f'<div style="position:absolute;left:6px;top:6px;background:#ffd23f;font-family:Prompt;font-weight:700;font-size:16px;padding:1px 8px;border-radius:8px">{s[0]:02d}</div></div>'
               f'<div style="font-size:15px;margin-top:6px;color:#6b6a55">{s[1]}</div><div style="font-family:Prompt;font-weight:600;font-size:16px;color:#243e1b;line-height:1.2">{s[2]}</div></div>' for s in SH)
acts=[("💪","Capy ขอลองเอง","01–02"),("🥲","ฟองไม่ขึ้น","03–04"),("🐰","Hibi สอนตัว M","05–07"),("😂","ฟองเนียน… จนล้น","08–09"),("📌","ชนแก้ว & เซฟไว้","10–11")]
actsH="".join(f'<div style="flex:1;background:#fff;border-radius:22px;padding:18px;text-align:center;box-shadow:0 8px 20px rgba(120,100,40,.1)"><div style="font-size:44px">{e}</div><div style="font-family:Prompt;font-weight:700;font-size:24px;color:#243e1b">{t}</div><div style="font-size:18px;color:#9a9578">ช็อต {r}</div></div>'+('<div style="align-self:center;font-size:30px;color:#e0a800">➜</div>' if i<4 else '') for i,(e,t,r) in enumerate(acts))
pal="".join(f'<div style="text-align:center"><div style="width:52px;height:52px;border-radius:50%;background:{c};box-shadow:0 4px 10px rgba(0,0,0,.12)"></div><div style="font-size:15px;margin-top:4px">{n}</div></div>' for c,n in [("#F8E9DD","ครีม Hibi"),("#F4C7C6","ชมพูแก้ม"),("#FFD23F","ประกายทอง"),("#FFF6E0","ฟองนม"),("#7FB24A","เขียวมัทฉะ"),("#A7B895","เซจ"),("#B07A4A","น้ำตาล Capy")])
cover=HD(1)+f'''
<div style="position:absolute;left:80px;top:180px;width:1240px">
 <div style="font-family:Prompt;font-weight:700;font-size:34px;color:#e0a800">Logline</div>
 <div style="font-size:30px;line-height:1.5;margin-top:6px">Capy อยากตีมัทฉะเอง แต่ตีวนเป็นวงกลมจน<b>ฟองไม่ขึ้น</b> 🥲 Hibi เลยมาสอน<b>ตีซิกแซกรูปตัว M</b> ฟองเนียนขึ้นทันที — แต่ Capy ตีเพลินจนฟองล้นถ้วย 😂 จบด้วยชนแก้ว Matcha Latte และการ์ดเคล็ดลับให้เซฟ</div>
 <div style="display:flex;gap:40px;margin-top:30px;font-size:24px;line-height:1.6">
  <div><b style="font-family:Prompt;color:#243e1b">Mood</b><br>น่ารัก · สดใส · ตลกนิด ๆ · ได้ความรู้<br><b style="font-family:Prompt;color:#243e1b">สไตล์ภาพ</b><br>Storybook 3D นุ่มฟู แสงแดดเช้า–บ่ายสีทอง</div>
  <div><b style="font-family:Prompt;color:#243e1b">Key message</b><br>“ตีรูปตัว M เร็ว ๆ จากข้อมือ = ฟองเนียน” (ให้คนเซฟ)<br><b style="font-family:Prompt;color:#243e1b">เสียง</b><br>อูคูเลเล่/กล็อคเกนสปีลเบา ๆ + ASMR ทุกขั้นตอน</div>
 </div>
</div>
<div style="position:absolute;right:80px;top:180px;width:920px;background:#fff;border-radius:26px;padding:26px 30px;box-shadow:0 10px 26px rgba(120,100,40,.12)">
 <div style="font-family:Prompt;font-weight:700;font-size:28px;color:#243e1b">ตัวละคร</div>
 <div style="display:flex;gap:26px;margin-top:12px;align-items:center">
  <div style="width:96px;height:96px;border-radius:50%;background:url(file://{CH}/hibi_face.png) center/cover;border:5px solid #F4C7C6;flex:none"></div>
  <div style="font-size:21px;line-height:1.45"><b style="font-family:Prompt;font-size:24px">Hibi</b> — คุณครูใจดี มาช่วยสอนด้วยรอยยิ้ม</div></div>
 <div style="display:flex;gap:26px;margin-top:14px;align-items:center">
  <div style="width:96px;height:96px;border-radius:50%;background:url(file://{CH}/capy_face.png) center/cover;border:5px solid #E8C9A0;flex:none"></div>
  <div style="font-size:21px;line-height:1.45"><b style="font-family:Prompt;font-size:24px">Capy</b> — มือใหม่ใจสู้ พลาดน่ารัก แล้วตีเพลินจนฟองล้น</div></div>
 <div style="font-family:Prompt;font-weight:700;font-size:22px;color:#243e1b;margin-top:12px">โทนสี</div>
 <div style="display:flex;gap:16px;margin-top:8px">{pal}</div>
</div>
<div style="position:absolute;left:80px;right:80px;top:660px;display:flex;gap:16px">{actsH}</div>
<div style="position:absolute;left:80px;right:80px;top:860px;display:flex;gap:14px">{thumbs}</div>
'''+FT
page("SB_01_overview",cover)
for pg,(a,b) in enumerate([(0,6),(6,11)],start=2):
    notes=('<div class="p" style="padding:24px 22px;font-size:20px;line-height:1.5;background:#fffdf5">'
      '<div class="tt" style="font-size:28px">📝 Production notes</div>'
      '<div style="margin-top:6px"><b>ผลิตต่อ:</b> ช็อต 1, 2, 6, 7, 9 ทำเป็นวิดีโอ (Seedance 720p) · ช็อตอื่นใช้ภาพนิ่ง + กล้องเคลื่อน + motion graphic</div>'
      '<div style="margin-top:8px"><b>Motion graphic:</b> ป้ายข้อความเด้ง · เมฆฝนจิ๋ว · เส้นตัว M วาดตามจังหวะ · ฟอง/หัวใจลอย · การ์ดเคล็ดลับ</div>'
      '<div style="margin-top:8px"><b>เสียง:</b> เพลงน่ารักแต่งเอง + ASMR ตีมัทฉะ · ไม่มีช่วงเงียบ</div>'
      '<div style="margin-top:12px;padding:12px 14px;border-radius:16px;background:#fff3c4"><b>💰 เครดิต</b><br>ภาพนิ่ง 10 ภาพ ~5 เครดิต (ทำแล้ว)<br>วิดีโอ 5 ช็อต × 28 = ~140 เครดิต<br>คงเหลือตอนนี้ ~63 → ต้องเติมก่อนผลิต</div></div>') if pg==3 else ''
    page(f"SB_0{pg}_shots",HD(pg)+'<div class="row">'+"".join(panel(s) for s in SH[a:b])+notes+'</div>'+FT)
print("ok")
