#!/bin/bash
# compute destination file name and show
out=$(echo ${1} | sed 's/\.m4a/\.mp3/')
echo "$1 -> $out"
# transcode
ffmpeg -i "$1" -f mp3 -y "$out" > /dev/null 2>&1
