"""Storyboard: 'Hibi & Capy Holiday Jam' — 30 s Christmas / season-of-giving band reel (reuses page CSS of Matcha Lab #1)."""
import subprocess, os
from PIL import Image
_src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"../../matcha-lab-01-shade/src/build_storyboard.py"),encoding="utf-8").read()
exec(_src.split("SH=[")[0])          # D, F, O, CH, W, H, CSS (paths follow this file)
CSS+=""".vo{background:#fdecec;color:#7a2a2a} .p .ost{top:12%} .bar{display:flex;height:34px;border-radius:10px;overflow:hidden;font-family:Prompt;font-weight:600;font-size:15px;color:#fff}
.bar div{display:flex;align-items:center;justify-content:center}"""
# no, timecode, title, picture, camera/motion, beat/sound, on-screen text, music cue
SH=[
 (1,"0:00–0:02","HOOK · ตีกลองระเบิดมัทฉะ","Hibi หมวกซานต้าตีสแนร์เต็มแรง ผงมัทฉะเขียวสดระเบิดขึ้นเหมือนคอนเฟตตี ผสมเกล็ดหิมะ","Close-up มุมต่ำ · ซูมกระแทกตรงจังหวะตี","ตีบนบีต 1 + เสียง “ปุ๊ฟ” ผง","🎄 Hibi &amp; Capy<br>Holiday Jam!","เพลงเข้าช่วงกรูฟ (2:08)"),
 (2,"0:02–0:04","Capy ดีดกีตาร์","Capy ผ้ากันเปื้อนเซจ ส้มบนหัวสวมหมวกซานต้าจิ๋ว ดีดกีตาร์ โน้ตกับใบชาลอยออกมา","Medium · แพนตามมือดีด","ตัดบนบีต · โน้ตเด้งตามจังหวะ","🎸 Capy on guitar","กรูฟต่อ"),
 (3,"0:04–0:08","วงเล็กในร้านมัทฉะ","เวทีไม้ในร้าน · ต้นคริสต์มาสทำจากถ้วยชาและแปรงไม้ไผ่ · กล่องของขวัญ เขียว-ครีม-แดง","Wide · dolly-in ช้า 2 บาร์","หิมะกระดาษร่วง · ไฟกะพริบตามบีต","Season of Giving 🎁","กรูฟ 2 บาร์"),
 (4,"0:08–0:10","กล่องของขวัญเด้งเปิด","Hibi ตีกลองรัว แต่ละทีกล่องของขวัญเด้งเปิด เจอมัทฉะลาเต้ / มัทฉะสตรอว์เบอร์รีลาเต้","Top-down · ซูมกระแทกทุกบีต","กล่องเปิด 3 ที ตรง 3 บีต","เปิดกล่อง…เจอมัทฉะ! 💚","บิลด์อัป"),
 (5,"0:10–0:12","Capy โซโล่","Capy ไถลเข่าโซโล่ โน้ตกลายเป็นเกล็ดหิมะสีเขียววนรอบตัว","Low angle · whip-pan ออก","ไรเซอร์ขึ้นก่อนดรอป","—","บิลด์สุด → ดรอป"),
 (6,"0:12–0:14","DROP · โยนของขวัญ","Hibi โยนกล่องของขวัญเขียวโบว์แดงเป็นโค้ง Capy รับด้วยสองมือ ประกายตามกล่อง","Medium · speed-ramp ตอนกล่องลอย","ดรอปเต็ม (2:20)","ความสุข…ต้องส่งต่อ 🎁","ดรอป"),
 (7,"0:14–0:18","ส่งให้ลูกค้า","มุมมองลูกค้าหน้าเคาน์เตอร์: Hibi &amp; Capy ยื่นมัทฉะสตรอว์เบอร์รีลาเต้ผูกโบว์แดงมาให้","POV · push-in เข้าหาแก้ว","เสียงกระดิ่งเบา ๆ บนบีต","ส่งความสดชื่น<br>ให้คนที่คุณรัก 💚","คอรัสเต็ม"),
 (8,"0:18–0:22","แก้วเรียงเป็นของขวัญ","มัทฉะ 4 แก้วในแก้วใสทรง U ผูกโบว์ บนเคาน์เตอร์ไม้ ผงมัทฉะโรยเหมือนหิมะ","ภาพนิ่ง · ซูมกระแทกทีละแก้ว 4 บีต","“ป๊อป” ทีละแก้ว","เขียว · สด · ชื่นใจ ✨","คอรัสเต็ม"),
 (9,"0:22–0:26","ไฟนาเล่","Hibi กระโดดชูไม้กลอง Capy ชูกีตาร์ ต้นคริสต์มาสถ้วยชาไฟสว่าง ดาวใบชาบนยอด","Wide · ซูมออก + คอนเฟตตี","คอนเฟตตีตกบนบีต 1","Merry Matcha-mas! 🎄","พีกสุดท้าย"),
 (10,"0:26–0:30","End card","Hibi &amp; Capy แก้มชนกัน ถือกล่องของขวัญใหญ่ · ครึ่งบนโล่งไว้ใส่ข้อความ","ภาพนิ่ง · ตัวหนังสือเด้งตามบีต","เพลงจบเองที่ 2:38","—","จบเพลงจริง (ไม่ต้อง fade)"),
]
END=('<div style="position:absolute;left:7%;right:7%;top:13%;background:rgba(255,252,244,.96);border-radius:20px;padding:14px 10px;text-align:center;box-shadow:0 8px 20px rgba(0,0,0,.15)">'
     '<div style="font-family:Prompt;font-weight:700;font-size:22px;color:#243e1b;line-height:1.2">Merry Matcha-mas 🎄<br><span style="color:#c8323a">ส่งความสดชื่นเป็นของขวัญ</span></div>'
     '<div style="font-size:14px;color:#2f4a22;margin-top:8px;line-height:1.4">แท็กคนที่อยากส่งมัทฉะให้ 💚</div>'
     '<div style="font-size:13px;color:#6b6a55;margin-top:6px">@hibimatchacafe</div></div>')
img=lambda n:f"url('file://{F}/s{n:02d}.png')"
def panel(s):
    n,tc,tt,a,cam,snd,ost,mus=s
    o=f'<div class="ost">{ost}</div>' if ost!="—" else ""
    return (f'<div class="p"><div class="im" style="background-image:{img(n)}">{END if n==10 else ""}<div class="no">{n:02d}</div><div class="tc">{tc}</div>{o}</div>'
            f'<div class="tx"><div class="tt">{tt}</div><div>{a}</div><div class="k"><b>🎥</b><span>{cam}</span></div><div class="k"><b>🥁</b><span>{snd}</span></div>'
            f'<div class="vo">🎵 {mus}</div></div></div>')
def page(name,body):
    p=f"{O}/{name}.html"; open(p,"w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>")
    subprocess.run(["/opt/pw-browsers/chromium","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--allow-file-access-from-files",
        "--virtual-time-budget=4000",f"--screenshot={O}/{name}_raw.png",f"--window-size={W},{H+150}","file://"+p],check=True,capture_output=True)
    Image.open(f"{O}/{name}_raw.png").crop((0,0,W,H)).convert("RGB").save(f"{O}/{name}.jpg",quality=92); os.remove(f"{O}/{name}_raw.png"); os.remove(p)
HD=lambda pg:(f'<div class="hd"><h1>🎄 Hibi &amp; Capy Holiday Jam <span>·</span> วงดนตรีแห่งการให้</h1>'
              f'<div class="meta">Storyboard · Reels/TikTok 9:16 · 30 วิ · เพลง Funky Hibi Matcha<span class="pill">หน้า {pg}/3</span></div></div>')
FT='<div class="ft"><span>Holiday Jam · Storyboard v1 · 11 พ.ย. 2026</span><span>ภาพประกอบ: Higgsfield (Hibi &amp; Capy อ้างอิงชีตทางการ)</span></div>'
thumbs="".join(f'<div style="flex:1;text-align:center"><div style="aspect-ratio:9/16;border-radius:12px;background:{img(s[0])} center/cover;box-shadow:0 6px 14px rgba(0,0,0,.12);position:relative">'
               f'<div style="position:absolute;left:5px;top:5px;background:#a8d48a;font-family:Prompt;font-weight:700;font-size:15px;padding:1px 7px;border-radius:8px">{s[0]:02d}</div></div>'
               f'<div style="font-size:14px;margin-top:5px;color:#6b6a55">{s[1]}</div><div style="font-family:Prompt;font-weight:600;font-size:15px;color:#243e1b;line-height:1.2">{s[2]}</div></div>' for s in SH)
segs=[("กรูฟ · แนะนำวง",8,"#7fb24a"),("บิลด์อัป",4,"#e0a526"),("ดรอป · ส่งของขวัญ",10,"#c8323a"),("ไฟนาเล่ + End card",8,"#243e1b")]
bar="".join(f'<div style="width:{l/30*100}%;background:{c}">{t} ({l} วิ)</div>' for t,l,c in segs)
cover=HD(1)+f'''
<div style="position:absolute;left:80px;top:170px;width:1260px">
 <div style="font-family:Prompt;font-weight:700;font-size:32px;color:#3f8f3a">แนวคิด · “วงดนตรีแห่งการให้”</div>
 <div style="font-size:26px;line-height:1.5;margin-top:4px"><b>Hibi ตีกลอง · Capy เล่นกีตาร์</b> ในร้านมัทฉะที่แต่งคริสต์มาส — ทุกจังหวะกลอง = <b>ผงมัทฉะระเบิดเป็นคอนเฟตตี</b> และ<b>กล่องของขวัญเด้งเปิดเจอเครื่องดื่ม</b> ·
 ตอนเพลงดรอป เปลี่ยนจาก “เล่นดนตรี” เป็น “<b>ส่งต่อความสุข</b>” — โยนของขวัญ → ยื่นแก้วให้ลูกค้า → จบด้วยชวน<b>แท็กคนที่อยากส่งมัทฉะให้</b></div>
 <div style="display:flex;gap:40px;margin-top:20px;font-size:22px;line-height:1.55">
  <div><b style="font-family:Prompt;color:#243e1b">Mood</b><br>สด · ป๊อป · สนุก · อบอุ่น<br><b style="font-family:Prompt;color:#243e1b">พาเลต</b><br><span style="color:#4e7c3a">■</span> เขียวมัทฉะ <span style="color:#d8c9a8">■</span> ครีม <span style="color:#c8323a">■</span> แดงเชอร์รี <span style="color:#e0a526">■</span> ทองไฟ</div>
  <div><b style="font-family:Prompt;color:#243e1b">พระเอกเมนู</b><br>มัทฉะสตรอว์เบอร์รีลาเต้ (แดง-เขียว = สีคริสต์มาส)<br><b style="font-family:Prompt;color:#243e1b">ตัดต่อ</b><br>ตัดทุก 1 บาร์ (2 วิ) · ซูมกระแทกบนบีต</div>
 </div>
</div>
<div style="position:absolute;right:80px;top:170px;width:880px;background:#fff;border-radius:26px;padding:22px 28px;box-shadow:0 10px 26px rgba(60,90,40,.12);font-size:19px;line-height:1.5">
 <div style="font-family:Prompt;font-weight:700;font-size:26px;color:#243e1b">🎵 ช่วงเพลงที่ใช้</div>
 <div>Funky Hibi Matcha · ~120 BPM (1 บาร์ = 2 วิ) · ใช้ช่วง <b>2:08 → 2:38</b><br>เริ่มกรูฟเบา ๆ → บิลด์ → <b>ดรอปที่ 0:12</b> → จบเพลงจริงพอดี 30 วิ (ไม่ต้อง fade)</div>
 <div class="bar" style="margin-top:12px">{bar}</div>
 <div style="margin-top:12px;padding:10px 14px;border-radius:14px;background:#fff3c4"><b>🟡 ข้อสังเกต</b><br>• Hook ตอนเปิดใช้ภาพแรงชดเชยเพลงช่วงกรูฟที่เบากว่า (มีสำรอง: ช่วง 0:47–1:17 ดังตลอด แต่ไม่มีตอนจบ)<br>• ไม่มีเสียงพูด — สื่อด้วยภาพ + ตัวหนังสือสั้น</div>
 <div style="margin-top:8px;padding:10px 14px;border-radius:14px;background:#ecf8e6"><b>⚠️ ห้ามใส่</b> โปร/ราคา/ชุดของขวัญ/บัตรของขวัญ จนกว่าร้านยืนยัน · แก้วต้องเป็นแก้วใสทรง U</div>
</div>
<div style="position:absolute;left:80px;right:80px;top:820px;display:flex;gap:12px">{thumbs}</div>
'''+FT
page("SB_01_overview",cover)
notes=('<div class="p" style="padding:22px 20px;font-size:18.5px;line-height:1.5;background:#fbfdf6">'
  '<div class="tt" style="font-size:26px">📝 Production notes</div>'
  '<div style="margin-top:6px"><b>วิดีโอ (Seedance):</b> ช็อต 1–7, 9 (5 วิ ตัดใช้ 2–4 วิ) · ช็อต 8, 10 ภาพนิ่ง + ซูมตามบีต</div>'
  '<div style="margin-top:8px"><b>Sync:</b> ทุกคัตลงบนบีต (ตาราง beat จาก librosa) · ซูมกระแทกบีต 1 ของทุกบาร์</div>'
  '<div style="margin-top:8px"><b>Motion graphic:</b> ตัวหนังสือเด้งตามบีต · เกล็ดหิมะ/ใบชาลอย · สติกเกอร์ 🎁 🎄</div>'
  '<div style="margin-top:8px"><b>แก้ก่อนผลิต:</b> ช็อต 5 Capy ถือกีตาร์ไฟฟ้า → ทำใหม่เป็นกีตาร์โปร่งให้ตรงช็อตอื่น</div>'
  '<div style="margin-top:8px"><b>ลงโพสต์:</b> 1–24 ธ.ค. (ช่วงซื้อของขวัญ) · เปิดป้าย AI-generated</div>'
  '<div style="margin-top:12px;padding:12px 14px;border-radius:16px;background:#fff3c4"><b>💰 เครดิต</b><br>ภาพนิ่ง 10 ภาพ (ทำแล้ว)<br>วิดีโอ 8 ช็อต 1080p ≈ 550–650</div></div>')
page("SB_02_shots",HD(2)+'<div class="row">'+"".join(panel(s) for s in SH[0:5])+'</div>'+FT)
page("SB_03_shots",HD(3)+'<div class="row">'+"".join(panel(s) for s in SH[5:10])+notes+'</div>'+FT)
ims=[Image.open(f"{O}/{n}.jpg").convert("RGB") for n in ["SB_01_overview","SB_02_shots","SB_03_shots"]]
ims[0].save(f"{O}/HolidayJam_HibiCapy_Storyboard.pdf",save_all=True,append_images=ims[1:],resolution=150)
print("ok")
