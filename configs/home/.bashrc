#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

export PS1="\[\033[38;5;1m\]\u\[$(tput bold)\]\[$(tput sgr0)\]\[\033[38;5;15m\] \[$(tput sgr0)\]\W \[$(tput sgr0)\]\[\033[38;5;1m\]\\$\[$(tput sgr0)\]\[\033[38;5;15m\] \[$(tput sgr0)\]"
export PS2="\033[38;5;11m> \033[00m\]"

for file in ~/.bash/*.sh
do
	source $file
done

#source ~/.bash/fzfcd.sh
#source ~/.bash/aliases.sh
#source ~/.bash/*.sh

export VISUAL=nvim
export EDITOR=nvim
export BROWSER=qutebrowser
export WINIT_X11_SCALE_FACTOR=1.0

GPG_TTY=$(tty)
export GPG_TTY
export PATH=$PATH:/home/deniz/.local/bin:/home/deniz/.cabal/bin

# for stack auto-complete

eval "$(stack --bash-completion-script stack)"

set -o vi

#avoid nested rangers
ranger() {
    if [ -z "$RANGER_LEVEL" ]; then
        /usr/bin/ranger "$@"
    else 
        exit
    fi
}

