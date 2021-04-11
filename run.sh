#! /bin/bash

# [ TEMP=(uname -a) | grep microsoft - ];

(uname -a) | (grep --binary-files=text -q microsoft - 2>&1 >/dev/null)

if [ $? != 0 ]; then

    python3 ./redblue.py

    while [ true ];
    do
        rm "recordings/wak.wav"
        rm Wake.wav
        rm alex.wav

        val=1

        while [ $val != 0 ];
        do
        
        arecord -d 2 "recordings/wak.wav"
        ffmpeg -hide_banner -loglevel error -i "recordings/wak.wav" Wake.wav

        ./start
        val=$?
        
        # echo $val
        rm Wake.wav
        rm "recordings/wak.wav"
        
        done

        aplay alex.wav

        arecord -d 4 "recordings/Recording$1.wav"

        echo 'y' | ffmpeg -hide_banner -loglevel error -i "recordings/Recording$1.wav" Recording.wav

        ./main

        aplay response.wav
    done
else
    # for testing on windows
    mv ~/winhome/Documents/'Sound recordings'/Recording.m4a ~/winhome/Documents/'Sound recordings'/"Recording$1.m4a"

    cp ~/winhome/Documents/'Sound recordings'/Recording$1.m4a recordings/

    echo 'y' | ffmpeg -i "recordings/Recording$1.m4a" Recording.wav

    ./main

    explorer.exe response.wav

fi
