"""Storyboard: 'Hibi & Capy · Small Moments' series + EP1 'จำได้ด้วย?!' (reuses page CSS of Matcha Lab #1)."""
import subprocess, os
from PIL import Image
_src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"../../matcha-lab-01-shade/src/build_storyboard.py"),encoding="utf-8").read()
exec(_src.split("SH=[")[0])
CSS+=""".vo{background:#fdeef1;color:#7a2a44} .p .ost{top:11%} .bub{font-family:Prompt}"""
# no, time, title, picture, camera, sound, on-screen text, dialogue bubble
SH=[
 (1,"0:00–0:03","HOOK · ยืนงงหน้าเมนู","Hibi ยืนเอามือแนบแก้ม จ้องเมนู มีเครื่องหมาย ? ลอยรอบหัว","Close-up · push-in ช้า","เพลงอูคูเลเล่เบา ๆ + “ติ๊ง?”","ทุกครั้งที่มาร้านด้วยกัน…","—"),
 (2,"0:03–0:06","เลือกไม่ถูก","ภาพในหัว Hibi: แก้วมัทฉะ/สตรอว์เบอร์รี/โฮจิฉะลอยหมุนรอบหัว ตาเป็นก้นหอย","Medium · หมุนวน (spin)","“วื้ด” ตามแก้วหมุน","เลือกไม่ถูกสักที 😵‍💫","“อันไหนดีอ่า…”"),
 (3,"0:06–0:09","ส่วนเขา…","Capy ยืนข้าง ๆ มอง Hibi ยิ้มอ่อน ๆ หัวใจเล็ก ๆ ลอยขึ้น","Medium · rack focus จาก Hibi → Capy","เพลงเบาลง","ส่วนเขา…","—"),
 (4,"0:09–0:12","สั่งแทนให้เลย","Capy ยกมือสั่งที่เคาน์เตอร์ หลับตายิ้มมั่นใจ มือพนักงานจดออเดอร์","Medium · ซูมกระแทกตอนพูด","“ป๊อป” ตอนขึ้นบับเบิล","—","“เหมือนเดิมครับ<br>Strawberry Latte หวาน 5g”"),
 (5,"0:12–0:15","จำได้ด้วย?!","Hibi หูตั้ง ตาเป็นประกาย หน้าแดง เอามือปิดปาก หัวใจลอย","Close-up · ซูมกระแทก + เขย่าเบา ๆ","“ดึ๋ง!” + หัวใจเด้ง","—","“จำได้ด้วยเหรอ?!”"),
 (6,"0:15–0:18","ยื่นแก้วให้","Capy เลื่อนแก้วมัทฉะสตรอว์เบอร์รีลาเต้ให้ Hibi กอดแก้วหลับตายิ้ม","Close · ตามแก้ว","เสียงน้ำแข็งกระทบแก้ว","—","“จำได้ทุกครั้งแหละ”"),
 (7,"0:18–0:21","มุมโปรดริมหน้าต่าง","นั่งข้างกันริมหน้าต่าง แสงบ่าย Hibi เอนหัวพิงไหล่ Capy","Wide จากด้านหลัง · dolly-in ช้า","เพลงอบอุ่นขึ้น","—","—"),
 (8,"0:21–0:25","End card","ชนแก้วกันบนม้านั่งไม้ หัวใจลอย · ครึ่งบนโล่งไว้ใส่ข้อความ","ภาพนิ่ง · ตัวหนังสือขึ้นทีละบรรทัด","เพลงจบ","—","—"),
]
END=('<div style="position:absolute;left:7%;right:7%;top:12%;background:rgba(255,252,244,.96);border-radius:20px;padding:14px 10px;text-align:center;box-shadow:0 8px 20px rgba(0,0,0,.15)">'
     '<div style="font-family:Prompt;font-weight:700;font-size:20px;color:#243e1b;line-height:1.3">ความรัก…<br>คือการจำเรื่องเล็ก ๆ<br>ของกันและกันได้ 💚</div>'
     '<div style="font-size:13.5px;color:#2f4a22;margin-top:8px;line-height:1.4">แท็กคนที่จำเมนูโปรดของคุณได้ 👇</div>'
     '<div style="font-size:12px;color:#6b6a55;margin-top:6px">Small Moments · Hibi &amp; Capy</div></div>')
img=lambda n:f"url('file://{F}/s{n:02d}.png')"
def panel(s):
    n,tc,tt,a,cam,snd,ost,bub=s
    o=f'<div class="ost">{ost}</div>' if ost!="—" else ""
    b=(f'<div style="position:absolute;left:8%;right:8%;bottom:9%;background:#fff;border-radius:18px;padding:8px 10px;text-align:center;font-family:Prompt;font-weight:600;font-size:17px;color:#7a2a44;box-shadow:0 6px 14px rgba(0,0,0,.18)">{bub}</div>' if bub!="—" else "")
    return (f'<div class="p"><div class="im" style="background-image:{img(n)}">{END if n==8 else ""}<div class="no">{n:02d}</div><div class="tc">{tc}</div>{o}{b}</div>'
            f'<div class="tx"><div class="tt">{tt}</div><div>{a}</div><div class="k"><b>🎥</b><span>{cam}</span></div><div class="k"><b>🔊</b><span>{snd}</span></div>'
            f'<div class="vo">💬 {bub.replace("<br>"," ") if bub!="—" else "(ไม่มีบทพูด)"}</div></div></div>')
def page(name,body):
    p=f"{O}/{name}.html"; open(p,"w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>")
    subprocess.run(["/opt/pw-browsers/chromium","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--allow-file-access-from-files",
        "--virtual-time-budget=4000",f"--screenshot={O}/{name}_raw.png",f"--window-size={W},{H+150}","file://"+p],check=True,capture_output=True)
    Image.open(f"{O}/{name}_raw.png").crop((0,0,W,H)).convert("RGB").save(f"{O}/{name}.jpg",quality=92); os.remove(f"{O}/{name}_raw.png"); os.remove(p)
HD=lambda pg:(f'<div class="hd"><h1>💚 Hibi &amp; Capy · Small Moments <span>·</span> EP1 จำได้ด้วย?!</h1>'
              f'<div class="meta">Storyboard · Reels/TikTok 9:16 · ~25 วิ · ไม่มีเสียงพากย์<span class="pill">หน้า {pg}/3</span></div></div>')
FT='<div class="ft"><span>Small Moments · Storyboard v1 · 11 พ.ย. 2026</span><span>ภาพประกอบ: Higgsfield (Hibi &amp; Capy อ้างอิงชีตทางการ)</span></div>'
EPS=[("1","จำได้ด้วย?!","สั่งเมนูโปรด + ระดับหวานให้โดยไม่ต้องถาม","จำเรื่องเล็ก ๆ ได้","แท็กคนที่จำเมนูโปรดคุณได้","★ ตอนนี้"),
     ("2","ตื่นก่อน","ค่อย ๆ ตีมัทฉะเบา ๆ กลัวอีกคนตื่น วางแก้วข้างหมอน","ดูแลแบบเงียบ ๆ","ใครชงให้คุณทุกเช้า?",""),
     ("3","คำสุดท้าย","ขนมชิ้นสุดท้าย (Noisette Financier) ดันให้กันไปมาไม่มีใครยอมกิน","ยอมให้เสมอ","แบ่งคำสุดท้ายหรือแย่ง?",""),
     ("4","ช่างภาพจำเป็น","ถ่ายให้ 30 รูป ได้ใช้ 1 รูป แต่ยังยิ้มถ่ายต่อ","ความอดทนน่ารัก ๆ","แท็กช่างภาพประจำตัว",""),
     ("5","ร่มคันเดียว","ฝนตก เอียงร่มไปทางอีกคน ไหล่ตัวเองเปียกหมด","ห่วงอีกคนก่อน","ฝนตกต้องพกใคร?",""),
     ("6","อีก 5 นาที","รอแต่งตัว “อีก 5 นาที” ×3 นั่งจิบมัทฉะรอใจเย็น","ใจเย็นให้กัน","คุณเป็นคนรอหรือคนให้รอ?",""),
     ("7","งอนแล้วง้อ","งอนเรื่องเล็ก ๆ อีกคนง้อด้วยแก้วโปรด + โน้ต “ขอโทษนะ”","ง้อเป็น","ง้อด้วยเมนูไหนได้ผล?",""),
     ("8","หลับบนไหล่","ขากลับบนรถไฟ หลับพิงไหล่ อีกคนไม่กล้าขยับจนเมื่อย","ยอมเมื่อยเพื่อกัน","แท็กหมอนประจำตัวคุณ","")]
eps="".join(f'<div style="background:{"#fff3c4" if e[5] else "#fff"};border-radius:18px;padding:12px 14px;box-shadow:0 6px 16px rgba(60,90,40,.1)">'
            f'<div style="font-family:Prompt;font-weight:700;font-size:21px;color:#243e1b">EP{e[0]} · {e[1]} <span style="font-size:15px;color:#c8323a">{e[5]}</span></div>'
            f'<div style="font-size:16.5px;line-height:1.35;margin-top:3px">{e[2]}</div>'
            f'<div style="font-size:15px;color:#4e7c3a;margin-top:5px">💚 {e[3]} · 💬 {e[4]}</div></div>' for e in EPS)
thumbs="".join(f'<div style="flex:1;text-align:center"><div style="aspect-ratio:9/16;border-radius:12px;background:{img(s[0])} center/cover;box-shadow:0 6px 14px rgba(0,0,0,.12);position:relative">'
               f'<div style="position:absolute;left:5px;top:5px;background:#a8d48a;font-family:Prompt;font-weight:700;font-size:15px;padding:1px 7px;border-radius:8px">{s[0]:02d}</div></div>'
               f'<div style="font-size:14px;margin-top:5px;color:#6b6a55">{s[1]}</div><div style="font-family:Prompt;font-weight:600;font-size:15px;color:#243e1b;line-height:1.2">{s[2]}</div></div>' for s in SH)
cover=HD(1)+f'''
<div style="position:absolute;left:80px;top:165px;width:1000px">
 <div style="font-family:Prompt;font-weight:700;font-size:32px;color:#3f8f3a">แนวคิดซีรีส์ · “Small Moments, Big Happiness”</div>
 <div style="font-size:24px;line-height:1.5;margin-top:4px">ไมโครโมเมนต์ที่คู่รักเจอ<b>ทุกวัน</b> เรื่องเล็กจนมองข้าม แต่คือความรักจริง ๆ — เล่าผ่าน <b>Hibi (สดใส ขี้ลังเล)</b> &amp; <b>Capy (ใจเย็น ช่างสังเกต)</b>
 ทุกตอนมี<b>มัทฉะเป็นส่วนหนึ่งของชีวิตคู่</b>อย่างเป็นธรรมชาติ ไม่ขายของตรง ๆ · จบด้วยประโยคให้คนดู “อิน” + คำถามชวนแท็กคนสำคัญ</div>
 <div style="display:flex;gap:30px;margin-top:16px;font-size:20px;line-height:1.5">
  <div><b style="font-family:Prompt;color:#243e1b">สูตรทุกตอน (~20–25 วิ)</b><br>① Hook: สถานการณ์ที่ทุกคู่เคยเจอ (3 วิ)<br>② อีกคนทำเรื่องเล็ก ๆ ที่น่ารัก<br>③ รีแอ็กชันเขิน/ซึ้ง<br>④ End card: ประโยคความรัก + ชวนแท็ก</div>
  <div><b style="font-family:Prompt;color:#243e1b">โทน</b><br>ละมุน อบอุ่น ตลกนิด ๆ · แสงเช้า/บ่าย<br><b style="font-family:Prompt;color:#243e1b">เสียง</b><br>อูคูเลเล่/lo-fi เบา ๆ · ไม่มีพากย์<br>บทพูดเป็นบับเบิลสั้น ๆ</div>
 </div>
</div>
<div style="position:absolute;right:80px;top:165px;width:1100px;display:grid;grid-template-columns:1fr 1fr;gap:12px">{eps}</div>
<div style="position:absolute;left:80px;right:80px;top:850px;display:flex;gap:12px">{thumbs}</div>
'''+FT
page("SB_01_overview",cover)
notes=('<div class="p" style="padding:22px 20px;font-size:18px;line-height:1.5;background:#fbfdf6">'
  '<div class="tt" style="font-size:26px">📝 Production notes</div>'
  '<div style="margin-top:6px"><b>วิดีโอ (Seedance):</b> ช็อต 1–7 · ช็อต 8 ภาพนิ่ง + ตัวหนังสือ</div>'
  '<div style="margin-top:8px"><b>บับเบิลบทพูด:</b> เด้งขึ้นพร้อมเสียง “ป๊อป” ให้อ่านทันใน ~2 วิ</div>'
  '<div style="margin-top:8px"><b>เพลง:</b> อูคูเลเล่/lo-fi ไม่มีลิขสิทธิ์ หรือสังเคราะห์เอง (music.py)</div>'
  '<div style="margin-top:8px"><b>เมนู:</b> Matcha Strawberry Latte · ระดับหวาน 5g (ระดับที่ร้านมีจริง)</div>'
  '<div style="margin-top:12px;padding:12px 14px;border-radius:16px;background:#fff3c4"><b>🟡 ให้เจ้าของร้านยืนยัน</b><br>• วาง Hibi &amp; Capy เป็น “คู่รัก” ได้ไหม (หรือเป็น “เพื่อนสนิท” ก็ใช้บทเดิมได้)</div>'
  '<div style="margin-top:8px;padding:12px 14px;border-radius:16px;background:#ecf8e6"><b>💰 เครดิต</b><br>ภาพนิ่ง 8 ภาพ (ทำแล้ว)<br>วิดีโอ 7 ช็อต ≈ 500</div></div>')
page("SB_02_shots",HD(2)+'<div class="row">'+"".join(panel(s) for s in SH[0:4])+'</div>'+FT)
page("SB_03_shots",HD(3)+'<div class="row">'+"".join(panel(s) for s in SH[4:8])+notes+'</div>'+FT)
ims=[Image.open(f"{O}/{n}.jpg").convert("RGB") for n in ["SB_01_overview","SB_02_shots","SB_03_shots"]]
ims[0].save(f"{O}/SmallMoments_EP1_Storyboard.pdf",save_all=True,append_images=ims[1:],resolution=150)
print("ok")
