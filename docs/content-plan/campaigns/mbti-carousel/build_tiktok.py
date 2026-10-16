# TikTok photo-mode version (1080x1920). Safe zone: x 70-950, y 190-1440 (bottom = caption/music, right = buttons)
import os, subprocess
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
src = open(f"{D}/build3.py").read().split("# slide 1")[0]
ns = {"__file__": f"{D}/build3.py"}; exec(src, ns)
img, avatar, GROUPS, FONTS = ns["img"], ns["avatar"], ns["GROUPS"], ns["FONTS"]
ART = lambda n: img(n, "art", maxh=1100)
OUT = f"{D}/out_tk"; os.makedirs(OUT, exist_ok=True)
TOTAL = 10  # TikTok photo posts: max 10 images
W, H = 1080, 1920

BASE = FONTS + """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px}
body{overflow:hidden;font-family:'Plex',sans-serif;color:#1d2b18;position:relative}
.P{font-family:'Prompt',sans-serif}
.top{position:absolute;top:196px;left:70px;width:880px;display:flex;justify-content:space-between;align-items:center;font-family:'Prompt';font-size:24px;color:#243e1b;letter-spacing:1.5px}
.top .pg{background:#243e1b;color:#fff;border-radius:20px;padding:4px 16px;font-size:22px;letter-spacing:0}
.av{border-radius:50%;overflow:hidden;display:inline-block;vertical-align:middle;padding:3px}
.av img{width:100%;height:100%;border-radius:50%;display:block;object-fit:cover}
.av.h{background:#4e7c3a}.av.c{background:#a8744a}
.cut{filter:drop-shadow(0 18px 16px rgba(36,62,27,.20))}
.art{position:absolute;filter:drop-shadow(0 14px 18px rgba(36,62,27,.14))}
.swipe{position:absolute;left:70px;width:880px;top:1380px;text-align:center;font-family:'Prompt';font-weight:600;font-size:30px;color:#4e7c3a}
"""

def page(n, body, css="", bg=True, swipe="ปัดต่อ 👉"):
    bgcss = f"body{{background:#f3f8ec url('{img('bg_paper_tk', 'assets', maxh=1920)}') center/cover}}" if bg else ""
    sw = f'<div class="swipe">{swipe}</div>' if swipe else ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{BASE}{bgcss}{css}</style></head><body>
<div class="top"><span>HIBI MATCHA CAFE 日々</span><span class="pg">{n}/{TOTAL}</span></div>{body}{sw}</body></html>"""

COVER = """
body{background:url('COVERBG') center/cover}
.wrap{position:absolute;top:258px;left:70px;width:880px;text-align:center}
.chip{display:inline-block;background:#243e1b;color:#fff;font-family:'Prompt';font-weight:500;font-size:32px;padding:10px 30px;border-radius:40px}
h1{font-family:'Prompt';font-weight:700;color:#243e1b;font-size:124px;line-height:1.04;margin-top:18px;letter-spacing:-2px;text-shadow:0 2px 0 rgba(255,255,255,.6)}
h1 em{font-style:normal;color:#4e7c3a}
.sub{font-family:'Plex';font-weight:600;font-size:34px;color:#3a5a2c;margin-top:16px}
.teams{display:flex;justify-content:center;gap:12px;margin-top:14px}
.team{font-family:'Prompt';font-weight:600;font-size:27px;padding:6px 20px;border-radius:34px;background:rgba(255,255,255,.92);color:#243e1b;box-shadow:0 4px 14px rgba(36,62,27,.12)}
.team b{color:#4e7c3a}
"""
def cover():
    css = COVER.replace("COVERBG", img("cover_tk", "assets", maxh=1920))
    body = """<div class="wrap"><span class="chip">16 บุคลิก × Hibi &amp; Capy</span>
<h1>มัทฉะแก้วไหน<br><em>คือคุณ?</em></h1>
<div class="teams"><span class="team">ทีม Hibi · <b>สาย E</b></span><span class="team">ทีม Capy · <b>สาย I</b></span></div></div>"""
    return page(1, body, css, bg=False, swipe=None)

XCSS = """
.h1{position:absolute;top:270px;left:70px;width:880px;text-align:center;font-family:'Prompt';font-weight:700;font-size:96px;color:#243e1b;line-height:1.05}
.h2{position:absolute;top:390px;left:70px;width:880px;text-align:center;font-size:31px;color:#3f5236}
.pairs{position:absolute;top:780px;left:70px;width:880px;display:flex;flex-direction:column;gap:14px}
.pr{height:132px;background:rgba(255,255,255,.95);border-radius:28px;display:flex;align-items:center;padding:0 20px;box-shadow:0 8px 22px rgba(36,62,27,.07)}
.pr .s{flex:1;display:flex;align-items:center;gap:14px}
.pr .s.r{flex-direction:row-reverse;text-align:right}
.pr .L{width:84px;height:84px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;font-family:'Prompt';font-weight:700;font-size:46px;color:#fff}
.pr .w{font-family:'Prompt';font-weight:600;font-size:28px;color:#1d2b18;line-height:1.15}
.pr .d{font-size:21px;color:#5b6a53;line-height:1.3;margin-top:2px}
.pr .vs{font-family:'Prompt';font-weight:600;font-size:20px;color:#9aa892;padding:0 6px}
.lab{position:absolute;top:690px;font-family:'Prompt';font-weight:600;font-size:26px;padding:6px 18px;border-radius:24px;box-shadow:0 6px 16px rgba(0,0,0,.08)}
"""
def explain():
    pairs = [("E", "ชาร์จพลังจากคน", "เจอเพื่อนแล้วสดชื่น", "#4e7c3a", "I", "ชาร์จพลังคนเดียว", "ขออยู่เงียบ ๆ กับแก้วโปรด", "#a8744a"),
             ("S", "ดูของจริงตรงหน้า", "เชื่อสิ่งที่ลองแล้ว", "#5d7a2a", "N", "มองภาพรวม/อนาคต", "ชอบไอเดียใหม่ ๆ", "#243e1b"),
             ("T", "ใช้เหตุผล", "ตัดสินจากข้อมูล", "#243e1b", "F", "ใช้ความรู้สึก", "ตัดสินจากใจ", "#4e7c3a"),
             ("J", "ชอบวางแผน", "รู้แล้วว่าจะสั่งอะไร", "#5d7a2a", "P", "ยืดหยุ่น", "ไปถึงร้านค่อยเลือก", "#a06b17")]
    rows = "".join(f"""<div class="pr"><div class="s"><div class="L" style="background:{c1}">{a}</div><div><div class="w">{w1}</div><div class="d">{d1}</div></div></div>
<div class="vs">VS</div><div class="s r"><div class="L" style="background:{c2}">{b}</div><div><div class="w">{w2}</div><div class="d">{d2}</div></div></div></div>"""
                   for a, w1, d1, c1, b, w2, d2, c2 in pairs)
    body = f"""<div class="h1">MBTI อ่านยังไง?</div><div class="h2">4 ตัวอักษร = 4 คู่นิสัย เลือกฝั่งที่ “ใช่”</div>
<img class="art" src="{ART('explain')}" style="left:180px;top:450px;width:660px;height:300px;object-fit:contain">
<div class="lab" style="left:70px;background:#e3eedb;color:#243e1b">E = ทีม Hibi</div>
<div class="lab" style="left:720px;background:#f4ead9;color:#6f4529">I = ทีม Capy</div>
<div class="pairs">{rows}</div>"""
    return page(2, body, XCSS, swipe="4 กลุ่ม 16 บุคลิก ปัดหาของคุณ 👉")

GCSS = """
.hd{position:absolute;top:262px;left:70px;width:600px}
.hd .code{font-family:'Prompt';font-weight:700;font-size:104px;line-height:.95;letter-spacing:-3px}
.hd .nm{font-family:'Prompt';font-weight:600;font-size:42px;line-height:1.1;margin-top:4px}
.hd .nm small{font-size:24px;font-weight:500;opacity:.6;margin-left:10px}
.hd .kw{display:inline-block;margin-top:12px;font-family:'Prompt';font-weight:500;font-size:22px;padding:6px 16px;border-radius:24px;color:#fff}
.cards{position:absolute;top:540px;left:70px;width:880px;display:flex;flex-direction:column;gap:22px}
.cd{height:410px;border-radius:34px;background:rgba(255,255,255,.95);display:flex;position:relative;box-shadow:0 12px 30px rgba(36,62,27,.09)}
.cd .pic{width:290px;flex:none;border-radius:34px 0 0 34px;display:flex;align-items:center;justify-content:center}
.cd .pic img{max-height:380px;max-width:260px}
.cd .tx{flex:1;padding:24px 24px 20px 26px;min-width:0;display:flex;flex-direction:column}
.cd .mb{font-family:'Prompt';font-weight:700;font-size:72px;line-height:1;letter-spacing:-1px}
.cd .nick{font-family:'Prompt';font-weight:600;font-size:32px;color:#1d2b18;margin-top:6px;line-height:1.15}
.cd .nick small{display:block;font-weight:400;font-size:20px;color:#7b8a72}
.cd .tr{display:flex;flex-wrap:wrap;gap:7px;margin-top:12px}
.cd .tr span{font-family:'Prompt';font-size:20px;font-weight:500;padding:3px 12px;border-radius:14px}
.cd .en{font-family:'Prompt';font-weight:600;font-size:24px;line-height:1.2;margin-top:14px;color:#1d2b18}
.cd .q{font-size:21px;line-height:1.3;margin-top:6px;color:#3a4a33}
.cd .bt{margin-top:auto;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.team{display:inline-flex;align-items:center;gap:7px;font-family:'Prompt';font-weight:500;font-size:19px;padding:3px 14px 3px 3px;border-radius:24px}
.price{font-family:'Prompt';font-weight:600;font-size:24px;color:#fff;border-radius:22px;padding:3px 14px}
.sweet{font-family:'Prompt';font-weight:500;font-size:19px;border-radius:22px;padding:5px 12px;color:#243e1b}
"""
def group_page(n, g, part, last=False):
    code, name, ename, kw, tag, col, tint, art, items = g
    cards = ""
    for t, nick, enick, traits, a, en, th, price, sw, q in items[part*2:part*2+2]:
        team = (f'<span class="team" style="background:#e3eedb;color:#243e1b">{avatar("H",32)}ทีม Hibi</span>' if t[0] == "E"
                else f'<span class="team" style="background:#f4ead9;color:#6f4529">{avatar("C",32)}ทีม Capy</span>')
        swtxt = sw if not sw.endswith("g") else f"หวาน {sw}"
        trs = "".join(f'<span style="background:{tint};color:{col}">{x}</span>' for x in traits)
        pst = "" if price.endswith(".-") else "font-size:19px;padding:5px 12px"
        cards += f"""<div class="cd"><div class="pic" style="background:{tint}"><img class="cut" src="{img(a)}"></div>
<div class="tx"><div class="mb" style="color:{col}">{t}</div><div class="nick">{nick}<small>{enick}</small></div>
<div class="tr">{trs}</div><div class="en">{en}</div><div class="q">“{q}”</div>
<div class="bt"><span class="sweet" style="background:{tint}">{swtxt}</span><span class="price" style="background:{col};{pst}">{price}</span>{team}</div></div></div>"""
    body = f"""<div class="hd"><div class="code" style="color:{col}">{code}</div>
<div class="nm" style="color:{col}">{name}<small>{ename} · {part+1}/2</small></div>
<div class="kw" style="background:{col}">{kw}</div></div>
<img class="art" src="{ART(art)}" style="left:680px;top:250px;width:270px;height:270px;object-fit:contain">
<div class="cards">{cards}</div>"""
    return page(n, body, GCSS, swipe="คอมเมนต์ MBTI + ทีมของคุณ 👇" if last else "ปัดต่อ 👉")

SCSS = """
.h1{position:absolute;top:262px;left:70px;font-family:'Prompt';font-weight:700;font-size:84px;color:#243e1b;line-height:1.05}
.h2{position:absolute;top:366px;left:72px;width:600px;font-size:26px;color:#3f5236;line-height:1.35}
.grid{position:absolute;top:520px;left:70px;width:880px;display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.dt{background:rgba(255,255,255,.95);border-radius:26px;padding:20px 10px;text-align:center;box-shadow:0 8px 22px rgba(36,62,27,.07)}
.dt .c{width:96px;height:96px;border-radius:50%;margin:0 auto;display:flex;align-items:center;justify-content:center;font-family:'Prompt';font-weight:600;font-size:32px;color:#fff}
.dt .l{font-family:'Prompt';font-weight:600;font-size:24px;margin-top:10px}
.dt .m{font-size:20px;color:#4e7c3a;margin-top:4px;line-height:1.3}
.row2{position:absolute;top:1010px;left:70px;width:880px;display:grid;grid-template-columns:1fr 1fr;gap:14px}
.cd{background:rgba(255,255,255,.95);border-radius:28px;padding:22px 24px;height:330px;box-shadow:0 8px 22px rgba(36,62,27,.07)}
.cd h3{font-family:'Prompt';font-weight:600;font-size:28px;color:#243e1b;margin-bottom:6px;display:flex;align-items:center;gap:10px}
.cd .r{display:flex;justify-content:space-between;font-size:22px;padding:9px 0;border-bottom:1px solid #edf3e7}
.cd.dk{background:#243e1b;color:#fff}.cd.dk h3{color:#fff}
.cd.dk p{font-size:21px;line-height:1.4;margin-bottom:10px}
"""
def sweet():
    lv = [("0g", "ไม่หวานเลย", "INTJ", "#bcd9a6"), ("3g", "หวานถึงรสชาติ", "INTP · INFJ", "#9cc683"), ("5g", "หวานเล็กน้อย", "ISFJ · ESTJ<br>ENTJ · ISTP", "#7fb064"),
          ("8g", "หวานปกติ", "ISTJ · ISFP<br>ESTP", "#619447"), ("10g", "หวานชื่นใจ", "ENFP · ESFJ<br>ESFP", "#467334"), ("15g", "หวานจัดเต็ม", "สายหวานจัด", "#243e1b")]
    dots = "".join(f'<div class="dt"><div class="c" style="background:{c}">{g}</div><div class="l">{l}</div><div class="m">{m}</div></div>' for g, l, m, c in lv)
    milk = "".join(f'<div class="r"><span>{a}</span><b class="P" style="font-weight:600">{b}</b></div>' for a, b in [("นมสด", "ฟรี"), ("Lactose Free", "+10.-"), ("Oat Milk", "+20.-"), ("Almond Milk", "+25.-")])
    body = f"""<div class="h1">สั่งหวาน<br>แค่ไหนดี?</div>
<img class="art" src="{ART('sweet')}" style="left:660px;top:250px;width:290px;height:260px;object-fit:contain">
<div class="grid">{dots}</div>
<div class="row2"><div class="cd"><h3>🥛 เปลี่ยนนมได้</h3>{milk}</div>
<div class="cd dk"><h3>{avatar("C",42)}Capy แนะนำ</h3><p>🍵 มือใหม่เริ่ม 5–8g</p><p>☁️ Cloud Latte / Thai Tea × Matcha สูตรคงที่</p><p>✨ อยากนุ่ม เพิ่ม Velvet Milk Foam</p></div></div>"""
    return page(11, body, SCSS, swipe="📌 เซฟไว้ก่อนสั่งครั้งหน้า")

ECSS = """
.h1{position:absolute;top:268px;left:70px;width:880px;text-align:center;font-family:'Prompt';font-weight:700;font-size:100px;color:#243e1b;line-height:1.05}
.h2{position:absolute;top:390px;left:70px;width:880px;text-align:center;font-size:32px;color:#3f5236}
.box{position:absolute;top:880px;left:110px;width:800px;background:#fff;border-radius:30px;padding:24px 30px;text-align:center;box-shadow:0 10px 26px rgba(36,62,27,.09)}
.box .k{font-size:22px;color:#66745e}.box .v{font-family:'Prompt';font-weight:600;font-size:38px;color:#243e1b;margin-top:4px}
.br{position:absolute;top:1060px;left:70px;width:880px;background:#243e1b;color:#fff;border-radius:30px;padding:24px 26px;text-align:center}
.br .t{font-family:'Prompt';font-weight:600;font-size:30px}
.br .l{font-size:23px;margin-top:8px;line-height:1.5}
.br .d{font-size:21px;margin-top:8px;color:#cfe6bd}
.disc{position:absolute;top:1290px;left:70px;width:880px;text-align:center;font-size:19px;color:#7b8a72}
"""
def end():
    body = f"""<div class="h1">คุณคือ<br>MBTI ไหน?</div>
<img class="art" src="{ART('end')}" style="left:190px;top:500px;width:640px;height:370px;object-fit:contain">
<div class="box"><div class="k">คอมเมนต์แบบนี้เลย 👇</div><div class="v">“INFP · ทีม Capy”</div></div>
<div class="br"><div class="t">📍 Hibi Matcha Cafe 5 สาขา</div>
<div class="l">ลาดพร้าว 107 · นาคนิวาส 48 · สะพานควาย<br>นวมินทร์ 111 · สามย่าน (จุฬาฯ 11)</div>
<div class="d">Delivery: LINE MAN · Grab · ShopeeFood</div></div>
<div class="disc">*เพื่อความสนุก ไม่ใช่แบบทดสอบจริง · เมนู/ราคาอาจต่างกันแต่ละสาขา</div>"""
    return page(12, body, ECSS.replace("top:390px", "top:9999px"), swipe=None)

slides = [cover(), explain()]
for g in GROUPS:
    slides += [group_page(len(slides) + 1, g, 0), group_page(len(slides) + 2, g, 1, last=g is GROUPS[-1])]
for n, html in enumerate(slides, 1):
    p = f"{OUT}/t{n}.html"; open(p, "w").write(html)
    png = f"{OUT}/HIBI_MBTI_TT_{n:02d}.png"
    subprocess.run(["/opt/pw-browsers/chromium", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    "--allow-file-access-from-files", "--virtual-time-budget=4000", "--force-device-scale-factor=1",
                    f"--screenshot={png}", "--window-size=1080,2070", "file://" + p], check=True, capture_output=True)
    Image.open(png).crop((0, 0, W, H)).convert("RGB").save(png.replace(".png", ".jpg"), quality=93)
    os.remove(png)
print("done", len(slides))
