#!/bin/bash

# Set Session Name
SESSION="c_n_b"
SESSIONEXISTS=$(tmux list-sessions | grep $SESSION)
docker_mysql_dev1='docker exec -it some-mysql mysql -h192.168.1.17 -uroot -pxthk123456 --auto-rehash'

# Only create tmux session if it doesn't already exist
if [ "$SESSIONEXISTS" = "" ]
then
    # Start New Session with our name
    tmux new-session -d -s $SESSION

    # Name first Pane and start zsh
    # tmux rename-window -t 0 'Main'
    tmux send-keys -t 0 C-m 'clear' C-m

    # Create and setup pane for hugo server
    tmux new-window -t $SESSION:1 -n 'database'
    tmux send-keys -t 'database' C-m "$docker_mysql_dev1" C-m
    tmux splitw -v -p 50


    # setup Writing window
    tmux new-window -t $SESSION:2 -n 'work_dir'
    tmux send-keys -t 'work_dir' C-m 'cd ~/code/; clear' C-m
    tmux splitw -v -p 50

    # Setup an additional shell
    tmux new-window -t $SESSION:3
    # tmux send-keys -t 'Shell' "zsh" C-m
fi

# Attach Session, on the Main window
tmux attach-session -t $SESSION:2
