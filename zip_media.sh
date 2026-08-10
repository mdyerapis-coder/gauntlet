#!/bin/bash
# zip_media.sh — package the 35 generated gauntlet assets into gauntlet-media.zip
# Run this in the folder where Grok saved the files.
set -e
FILES="00.png 01.png 02.png 03.png 04.png 05.png 06.png 07.png 08.png 09.png 10.png \
11.png 12.png 13.png 14.png 15.png 16.png 17.png 18.png 19.png 20.png 21.png 22.png \
23.png 24.png 25.png 26.png 27.png 28.png 29.png 30.png \
intro.mp4 track1-2.mp4 track2-3.mp4 finale.mp4"
missing=""
for f in $FILES; do [ -f "$f" ] || missing="$missing $f"; done
if [ -n "$missing" ]; then echo "Missing:$missing"; echo "Aborting — generate those first."; exit 1; fi
zip -q gauntlet-media.zip $FILES
echo "Created gauntlet-media.zip with 35 files."
