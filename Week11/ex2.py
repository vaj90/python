file = "myfile.txt"
with open(file, 'r') as my_file:
    print("First line is: ", my_file.readline())
    print("Second line is: ", my_file.readline())
    print("Third line is: ", my_file.readline())
    print("4th does not exists: ", my_file.readline())

print("\n")
with open(file, 'r') as my_file:
    while True:
        line = my_file.readline()
        if len(line) > 0:
            print(line, end="")
        else:
            break

print("\n")
filestream = open(file, 'r')
while True:
    line = filestream.readline()
    if len(line) > 0:
        print(line, end="")
    else:
        break

print("\n")