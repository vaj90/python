# break and continue
for i in range(10, 90, 30):
    if i == 40:
        break
    print(i)

print("\n")
for i in range(10, 900, 40):
    if i == 250:
        break
    print(i)

print("\n")
for i in range(20, 0, -1):
    if i < 14:
        break
    print(i)

print("\nContinue")
for i in range(10, 90, 30):
    if i == 40:
        continue
    print(i)

print("\n")
for i in range(10, 900, 40):
    if i == 250:
        continue
    print(i)

print("\n")
for i in range(1, 26):
    if i >= 13 and i<18:
        continue
    print(i)

mySring = "hello class"
for c in mySring:
    print(c, " in uppercase is ", c.upper())

print("\n")
for c in mySring:
    print("ASCII value of", c, "is ", ord(c))

print("\n")
mySring = "MaGiCal"
for c in mySring:
    if ord(c) >= 97:
        print(c, " is lowercase")

print("\n")
mySring = "My phone number is 123-456=7890"
for c in mySring:
    if c == ' ' or c == '-':
        continue
    print(c)