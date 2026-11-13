"""Edit Small Moments EP1 'จำได้ด้วย?!' (25 s): 7 Seedance shots + end-card still, MG overlay, original ukulele bed (music.py) + soft SFX."""
import subprocess, os
D=os.path.dirname(os.path.abspath(__file__)); os.chdir(D)
F=f"{D}/../frames"; S=[0,3,6,9,12,15,18,21,25]; T=25
OFF={1:0.2,2:0.5,3:0.4,4:0.6,5:0.1,6:0.4,7:0.5}     # where each 5 s clip is cut in
def run(a): subprocess.run(["ffmpeg","-v","error","-y"]+a,check=True)
def dur(p): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p]))
GR="eq=saturation=1.03:contrast=1.02:brightness=0.01,unsharp=5:5:0.25:5:5:0"
def shot(i,out,t):
    n=round(t*30); v=f"clips/v{i:02d}.mp4"
    z="if(lte(on,8),1.10-0.0125*on,1.0+0.03*(on-8)/%d)"%n if i==5 else "1.0+0.05*on/%d"%n   # soft push; a small punch on the surprise
    if os.path.exists(v):
        o=min(OFF.get(i,0.3),dur(v)-t-0.05)
        vf=(f"[0:v]trim=start={o:.2f},setpts=PTS-STARTPTS,fps=30,scale=2160:3840:flags=lanczos,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,setsar=1,{GR}[v]")
        run(["-i",v,"-filter_complex",vf,"-map","[v]","-frames:v",str(n),"-an","-c:v","libx264","-pix_fmt","yuv420p","-crf","16","-preset","medium",out])
    else:
        vf=f"[0:v]scale=2160:3840:flags=lanczos,zoompan=z='1.0+0.04*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,setsar=1,{GR}[v]"
        run(["-loop","1","-i",f"{F}/s{i:02d}.png","-filter_complex",vf,"-map","[v]","-frames:v",str(n),"-an","-c:v","libx264","-pix_fmt","yuv420p","-crf","16",out])
    return out
os.makedirs("segs",exist_ok=True); L=[shot(i,f"segs/s{i:02d}.mp4",S[i]-S[i-1]) for i in range(1,9)]
open("segs/list.txt","w").write("".join(f"file '{os.path.basename(x)}'\n" for x in L))
run(["-f","concat","-safe","0","-i","segs/list.txt","-c","copy","base.mp4"])
if not os.path.exists("music.wav"): subprocess.run(["python3","music.py"],check=True)
# SFX
run(["-f","lavfi","-i","aevalsrc='0.6*sin(2*PI*1320*t)*exp(-t*9)+0.4*sin(2*PI*1980*t)*exp(-t*11)':s=48000:d=0.6","-af","volume=-22dB","ting.wav"])
run(["-f","lavfi","-i","aevalsrc='0.9*sin(2*PI*(300+900*exp(-t*40))*t)*exp(-t*28)':s=48000:d=0.18","-af","volume=-21dB","pop.wav"])
run(["-f","lavfi","-i","aevalsrc='0.8*sin(2*PI*(220+520*t*(1-t*1.2))*t+3*sin(2*PI*9*t))*exp(-t*5)':s=48000:d=0.55","-af","volume=-21dB","boing.wav"])
run(["-f","lavfi","-i","aevalsrc='0.5*sin(2*PI*1568*t)*exp(-t*4)+0.35*sin(2*PI*2093*t)*exp(-t*5)+0.25*sin(2*PI*2637*t)*exp(-t*6)':s=48000:d=1.4","-af","volume=-23dB","chime.wav"])
run(["-f","lavfi","-i","aevalsrc='0.5*sin(2*PI*3100*t)*exp(-t*45)+0.4*sin(2*PI*4200*(t-0.07))*exp(-abs(t-0.07)*55)*gt(t,0.07)':s=48000:d=0.3","-af","volume=-22dB","clink.wav"])
ev=[("ting.wav",0.25),("pop.wav",3.25),("pop.wav",3.9),("pop.wav",6.35),("pop.wav",9.05),("boing.wav",12.0),("pop.wav",12.05),("chime.wav",12.4),
    ("clink.wav",15.25),("pop.wav",15.35),("chime.wav",18.1),("chime.wav",20.95)]
ins=[];fl=[]
for k,(f,t) in enumerate(ev): ins+=["-i",f]; fl.append(f"[{k}]adelay={int(t*1000)}|{int(t*1000)}[e{k}]")
fl.append("".join(f"[e{k}]" for k in range(len(ev)))+f"amix=inputs={len(ev)}:normalize=0,apad,atrim=0:{T}[o]")
run(ins+["-filter_complex",";".join(fl),"-map","[o]","-ac","2","-ar","48000","sfx.wav"])
run(["-i","music.wav","-i","sfx.wav","-filter_complex",f"[0:a]volume=-4dB[m];[m][1:a]amix=inputs=2:normalize=0,atrim=0:{T},afade=t=out:st={T-0.6}:d=0.6,loudnorm=I=-15:TP=-2:LRA=7,volume=1dB,alimiter=limit=0.82:level=disabled[a]",
     "-map","[a]","-ar","48000","mix.wav"])
run(["-i","base.mp4","-framerate","30","-i","frames/%05d.png","-i","mix.wav","-filter_complex","[0:v][1:v]overlay=0:0:format=auto,format=yuv420p[v]",
     "-map","[v]","-map","2:a","-c:v","libx264","-preset","medium","-crf","19","-r","30","-c:a","aac","-b:a","192k","-movflags","+faststart","-t",str(T),
     "../small_moments_ep1_jam_dai_duay.mp4"])
print("done")
