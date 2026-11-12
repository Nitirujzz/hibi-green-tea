"""VO reel '5 ความผิดพลาดที่ทำให้มัทฉะขม' — base picture cut to the tightened VO, then MG layer + SFX on top.
Shots: AI = Higgsfield (gpt_image_2_5 stills / seedance_2_5 motion), real = in-store footage from the process reel."""
import subprocess, os, sys
from timing import m, total
D=os.path.dirname(os.path.abspath(__file__)); os.chdir(D)
AI="../ai"; FT="/home/user/hibi-green-tea/docs/content-plan/campaigns/matcha-process-reel/src"
T=total()
def run(a): subprocess.run(["ffmpeg","-v","error","-y"]+a,check=True)
def dur(f): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]))
VENC="-c:v libx264 -pix_fmt yuv420p -r 30 -preset medium -crf 18 -an".split()

def shot(src,out,t,ss=0.0,zoom="ramp",amt=0.12,z0=1.0,zy=0.5,still=False,maxslow=0.55,fx=""):
    n=max(1,int(round(t*30)))
    if not still:
        avail=dur(src)-ss-0.05; sp=min(1.0,avail/t)
    else: sp=1.0
    if zoom=="ramp": z=f"{z0}+{amt}*on/{n}"
    elif zoom=="out": z=f"{z0+amt}-{amt}*on/{n}"
    elif zoom=="punch": z=f"if(lt(on,8),{z0}+0.16-0.16*on/8,{z0}+{amt}*(on-8)/{n})"
    else: z=str(z0)
    pre=f"setpts=PTS/{sp:.4f}," if sp!=1 else ""
    v=(f"[0:v]{pre}fps=30,scale=2160:3840:force_original_aspect_ratio=increase:flags=lanczos,crop=2160:3840,"
       f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih*{zy}-(ih/zoom/2)':d=1:s=1080x1920:fps=30,setsar=1,eq=saturation=1.06:contrast=1.03{fx}[v]")
    ins=(["-loop","1","-t",f"{t+0.2:.3f}","-i",src] if still else ["-ss",str(ss),"-i",src])
    run(ins+["-filter_complex",v,"-map","[v]","-frames:v",str(n)]+VENC+[out]); return out

# (start_orig, end_orig) are VO times; each shot fills [m(a), m(b)) on the new timeline
P=[]
def add(a,b,src,**k):
    t0=0 if a is None else m(a); t1=T if b is None else m(b)
    P.append((t0,t1,src,k))
add(None,4.8, f"{AI}/v0_face.mp4", zoom="ramp",amt=0.10)                                   # HOOK: bitter sip (AI)
add(4.8,7.6,  f"{FT}/footage/f3.mp4", ss=5.0, zoom="ramp",z0=1.35,amt=0.12,zy=0.62)        # silky real pour = what it should be
for i,(img,zy) in enumerate([("img1",.5),("img3",.5),("img4",.5),("img5",.55),("img6",.6)]):  # 5-mistake teaser flashes
    a=7.6+i*(10.6-7.6)/5; add(a,a+(10.6-7.6)/5, f"{AI}/{img}.png", still=True, zoom="punch",z0=1.05,amt=0.04,zy=zy)
add(10.6,16.4, f"{AI}/v1_boil.mp4", zoom="punch",amt=0.08)                                  # 1 ❌ boiling
add(16.4,20.6, f"{AI}/img1.png", still=True, zoom="ramp",z0=1.1,amt=0.18,zy=0.35)             # steam close
add(20.6,24.7, f"{AI}/img0.png", still=True, zoom="ramp",z0=1.15,amt=0.15,zy=0.3,fx=",eq=saturation=0.85")  # bitter face
add(24.7,30.2, f"{AI}/v4_gooseneck.mp4", zoom="punch",amt=0.06)                             # 1 ✅ 70–80°C
add(30.2,34.4, f"{AI}/img3.png", still=True, zoom="punch",z0=1.0,amt=0.10)                   # 2 ❌ clumps
add(34.4,38.2, f"{AI}/img3.png", still=True, zoom="ramp",z0=1.35,amt=0.2,zy=0.45)
add(38.2,41.6, f"{FT}/ai/sift.mp4", zoom="punch",amt=0.08)                                   # 2 ✅ sift
add(41.6,46.7, f"{AI}/img4.png", still=True, zoom="punch",z0=1.0,amt=0.12)                  # 3 most common
add(46.7,51.7, f"{AI}/v2_circle.mp4", zoom="ramp",amt=0.06)                                 # 3 ❌ circular
add(51.7,59.8, f"{FT}/ai/whisk.mp4", zoom="punch",amt=0.12,maxslow=0.6)                     # 3 ✅ M whisk
add(59.8,64.8, f"{AI}/img5.png", still=True, zoom="punch",z0=1.0,amt=0.1)                   # 4 ❌ heaped
add(64.8,70.9, f"{AI}/img5.png", still=True, zoom="ramp",z0=1.4,amt=0.15,zy=0.6)
add(70.9,77.5, f"{FT}/footage/f2_stab.mp4", zoom="punch",amt=0.10,zy=0.45)                  # 4 ✅ scoop on scale (real)
add(77.5,83.4, f"{FT}/footage/f1.mp4", zoom="ramp",amt=0.10,maxslow=0.4)                    # adjust to taste (real)
add(83.4,88.6, f"{AI}/v5_storage.mp4", zoom="punch",amt=0.06)                               # 5 ❌ open bag by stove
add(88.6,95.9, f"{AI}/img6.png", still=True, zoom="ramp",z0=1.3,amt=0.25,zy=0.65,fx=",eq=saturation=0.8")
add(95.9,103.3,f"{AI}/v3_fridge.mp4", zoom="punch",amt=0.08,maxslow=0.6)                     # 5 ✅ airtight in fridge
add(103.3,111.4,f"{FT}/footage/f3.mp4", ss=0.0, zoom="ramp",z0=1.3,amt=0.15,zy=0.62)          # CTA real pour
add(111.4,None,f"{FT}/ai/hero.mp4", zoom="ramp",z0=1.25,amt=0.1,zy=0.62,maxslow=0.4,fx=",gblur=sigma=14,eq=brightness=-0.08")  # recap bg
os.makedirs("segs",exist_ok=True); L=[]
for i,(t0,t1,src,k) in enumerate(P):
    # frame-accurate lengths: round boundaries to frames
    f0,f1=round(t0*30),round(t1*30)
    # long shots get a jump-cut punch-in halfway so the picture never sits still > ~2.5 s
    parts=[(f0,f1)] if f1-f0<=100 else [(f0,(f0+f1)//2),((f0+f1)//2,f1)]
    for j,(g0,g1) in enumerate(parts):
        kk=dict(k)
        if j==1:
            kk["z0"]=kk.get("z0",1.0)+0.18; kk["zoom"]="punch"; kk["amt"]=0.05
            if not kk.get("still"): kk["ss"]=kk.get("ss",0)+(g0-f0)/30*0.9
        L.append(shot(src,f"segs/s{i:02d}{j}.mp4",(g1-g0)/30,**kk))
open("segs/list.txt","w").write("".join(f"file '{os.path.basename(s)}'\n" for s in L))
run(["-f","concat","-safe","0","-i","segs/list.txt","-c","copy","base.mp4"])
print("base",round(dur("base.mp4"),2),"T",round(T,2))
