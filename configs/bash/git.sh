#!/usr/bin/env bash

function mygcp()
{
	git commit -a -m "$*"
	if [[ $(git config --local -l | grep "remote") ]]
	then
		git push
	fi
}
