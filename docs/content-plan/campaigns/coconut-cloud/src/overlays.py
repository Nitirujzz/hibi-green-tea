import subprocess, base64, io, os
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__))
FONTS="".join(f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('file:///root/.fonts/{f}-{w}-{s}.woff2') format('woff2');}}"
  for fam,f in [("Prompt","Prompt"),("Plex","IBMPlexSansThai")] for w in ([400,500,600,700] if f=="Prompt" else [400,600]) for s in ["thai","latin"])
def b64(p):
    b=io.BytesIO(); Image.open(p).save(b,"PNG"); return "data:image/png;base64,"+base64.b64encode(b.getvalue()).decode()
CSS=FONTS+"""*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1920px;background:transparent;overflow:hidden;position:relative}
.box{position:absolute;left:70px;width:880px;text-align:center;font-family:'Prompt'}
.pill{display:inline-block;background:#243e1b;color:#fff;font-weight:600;font-size:34px;padding:10px 28px;border-radius:40px}
.big{font-weight:700;font-size:96px;line-height:1.08;color:#243e1b;text-shadow:0 3px 0 rgba(255,255,255,.85),0 0 30px rgba(255,255,255,.9)}
.big em{font-style:normal;color:#4e7c3a}
.mid{font-weight:600;font-size:46px;color:#243e1b;text-shadow:0 2px 0 rgba(255,255,255,.9),0 0 22px rgba(255,255,255,.95)}
.card{display:inline-block;background:rgba(255,255,255,.92);border-radius:34px;padding:22px 34px;box-shadow:0 10px 30px rgba(36,62,27,.15)}
"""
OV={
"o1":"""<div class="box" style="top:250px"><span class="pill">เทรนด์ TikTok 2026 ☁️</span>
<div class="big" style="margin-top:22px">Coconut Cloud<br><em>มีที่ Hibi แล้ว!</em></div></div>""",
"o2":"""<div class="box" style="top:300px"><div class="mid">มัทฉะคลาวด์ ลอยบนน้ำมะพร้าวใส 🥥</div></div>""",
"o3":"""<div class="box" style="top:1130px"><div class="card"><div style="font-weight:700;font-size:68px;color:#243e1b;line-height:1.1">Coconut Cloud</div>
<div style="font-family:'Plex';font-weight:600;font-size:32px;color:#4e7c3a;margin-top:6px">น้ำมะพร้าวใส × มัทฉะคลาวด์โฟม</div>
<div style="margin-top:14px"><span class="pill" style="font-size:30px">สดชื่น · ใส · เบา ๆ</span></div></div></div>""",
}
END=f"""<div style="position:absolute;inset:0;background:rgba(243,248,236,.82)"></div>
<div class="box" style="top:300px"><div class="big" style="font-size:84px">ลองแก้ว Cloud<br><em>ของจริงที่ Hibi</em></div></div>
<img src="{b64(D+'/art_end.png')}" style="position:absolute;left:215px;top:620px;width:650px;height:560px;object-fit:contain;filter:drop-shadow(0 14px 18px rgba(36,62,27,.15))">
<div class="box" style="top:1200px"><div class="card" style="background:#243e1b;color:#fff;width:880px">
<div style="font-weight:600;font-size:38px">📍 Hibi Matcha Cafe 5 สาขา</div>
<div style="font-family:'Plex';font-size:27px;margin-top:6px;opacity:.95">ลาดพร้าว 107 · นาคนิวาส 48 · สะพานควาย · นวมินทร์ 111 · สามย่าน</div>
<div style="font-family:'Plex';font-size:25px;margin-top:6px;color:#cfe6bd">Delivery: LINE MAN · Grab · ShopeeFood</div></div></div>"""
OV["hook"]="""<div class="box" style="top:300px"><div class="card" style="padding:26px 40px;background:rgba(255,255,255,.88)">
<div style="font-weight:700;font-size:92px;line-height:1.05;color:#243e1b">มัทฉะ<span style="color:#4e7c3a"> × </span>น้ำมะพร้าว</div>
<div style="font-weight:600;font-size:46px;color:#4e7c3a;margin-top:10px">เคยลองแบบใส ๆ ยัง? ☁️🥥</div></div></div>"""
OV["oreal"]="""<div class="box" style="top:1260px"><div class="card" style="font-weight:600;font-size:40px;color:#243e1b">มัทฉะคลาวด์ ลอยบนน้ำมะพร้าวใส 🥥</div></div>"""
OV["end"]=END
for k,body in OV.items():
    p=f"{D}/{k}.html"; open(p,"w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>")
    subprocess.run(["/opt/pw-browsers/chromium","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--default-background-color=00000000",
      "--allow-file-access-from-files","--virtual-time-budget=3000",f"--screenshot={D}/{k}_raw.png","--window-size=1080,2070","file://"+p],check=True,capture_output=True)
    Image.open(f"{D}/{k}_raw.png").crop((0,0,1080,1920)).save(f"{D}/{k}.png"); os.remove(f"{D}/{k}_raw.png")
print("ok")
