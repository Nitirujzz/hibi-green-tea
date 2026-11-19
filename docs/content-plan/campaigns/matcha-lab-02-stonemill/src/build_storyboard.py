"""Storyboard pages for 'Matcha Lab #2 · หินโม่ 1 ชม. ได้มัทฉะแค่ ~40 กรัม' (reuses the page CSS of episode 1)."""
import subprocess, os
from PIL import Image
_src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"../../matcha-lab-01-shade/src/build_storyboard.py"),encoding="utf-8").read()
exec(_src.split("SH=[")[0])          # D, F, O, CH, W, H, CSS (paths follow this file)
SH=[ # no, timecode, title, picture, camera, sound, on-screen text, VO
 (1,"0:00–0:04","HOOK · หินโม่หมุนช้า ๆ","หินโม่แกรนิตหมุนช้า ผงเขียวสดค่อย ๆ ไหลออกจากร่องระหว่างหิน ละอองผงลอยในลำแสง","Macro · push-in ช้า → ซูมกระแทกตอนตัวเลขขึ้น","เสียงหินครูดเบา ๆ + “ติ๊ก” นาฬิกา","หินโม่หมุน 1 ชั่วโมง…<br>ได้มัทฉะแค่ ~40 กรัม ⏳","หินโม่หมุนหนึ่งชั่วโมง ได้มัทฉะแค่ราวสี่สิบกรัม"),
 (2,"0:04–0:07","Hibi จับเวลา","Hibi ชุดกาวน์ถือนาฬิกาจับเวลา ตกใจกับกองผงเล็กจิ๋ว (ตัดออกได้ถ้าไม่ใช้ตัวละคร)","Medium · ซูมเข้ากองผง","“ติ๊ง” + เสียงตกใจน่ารัก","ทำไมช้าขนาดนี้? 🔬","ทำไมถึงช้าขนาดนี้? มาส่องกัน"),
 (3,"0:07–0:11","เริ่มจาก ‘เทนฉะ’","ใบชาอบแห้งเป็นแผ่นบางเบาในมือ เหนือชามไม้","Macro · rack focus จากมือไปชาม","เสียงใบชาแห้งกรอบ","เทนฉะ = ใบชาอบแห้ง<br>แยกก้านและเส้นใบออกแล้ว","มัทฉะเริ่มจาก ‘เทนฉะ’ ใบชาอบแห้งที่แยกก้านและเส้นใบออกแล้ว"),
 (4,"0:11–0:15","ป้อนทีละน้อย","มือใช้ช้อนไม้เทเทนฉะลงรูกลางหินโม่ เกล็ดใบชาร่วงกลางอากาศ","Close-up · ตามช้อน","เสียงเกล็ดใบชาร่วง","ใส่ทีละน้อย<br>ลงรูกลางหินโม่","ใส่ลงรูกลางหินโม่ทีละน้อย"),
 (5,"0:15–0:21","ข้างในหินโม่","ภาพตัดจำลอง: หินบนยกขึ้น เห็นร่องหินเป็นรัศมี ใบชาเดินจากกลางไปขอบ ละเอียดขึ้นเรื่อย ๆ","ภาพจำลอง 3D · ลูกศร motion graphic จากกลาง→ขอบ","pad + “วืด” ตามลูกศร","ใบชาเดินจากกลาง → ขอบหิน<br>ผ่านร่องหิน ละเอียดขึ้นเรื่อย ๆ","ใบชาจะค่อย ๆ เดินจากกลางไปขอบหิน ผ่านร่องที่สลักไว้ ละเอียดขึ้นเรื่อย ๆ"),
 (6,"0:21–0:26","ทำไมต้องหมุนช้า","ห้องโม่แสงเย็น หินโม่เรียงแถวหมุนช้า ๆ","Wide · dolly ช้า","เสียงห้องเงียบ + หินหมุน","หมุนช้า = ไม่ร้อนจากแรงเสียดทาน<br>ถนอมสีเขียวและกลิ่นหอม","ที่ต้องหมุนช้า เพราะถ้าเร็ว แรงเสียดทานจะทำให้ร้อน สีเขียวและกลิ่นหอมจะเสียไป"),
 (7,"0:26–0:31","ละเอียดแค่ไหน","ภาพจำลองแบบกล้องจุลทรรศน์: เส้นผม 1 เส้น เทียบกับผงมัทฉะจิ๋ว","ภาพจำลอง · ซูมเข้าเรื่อย ๆ","“วิ้ง” + pad","ผงละเอียดราว 5–10 ไมครอน<br>เล็กกว่าเส้นผมหลายเท่า","ผงที่ได้ละเอียดราวห้าถึงสิบไมครอน เล็กกว่าเส้นผมของเราหลายเท่า"),
 (8,"0:31–0:36","40 กรัม = กี่ถ้วย","กองผงบนตาชั่ง ล้อมด้วยถ้วยมัทฉะเรียงเป็นแถว ~20 ถ้วย","Top-down · ถ้วยนับเลขเด้งทีละใบ","“ป๊อป” นับถ้วย","40 กรัม ≈ มัทฉะ ~20 ถ้วย<br>(ถ้วยละ ~2 กรัม)","สี่สิบกรัม ชงได้ราวยี่สิบถ้วยเท่านั้น"),
 (9,"0:36–0:41","จึงต้องร่อนก่อนชง","ร่อนผงผ่านตะแกรง ผงร่วงเหมือนหิมะสีเขียว ก้อนผงค้างบนตะแกรง","Macro side · slow-mo","เสียงร่อน ASMR","ผงละเอียดมาก จับเป็นก้อนง่าย<br>→ ร่อนก่อนชงทุกครั้ง","และเพราะผงละเอียดมาก จึงจับเป็นก้อนง่าย ต้องร่อนก่อนชงทุกครั้ง"),
 (10,"0:41–0:45","กระดานสรุป","Hibi ชี้กระดาน: 3 ตัวเลขของหินโม่ (motion graphic)","Medium · บรรทัดเด้งทีละแถว","“ป๊อป” ทีละบรรทัด","—","หนึ่งชั่วโมง สี่สิบกรัม ห้าถึงสิบไมครอน นี่คือความช้าที่ตั้งใจ"),
 (11,"0:45–0:50","End card · เซฟไว้","การ์ดสรุป 3 ข้อ + 📌 เซฟไว้ + ตัวอย่างตอนหน้า","ภาพนิ่ง · ตัวหนังสือเด้ง","เพลงจบ","📌 เซฟไว้","เซฟไว้ แล้วตอนหน้ามาดูกันว่า น้ำเดือดทำให้มัทฉะขม จริงไหม"),
]
BOARD=('<div style="position:absolute;left:50%;right:6%;top:13%;height:32%;display:flex;flex-direction:column;justify-content:center;gap:4px;padding:6px 8px;font-family:Prompt;color:#243e1b">'
       '<div style="font-weight:700;font-size:13px;line-height:1.15">หินโม่ 1 ตัว</div>'
       '<div style="font-size:11px;line-height:1.3">⏳ 1 ชม. ≈ 30–40 กรัม<br>🔬 ผง ~5–10 ไมครอน<br>🌡️ หมุนช้า กันร้อน<br><b style="color:#3f8f3a">🍵 ≈ ~20 ถ้วย</b></div></div>')
END=('<div style="position:absolute;inset:0;backdrop-filter:blur(10px) brightness(1.05);background:rgba(250,252,244,.4)"></div>'
     '<div style="position:absolute;left:8%;right:8%;top:24%;background:rgba(255,252,244,.96);border-radius:22px;padding:18px 12px;text-align:center;box-shadow:0 8px 20px rgba(0,0,0,.15)">'
     '<div style="font-family:Prompt;font-weight:700;font-size:23px;color:#243e1b;line-height:1.15">📌 เซฟไว้<br>ทำไมมัทฉะต้องโม่ช้า</div>'
     '<div style="font-size:14px;color:#2f4a22;margin-top:8px;text-align:left;padding-left:6px;line-height:1.45">① หินโม่ 1 ชม. ≈ 30–40 กรัม<br>② หมุนช้า = ไม่ร้อน ถนอมสีและกลิ่น<br>③ ผงละเอียดมาก → ร่อนก่อนชง</div>'
     '<div style="font-size:14px;color:#6b6a55;margin-top:10px;padding-top:8px;border-top:2px dashed #d8e3c8">ตอนหน้า 🔬 น้ำเดือดทำให้มัทฉะขม จริงไหม?</div></div>'
     '<div style="position:absolute;left:0;right:0;bottom:5%;text-align:center;font-size:14px;color:#6b6a55">Matcha Lab 🔬 · @hibimatchacafe</div>')
img=lambda n:f"url('file://{F}/s{(9 if n==11 else n):02d}.png')"
def panel(s):
    n,tc,tt,a,cam,snd,ost,vo=s
    extra=BOARD if n==10 else END if n==11 else ""
    o=f'<div class="ost">{ost}</div>' if ost!="—" and n!=11 else ""
    return (f'<div class="p"><div class="im" style="background-image:{img(n)}">{extra}<div class="no">{n:02d}</div><div class="tc">{tc}</div>{o}</div>'
            f'<div class="tx"><div class="tt">{tt}</div><div>{a}</div><div class="k"><b>🎥</b><span>{cam}</span></div><div class="k"><b>🔊</b><span>{snd}</span></div>'
            f'<div class="vo">🎙️ “{vo}”</div></div></div>')
def page(name,body):
    p=f"{O}/{name}.html"; open(p,"w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>")
    subprocess.run(["/opt/pw-browsers/chromium","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--allow-file-access-from-files",
        "--virtual-time-budget=4000",f"--screenshot={O}/{name}_raw.png",f"--window-size={W},{H+150}","file://"+p],check=True,capture_output=True)
    Image.open(f"{O}/{name}_raw.png").crop((0,0,W,H)).convert("RGB").save(f"{O}/{name}.jpg",quality=92); os.remove(f"{O}/{name}_raw.png"); os.remove(p)
HD=lambda pg:(f'<div class="hd"><h1>Matcha Lab 🔬 #2 <span>·</span> หินโม่ 1 ชม. ได้มัทฉะแค่ ~40 กรัม?</h1>'
              f'<div class="meta">Storyboard · Reels/TikTok 9:16 · ~50 วิ<span class="pill">หน้า {pg}/3</span></div></div>')
FT='<div class="ft"><span>Matcha Lab · Storyboard v1 · 10 พ.ย. 2026</span><span>ภาพประกอบ: Higgsfield (ภาพจำลอง · Hibi อ้างอิงชีตทางการ)</span></div>'
thumbs="".join(f'<div style="flex:1;text-align:center"><div style="aspect-ratio:9/16;border-radius:12px;background:{img(s[0])} center/cover;box-shadow:0 6px 14px rgba(0,0,0,.12);position:relative">'
               f'<div style="position:absolute;left:5px;top:5px;background:#a8d48a;font-family:Prompt;font-weight:700;font-size:15px;padding:1px 7px;border-radius:8px">{s[0]:02d}</div></div>'
               f'<div style="font-size:14px;margin-top:5px;color:#6b6a55">{s[1]}</div><div style="font-family:Prompt;font-weight:600;font-size:15px;color:#243e1b;line-height:1.2">{s[2]}</div></div>' for s in SH)
acts=[("⏳","ตัวเลขชวนสงสัย","01–02"),("🍃","เทนฉะ → หินโม่","03–04"),("⚙️","ข้างในหิน & ทำไมช้า","05–06"),("🔬","ละเอียดแค่ไหน · ได้กี่ถ้วย","07–09"),("📌","สรุป & เซฟไว้","10–11")]
actsH="".join(f'<div style="flex:1;background:#fff;border-radius:22px;padding:16px;text-align:center;box-shadow:0 8px 20px rgba(60,90,40,.1)"><div style="font-size:40px">{e}</div><div style="font-family:Prompt;font-weight:700;font-size:22px;color:#243e1b">{t}</div><div style="font-size:17px;color:#9a9578">ช็อต {r}</div></div>'+('<div style="align-self:center;font-size:28px;color:#7fb24a">➜</div>' if i<4 else '') for i,(e,t,r) in enumerate(acts))
cover=HD(1)+f'''
<div style="position:absolute;left:80px;top:170px;width:1260px">
 <div style="font-family:Prompt;font-weight:700;font-size:32px;color:#3f8f3a">แนวคิด</div>
 <div style="font-size:27px;line-height:1.5;margin-top:4px">เปิดด้วย<b>ตัวเลขที่ไม่น่าเชื่อ</b> — หินโม่หมุนทั้งชั่วโมงได้ผงแค่ราว 40 กรัม แล้วพาดู<b>ข้างในหินโม่</b>: ใบชา “เทนฉะ” เดินผ่านร่องหินจากกลางไปขอบ ·
 หมุนช้าเพื่อ<b>ไม่ให้ร้อน</b> · ได้ผงละเอียดกว่าเส้นผมหลายเท่า → จึงต้อง<b>ร่อนก่อนชง</b> · จบด้วยกระดานสรุป + การ์ดให้เซฟ + ปูตอนหน้า</div>
 <div style="display:flex;gap:40px;margin-top:22px;font-size:22px;line-height:1.55">
  <div><b style="font-family:Prompt;color:#243e1b">Mood</b><br>ช้า นิ่ง ประณีต → “อ๋อ เลยแพง/เลยต้องร่อน”<br><b style="font-family:Prompt;color:#243e1b">สไตล์ภาพ</b><br>สารคดี/มาโครสมจริง + ภาพจำลอง 2 ช็อต (ตัดหินโม่ · กล้องจุลทรรศน์)</div>
  <div><b style="font-family:Prompt;color:#243e1b">Key message (ให้คนเซฟ)</b><br>“โม่ช้าเพื่อไม่ให้ร้อน · ผงละเอียดจึงต้องร่อน”<br><b style="font-family:Prompt;color:#243e1b">เสียง</b><br>รอ VoiceOver (สคริปต์ใน README) · เพลงแล็บเดิม + เสียงหินโม่/ร่อนผง</div>
 </div>
</div>
<div style="position:absolute;right:80px;top:170px;width:880px;background:#fff;border-radius:26px;padding:22px 28px;box-shadow:0 10px 26px rgba(60,90,40,.12);font-size:19px;line-height:1.5">
 <div style="font-family:Prompt;font-weight:700;font-size:26px;color:#243e1b">🔎 ข้อมูลที่ใช้</div>
 <div>• หินโม่ 1 ตัว ≈ 30–40 กรัม/ชม. · ผง ~5–10 ไมครอน (ผู้ผลิตหินโม่/ร้านชา: Yunomi · Tokichi — <b>ไม่ใช่งานวิจัย</b> จึงเขียน “ราว/ประมาณ”)</div>
 <div>• ผงละเอียดมีประจุไฟฟ้าสถิต ไหลตัวไม่ดี → จับก้อน (FAO AGRIS)</div>
 <div style="margin-top:8px;padding:10px 14px;border-radius:14px;background:#fff3c4"><b>🟡 ต้องเช็กก่อนผลิต</b><br>• ช็อต 6 “หมุนช้ากันร้อน ถนอมสี/กลิ่น” — มีแหล่งเดียว (ร้านชา)<br>• ช็อต 7 เส้นผม — ความรู้ทั่วไป (~50–100 ไมครอน) ยังไม่แนบแหล่ง → ใช้คำว่า “หลายเท่า” ไม่ใส่ตัวเลข<br>• ช็อต 8 “~20 ถ้วย” = คำนวณจาก 40 ก. ÷ ~2 ก./ถ้วย</div>
 <div style="margin-top:8px;padding:10px 14px;border-radius:14px;background:#ecf8e6"><b>⚠️ ห้ามพูด</b> ว่าร้านใช้มัทฉะโม่หิน/จากแหล่งไหน (ยังรอยืนยัน) · ไม่อ้างสุขภาพ</div>
</div>
<div style="position:absolute;left:80px;right:80px;top:690px;display:flex;gap:14px">{actsH}</div>
<div style="position:absolute;left:80px;right:80px;top:870px;display:flex;gap:12px">{thumbs}</div>
'''+FT
page("SB_01_overview",cover)
notes=('<div class="p" style="padding:22px 20px;font-size:18.5px;line-height:1.5;background:#fbfdf6">'
  '<div class="tt" style="font-size:26px">📝 Production notes</div>'
  '<div style="margin-top:6px"><b>วิดีโอ (Seedance):</b> ช็อต 1–9 · ช็อต 10 ภาพนิ่ง · ช็อต 11 การ์ด</div>'
  '<div style="margin-top:8px"><b>ภาพจริงแทน AI:</b> ช็อต 9 (ร่อนผง) ใช้ภาพ/คลิปจากบรีฟ LAB-PHOTO ของ Year ได้เมื่อถ่ายเสร็จ</div>'
  '<div style="margin-top:8px"><b>Motion graphic:</b> ตัวเลข ⏳ นับเวลา · ลูกศรกลาง→ขอบ · ป้าย “ภาพจำลอง” ช็อต 5, 7 · นับถ้วย · กระดาน</div>'
  '<div style="margin-top:8px"><b>VO:</b> รออัดเสียง (เหมือนตอน 1) → ความยาวช็อตปรับตามเสียงจริง</div>'
  '<div style="margin-top:12px;padding:12px 14px;border-radius:16px;background:#fff3c4"><b>💰 เครดิต</b><br>ภาพนิ่ง 10 ภาพ (ทำแล้ว)<br>วิดีโอ 9 ช็อต 1080p ≈ 600–700</div></div>')
page("SB_02_shots",HD(2)+'<div class="row">'+"".join(panel(s) for s in SH[0:6])+'</div>'+FT)
page("SB_03_shots",HD(3)+'<div class="row">'+"".join(panel(s) for s in SH[6:11])+notes+'</div>'+FT)
ims=[Image.open(f"{O}/{n}.jpg").convert("RGB") for n in ["SB_01_overview","SB_02_shots","SB_03_shots"]]
ims[0].save(f"{O}/MatchaLab02_StoneMill_Storyboard.pdf",save_all=True,append_images=ims[1:],resolution=150)
print("ok")
