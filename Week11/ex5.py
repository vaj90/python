file = "myfile.txt"
line = "\n" + "This line will be appended - Allan John"
with open(file, 'a') as my_file:
    my_file.write(line)

with open(file, 'r') as my_file:
    lines = my_file.readlines()
    for current_line in lines:
        print(current_line, end="")

print("\n")

line = "\n" + "This line will be appended - filesteam"
filestream = open(file, 'a')
filestream.write(line)
filestream.close()

with open(file, 'r') as my_file:
    lines = my_file.readlines()
    for current_line in lines:
        print(current_line, end="")