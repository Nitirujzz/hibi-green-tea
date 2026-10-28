"""Motion graphics for the Honey Lemon reel (transparent 1080x1920, 30 fps)."""
import json, os
D=os.path.dirname(os.path.abspath(__file__))
S=[0,3,6,9,11,14,18,20,23,26,30,33,36,40]; T=40.0
CH="/home/user/hibi-green-tea/docs/content-plan/campaigns/mbti-carousel/characters"
FONTS="".join(f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('file:///root/.fonts/{f}-{w}-{s}.woff2') format('woff2');}}"
  for fam,f in [("Prompt","Prompt"),("Plex","IBMPlexSansThai")] for w in ([400,500,600,700] if f=="Prompt" else [400,600]) for s in ["thai","latin"])
CSS=FONTS+"""*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1920px;background:transparent;overflow:hidden;font-family:'Prompt'}
.e{position:absolute;opacity:0}
.pill{left:540px;top:1250px;translate:-50% 0;white-space:nowrap;background:rgba(255,252,244,.96);color:#243e1b;font-weight:700;font-size:56px;padding:18px 42px;border-radius:60px;box-shadow:0 12px 30px rgba(120,80,0,.25);border:4px solid #ffe066}
.hook{left:60px;width:960px;top:270px;text-align:center;color:#fff;font-weight:700;font-size:84px;line-height:1.15;text-shadow:0 4px 0 #7a5200,0 10px 28px rgba(0,0,0,.35);white-space:nowrap}
.day{left:540px;top:300px;translate:-50% 0;width:420px;background:#fffaf0;border-radius:36px;box-shadow:0 14px 34px rgba(0,0,0,.25);overflow:hidden;text-align:center}
.day .top{background:#e5484d;color:#fff;font-weight:700;font-size:40px;padding:10px 0;letter-spacing:2px}
.day .num{font-weight:700;font-size:170px;color:#243e1b;line-height:1.05;padding:6px 0 10px}
.title{left:40px;width:1000px;top:1130px;text-align:center;white-space:nowrap}
.title .a{font-weight:700;font-size:112px;color:#fff;text-shadow:0 5px 0 #2f5d1a,0 12px 30px rgba(0,0,0,.35);line-height:1}
.title .b{font-weight:700;font-size:112px;color:#ffe066;text-shadow:0 5px 0 #8a5a00,0 12px 30px rgba(0,0,0,.35);line-height:1.05}
.end{left:90px;width:900px;top:420px;background:rgba(255,252,244,.96);border-radius:48px;padding:50px 40px 44px;text-align:center;box-shadow:0 18px 44px rgba(0,0,0,.22);border:5px solid #ffe066}
.face{width:230px;height:230px;border-radius:50%;border:8px solid #fff;box-shadow:0 10px 26px rgba(0,0,0,.2);background-size:cover;background-position:center}
#fx{position:absolute;inset:0}
"""
H=[];C=[]
def el(cls,html,a,b,anim="pop",style=""):
    i=len(C);C.append(dict(id=f"e{i}",a=a,b=b,anim=anim));H.append(f'<div id="e{i}" class="e {cls}" style="{style}">{html}</div>')
el("hook","แก้วนี้… เริ่มจาก<br><span style='color:#ffe066'>ต้นเลมอน</span> 🍋",0.0,2.85,"slam")
for i,txt in {2:"สไลซ์บาง ๆ",3:"น้ำผึ้งสดจาก Capy 🍯",5:"เลมอน × น้ำผึ้ง",8:"ตีมัทฉะสด 🍵",9:"ไซรัปหมัก 20 วัน",11:"ชิมหน่อยไหม? 💚",12:"หมดแก้ว! 🥰"}.items():
    el("pill",txt,S[i-1]+0.15,S[i]-0.08,"pop")
el("day",'<div class="top">วันที่</div><div class="num" id="dnum">1</div>',S[5]+0.1,S[7]-0.08,"pop")
el("pill","หมักไว้ 20 วัน ⏳",S[5]+0.3,S[6]-0.05,"pop")
el("pill","เปิดโหล! ✨",S[6]+0.1,S[7]-0.08,"slam")
el("title",'<div class="a">Matcha</div><div class="b">Honey Lemon</div>',S[9]+0.6,S[10]-0.1,"slam")
el("end",'<div style="font-weight:700;font-size:96px;color:#243e1b;line-height:1.02">Matcha<br><span style="color:#d99a00">Honey Lemon</span></div>'
   '<div style="font-family:Plex;font-weight:600;font-size:40px;color:#7a6a2a;margin-top:16px">🍋 เลมอนหมักน้ำผึ้ง 20 วัน × มัทฉะ</div>'
   '<div style="font-family:Plex;font-weight:600;font-size:40px;color:#3f8f3a;margin-top:26px">แท็กคนที่อยากแบ่งแก้วนี้ให้ 💚</div>'
   '<div style="font-family:Plex;font-size:34px;color:#6b6a55;margin-top:22px">Hibi Matcha Cafe · 5 สาขา<br>LINE MAN · Grab · ShopeeFood</div>',S[12]+0.15,T+1,"pop")
el("face","",S[12]+0.6,T+1,"pop",f"left:120px;top:1170px;background-image:url(file://{CH}/hibi_face.png)")
el("face","",S[12]+0.8,T+1,"pop",f"left:730px;top:1170px;background-image:url(file://{CH}/capy_face.png)")
FX=[dict(kind="heart",a=S[3],b=S[4]),dict(kind="heart",a=S[10]+1.2,b=S[11]),dict(kind="heart",a=S[11],b=S[12]),
    dict(kind="spark",a=S[6],b=S[7]),dict(kind="spark",a=S[9],b=S[10]),dict(kind="spark",a=S[12],b=T)]
JS="""
const C=__C__, FX=__FX__;
const ease=x=>1-Math.pow(1-x,3), back=x=>{const c=1.9;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)}, cl=x=>Math.max(0,Math.min(1,x));
function rnd(i){const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x)}
const HEART='<svg viewBox="0 0 24 22" width="100%" height="100%"><path d="M12 21s-9-5.6-9-12A5 5 0 0 1 12 6a5 5 0 0 1 9 3c0 6.4-9 12-9 12z" fill="#ff7aa2" stroke="#fff" stroke-width="1.6"/></svg>';
const SPARK='<svg viewBox="0 0 24 24" width="100%" height="100%"><path d="M12 0l2.6 9.4L24 12l-9.4 2.6L12 24l-2.6-9.4L0 12l9.4-2.6z" fill="#fff6b0"/></svg>';
const fx=document.getElementById('fx'); const parts=[];
FX.forEach((f,k)=>{const n=f.kind=='heart'?14:16;for(let i=0;i<n;i++){const d=document.createElement('div');d.style.cssText='position:absolute;opacity:0';d.innerHTML=f.kind=='heart'?HEART:SPARK;fx.appendChild(d);parts.push({d,f,i,k})}});
function render(t){
 for(const c of C){const e=document.getElementById(c.id);
  if(t<c.a||t>c.b){e.style.opacity=0;continue}
  const i=cl((t-c.a)/0.35),o=cl((c.b-t)/0.2);let op=o,tr='';
  if(c.anim=='pop'){op*=cl(i*2.5);tr=`scale(${0.7+0.3*back(i)})`}
  else if(c.anim=='slam'){op*=cl(i*3);tr=`scale(${1.5-0.5*ease(cl((t-c.a)/0.25))})`}
  e.style.opacity=op;e.style.transform=tr+(o<1?` scale(${0.94+0.06*o})`:'');}
 const dn=document.getElementById('dnum'); if(dn){const a=__S5__+0.4,b=__S6__-0.4;dn.textContent=Math.max(1,Math.min(20,1+Math.floor(19*cl((t-a)/(b-a)))));}
 for(const p of parts){const {f,i,d}=p;const life=f.b-f.a;const st=f.a+rnd(i+p.k*31)*life*0.6;const dur=f.kind=='heart'?1.8:0.9;const u=(t-st)/dur;
  if(t<f.a||t>f.b||u<0||u>1){d.style.opacity=0;continue}
  const x=80+rnd(i*7+p.k)*920, sz=f.kind=='heart'?50+rnd(i*3)*60:36+rnd(i*5)*50;
  let y,op,sc;
  if(f.kind=='heart'){y=1350-u*700-rnd(i*11)*250;op=Math.sin(Math.PI*u);sc=0.6+0.5*ease(cl(u*3))}
  else{y=300+rnd(i*13+p.k)*1000;op=Math.sin(Math.PI*u);sc=0.4+Math.sin(Math.PI*u)}
  d.style.left=x+'px';d.style.top=y+'px';d.style.width=sz+'px';d.style.height=sz+'px';d.style.opacity=op;
  d.style.transform=`translate(-50%,-50%) scale(${sc}) rotate(${(rnd(i)-0.5)*40+(f.kind=='spark'?u*90:Math.sin(u*6)*10)}deg)`;}
}
""".replace("__C__",json.dumps(C)).replace("__FX__",json.dumps(FX)).replace("__S5__",str(S[5])).replace("__S6__",str(S[6]))
open(f"{D}/mg.html","w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div id='fx'></div>{''.join(H)}<script>{JS}</script></body></html>")
print("ok")
