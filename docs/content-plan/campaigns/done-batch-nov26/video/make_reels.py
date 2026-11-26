"""Turn carousel slides (tiktok/{code}_nn.jpg, 1080x1920) into short Reels: slide-in transitions + slow zoom + soft ukulele bed."""
import subprocess, glob, os
D=os.path.dirname(os.path.abspath(__file__)); SRC=f"{D}/../tiktok"
MUSIC=f"{D}/../../hibi-capy-small-moments/src/music.wav"
SLIDE=2.6; X=0.35            # seconds per slide, transition length
def run(a): subprocess.run(["ffmpeg","-v","error","-y"]+a,check=True)
for code in ("G12","K09","SQ05"):
    fs=sorted(glob.glob(f"{SRC}/{code}_*.jpg")); n=len(fs)
    ins=[];fl=[]
    for i,f in enumerate(fs):
        d=SLIDE+X; fr=round(d*30)
        ins+=["-loop","1","-framerate","30","-t",f"{d:.2f}","-i",f]
        z="1.0+0.04*on/%d"%fr
        fl.append(f"[{i}:v]scale=2160:3840,zoompan=z='{z}':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d=1:s=1080x1920:fps=30,setsar=1,format=yuv420p[v{i}]")
    prev="v0"; off=0
    for i in range(1,n):
        off+=SLIDE
        tr="slideleft" if i%2 else "smoothleft"
        fl.append(f"[{prev}][v{i}]xfade=transition={tr}:duration={X}:offset={off:.2f}[x{i}]"); prev=f"x{i}"
    T=SLIDE*n+X
    fl.append(f"[{prev}]trim=0:{T:.2f}[v]")
    fl.append(f"[{n}:a]atrim=0:{T:.2f},afade=t=out:st={T-0.8:.2f}:d=0.8,loudnorm=I=-15:TP=-2,volume=1dB,alimiter=limit=0.82:level=disabled[a]")
    run(ins+["-i",MUSIC,"-filter_complex",";".join(fl),"-map","[v]","-map","[a]","-c:v","libx264","-crf","20","-preset","medium","-pix_fmt","yuv420p","-r","30",
             "-c:a","aac","-b:a","192k","-movflags","+faststart",f"{D}/{code}_reel.mp4"])
    print(code, round(T,2))
