rate1 = [
    [2, 4, 6, 8],
    [3, 6, 9, 12]
]

studentlist = [
    ["studentfirstname1", "studentlastname1"],
    ["studentfirstname2", "studentlastname2"],
    ["studentfirstname3", "studentlastname3"]
]

print("rate1 has {:d} rows and "\
      "studentlist has {:d} rows" \
      .format(len(rate1), len(studentlist)))

calories = [
    [[1, 2, 3], [4, 5, 6]],
    [[2,4,6], [8, 10, 12]],
    [[3,6,9], [12, 15, 18]],
    [[4,8, 12], [16, 20,24]]
]



print(rate1[0][3])
print(calories[2][1][1])
calories [2][1][1] = 99
print(calories)

row = 0
for i in rate1:
    row +=1
    column = 0
    for j in i:
        column += 1
        print("Row {:d}, Column {:d} value is: {:d}".format(row,column, j))


calories = [
    [[1, 2, 3], [4, 5, 6]],
    [[2,4,6], [8, 10, 12]],
    [[3,6,9], [12, 15, 18]],
    [[4,8, 12], [16, 20,24]]
]

dim1 = 0
for i in calories:
    dim1 += 1
    dim2 = 0
    for j in i:
        dim2 += 1
        dim3 =0
        for z in j:
            dim3 += 1
            print("Dimension ({:d},{:d},{:d}) value is : {:d}".format(dim1,dim2,dim3,z))