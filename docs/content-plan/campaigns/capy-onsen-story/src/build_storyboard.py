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
 (1,"0:00–0:03","หนาวแล้ววว","Capy ใส่ผ้าพันคอถักจิ๋ว ยืนตัวสั่นหน้าร้าน ลมพัดใบเมเปิลปลิว","Medium · ใบไม้ปลิวผ่านกล้อง (HOOK)","ลมหวีด · ฟันกระทบ “กึก ๆ”","หนาวแล้ววว Capy สั่นเลย 🥶"),
 (2,"0:03–0:06","ไอร้อนอะไรนั่น?","Capy แอบมองจากหลังโคมหิน เห็นบ่อออนเซ็นไอลอย ตาเป็นประกาย","Over-shoulder → ไอน้ำ","น้ำไหลเบา ๆ · “ติ๊ง✨”","เอ๊ะ… ไอร้อนอะไรนั่น 👀"),
 (3,"0:06–0:09","จุ่มเท้าก่อน","Capy นั่งขอบบ่อ ค่อย ๆ จุ่มเท้าจิ๋วลงน้ำ หน้าลุ้น ๆ","Close-up เท้า + หน้า","น้ำกระเพื่อม “จ๋อม”","จุ่มเท้าก่อน… 🦶"),
 (4,"0:09–0:12","ฟินนน","Capy แช่ถึงคาง ผ้าขนหนูบนหัว หลับตายิ้มฟิน ไอลอย","Medium · push-in ช้า","เสียงถอนหายใจฟิน “ฮ้าาา~”","ฟินนน ♨️"),
 (5,"0:12–0:14","Hibi มีไอเดีย","Hibi มองจากหน้าต่างร้าน หูตั้ง ตาเป็นประกาย หลอดไฟวิ้ง","Medium · ระดับสายตา","“ปิ๊ง💡”","Hibi มีไอเดีย 💡"),
 (6,"0:14–0:17","Hojicha Latte อุ่น ๆ","Hibi เทนมลงชาโฮจิฉะสีอำพัน ไอร้อนลอย โทนคาราเมล","Close-up ถ้วย · slow-mo ตอนเทนม","เทนมนุ่ม ๆ","Hojicha Latte อุ่น ๆ ☕"),
 (7,"0:17–0:20","เดินเสิร์ฟถึงบ่อ","Hibi ถือถาดไม้มีถ้วยโฮจิฉะ 2 ใบ + ส้ม เดินบนทางหิน ใบไม้ร่วง","Tracking ตาม Hibi","ฝีเท้าเบา ๆ · ใบไม้กรอบ","เสิร์ฟถึงบ่อเลย 🐰"),
 (8,"0:20–0:23","ส้มบนหัว","Hibi วางส้มบนหัว Capy ถาดลอยมีถ้วยโฮจิฉะลอยข้าง ๆ","Two-shot · ซูมเข้าส้ม","“ปุ๊ก” วางส้ม + หัวเราะ","ส้มบนหัว = ของมันต้องมี 🍊"),
 (9,"0:23–0:26","จิบแล้วอุ่นใจ","Capy ประคองถ้วยจิบ แก้มแดง ไอน้ำลอยเป็นรูปหัวใจ","Close-up · แสงทองนุ่ม","จิบ “ซู้ด” + “อื้มม~”","อุ่นทั้งตัว อุ่นทั้งใจ 💛"),
 (10,"0:26–0:29","หลับปุ๋ยทั้งคู่","Hibi & Capy แช่คู่กัน ผ้าขนหนูบนหัว หลับยิ้ม ฟ้าพลบค่ำสีชมพู","Wide · แสงพลบค่ำ","กล่อมเบา ๆ · “zzz”","zzz… 😴"),
 (11,"0:29–0:33","End card","“หนาวนี้… มาอุ่นใจที่ Hibi” + Hojicha Latte + 5 สาขา + ชวนแท็ก","ภาพนิ่ง · ตัวหนังสือเด้ง","เพลงจบอบอุ่น","หนาวนี้มาอุ่นใจที่ Hibi ☕"),
]
def img(n):
    if n==11: return f"url('file://{F}/s09.png')"
    return f"url('file://{F}/s{n:02d}.png')"
def panel(s):
    n,tc,tt,a,cam,snd,ost=s
    extra=""
    if n==11:
        extra=('<div style="position:absolute;inset:0;backdrop-filter:blur(10px) brightness(1.05);background:rgba(255,250,235,.35)"></div>'
               '<div style="position:absolute;left:8%;right:8%;top:30%;background:rgba(255,252,244,.95);border-radius:22px;padding:22px 12px;text-align:center;box-shadow:0 8px 20px rgba(0,0,0,.15)">'
               '<div style="font-family:Prompt;font-weight:700;font-size:25px;color:#243e1b;line-height:1.15">หนาวนี้…<br>มาอุ่นใจที่ Hibi ☕</div>'
               '<div style="font-size:16px;color:#8a5a2a;margin-top:6px">Hojicha Latte อุ่น ๆ</div>'
               '<div style="font-size:15px;color:#3f8f3a;margin-top:4px">แท็กคนที่อยากไปแช่ด้วย ♨️</div>'
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
HD=lambda pg:(f'<div class="hd"><h1>หนาวนี้ Capy แช่ออนเซ็น <span>·</span> Hibi &amp; Capy</h1>'
              f'<div class="meta">Storyboard · Reels/TikTok 9:16 · ~33 วิ<span class="pill">หน้า {pg}/3</span></div></div>')
FT='<div class="ft"><span>Hibi Matcha Cafe · Storyboard v1 · พ.ย. 2026</span><span>ภาพประกอบ: Higgsfield (อ้างอิงชีตตัวละครทางการ Hibi &amp; Capy)</span></div>'
# ---- cover
thumbs="".join(f'<div style="flex:1;text-align:center"><div style="aspect-ratio:9/16;border-radius:14px;background:{img(s[0])} center/cover;box-shadow:0 6px 14px rgba(0,0,0,.12);position:relative">'
               f'<div style="position:absolute;left:6px;top:6px;background:#ffd23f;font-family:Prompt;font-weight:700;font-size:16px;padding:1px 8px;border-radius:8px">{s[0]:02d}</div></div>'
               f'<div style="font-size:15px;margin-top:6px;color:#6b6a55">{s[1]}</div><div style="font-family:Prompt;font-weight:600;font-size:16px;color:#243e1b;line-height:1.2">{s[2]}</div></div>' for s in SH)
acts=[("🥶","Capy หนาวสั่น","01–02"),("♨️","แช่ออนเซ็น","03–04"),("☕","Hibi ชงโฮจิฉะ","05–07"),("🍊","ส้มบนหัว & จิบ","08–09"),("😴","หลับปุ๋ยคู่กัน","10–11")]
actsH="".join(f'<div style="flex:1;background:#fff;border-radius:22px;padding:18px;text-align:center;box-shadow:0 8px 20px rgba(120,100,40,.1)"><div style="font-size:44px">{e}</div><div style="font-family:Prompt;font-weight:700;font-size:24px;color:#243e1b">{t}</div><div style="font-size:18px;color:#9a9578">ช็อต {r}</div></div>'+('<div style="align-self:center;font-size:30px;color:#e0a800">➜</div>' if i<4 else '') for i,(e,t,r) in enumerate(acts))
pal="".join(f'<div style="text-align:center"><div style="width:52px;height:52px;border-radius:50%;background:{c};box-shadow:0 4px 10px rgba(0,0,0,.12)"></div><div style="font-size:15px;margin-top:4px">{n}</div></div>' for c,n in [("#F8E9DD","ครีม Hibi"),("#F4C7C6","ชมพูแก้ม"),("#E07B39","ใบเมเปิล"),("#C99A6B","โฮจิฉะลาเต้"),("#7FB24A","เขียวมัทฉะ"),("#A7B895","เซจ"),("#B07A4A","น้ำตาล Capy")])
cover=HD(1)+f'''
<div style="position:absolute;left:80px;top:180px;width:1240px">
 <div style="font-family:Prompt;font-weight:700;font-size:34px;color:#e0a800">Logline</div>
 <div style="font-size:30px;line-height:1.5;margin-top:6px">ลมหนาวมา Capy ตัวสั่น 🥶 เลยแอบไป<b>แช่ออนเซ็น</b>หลังร้าน ♨️ Hibi เห็นเข้าก็ชง<b>Hojicha Latte อุ่น ๆ</b> เดินไปเสิร์ฟถึงบ่อ วาง<b>ส้มบนหัว</b> Capy ให้ด้วย 🍊 จิบแล้วอุ่นทั้งตัวทั้งใจ — จบที่หลับปุ๋ยแช่น้ำคู่กัน 😴</div>
 <div style="display:flex;gap:40px;margin-top:30px;font-size:24px;line-height:1.6">
  <div><b style="font-family:Prompt;color:#243e1b">Mood</b><br>อบอุ่น · น่ารัก · ผ่อนคลาย · cozy<br><b style="font-family:Prompt;color:#243e1b">สไตล์ภาพ</b><br>Storybook 3D นุ่มฟู · ไอน้ำ · ใบเมเปิล · แสงเช้าหมอก → พลบค่ำชมพู</div>
  <div><b style="font-family:Prompt;color:#243e1b">Key message</b><br>“หนาวนี้ มาอุ่นใจด้วย Hojicha Latte ที่ Hibi”<br><b style="font-family:Prompt;color:#243e1b">เสียง</b><br>เพลงช้า อบอุ่น (กล็อคเกนสปีล + pad) + ASMR น้ำ ไอร้อน เทนม</div>
 </div>
</div>
<div style="position:absolute;right:80px;top:180px;width:920px;background:#fff;border-radius:26px;padding:26px 30px;box-shadow:0 10px 26px rgba(120,100,40,.12)">
 <div style="font-family:Prompt;font-weight:700;font-size:28px;color:#243e1b">ตัวละคร</div>
 <div style="display:flex;gap:26px;margin-top:12px;align-items:center">
  <div style="width:96px;height:96px;border-radius:50%;background:url(file://{CH}/hibi_face.png) center/cover;border:5px solid #F4C7C6;flex:none"></div>
  <div style="font-size:21px;line-height:1.45"><b style="font-family:Prompt;font-size:24px">Hibi</b> — เพื่อนใจดี ชงเครื่องดื่มอุ่น ๆ มาเสิร์ฟถึงที่</div></div>
 <div style="display:flex;gap:26px;margin-top:14px;align-items:center">
  <div style="width:96px;height:96px;border-radius:50%;background:url(file://{CH}/capy_face.png) center/cover;border:5px solid #E8C9A0;flex:none"></div>
  <div style="font-size:21px;line-height:1.45"><b style="font-family:Prompt;font-size:24px">Capy</b> — ขี้หนาว สายชิล แช่ออนเซ็นพร้อมส้มบนหัว (ท่าประจำในชีตตัวละคร)</div></div>
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
      '<div style="margin-top:6px"><b>ผลิตต่อ:</b> ช็อต 1–10 ทำเป็นวิดีโอ Seedance 1080p พร้อมเสียง ASMR (ไอน้ำ น้ำกระเพื่อม เทนม)</div>'
      '<div style="margin-top:8px"><b>Motion graphic:</b> ป้ายข้อความเด้ง · ใบไม้ปลิว · ไอน้ำรูปหัวใจ · zzz ลอย · การ์ดจบ</div>'
      '<div style="margin-top:8px"><b>เสียง:</b> เพลงช้าอบอุ่นแต่งเอง + ASMR · ไม่มีช่วงเงียบ</div>'
      '<div style="margin-top:12px;padding:12px 14px;border-radius:16px;background:#fff3c4"><b>💰 เครดิต</b><br>ภาพนิ่ง 10 ภาพ ~6 เครดิต (ทำแล้ว)<br>วิดีโอ 10 ช็อต × 64 = ~640 เครดิต<br>คงเหลือ ~5,347 → พอผลิต</div></div>') if pg==3 else ''
    page(f"SB_0{pg}_shots",HD(pg)+'<div class="row">'+"".join(panel(s) for s in SH[a:b])+notes+'</div>'+FT)
print("ok")
