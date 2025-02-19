local lastInputString = nil -- last user input, nil or string

function processPlayerInput(input)
    print("Player input received: " .. input)
    lastInputString = input

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
