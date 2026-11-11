"""Edit Holiday Jam (30 s): 10 shots cut on the bar grid of 'Funky Hibi Matcha' 2:08.14-2:38.14, beat punch-zooms, MG overlay, music + light SFX."""
import subprocess, os
D=os.path.dirname(os.path.abspath(__file__)); os.chdir(D)
F=f"{D}/../frames"; SONG=f"{D}/../audio/funky_hibi_matcha_2m08-2m38.m4a"
S=[0,2,4,8,10,12,14,18,22,26,30]; T=30; BEAT=0.5
def run(a): subprocess.run(["ffmpeg","-v","error","-y"]+a,check=True)
def dur(p): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p]))
GR="eq=saturation=1.08:contrast=1.04,unsharp=5:5:0.3:5:5:0"
# punch on first frames of the shot (1.10 -> 1.0 in 8 frames), then slow push
PUNCH="if(lte(on,8),1.10-0.0125*on,1.0+0.04*(on-8)/{n})"
OFF={1:2.35,2:0.4,3:0.6,4:0.9,5:0.4,6:0.8,7:0.5,9:0.0}
SPD={6:1.6}   # speed-up so the whole gift toss + catch fits the 2 s shot
def shot(i,out,t):
    n=round(t*30); v=f"clips/v{i:02d}.mp4"
    if os.path.exists(v):
        sp=SPD.get(i,1.0); o=min(OFF.get(i,0.3),dur(v)-t*sp-0.05)
        vf=(f"[0:v]trim=start={o:.2f},setpts=(PTS-STARTPTS)/{sp},fps=30,scale=2160:3840:flags=lanczos,"
            f"zoompan=z='{PUNCH.format(n=n)}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,setsar=1,{GR}[v]")
        run(["-i",v,"-filter_complex",vf,"-map","[v]","-frames:v",str(n),"-an","-c:v","libx264","-pix_fmt","yuv420p","-crf","16","-preset","medium",out])
    elif i==8:   # still: 4 drinks — punch-zoom onto each cup, one per second (2 beats)
        parts=[]
        for k,cx in enumerate([0.14,0.37,0.62,0.87]):
            p=f"segs/s08_{k}.mp4"; parts.append(p)
            vf=(f"[0:v]scale=2160:3840:flags=lanczos,zoompan=z='if(lte(on,6),2.1-0.05*on,1.8+0.003*(on-6))':"
                f"x='max(0,min(iw-iw/zoom,iw*{cx}-iw/zoom/2))':y='ih*0.50-ih/zoom/2':d=1:s=1080x1920:fps=30,setsar=1,{GR}[v]")
            run(["-loop","1","-i",f"{F}/s08.png","-filter_complex",vf,"-map","[v]","-frames:v","30","-an","-c:v","libx264","-pix_fmt","yuv420p","-crf","16",p])
        open("segs/s08.txt","w").write("".join(f"file '{os.path.basename(p)}'\n" for p in parts))
        run(["-f","concat","-safe","0","-i","segs/s08.txt","-c","copy",out])
    else:        # end card still: slow push
        vf=f"[0:v]scale=2160:3840:flags=lanczos,zoompan=z='{PUNCH.format(n=n)}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,setsar=1,{GR}[v]"
        run(["-loop","1","-i",f"{F}/s{i:02d}.png","-filter_complex",vf,"-map","[v]","-frames:v",str(n),"-an","-c:v","libx264","-pix_fmt","yuv420p","-crf","16","-preset","medium",out])
    return out
os.makedirs("segs",exist_ok=True); L=[shot(i,f"segs/s{i:02d}.mp4",S[i]-S[i-1]) for i in range(1,11)]
open("segs/list.txt","w").write("".join(f"file '{os.path.basename(x)}'\n" for x in L))
run(["-f","concat","-safe","0","-i","segs/list.txt","-c","copy","base.mp4"])
# light SFX on top of the song: powder poof on the hook, pops when stickers land, chime on the end card
run(["-f","lavfi","-i","anoisesrc=d=0.5:c=pink:a=0.7","-af","highpass=f=600,lowpass=f=7000,afade=t=in:d=0.02,afade=t=out:st=0.05:d=0.45,volume=-20dB","poof.wav"])
run(["-f","lavfi","-i","aevalsrc='0.9*sin(2*PI*(300+900*exp(-t*40))*t)*exp(-t*28)':s=48000:d=0.18","-af","volume=-22dB","pop.wav"])
run(["-f","lavfi","-i","aevalsrc='0.5*sin(2*PI*1568*t)*exp(-t*4)+0.35*sin(2*PI*2093*t)*exp(-t*5)+0.25*sin(2*PI*2637*t)*exp(-t*6)':s=48000:d=1.4","-af","volume=-20dB","chime.wav"])
ev=[("poof.wav",0.0)]+[("pop.wav",t) for t in (0.05,2.05,4.05,8.05,12.0,14.05,18.05,22.05,26.5,27.0,27.5,28.0)]
ev+=[("pop.wav",18.0+k) for k in range(1,4)]+[("chime.wav",26.05)]
ins=[];fl=[]
for k,(f,t) in enumerate(ev): ins+=["-i",f]; fl.append(f"[{k}]adelay={int(t*1000)}|{int(t*1000)}[e{k}]")
fl.append("".join(f"[e{k}]" for k in range(len(ev)))+f"amix=inputs={len(ev)}:normalize=0,apad,atrim=0:{T}[o]")
run(ins+["-filter_complex",";".join(fl),"-map","[o]","-ac","2","-ar","48000","sfx.wav"])
run(["-i",SONG,"-i","sfx.wav","-filter_complex",f"[0:a]aresample=48000,afade=t=in:d=0.03[m];[m][1:a]amix=inputs=2:normalize=0,atrim=0:{T},loudnorm=I=-15.5:TP=-2:LRA=8[a]",
     "-map","[a]","-ar","48000","mix.wav"])
run(["-i","base.mp4","-framerate","30","-i","frames/%05d.png","-i","mix.wav","-filter_complex","[0:v][1:v]overlay=0:0:format=auto,format=yuv420p[v]",
     "-map","[v]","-map","2:a","-c:v","libx264","-preset","medium","-crf","19","-r","30","-c:a","aac","-b:a","192k","-movflags","+faststart","-t",str(T),
     "../hibi_capy_holiday_jam_30s.mp4"])
print("done")
