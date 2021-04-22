import platform
import os
import sys

print("Task1")
# Task 1
# - Output the Operating System name
print("System:",platform.system())

print("\nTask2")
# Task 2
# -Output the current working directory location
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
# other way of getting current working directory location
# print(os.getcwd())

print("\nTask3")
# Task 3
# -Store all the files and folders of the current working directory
# -Output each file/directory on a new line

# not sure, what exactly the store all the files and folders?
# do i need to declare a value in files and folder to store in the current directory
files = []
folders = []
for i in os.listdir(os.getcwd()):
    files.append(i)

abs_path = os.path.abspath(os.curdir)
for i in os.listdir(abs_path):
    folders.append(i)

print("Files: ", files, "\nFolders: ", folders)

print("\nTask4")
# Task 4
# -Create a sub-directory in the current working directory
path = "sub-directory"
os.makedirs(path)

print("\nTask5")
# Task 5
# -Create the following sub-directories in the current working directory
#	d1
#		d2
#			d3
# Add 2 empty text files in each directory above (6 files total). You choose the file names. They must all be unique

path = "d1/d2/d3"
os.makedirs(path)
sub_dir = ["d1","d2","d3"]
files = [
    ["d1_f1.txt","d1_f2.txt"],
    ["d2_f1.txt", "d2_f2.txt"],
    ["d3_f1.txt", "d3_f2.txt"]
]
path_dir = "";
for i in range(0,len(sub_dir)):
    path_dir += sub_dir[i] + "/"
    for f in files[i]:
        file_path = path_dir + f
        f = open(file_path, "w")
        f.close()

print("\nTask6")
# Task 6
# - Output all the files and folders of the current working directory recursively (go through sub-directories)
# HINT: use walk() method
for (r,ds,fs) in os.walk(os.getcwd()):
    print("Current Directory:", r)
    print("Files:",fs)
    print("Folders:", ds)
    print("\n")

print("\nTask7")
# Task 7
# -Ask the user for a string at least 5 characters long
# -If it is not 5+ characters, raise an exception (make sure you use try-except blocks)
# -Write a final statement
try:
    userInput = input("Enter a user input: ")
    if not (len(userInput) >= 5):
        raise Exception("Inputs must at least 5 characters")
except Exception as error:
    print("An exception occurred,", error)
finally:
    print("try-except block is finished")

print("\nTask8")
# Task 8
# -Open a file for reading
# -Attempt to write content to the file
# -Except a FileNotFound, IOError and general error
try:
    curr_dir = os.getcwd()
    file_path = curr_dir + "/d1/d1_f1.txt"
    print(file_path)
    file = open(file_path, "x")
    file.write("Hello World")
except FileNotFoundError:
    print("File path is not valid, please check the file if exists")
except IOError:
    print("Input/Output operation fails")
except:
    print("Unexpected error:", sys.exc_info())



