"""Storyboard pages for 'Matcha Lab #1 · ทำไมชาที่ดีที่สุดต้องปลูกในที่มืด' (HTML -> Chromium screenshot)."""
import subprocess, os
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__)); F=f"{D}/../frames"; O=f"{D}/../storyboard"
CH="/home/user/hibi-green-tea/docs/content-plan/campaigns/mbti-carousel/characters"
W,H=2400,1400
FONTS="".join(f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('file:///root/.fonts/{f}-{w}-{s}.woff2') format('woff2');}}"
  for fam,f in [("Prompt","Prompt"),("Plex","IBMPlexSansThai")] for w in ([400,500,600,700] if f=="Prompt" else [400,600]) for s in ["thai","latin"])
CSS=FONTS+f"""*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;font-family:'Plex';color:#3b3a2e;
 background:radial-gradient(circle at 10% 6%,#e9f5df 0,transparent 32%),radial-gradient(circle at 94% 96%,#fff3c4 0,transparent 30%),#fbfaf4}}
.hd{{position:absolute;left:80px;right:80px;top:44px;height:96px;display:flex;align-items:center;justify-content:space-between;border-bottom:3px dashed #d8e3c8}}
.hd h1{{font-family:'Prompt';font-weight:700;font-size:44px;color:#243e1b}} .hd h1 span{{color:#7fb24a}}
.hd .meta{{font-size:23px;color:#6b6a55;text-align:right;line-height:1.35}}
.pill{{display:inline-block;padding:4px 16px;border-radius:30px;background:#243e1b;color:#fff;font-weight:600;font-size:20px;margin-left:8px}}
.row{{position:absolute;left:80px;right:80px;top:172px;display:flex;gap:22px}}
.p{{flex:1;background:#fff;border-radius:26px;box-shadow:0 10px 26px rgba(60,90,40,.13);overflow:hidden;display:flex;flex-direction:column}}
.p .im{{position:relative;width:100%;aspect-ratio:9/16;background:#eee center/cover no-repeat}}
.p .no{{position:absolute;left:12px;top:12px;background:#a8d48a;color:#1d3314;font-family:'Prompt';font-weight:700;font-size:26px;padding:3px 14px;border-radius:14px;box-shadow:0 4px 10px rgba(0,0,0,.18)}}
.p .tc{{position:absolute;right:12px;top:12px;background:rgba(36,62,27,.85);color:#fff;font-weight:600;font-size:19px;padding:5px 12px;border-radius:12px}}
.p .ost{{position:absolute;left:7%;right:7%;top:15%;text-align:center;background:rgba(255,252,244,.94);color:#243e1b;font-family:'Prompt';font-weight:700;font-size:19px;line-height:1.3;padding:8px 10px;border-radius:14px;box-shadow:0 6px 14px rgba(0,0,0,.18)}}
.p .tx{{padding:14px 15px 16px;font-size:17.5px;line-height:1.4}}
.p .tt{{font-family:'Prompt';font-weight:700;font-size:23px;color:#243e1b;margin-bottom:4px}}
.k{{display:flex;gap:6px;margin-top:5px}} .k b{{flex:none;width:28px;text-align:center}}
.vo{{margin-top:6px;padding:7px 10px;border-radius:12px;background:#f1f7ea;color:#2f4a22}}
.ft{{position:absolute;left:80px;right:80px;bottom:30px;display:flex;justify-content:space-between;font-size:19px;color:#9a9578}}
"""
SH=[ # no, timecode, title, picture, camera, sound, on-screen text, VO
 (1,"0:00–0:03","HOOK · ไร่ชาในความมืด","อุโมงค์ตาข่ายดำคลุมแถวต้นชา แสงทองลอดช่องเล็ก ๆ หมอกบาง","มุมต่ำ · push-in ช้า → ซูมกระแทกตอนข้อความขึ้น","โดรนต่ำ ๆ + “ฟึ่บ” เบา","ชาที่ดีที่สุด…<br>ถูกปลูกในที่มืด 🤫","รู้ไหม ชาที่ดีที่สุดในญี่ปุ่น ถูกปลูกในที่มืด"),
 (2,"0:03–0:06","Hibi นักวิทยาศาสตร์","Hibi ใส่เสื้อกาวน์+แว่น ส่องใบชาด้วยแว่นขยาย (ผู้ดำเนินเรื่อง · ตัดออกได้ถ้าไม่ใช้ตัวละคร)","Medium · ซูมเข้าแว่นขยาย","“ติ๊ง” แว่นขยาย","ทำไมต้องปิดแสง? 🔬","ทำไมต้องปิดแสงล่ะ? มาส่องกัน"),
 (3,"0:06–0:10","คลุมต้นชาก่อนเก็บ","บน: ต้นชากลางแดด ใบเขียวอ่อน · ล่าง: มือดึงตาข่ายพรางแสงคลุมต้นชา","Split screen · เลื่อนจากบนลงล่าง","เสียงตาข่ายลาก","คลุมต้นชาราว 3–4 สัปดาห์<br>ก่อนเก็บใบ","ก่อนเก็บใบชาราวสามถึงสี่สัปดาห์ ชาวไร่จะคลุมต้นชาด้วยตาข่ายพรางแสง"),
 (4,"0:10–0:14","พบ ‘ธีอะนีน’","มาโครใบชาอ่อน มีอนุภาคสีทองเรืองแสงในใบ (ภาพจำลองทางวิทยาศาสตร์)","Macro · rack focus เข้าอนุภาค","ประกายวิ้ง ✨","ธีอะนีน ✨<br>= รสอุมามิ กลมกล่อม","ในใบชาอ่อนมีสารชื่อ ‘ธีอะนีน’ ตัวที่ให้รสอุมามิ กลมกล่อม"),
 (5,"0:14–0:19","แดดเปลี่ยนสาร","แสงแดดแรงส่องใบ อนุภาคทองถูกแสงแล้วกลายเป็นสีเทาเงิน","Macro · แสงวาบ + ลูกศร motion graphic ทอง→เทา","“วูบ” แสงแดด","☀️ แดดเปลี่ยน ธีอะนีน<br>→ คาเทชิน (ฝาด · ขม)","แต่เมื่อโดนแดด ใบชาจะเปลี่ยนธีอะนีน ไปเป็น ‘คาเทชิน’ ตัวที่ให้รสฝาดและขม"),
 (6,"0:19–0:23","ใต้ร่ม สารยังอยู่","ใบเขียวเข้มใต้ตาข่าย อนุภาคทองยังสว่างนิ่ง","Macro · dolly ช้า","pad นุ่ม ๆ","คลุมไว้ = เปลี่ยนน้อยลง<br>ธีอะนีนเหลือมาก","พอคลุมไว้ การเปลี่ยนนี้เกิดน้อยลง ธีอะนีนจึงเหลืออยู่มาก"),
 (7,"0:23–0:27","เทียบใบ 2 ใบ","ใบกลางแดด (เขียวอ่อน) vs ใบใต้ร่ม (เขียวมรกตเข้ม) บนกระดาษครีม","Top-down · ป้ายชื่อเด้งทีละใบ","“ป๊อป” × 2","กลางแดด ☀️ vs ใต้ร่ม 🌿","ใบที่โตใต้ร่มยังเขียวเข้มกว่าด้วย"),
 (8,"0:27–0:31","เก็บยอดอ่อน","มือเด็ดยอดอ่อนใต้แสงสลัวของตาข่าย ตะกร้าไม้ไผ่ใบเขียวเข้ม","Close-up · ตามมือ","เสียงเด็ดใบ ASMR","เก็บเฉพาะยอดอ่อน<br>→ ไปทำมัทฉะ","ยอดอ่อนใต้ร่มเหล่านี้ จะถูกนำไปทำเป็นมัทฉะ"),
 (9,"0:31–0:35","ผลลัพธ์ในถ้วย","ถ้วยมัทฉะเขียวสด ฟองเนียน แปรงไม้ไผ่ ใบชาสด","Macro top-down · หมุนช้า","ฟองนุ่ม","รสกลม หวานอุมามิ<br>ไม่จำเป็นต้องขม 🍵","นี่คือเหตุผลที่มัทฉะดี รสกลม หวานอุมามิ และไม่จำเป็นต้องขม"),
 (10,"0:35–0:40","กระดานสรุป","Hibi ชี้กระดาน: ชาแต่ละชนิดถูกคลุมนานแค่ไหน (ตัวหนังสือ motion graphic)","Medium · บรรทัดเด้งทีละแถว","“ป๊อป” ทีละบรรทัด","—","คาบุเสะฉะคลุมราวสองสัปดาห์ เกียวคุโระราวสาม มัทฉะราวสี่สัปดาห์"),
 (11,"0:40–0:44","End card · เซฟไว้","การ์ดสรุป 3 บรรทัด + 📌 เซฟไว้ + ตัวอย่างตอนหน้า","ภาพนิ่ง · ตัวหนังสือเด้ง","เพลงจบ","📌 เซฟไว้","เซฟไว้ แล้วตอนหน้ามาดูกันว่า ทำไมหินโม่หนึ่งชั่วโมง ได้มัทฉะแค่ราวสี่สิบกรัม"),
]
BOARD=('<div style="position:absolute;left:47%;right:7%;top:14%;height:30%;display:flex;flex-direction:column;justify-content:center;gap:4px;padding:6px 8px;font-family:Prompt;color:#243e1b">'
       '<div style="font-weight:700;font-size:13px;line-height:1.15">คลุมนานแค่ไหน?</div>'
       '<div style="font-size:11px;line-height:1.25">เซนฉะทั่วไป · ไม่คลุม ☀️<br>คาบุเสะฉะ · ~2 สัปดาห์<br>เกียวคุโระ · ~3 สัปดาห์<br><b style="color:#3f8f3a">มัทฉะ (เทนฉะ) · ~4 สัปดาห์</b></div></div>')
END=('<div style="position:absolute;inset:0;backdrop-filter:blur(10px) brightness(1.05);background:rgba(250,252,244,.4)"></div>'
     '<div style="position:absolute;left:8%;right:8%;top:24%;background:rgba(255,252,244,.96);border-radius:22px;padding:18px 12px;text-align:center;box-shadow:0 8px 20px rgba(0,0,0,.15)">'
     '<div style="font-family:Prompt;font-weight:700;font-size:23px;color:#243e1b;line-height:1.15">📌 เซฟไว้<br>ทำไมต้องปลูกในที่มืด</div>'
     '<div style="font-size:14px;color:#2f4a22;margin-top:8px;text-align:left;padding-left:6px;line-height:1.45">① คลุมต้นชา ~3–4 สัปดาห์ก่อนเก็บ<br>② แดดเปลี่ยนธีอะนีน (อุมามิ) → คาเทชิน (ฝาด)<br>③ คลุมไว้ = รสกลม ไม่ขม · ใบเขียวเข้ม</div>'
     '<div style="font-size:14px;color:#6b6a55;margin-top:10px;padding-top:8px;border-top:2px dashed #d8e3c8">ตอนหน้า 🔬 หินโม่ 1 ชม. ได้มัทฉะแค่ ~40 กรัม?</div></div>'
     '<div style="position:absolute;left:0;right:0;bottom:5%;text-align:center;font-size:14px;color:#6b6a55">Matcha Lab 🔬 · @hibimatchacafe</div>')
img=lambda n:f"url('file://{F}/s{(9 if n==11 else n):02d}.png')"
def panel(s):
    n,tc,tt,a,cam,snd,ost,vo=s
    extra=BOARD if n==10 else END if n==11 else ""
    o=f'<div class="ost">{ost}</div>' if ost!="—" and n!=11 else ""
    return (f'<div class="p"><div class="im" style="background-image:{img(n)}">{extra}<div class="no">{n:02d}</div><div class="tc">{tc}</div>{o}</div>'
            f'<div class="tx"><div class="tt">{tt}</div><div>{a}</div>'
            f'<div class="k"><b>🎥</b><span>{cam}</span></div><div class="k"><b>🔊</b><span>{snd}</span></div>'
            f'<div class="vo">🎙️ “{vo}”</div></div></div>')
def page(name,body):
    p=f"{O}/{name}.html"; open(p,"w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>")
    subprocess.run(["/opt/pw-browsers/chromium","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--allow-file-access-from-files",
        "--virtual-time-budget=4000",f"--screenshot={O}/{name}_raw.png",f"--window-size={W},{H+150}","file://"+p],check=True,capture_output=True)
    Image.open(f"{O}/{name}_raw.png").crop((0,0,W,H)).convert("RGB").save(f"{O}/{name}.jpg",quality=92); os.remove(f"{O}/{name}_raw.png"); os.remove(p)
HD=lambda pg:(f'<div class="hd"><h1>Matcha Lab 🔬 #1 <span>·</span> ทำไมชาที่ดีที่สุด ต้องปลูกในที่มืด?</h1>'
              f'<div class="meta">Storyboard · Reels/TikTok 9:16 · ~44 วิ<span class="pill">หน้า {pg}/3</span></div></div>')
FT='<div class="ft"><span>Matcha Lab · Storyboard v1 · 10 พ.ย. 2026</span><span>ภาพประกอบ: Higgsfield (ภาพจำลองทางวิทยาศาสตร์ · Hibi อ้างอิงชีตทางการ)</span></div>'
thumbs="".join(f'<div style="flex:1;text-align:center"><div style="aspect-ratio:9/16;border-radius:12px;background:{img(s[0])} center/cover;box-shadow:0 6px 14px rgba(0,0,0,.12);position:relative">'
               f'<div style="position:absolute;left:5px;top:5px;background:#a8d48a;font-family:Prompt;font-weight:700;font-size:15px;padding:1px 7px;border-radius:8px">{s[0]:02d}</div></div>'
               f'<div style="font-size:14px;margin-top:5px;color:#6b6a55">{s[1]}</div><div style="font-family:Prompt;font-weight:600;font-size:15px;color:#243e1b;line-height:1.2">{s[2]}</div></div>' for s in SH)
acts=[("🤫","ความลับ","01–02"),("🌑","คลุมต้นชา","03"),("✨","เคมีในใบ","04–06"),("🌿","ผลที่เห็นได้","07–09"),("📌","สรุป & เซฟไว้","10–11")]
actsH="".join(f'<div style="flex:1;background:#fff;border-radius:22px;padding:16px;text-align:center;box-shadow:0 8px 20px rgba(60,90,40,.1)"><div style="font-size:40px">{e}</div><div style="font-family:Prompt;font-weight:700;font-size:23px;color:#243e1b">{t}</div><div style="font-size:17px;color:#9a9578">ช็อต {r}</div></div>'+('<div style="align-self:center;font-size:28px;color:#7fb24a">➜</div>' if i<4 else '') for i,(e,t,r) in enumerate(acts))
cover=HD(1)+f'''
<div style="position:absolute;left:80px;top:170px;width:1260px">
 <div style="font-family:Prompt;font-weight:700;font-size:32px;color:#3f8f3a">แนวคิด</div>
 <div style="font-size:27px;line-height:1.5;margin-top:4px">เปิดด้วย<b>ความลับ</b> — ชาที่ดีที่สุดถูกปลูกใน<b>ที่มืด</b> แล้วพาเข้าไป “ในใบชา” ด้วยภาพจำลองวิทยาศาสตร์:
 แดดเปลี่ยน <b style="color:#b8860b">ธีอะนีน (อุมามิ)</b> เป็น <b style="color:#6b6a55">คาเทชิน (ฝาด·ขม)</b> → การคลุมต้นชาจึงทำให้มัทฉะรสกลม ไม่ขม · จบด้วยกระดานสรุป + การ์ดให้เซฟ + ปูตอนหน้า</div>
 <div style="display:flex;gap:40px;margin-top:22px;font-size:22px;line-height:1.55">
  <div><b style="font-family:Prompt;color:#243e1b">Mood</b><br>ลึกลับนิด ๆ → สว่าง เข้าใจ “อ๋อ!”<br><b style="font-family:Prompt;color:#243e1b">สไตล์ภาพ</b><br>สารคดี/มาโครสมจริง + ภาพจำลองอนุภาคเรืองแสง · Hibi 3D นุ่มฟูเป็นผู้ดำเนินเรื่อง</div>
  <div><b style="font-family:Prompt;color:#243e1b">Key message (ให้คนเซฟ)</b><br>“แดดทำให้ชาฝาด — คลุมไว้ = อุมามิ”<br><b style="font-family:Prompt;color:#243e1b">เสียง</b><br>VO เล่าเรื่อง (ตัด dead air) + pad/อิเล็กทรอนิกส์เบา ๆ แนวแล็บ + เสียงประกอบ</div>
 </div>
</div>
<div style="position:absolute;right:80px;top:170px;width:880px;background:#fff;border-radius:26px;padding:22px 28px;box-shadow:0 10px 26px rgba(60,90,40,.12);font-size:19px;line-height:1.5">
 <div style="font-family:Prompt;font-weight:700;font-size:26px;color:#243e1b">🔎 ข้อมูลที่ใช้ (มีแหล่งอ้างอิง)</div>
 <div>• ระยะคลุม: คาบุเสะ ~2 · เกียวคุโระ ~3 · มัทฉะ ~4 สัปดาห์ (Obubu Tea · Wikipedia Gyokuro)</div>
 <div>• แดดเปลี่ยนธีอะนีนเป็นคาเทชิน · คลุมแล้วธีอะนีน↑ คาเทชิน↓ (Frontiers in Plant Science 2020 · Yunomi)</div>
 <div style="margin-top:8px;padding:10px 14px;border-radius:14px;background:#fff3c4"><b>⚠️ ห้ามพูด</b> ธีอะนีน “ช่วยผ่อนคลาย/ดีต่อสมอง” หรือเรื่องสุขภาพใด ๆ · อนุภาคเรืองแสง = <b>ภาพจำลอง</b> (ระบุในแคปชัน)</div>
 <div style="margin-top:8px;padding:10px 14px;border-radius:14px;background:#ecf8e6"><b>🟡 ต้องเช็ก</b> ช็อต 7 “ใบใต้ร่มเขียวเข้มกว่า” — เป็นที่รู้กันทั่วไปแต่ยังไม่ได้ใส่แหล่งอ้างอิง</div>
</div>
<div style="position:absolute;left:80px;right:80px;top:640px;display:flex;gap:14px">{actsH}</div>
<div style="position:absolute;left:80px;right:80px;top:830px;display:flex;gap:12px">{thumbs}</div>
'''+FT
page("SB_01_overview",cover)
notes=('<div class="p" style="padding:22px 20px;font-size:18.5px;line-height:1.5;background:#fbfdf6">'
  '<div class="tt" style="font-size:26px">📝 Production notes</div>'
  '<div style="margin-top:6px"><b>วิดีโอ (Seedance):</b> ช็อต 1, 3, 5, 8, 9 · ช็อตอื่นใช้ภาพนิ่ง + กล้องเคลื่อน + motion graphic</div>'
  '<div style="margin-top:8px"><b>Motion graphic:</b> ป้ายชื่อสาร (ทอง=ธีอะนีน · เทา=คาเทชิน) · ลูกศรเปลี่ยนสาร · ตารางบนกระดาน · การ์ดเซฟ</div>'
  '<div style="margin-top:8px"><b>VO:</b> ร้านอัดเสียง (สคริปต์ Teleprompter ใน README) หรือเสียงพากย์ AI → ตัด dead air ตามสูตร knowledge/04</div>'
  '<div style="margin-top:8px"><b>ไม่ใช้ตัวละคร?</b> ตัดช็อต 2 · ช็อต 10 เปลี่ยนเป็นกระดานอย่างเดียว</div>'
  '<div style="margin-top:12px;padding:12px 14px;border-radius:16px;background:#fff3c4"><b>💰 เครดิต</b><br>ภาพนิ่ง 10 ภาพ (ทำแล้ว)<br>วิดีโอ 5 ช็อต × 64 (1080p) ≈ 320<br>คงเหลือ ~4,590 ✅</div></div>')
page("SB_02_shots",HD(2)+'<div class="row">'+"".join(panel(s) for s in SH[0:6])+'</div>'+FT)
page("SB_03_shots",HD(3)+'<div class="row">'+"".join(panel(s) for s in SH[6:11])+notes+'</div>'+FT)
ims=[Image.open(f"{O}/{n}.jpg").convert("RGB") for n in ["SB_01_overview","SB_02_shots","SB_03_shots"]]
ims[0].save(f"{O}/MatchaLab01_Shade_Storyboard.pdf",save_all=True,append_images=ims[1:],resolution=150)
print("ok")
