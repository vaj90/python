# writing to a file  -use the write() method
file = "myfile.txt"
line = "this is the new line - Allan John"
with open(file, 'w') as my_file:
    my_file.write(line)

with open(file, 'r') as my_file:
    lines = my_file.readline()
    for current_line in lines:
        print(current_line, end="")

print("\n")
line = "this is the new line - Allan John - filestream"
filestream = open(file, 'w')
filestream.write(line)
filestream.close()

with open(file, 'r') as my_file:
    lines = my_file.readline()
    for current_line in lines:
        print(current_line, end="")