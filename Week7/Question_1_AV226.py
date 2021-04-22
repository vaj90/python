# Allow the user to enter some inputs
userInput = input("Enter your an integer between 1 and 50: ");
# condition to check if userInput is digit or numeric (number)
if userInput.isdigit() and userInput.isnumeric():
    # declare and initialize factorial variable set to 1
    factorial = 1
    # loop that calculate the factorial or a product for 1 to the value of userinput
    for i in range(1, int(userInput) + 1):
        factorial = factorial * i
    #display
    print("The factorial of", userInput, "is", factorial)