"""Coconut Cloud reel v6.
Hook 3s (B-roll + key message) -> real pour split into shots (stabilized) w/ info text -> [stir.mp4] -> [sip.mp4]
-> AI orbit + menu card -> end card -> loop tail (matches first frame).  Audio normalized per segment.
Drop real clips named stir.mp4 / sip.mp4 into ./shop/ and re-run to include them."""
import subprocess, os, sys
D = os.path.dirname(os.path.abspath(__file__)); os.chdir(D)
ENC = "-c:v libx264 -pix_fmt yuv420p -r 30 -preset medium -crf 18 -c:a aac -b:a 160k -ar 48000 -ac 2".split()
LN = "loudnorm=I=-16:TP=-1.5:LRA=11"
def run(args): subprocess.run(["ffmpeg", "-v", "error", "-y"] + args, check=True)
def dur(f): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))

def seg(src, out, ss, t, speed=1.0, zoom=1.0, zy=0.5, ov=None, ov_in=0.0, gain=0, grade=False):
    """cut [ss, ss+t] of src (source seconds), speed up, punch-in zoom (center x, zy = vertical focus), optional overlay"""
    v = f"[0:v]setpts=PTS/{speed},scale=1080:1920:flags=lanczos,setsar=1"
    if zoom > 1:
        w, h = int(1080 / zoom) // 2 * 2, int(1920 / zoom) // 2 * 2
        v += f",crop={w}:{h}:(iw-{w})/2:(ih-{h})*{zy},scale=1080:1920:flags=lanczos"
    if grade: v += ",eq=saturation=1.1:contrast=1.04:gamma=1.02,unsharp=5:5:0.5:5:5:0"
    v += "[b]"
    a = f"[0:a]atempo={speed}" if speed != 1 else "[0:a]anull"
    a += f",volume={gain}dB,{LN},afade=in:st=0:d=0.05[a]"
    inputs = ["-ss", str(ss), "-t", str(t), "-i", src]
    if ov:
        inputs += ["-loop", "1", "-i", ov]
        fc = f"{v};[1]format=rgba,fade=in:st={ov_in}:d=0.25:alpha=1[o];[b][o]overlay=0:0:shortest=1[v];{a}"
    else:
        fc = f"{v.replace('[b]','[v]')};{a}"
    run(inputs + ["-filter_complex", fc, "-map", "[v]", "-map", "[a]", "-t", str(t / speed)] + ENC + [out])

def build(hook_png, out):
    parts = []
    # HOOK 3s: whisk -> coconut water pour -> cloud lands (B-roll), key message from frame 1
    for i, (f, ss) in enumerate([("broll/b2.mp4", 1.5), ("broll/b1.mp4", 1.0), ("broll/b3.mp4", 1.0)]):
        seg(f, f"h{i}.mp4", ss, 1.0, gain=4); parts.append(f"h{i}.mp4")
    open("hl.txt", "w").write("".join(f"file '{p}'\n" for p in parts))
    run(["-f", "concat", "-safe", "0", "-i", "hl.txt", "-c", "copy", "hraw.mp4"])
    run(["-i", "hraw.mp4", "-loop", "1", "-t", "3", "-i", hook_png, "-filter_complex",
         "[1]format=rgba,fade=in:st=0:d=0.12:alpha=1[o];[0:v][o]overlay=0:0:shortest=1[v]", "-map", "[v]", "-map", "0:a"] + ENC + ["segH.mp4"])
    seq = ["segH.mp4"]
    # REAL pour (stabilized, real_stab starts at source 5s) split into shots
    R = "real/real_stab.mp4"
    seg(R, "r1.mp4", 0.8, 3.2, speed=1.6, ov="oreal.png", ov_in=0.2, gain=6, grade=True)              # wide: pour begins
    seg(R, "r2.mp4", 5.0, 3.5, speed=1.6, zoom=1.2, zy=0.45, ov="oreal.png", gain=6, grade=True)     # punch-in: cloud lands
    seg("broll/b3.mp4", "w1.mp4", 2.5, 1.2, gain=8)                                                    # B-roll macro wisps
    seg(R, "r3.mp4", 12.0, 4.0, speed=1.6, zoom=1.15, zy=0.6, ov="mid2.png", ov_in=0.1, gain=6, grade=True)  # layer builds
    seg(R, "r4.mp4", 17.0, 2.6, speed=1.6, ov="mid2.png", gain=6, grade=True)                          # finished layer, wide
    seq += ["r1.mp4", "r2.mp4", "w1.mp4", "r3.mp4", "r4.mp4"]
    # optional real shots from the shop (stir / sip) — included automatically when present
    for name in ("stir", "sip"):
        f = f"shop/{name}.mp4"
        if os.path.exists(f):
            seg(f, f"{name}_s.mp4", 0, min(3.0, dur(f)), gain=6, grade=True); seq.append(f"{name}_s.mp4")
    # AI orbit + menu card
    seg("clipB.mp4", "segB.mp4", 0, dur("clipB.mp4"), ov="o3.png", ov_in=0.4); seq.append("segB.mp4")
    # end card (soft ice ambience instead of dead silence)
    run(["-sseof", "-0.1", "-i", "clipB.mp4", "-frames:v", "1", "-vf", "scale=1080:1920", "lastB.png"])
    run(["-loop", "1", "-t", "2.2", "-i", "lastB.png", "-loop", "1", "-t", "2.2", "-i", "end.png", "-ss", "0", "-t", "2.2", "-i", "broll/b1.mp4",
         "-filter_complex", f"[1]format=rgba,fade=in:st=0:d=0.3:alpha=1[e];[0:v]setsar=1[b];[b][e]overlay=0:0[v];[2:a]{LN},volume=-10dB,afade=out:st=1.6:d=0.6[a]",
         "-map", "[v]", "-map", "[a]", "-shortest"] + ENC + ["segE.mp4"])
    seq.append("segE.mp4")
    # loop tail: the 0.6s right before the hook's first frame, so the video loops seamlessly
    seg("broll/b2.mp4", "tail.mp4", 0.9, 0.6, gain=4); seq.append("tail.mp4")
    open("list.txt", "w").write("".join(f"file '{p}'\n" for p in seq))
    run(["-f", "concat", "-safe", "0", "-i", "list.txt"] + ENC + ["-movflags", "+faststart", out])
    print(out, round(dur(out), 2), "s")

if __name__ == "__main__":
    for png, out in [("hook.png", "reel_A.mp4"), ("hookB.png", "reel_B.mp4"), ("hookC.png", "reel_C.mp4")][: int(sys.argv[1]) if len(sys.argv) > 1 else 3]:
        build(png, out)
