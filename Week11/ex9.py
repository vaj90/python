# work with csv files
import csv
file = 'csvfile.csv'
with open(file, 'r') as my_file:
    reader = csv.reader(my_file)
    rowCount = 0
    for row in reader:
        rowCount += 1
        print("Row", rowCount, "Data:")
        columnCount = 0
        for column in row:
            columnCount += 1
            print("Row", rowCount, "Column", columnCount, "=", column)

print("\n\n")
filestream = open(file, 'r')
reader = csv.reader(filestream)
rowCount = 0
for row in reader:
    rowCount += 1
    print("Row", rowCount, "Data:")
    columnCount = 0
    for column in row:
        columnCount += 1
        print("Row", rowCount, "Column", columnCount, "=", column)

filestream.close()