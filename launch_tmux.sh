#!/bin/bash
# Use -d to allow the rest of the function to run
SessionName="auto_hd"
tmux new-session -d -s $SessionName ; set-option -g default-shell /bin/bash
# -d to prevent current window from changing
tmux splitw -v 
tmux selectp -t 0
tmux send-keys -t 0 "bash /home/lihongde/scripts/shadowsocks.sh" Enter
tmux new-window -d -n 1 bash /home/lihongde/scripts/login_mysql.sh
tmux new-window -d -n 2 -c /data/htdocs/server
tmux new-window -d -n 3
# -d to detach any other client (which there shouldn't be,
# since you just created the session).
tmux attach-session -d -t $SessionName:2
