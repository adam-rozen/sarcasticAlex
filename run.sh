#! /bin/bash

# [ TEMP=(uname -a) | grep microsoft - ];

(uname -a) | (grep --binary-files=text -q microsoft - 2>&1 >/dev/null)

if [ $? != 0 ]; then
    
    val=1

    while [ $val != 0 ];
    do
    
    arecord -d 2 "recordings/Wake.wav"
    echo 'yy' | ffmpeg -hide_banner -loglevel error -i "recordings/Wake.wav" Wake.wav

    ./start
    val=$?
    echo $val
    done

    echo "ALEX:"

    arecord -d 4 "recordings/Recording$1.wav"

    echo 'y' | ffmpeg -i "recordings/Recording$1.wav" Recording.wav

    ./main

    aplay response.wav

else
    # for testing on windows
    mv ~/winhome/Documents/'Sound recordings'/Recording.m4a ~/winhome/Documents/'Sound recordings'/"Recording$1.m4a"

    cp ~/winhome/Documents/'Sound recordings'/Recording$1.m4a recordings/

    echo 'y' | ffmpeg -i "recordings/Recording$1.m4a" Recording.wav

    ./main

    explorer.exe response.wav

fi
