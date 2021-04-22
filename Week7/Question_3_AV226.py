userInput = ""
isExit = False
while not isExit:
    userInput = input('Enter some input or type \"quit\", \"stop\", or \"exit\" to end the program: ')
    print(userInput.upper())
    if userInput == "quit" or userInput == "stop" or userInput == "exit":
        isExit = True
