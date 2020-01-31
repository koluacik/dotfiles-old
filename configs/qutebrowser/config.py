# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# Aliases for commands. The keys of the given dictionary are the
# aliases, while the values are the commands they map to.
# Type: Dict
c.aliases = {'w': 'session-save', 'q': 'quit', 'wq': 'quit --save'}

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value.
# Type: FormatString
c.content.headers.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://accounts.google.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://docs.google.com/*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'chrome-devtools://*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'file://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome-devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# Editor (and arguments) to use for the `open-editor` command. The
# following placeholders are defined:  * `{file}`: Filename of the file
# to be edited. * `{line}`: Line in which the caret is found in the
# text. * `{column}`: Column in which the caret is found in the text. *
# `{line0}`: Same as `{line}`, but starting from index 0. * `{column0}`:
# Same as `{column}`, but starting from index 0.
# Type: ShellCommand
c.editor.command = ['alacritty', '-e', 'nvim', '-f', '{file}', '-c', 'normal {line}G{column0}l']

# Position of the tab bar.
# Type: Position
# Valid values:
#   - top
#   - bottom
#   - left
#   - right
c.tabs.position = 'top'

# When to show the tab bar.
# Type: String
# Valid values:
#   - always: Always show the tab bar.
#   - never: Always hide the tab bar.
#   - multiple: Hide the tab bar if only one tab is open.
#   - switching: Show the tab bar when switching tabs.
c.tabs.show = 'multiple'

# Duration (in milliseconds) to show the tab bar before hiding it when
# tabs.show is set to 'switching'.
# Type: Int
c.tabs.show_switching_delay = 800

# Open a new window for every tab.
# Type: Bool
c.tabs.tabs_are_windows = False

# Search engines which can be used via the address bar. Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` signs. The search engine named
# `DEFAULT` is used when `url.auto_search` is turned on and something
# else than a URL was entered to be opened. Other search engines can be
# used by prepending the search engine name to the search term, e.g.
# `:open google qutebrowser`.
# Type: Dict
c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}', 'aw': 'https://wiki.archlinux.org/?search={}', 'yt': 'https://www.youtube.com/results?search_query={}', 'yd': 'https://duckduckgo.com/?q={}&iar=videos&iax=videos&ia=videos', '4': 'https://4chan.org/{}', '8': 'https://8ch.net/{}', 'enwk': 'https://en.wikipedia.org/?search={}', 'trwk': 'https://tr.wikipedia.org/?search={}', 'aur': 'https://aur.archlinux.org/packages/?O=0&K={}', 'img': 'https://duckduckgo.com/?q={}&iar=images&iax=images&ia=images', 'reddt': 'https://www.reddit.com/r/{}', 'yemekad': 'http://kafeterya.metu.edu.tr/tarih/{}', 'aps': 'https://www.archlinux.org/packages/?q={}', 'dict': 'https://www.dictionary.com/browse/{}', 'thes': 'https://www.thesaurus.com/browse/{}', 'abb': 'https://www.abbreviations.com/{}', 'enwd': 'https://en.wiktionary.org/wiki/{}', 'trwd': 'https://tr.wiktionary.org/wiki/{}', 'imdb': 'https://www.imdb.com/find?q={}'}

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
# Type: List of QtColor, or QtColor
c.colors.completion.fg = '#FFCB6B'

# Background color of the completion widget for odd rows.
# Type: QssColor
c.colors.completion.odd.bg = '#444267'

# Background color of the completion widget for even rows.
# Type: QssColor
c.colors.completion.even.bg = '#292D3E'

# Foreground color of completion widget category headers.
# Type: QtColor
c.colors.completion.category.fg = '#C3E88D'

# Background color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.bg = '#292D3E'

# Top border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.top = '#292D3E'

# Bottom border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.bottom = '#292D3E'

# Foreground color of the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.fg = '#444267'

# Background color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.bg = '#FFCB6B'

# Top border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.top = '#FFCB6B'

# Bottom border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.bottom = '#FFCB6B'

# Foreground color of the matched text in the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.match.fg = '#F07178'

# Foreground color of the matched text in the completion.
# Type: QtColor
c.colors.completion.match.fg = '#C3E88D'

# Color of the scrollbar handle in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.fg = '#959DCB'

# Color of the scrollbar in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.bg = '#292D3E'

# Background color for the download bar.
# Type: QssColor
c.colors.downloads.bar.bg = '#292D3E'

# Color gradient start for download text.
# Type: QtColor
c.colors.downloads.start.fg = '#292D3E'

# Color gradient start for download backgrounds.
# Type: QtColor
c.colors.downloads.start.bg = '#FFCB6B'

# Color gradient end for download text.
# Type: QtColor
c.colors.downloads.stop.fg = '#292D3E'

# Color gradient stop for download backgrounds.
# Type: QtColor
c.colors.downloads.stop.bg = '#C3E88D'

# Foreground color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.fg = '#292D3E'

# Font color for hints.
# Type: QssColor
c.colors.hints.fg = '#292D3E'

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
# Type: QssColor
c.colors.hints.bg = '#FFCB6B'

# Font color for the matched part of hints.
# Type: QtColor
c.colors.hints.match.fg = '#959DCB'

# Text color for the keyhint widget.
# Type: QssColor
c.colors.keyhint.fg = '#959DCB'

# Highlight color for keys to complete the current keychain.
# Type: QssColor
c.colors.keyhint.suffix.fg = '#959DCB'

# Background color of the keyhint widget.
# Type: QssColor
c.colors.keyhint.bg = '#292D3E'

# Foreground color of an error message.
# Type: QssColor
c.colors.messages.error.fg = '#292D3E'

# Background color of an error message.
# Type: QssColor
c.colors.messages.error.bg = '#F07178'

# Border color of an error message.
# Type: QssColor
c.colors.messages.error.border = '#F07178'

# Foreground color of a warning message.
# Type: QssColor
c.colors.messages.warning.fg = '#292D3E'

# Background color of a warning message.
# Type: QssColor
c.colors.messages.warning.bg = '#C792EA'

# Border color of a warning message.
# Type: QssColor
c.colors.messages.warning.border = '#C792EA'

# Foreground color of an info message.
# Type: QssColor
c.colors.messages.info.fg = '#959DCB'

# Background color of an info message.
# Type: QssColor
c.colors.messages.info.bg = '#292D3E'

# Border color of an info message.
# Type: QssColor
c.colors.messages.info.border = '#292D3E'

# Foreground color for prompts.
# Type: QssColor
c.colors.prompts.fg = '#959DCB'

# Border used around UI elements in prompts.
# Type: String
c.colors.prompts.border = '#292D3E'

# Background color for prompts.
# Type: QssColor
c.colors.prompts.bg = '#292D3E'

# Background color for the selected item in filename prompts.
# Type: QssColor
c.colors.prompts.selected.bg = '#FFCB6B'

# Foreground color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.fg = '#C3E88D'

# Background color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.bg = '#292D3E'

# Foreground color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.fg = '#292D3E'

# Background color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.bg = '#82AAFF'

# Foreground color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.fg = '#292D3E'

# Background color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.bg = '#89DDFF'

# Foreground color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.fg = '#292D3E'

# Background color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.bg = '#676E95'

# Foreground color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.fg = '#959DCB'

# Background color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.bg = '#292D3E'

# Foreground color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.fg = '#959DCB'

# Background color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.bg = '#292D3E'

# Foreground color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.fg = '#292D3E'

# Background color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.bg = '#C792EA'

# Foreground color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.fg = '#292D3E'

# Background color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.bg = '#82AAFF'

# Background color of the progress bar.
# Type: QssColor
c.colors.statusbar.progress.bg = '#82AAFF'

# Default foreground color of the URL in the statusbar.
# Type: QssColor
c.colors.statusbar.url.fg = '#959DCB'

# Foreground color of the URL in the statusbar on error.
# Type: QssColor
c.colors.statusbar.url.error.fg = '#F07178'

# Foreground color of the URL in the statusbar for hovered links.
# Type: QssColor
c.colors.statusbar.url.hover.fg = '#959DCB'

# Foreground color of the URL in the statusbar on successful load
# (http).
# Type: QssColor
c.colors.statusbar.url.success.http.fg = '#89DDFF'

# Foreground color of the URL in the statusbar on successful load
# (https).
# Type: QssColor
c.colors.statusbar.url.success.https.fg = '#C3E88D'

# Foreground color of the URL in the statusbar when there's a warning.
# Type: QssColor
c.colors.statusbar.url.warn.fg = '#C792EA'

# Background color of the tab bar.
# Type: QssColor
c.colors.tabs.bar.bg = '#292D3E'

# Color gradient start for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.start = '#82AAFF'

# Color gradient end for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.stop = '#89DDFF'

# Color for the tab indicator on errors.
# Type: QtColor
c.colors.tabs.indicator.error = '#F07178'

# Foreground color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.fg = '#292D3E'

# Background color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.bg = '#959DCB'

# Foreground color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.fg = '#292D3E'

# Background color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.bg = '#959DCB'

# Foreground color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.fg = '#959DCB'

# Background color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.bg = '#292D3E'

# Foreground color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.fg = '#959DCB'

# Background color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.bg = '#292D3E'

# Foreground color of pinned unselected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.odd.fg = '#292D3E'

# Background color of pinned unselected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.odd.bg = '#959DCB'

# Foreground color of pinned unselected even tabs.
# Type: QtColor
c.colors.tabs.pinned.even.fg = '#292D3E'

# Background color of pinned unselected even tabs.
# Type: QtColor
c.colors.tabs.pinned.even.bg = '#959DCB'

# Foreground color of pinned selected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.odd.fg = '#959DCB'

# Background color of pinned selected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.odd.bg = '#292D3E'

# Foreground color of pinned selected even tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.even.fg = '#959DCB'

# Background color of pinned selected even tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.even.bg = '#292D3E'

# Default monospace fonts. Whenever "monospace" is used in a font
# setting, it's replaced with the fonts listed here.
# Type: Font
c.fonts.monospace = '"Iosevka SS08", Monospace, "DejaVu Sans Mono", Monaco, "Bitstream Vera Sans Mono", "Andale Mono", "Courier New", Courier, "Liberation Mono", monospace, Fixed, Consolas, Terminal'

# Font used in the completion widget.
# Type: Font
c.fonts.completion.entry = '10pt Iosevka SS08'

# Font used in the completion categories.
# Type: Font
c.fonts.completion.category = 'bold 10pt Iosevka SS08'

# Font used for the debugging console.
# Type: QtFont
c.fonts.debug_console = '10pt Iosevka SS08'

# Font used for the downloadbar.
# Type: Font
c.fonts.downloads = '10pt Iosevka SS08'

# Font used for the hints.
# Type: Font
c.fonts.hints = 'bold 10pt Iosevka SS08'

# Font used in the keyhint widget.
# Type: Font
c.fonts.keyhint = '10pt Iosevka SS08'

# Font used for error messages.
# Type: Font
c.fonts.messages.error = '10pt Iosevka SS08'

# Font used for info messages.
# Type: Font
c.fonts.messages.info = '10pt Iosevka SS08'

# Font used for warning messages.
# Type: Font
c.fonts.messages.warning = '10pt Iosevka SS08'

# Font used for prompts.
# Type: Font
c.fonts.prompts = '10pt Iosevka SS08'

# Font used in the statusbar.
# Type: Font
c.fonts.statusbar = '10pt Iosevka SS08'

# Font used in the tab bar.
# Type: QtFont
c.fonts.tabs = '10pt Iosevka SS08'

# Font family for cursive fonts.
# Type: FontFamily
c.fonts.web.family.cursive = None

# Bindings for normal mode
config.bind(';;y', 'hint all spawn --user watch.sh')
config.bind('<Ctrl+Shift+d>', 'open qute://bookmarks')
config.bind('\\ddd', 'spawn --user dmenu_download.sh')
config.bind('\\ddf', 'spawn --user prompt_download.sh')
config.bind('\\ddg', 'spawn --user dmenu_download_no_name.sh')
config.bind('\\po', 'set content.proxy socks://localhost:9090')
config.bind('\\pp', 'set content.proxy system')
config.bind('\\y', 'spawn --user watch.sh')

# Bindings for command mode
config.bind('<Ctrl+Shift+e>', 'edit-command', mode='command')

# base16-qutebrowser (https://github.com/theova/base16-qutebrowser)
# Base16 qutebrowser template by theova and Daniel Mulford
# Dracula scheme by Mike Barkmin (http://github.com/mikebarkmin) based on Dracula Theme (http://github.com/dracula)

base00 = "#282936"
base01 = "#3a3c4e"
base02 = "#4d4f68"
base03 = "#626483"
base04 = "#62d6e8"
base05 = "#e9e9f4"
base06 = "#f1f2f8"
base07 = "#f7f7fb"
base08 = "#ea51b2"
base09 = "#b45bcf"
base0A = "#00f769"
base0B = "#ebff87"
base0C = "#a1efe4"
base0D = "#62d6e8"
base0E = "#b45bcf"
base0F = "#00f769"

# set qutebrowser colors

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
c.colors.completion.fg = base05

# Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = base00

# Background color of the completion widget for even rows.
c.colors.completion.even.bg = base00

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = base0D

# Background color of the completion widget category headers.
c.colors.completion.category.bg = base00

# Top border color of the completion widget category headers.
c.colors.completion.category.border.top = base00

# Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = base00

# Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = base00

# Background color of the selected completion item.
c.colors.completion.item.selected.bg = base0D

# Top border color of the selected completion item
c.colors.completion.item.selected.border.top = base0D

# Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = base0D

# Foreground color of the matched text in the selected completion item.
c.colors.completion.item.selected.match.fg = base00

# Foreground color of the matched text in the completion.
c.colors.completion.match.fg = base09

# Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = base05

# Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = base00

# Background color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.bg = base00

# Foreground color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.fg =  base05

# Background color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.bg = base0D

#Foreground color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.fg = base00

# Background color for the download bar.
c.colors.downloads.bar.bg = base00

# Color gradient start for download text.
c.colors.downloads.start.fg = base00

# Color gradient start for download backgrounds.
c.colors.downloads.start.bg = base0D

# Color gradient end for download text.
c.colors.downloads.stop.fg = base00

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = base0C

# Foreground color for downloads with errors.
c.colors.downloads.error.fg = base08

# Font color for hints.
c.colors.hints.fg = base00

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
c.colors.hints.bg = base0A

# Font color for the matched part of hints.
c.colors.hints.match.fg = base05

# Text color for the keyhint widget.
c.colors.keyhint.fg = base05

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = base05

# Background color of the keyhint widget.
c.colors.keyhint.bg = base00

# Foreground color of an error message.
c.colors.messages.error.fg = base00

# Background color of an error message.
c.colors.messages.error.bg = base08

# Border color of an error message.
c.colors.messages.error.border = base08

# Foreground color of a warning message.
c.colors.messages.warning.fg = base00

# Background color of a warning message.
c.colors.messages.warning.bg = base0E

# Border color of a warning message.
c.colors.messages.warning.border = base0E

# Foreground color of an info message.
c.colors.messages.info.fg = base05

# Background color of an info message.
c.colors.messages.info.bg = base00

# Border color of an info message.
c.colors.messages.info.border = base00

# Foreground color for prompts.
c.colors.prompts.fg = base05

# Border used around UI elements in prompts.
c.colors.prompts.border = base00

# Background color for prompts.
c.colors.prompts.bg = base00

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = base0A

# Foreground color of the statusbar.
c.colors.statusbar.normal.fg = base05

# Background color of the statusbar.
c.colors.statusbar.normal.bg = base00

# Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = base0C

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = base00

# Foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = base0A

# Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = base00

# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = base0E

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = base00

# Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = base04

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = base01

# Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = base0E

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = base01

# Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = base0D

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = base00

# Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = base0D

# Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = base00

# Background color of the progress bar.
c.colors.statusbar.progress.bg = base0D

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = base05

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = base08

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = base09

# Foreground color of the URL in the statusbar on successful load
# (http).
c.colors.statusbar.url.success.http.fg = base0B

# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = base0B

# Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = base0E

# Background color of the tab bar.
c.colors.tabs.bar.bg = base00

# Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = base0D

# Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = base0C

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = base08

# Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = base05

# Background color of unselected odd tabs.
c.colors.tabs.odd.bg = base00

# Foreground color of unselected even tabs.
c.colors.tabs.even.fg = base05

# Background color of unselected even tabs.
c.colors.tabs.even.bg = base00

# Background color of pinned unselected even tabs.
c.colors.tabs.pinned.even.bg = base0B

# Foreground color of pinned unselected even tabs.
c.colors.tabs.pinned.even.fg = base00

# Background color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.bg = base0B

# Foreground color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.fg = base00

# Background color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.bg = base0D

# Foreground color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.fg = base00

# Background color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.bg = base0D

# Foreground color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.fg = base00

# Foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = base0B

# Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = base00

# Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = base0B

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = base00

# Background color for webpages if unset (or empty to use the theme's
# color).
c.colors.webpage.bg = base00
