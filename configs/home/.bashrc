#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
#PS1='[\u@\h \W]\$ '
#export PS1="\[\033[38;5;11m\][\u@\h\[$(tput sgr0)\]\[\033[38;5;15m\] \w\[$(tput sgr0)\]\[\033[38;5;11m\]]\\$\[$(tput sgr0)\] "
export PS1="\[\033[38;5;11m\]\u\\[\033[38;5;15m\] \W\\[\033[38;5;11m\] \\$\[$(tput sgr0)\] "
export PS2="\033[38;5;11m> \033[00m\]"
export VISUAL=nvim
export EDITOR=nvim

alias vim='nvim'

alias lockandhib='killall compton & i3lock -f -u -r 10 -s 5 & systemctl hibernate'
alias fixmyscreen='(sudo systemctl restart bumblebeed & wait) && intel-virtual-output && arandr'
alias strtmyscreen='intel-virtual-output && ~/Documents/miscconfs/xstuff/screen.sh && i3-msg restart && sleep 2 && i3-msg rename workspace 1 to 10 && i3-msg rename workspace 2 to 1'

#aliases to make my life easier
alias _nvim='vim ~/dotfiles/configs/nvim/init.vim'
alias _qute='vim ~/dotfiles/configs/qutebrowser/config.py'
alias _cdrang='cd ~/dotfiles/configs/ranger/'
alias _vim='vim ~/dotfiles/configs/home/.vimrc'
alias _cdc='cd ~/.config'
alias _cdd='cd ~/dotfiles'
alias _date='date +%Y-%m-%d'

alias bton='echo -e "power on" | bluetoothctl'
alias btjbl='echo -e "connect 04:FE:A1:22:95:97" | bluetoothctl'
alias btjbloff='echo -e "disconnect" | bluetoothctl'
alias btoff='echo -e "power off" | bluetoothctl'

alias screenkeysstart='screenkey --show-settings'
alias screenkeysstip='killall screenkey'
alias msl='/home/deniz/dotfiles/scripts/script_launcher.sh'
alias mcd='cd "$(find ~/* -type d | fzf --color -e)"'
alias mping='ping archlinux.org'

GPG_TTY=$(tty)
export GPG_TTY
export PATH=$PATH:/home/deniz/.local/bin

BASE16_SHELL="$HOME/.config/base16-shell/"
[ -n "$PS1" ] && \
    [ -s "$BASE16_SHELL/profile_helper.sh" ] && \
        eval "$("$BASE16_SHELL/profile_helper.sh")"
[ -f ~/.fzf.colors ] && source ~/.fzf.colors
