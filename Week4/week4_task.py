# Task 1
# -Create a dictionary of 3 items
# -GET one of the keys
# -Remove one of the keys
# -output the dictionary
dict = {
    "id": 101285226,
    "name": "allan john valiente",
    "course": "t127"
}
dict.pop("id",None)
print(dict)
0
print("\n")
# Task 2
# -Ask the user for an input
# -Output the ASCII values for each character of the input
# -Output the sum of the ASCII values for each character of the input
inp = input("Enter user input: ")
for c in inp:
    print("The ASCII value for", c, "is", ord(c))

sum = 0
for c in inp:
    sum += ord(c)
print("the sum of the ASCII values for each character is", sum)

print("\n")
# Task 3
# -Ask the user for a number
# -Determine if number is a digit
# 	If so, output the character that ASCII value represents
# 	If not, output an error message
inp = input("Enter a number: ")
if inp.isdigit():
    for c in inp:
        print("The ASCII value for", c, "is", ord(c))
else:
    print("user input is not a number")

print("\n")
# Task 4
# -Ask the user for an input
# -Determine if the input is a valid title
# 	If so, output a success message
# 	If not, transform the input into a title and output it
inp = input("Enter user input: ")
if inp.istitle():
    print("user input is a valid title")
else:
    print(inp.title())

print("\n")
# Task 5
# -Ask user for input
# -Ask user for character
# -Output a YES or NO value if the character is found in the input
# -Output a position of where the character is found
inp = input("Enter user input: ")
chr = input("Enter a character: ")
index = 0
if inp.find(chr):
    print("Yes")
    index = inp.index(chr)
else:
    print("NO")
print("The position of \"" + chr + "\" character found is", index)