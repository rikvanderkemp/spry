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

if [ "$1" = "start" ]
    then
        killTasks
        echo "Running SPRY on port 8000"
        python main.py & 

        jobs -p > run.lock
        echo "All tasks run in the background, press enter if you did not return to your cli"
elif [ "$1" = "stop" ]
    then
        killTasks
else
    echo "Please run with start|stop"
fi
