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

print(len(fruits))
print(len(colours))
print(len(cars))


fruits['red'] = 'strawberries'
colours['fav'] = 'green'
cars['compact'] = 'accent'

print(fruits)
del fruits['orange']
print(fruits)

print("\n")
print(colours)
print(cars)

for key in fruits:
    print("key is", key)

for key in fruits.keys():
    print("key is", key)

for value in fruits:
    print("value is", value)

for value in fruits.values():
    print("value is", value)

for key, value in fruits.items():
    print("key is {:s}, value is {:s}".format(key, value))

