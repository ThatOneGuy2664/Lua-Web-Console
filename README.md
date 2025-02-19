# What is this?
This is a html script that uses Fengari to allow Lua to run in (and print to) a custom browser terminal. (Fengari's license is found in Fengari_License)

# What can it do?
Html allows Lua to call _G.customPrint() (or just customPrint()), which prints the string (passed as an argument) to the web console. The function allows CSS color formatting as well from Lua. I.e. "[red]RedText" will make "RedText" red in the web console. Lua can run in the background with little memory use. Run main.py to auto-open an HTTP server with the html file.
