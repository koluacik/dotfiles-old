" coc.nvim 

" use <c-space>for trigger completion
inoremap <silent><expr> <c-space> coc#refresh()

inoremap <expr> <Tab> pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"

inoremap <expr> <cr> pumvisible() ? "\<C-y>" : "\<C-g>u\<CR>"
inoremap <silent><expr> <cr> pumvisible() ? coc#_select_confirm() : "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"

set signcolumn=yes

" Better display for messages
set cmdheight=2
"
" " You will have bad experience for diagnostic messages when it's default
" 4000.
set updatetime=300
"
" " don't give |ins-completion-menu| messages.
set shortmess+=c

"to go back and forth between unsaved buffers
set hidden

"looks fancy
set guicursor=

"saner splitting
set splitbelow
set splitright

"to confuse normal and functional individuals
set nu relativenumber

"to un-confuse normal and functional individuals
set mouse=a

"load goodies
call plug#begin('~/.local/share/nvim/plugged')
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'chriskempson/base16-vim'
call plug#end()

"nobody wants a terminal with line numbers 
au TermOpen * startinsert|setlocal nonumber norelativenumber signcolumn=no
"use instead of the "terminal command
command Newterm split +terminal

"default <leader> key is \. use these to copy to or paste from the clipboard.
"use \\ to yank from or to the system clipboard, \\yy etc.
noremap <leader><leader> "+

"yank the file to the clipboard
noremap <leader>yy :%y+<CR>

"latex
"\lb to build a latex file. (uses CoC and its tex extension)
noremap <leader>ll :CocCommand latex.Build <CR>
noremap <leader>lwl :w <bar> :CocCommand latex.Build <CR>
"\lz to display the already built pdf file in zathura
noremap <silent><leader>lz :! zathura %:r.pdf & <CR>

"no highlighting
noremap <silent><leader>] :noh <CR>

"ctrl \ ctrl n is a hassle
tnoremap <Esc> <C-\><C-n>

":e $MYVIMRC is a hassle
command Evimrc edit $MYVIMRC


"that's all folks!
