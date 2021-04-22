# write data into a csv file
import csv
try:
    file = "student.csv"
    listData = []
    strLine = "+----------------------+----------------------+--------+"
    strHeader = ["Student First Name", "Student Last Name", "Grade"]
    strFormat = "| {0:20s} | {1:20s} | {2:6s} |"

    def readData():
        global listData
        listData = []
        filestream = open(file, 'r')
        reader = csv.reader(filestream)
        for row in reader:
            listData.append(row)


    def displayOutput():
        global listData
        global strFormat
        grade = 0
        cnt = 0
        print(strLine)
        print(strFormat.format(strHeader[0], strHeader[1], str(strHeader[2])))
        print(strLine)
        for item in listData:
            cnt += 1
            grade += int(item[2])
            strLet = strFormat.format(item[0], item[1], str(item[2]))
            print(strLet)
            print(strLine)
        gradeAve = grade / cnt
        try:
            print("Grade average {0}".format(int(gradeAve)))
        except:
            print("Grade average 0")
        print("\n")

    def updateData(students):
        with open(file, 'w') as my_file:
            writer = csv.writer(my_file, lineterminator='\n')
            writer.writerows(students)

    def addStudent():
        try:
            global listData
            studentName = input("Enter student name: ")
            grade = int(input("Enter your grade: "))
            firstName, lastName = studentName.split(' ', 1)
            item = [firstName, lastName, str(grade)]
            listData.append(item)
            updateData(listData)
        except IOError:
            print("Input/Output operation fails")
        except:
            print("Invalid input, Error occured in student name or grade")

    readData();
    displayOutput()
    addStudent()
    displayOutput()

except FileNotFoundError:
    print("File path is not valid, please check the file if exists")
except IOError:
    print("Input/Output operation fails")