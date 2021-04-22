# if statements
# one-way if statements
myBol = True
if myBol :
    print("success")

i = 4
if i > 2 :
   print("hello")
print("there")

# two-way if statements
i = -1
if i < 0 :
    print("number is negative")
    print("it is winter")
else :
    print("number is positive")
    print("it is spring")

# multi-way if statements
i = 4
if i == 0 :
    print("first")
elif i > 0 and i < 4 :
    print("second")
elif i > 3 and i != 5 :
    print("third")
else :
    print("fourth")

# nested if statements
hourlyEmployee = True
hours = 30
bonus = 0
yearsEmployed = 5
if hourlyEmployee == True :
    if hours > 40 :
        bonus = 500
    else :
        bonus = 100
else :
    if yearsEmployed > 10:
        bonus = 300
    else :
        bonus = 200
print()
print("hourlyEmployee: ", hourlyEmployee, "\nhours: ", hours,
      "\nbonus: ", bonus)

number = int(input("Enter number: "))
if number > 0 :
    print("number is greater than 0")
elif number == 0 :
    print("number is equal to 0")
else :
    print("number is less than 0")

print("\n")
# compacting if statements
examScore = 90
grade = 'A' if examScore > 89 else 'C'
print(grade)

timeAtSite = 3.5
charges = 100.00 if timeAtSite < 2.00 else timeAtSite * 50.00
print(charges)

# order of operators
# 1. **
# 2. * ? // %
# 3. + -
# 4. < > <= >=
# 5. == !=
# 6. NOT
# 7. AND
# 8. OR

val1 = 10
val2 = 20
val3 = 30
val4 = 40
val5 = 50
val6 = 60

if val1 > val2 or val3 == 10 and val4 + 5 < val5 :
    print("the expression is True")
else :
    print("the expression is True")
