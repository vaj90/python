# write data into a csv file
import csv
file = 'csvfile.csv'
data = [['new', 'row', 30, 543], ['boo', 'hoo', 21, 345]]
with open(file, 'a') as my_file:
    writer = csv.writer(my_file, lineterminator='\n')
    for row in data:
        writer.writerow(row)

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