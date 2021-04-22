from boxclass import Box
box1 = Box('My Box',10,20,30)
box2 = Box('My Box 2',11,21)
box3 = Box('My Box 3')
box1.__del__()

print(box1.name)
print(box1.width)
print(box1.height)
print(box1.depth)

print(box1.area())
print(box1.volume())

print("\n")
print(Box.numBoxes)
print(box1.numBoxes)
Box.numBoxes = 5
print(Box.numBoxes)
print(box1.numBoxes)
print("\n")

print(Box.MyClassMethod(box1))
print(box1.MyClassMethod())