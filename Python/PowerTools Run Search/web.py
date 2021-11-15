# We use the sys library to get the search word
from sys import argv as args

# We import webbrowser so that we can open the final page
from webbrowser import open_new_tab, get

# We have to open a new tab with the search query
# If there is no search query open a empty tab
get('windows-default').open_new_tab(f'https://duckduckgo.com/?q={" ".join(args[1:])}')

# Run pyinstaller web.py -F -i icon.ico --noconsole to compile
# This will create a web.exe file in the dist folder which you can copy to
# D:\Program Files\Python\Scripts
# Rename the file to q.exe