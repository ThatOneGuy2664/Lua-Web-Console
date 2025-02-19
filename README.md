# What is this?
This is a html script that uses Fengari to allow Lua to run in (and print to) a custom browser terminal. (Fengari's license is found in Fengari_License) Open main.py (Requires Python on your device) to automatically open an HTTP server in the file's current directory, ensure the html script AND Fengari are in the directory as well. This is made more as a framework for others to work off of, and it's recommended you understand what you're doing whenever you change anything with it. If you don't need local file access, simply ensure Fengari-web.js is in the same directory as the html script and open the script in your browser of choice. The code is commented, but it's recommended for you to be at least familar with html and Lua before changing things.

# What can it do?
Html allows Lua to call _G.customPrint() (or just customPrint()), which prints the string (passed as an argument) to the web console. The function allows CSS color formatting as well from Lua. I.e. "[red]RedText" will make "RedText" red in the web console. Lua can run in the background with little memory use. Run main.py to auto-open an HTTP server with the html file.

Test it out (here)[https://thatoneguy2664.github.io/Lua-Web-Console/Main/luaConsole.html]!
