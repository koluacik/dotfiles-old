#!/usr/bin/bash

DIR=~/.myaur #location of your AUR repositories, this directory should consist of AUR repository clone directories and nothing else.

DATE="$(date +%Y%m%d_%H%M%S)"
LOG="$HOME/aur_update$DATE.log"
UPTODATE="Already up to date."
NO_REPOS=$(ls | wc -l)
NEW=0

cd $DIR

echo "Log for the AURate script." >> $LOG
echo "$NO_REPOS repositories to be checked." >> $LOG
echo >> $LOG
echo "Updated repositories:" >> $LOG

for REPO in $(ls)
do
	cd $REPO
	echo $REPO
	if [ "$(git pull)" != "$UPTODATE" ]
	then
		((NEW+=1))
		echo "-$REPO" >> $LOG
	fi
	cd ..
done

echo "$NEW repositories updated." 




	


