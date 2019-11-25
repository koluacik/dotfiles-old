#!/usr/bin/env bash

#aliases to make my life easier
alias _nvim='vim ~/dotfiles/configs/nvim/init.vim'
alias _qute='vim ~/dotfiles/configs/qutebrowser/config.py'
alias _cdrang='cd ~/dotfiles/configs/ranger/'
alias _vim='vim ~/dotfiles/configs/home/.vimrc'
alias _cdc='cd ~/.config'
alias _cdd='cd ~/dotfiles'
alias _date='date +%Y-%m-%d'

alias btw='sudo pacman -Syu'

alias bton='echo -e "power on" | bluetoothctl'
alias btjbl='echo -e "connect 04:FE:A1:22:95:97" | bluetoothctl'
alias btjbloff='echo -e "disconnect" | bluetoothctl'
alias btoff='echo -e "power off" | bluetoothctl'

alias screenkeysstart='screenkey --show-settings'
alias screenkeysstip='killall screenkey'
alias msl='/home/deniz/dotfiles/scripts/script_launcher.sh'
#alias mcd='cd "$(find ~/* -type d | fzf --color -e)"'
alias mping='ping archlinux.org'

alias cal='cal -m'
alias ls='ls --color=auto'
alias vim='nvim'

alias lockandhib='killall compton & i3lock -f -u -r 10 -s 5 & systemctl hibernate'

alias socks='ssh -N -f cengsocks'
alias nosocks='pkill ssh'
