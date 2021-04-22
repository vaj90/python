import copy
def changemyarray(numArray):
    numArray[0] = 100
    numArray[1] = 200
    numArray[2] = 300


onetofive = [1, 2, 3, 4, 5]
print("Before calling changemyarray method:", onetofive)
changemyarray(onetofive)
print("After calling changemyarray method:", onetofive)

def copyandswap(numArray):
    newArray = copy.deepcopy(numArray)
    temp = newArray[0]
    newArray[0] = newArray[len(newArray)-1]
    newArray[len(newArray)-1] = temp

    return newArray

numbers3 = [1, 2, 3, 4, 5]
numbers4 = copyandswap(numbers3)
print("Numbers 3 array:",numbers3)
print("Numbers 4 array:",numbers4)

