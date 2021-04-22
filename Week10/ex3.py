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

if "fav" in colours.keys():
    print("fav is found")
else:
    print("fav is not found")

if "red" in colours.values():
    print("red is found")
else:
    print("red is not found")