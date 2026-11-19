"""Tighten each TTS line: drop leading/trailing silence, shrink every pause (0.07 s short / 0.16 s long),
voice chain from knowledge/04, then 1.1x tempo (pitch kept). Writes vo/t01..t11.wav + durations to vo/dur.txt."""
import subprocess, re, os, sys
D=os.path.dirname(os.path.abspath(__file__)); os.chdir(D)
PAD=0.04; TEMPO=1.10
CHAIN=("highpass=f=80,deesser=i=0.3,equalizer=f=250:t=q:w=1.2:g=-2,equalizer=f=3500:t=q:w=1.2:g=2.5,"
       "highshelf=f=10000:g=1.5,acompressor=threshold=-20dB:ratio=3:attack=6:release=90:makeup=2")
def dur(p): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p]))
def sil(p):
    o=subprocess.run(["ffmpeg","-hide_banner","-i",p,"-af","silencedetect=n=-40dB:d=0.10","-f","null","-"],capture_output=True,text=True).stderr
    s=[float(x) for x in re.findall(r"silence_start: ([\d.]+)",o)]; e=[float(x) for x in re.findall(r"silence_end: ([\d.]+)",o)]
    if len(e)<len(s): e.append(dur(p))
    return list(zip(s,e))
out=[]
for n in range(1,12):
    src=f"vo/l{n:02d}.wav"
    if not os.path.exists(src): continue
    T=dur(src); sp=[]; prev=0.0
    for a,b in sil(src):
        if a-prev>0.03: sp.append((prev,a))
        prev=b
    if T-prev>0.03: sp.append((prev,T))
    parts=[];fl=[]
    for k,(a,b) in enumerate(sp):
        a2=max(0,a-PAD); b2=min(T,b+PAD)
        fl.append(f"[0:a]atrim={a2:.3f}:{b2:.3f},asetpts=PTS-STARTPTS[s{k}]")
        parts.append(f"[s{k}]")
        if k<len(sp)-1:
            g=0.16 if sp[k+1][0]-b>0.6 else 0.07
            fl.append(f"anullsrc=r=44100:cl=mono,atrim=0:{g:.3f}[g{k}]"); parts.append(f"[g{k}]")
    fl.append("".join(parts)+f"concat=n={len(parts)}:v=0:a=1,{CHAIN},rubberband=tempo={TEMPO}:formant=preserved,aresample=48000[o]")
    subprocess.run(["ffmpeg","-v","error","-y","-i",src,"-filter_complex",";".join(fl),"-map","[o]","-ac","1",f"vo/t{n:02d}.wav"],check=True)
    out.append(f"{n} {dur(f'vo/t{n:02d}.wav'):.3f}")
open("vo/dur.txt","w").write("\n".join(out)+"\n"); print("\n".join(out))
