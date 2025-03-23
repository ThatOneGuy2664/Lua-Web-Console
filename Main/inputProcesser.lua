local lastInputString = nil -- last user input, nil or string

-- example to process user input
function processPlayerInput(input)
    print("Player input received: " .. input)
    lastInputString = input

    if lastInputString and type(lastInputString) == "string" then
        local func, err = load(lastInputString)
        if not func then
            customPrint("[crimson]Error in code: " .. err)
        else
            func()
        end
    end
        
    return input
end

-- example to wait for input via a coroutine function and respond accordingly (recommended)
local function waitForInput()
    lastInputString = nil
    while lastInputString == nil do
        coroutine.yield()
    end
end

customPrint("[chartreuse]Lua is running!")
