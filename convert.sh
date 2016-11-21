#!/bin/bash
echo "$1"
ffmpeg -i "$1" -f mp3 -y "$1.mp3" > /dev/null 2>&1
# comment
