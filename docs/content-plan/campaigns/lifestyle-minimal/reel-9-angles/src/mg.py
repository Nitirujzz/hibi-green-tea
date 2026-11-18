"""MG for '1 แก้ว 9 มุม' reel (16 s): hook title, 01/09 counters, animated 3x3 grid finale + end text -> mg.html."""
import os, json
D=os.path.dirname(os.path.abspath(__file__)); FR=os.path.abspath(f"{D}/../frames")
CSSF=open("/root/.fonts/extra/cormorant_local.css").read()
FONTS=CSSF+"".join(f"@font-face{{font-family:'Prompt';font-weight:{w};src:url('file:///root/.fonts/Prompt-{w}-{s}.woff2') format('woff2');}}" for w in (500,600) for s in ("thai","latin"))
G0=11.0                      # grid starts
TW,TH,GAP,X0,Y0=290,362,12,93,330
tiles="".join(f'<div class="t" id="t{i}" style="left:{X0+(i%3)*(TW+GAP)}px;top:{Y0+(i//3)*(TH+GAP)}px;background-image:url(\'file://{FR}/a{i+1:02d}.png\')"><span>{i+1}</span></div>' for i in range(9))
html=f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}} html,body{{width:1080px;height:1920px;background:transparent;overflow:hidden}}
.serif{{font-family:'Cormorant Garamond',serif}} .th{{font-family:Prompt}}
#hook{{position:absolute;left:0;right:0;top:300px;text-align:center;color:#fff;text-shadow:0 4px 30px rgba(0,0,0,.45)}}
#hook .a{{font-family:Prompt;font-weight:600;font-size:150px;line-height:1;opacity:0}}
#hook .b{{font-family:Prompt;font-weight:500;font-size:64px;margin-top:20px;opacity:0}}
#cnt{{position:absolute;left:540px;top:1370px;transform:translateX(-50%);font-family:'Cormorant Garamond',serif;font-size:44px;letter-spacing:4px;color:#fff;
 background:rgba(36,62,27,.55);padding:4px 26px;border-radius:30px;opacity:0}}
#grid{{position:absolute;inset:0;background:#f6f4ee;opacity:0}}
#gt{{position:absolute;left:0;right:0;top:200px;text-align:center;color:#243e1b}}
#gt .a{{font-family:Prompt;font-weight:600;font-size:66px}} #gt .a i{{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:400;font-size:74px;color:#4e7c3a}}
.t{{position:absolute;width:{TW}px;height:{TH}px;background-size:cover;background-position:center;border-radius:6px;opacity:0;box-shadow:0 6px 18px rgba(0,0,0,.10)}}
.t span{{position:absolute;left:10px;top:8px;font-family:'Cormorant Garamond',serif;font-size:34px;color:#fff;text-shadow:0 2px 8px rgba(0,0,0,.5);opacity:0}}
#more{{position:absolute;left:0;right:0;top:1460px;text-align:center;font-family:Prompt;font-weight:500;font-size:52px;color:#243e1b;opacity:0}}
#veil{{position:absolute;inset:0;background:rgba(246,244,238,.0)}}
#end{{position:absolute;left:0;right:0;top:760px;text-align:center;opacity:0}}
#end .a{{font-family:Prompt;font-weight:600;font-size:76px;color:#243e1b;line-height:1.25}}
#end .b{{font-family:Prompt;font-weight:500;font-size:46px;color:#4e7c3a;margin-top:26px}}
#end .c{{font-family:'Cormorant Garamond',serif;font-size:44px;letter-spacing:3px;color:#6b6a55;margin-top:40px}}
</style></head><body>
<div id="hook"><div class="a">1 แก้ว</div><div class="b">เล่าได้ 9 มุม 👀</div></div>
<div id="cnt">01 / 09</div>
<div id="grid"><div id="gt"><div class="a">1 แก้ว · <i>9 angles</i></div></div>{tiles}<div id="more">…เล่าได้อีกเยอะ 👀</div><div id="veil"></div>
<div id="end"><div class="a">มุมไหน<br>คือคุณ?</div><div class="b">คอมเมนต์เลข 1–9 👇</div><div class="c">@hibimatchacafe</div></div></div>
<script>
const G0={G0};
const back=x=>{{const c=1.8;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)}}, cl=x=>Math.max(0,Math.min(1,x));
function render(t){{
 const H=document.getElementById('hook').children;
 [[0.1,0],[0.6,1]].forEach(([s,i])=>{{const u=t-s,v=1.95-t;const o=u<0?0:cl(u/0.12)*cl(v/0.12);H[i].style.opacity=o;H[i].style.transform=`scale(${{u<0?0.8:(u<0.3?back(u/0.3):1)}})`}});
 const C=document.getElementById('cnt');
 if(t>=2&&t<G0){{const k=Math.floor(t-2);C.textContent=String(k+1).padStart(2,'0')+' / 09';const u=(t-2)%1;C.style.opacity=cl(u/0.08)*cl((1-u)/0.06)}} else C.style.opacity=0;
 const Gd=document.getElementById('grid');Gd.style.opacity=t<G0?0:cl((t-G0)/0.12);
 for(let i=0;i<9;i++){{const e=document.getElementById('t'+i),u=t-(G0+0.15+i*0.125);
  e.style.opacity=u<0?0:cl(u/0.08);e.style.transform=`scale(${{u<0?0.6:(u<0.3?back(u/0.3):1)}})`;e.children[0].style.opacity=cl((t-13.9)/0.3)}}
 const M=document.getElementById('more'),um=t-12.5;M.style.opacity=um<0?0:cl(um/0.2)*cl((14.0-t)/0.2);M.style.transform=`translateY(${{um<0?20:Math.max(0,20*(1-um/0.3))}}px)`;
 const V=document.getElementById('veil'),ue=t-14.0;V.style.background=`rgba(246,244,238,${{0.86*cl(ue/0.3)}})`;
 const E=document.getElementById('end');E.style.opacity=cl(ue/0.25);E.style.transform=`scale(${{ue<0?0.9:(ue<0.35?back(ue/0.35):1)}})`;
}}
</script></body></html>"""
open(f"{D}/mg.html","w").write(html); print("ok")
