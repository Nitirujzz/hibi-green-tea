# Halloween "Matcha-ween" carousel (IG 1080x1350) — Hibi & Capy costumes x real menu
import os, subprocess
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
src = open(f"{D}/build3.py").read().split("# slide 1")[0]
ns = {"__file__": f"{D}/build3.py"}; exec(src, ns)
img, CSS = ns["img"], ns["CSS"]
OUT = f"{D}/out_hw"; os.makedirs(OUT, exist_ok=True)
A = lambda n, mh=1100: img(n, "hw", maxh=mh)
TOTAL = 4
CREAM, ORANGE, LEAF, NIGHT = "#f7f1e3", "#f29a4a", "#a8d48a", "#1d2b18"

def page(n, body, css=""):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
body{{background:{NIGHT} url('{A("bg_night", 1350)}') center/cover;color:{CREAM}}}
.top{{color:{CREAM}}}.top .pg{{background:{ORANGE};color:{NIGHT}}}
.foot{{background:#121b0f}}
.art{{position:absolute;filter:drop-shadow(0 16px 24px rgba(0,0,0,.35))}}
.h1{{font-family:'Prompt';font-weight:700;line-height:1.05;letter-spacing:-1px}}
.chip{{display:inline-block;background:{ORANGE};color:{NIGHT};font-family:'Prompt';font-weight:600;font-size:26px;padding:8px 22px;border-radius:30px}}
{css}</style></head><body>
<div class="top"><span>HIBI MATCHA CAFE 日々</span><span class="pg">{n}/{TOTAL}</span></div>{body}
<div class="foot"><span>Hibi หรือ Capy? 🎃</span><span class="r">@hibimatchacafe</span></div></body></html>"""

def s1():
    css = f""".w{{position:absolute;top:100px;left:0;right:0;text-align:center}}
.t{{font-size:72px;color:{CREAM};margin-top:14px;text-shadow:0 4px 18px rgba(0,0,0,.35)}}
.s{{font-size:31px;color:#e8e1cf;margin-top:10px}}.s b{{color:{LEAF}}}.s i{{font-style:normal;color:{ORANGE}}}
.promo{{display:inline-block;margin-top:14px;font-family:'Prompt';font-weight:600;font-size:27px;color:{NIGHT};background:{ORANGE};padding:7px 22px;border-radius:26px}}
.vs{{position:absolute;top:760px;left:490px;width:100px;height:100px;border-radius:50%;background:{ORANGE};color:{NIGHT};font-family:'Prompt';font-weight:700;font-size:40px;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 20px rgba(0,0,0,.35)}}
.lb{{position:absolute;top:1120px;font-family:'Prompt';font-weight:700;font-size:34px;padding:10px 26px;border-radius:34px;box-shadow:0 8px 20px rgba(0,0,0,.3)}}
.sw{{position:absolute;right:56px;top:1206px;font-family:'Prompt';font-weight:600;font-size:24px;color:{ORANGE}}}"""
    body = f"""<div class="w"><span class="chip">🎃 Happy Matcha-ween</span>
<div class="h1 t">Halloween นี้ แต่งแบบไหนดี?</div><div class="s">แต่งแบบ <b>Hibi</b> หรือแบบ <i>Capy</i>? ปัดดูแล้วเลือกเลย</div>
<div class="promo">🎁 แต่งคอสตูมมาถ่ายรูป รับ Noisette Financier ฟรี!</div></div>
<img class="art" src="{A('art_duo')}" style="left:110px;top:430px;width:860px;height:720px;object-fit:contain">
<div class="vs">VS</div>
<div class="lb" style="left:120px;background:{LEAF};color:{NIGHT}">🐰 แบบ Hibi</div>
<div class="lb" style="right:120px;background:{ORANGE};color:{NIGHT}">🎃 แบบ Capy</div>"""
    return page(1, body, css)

CARD = f""".hd{{position:absolute;top:96px;left:56px}}
.hd .t{{font-size:64px;color:{CREAM}}}.hd .s{{font-size:26px;color:#e8e1cf;margin-top:6px}}
.cards{{position:absolute;top:250px;left:48px;right:48px;display:flex;flex-direction:column;gap:22px}}
.cd{{height:470px;border-radius:34px;background:rgba(247,241,227,.96);color:#2b2219;display:flex;align-items:center;position:relative;overflow:hidden;box-shadow:0 14px 34px rgba(0,0,0,.30)}}
.cd .ar{{width:400px;height:470px;flex:none;display:flex;align-items:center;justify-content:center;background:radial-gradient(circle at 50% 55%,#ffe7c9 0%,#f6e9d4 60%,rgba(246,233,212,0) 75%)}}
.cd .ar img{{max-width:380px;max-height:430px;filter:drop-shadow(0 10px 14px rgba(60,40,20,.2))}}
.cd .tx{{flex:1;padding:30px 24px 26px 6px;align-self:stretch;display:flex;flex-direction:column}}
.cos{{font-family:'Prompt';font-weight:700;font-size:52px;color:#c4611b;line-height:1.05}}
.arrow{{font-family:'Prompt';font-weight:500;font-size:24px;color:#7a6a5d;margin-top:12px}}
.mn{{font-family:'Prompt';font-weight:700;font-size:34px;color:#243e1b;line-height:1.15;margin-top:4px}}
.q{{font-size:24px;color:#4a3d32;line-height:1.35;margin-top:12px;max-width:330px}}
.pr{{position:absolute;left:406px;bottom:26px;font-family:'Prompt';font-weight:600;font-size:28px;color:#fff;background:#243e1b;padding:4px 18px;border-radius:24px}}
.dk{{position:absolute;right:22px;bottom:14px;height:250px;filter:drop-shadow(0 12px 14px rgba(36,62,27,.25))}}"""

def card(art, cos, menu, price, q, drink):
    return f"""<div class="cd"><div class="ar"><img src="{A(art, 900)}"></div>
<div class="tx"><div class="cos">{cos}</div><div class="arrow">แก้วคู่ชุดนี้ 👉</div><div class="mn">{menu}</div><div class="q">“{q}”</div></div>
<div class="pr">{price}</div><img class="dk" src="{img(drink)}"></div>"""

def s2():
    body = f"""<div class="hd"><div class="h1 t">🐰 แต่งแบบ <span style="color:{LEAF}">Hibi</span></div><div class="s">สายสดใส ขี้เล่น ชอบเป็นจุดสนใจ · เลือกได้ 2 ชุด</div></div>
<div class="cards">{card('hibi_ghost', '👻 ผีน้อย', 'Clear Matcha', '59.-', 'ใส ๆ ลอย ๆ แบบผีน้อย ไม่ต้องหวานก็ได้', 'clear_matcha')}
{card('hibi_witch', '🧙 แม่มด', 'Matcha Latte', '79.-', 'น้ำยาวิเศษสีเขียว ตีสด ๆ ทุกแก้ว', 'matcha_latte')}</div>"""
    return page(2, body, CARD)

def s3():
    body = f"""<div class="hd"><div class="h1 t">🎃 แต่งแบบ <span style="color:{ORANGE}">Capy</span></div><div class="s">สายชิล ใจเย็น น่ากอด · เลือกได้ 2 ชุด</div></div>
<div class="cards">{card('capy_pumpkin', '🎃 ฟักทอง', 'Hojicha Latte', '79.-', 'สีส้มน้ำตาลอุ่น ๆ หอมคั่วเหมือนขนมฟักทอง', 'hojicha_latte')}
{card('capy_vampire', '🧛 แวมไพร์', 'Matcha Strawberry Latte', '89.-', 'สีแดงสด… สตรอว์เบอร์รีจริง ไม่ใช่เลือดนะ 🍓', 'strawberry')}</div>"""
    return page(3, body, CARD)

def s4():
    css = f""".w{{position:absolute;top:96px;left:0;right:0;text-align:center}}
.t{{font-size:66px;color:{CREAM}}}.t em{{font-style:normal;color:{ORANGE}}}
.dt{{display:inline-block;margin-top:10px;font-family:'Prompt';font-weight:600;font-size:28px;color:{NIGHT};background:{LEAF};padding:6px 22px;border-radius:26px}}
.pc{{position:absolute;top:290px;left:48px;right:48px;background:rgba(247,241,227,.97);color:#2b2219;border-radius:34px;padding:30px 34px 26px;box-shadow:0 14px 34px rgba(0,0,0,.3)}}
.pc .gift{{text-align:center;font-family:'Prompt';font-weight:700;font-size:44px;color:#c4611b;line-height:1.15}}
.pc .gift b{{display:block;font-size:58px;color:#243e1b}}
.st{{display:flex;gap:14px;margin-top:22px}}
.st .i{{flex:1;background:#fbf3e4;border-radius:22px;padding:18px 14px;text-align:center}}
.st .n{{width:54px;height:54px;margin:0 auto;border-radius:50%;background:{ORANGE};color:#fff;font-family:'Prompt';font-weight:700;font-size:28px;display:flex;align-items:center;justify-content:center}}
.st .e{{font-size:46px;margin-top:8px}}.st .x{{font-family:'Prompt';font-weight:600;font-size:23px;margin-top:6px;line-height:1.25;color:#3f3229}}
.ask{{position:absolute;top:812px;left:48px;right:48px;background:rgba(18,27,15,.85);border:2px solid {ORANGE};border-radius:26px;padding:18px 24px;text-align:center}}
.ask .k{{font-size:21px;color:#e8e1cf}}.ask .v{{font-family:'Prompt';font-weight:700;font-size:34px;color:{CREAM};margin-top:2px}}
.br{{position:absolute;top:972px;left:48px;right:48px;background:rgba(18,27,15,.85);border:2px solid #3d5530;border-radius:26px;padding:18px 24px;text-align:center}}
.br .t2{{font-family:'Prompt';font-weight:600;font-size:26px}}.br .l{{font-size:21px;margin-top:6px;line-height:1.5;color:#e8e1cf}}
.note{{position:absolute;top:1170px;left:0;right:0;text-align:center;font-size:19px;color:#cfc6b2}}"""
    body = f"""<div class="w"><div class="h1 t">แต่งคอสตูมมา <em>รับขนมฟรี!</em> 🎁</div><span class="dt">📅 เสาร์ 31 ต.ค.</span></div>
<div class="pc"><div class="gift">ถ่ายรูปคู่ชุดคอสตูมฮาโลวีน รับฟรี<b>Noisette Financier 1 ชิ้น</b></div>
<div class="st"><div class="i"><div class="n">1</div><div class="e">🧙</div><div class="x">แต่งคอสตูม<br>ธีมฮาโลวีนมาร้าน</div></div>
<div class="i"><div class="n">2</div><div class="e">📸</div><div class="x">ถ่ายรูปคู่<br>แก้ว Hibi</div></div>
<div class="i"><div class="n">3</div><div class="e">🎁</div><div class="x">โชว์รูปกับพนักงาน<br>รับขนมฟรี</div></div></div></div>
<div class="ask"><div class="k">แท็ก @hibimatchacafe #HibiMatchaween · คอมเมนต์โหวต 👇</div><div class="v">แต่งแบบ Hibi 🐰 หรือ Capy 🎃?</div></div>
<div class="br"><div class="t2">📍 Hibi Matcha Cafe 5 สาขา</div><div class="l">ลาดพร้าว 107 · นาคนิวาส 48 · สะพานควาย · นวมินทร์ 111 · สามย่าน (จุฬาฯ 11)</div></div>
<div class="note">*1 ท่าน / 1 ชิ้น · เงื่อนไขเป็นไปตามที่ร้านกำหนด</div>"""
    return page(4, body, css)

for n, html in enumerate([s1(), s2(), s3(), s4()], 1):
    p = f"{OUT}/s{n}.html"; open(p, "w").write(html)
    png = f"{OUT}/HIBI_HALLOWEEN_{n:02d}.png"
    subprocess.run(["/opt/pw-browsers/chromium", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    "--allow-file-access-from-files", "--virtual-time-budget=4000", "--force-device-scale-factor=1",
                    f"--screenshot={png}", "--window-size=1080,1500", "file://" + p], check=True, capture_output=True)
    Image.open(png).crop((0, 0, 1080, 1350)).convert("RGB").save(png.replace(".png", ".jpg"), quality=94); os.remove(png)
print("done")
