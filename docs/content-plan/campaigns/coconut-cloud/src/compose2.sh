#!/bin/bash
# AI hook (clipA 0-3.5s) -> real in-store pour (real.mp4 5s-end, 1.6x) -> AI orbit (clipB) + card -> end card
set -e
cd "$(dirname "$0")"
ENC="-c:v libx264 -pix_fmt yuv420p -r 30 -preset medium -crf 18 -c:a aac -b:a 160k -ar 48000 -ac 2"
HA=3.5
ffmpeg -v error -y -t $HA -i clipA.mp4 -loop 1 -t $HA -i o1.png -filter_complex \
"[1]format=rgba,fade=in:st=0:d=0.25:alpha=1,fade=out:st=3.1:d=0.35:alpha=1[a1];[0:v]scale=1080:1920,setsar=1[b];[b][a1]overlay=0:0[v];[0:a]afade=out:st=3.2:d=0.3[a]" \
-map "[v]" -map "[a]" $ENC segA.mp4
SP=1.6; RS=5.0
DR=$(python3 -c "print((24.72-$RS)/$SP)")
ffmpeg -v error -y -ss $RS -i real/real.mp4 -loop 1 -i oreal.png -filter_complex \
"[0:v]setpts=PTS/$SP,scale=1080:1920:flags=lanczos,setsar=1,eq=saturation=1.08:contrast=1.03[b];[1]format=rgba,fade=in:st=0:d=0.3:alpha=1[o];[b][o]overlay=0:0:shortest=1[v];[0:a]atempo=$SP,volume=8dB,afade=in:st=0:d=0.3[a]" \
-map "[v]" -map "[a]" -t $DR $ENC segR.mp4
DB=$(ffprobe -v error -show_entries format=duration -of csv=p=0 clipB.mp4)
ffmpeg -v error -y -i clipB.mp4 -loop 1 -t $DB -i o3.png -filter_complex \
"[1]format=rgba,fade=in:st=0.4:d=0.35:alpha=1[a3];[0:v]scale=1080:1920,setsar=1[b];[b][a3]overlay=0:0:enable='gte(t,0.4)'[v]" \
-map "[v]" -map 0:a $ENC segB.mp4
ffmpeg -v error -y -sseof -0.1 -i clipB.mp4 -frames:v 1 -vf scale=1080:1920 lastB.png
ffmpeg -v error -y -loop 1 -t 2.5 -i lastB.png -loop 1 -t 2.5 -i end.png -f lavfi -t 2.5 -i anullsrc=r=48000:cl=stereo -filter_complex \
"[1]format=rgba,fade=in:st=0:d=0.35:alpha=1[e];[0:v]setsar=1[b];[b][e]overlay=0:0[v]" -map "[v]" -map 2:a $ENC -shortest segE.mp4
printf "file 'segA.mp4'\nfile 'segR.mp4'\nfile 'segB.mp4'\nfile 'segE.mp4'\n" > list.txt
ffmpeg -v error -y -f concat -safe 0 -i list.txt $ENC -movflags +faststart coconut_cloud_reel.mp4
ffprobe -v error -show_entries format=duration,size -of compact coconut_cloud_reel.mp4
