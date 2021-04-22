file = "myfile.txt"
chars_to_skip = 4
with open(file, 'r') as my_file:
    my_file.seek(chars_to_skip)
    print("The 5th Character is ", my_file.read()[0])

chars_to_skip = 6
filestream = open(file, 'r')
filestream.seek(chars_to_skip)
print("The 7th Character is ", filestream.read()[0])
filestream.close()


with open(file,'r') as my_file:
    my_file.seek(0)
filestream = open(file, 'r')
filestream.seek(0)
filestream.close()