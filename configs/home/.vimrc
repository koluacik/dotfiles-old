" An example for a vimrc file.
"
" Maintainer:	Bram Moolenaar <Bram@vim.org>
" Last change:	2017 Sep 20
"
" To use it, copy it to
"     for Unix and OS/2:  ~/.vimrc
"	      for Amiga:  s:.vimrc
"  for MS-DOS and Win32:  $VIM\_vimrc
"	    for OpenVMS:  sys$login:.vimrc

" When started as "evim", evim.vim will already have done these settings.
if v:progname =~? "evim"
  finish
endif

" Get the defaults that most users want.
source $VIMRUNTIME/defaults.vim

if has("vms")
  set nobackup		" do not keep a backup file, use versions instead
else
  set backup		" keep a backup file (restore to previous version)
  if has('persistent_undo')
    set undofile	" keep an undo file (undo changes after closing)
  endif
endif

if &t_Co > 2 || has("gui_running")
  " Switch on highlighting the last used search pattern.
  set hlsearch
endif

" Only do this part when compiled with support for autocommands.
if has("autocmd")

  " Put these in an autocmd group, so that we can delete them easily.
  augroup vimrcEx
  au!

  " For all text files set 'textwidth' to 78 characters.
  autocmd FileType text setlocal textwidth=78

  augroup END

else

  set autoindent		" always set autoindenting on

endif " has("autocmd")

" Add optional packages.
"
" The matchit plugin makes the % command work better, but it is not backwards
" compatible.
" The ! means the package won't be loaded right away but when plugins are
" loaded during initialization.
if has('syntax') && has('eval')
  packadd! matchit
endif

set nu relativenumber
set cmdheight=2

hi Search cterm=NONE ctermfg=2 ctermbg=7
hi IncSearch cterm=bold,underline ctermfg=233 ctermbg=7

hi TabLineSel ctermfg=0 ctermbg=7 cterm=None
hi TabLineFill ctermfg=0 ctermbg=7 
hi tabLine ctermbg=0 cterm=NONE

hi LineNr ctermfg=7 cterm=NONE
hi CursorLineNr ctermbg=0 ctermfg=7 cterm=bold
hi VertSplit ctermfg=0 ctermbg=7


hi StatusLineTermNC ctermbg=0 ctermfg=8
hi StatusLineTerm ctermbg=7 ctermfg=0 cterm=NONE

hi StatusLineNC ctermbg=8 ctermfg=0
hi StatusLine ctermbg=0 ctermfg=7

"to make matchingparen highlighting more readable
hi MatchParen ctermfg=0 ctermbg=1

"python: make def return or etc bold and white
"hi pythonConditional cterm=bold ctermfg=7
hi Statement ctermfg=7 cterm=bold
hi cType cterm=bold ctermfg=4


set splitbelow
set splitright

set ignorecase
set smartcase

call plug#begin('~/.vim/plugged/')

Plug 'powerline/powerline'

call plug#end()

"netrw"
let g:netrw_liststyle=3
let g:netrw_browse_split=2
let g:netrw_winsize=25
let g:netrw_banner=0 

set cb=unnamedplus
set hidden

