#!/usr/bin/env bash

# To use:
#  - Append the lines below # CONTENT to '~/.bashrc' file.
#  - Then logout and re-login.  Or use 'source ~/.bashrc' to load the changes.
#
# One-time, non-persistent, use:
#  - Use 'source ./fzfcd.sh' for the shell session.

# TODO: Write a single __FIND_FZF__ that does not find hidden files unless the
# user wants to do so :). There are too many hidden files, and most of the time we
# don't need them in the result list.

__FIND_FZF__ () {
    find $HOME \
	 -type "$1" \
	 -not -path "*/.git/*" \
	 -not -path "*/Cache/*" \
	 -not -path "*/.log/*" \
	 -not -path "*/.wine/*" \
	 -not -path "*/Android/*" \
	 -not -path "*/.cache/*" \
	 -not -path "*/.local/*" \
	 -not -path "*/.cargo/*" \
	 -not -path "*/.npm/*" \
	 -not -path "*/.stack/*" \
	 -not -path "*/.myaur/*" \
	 -not -path "*/hie/*" \
	 -not -path "*/CacheStorage/*" \
	 -not -name .git |
	fzf -e
}

__FIND_FZFH__ () {
    find $HOME "$HOME/.*" \
	 -type "$1" \
	 -not -path "*/.git/*" \
	 -not -path "*/Cache/*" \
	 -not -path "*/.log/*" \
	 -not -path "*/.wine/*" \
	 -not -path "*/Android/*" \
	 -not -path "*/.cache/*" \
	 -not -path "*/.local/*" \
	 -not -path "*/.cargo/*" \
	 -not -path "*/.npm/*" \
	 -not -path "*/.stack/*" \
	 -not -path "*/.myaur/*" \
	 -not -path "*/hie/*" \
	 -not -path "*/CacheStorage/*" \
	 -not -name .git |
	fzf -e
}
#the -e flag above is required especially when find is used for
#finding hidden files.

alias _fzfcd='cd "$(__FIND_FZFH__ d )"'
alias fzfcd='cd "$(__FIND_FZF__ d)"'
alias _fzfind='cd "$(__FIND_FZFH__ f | sed 's,[^/]*$,,')"'
alias fzfind='cd "$(__FIND_FZF__ f | sed 's,[^/]*$,,')"'
