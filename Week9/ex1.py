numbers = [1, 2, 3, 4, 5, 6, 7]
strings = ["hello", "world", "from", "Python"]
str_num = [1, 2, "hello", "world"]
print(numbers[0])
print(str_num[2])

emptylist =  []
emptylist.append("hello")
emptylist.insert(1, "goodbye")
emptylist.append("friend")
print(emptylist)

emptylist.insert(10, True)
print(emptylist)

strings[2] = "third index"
strings[3] = "fourth index"
numbers[1] = 77
numbers[4] = 55
print(numbers)

for item in strings:
    print(item)

for item in numbers:
    print(item)

for item in emptylist:
    print(item)

del strings

str = "abcdefg"
str_list = list(str)
print(str_list)

list1= [1, 2, 3]
list2= [4, 5, 6]
list3 = list1 + list2
print(list3)

strings = ["hello", "world", "from", "Python"]
print(strings[:2])
print(strings[1:4])
print(strings[0:6:2])

print("hello" in strings)
print("bye" in strings)
print(2 in numbers)

rep_list = [5] * 3
print(rep_list)

strings.append("last")
numbers.append(987)

strings.insert(0, "Insert first")
print(strings)
strings.insert(4, "insert fifth")
print(strings)

numbers = [1, 2, 3, 4, 5, 6, 7, 3, 3, 6]
print(numbers.count(6))

numbers.remove(6)
print(numbers)

print(numbers.index(3))
print(numbers)
numbers.reverse()
print(numbers)

print(strings)
strings.reverse()
print(strings)

numbers.sort()
print(numbers)

strings.sort()
print(strings)