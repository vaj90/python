print("Task 1 and Task 5")
# Create an empty list
# Ask the user for any input 5 times
# Only add the input to the list if it does NOT already exist
list = []
i = 0
while i < 5:
    dataInput = input("Enter anything: ")
    if dataInput not in list:
        list.append(dataInput)
        i += 1
print(list)

print("\nTask 2")
# Write 6 boolean expressions using six relational operators
num1 = 1
num2 = 50

# < : less than
result = num1 < num2
print(result)

# <= : less than or equal to
result = num1 <= num2
print(result)

# > : greater than
result = num1 > num2
print(result)

# >= : greater than or equal
result = num1 >= num2
print(result)

# == : equal to
result = num1 == num2
print(result)

# != : not equal to
result = num1 != num2
print(result)

print("\nTask 3")
# Write 6 boolean expressions using logical operators
var1 = 10;
var2 = 30
bool1 = True
# using and
result = var1 > 0 and var1 <= 10  # 0 < i <= 10
print(result)
result = var1 <= var2 and var1 == 20
print(result)

# using or
result = var1 == var2 or bool1
print(result)
result = (var1 == var2) == bool1 or bool1
print(result)

# using not
result = not (var1 == var2)
print(result)
result = not (var1 <= var2)
print(result)

print("\nTask 4")
# Ask user for input
# Using one IF statement block
    # Determine if input is
        # a string greater than 3 characters
        # an empty string
        # If neither of the above cases are true, display message thanking user for input.
userInput = input("Enter your inputs: ")
if len(userInput) > 3:
    print("a string greater than 3 characters")
if not userInput:
    print("an empty string")
if not (len(userInput) > 3 or not userInput):
    print("Thanks for the inputs")


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



