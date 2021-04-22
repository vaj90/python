# string functions
str = "abc def fed cba"
new_str = str.split()
print(new_str)

new_str = str.split(' ', 2)
print(new_str)

# title() - transform the first character of each word into a capital letter
str = "a brave new world"
new_str = str.title()
print(new_str)

# endswith(), startswith()- determine if a string start/ends with a string
str = "hello"
ans1 = str.endswith("o")
ans2 = str.endswith("o", 1, 3)
print(ans1)
print(ans2)
ans3 = str.startswith("H")
ans4 = str.startswith("h", 1, 3)
print(ans3)
print(ans4)

# find() - return a index position of argument
str = "Hello"
pos1 = str.find("e");
pos2 = str.find("e", 2, 4);
print(pos1)
print(pos2)

# lower(), upper()
str = "Hello"
str_lower = str.lower();
print(str_lower)
str_upper = str.upper();
print(str_upper)

# islower(), isupper(), istitle
str = "Hello"
print(str.islower())
print(str.isupper())
print(str.istitle())

# lstrip(), rstrip(), strip()
str = "   GoodBye   "
print(str.lstrip())
print(str.rstrip())
print(str.strip())

print("\n")
# isalpha() - determine string contains letters
str = "Hallo123"
print(str.isalpha())
str = "Hello"
print(str.isalpha())

print("\n")
# isdigit() - determine string contains only numbers
str = "234"
print(str.isdigit())
str = "-234"
print(str.isdigit())
str = "234.56"
print(str.isdigit())
print(str.isdecimal())

print("\n")
# isalnum() - determine string only contains aplha-numerical characters
str = "hello123"
print(str.isalnum())
str = "Hello"
print(str.isalnum())