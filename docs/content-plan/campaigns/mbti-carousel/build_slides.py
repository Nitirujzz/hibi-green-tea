import os, subprocess, base64, io
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(D, "out2"); os.makedirs(OUT, exist_ok=True)
_cache = {}
def img(name, folder="cut", maxh=900):
    k = (name, folder)
    if k not in _cache:
        im = Image.open(f"{D}/{folder}/{name}.png")
        if im.size[1] > maxh: im = im.resize((int(im.size[0] * maxh / im.size[1]), maxh), Image.LANCZOS)
        b = io.BytesIO(); im.save(b, "PNG"); _cache[k] = "data:image/png;base64," + base64.b64encode(b.getvalue()).decode()
    return _cache[k]
LOGO = lambda: img("hibi_logo", "assets")

FONTS = "".join(
    f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('file:///root/.fonts/{f}-{w}-{s}.woff2') format('woff2');}}"
    for fam, f in [("Prompt", "Prompt"), ("Plex", "IBMPlexSansThai")]
    for w in ([400, 500, 600, 700] if f == "Prompt" else [400, 600])
    for s in ["thai", "latin"])

CAPY = """<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
<ellipse cx="100" cy="158" rx="70" ry="38" fill="#a8744a"/>
<circle cx="62" cy="62" r="13" fill="#946240"/><circle cx="138" cy="62" r="13" fill="#946240"/>
<circle cx="62" cy="62" r="6" fill="#6f4529"/><circle cx="138" cy="62" r="6" fill="#6f4529"/>
<rect x="38" y="52" width="124" height="100" rx="50" fill="#c08a5c"/>
<ellipse cx="100" cy="122" rx="38" ry="25" fill="#a8744a"/>
<rect x="87" y="108" width="26" height="11" rx="5.5" fill="#4a2f1d"/>
<path d="M68 94 q10 8 20 0" stroke="#3b2416" stroke-width="5.5" fill="none" stroke-linecap="round"/>
<path d="M112 94 q10 8 20 0" stroke="#3b2416" stroke-width="5.5" fill="none" stroke-linecap="round"/>
<ellipse cx="58" cy="114" rx="11" ry="6.5" fill="#f2a99a" opacity=".75"/><ellipse cx="142" cy="114" rx="11" ry="6.5" fill="#f2a99a" opacity=".75"/>
<path d="M80 26 L120 26 L114 52 L86 52 Z" fill="#fbf6ec" stroke="#7a5233" stroke-width="2.5" stroke-linejoin="round"/>
<ellipse cx="100" cy="26" rx="20" ry="6" fill="#4e7c3a"/>
</svg>"""

CSS = FONTS + """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px}
body{overflow:hidden;background:#f2f9ea;font-family:'Plex',sans-serif;color:#1d2b18;position:relative}
.P{font-family:'Prompt',sans-serif}
.top{position:absolute;top:34px;left:56px;right:56px;display:flex;justify-content:space-between;align-items:center;font-family:'Prompt';font-size:22px;color:#243e1b;letter-spacing:1.5px}
.top .pg{background:#243e1b;color:#fff;border-radius:20px;padding:4px 16px;font-size:20px;letter-spacing:0}
.foot{position:absolute;left:0;right:0;top:1270px;height:80px;background:#243e1b;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 56px;font-family:'Prompt';font-size:22px}
.foot .r{opacity:.85}
.swipe{position:absolute;right:56px;top:1205px;font-family:'Prompt';font-weight:500;font-size:22px;color:#4e7c3a}
.av{border-radius:50%;overflow:hidden;display:inline-block;vertical-align:middle}
.av.h{background:#4e7c3a;padding:3px}.av.h img{width:100%;height:100%;border-radius:50%;display:block}
.av.c{background:#f1e4d1;padding:2px}.av.c svg{width:100%;height:100%;display:block}
.cut{filter:drop-shadow(0 18px 16px rgba(36,62,27,.20))}
"""

def avatar(kind, size):
    if kind == "H": return f'<span class="av h" style="width:{size}px;height:{size}px"><img src="{LOGO()}"></span>'
    return f'<span class="av c" style="width:{size}px;height:{size}px">{CAPY}</span>'

def page(n, body, css="", swipe=True):
    sw = ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{css}</style></head><body>
<div class="top"><span>HIBI MATCHA CAFE 日々</span><span class="pg">{n}/7</span></div>{body}{sw}
<div class="foot"><span>มัทฉะแก้วไหนคือคุณ?</span><span class="r">@hibimatchacafe</span></div></body></html>"""

# ---------- data (เมนูจริงจากร้าน) ----------
GROUPS = [
    ("NT", "นักวิเคราะห์", "ขอของแท้ ไม่ต้องปรุงเยอะ", "#243e1b", "#e3eedb", [
        ("INTJ", "clear_matcha", "Clear Matcha", "มัทฉะใส", "59.-", "0g", "วางแผนมาแล้ว ขอมัทฉะแท้ ๆ ไม่ต้องหวาน"),
        ("INTP", "kirei_yuzu", "Kirei Yuzu Matcha", "มัทฉะยูซุคิเรอิ", "79.-", "3g", "ยูซุ + มัทฉะ เข้ากันได้ไง… ขอทดลองก่อน"),
        ("ENTJ", "velvet_whisk", "Velvet Matcha Whisk Latte", "ท็อปโฟมนมเย็น", "129.-", "5g", "เลือกตัวท็อปของร้าน ไม่เสียเวลาลังเล"),
        ("ENTP", "thai_matcha", "Jasmine Thai Tea × Matcha", "ชาไทยมะลิ × มัทฉะ", "109.-", "สูตรคงที่", "ชาไทยกับมัทฉะเข้ากันไม่ได้? ขอเถียง!"),
    ]),
    ("NF", "นักการทูต", "หอม ละมุน มีเรื่องราว", "#4e7c3a", "#e6f1dc", [
        ("INFJ", "coconut_jasmine", "Clear Matcha Coconut Jasmine", "มัทฉะใสมะพร้าวมะลิ", "79.-", "3g", "หอมมะลิบาง ๆ ลึกหลายชั้น เหมือนใจเรา"),
        ("INFP", "osmanthus", "Osmanthus Honey Coconut", "หอมหมื่นลี้ น้ำผึ้ง มะพร้าว", "เมนูแนะนำ", "ไม่หวานเกิน", "นั่งริมหน้าต่าง ฝันกลางวันได้ทั้งบ่าย"),
        ("ENFJ", "cloud_latte", "Matcha Cloud Latte", "มัทฉะคลาวด์ลาเต้", "79.-", "สูตรคงที่", "นุ่มเหมือนเมฆ อุ่นเหมือนคนที่ดูแลทุกคน"),
        ("ENFP", "pink_cloud", "Pink Coconut Cloud", "Pink is Fine Collection", "79.-", "10g", "สีชมพู! ถ่าย 30 รูปก่อนจิบคำแรก"),
    ]),
    ("SJ", "ผู้พิทักษ์", "คลาสสิก ไว้ใจได้ทุกวัน", "#5d7a2a", "#ebf0db", [
        ("ISTJ", "matcha_latte", "Matcha Latte (Whisked Milk)", "มัทฉะลาเต้ตีนมราดนม", "79.-", "8g", "เมนูเดิม หวานเดิม สาขาเดิม ทุกวัน"),
        ("ISFJ", "hojicha_latte", "Hojicha Latte", "โฮจิฉะลาเต้ ตีนมราดนม", "79.-", "5g", "ซื้อแก้วตัวเองแล้ว ต้องซื้อฝากที่บ้านด้วย"),
        ("ESTJ", "cold_whisked", "Cold Whisked Latte", "มัทฉะตีน้ำสไตล์ญี่ปุ่น", "59.-", "5g", "ตีสด เร็ว คุ้ม แล้วไปทำงานต่อ"),
        ("ESFJ", "strawberry", "Matcha Strawberry Latte", "มัทฉะลาเต้สตรอว์เบอร์รีสด", "89.-", "10g", "แก้วที่ทั้งแก๊งชอบ จำได้ว่าใครหวานเท่าไหร่"),
    ]),
    ("SP", "นักสำรวจ", "ของใหม่ ต้องได้ลองก่อน", "#a06b17", "#f5ecd8", [
        ("ISTP", "kokoro_honeycomb", "Kokoro Hojicha Honeycomb Velvet", "โฮจิฉะฮันนี่คอมบ์", "159.-", "5g", "กรุบ ๆ honeycomb เคี้ยวไปคิดไป สาย texture"),
        ("ISFP", "mango_pandan", "Matcha Mango Pandan Cloud", "มัทฉะมะม่วงใบเตย", "Signature", "8g", "เลือกแก้วจากสี เลือกโต๊ะจากแสง"),
        ("ESTP", "pistachio", "Pistachio Kunafeh Matcha Luxe", "พิสตาชิโอคูนาเฟห์", "Signature", "8g", "เห็นเมนูใหม่ปุ๊บ สั่งปั๊บ ไม่อ่านต่อ"),
        ("ESFP", "kokoro_cheesecake", "Kokoro Hojicha Cheesecake Mochi", "โฮจิฉะชีสเค้กโมจิ", "179.-", "10g", "มีโมจิเสียบไม้! ไลฟ์ก่อนกิน"),
    ]),
]

GCSS = """
.hd{position:absolute;top:96px;left:56px;right:56px;height:140px;display:flex;align-items:center;gap:26px}
.hd .code{font-family:'Prompt';font-weight:700;font-size:120px;line-height:1;letter-spacing:-2px}
.hd .nm{font-family:'Prompt';font-weight:600;font-size:46px;line-height:1.1}
.hd .tg{font-size:26px;color:#4a5a43;margin-top:6px}
.list{position:absolute;top:256px;left:56px;right:56px;display:flex;flex-direction:column;gap:18px}
.row{height:230px;border-radius:30px;background:#fff;position:relative;display:flex;align-items:center;overflow:visible;box-shadow:0 8px 24px rgba(36,62,27,.07)}
.row .pic{width:250px;height:230px;position:relative;flex:none;border-radius:30px 0 0 30px;display:flex;align-items:center;justify-content:center}
.row .pic img{max-height:212px;max-width:220px}
.row .wm{position:absolute;left:14px;top:6px;font-family:'Prompt';font-weight:700;font-size:64px;opacity:.10;letter-spacing:-1px}
.row .tx{flex:1;padding:18px 24px 16px 26px;min-width:0}
.row .l1{display:flex;align-items:center;gap:14px}
.row .mb{font-family:'Prompt';font-weight:700;font-size:48px;line-height:1}
.team{display:inline-flex;align-items:center;gap:8px;font-family:'Prompt';font-weight:500;font-size:19px;padding:3px 14px 3px 4px;border-radius:24px}
.row .en{font-family:'Prompt';font-weight:600;font-size:25px;line-height:1.2;margin-top:8px;color:#1d2b18;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.row .th{font-size:19px;color:#66745e;margin-top:1px}
.row .q{font-size:22px;line-height:1.35;margin-top:8px;color:#1d2b18}
.row .tags{position:absolute;right:20px;top:18px;display:flex;gap:8px}
.price{font-family:'Prompt';font-weight:600;font-size:24px;color:#fff;border-radius:22px;padding:4px 16px}
.sweet{font-family:'Prompt';font-weight:500;font-size:19px;border-radius:22px;padding:6px 14px;color:#243e1b}
"""

def group_slide(n, g):
    code, name, tag, col, tint, items = g
    rows = ""
    for t, a, en, th, price, sw, q in items:
        team = (f'<span class="team" style="background:#e3eedb;color:#243e1b">{avatar("H",34)}ทีม Hibi</span>' if t[0] == "E"
                else f'<span class="team" style="background:#f4ead9;color:#6f4529">{avatar("C",34)}ทีม Capy</span>')
        swtxt = sw if not sw.endswith("g") else f"หวาน {sw}"
        rows += f"""<div class="row"><div class="pic" style="background:{tint}">
<img class="cut" src="{img(a)}"></div>
<div class="tx"><div class="l1"><span class="mb" style="color:{col}">{t}</span>{team}</div>
<div class="en">{en}</div><div class="th">{th}</div><div class="q">“{q}”</div></div>
<div class="tags"><span class="sweet" style="background:{tint}">{swtxt}</span><span class="price" style="background:{col};{'font-size:19px;padding:6px 14px' if not price.endswith('.-') else ''}">{price}</span></div></div>"""
    body = f"""<div class="hd"><div class="code" style="color:{col}">{code}</div>
<div><div class="nm" style="color:{col}">{name}</div><div class="tg">{tag}</div></div></div>
<div class="list">{rows}</div>"""
    return page(n, body, GCSS)

COVER = """
.chip{position:absolute;top:110px;left:56px;display:flex;gap:10px}
.chip span{font-family:'Prompt';font-weight:500;font-size:24px;padding:8px 20px;border-radius:30px}
.ttl{position:absolute;top:178px;left:56px;right:56px;font-family:'Prompt';font-weight:700;font-size:132px;line-height:1.02;color:#243e1b;letter-spacing:-2px}
.ttl em{font-style:normal;color:#4e7c3a}
.sub{position:absolute;top:470px;left:60px;font-size:30px;color:#3f5236}
.blob{position:absolute;left:-60px;right:-60px;top:640px;height:640px;background:radial-gradient(ellipse at 50% 60%,#cfe6bd 0%,#e4f1d8 45%,rgba(242,249,234,0) 70%)}
.disk{position:absolute;left:140px;right:140px;top:1080px;height:90px;border-radius:50%;background:#4e7c3a;opacity:.9}
.d{position:absolute;bottom:200px}
.tm{position:absolute;top:1100px;display:flex;align-items:center;gap:10px;font-family:'Prompt';font-weight:600;font-size:22px;background:#fff;border-radius:40px;padding:6px 18px 6px 6px;box-shadow:0 6px 18px rgba(0,0,0,.08)}
.cta{position:absolute;left:56px;top:1196px;font-family:'Prompt';font-weight:600;font-size:26px;color:#243e1b}
"""

def cover():
    drinks = [("pink_cloud", 64, 350, -7), ("velvet_whisk", 262, 415, -2), ("osmanthus", 528, 415, 3), ("kokoro_cheesecake", 742, 375, 7)]
    ds = "".join(f'<img class="d cut" src="{img(a)}" style="left:{x}px;height:{h}px;transform:rotate({r}deg);bottom:{218 if h>400 else 226}px">' for a, x, h, r in drinks)
    body = f"""<div class="chip"><span style="background:#243e1b;color:#fff">16 บุคลิก</span><span style="background:#fff;color:#243e1b">16 แก้วจริงจากเมนู</span></div>
<div class="ttl">มัทฉะแก้วไหน<br><em>คือคุณ?</em></div>
<div class="sub">ทาย MBTI จากแก้วโปรด · หาตัวเองแล้วแท็กเพื่อน</div>
<div class="blob"></div><div class="disk"></div>{ds}
<div class="tm" style="left:56px">{avatar("H",52)}ทีม Hibi = สาย E</div>
<div class="tm" style="right:56px">{avatar("C",52)}ทีม Capy = สาย I</div>
<div class="cta">ปัดหาแก้วของคุณ 👉</div>"""
    return page(1, body, COVER, swipe=False)

SWEET = """
.h1{position:absolute;top:104px;left:56px;font-family:'Prompt';font-weight:700;font-size:86px;color:#243e1b;line-height:1.05}
.h2{position:absolute;top:212px;left:58px;font-size:28px;color:#3f5236}
.bar{position:absolute;top:290px;left:56px;right:56px;background:#fff;border-radius:32px;padding:34px 30px 28px}
.track{height:18px;border-radius:9px;background:linear-gradient(90deg,#d9ebcb,#243e1b);margin:0 46px 18px}
.dots{display:flex;justify-content:space-between}
.dt{width:150px;text-align:center}
.dt .c{width:92px;height:92px;border-radius:50%;margin:0 auto;display:flex;align-items:center;justify-content:center;font-family:'Prompt';font-weight:600;font-size:30px;color:#fff;box-shadow:0 6px 14px rgba(36,62,27,.15)}
.dt .l{font-family:'Prompt';font-weight:500;font-size:20px;margin-top:12px}
.dt .m{font-size:18px;color:#4e7c3a;margin-top:4px;line-height:1.3}
.cards{position:absolute;top:640px;left:56px;right:56px;display:grid;grid-template-columns:1fr 1fr;gap:22px}
.cd{background:#fff;border-radius:30px;padding:28px 30px;height:420px}
.cd h3{font-family:'Prompt';font-weight:600;font-size:32px;color:#243e1b;margin-bottom:12px}
.cd .r{display:flex;justify-content:space-between;font-size:24px;padding:11px 0;border-bottom:1px solid #edf3e7}
.cd.dk{background:#243e1b;color:#fff;position:relative}.cd.dk h3{color:#fff;display:flex;align-items:center;gap:12px}
.cd.dk p{font-size:22px;line-height:1.45;margin-bottom:12px}
.save{position:absolute;top:1100px;left:56px;right:56px;height:78px;border-radius:24px;border:3px dashed #4e7c3a;display:flex;align-items:center;justify-content:center;font-family:'Prompt';font-weight:600;font-size:30px;color:#243e1b}
"""

def sweet():
    lv = [("0g", "ไม่หวานเลย", "INTJ", "#bcd9a6"), ("3g", "หวานถึงรสชาติ", "INTP · INFJ", "#9cc683"), ("5g", "หวานเล็กน้อย", "ISFJ · ESTJ\nENTJ · ISTP", "#7fb064"),
          ("8g", "หวานปกติ", "ISTJ · ISFP\nESTP", "#619447"), ("10g", "หวานชื่นใจ", "ENFP · ESFJ\nESFP", "#467334"), ("15g", "หวานในเกิน100", "สายหวานจัด", "#243e1b")]
    dots = "".join(f'<div class="dt"><div class="c" style="background:{c}">{g}</div><div class="l">{l}</div><div class="m">{m.replace(chr(10),"<br>")}</div></div>' for g, l, m, c in lv)
    milk = "".join(f'<div class="r"><span>{a}</span><b class="P" style="font-weight:600">{b}</b></div>' for a, b in [("นมสด", "ฟรี"), ("Lactose Free", "+10.-"), ("Oat Milk", "+20.-"), ("Almond Milk", "+25.-")])
    body = f"""<div class="h1">สั่งหวานแค่ไหนดี?</div><div class="h2">ระดับความหวานของ Hibi เลือกได้ทุกแก้ว (ยกเว้นเมนูสูตรคงที่)</div>
<div class="bar"><div class="track"></div><div class="dots">{dots}</div></div>
<div class="cards"><div class="cd"><h3>เปลี่ยนนมได้</h3>{milk}</div>
<div class="cd dk"><h3>{avatar("C",48)}Capy แนะนำ</h3><p>🍵 มือใหม่เริ่ม 5–8g จะได้กลิ่นมัทฉะชัด</p><p>☁️ Cloud Latte / Cream Cheese / Thai Tea × Matcha เป็นสูตรคงที่</p><p>✨ อยากนุ่มขึ้น เพิ่ม Velvet Milk Foam หรือ Milk Mochi</p></div></div>
<div class="save">📌 เซฟสไลด์นี้ไว้ ก่อนสั่งครั้งหน้า</div>"""
    return page(6, body, SWEET)

END = """
.h1{position:absolute;top:120px;left:0;right:0;text-align:center;font-family:'Prompt';font-weight:700;font-size:100px;color:#243e1b;line-height:1.05}
.h2{position:absolute;top:240px;left:0;right:0;text-align:center;font-size:30px;color:#3f5236}
.duo{position:absolute;top:320px;left:0;right:0;display:flex;justify-content:center;gap:40px}
.duo .w{text-align:center;font-family:'Prompt';font-weight:600;font-size:26px}
.box{position:absolute;top:640px;left:120px;right:120px;background:#fff;border-radius:30px;padding:30px 36px;box-shadow:0 8px 24px rgba(36,62,27,.08)}
.box .k{font-size:22px;color:#66745e}
.box .v{font-family:'Prompt';font-weight:600;font-size:40px;color:#243e1b;margin-top:6px}
.tag{position:absolute;top:850px;left:0;right:0;text-align:center;font-family:'Prompt';font-weight:600;font-size:32px;color:#4e7c3a}
.br{position:absolute;top:940px;left:56px;right:56px;background:#243e1b;color:#fff;border-radius:30px;padding:26px 30px;text-align:center}
.br .t{font-family:'Prompt';font-weight:600;font-size:28px}
.br .l{font-size:23px;margin-top:8px;line-height:1.5;opacity:.95}
.br .d{font-size:21px;margin-top:8px;color:#cfe6bd}
.disc{position:absolute;top:1218px;left:0;right:0;text-align:center;font-size:18px;color:#7b8a72}
"""

def end():
    body = f"""<div class="h1">คุณคือ MBTI ไหน?</div><div class="h2">บอก Hibi &amp; Capy ในคอมเมนต์หน่อย 👇</div>
<div class="duo"><div class="w">{avatar("H",250)}<div style="margin-top:12px;color:#4e7c3a">ทีม Hibi</div></div>
<div class="w">{avatar("C",250)}<div style="margin-top:12px;color:#6f4529">ทีม Capy</div></div></div>
<div class="box"><div class="k">พิมพ์แบบนี้เลย</div><div class="v">“INFP · ทีม Capy · Osmanthus”</div></div>
<div class="tag">แท็กเพื่อนที่เป็น ENFP ตัวจริง 😆</div>
<div class="br"><div class="t">📍 Hibi Matcha Cafe 5 สาขา</div>
<div class="l">ลาดพร้าว 107 · นาคนิวาส 48 · สะพานควาย · นวมินทร์ 111 · สามย่าน (จุฬาฯ 11)</div>
<div class="d">สั่ง Delivery: LINE MAN · Grab · ShopeeFood</div></div>
<div class="disc">*เพื่อความสนุก ไม่ใช่แบบทดสอบบุคลิกภาพจริง · เมนูและราคาอาจต่างกันในแต่ละสาขา</div>"""
    return page(7, body, END, swipe=False)

slides = [cover()] + [group_slide(i + 2, g) for i, g in enumerate(GROUPS)] + [sweet(), end()]
for n, html in enumerate(slides, 1):
    p = f"{OUT}/s{n}.html"; open(p, "w").write(html)
    png = f"{OUT}/HIBI_MBTI_{n:02d}.png"
    subprocess.run(["/opt/pw-browsers/chromium", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    "--allow-file-access-from-files", "--virtual-time-budget=4000", "--force-device-scale-factor=1",
                    f"--screenshot={png}", "--window-size=1080,1500", "file://" + p], check=True, capture_output=True)
    Image.open(png).crop((0, 0, 1080, 1350)).convert("RGB").save(png.replace(".png", ".jpg"), quality=95)
    os.remove(png)
ims = [Image.open(f"{OUT}/HIBI_MBTI_{i:02d}.jpg") for i in range(1, 8)]
sh = Image.new("RGB", (540 * 4, 675 * 2), "white")
for i, im in enumerate(ims): sh.paste(im.resize((540, 675)), ((i % 4) * 540, (i // 4) * 675))
sh.save(f"{OUT}/overview.jpg", quality=90)
print("done")
