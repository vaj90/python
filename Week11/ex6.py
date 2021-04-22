file = "myfile.txt"
lines = ["New line Content 1\n",
         "New line Content 2\n",
         "New line Content 3\n"]
with open(file, 'w') as my_file:
    my_file.writelines(lines)

with open(file, 'r') as my_file:
    lines = my_file.readlines()
    for current_line in lines:
        print(current_line, end="")

print("\n")
lines = ["New line Content 1 - filestream\n",
         "New line Content 2 - filestream\n",
         "New line Content 3 - filestream\n"]
filestream = open(file, 'a')
filestream.writelines(lines)
filestream.close()

with open(file, 'r') as my_file:
    lines = my_file.readlines()
    for current_line in lines:
        print(current_line, end="")