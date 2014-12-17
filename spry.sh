#!/bin/bash

function killTasks() {
    if [ -f run.lock ]
        then
            echo "Killing previous background tasks"
            while read line
            do
                kill $line
            done < run.lock
    fi
}

function runAll() {
    echo "Running SPRY on port 8000"
    python main.py & 
    jobs -p > run.lock
}

if [ "$1" = "start" ]
    then
        killTasks
        runAll
        echo "All tasks run in the background, press enter if you did not return to your cli"
elif [ "$1" = "stop" ]
    then
        killTasks
        rm run.lock
elif [ "$1" = "build" ]
    then
        if [ ! -f run.lock ];
            then
                runAll
        fi

        FILES=./web/templates/*

        if [ -d build ]
            then
                rm -Rf build
        fi

        mkdir build

        cp -Rf web/static build

        for f in $FILES
        do
            if [ -f $f ];
                then
                  echo "Processing $f file..."
                  wget  "http://localhost:8000/$(basename $f)" -O ./build/$(basename $f)
            fi
        done

        echo "Build complete."
else
    echo "Please run with start|stop"
fi
