fruits = {
    'red': 'apple',
    'blue': 'berries',
    'orange': 'mandarines'
}

colours = {
    'fav': 'red',
    'least': 'blue',
    False: 0,
    'soso': 'yellow'
}

cars = {
    'truck': 'F-50',
    'compact': 'civic',
    12: 'twelve'
}

print(colours.keys())
print(list(colours.keys()))
print(list(fruits.keys()))

print("\n")
print(colours.values())
print(list(colours.values()))
print(list(fruits.values()))

print("\n")
print(fruits.items())
print(list(fruits.items()))

print("\n")
d1 = dict.fromkeys([2, 4])
print(d1)
d2 = dict.fromkeys([7, 8, "goodbye"])
print(d2)

print("\n")
print(fruits.get('red'))
print(cars.get('van'))
print(fruits.get('white', 'grapes'))
print(fruits)

print("\n")
colours.update(fruits)
print(colours)

print("\n")
print(cars.setdefault('van'))
print(cars.setdefault('suv'))
print(cars)

cars.clear()
print(cars)