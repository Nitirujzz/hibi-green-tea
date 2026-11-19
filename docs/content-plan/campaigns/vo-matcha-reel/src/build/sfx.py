"""Subtle SFX bed synced to the MG cues: soft 'pop' on card entries, airy whoosh on each section change."""
import subprocess, contextlib, io, os
with contextlib.redirect_stdout(io.StringIO()): import mg
D=os.path.dirname(os.path.abspath(__file__)); os.chdir(D)
def run(a): subprocess.run(["ffmpeg","-v","error","-y"]+a,check=True)
run(["-f","lavfi","-i","aevalsrc='0.9*sin(2*PI*(260+900*exp(-t*40))*t)*exp(-t*28)':s=48000:d=0.18","-af","volume=-17dB","pop.wav"])
run(["-f","lavfi","-i","anoisesrc=color=pink:d=0.5:a=0.6:r=48000","-af","bandpass=f=1800:w=1600,afade=in:d=0.28:curve=exp,afade=out:st=0.28:d=0.22,volume=-19dB","whoosh.wav"])
ev=[]
for c in mg.CUES:
    if c["anim"] in ("pop","slam","wobble","shake","row"): ev.append(("pop.wav",c["a"]))
    if c["anim"]=="flash": ev.append(("whoosh.wav",c["a"]-0.2))
ev.append(("whoosh.wav",mg.CUES[[c['id'] for c in mg.CUES].index('recap')]["a"]-0.25))
ins=[];fl=[]
for i,(f,t) in enumerate(ev):
    ins+=["-i",f]; d=max(0,int(t*1000)); fl.append(f"[{i}]adelay={d}|{d}[a{i}]")
fl.append("".join(f"[a{i}]" for i in range(len(ev)))+f"amix=inputs={len(ev)}:normalize=0,apad,atrim=0:{mg.T:.3f}[o]")
run(ins+["-filter_complex",";".join(fl),"-map","[o]","-ac","2","sfx.wav"]); print("sfx events",len(ev))
