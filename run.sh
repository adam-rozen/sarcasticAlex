#! /bin/bash

TEMP=(uname -a) | grep microsoft -

if [ TEMP = '' ]; then

    echo 'y' | ffmpeg -i "recordings/Recording$1.wav" Recording.wav

    ./main

    aplay response.wav

else

    mv ~/winhome/Documents/'Sound recordings'/Recording.m4a ~/winhome/Documents/'Sound recordings'/"Recording$1.m4a"

    cp ~/winhome/Documents/'Sound recordings'/Recording$1.m4a recordings/

    echo 'y' | ffmpeg -i "recordings/Recording$1.m4a" Recording.wav

    ./main

    explorer.exe response.wav

fi
