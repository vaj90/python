# Task 1

# -Open a file text file for writing
# -create a list of strings
# -write to the file each item of the list,  appending each item to a new line of the file

path = "list.txt"
lists = ["Allan", "Jenny", "Richard", "Juanito", "Gherick"]
with open(path, "w") as file:
    for l in lists:
        file.write(l + "\n")


# Task 2
# -Open the file in Task 1 and read its contents
# -Output each line on a new line
with open(path) as file:
    for line in file:
        line = line.replace("\n", "")
        print(line)

# Task 3
# -Open a csv file for writing
# -create a list of 3 rows that store a username, first name, last name and age (four columns)
# -write the data to csv file using the csv module.
students = [["Allan John", "Valiente", 31],
            ["Richard", "Eclipse", 32],
            ["Juanito", "Soliman", 33]]
import csv
with open("student.csv", "w") as file:
    wr = csv.writer(file)
    wr.writerows(students)

# Task 4
# -Open the file in Task 3 and read its contents
# -Output the content in a tabular format of columns and values
print()
txt = "{0:20s}{1:20s}{2:20s}"
print(txt.format("First Name","Last Name","Age"))
with open("student.csv") as file:
    reader = csv.reader(file)
    for r in reader:
        if len(r) > 0:
            print(txt.format(r[0], r[1], r[2]))