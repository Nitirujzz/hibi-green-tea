#!/bin/bash
# Hook 3s (B-roll whisk / coconut pour / cloud lands + key message) -> real pour (stabilized, 1.6x)
# -> B-roll wisps macro -> AI orbit + card -> end card
set -e
cd "$(dirname "$0")"
ENC="-c:v libx264 -pix_fmt yuv420p -r 30 -preset medium -crf 18 -c:a aac -b:a 160k -ar 48000 -ac 2"
cut(){ ffmpeg -v error -y -ss $2 -t $3 -i $1 -vf scale=1080:1920,setsar=1 $ENC $4; }
cut broll/b2.mp4 1.5 1.0 h1.mp4
cut broll/b1.mp4 1.0 1.0 h2.mp4
cut broll/b3.mp4 1.0 1.0 h3.mp4
printf "file 'h1.mp4'\nfile 'h2.mp4'\nfile 'h3.mp4'\n" > hl.txt
ffmpeg -v error -y -f concat -safe 0 -i hl.txt -c copy hcat.mp4
ffmpeg -v error -y -i hcat.mp4 -loop 1 -t 3 -i hook.png -filter_complex \
"[1]format=rgba,fade=in:st=0:d=0.15:alpha=1[o];[0:v][o]overlay=0:0:shortest=1[v]" -map "[v]" -map 0:a $ENC segH.mp4
SP=1.6
DR=$(python3 -c "print(19.7/$SP)")
ffmpeg -v error -y -i real/real_stab.mp4 -loop 1 -i oreal.png -filter_complex \
"[0:v]setpts=PTS/$SP,scale=1080:1920:flags=lanczos,setsar=1,eq=saturation=1.08:contrast=1.03[b];[1]format=rgba,fade=in:st=0.5:d=0.3:alpha=1[o];[b][o]overlay=0:0:shortest=1[v];[0:a]atempo=$SP,volume=8dB,afade=in:st=0:d=0.2[a]" \
-map "[v]" -map "[a]" -t $DR $ENC segR.mp4
cut broll/b3.mp4 2.5 1.2 segW.mp4
DB=$(ffprobe -v error -show_entries format=duration -of csv=p=0 clipB.mp4)
ffmpeg -v error -y -i clipB.mp4 -loop 1 -t $DB -i o3.png -filter_complex \
"[1]format=rgba,fade=in:st=0.4:d=0.35:alpha=1[a3];[0:v]scale=1080:1920,setsar=1[b];[b][a3]overlay=0:0:enable='gte(t,0.4)'[v]" \
-map "[v]" -map 0:a $ENC segB.mp4
ffmpeg -v error -y -sseof -0.1 -i clipB.mp4 -frames:v 1 -vf scale=1080:1920 lastB.png
ffmpeg -v error -y -loop 1 -t 2.5 -i lastB.png -loop 1 -t 2.5 -i end.png -f lavfi -t 2.5 -i anullsrc=r=48000:cl=stereo -filter_complex \
"[1]format=rgba,fade=in:st=0:d=0.35:alpha=1[e];[0:v]setsar=1[b];[b][e]overlay=0:0[v]" -map "[v]" -map 2:a $ENC -shortest segE.mp4
printf "file 'segH.mp4'\nfile 'segR.mp4'\nfile 'segW.mp4'\nfile 'segB.mp4'\nfile 'segE.mp4'\n" > list.txt
ffmpeg -v error -y -f concat -safe 0 -i list.txt $ENC -movflags +faststart coconut_cloud_reel.mp4
ffprobe -v error -show_entries format=duration,size -of compact coconut_cloud_reel.mp4
