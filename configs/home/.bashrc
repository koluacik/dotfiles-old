#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

export PS1="\[\033[38;5;11m\]\u\\[\033[38;5;15m\] \W\\[\033[38;5;11m\] \\$\[$(tput sgr0)\] "
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

GPG_TTY=$(tty)
export GPG_TTY
export PATH=$PATH:/home/deniz/.local/bin

#BASE16_SHELL="$HOME/.config/base16-shell/"
#[ -n "$PS1" ] && \
#    [ -s "$BASE16_SHELL/profile_helper.sh" ] && \
#        eval "$("$BASE16_SHELL/profile_helper.sh")"
#[ -f ~/.fzf.colors ] && source ~/.fzf.colors
