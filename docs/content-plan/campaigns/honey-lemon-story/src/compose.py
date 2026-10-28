"""Edit the Honey Lemon reel: 13 shots on the storyboard timing, MG overlay, native ASMR + original music + SFX."""
import subprocess, os
D=os.path.dirname(os.path.abspath(__file__)); os.chdir(D)
V=f"{D}/../v"; F=f"{D}/../f"
S=[0,3,6,9,11,14,18,20,23,26,30,33,36,40]; T=40.0
def run(a): subprocess.run(["ffmpeg","-v","error","-y"]+a,check=True)
def has(p): return os.path.exists(p)
GR="eq=saturation=1.05:contrast=1.02,unsharp=5:5:0.3:5:5:0"
def shot(i,out,t):
    n=round(t*30); v=f"{V}/v{i:02d}.mp4"
    if has(v):
        d=float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",v]))
        ss=min(0.5,max(0,d-t-0.05))
        z={10:"1+0.06*on/%d"%n,6:"1"}.get(i,"1+0.05*on/%d"%n)
        vf=f"[0:v]fps=30,scale=2160:3840:flags=lanczos,zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,setsar=1,{GR}[v]"
        af=f"[0:a]aformat=channel_layouts=stereo:sample_rates=48000,afade=t=in:d=0.08,afade=t=out:st={t-0.12:.2f}:d=0.12[a]"
        run(["-ss",f"{ss:.2f}","-i",v,"-filter_complex",vf+";"+af,"-map","[v]","-map","[a]","-frames:v",str(n),"-t",f"{t:.3f}",
             "-c:v","libx264","-pix_fmt","yuv420p","-crf","17","-preset","medium","-c:a","pcm_s16le",out])
    else:   # still fallback (credits ran out / blocked): camera move on the storyboard frame
        src=f"{F}/s{min(i,12) if i!=13 else 10:02d}.png"
        z={4:f"1.0+0.10*on/{n}",11:f"1.12",12:f"1.22-0.20*on/{n}",13:f"1.1"}.get(i,f"1+0.08*on/{n}")
        x={11:f"(iw-iw/zoom)*on/{n}"}.get(i,"iw/2-(iw/zoom/2)")
        extra=",gblur=sigma=18,eq=brightness=0.04:saturation=0.9" if i==13 else ""
        vf=f"[0:v]scale=2160:3840:flags=lanczos,zoompan=z='{z}':x='{x}':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,setsar=1,{GR}{extra}[v]"
        run(["-loop","1","-i",src,"-f","lavfi","-i","anullsrc=r=48000:cl=stereo","-filter_complex",vf,"-map","[v]","-map","1:a","-frames:v",str(n),"-t",f"{t:.3f}",
             "-c:v","libx264","-pix_fmt","yuv420p","-crf","17","-preset","medium","-c:a","pcm_s16le",out])
    return out
os.makedirs("segs",exist_ok=True); L=[]
for i in range(1,14): L.append(shot(i,f"segs/s{i:02d}.mov",S[i]-S[i-1]))
open("segs/list.txt","w").write("".join(f"file '{os.path.basename(x)}'\n" for x in L))
run(["-f","concat","-safe","0","-i","segs/list.txt","-c","copy","base.mov"])
# SFX: pops on text/heart moments + chimes on magic moments
run(["-f","lavfi","-i","aevalsrc='0.9*sin(2*PI*(300+900*exp(-t*40))*t)*exp(-t*28)':s=48000:d=0.18","-af","volume=-16dB","pop.wav"])
run(["-f","lavfi","-i","aevalsrc='0.5*sin(2*PI*1568*t)*exp(-t*4)+0.35*sin(2*PI*2093*t)*exp(-t*5)+0.25*sin(2*PI*2637*t)*exp(-t*6)':s=48000:d=1.4","-af","volume=-14dB","chime.wav"])
ev=[("pop.wav",t) for t in [S[1]+0.15,S[2]+0.15,S[4]+0.15,S[5]+0.1,S[7]+0.15,S[8]+0.15,S[10]+0.15,S[11]+0.15,S[12]+0.15,S[12]+0.6,S[12]+0.8]]
ev+=[("pop.wav",S[3]+0.3+k*0.35) for k in range(4)]+[("pop.wav",S[11]+0.3+k*0.4) for k in range(6)]
ev+=[("chime.wav",t) for t in [S[3]+0.1,S[6]+0.05,S[9]+0.55,S[11]+0.1,S[12]+0.1]]
ins=[];fl=[]
for k,(f,t) in enumerate(ev): ins+=["-i",f]; fl.append(f"[{k}]adelay={int(t*1000)}|{int(t*1000)}[e{k}]")
fl.append("".join(f"[e{k}]" for k in range(len(ev)))+f"amix=inputs={len(ev)}:normalize=0,apad,atrim=0:{T}[o]")
run(ins+["-filter_complex",";".join(fl),"-map","[o]","-ac","2","sfx.wav"])
# mix: native ASMR (leveled) + music bed + sfx
run(["-i","base.mov","-i","music.wav","-i","sfx.wav","-filter_complex",
     "[0:a]highpass=f=60,dynaudnorm=f=150:g=7:m=6,volume=-6dB[asmr];[1:a]volume=-15dB[mu];[asmr][mu][2:a]amix=inputs=3:normalize=0,atrim=0:40,loudnorm=I=-14:TP=-2.5:LRA=9[a]",
     "-map","[a]","-ar","48000","mix.wav"])
run(["-i","base.mov","-loop","1","-i","scrim.png","-loop","1","-i","scrim_bot.png","-framerate","30","-i","frames/%05d.png","-i","mix.wav","-filter_complex","[0:v][1:v]overlay=0:0:enable='lt(t,3)':shortest=1[b0];[b0][2:v]overlay=0:0:enable='between(t,26.5,30)':shortest=1[b1];[b1][3:v]overlay=0:0:format=auto,format=yuv420p[v]",
     "-map","[v]","-map","4:a","-c:v","libx264","-preset","medium","-crf","19","-r","30","-c:a","aac","-b:a","192k","-movflags","+faststart","-t","40","final.mp4"])
print("done")
