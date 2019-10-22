#!/usr/bin/bash

echo "set downloads.location.directory ~" >> "$QUTE_FIFO"
echo "set downloads.location.prompt true" >> "$QUTE_FIFO"
echo "set downloads.location.suggestion both" >> "$QUTE_FIFO"
