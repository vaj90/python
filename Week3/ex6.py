# create a program that asks the user for a number, and then prints a list of all divisors of that number
# a divisor is a number that divides evenly into another number
# example: 13 is a divisor of 26 (26/13 has no remainder
num = int(input("Enter number: "))
arrNum = ""
i = 1
while i <= num:
    if num % i == 0:
        arrNum += str(i) + " "
    i += 1
print("the divisors of ", num, "are: ", arrNum)

# Other solution
listRange = range(1, num+1)
divisorsList = [];
for i in listRange:
    if num % i == 0:
        divisorsList.append(i)
print(divisorsList)




