"""Edit '1 แก้ว 9 มุม' reel (16 s @ 120 BPM, 1 shot = 2 beats): real-photo hook, 9 Higgsfield angles, MG grid finale.
Music: Funky Hibi Matcha 2:22.14 -> 2:38.14 (ends on the song's real ending)."""
import subprocess, os
D=os.path.dirname(os.path.abspath(__file__)); os.chdir(D)
F=f"{D}/../frames"; REAL=f"{D}/../real/hero_IMG_9222_916.jpg"
SONG=f"{D}/../../../xmas-band-hibi-capy/audio/funky_hibi_matcha_2m08-2m38.m4a"; SONG_OFF=14.0
T=16; S=[0,2]+[3+k for k in range(9)]+[T]       # hook 0-2, angles 2-11 (1 s each), MG grid 11-16
def run(a): subprocess.run(["ffmpeg","-v","error","-y"]+a,check=True)
GR="eq=saturation=1.03:contrast=1.02,unsharp=5:5:0.25:5:5:0"
PUNCH="if(lte(on,5),1.08-0.016*on,1.0+0.025*(on-5)/{n})"
def still(src,out,t,z=PUNCH):
    n=round(t*30)
    vf=f"[0:v]scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,zoompan=z='{z.format(n=n)}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,setsar=1,{GR}[v]"
    run(["-loop","1","-i",src,"-filter_complex",vf,"-map","[v]","-frames:v",str(n),"-an","-c:v","libx264","-pix_fmt","yuv420p","-crf","16",out])
def clip(src,out,t,off=0.6):
    n=round(t*30)
    vf=(f"[0:v]trim=start={off},setpts=PTS-STARTPTS,fps=30,scale=2160:3840:flags=lanczos,"
        f"zoompan=z='{PUNCH.format(n=n)}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,setsar=1,{GR}[v]")
    run(["-i",src,"-filter_complex",vf,"-map","[v]","-frames:v",str(n),"-an","-c:v","libx264","-pix_fmt","yuv420p","-crf","16",out])
os.makedirs("segs",exist_ok=True); L=[]
still(REAL,"segs/h.mp4",2.0,"1.0+0.06*on/{n}"); L.append("segs/h.mp4")
for i in range(1,10):
    o=f"segs/a{i:02d}.mp4"; v=f"clips/v{i:02d}.mp4"
    clip(v,o,1.0) if os.path.exists(v) else still(f"{F}/a{i:02d}.png",o,1.0); L.append(o)
still(f"{F}/a09.png","segs/tail.mp4",T-11,"1"); L.append("segs/tail.mp4")      # under the opaque grid
open("segs/list.txt","w").write("".join(f"file '{os.path.basename(x)}'\n" for x in L))
run(["-f","concat","-safe","0","-i","segs/list.txt","-c","copy","base.mp4"])
# SFX: soft shutter tick on every angle, pops as grid tiles land
run(["-f","lavfi","-i","anoisesrc=d=0.06:c=white:a=0.8","-af","highpass=f=2500,afade=t=out:st=0.0:d=0.06,volume=-24dB","tick.wav"])
run(["-f","lavfi","-i","aevalsrc='0.9*sin(2*PI*(300+900*exp(-t*40))*t)*exp(-t*28)':s=48000:d=0.18","-af","volume=-25dB","pop.wav"])
ev=[("tick.wav",2.0+k) for k in range(9)]+[("pop.wav",11.15+k*0.125) for k in range(9)]+[("pop.wav",14.0)]
ins=[];fl=[]
for k,(f,t) in enumerate(ev): ins+=["-i",f]; fl.append(f"[{k}]adelay={int(t*1000)}|{int(t*1000)}[e{k}]")
fl.append("".join(f"[e{k}]" for k in range(len(ev)))+f"amix=inputs={len(ev)}:normalize=0,apad,atrim=0:{T}[o]")
run(ins+["-filter_complex",";".join(fl),"-map","[o]","-ac","2","-ar","48000","sfx.wav"])
run(["-ss",str(SONG_OFF),"-t",str(T),"-i",SONG,"-i","sfx.wav","-filter_complex",
     f"[0:a]aresample=48000,afade=t=in:d=0.02[m];[m][1:a]amix=inputs=2:normalize=0,atrim=0:{T},loudnorm=I=-15:TP=-2:LRA=8,volume=1dB,alimiter=limit=0.82:level=disabled[a]",
     "-map","[a]","-ar","48000","mix.wav"])
run(["-i","base.mp4","-framerate","30","-i","frames/%05d.png","-i","mix.wav","-filter_complex","[0:v][1:v]overlay=0:0:format=auto,format=yuv420p[v]",
     "-map","[v]","-map","2:a","-c:v","libx264","-preset","medium","-crf","19","-r","30","-c:a","aac","-b:a","192k","-movflags","+faststart","-t",str(T),
     "../one_cup_nine_angles_reel.mp4"])
print("done")
