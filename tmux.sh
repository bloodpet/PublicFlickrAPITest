#!/bin/sh
cd $(dirname $0)
name=$(basename $(pwd))
tmux new -s "$name" \; split-window -h -t "$name" || \
tmux attach -t "$name"
