# Allan John Valiente
# 101285226
# COMP 2152 – Assignment 1

import random
from pip._vendor.distlib.compat import raw_input

themeName = input("Enter a theme: ")
listItem = []
isExit = False
print("Please enter " + themeName + " or \ntype \"exit\" to end entering an items: ")
while not isExit:
    userInput = input("- ")
    if userInput.lower() == "exit":
        isExit = True
    elif userInput not in listItem:
        listItem.append(userInput)
cnt = len(listItem)
ranNum = random.randint(0, cnt - 1)
print("The list is", listItem)
print("The index number generated at random is", ranNum)
print("List item with an index of " + str(ranNum) + " is " + listItem[ranNum])
charInput = ''
while len(charInput) != 1:
    charInput = raw_input('Please enter character to search: ')
checkInputExists = charInput.lower() in listItem[ranNum] or charInput.upper() in listItem[ranNum]
if checkInputExists:
    print("Character \'{0}\' or \'{1}\' is found in \"{2}\"".format(charInput.lower(), charInput.upper(),
                                                                    listItem[ranNum]))
else:
    print("Character \'{0}\' or \'{1}\' is not found in \"{2}\"".format(charInput.lower(), charInput.upper(),
                                                                        listItem[ranNum]))
