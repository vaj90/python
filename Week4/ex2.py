str = "Hello"
for c in str:
    print(c)

print("\n")
for c in str:
    print("The ASCII value for", c, "is", ord(c))

# splitting strings
print("The last three character are", str[2:])
print("Character 2-4 are", str[1:4])

print("Every other character is", str[0:len(str):2])
print("Every second character is", str[1:len(str):2])

# searching strings
search = "e";
if search in str:
    print(search, "was found in", str)
