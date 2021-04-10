#! /bin/bash

# ls ~/winhome/Documents/'Sound recordings'/"Recording.m4a" 


mv ~/winhome/Documents/'Sound recordings'/Recording.m4a ~/winhome/Documents/'Sound recordings'/"Recording$1.m4a"

cp ~/winhome/Documents/'Sound recordings'/Recording$1.m4a recordings/

echo 'y' | ffmpeg -i "recordings/Recording$1.m4a" Recording.wav

./main

explorer.exe response.wav