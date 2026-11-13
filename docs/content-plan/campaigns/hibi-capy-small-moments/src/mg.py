"""Motion graphics for Small Moments EP1: top captions, speech bubbles with speaker tags, end card -> mg.html (render with render_mg.js)."""
import os, json
D=os.path.dirname(os.path.abspath(__file__))
FONTS="".join(f"@font-face{{font-family:'Prompt';font-weight:{w};src:url('file:///root/.fonts/Prompt-{w}-{s}.woff2') format('woff2');}}" for w in (500,600,700) for s in ("thai","latin"))
# captions: (start, end, html)
CAP=[(0.12,3.05,'ทุกครั้งที่มาร้านด้วยกัน…'),(3.25,6.15,'เลือกไม่ถูกสักที 😵‍💫'),(6.35,8.7,'ส่วนเขา…')]
# bubbles: (start, end, who, html, size)
BUB=[(3.9,6.15,'Hibi','อันไหนดีอ่า…',58,1180,120),
     (9.05,11.8,'Capy','“เหมือนเดิมครับ<br>Strawberry Latte หวาน 5g”',54,1180,760),
     (12.05,14.95,'Hibi','จำได้ด้วยเหรอ?! 😳',66,1180,120),
     (15.35,18.05,'Capy','จำได้ทุกครั้งแหละ 💚',60,330,170)]
html=f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}} html,body{{width:1080px;height:1920px;background:transparent;overflow:hidden;font-family:Prompt}}
.cap{{position:absolute;left:540px;top:250px;white-space:nowrap;font-weight:700;font-size:62px;color:#fff;padding:16px 40px;border-radius:40px;
 background:rgba(36,62,27,.82);box-shadow:0 10px 30px rgba(0,0,0,.25);opacity:0;transform-origin:50% 50%}}
.bub{{position:absolute;left:540px;top:1180px;white-space:nowrap;text-align:center;font-weight:600;line-height:1.25;color:#3b2a30;background:#fff;
 padding:30px 46px 26px;border-radius:46px;box-shadow:0 14px 34px rgba(0,0,0,.25);opacity:0;transform-origin:50% 100%}}
.bub:after{{content:'';position:absolute;bottom:-30px;left:var(--tx);border:22px solid transparent;border-top:32px solid #fff;border-bottom:0}}
.tag{{position:absolute;top:-26px;left:30px;font-weight:700;font-size:32px;color:#fff;padding:4px 20px;border-radius:22px}}
.Hibi .tag{{background:#e88aa6}} .Capy .tag{{background:#4e7c3a}}
#end{{position:absolute;left:80px;right:80px;top:240px;text-align:center;opacity:0}}
#end .l{{opacity:0;white-space:nowrap}}
#end .a{{font-weight:600;font-size:58px;color:#4e7c3a}}
#end .b{{font-weight:700;font-size:80px;color:#243e1b;line-height:1.2;margin-top:6px}}
#end .c{{font-weight:600;font-size:46px;color:#7a2a44;margin-top:34px;display:inline-block;background:#fff;padding:14px 34px;border-radius:40px;box-shadow:0 10px 26px rgba(0,0,0,.12)}}
#end .d{{font-weight:500;font-size:36px;color:#6b6a55;margin-top:24px}}
</style></head><body>
{''.join(f'<div class="cap" id="c{i}">{h}</div>' for i,(a,b,h) in enumerate(CAP))}
{''.join(f'<div class="bub {w}" id="b{i}" style="font-size:{s}px;top:{y}px;--tx:{tx}px"><span class="tag">{w}</span>{h}</div>' for i,(a,b,w,h,s,y,tx) in enumerate(BUB))}
<div id="end"><div class="l a">ความรัก…</div><div class="l b">คือการจำเรื่องเล็ก ๆ<br>ของกันและกันได้ 💚</div><div class="l c">แท็กคนที่จำเมนูโปรดของคุณได้ 👇</div><div class="l d">Small Moments · Hibi &amp; Capy</div></div>
<script>
const CAP={json.dumps([(a,b) for a,b,h in CAP])}, BUB={json.dumps([(a,b) for a,b,w,h,s,y,tx in BUB])};
const back=x=>{{const c=2.0;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)}};
function life(t,a,b,ia=0.3){{if(t<a||t>b)return [0,0];const u=t-a,v=b-t;let s=u<ia?back(u/ia):1,o=Math.min(1,u/0.08);
 if(v<0.18){{s*=0.85+0.15*v/0.18;o*=v/0.18}} return [s,o]}}
function render(t){{
 CAP.forEach(([a,b],i)=>{{const [s,o]=life(t,a,b),e=document.getElementById('c'+i);e.style.opacity=o;e.style.transform=`translateX(-50%) scale(${{s}})`}});
 BUB.forEach(([a,b],i)=>{{let [s,o]=life(t,a,b,0.35),e=document.getElementById('b'+i);
  const sh=(i==2&&t>a&&t<a+0.5)?Math.sin((t-a)*60)*8*(1-(t-a)/0.5):0;   // little shake on 'จำได้ด้วยเหรอ?!'
  e.style.opacity=o;e.style.transform=`translateX(calc(-50% + ${{sh}}px)) scale(${{s}})`}});
 const E=document.getElementById('end'),u=t-20.9;E.style.opacity=u<0?0:1;
 [...E.children].forEach((l,k)=>{{const w=u-k*0.7;l.style.opacity=w<0?0:Math.min(1,w/0.25);l.style.transform=`translateY(${{w<0?30:Math.max(0,30*(1-w/0.35))}}px)`}});
}}
</script></body></html>"""
open(f"{D}/mg.html","w").write(html); print("mg.html ok")
