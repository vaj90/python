numlist = [5, 15, 84, 3, 14, 2, 8, 10, 14, 25]
numlist.sort(reverse=True)
print(numlist)
x = 1
print(x)
print(2**4)




list1 = [1, 2, 3, 4, 5]
list2 = list1
list2[0]=0
print("list1=", list1) #This will print list 1

a=2
b=5
c=3

print((b//a)**c)
print((a+b/c)*c)

def myFunction(value):
    value = value ** 2
    return value
value1 = 10
value2 = myFunction(value1)
print(value1)
print(value2)


count = 1
def doThis():
  global count
  for i in (1,2,3):
    count+=1
doThis()
print(count)


print(4/2)

scores = [70, 80, 90, -100]
total = 10
for score in scores:
    total += score
print(total)

count = 1
def doThis():
  count=0
  for i in (1,2,3):
    count+=1
doThis()
print(count)

print('Type \"x\" to exit')

a=True
b=False
c=False
if not a or b:
  print(1)
elif not a or not b and c:
  print(2)
elif not a or b or not b and a:
  print(3)
else:
  print(4)




quantity = input("Enter the quantity: ")
quantity = int(quantity)

quantity = int(input("Enter the quantity: "))