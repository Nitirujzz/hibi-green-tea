import subprocess, os
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__)); O=f"{D}/ov"
FONTS="".join(f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('file:///root/.fonts/{f}-{w}-{s}.woff2') format('woff2');}}"
  for fam,f in [("Prompt","Prompt"),("Plex","IBMPlexSansThai")] for w in ([400,500,600,700] if f=="Prompt" else [400,600]) for s in ["thai","latin"])
CSS=FONTS+"""*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1920px;background:transparent;overflow:hidden;position:relative;font-family:'Prompt'}
.card{position:absolute;left:70px;width:880px;background:rgba(255,255,255,.92);border-radius:32px;box-shadow:0 12px 30px rgba(0,0,0,.18)}
.step{top:230px;display:flex;align-items:center;gap:24px;padding:22px 30px}
.num{width:96px;height:96px;border-radius:50%;background:#243e1b;color:#fff;font-weight:700;font-size:54px;display:flex;align-items:center;justify-content:center;flex:none}
.tt{font-weight:700;font-size:52px;color:#243e1b;line-height:1.1}.tp{font-family:'Plex';font-weight:600;font-size:30px;color:#4e7c3a;margin-top:4px}
.prog{position:absolute;top:196px;left:70px;width:880px;display:flex;gap:10px}.prog i{flex:1;height:8px;border-radius:4px;background:rgba(255,255,255,.45)}.prog i.on{background:#a8d48a}
"""
def prog(n): return '<div class="prog">'+''.join(f'<i class="{"on" if k<=n else ""}"></i>' for k in range(1,5))+'</div>'
def step(n,t,tip): return prog(n)+f'<div class="card step"><div class="num">{n}</div><div><div class="tt">{t}</div><div class="tp">{tip}</div></div></div>'
OV={
"hook":"""<div class="card" style="top:290px;padding:30px 40px;text-align:center">
<div style="font-weight:700;font-size:78px;line-height:1.1;color:#243e1b">มัทฉะตีมือ<br><span style="color:#4e7c3a">4 ขั้น ฟองเนียนกริบ</span></div>
<div style="font-family:'Plex';font-weight:600;font-size:34px;color:#7a5a2a;margin-top:12px">📌 เซฟไว้ ดูตอนทำเอง</div></div>""",
"s1":step(1,"ตัก + ชั่งทุกแก้ว","ปริมาณเป๊ะ รสชาติคงที่"),
"s2":step(2,"ร่อนผ่านตะแกรง","ผงไม่จับตัวเป็นก้อน"),
"s3":step(3,"ตีเป็นรูปตัว M","ได้ฟองละเอียด เนียนนุ่ม"),
"s4":step(4,"เทลงแก้วน้ำแข็ง","ดื่มตอนฟองยังนุ่ม อร่อยสุด"),
"end":"""<div class="card" style="top:1200px;padding:28px 36px;text-align:center">
<div style="font-weight:700;font-size:56px;color:#243e1b;line-height:1.15">มัทฉะตีมือ ฉบับ Hibi 🍵</div>
<div style="font-family:'Plex';font-weight:600;font-size:30px;color:#4e7c3a;margin-top:8px">ตัก · ร่อน · ตี · เท — เซฟไว้แล้วแท็กเพื่อนสายมัทฉะ 📌</div>
<div style="font-family:'Plex';font-size:26px;color:#5b5b5b;margin-top:14px">📍 Hibi Matcha Cafe 5 สาขา · LINE MAN · Grab · ShopeeFood</div></div>""",
}
for k,body in OV.items():
    p=f"{O}/{k}.html"; open(p,"w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>")
    subprocess.run(["/opt/pw-browsers/chromium","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--default-background-color=00000000",
      "--allow-file-access-from-files","--virtual-time-budget=3000",f"--screenshot={O}/{k}_raw.png","--window-size=1080,2070","file://"+p],check=True,capture_output=True)
    Image.open(f"{O}/{k}_raw.png").crop((0,0,1080,1920)).save(f"{O}/{k}.png"); os.remove(f"{O}/{k}_raw.png")
print("ok")
