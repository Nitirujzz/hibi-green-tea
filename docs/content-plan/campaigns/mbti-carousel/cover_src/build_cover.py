import re, subprocess
from PIL import Image
src = open("build2.py").read()
ns = {"__file__": __import__("os").path.abspath("build2.py")}
exec(src.split("def avatar")[0], ns)
CSS = ns["CSS"]
Image.open("hf/v2a.png").resize((1080,1350), Image.LANCZOS).save("hf/bg.jpg", quality=95)
html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
body{{background:url('file://{__import__('os').getcwd()}/hf/bg.jpg') center/cover}}
.wrap{{position:absolute;top:96px;left:0;right:0;text-align:center}}
.chip{{display:inline-block;background:#243e1b;color:#fff;font-family:'Prompt';font-weight:500;font-size:26px;padding:8px 26px;border-radius:40px;letter-spacing:.5px}}
h1{{font-family:'Prompt';font-weight:700;color:#243e1b;font-size:118px;line-height:1.08;margin-top:22px;letter-spacing:-1px;text-shadow:0 2px 0 rgba(255,255,255,.6)}}
h1 em{{font-style:normal;color:#4e7c3a}}
.sub{{font-family:'Plex';font-weight:600;font-size:30px;color:#3a5a2c;margin-top:14px}}
.team{{position:absolute;top:1188px;font-family:'Prompt';font-weight:600;font-size:23px;padding:7px 18px;border-radius:30px;background:rgba(255,255,255,.88);color:#243e1b;box-shadow:0 4px 14px rgba(36,62,27,.12)}}
.team b{{color:#4e7c3a}}
</style></head><body>
<div class="top"><span>HIBI MATCHA CAFE 日々</span><span class="pg">1/7</span></div>
<div class="wrap">
 <span class="chip">16 บุคลิก × Hibi &amp; Capy</span>
 <h1>มัทฉะแก้วไหน<br><em>คือคุณ?</em></h1>
 <div class="sub">ปัดหา MBTI ของคุณ แล้วแท็กเพื่อนที่ “ใช่เลย”</div>
</div>
<div class="team" style="left:36px">ทีม Hibi · <b>สาย E</b></div>
<div class="team" style="right:36px">ทีม Capy · <b>สาย I</b></div>
<div class="foot"><span>ปัดหาแก้วของคุณ 👉</span><span class="r">5 สาขา · Delivery</span></div>
</body></html>"""
open("hf/cover.html","w").write(html)
subprocess.run(["/opt/pw-browsers/chromium","--headless=new","--no-sandbox","--hide-scrollbars","--window-size=1080,1500","--screenshot=hf/cover_raw.png","file://"+__import__('os').getcwd()+"/hf/cover.html"],capture_output=True)
Image.open("hf/cover_raw.png").convert("RGB").crop((0,0,1080,1350)).save("hf/HIBI_MBTI_01.jpg",quality=93)
