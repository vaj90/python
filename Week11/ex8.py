file = "myfile.txt"
with open(file, 'r') as my_file:
    my_file.readline()
    print(my_file.readline())
    position = my_file.tell()
    my_file.seek(0)
    my_file.seek(position)
    print(my_file.readline())