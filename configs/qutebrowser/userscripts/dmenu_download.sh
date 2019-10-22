#!/usr/bin/bash
#echo "open www.google.com" >> "$QUTE_FIFO"
DDIR="$(find $HOME -type d | rofi -dmenu -i -location 2 -width 100 -line-margin 1 -line-padding 1)"
echo "set downloads.location.prompt true" >> "$QUTE_FIFO"
echo "set downloads.location.suggestion filename" >> "$QUTE_FIFO"
echo "set downloads.location.directory $DDIR" >> "$QUTE_FIFO"
