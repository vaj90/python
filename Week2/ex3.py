# logical operators
# and , or, not

mark = 75
print(mark >= 70 and mark <= 80)
mark1 = 50
mark2 = 70
mark3 = 90
print(mark1 < mark2 and mark2 < mark3)

print("\n")
color = "red"
print(color == "red" or color == "blue" or color == "green")
print(len(color)>5 or color == "red")
color = "orange"
print('a' in color or len(color)==3)

print("\n")
mark = 60
print( not mark == 60)
trueOrFalse = True
print(not trueOrFalse)
