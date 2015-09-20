find . -name '*.mp4' -exec ffprobe -v quiet -of csv=p=0 -show_entries format=duration {} \; | paste -sd+ -| bc
