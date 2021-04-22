print("\nTask 6")
# Create Number Guessing Game
# upon running script
    # Get a random number (user random module)

# ask user to guess number until they "quit" or "exit" (case in-sensitive)
# store the incorrect guesses

# if guess is "close" (define close as +/- 3)
    # give message saying "getting warmer"
# if not "close"
    # give message saying "not close"
# after 5 amount of incorrect guesses
    # give a SUPER EASY hint (your choice)
        # I.E. "twice the value of this number is ______"
# when they have guessed number
    # give congrats message
        # display all incorrect guess
        # tell them how many guesses it took to get correct

import random

def guessChecker(n, rN) -> bool:
    chk = (rN >= n >= (rN - 3)) or ((rN + 3) >= n >= rN)
    return chk

guessList = []
isContinue = True
ranNum = random.randint(1, 100);
print(ranNum)
counter = 0;
while isContinue :
    guessNum = int(input("Guess the number: "))
    counter += 1
    if guessNum == ranNum:
        print("Congratulation!, you guess the number")
        inputsGuess = ', '.join(guessList);
        print("Incorrect Guess: ", inputsGuess)
        print("You took", counter, "times before you guess the right number")
        isContinue = False
        break
    if guessChecker(guessNum, ranNum):
        print("getting warmer")
    else:
        print("not close")

    if counter == 5:
        if ranNum < guessNum:
            print("The number can be lower than your input")
        else:
            print("The number can be higher than your input or \n")
    elif counter > 5:
        isContinue = False
    guessList.append(str(guessNum))
    keyCon = input("\nPress enter to continue or \nType \"guit\" or \"exit\" to end the program: ")
    if keyCon == "quit" or keyCon == "exit":
        isContinue = False

    print("\n")


