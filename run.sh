#! /bin/bash

# [ TEMP=(uname -a) | grep microsoft - ];

(uname -a) | (grep --binary-files=text -q microsoft - 2>&1 >/dev/null)

if [ $? != 0 ]; then
    # val=0
    # while [  ];
    # do
    # done

    arecord -d 5 "recordings/Recording$1.wav"

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
