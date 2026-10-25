"""Matcha process reel (9:16, ~21s): hook -> 4 steps (scoop, sift, whisk, pour) -> hero.
Real footage stabilized (vidstab); AI shots from Higgsfield (sift macro, whisk, transition, hero angle).
Zoom: 'ramp' = slow push-in; 'punch' = 1.18x->1.0 impact on the cut."""
import subprocess, os
D = os.path.dirname(os.path.abspath(__file__)); os.chdir(D)
ENC = "-c:v libx264 -pix_fmt yuv420p -r 30 -preset medium -crf 18 -c:a aac -b:a 160k -ar 48000 -ac 2".split()
LN = "loudnorm=I=-16:TP=-1.5:LRA=11"
def run(a): subprocess.run(["ffmpeg", "-v", "error", "-y"] + a, check=True)
def dur(f): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))

def seg(src, out, ss, t, speed=1.0, zoom=None, amt=0.15, zy=0.5, ov=None, gain=0, grade=True):
    n = int(round(t / speed * 30))
    if zoom == "ramp":  z = f"1+{amt}*on/{n}"
    elif zoom == "punch": z = "if(lt(on,9),1.18-0.18*on/9,1)"
    elif zoom == "punchramp": z = f"if(lt(on,9),1.18-0.18*on/9,1+{amt}*(on-9)/{n})"
    else: z = "1"
    v = (f"[0:v]setpts=PTS/{speed},fps=30,scale=2160:3840:flags=lanczos,"
         f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih*{zy}-(ih/zoom/2)':d=1:s=1080x1920:fps=30,setsar=1")
    if grade: v += ",eq=saturation=1.08:contrast=1.04,unsharp=5:5:0.4:5:5:0"
    a = (f"[0:a]atempo={speed}," if speed != 1 else "[0:a]") + f"volume={gain}dB,{LN},afade=in:st=0:d=0.04"
    ins = ["-ss", str(ss), "-t", str(t), "-i", src]
    if ov:
        ins += ["-loop", "1", "-i", ov]
        fc = f"{v}[b];[1]format=rgba,fade=in:st=0:d=0.2:alpha=1[o];[b][o]overlay=0:0:shortest=1[v];{a}[a]"
    else:
        fc = f"{v}[v];{a}[a]"
    run(ins + ["-filter_complex", fc, "-map", "[v]", "-map", "[a]", "-t", f"{t/speed:.3f}"] + ENC + [out])
    return out

S = []
S.append(seg("f3.mp4", "p0.mp4", 4.8, 3.6, speed=1.6, zoom="ramp", amt=0.25, zy=0.42, ov="ov/hook.png", gain=4))        # HOOK: foam cascade
S.append(seg("f2_stab.mp4", "p1.mp4", 0.3, 4.8, speed=1.6, zoom="punchramp", amt=0.12, zy=0.45, ov="ov/s1.png", gain=4)) # 1 scoop + scale
S.append(seg("ai/sift.mp4", "p2.mp4", 0.0, 4.0, speed=1.25, zoom="punch", ov="ov/s2.png"))                               # 2 sift (AI macro)
S.append(seg("ai/trans.mp4", "p3.mp4", 0.9, 3.1, speed=3.0, ov="ov/s2.png", grade=False))                                # AI transition
S.append(seg("ai/whisk.mp4", "p4.mp4", 0.0, 5.0, speed=1.2, zoom="punchramp", amt=0.15, zy=0.5, ov="ov/s3.png"))          # 3 whisk (AI)
S.append(seg("f3.mp4", "p5.mp4", 0.0, 4.8, speed=1.4, zoom="punchramp", amt=0.18, zy=0.45, ov="ov/s4.png", gain=4))      # 4 pour over ice
S.append(seg("ai/hero.mp4", "p6.mp4", 0.0, 4.0, speed=1.0, ov="ov/end.png"))                                              # hero angle + end card
open("list.txt", "w").write("".join(f"file '{s}'\n" for s in S))
run(["-f", "concat", "-safe", "0", "-i", "list.txt"] + ENC + ["-movflags", "+faststart", "matcha_process_reel.mp4"])
print("done", round(dur("matcha_process_reel.mp4"), 2))
