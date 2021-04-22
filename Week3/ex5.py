# Ask the user for a number. Depending on whether the number is odd or even,
# print out an appropriate message to the user.
number = int(input("Enter number: "))
if number % 2 == 0:
    print("the number ", number, " is even")
else:
    print("the number ", number, " is odd")

print("\n")
#Bonus:
# if the number is a multiple of 4, print out a different message
number = int(input("Enter number: "))
if number % 4 == 0:
    print("the number is multiple of 4")
elif number % 2 == 0:
    print("the number ", number, " is even")
else:
    print("the number ", number, " is odd")

print("\n")
# ask the user for 2 numbers: one to check and one number to divide by.
# If check divides evenly into num, tell that to user. if not, another message
num = int(input("Enter number: "))
check = int(input("Enter number to divide by: "))
if num % check == 0:
    print(num, "divides evenly by ", check)
else:
    print(num, "does not divide evenly by ", check)
