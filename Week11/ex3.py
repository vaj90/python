file = "myfile.txt"
with open(file, 'r') as my_file:
    lines = my_file.readline()
    for current_line in lines:
        print(current_line, end="")

print("\n")
filestream = open(file, 'r')
lines = filestream.readline()
for current_line in lines:
    print(current_line, end="")
filestream.close()



