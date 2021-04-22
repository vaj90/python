# working with files
# Modes: r - read, w - write, a - append, r+ - read and write,  w+ - write and read, a+ - append and read

file = "myfile.txt"
with open(file, 'r') as my_file_stream:
    print("Statements with file", str(my_file_stream))
    print("Statements outside the file")

print("\n\n")
with open(file, 'r') as my_file:
    content = my_file.read()
    print(content)
    print("Data type of <content> is: ", type(content))

print("\n\n")
filestream = open(file,'r')
content = filestream.read()
print(content)
filestream.close()
