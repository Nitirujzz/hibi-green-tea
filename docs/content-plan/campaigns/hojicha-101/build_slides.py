# Hojicha 101 carousel (IG 1080x1350) — reuses the MBTI v3 design system (fonts, paper bg, avatars)
import os, subprocess
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
src = open(f"{D}/build3.py").read().split("# slide 1")[0]
ns = {"__file__": f"{D}/build3.py"}; exec(src, ns)
img, avatar, CSS = ns["img"], ns["avatar"], ns["CSS"]
OUT = f"{D}/out_hoji"; os.makedirs(OUT, exist_ok=True)
H = lambda n, mh=1100: img(n, "hoji", maxh=mh)
TOTAL = 7
BR, BRM, BRT = "#6b3f22", "#a0673c", "#f4e8da"   # hojicha browns
GR, GRM, GRT = "#243e1b", "#4e7c3a", "#e3eedb"   # matcha greens

def page(n, body, css=""):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
body{{background:#f3f8ec url('{img("bg_paper", "assets", maxh=1350)}') center/cover}}
.art{{position:absolute;filter:drop-shadow(0 14px 18px rgba(60,40,20,.15))}}
.h1{{font-family:'Prompt';font-weight:700;line-height:1.05;letter-spacing:-1px}}
.cardw{{background:rgba(255,255,255,.95);border-radius:28px;box-shadow:0 10px 26px rgba(60,40,20,.08)}}
.swipe{{position:absolute;right:56px;top:1206px;font-family:'Prompt';font-weight:600;font-size:24px;color:{BRM}}}
{css}</style></head><body>
<div class="top"><span>HIBI MATCHA CAFE 日々</span><span class="pg">{n}/{TOTAL}</span></div>{body}
<div class="foot"><span>Hojicha 101 🍂</span><span class="r">@hibimatchacafe</span></div></body></html>"""

def s1():
    css = f""".chip{{position:absolute;top:104px;left:56px;background:{BR};color:#fff;font-family:'Prompt';font-weight:600;font-size:26px;padding:8px 22px;border-radius:30px}}
.t1{{position:absolute;top:166px;left:56px;font-size:88px;color:{GR}}}
.t2{{position:absolute;top:262px;left:56px;font-size:118px;color:{BR}}}
.sub{{position:absolute;top:404px;left:60px;font-size:31px;color:#5b4a3c}}"""
    body = f"""<div class="chip">Hojicha 101</div><div class="h1 t1">ไม่ชอบมัทฉะขม?</div>
<div class="h1 t2">ลอง “โฮจิฉะ” 🍂</div><div class="sub">ชาเขียวคั่ว · หอมคาราเมล · ขมน้อย · ดื่มง่าย</div>
<img class="art" src="{H('art_cover')}" style="left:130px;top:470px;width:820px;height:740px;object-fit:contain">
<div class="swipe">ปัดดูให้รู้จัก 👉</div>"""
    return page(1, body, css)

def s2():
    facts = [("🔥", "ชาเขียวญี่ปุ่นที่นำไป “คั่ว”", "ใช้ใบชาและก้าน คั่วด้วยไฟแรงจนเป็นสีน้ำตาลแดง"),
             ("🍂", "คั่วแล้ว ขมน้อยลง", "ได้กลิ่นคั่วหอม รสนุ่ม ดื่มง่ายสำหรับมือใหม่"),
             ("🌙", "คาเฟอีน มักน้อยกว่ามัทฉะ*", "ดื่มช่วงบ่าย–เย็นได้สบายขึ้น")]
    rows = "".join(f"""<div class="cardw fc"><div class="ic">{e}</div><div><div class="ft">{t}</div><div class="fd">{d}</div></div></div>""" for e, t, d in facts)
    css = f""".h{{position:absolute;top:96px;left:56px;font-size:72px;color:{BR}}}
.ph{{position:absolute;top:196px;left:56px;width:968px;height:470px;border-radius:30px;object-fit:cover;object-position:50% 78%;box-shadow:0 10px 26px rgba(60,40,20,.12)}}
.lab{{position:absolute;top:620px;font-family:'Prompt';font-weight:600;font-size:22px;padding:5px 16px;border-radius:20px;background:rgba(255,255,255,.92)}}
.fs{{position:absolute;top:690px;left:56px;right:56px;display:flex;flex-direction:column;gap:14px}}
.fc{{display:flex;align-items:center;gap:22px;padding:20px 26px;height:146px}}
.fc .ic{{width:86px;height:86px;border-radius:50%;background:{BRT};display:flex;align-items:center;justify-content:center;font-size:44px;flex:none}}
.ft{{font-family:'Prompt';font-weight:600;font-size:33px;color:{BR}}}
.fd{{font-size:23px;color:#5b4a3c;margin-top:4px}}
.note{{position:absolute;top:1222px;left:60px;font-size:17px;color:#8a7b6e}}"""
    body = f"""<div class="h1 h">โฮจิฉะ คืออะไร?</div><img class="ph" src="{H('photo_leaves', 1000)}">
<div class="lab" style="left:80px;color:{GRM}">ใบชาเขียว</div><div class="lab" style="left:820px;color:{BR}">คั่วแล้ว = โฮจิฉะ</div>
<div class="fs">{rows}</div><div class="note">*ปริมาณคาเฟอีนขึ้นกับชนิดใบชาและสูตรของแต่ละแก้ว</div>"""
    return page(2, body, css)

def s3():
    rows = [("วิธีทำ", "ใบชาปลูกในร่ม บดเป็นผง", "ใบชาและก้าน นำไปคั่ว"),
            ("สี", "เขียวสด", "น้ำตาลแดง"),
            ("รสชาติ", "อูมามิ สดชื่น ขมนิด ๆ", "หอมคั่ว คาราเมล ขมน้อย"),
            ("คาเฟอีน", "สูงกว่า", "มักน้อยกว่า"),
            ("เหมาะกับ", "สายชาเข้ม อยากตื่นตัว", "มือใหม่ · สายกาแฟ · ดื่มบ่าย")]
    tr = "".join(f"""<div class="r"><div class="k">{k}</div><div class="c g">{a}</div><div class="c b">{b}</div></div>""" for k, a, b in rows)
    css = f""".h{{position:absolute;top:96px;left:0;right:0;text-align:center;font-size:76px}}
.tb{{position:absolute;top:560px;left:48px;right:48px;padding:16px 18px}}
.hd{{display:flex;gap:10px;margin-bottom:6px}}.hd div{{flex:1;text-align:center;font-family:'Prompt';font-weight:700;font-size:34px;padding:10px;border-radius:18px;color:#fff}}
.hd .k0{{flex:0 0 150px;background:none}}
.r{{display:flex;gap:10px;align-items:stretch;border-top:1px solid #efe7dc}}
.r .k{{flex:0 0 150px;font-family:'Prompt';font-weight:600;font-size:27px;color:#5b4a3c;display:flex;align-items:center;padding:28px 4px}}
.r .c{{flex:1;font-size:28px;line-height:1.3;padding:28px 16px;display:flex;align-items:center}}
.r .g{{color:{GR}}}.r .b{{color:{BR};background:{BRT}55}}"""
    body = f"""<div class="h1 h"><span style="color:{GRM}">มัทฉะ</span> <span style="font-size:52px;color:#9a8b7e">vs</span> <span style="color:{BR}">โฮจิฉะ</span></div>
<img class="art" src="{H('art_vs')}" style="left:140px;top:190px;width:800px;height:360px;object-fit:contain">
<div class="cardw tb"><div class="hd"><div class="k0"></div><div style="background:{GRM}">🍵 มัทฉะ</div><div style="background:{BRM}">🍂 โฮจิฉะ</div></div>{tr}</div>"""
    return page(3, body, css)

def s4():
    fl = [("🔥", "หอมคั่ว"), ("🍯", "คาราเมล"), ("🥜", "ถั่วอบ"), ("🍫", "โกโก้อ่อน ๆ"), ("🪵", "ไม้หอม")]
    ch = "".join(f'<div class="fl"><div class="e">{e}</div><div class="n">{n}</div></div>' for e, n in fl)
    likes = [("☕", "ลาเต้ / กาแฟนม"), ("🧋", "ชานมคาราเมล"), ("🍪", "ขนมอบ หอมเนย")]
    lk = "".join(f'<div class="cardw lk"><span class="e">{e}</span>{t}</div>' for e, t in likes)
    css = f""".h{{position:absolute;top:96px;left:56px;font-size:72px;color:{BR}}}
.s{{position:absolute;top:186px;left:58px;font-size:28px;color:#5b4a3c}}
.fls{{position:absolute;top:262px;left:48px;right:48px;display:flex;justify-content:space-between}}
.fl{{width:186px;text-align:center}}
.fl .e{{width:150px;height:150px;margin:0 auto;border-radius:50%;background:{BRT};display:flex;align-items:center;justify-content:center;font-size:70px;box-shadow:0 8px 20px rgba(60,40,20,.10)}}
.fl .n{{font-family:'Prompt';font-weight:600;font-size:26px;color:{BR};margin-top:12px}}
.q{{position:absolute;top:520px;left:56px;font-family:'Prompt';font-weight:700;font-size:44px;color:{GR}}}
.lks{{position:absolute;top:600px;left:56px;width:560px;display:flex;flex-direction:column;gap:14px}}
.lk{{font-family:'Prompt';font-weight:600;font-size:30px;color:#3f3229;padding:20px 24px;display:flex;align-items:center;gap:16px}}
.lk .e{{font-size:40px}}
.ans{{position:absolute;top:1000px;left:56px;width:560px;background:{BR};color:#fff;border-radius:28px;padding:24px 28px;font-family:'Prompt';font-weight:600;font-size:34px;line-height:1.3}}"""
    body = f"""<div class="h1 h">รสชาติเป็นแบบไหน?</div><div class="s">กลิ่นที่คนดื่มโฮจิฉะมักพูดถึง</div>
<div class="fls">{ch}</div><div class="q">ถ้าคุณชอบสิ่งเหล่านี้…</div><div class="lks">{lk}</div>
<div class="ans">👉 คุณน่าจะชอบโฮจิฉะ!<div style="font-family:'Plex';font-weight:400;font-size:22px;opacity:.9;margin-top:4px">หอมคั่ว นุ่ม ไม่ขมแบบชาเข้ม</div></div>
<img class="art" src="{H('art_cover')}" style="left:600px;top:600px;width:450px;height:560px;object-fit:contain">"""
    return page(4, body, css)

def s5():
    items = [("hojicha_latte", "Hojicha Latte", "โฮจิฉะลาเต้ ตีนมราดนม", "79.-", "🌱 มือใหม่เริ่มแก้วนี้", "รสคั่วกลมกล่อม นุ่มนม"),
             ("kokoro_honeycomb", "Kokoro Hojicha Honeycomb Velvet", "โฮจิฉะฮันนี่คอมบ์", "159.-", "✨ สาย texture", "กรุบ ๆ honeycomb + velvet foam"),
             ("kokoro_cheesecake", "Kokoro Hojicha Cheesecake Mochi", "โฮจิฉะชีสเค้กโมจิ", "179.-", "🍡 สายของหวาน", "ชีสเค้ก + โมจิเสียบไม้")]
    rows = "".join(f"""<div class="cardw it"><div class="pic"><img class="cut" src="{img(a)}"></div>
<div class="tx"><span class="bd">{bd}</span><div class="en">{en}</div><div class="th">{th}</div><div class="d">“{d}”</div></div><div class="pr">{p}</div></div>""" for a, en, th, p, bd, d in items)
    css = f""".h{{position:absolute;top:96px;left:56px;font-size:70px;color:{BR}}}
.s{{position:absolute;top:184px;left:58px;font-size:27px;color:#5b4a3c}}
.its{{position:absolute;top:250px;left:48px;right:48px;display:flex;flex-direction:column;gap:18px}}
.it{{height:300px;display:flex;align-items:center;position:relative}}
.it .pic{{width:250px;height:300px;flex:none;background:{BRT};border-radius:28px 0 0 28px;display:flex;align-items:center;justify-content:center}}
.it .pic img{{max-height:280px;max-width:220px}}
.it .tx{{padding:20px 26px;flex:1;min-width:0}}
.bd{{display:inline-block;font-family:'Prompt';font-weight:600;font-size:21px;color:{BR};background:{BRT};padding:4px 14px;border-radius:16px}}
.en{{font-family:'Prompt';font-weight:700;font-size:31px;color:#2f241c;margin-top:10px;line-height:1.15}}
.th{{font-size:21px;color:#7a6a5d;margin-top:2px}}
.d{{font-size:24px;color:#3f3229;margin-top:10px}}
.pr{{position:absolute;right:20px;top:18px;font-family:'Prompt';font-weight:600;font-size:26px;color:#fff;background:{BR};padding:4px 16px;border-radius:22px}}"""
    body = f"""<div class="h1 h">3 แก้วโฮจิฉะที่ Hibi</div><div class="s">เริ่มจากซ้ายสุด แล้วค่อยขยับไปแก้วพิเศษ</div><div class="its">{rows}</div>"""
    return page(5, body, css)

def s6():
    tips = [("🍬", "มือใหม่ เริ่มหวาน 5g", "รสคั่วชัด ไม่หวานกลบ"),
            ("🌾", "ลองนมโอ๊ต (+20.-)", "เข้ากับกลิ่นคั่วแบบถั่ว ๆ"),
            ("🖤", "ชอบเข้ม ขอหวาน 0–3g", "ได้กลิ่นชาเต็ม ๆ"),
            ("🌙", "แก้วบ่าย–เย็น", "คาเฟอีนมักน้อยกว่ามัทฉะ")]
    tc = "".join(f"""<div class="cardw tp"><div class="ic">{e}</div><div class="tt">{t}</div><div class="td">{d}</div></div>""" for e, t, d in tips)
    css = f""".h{{position:absolute;top:96px;left:56px;font-size:70px;color:{BR}}}
.tps{{position:absolute;top:210px;left:48px;right:48px;display:grid;grid-template-columns:1fr 1fr;gap:18px}}
.tp{{height:300px;padding:26px;text-align:center}}
.tp .ic{{width:100px;height:100px;margin:0 auto;border-radius:50%;background:{BRT};display:flex;align-items:center;justify-content:center;font-size:52px}}
.tt{{font-family:'Prompt';font-weight:700;font-size:31px;color:{BR};margin-top:18px;line-height:1.2}}
.td{{font-size:23px;color:#5b4a3c;margin-top:8px}}
.cp{{position:absolute;top:860px;left:48px;right:48px;background:{GR};color:#fff;border-radius:28px;padding:24px 28px;display:flex;align-items:center;gap:20px}}
.cp .t{{font-family:'Prompt';font-weight:600;font-size:30px}}.cp .d{{font-size:23px;opacity:.92;margin-top:4px}}
.save{{position:absolute;top:1100px;left:48px;right:48px;height:80px;border-radius:24px;border:3px dashed {BRM};background:rgba(255,255,255,.6);display:flex;align-items:center;justify-content:center;font-family:'Prompt';font-weight:600;font-size:30px;color:{BR}}}"""
    body = f"""<div class="h1 h">สั่งยังไงให้อร่อย?</div><div class="tps">{tc}</div>
<div class="cp">{avatar("C",84)}<div><div class="t">Capy แนะนำ</div><div class="d">ยังลังเล? เริ่ม Hojicha Latte หวาน 5g ร้อนหรือเย็นก็อร่อย</div></div></div>
<div class="save">📌 เซฟไว้ ก่อนสั่งครั้งหน้า</div>"""
    return page(6, body, css)

def s7():
    css = f""".h{{position:absolute;top:100px;left:0;right:0;text-align:center;font-size:90px;color:{GR}}}
.s{{position:absolute;top:212px;left:0;right:0;text-align:center;font-size:30px;color:#5b4a3c}}
.tm{{position:absolute;top:640px;font-family:'Prompt';font-weight:700;font-size:40px;color:#fff;padding:14px 30px;border-radius:40px}}
.ex{{position:absolute;top:740px;left:110px;right:110px;padding:22px 30px;text-align:center}}
.ex .k{{font-size:21px;color:#7a6a5d}}.ex .v{{font-family:'Prompt';font-weight:600;font-size:36px;color:#2f241c;margin-top:4px}}
.br{{position:absolute;top:920px;left:48px;right:48px;background:{GR};color:#fff;border-radius:28px;padding:24px 28px;text-align:center}}
.br .t{{font-family:'Prompt';font-weight:600;font-size:28px}}.br .l{{font-size:22px;margin-top:8px;line-height:1.5}}.br .d{{font-size:20px;margin-top:6px;color:#cfe6bd}}"""
    body = f"""<div class="h1 h">คุณเป็นทีมไหน?</div><div class="s">คอมเมนต์บอก Hibi &amp; Capy หน่อย 👇</div>
<img class="art" src="{H('art_vs')}" style="left:120px;top:270px;width:840px;height:380px;object-fit:contain">
<div class="tm" style="left:110px;background:{GRM}">🍵 ทีมมัทฉะ</div><div class="tm" style="right:110px;background:{BRM}">🍂 ทีมโฮจิฉะ</div>
<div class="cardw ex"><div class="k">พิมพ์แบบนี้เลย</div><div class="v">“ทีมโฮจิฉะ · หวาน 5g · นมโอ๊ต”</div></div>
<div class="br"><div class="t">📍 Hibi Matcha Cafe 5 สาขา</div>
<div class="l">ลาดพร้าว 107 · นาคนิวาส 48 · สะพานควาย · นวมินทร์ 111 · สามย่าน (จุฬาฯ 11)</div>
<div class="d">Delivery: LINE MAN · Grab · ShopeeFood</div></div>"""
    return page(7, body, css)

for n, html in enumerate([s1(), s2(), s3(), s4(), s5(), s6(), s7()], 1):
    p = f"{OUT}/s{n}.html"; open(p, "w").write(html)
    png = f"{OUT}/HIBI_HOJICHA_{n:02d}.png"
    subprocess.run(["/opt/pw-browsers/chromium", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    "--allow-file-access-from-files", "--virtual-time-budget=4000", "--force-device-scale-factor=1",
                    f"--screenshot={png}", "--window-size=1080,1500", "file://" + p], check=True, capture_output=True)
    Image.open(png).crop((0, 0, 1080, 1350)).convert("RGB").save(png.replace(".png", ".jpg"), quality=94); os.remove(png)
print("done")
