print()
print("Hello", "There", "From", "Multiple", "line")
print("Hello", True, 468, 98.74)

print("Hello", "There", "From", "Multiple", "line", sep='\t')
print("Hello", True, 468, 98.74, sep='\t')

print("Hello", "There", "From", "Multiple", "line", end='--END--')
print("Hello", True, 468, 98.74, end='--END--')

print()
print("Hello", "There", "From", "Multiple", "line", sep='\t', end='--END--')
print("Hello", True, 468, 98.74, sep='\t', end='--END--')

print("\n")
user_name = input("Enter your name: ")
print(user_name)

str_from_number = str(1)
str_from_boolean = str(bool)
str_from_float = str(12.35)

float_from_int = float(2)
float_from_str = float("56.78")
float_from_boolean = float(False)

int_from_boolean = int(False)
int_from_float = int(123.45)
int_from_str = int("123")

#round()
print(round(123.45))
print(round(123.45, 1))

#len()
print(len("Allan John"))
