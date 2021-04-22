# relational operators and tests
# > , < , >= , <=
num1 = 10
num2 = 20
num3 = 30
c1 = 'T'
c2 = 'W'

print(num1 > 10)
print(num1 > num2)
print(num1 <= 20)
print(num1 >= 13)

print("\n")
print(c1 <= 'C')
print(c1 >= 'R')
print(c1 > c2)

print("\n")
print(c1 > 'T')
print(c1 >= 'X')
print(c2 > c1)

print("\n")
print(num1 < 20)
print(num2 > num1)
print(num2 >= 10)
print(num2 <= 15)

print("\n")
print(num1 + num2 > num3)
print(num1 - num2 < num3)
print(num2 / num3 < num1)
print(num2 * num3 < num3)