# Task 1
# -Create a class called Window
# -It has
#       -2 public properties
#       -1 private property
#       -1 constructor that takes 3 arguments

class Window:
    _id = 0
    width = 0
    height = 0

    def __init__(self, id, width, height):
        self._id = id
        self.width = width
        self.height = height
