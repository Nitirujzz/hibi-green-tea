#!/bin/bash
set -e
cd "$(dirname "$0")"
DA=$(ffprobe -v error -show_entries format=duration -of csv=p=0 clipA.mp4)
DB=$(ffprobe -v error -show_entries format=duration -of csv=p=0 clipB.mp4)
ENC="-c:v libx264 -pix_fmt yuv420p -r 30 -preset medium -crf 18 -c:a aac -b:a 160k -ar 48000 -ac 2"
# A: hook + line 2
ffmpeg -v error -y -i clipA.mp4 -loop 1 -t $DA -i o1.png -loop 1 -t $DA -i o2.png -filter_complex \
"[1]format=rgba,fade=in:st=0:d=0.25:alpha=1,fade=out:st=2.3:d=0.3:alpha=1[a1];[2]format=rgba,fade=in:st=2.8:d=0.3:alpha=1[a2];\
[0:v]scale=1080:1920,setsar=1[b];[b][a1]overlay=0:0:enable='lte(t,2.6)'[v1];[v1][a2]overlay=0:0:enable='gte(t,2.8)'[v]" \
-map "[v]" -map 0:a $ENC segA.mp4
# B: product card
ffmpeg -v error -y -i clipB.mp4 -loop 1 -t $DB -i o3.png -filter_complex \
"[1]format=rgba,fade=in:st=0.4:d=0.35:alpha=1[a3];[0:v]scale=1080:1920,setsar=1[b];[b][a3]overlay=0:0:enable='gte(t,0.4)'[v]" \
-map "[v]" -map 0:a $ENC segB.mp4
# End card on last frame of B
ffmpeg -v error -y -sseof -0.1 -i clipB.mp4 -frames:v 1 -vf scale=1080:1920 lastB.png
ffmpeg -v error -y -loop 1 -t 2.5 -i lastB.png -loop 1 -t 2.5 -i end.png -f lavfi -t 2.5 -i anullsrc=r=48000:cl=stereo -filter_complex \
"[1]format=rgba,fade=in:st=0:d=0.35:alpha=1[e];[0:v]setsar=1[b];[b][e]overlay=0:0[v]" -map "[v]" -map 2:a $ENC -shortest segE.mp4
printf "file 'segA.mp4'\nfile 'segB.mp4'\nfile 'segE.mp4'\n" > list.txt
ffmpeg -v error -y -f concat -safe 0 -i list.txt $ENC -movflags +faststart coconut_cloud_reel.mp4
ffprobe -v error -show_entries format=duration,size -of compact coconut_cloud_reel.mp4
