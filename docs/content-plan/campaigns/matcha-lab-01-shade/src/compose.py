"""Edit Matcha Lab #1: 11 shots on the VO-driven timeline, MG overlay, VO + original music bed + SFX."""
import subprocess, os, timeline
D=os.path.dirname(os.path.abspath(__file__)); os.chdir(D)
F=f"{D}/../frames"; S,VO=timeline.plan(); T=S[-1]
def run(a): subprocess.run(["ffmpeg","-v","error","-y"]+a,check=True)
def dur(p): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p]))
GR="eq=saturation=1.04:contrast=1.03,unsharp=5:5:0.3:5:5:0"
def shot(i,out,t):
    n=round(t*30); v=f"clips/v{i:02d}.mp4"
    if os.path.exists(v):
        d=dur(v)-0.1; sp=min(1.0,d/t)             # stretch (slow-mo) if the shot is longer than the clip
        z=f"1+0.05*on/{n}"
        vf=(f"[0:v]setpts=PTS/{sp:.4f},fps=30,scale=2160:3840:flags=lanczos,zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,setsar=1,{GR}[v]")
        run(["-i",v,"-filter_complex",vf,"-map","[v]","-frames:v",str(n),"-an","-c:v","libx264","-pix_fmt","yuv420p","-crf","16","-preset","medium",out])
    else:                                           # still: slow camera move on the frame (end card = blurred s09)
        src=f"{F}/s{9 if i==11 else i:02d}.png"
        z="1.12" if i==11 else f"1+0.07*on/{n}"
        y="ih/2-(ih/zoom/2)"
        extra=",gblur=sigma=20,eq=brightness=0.05:saturation=0.85" if i==11 else ""
        vf=f"[0:v]scale=2160:3840:flags=lanczos,zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='{y}':d=1:s=1080x1920:fps=30,setsar=1,{GR}{extra}[v]"
        run(["-loop","1","-i",src,"-filter_complex",vf,"-map","[v]","-frames:v",str(n),"-an","-c:v","libx264","-pix_fmt","yuv420p","-crf","16","-preset","medium",out])
    return out
os.makedirs("segs",exist_ok=True); L=[]
for i in range(1,12): L.append(shot(i,f"segs/s{i:02d}.mp4",S[i]-S[i-1]))
open("segs/list.txt","w").write("".join(f"file '{os.path.basename(x)}'\n" for x in L))
run(["-f","concat","-safe","0","-i","segs/list.txt","-c","copy","base.mp4"])
# VO track: each tightened line placed at its shot start + lead
ins=[];fl=[]
for k in range(11):
    p=f"vo/t{k+1:02d}.wav"
    if not os.path.exists(p): continue
    ins+=["-i",p]; j=len(ins)//2-1; ms=int(VO[k]*1000); fl.append(f"[{j}]adelay={ms}|{ms}[v{j}]")
m=len(ins)//2
fl.append("".join(f"[v{j}]" for j in range(m))+f"amix=inputs={m}:normalize=0,apad,atrim=0:{T:.3f},loudnorm=I=-16:TP=-2:LRA=7[o]")
run(ins+["-filter_complex",";".join(fl),"-map","[o]","-ac","1","-ar","48000","vo.wav"])
# SFX: whoosh on shot changes, pops on labels, shimmer on reveals
run(["-f","lavfi","-i","anoisesrc=d=0.45:c=pink:a=0.6","-af","highpass=f=400,lowpass=f=5000,afade=t=in:d=0.25,afade=t=out:st=0.25:d=0.2,volume=-24dB","whoosh.wav"])
run(["-f","lavfi","-i","aevalsrc='0.9*sin(2*PI*(300+900*exp(-t*40))*t)*exp(-t*28)':s=48000:d=0.18","-af","volume=-20dB","pop.wav"])
run(["-f","lavfi","-i","aevalsrc='0.5*sin(2*PI*1568*t)*exp(-t*4)+0.35*sin(2*PI*2093*t)*exp(-t*5)+0.25*sin(2*PI*2637*t)*exp(-t*6)':s=48000:d=1.4","-af","volume=-19dB","chime.wav"])
ev=[("whoosh.wav",max(0,s-0.2)) for s in S[1:11]]+[("pop.wav",S[i-1]+0.15) for i in (2,3,4,5,6,8,9)]
ev+=[("pop.wav",t) for t in (S[4]+0.3,S[4]+1.6,S[6]+0.2,S[6]+0.7)]+[("pop.wav",S[9]+0.6+k*0.75) for k in range(4)]
ev+=[("chime.wav",t) for t in (0.05,S[3]+0.5,S[4]+2.2,S[8]+0.15,S[10]+0.15)]
ins=[];fl=[]
for k,(f,t) in enumerate(ev): ins+=["-i",f]; fl.append(f"[{k}]adelay={int(t*1000)}|{int(t*1000)}[e{k}]")
fl.append("".join(f"[e{k}]" for k in range(len(ev)))+f"amix=inputs={len(ev)}:normalize=0,apad,atrim=0:{T:.3f}[o]")
run(ins+["-filter_complex",";".join(fl),"-map","[o]","-ac","2","sfx.wav"])
# mix: VO on top, music ducked under the voice (sidechain), SFX
run(["-i","vo.wav","-i","music.wav","-i","sfx.wav","-filter_complex",
     "[0:a]aformat=channel_layouts=stereo,asplit=2[vo][sc];[1:a]volume=-12dB[mu];[mu][sc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=350[duck];"
     f"[vo][duck][2:a]amix=inputs=3:normalize=0,atrim=0:{T:.3f},loudnorm=I=-14:TP=-1.5:LRA=8[a]","-map","[a]","-ar","48000","mix.wav"])
run(["-i","base.mp4","-framerate","30","-i","frames/%05d.png","-i","mix.wav","-filter_complex","[0:v][1:v]overlay=0:0:format=auto,format=yuv420p[v]",
     "-map","[v]","-map","2:a","-c:v","libx264","-preset","medium","-crf","19","-r","30","-c:a","aac","-b:a","192k","-movflags","+faststart","-t",f"{T:.3f}","final.mp4"])
print("done",round(T,2))
